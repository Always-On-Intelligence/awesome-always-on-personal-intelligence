#!/usr/bin/env python3
"""Validate the reading list and generate README.md (stdlib only).

data/sections.json follows the survey's chapters and titles; every entry names the section where
the survey discusses it, and optionally one of the survey's groupings inside that section, which
is shown as a short tag. Each list runs from the newest work to the oldest.
"""

import argparse
from datetime import date
import html
import json
from pathlib import Path
import re
import sys
from urllib.parse import quote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
CHANNELS = ["S→A", "S→M", "M→A", "A→S", "M→S", "A→M"]
TAGS = set(CHANNELS) | {f"L{i}" for i in range(6)} | {"Product"}
LINK_LABELS = ["paper", "blog", "docs", "website", "project", "code", "data"]
PRODUCT_SECTIONS = {"products-wearable", "products-digital", "products-physical", "products-devices"}
TOOL_GROUPS = {"memory": "Memory", "runtime": "Runtime", "integrations": "Integrations"}
ROMAN = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
# Badge colours from the survey's palette: channels by the module that receives them (rose = Memory,
# blue = Action, sage = Sensing), levels from grey to gold (L3 to L5 are the always-on levels).
CHANNEL_COLORS = {"S→M": "9d675d", "A→M": "9d675d", "S→A": "556b88", "M→A": "556b88", "M→S": "607a6d", "A→S": "607a6d"}
LEVEL_COLORS = {"L0": "9a9a9a", "L1": "868e98", "L2": "6b7785", "L3": "b8924a", "L4": "9a7430", "L5": "6b4e17"}
GROUP_COLORS = {"sec-3": "8fa399", "sec-4": "bb9188", "sec-5": "8a9bb3", "sec-6": "a39a87"}
VENUE_COLORS = {"arXiv": "a1574a", "Preprints": "8c8c8c", "Book": "8c8c8c"}
VENUE_DEFAULT, PRODUCT_COLOR, NEUTRAL = "355774", "8a6400", "8c8c8c"
NO_LEVEL = "d0d0d0"  # products the survey gives no level: lighter than the L0 to L2 greys, with dark text


class Badges:
    """Coloured shields.io badges, written as reference-style images so each badge URL appears once."""

    def __init__(self):
        self.refs = {}

    @staticmethod
    def url(text, color):
        label = text.replace("-", "--").replace("_", "__").replace(" ", "_")
        return f"https://img.shields.io/badge/{quote(label, safe='')}-{color}?style=flat-square"

    @staticmethod
    def color(tag):
        return CHANNEL_COLORS.get(tag) or LEVEL_COLORS.get(tag) or (PRODUCT_COLOR if tag == "Product" else NEUTRAL)

    def __call__(self, text, color):
        key = "b-" + re.sub(r"[^a-z0-9]+", "-", f"{text} {color}".lower().replace("→", " to ")).strip("-")
        if key not in self.refs:
            self.refs[key] = self.url(text, color)
        return f"![{md(text)}][{key}]"

    def tag(self, tag):
        return self(tag, self.color(tag))

    def img(self, text, color=None):
        """A badge as an HTML image, for HTML tables, where Markdown references are not read. It sits at the top of its
        line, so a line of badges is exactly as tall as a line of text."""
        return f'<img src="{self.url(text, color or self.color(text))}" alt="{html.escape(text)}" align="top"/>'

    def definitions(self):
        return [f"[{key}]: {url}" for key, url in sorted(self.refs.items())]


def is_single_line(value):
    return isinstance(value, str) and bool(value.strip()) and not any(c in value for c in "\n\r")


def normalized(url):
    return re.sub(r"v\d+$", "", url.rstrip("/").replace("/pdf/", "/abs/").removesuffix(".pdf")).lower()


def load_sections():
    sections = json.loads((ROOT / "data" / "sections.json").read_text(encoding="utf-8"))
    by_id = {}
    for node in sections:
        name = node.get("id", "<missing id>")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or name in by_id:
            raise ValueError(f"section {name}: invalid or duplicate id")
        if node.get("level") not in (2, 3, 4) or not is_single_line(node.get("title")):
            raise ValueError(f"section {name}: needs a title and level 2, 3, or 4")
        if node["level"] == 2 and not (is_single_line(node.get("icon")) and is_single_line(node.get("description"))):
            raise ValueError(f"section {name}: a top-level section needs an icon and a description")
        if node["level"] > 2 and by_id.get(node.get("parent"), {}).get("level") != node["level"] - 1:
            raise ValueError(f"section {name}: parent must be the enclosing section")
        if node.get("sort", "year") not in ("year", "level"):
            raise ValueError(f"section {name}: sort must be year or level")
        groups = node.get("groups", [])
        if not all(isinstance(g, dict) and is_single_line(g.get("name")) and is_single_line(g.get("tag")) for g in groups):
            raise ValueError(f"section {name}: groups need a name and a tag")
        by_id[name] = node
    return sections, by_id


def check_links(name, links):
    if not isinstance(links, dict) or not links:
        raise ValueError(f"{name}: missing links")
    for label, url in links.items():
        if label not in LINK_LABELS:
            raise ValueError(f"{name}: unknown link type {label}")
        parsed = urlsplit(url) if isinstance(url, str) else None
        if not parsed or parsed.scheme != "https" or not parsed.netloc or not url.isascii() or any(c in url for c in '<>"') or any(c.isspace() for c in url):
            raise ValueError(f"{name}: invalid HTTPS URL {url}")


def load_entries(by_id):
    entries = []
    seen_ids = set()
    seen_urls = set()
    for filename in ("research.json", "products.json", "tools.json"):
        data = json.loads((ROOT / "data" / filename).read_text(encoding="utf-8"))
        if not isinstance(data, list) or not data:
            raise ValueError(f"{filename}: expected a nonempty array")
        for entry in data:
            name = entry.get("id", "<missing id>") if isinstance(entry, dict) else "<not an object>"
            if not isinstance(entry, dict) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or name in seen_ids:
                raise ValueError(f"{name}: invalid or duplicate id")
            seen_ids.add(name)
            if not is_single_line(entry.get("title")):
                raise ValueError(f"{name}: invalid title")
            node = by_id.get(entry.get("section"))
            if not node:
                raise ValueError(f"{name}: unknown section {entry.get('section')}")
            check_links(name, entry.get("links"))
            if filename == "research.json":
                if entry["section"].startswith("products"):
                    raise ValueError(f"{name}: products and tools belong in products.json and tools.json")
                if "group" in entry and entry["group"] not in [g["name"] for g in node.get("groups", [])]:
                    raise ValueError(f"{name}: group {entry['group']!r} is not listed for section {node['id']}")
                year = entry.get("year")
                if type(year) is not int or not 1900 <= year <= date.today().year:
                    raise ValueError(f"{name}: invalid year")
                if not is_single_line(entry.get("venue")) or "`" in entry["venue"]:
                    raise ValueError(f"{name}: missing or invalid venue")
                links = entry["links"]
                primary = next((links[k] for k in ("paper", "blog", "docs", "website", "code") if k in links), None)
                if not primary:
                    raise ValueError(f"{name}: needs a paper, blog, docs, website, or code link")
                if normalized(primary) in seen_urls:
                    raise ValueError(f"{name}: duplicate source; choose one home")
                seen_urls.add(normalized(primary))
                tags = entry.get("tags", [])
                if not isinstance(tags, list) or len(tags) > 4 or any(t not in TAGS for t in tags):
                    raise ValueError(f"{name}: tags must be channels ({', '.join(CHANNELS)}), levels L0 to L5, or Product")
            else:
                checked = entry.get("checked", "")
                if not isinstance(checked, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", checked) or date.fromisoformat(checked) > date.today():
                    raise ValueError(f"{name}: checked must be a past YYYY-MM-DD date")
                if filename == "products.json":
                    # One line per product: its organization and its official page, never a blog post.
                    if entry["section"] not in PRODUCT_SECTIONS or not is_single_line(entry.get("org")) or "`" in entry["org"]:
                        raise ValueError(f"{name}: products need an org and one of {', '.join(sorted(PRODUCT_SECTIONS))}")
                    if list(entry["links"]) != ["website"]:
                        raise ValueError(f"{name}: a product links only its official website page")
                    tags = entry.get("tags", [])
                    if not isinstance(tags, list) or len(tags) > 3 or any(t not in TAGS for t in tags):
                        raise ValueError(f"{name}: invalid product tags")
                    if not isinstance(entry.get("sources", []), list) or not all(is_single_line(s) for s in entry.get("sources", [])):
                        raise ValueError(f"{name}: sources must list survey citation keys")
                    if "logo" in entry and not re.fullmatch(r"[a-z0-9.-]+\.[a-z]{2,}", str(entry["logo"])):
                        raise ValueError(f"{name}: logo must be a domain such as claude.com")
                    if not is_single_line(entry.get("series")):
                        raise ValueError(f"{name}: products need a series (the product line a feature belongs to)")
                    for update in entry.get("updates", []):
                        if not (re.fullmatch(r"\d{4}-\d{2}", str(update.get("date", ""))) and is_single_line(update.get("label"))):
                            raise ValueError(f"{name}: an update needs a YYYY-MM date and a short label")
                        check_links(name, {"website": update.get("url")})
                    entry = dict(entry, label=entry["org"], order=0)
                else:
                    if entry["section"] != "products-tools" or entry.get("group") not in TOOL_GROUPS:
                        raise ValueError(f"{name}: tools use section products-tools and a group in {', '.join(TOOL_GROUPS)}")
                    if not is_single_line(entry.get("description")):
                        raise ValueError(f"{name}: invalid description")
                    entry = dict(entry, label=TOOL_GROUPS[entry["group"]], order=list(TOOL_GROUPS).index(entry["group"]))
            entries.append(entry)
    return entries


def md(value):
    value = html.escape(str(value), quote=False)
    for char in "|[]\\*_`":
        value = value.replace(char, f"&#{ord(char)};")
    return value


def markdown_url(url):
    for char in "()|\\`<>":
        url = url.replace(char, f"%{ord(char):02X}")
    return url


def resource_links(links):
    return " ".join(f"[[{label}]({markdown_url(links[label])})]" for label in LINK_LABELS if label in links)


def render_entry(entry, group_tags, badge, group_color=NEUTRAL):
    if "org" in entry:
        tags = "".join(f" {badge.tag(tag)}" for tag in entry.get("tags", []))
        title = md(entry["title"])
        return f"- **`{entry['label']}`** {title}. {resource_links(entry['links'])}{tags}"
    if "label" in entry:
        description = entry["description"]
        if len(description) > 1 and description[1].islower():
            description = description[0].lower() + description[1:]
        return f"- **`{entry['label']}`** {md(entry['title'])}: {md(description)} {resource_links(entry['links'])}"
    title = md(entry["title"])
    title = title if title[-1] in ".?!" else title + "."
    tags = [badge(group_tags[entry["group"]], group_color)] if entry.get("group") in group_tags else []
    tags = "".join(f" {t}" for t in tags + [badge.tag(tag) for tag in entry.get("tags", [])])
    venue = badge(f"{entry['venue']} {entry['year']}", VENUE_COLORS.get(entry["venue"], VENUE_DEFAULT))
    return f"- {venue} {title} {resource_links(entry['links'])}{tags}"


def logo(entry):
    """The site icon of a product line, from its official page's domain (or the entry's `logo` domain)."""
    host = entry.get("logo") or urlsplit(entry["links"]["website"]).netloc.lower().removeprefix("www.")
    labels = host.split(".")
    keep = 3 if len(labels) > 2 and ".".join(labels[-2:]) in ("com.cn", "co.uk", "com.au", "co.jp", "com.sg") else 2
    domain = ".".join(labels[-keep:])
    return f'<img src="https://www.google.com/s2/favicons?domain={domain}&sz=64" width="16" height="16" alt=""/> '


def product_name(entry):
    """A feature's name with its product line in front, unless the feature's name already starts with it."""
    title, series = entry["title"], entry["series"]
    if re.match(re.escape(series) + r"(\W|$)", title, re.IGNORECASE):
        return title
    return f"{series} {title}"


def product_table(rows, badge):
    """One table per domain with a row per company, so that a company's products share a row colour. Each product or
    feature has its own line with its link, and the last column gives each one its level and channels on the same line."""
    icons, companies = {}, {}
    for e in sorted(rows, key=lambda e: (e["series"].casefold(), e["title"].casefold())):
        icons.setdefault(e["series"], logo(e))
        companies.setdefault(e["org"].casefold(), []).append(e)
    rated = any(t in LEVEL_COLORS or t in CHANNEL_COLORS for e in rows for t in e.get("tags", []))
    head = "<th>Product</th><th>Company</th>" + ("<th>Level and channels</th>" if rated else "")
    body = []
    for group in sorted(companies.values(), key=lambda g: product_name(g[0]).casefold()):
        names, levels = [], []
        for e in group:
            names.append(f'{icons[e["series"]]}<b><a href="{html.escape(e["links"]["website"])}">{md(product_name(e))}</a></b>')
            tags = sorted((t for t in e.get("tags", []) if t in LEVEL_COLORS or t in CHANNEL_COLORS), key=lambda t: t not in LEVEL_COLORS)
            if not any(t in LEVEL_COLORS for t in tags):  # so that a line without a level does not seem to share the one above
                tags.insert(0, None)
            levels.append(" ".join(badge.img(t) if t else badge.img("No level", NO_LEVEL) for t in tags))
            for u in sorted(e.get("updates", []), key=lambda u: u["date"], reverse=True)[:3]:
                names.append(f'<sub>{u["date"].replace("-", "/")} · <a href="{html.escape(u["url"])}">{md(u["label"])}</a></sub>')
                levels.append("<sub>&nbsp;</sub>")  # keeps each feature's badges on the line of its name
        cells = f'<td nowrap valign="top">{"<br/>".join(names)}</td><td>{md(group[0]["org"])}</td>'
        if rated:
            cells += f'<td nowrap valign="top">{"<br/>".join(levels)}</td>'
        body.append(f"<tr>{cells}</tr>")
    return ["<table>", f"<thead><tr>{head}</tr></thead>", "<tbody>", *body, "</tbody>", "</table>"]


def order(entry, by_level=False):
    """Newest first; in the systems lists, highest loop-closure level first, then newest."""
    if "label" in entry:
        return (entry["order"], entry["title"].casefold())
    if by_level:
        level = max((int(t[1]) for t in entry.get("tags", []) if re.fullmatch(r"L[0-5]", t)), default=-1)
        return (-level, -entry["year"], entry["title"].casefold())
    return (-entry["year"], entry["title"].casefold())


def heading(node):
    return node["title"]


HALO_REPO = "https://github.com/Always-On-Intelligence/HALO"


def card(href, icon, title, lines, full=None, note=None):
    """One cell of the contents grid: icon, title, an optional small note, then lines of links."""
    href = href if href.startswith("https://") else f"#{href}"
    tip = f' title="{html.escape(full)}"' if full else ""
    body = (f"<br/><sub>{note}</sub>" if note else "") + "".join(f"<br/>{line}" for line in lines)
    return (f'<td align="center" valign="top" width="33%"><a href="{href}"{tip}><img src="assets/icons/{icon}.svg" width="40" alt=""/></a>'
            f'<br/><a href="{href}"{tip}><b>{html.escape(title)}</b></a>{body}</td>')


def contents(tops, children, count):
    """The table of contents as a grid of chapter cards, with Related Surveys, Contributing and Citation below."""
    def links(node):
        rows, width = [], 0
        for c in (c for c in children.get(node["id"], []) if count(c)):
            label = c.get("short", c["title"])
            if not rows or width + 3 + len(label) > 34:  # keep each line short enough not to wrap inside a card
                rows.append([])
                width = -3
            rows[-1].append(f'<a href="#{c["id"]}">{html.escape(label)}</a>')
            width += 3 + len(label)
        return "<br/>".join(" · ".join(r) for r in rows)

    def numbered(node):
        """Chapters carry the survey's section number in Roman numerals, as in Figure 1. Other cards have none."""
        m = re.fullmatch(r"sec-(\d+)", node["id"])
        title = node.get("short", node["title"])
        return f"{ROMAN[int(m.group(1))]}. {title}" if m else title

    cells = [card("foundations", "foundations", f"{ROMAN[2]}. Foundations", [], "Overview and Foundations", note="Definitions · Channels · Levels")]
    for node in tops:
        cells.append(card(node["id"], node["icon"], numbered(node), [links(node)] if links(node) else [], node["title"]))
        if node["id"] == "sec-6" and not any(n["id"] == "sec-7" for n in tops):
            # HALO lists no works of its own here, so its card leads to the HALO code instead
            cells.append(card(HALO_REPO, "evaluation", f"{ROMAN[7]}. HALO", [f'<a href="{HALO_REPO}">Code</a>'],
                              "HALO: Harness for Always-On Loop Oversight", note="Read mode · Run mode"))
    cells += ['<td width="33%"></td>'] * (-len(cells) % 3)
    rows = ["<tr>" + "".join(cells[i:i + 3]) + "</tr>" for i in range(0, len(cells), 3)]
    return ['<div align="center">', "", '<table align="center">', *rows, "</table>", "",
            '<p align="center"><a href="#contributing">Contributing</a> · <a href="#citation">Citation</a></p>', "", "</div>"]


def build(sections, entries):
    children = {}
    for node in sections:
        children.setdefault(node.get("parent"), []).append(node)
    direct = {}
    for entry in entries:
        direct.setdefault(entry["section"], []).append(entry)

    def count(node):
        return len(direct.get(node["id"], [])) + sum(count(c) for c in children.get(node["id"], []))

    works = sum(1 for e in entries if "label" not in e)
    products = sum(1 for e in entries if "org" in e)
    papers = sum(1 for e in entries if "label" not in e and "paper" in e["links"])
    tops = [n for n in sections if n["level"] == 2 and count(n)]
    toc = contents(tops, children, count)
    intro = (ROOT / "docs" / "readme-intro.md").read_text(encoding="utf-8").rstrip()
    intro = intro.replace("{{PAPER_COUNT}}", str(papers)).replace("{{WORK_COUNT}}", str(works)).replace("{{PRODUCT_COUNT}}", str(products)).replace("{{TOC}}", "\n".join(toc))
    parts = ["<!-- Generated by scripts/build_readme.py. Edit data/*.json or docs/readme-*.md, then regenerate. -->", "", intro, ""]
    badge = Badges()
    top_of = {}
    for node in sections:
        top_of[node["id"]] = top_of.get(node.get("parent"), node["id"])

    def emit(node):
        if not count(node):
            return
        level = node["level"]
        if level == 2:
            parts.append(f'---\n\n<a id="{node["id"]}"></a>\n## <img src="assets/icons/{node["icon"]}.svg" height="30" align="top" alt=""/> {heading(node)}\n\n{node["description"]}\n')
        else:
            parts.append(f'<a id="{node["id"]}"></a>\n{"#" * level} {heading(node)}\n')
        own = sorted(direct.get(node["id"], []), key=lambda e: order(e, node.get("sort") == "level"))
        if own and node["id"] in PRODUCT_SECTIONS:
            parts.extend(product_table(own, badge))
            parts.append("")
        elif own:
            group_tags = {g["name"]: g["tag"] for g in node.get("groups", [])}
            color = GROUP_COLORS.get(top_of.get(node["id"]), NEUTRAL)
            parts.extend(render_entry(e, group_tags, badge, color) for e in own)
            parts.append("")
        for child in children.get(node["id"], []):
            emit(child)

    for top in tops:
        emit(top)
    parts.append((ROOT / "docs" / "readme-footer.md").read_text(encoding="utf-8").rstrip())
    parts += ["", "<!-- badge images -->", *badge.definitions()]
    return "\n".join(parts) + "\n"


def validate_local_links(content):
    anchors = set(re.findall(r'<a id="([^"]+)"', content))
    content = re.sub(r"```.*?```", "", content, flags=re.S)
    for target in re.findall(r"\]\(([^\s)]+)\)", content) + re.findall(r'<a href="([^"]+)"', content):
        if target.startswith("#") and target[1:] not in anchors:
            raise ValueError(f"Broken anchor: {target}")
        if not target.startswith(("https://", "#", "mailto:")) and not (ROOT / target.split("#")[0]).exists():
            raise ValueError(f"Missing local link: {target}")
    for target in re.findall(r'<img[^>]+src="([^"]+)"', content):
        if not target.startswith("https://") and not (ROOT / target).is_file():
            raise ValueError(f"Missing image: {target}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validate the data and require README.md to match the generated output")
    args = parser.parse_args()
    sections, by_id = load_sections()
    entries = load_entries(by_id)
    content = build(sections, entries)
    validate_local_links(content)
    output = ROOT / "README.md"
    if args.check:
        if output.read_text(encoding="utf-8") != content:
            raise ValueError("README.md is stale. Run python3 scripts/build_readme.py")
        print(f"OK: {len(entries)} entries in {len(sections)} sections; schema, unique sources, local links, images, anchors, and generated README checked.")
    else:
        output.write_text(content, encoding="utf-8")
        print(f"Generated README.md with {len(entries)} entries.")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, TypeError, FileNotFoundError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)
