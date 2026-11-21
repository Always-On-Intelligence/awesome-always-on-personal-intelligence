#!/usr/bin/env python3
"""Validate the reading list and generate README.md (stdlib only).

data/sections.json follows the survey's chapters and titles; every entry names the section where
the survey discusses it, and one of the survey's own divisions of that section when the section
lists them (a paragraph of its text, a group of its benchmark table, an open problem). A section
whose works fall into two or more divisions shows one short list per division, in the paper's
order, under its own heading. Each list runs from the newest work to the oldest.
"""

import argparse
from datetime import date
import html
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
CHANNELS = ["S→A", "S→M", "M→A", "A→S", "M→S", "A→M"]
TAGS = set(CHANNELS) | {f"L{i}" for i in range(6)} | {"Product"}
LINK_LABELS = ["paper", "blog", "docs", "website", "project", "code", "data"]
PRODUCT_SECTIONS = {"products-wearable", "products-digital", "products-physical", "products-devices"}
ROMAN = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
# Badges are small SVG pills kept in assets/badges and generated here, in the survey's palette. A tinted pill has a
# light fill and dark text, and swaps to a dark fill and light text under a dark colour scheme; an outline pill uses
# one mid grey that reads on both. Channels take the tint of the module that receives them (rose = Memory,
# blue = Action, sage = Sensing). Levels are grey up to L2 and gold with a dot from L3, the first always-on level.
BADGE_DIR = "assets/badges"
#        light fill, light text, dark fill, dark text
TINTS = {"gold": ("F5ECD9", "6B4E17", "3D2F12", "E8CF98"), "grey": ("EEF0F2", "57606A", "2A313C", "C3CAD3"),
         "rose": ("F4E7E4", "7D4A41", "3E2925", "E5BDB5"), "blue": ("E6ECF3", "3D5370", "243044", "B9C9E0"),
         "sage": ("E5EDE8", "44604F", "24352B", "B7D0C1")}
OUTLINE, OUTLINE_MUTED, PRIMARY = "6E7781", "8C959F", "8B692E"
CHANNEL_TINTS = {"S→M": "rose", "A→M": "rose", "S→A": "blue", "M→A": "blue", "M→S": "sage", "A→S": "sage"}
LEVEL_DOTS = {"L3": ("B8924A", "9A7430"), "L4": ("9A7430", "C9A45C"), "L5": ("6B4E17", "F2DCA6")}  # light, dark
LEVELS = [f"L{i}" for i in range(6)]
GROUP_TINTS = {"sec-3": "sage", "sec-4": "rose", "sec-5": "blue", "sec-6": "grey"}
QUIET_VENUES = {"arXiv", "Preprints", "Book"}  # outline pills; every other venue gets the gold tint
# Links other than the one the venue badge opens, as outline pills after the title, in this order
LINK_BADGES = {"code": "Code", "project": "Project", "data": "Data", "docs": "Docs", "blog": "Blog", "website": "Website"}
GITHUB_MARK = ("M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94"
               "-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07"
               "-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27s1.36.09 2 .27"
               "c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48"
               " 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8Z")
FONT = "-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans',Helvetica,Arial,sans-serif"
MAIN_LINKS = ["paper", "project", "website", "docs", "blog", "code", "data"]


def text_width(text, size, bold=False):
    """An estimate of a label's width in a system sans font. The SVG sets textLength to it, so the label fits its pill
    whatever font the reader's system supplies."""
    total = 0.0
    for c in text:
        if c in "iIl.,:;|!'j·":
            total += 0.28
        elif c in "ftr()-[] /":
            total += 0.34
        elif c in "mw":
            total += 0.84
        elif c in "MW":
            total += 0.90
        elif c == "→":
            total += 1.0
        elif c.isdigit():
            total += 0.57
        elif c.isupper() or c in "&+@%":
            total += 0.69
        else:
            total += 0.55
    return round(total * size * (1.07 if bold else 1.0), 1)


class Badges:
    """SVG pills in assets/badges. Lists use them as reference-style images, so each file is named once in the README,
    and the product tables use them as HTML images. `files` collects every badge the README needs."""

    def __init__(self):
        self.refs = {}
        self.files = {}

    @staticmethod
    def svg(text, style, dot=None, mark=False, height=18, size=11, bold=False):
        """style is a tint name, "outline", "muted" (a fainter outline) or "primary" (a solid button)."""
        pad = 8 if height == 18 else 14
        lead = (11 if dot else 0) + (15 if mark else 0)
        tw = text_width(text, size, bold)
        width = round(pad * 2 + lead + tw)
        r, mid = height / 2, pad + lead + tw / 2
        css, shapes = "", ""
        if style in TINTS:
            lf, lt, df, dt = TINTS[style]
            css = f".b{{fill:#{lf}}}.t{{fill:#{lt}}}"
            dark = f".b{{fill:#{df}}}.t{{fill:#{dt}}}"
            if dot:
                css += f".d{{fill:#{dot[0]}}}"
                dark += f".d{{fill:#{dot[1]}}}"
            css += f"@media (prefers-color-scheme:dark){{{dark}}}"
            shapes = f'<rect class="b" width="{width}" height="{height}" rx="{r:g}"/>'
        elif style == "primary":
            css = f".b{{fill:#{PRIMARY}}}.t{{fill:#FFFFFF}}"
            shapes = f'<rect class="b" width="{width}" height="{height}" rx="{r:g}"/>'
        else:
            ink = OUTLINE_MUTED if style == "muted" else OUTLINE
            css = f".t{{fill:#{ink}}}.o{{fill:none;stroke:#8C959F;stroke-opacity:.55}}"
            shapes = f'<rect class="o" x=".5" y=".5" width="{width - 1}" height="{height - 1}" rx="{r - .5:g}"/>'
        if dot:
            shapes += f'<circle class="d" cx="{pad + 3}" cy="{r:g}" r="3"/>'
        if mark:
            shapes += f'<path class="t" transform="translate({pad} {(height - 11) / 2:g}) scale(.6875)" d="{GITHUB_MARK}"/>'
        weight = ' font-weight="600"' if bold else ""
        label = html.escape(text, quote=True)
        return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{label}">'
                f"<title>{label}</title><style>{css}</style>{shapes}"
                f'<text class="t" x="{mid:g}" y="{r + size * 0.36:g}" font-family="{FONT}" font-size="{size}"{weight} text-anchor="middle" textLength="{tw:g}">{label}</text></svg>\n')

    def path(self, text, style, name=None, **options):
        """Registers a badge file and returns its path."""
        name = name or style + "-" + re.sub(r"[^a-z0-9]+", "-", text.lower().replace("→", " to ")).strip("-")
        self.files[f"{name}.svg"] = self.svg(text, style, **options)
        return f"{BADGE_DIR}/{name}.svg"

    def __call__(self, text, style, **options):
        path = self.path(text, style, **options)
        key = "b-" + Path(path).stem
        self.refs[key] = path
        return f"![{md(text)}][{key}]"

    @staticmethod
    def tag_style(tag):
        if tag in CHANNEL_TINTS:
            return CHANNEL_TINTS[tag], {}
        if tag in LEVEL_DOTS:
            return "gold", {"dot": LEVEL_DOTS[tag]}
        return "grey", {}

    def tag(self, tag):
        style, options = self.tag_style(tag)
        return self(tag, style, **options)

    def venue(self, venue, year):
        return self(f"{venue} {year}", "outline" if venue in QUIET_VENUES else "gold")

    def img(self, text, style=None):
        """A badge as an HTML image, for HTML tables, where Markdown references are not read. It sits at the top of its
        line, so a line of badges is exactly as tall as a line of text."""
        options = {}
        if style is None:
            style, options = self.tag_style(text)
        return f'<img src="{self.path(text, style, **options)}" height="18" alt="{html.escape(text)}" align="top"/>'

    def definitions(self):
        return [f"[{key}]: {path}" for key, path in sorted(self.refs.items())]


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
        if "card_of" in node and (node["level"] != 2 or not is_single_line(node["card_of"])):
            raise ValueError(f"section {name}: card_of names a top-level section, on a top-level section only")
        if node.get("sort", "year") not in ("year", "level"):
            raise ValueError(f"section {name}: sort must be year or level")
        groups = node.get("groups", [])
        if not all(isinstance(g, dict) and is_single_line(g.get("name")) and is_single_line(g.get("tag")) for g in groups):
            raise ValueError(f"section {name}: groups need a name and a tag")
        by_id[name] = node
    for node in sections:
        host = by_id.get(node.get("card_of", ""))
        if "card_of" in node and (not host or host["level"] != 2 or "card_of" in host):
            raise ValueError(f"section {node['id']}: card_of must name a top-level section that has its own card")
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
    for filename in ("research.json", "products.json"):
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
                    raise ValueError(f"{name}: products belong in products.json")
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


def link_badges(links, badge, skip=None):
    """Each link as a small outline pill, with the GitHub mark on code hosted there."""
    out = []
    for label, text in LINK_BADGES.items():
        if label in links and label != skip:
            mark = label == "code" and urlsplit(links[label]).netloc == "github.com"
            pill = badge(text, "outline", name="link-" + label + ("-github" if mark else ""), mark=mark)
            out.append(f"[{pill}]({markdown_url(links[label])})")
    return "".join(f" {b}" for b in out)


def render_entry(entry, group_tags, badge, group_color="grey"):
    if "org" in entry:
        tags = "".join(f" {badge.tag(tag)}" for tag in entry.get("tags", []))
        title = md(entry["title"])
        return f"- **`{entry['label']}`** {title}.{link_badges(entry['links'], badge)}{tags}"
    title = md(entry["title"])
    title = title if title[-1] in ".?!" else title + "."
    tags = [badge(group_tags[entry["group"]], group_color)] if entry.get("group") in group_tags else []
    tags = "".join(f" {t}" for t in tags + [badge.tag(tag) for tag in entry.get("tags", [])])
    main = next(label for label in MAIN_LINKS if label in entry["links"])  # the venue badge opens it, the paper when there is one
    venue = badge.venue(entry["venue"], entry["year"])
    # the title comes first; the venue badge after it opens the paper (or the work's page when there is no paper)
    return f"- {title} [{venue}]({markdown_url(entry['links'][main])}){link_badges(entry['links'], badge, skip=main)}{tags}"


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
    rated = any(t in LEVELS or t in CHANNEL_TINTS for e in rows for t in e.get("tags", []))
    head = "<th>Product</th><th>Company</th>" + ("<th>Level and channels</th>" if rated else "")
    body = []
    for group in sorted(companies.values(), key=lambda g: product_name(g[0]).casefold()):
        names, levels = [], []
        for e in group:
            names.append(f'{icons[e["series"]]}<b><a href="{html.escape(e["links"]["website"])}">{md(product_name(e))}</a></b>')
            tags = sorted((t for t in e.get("tags", []) if t in LEVELS or t in CHANNEL_TINTS), key=lambda t: t not in LEVELS)
            if not any(t in LEVELS for t in tags):  # so that a line without a level does not seem to share the one above
                tags.insert(0, None)
            levels.append(" ".join(badge.img(t) if t else badge.img("No level", "muted") for t in tags))
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
DOI = "10.20944/preprints202611.0793.v1"


def card(href, icon, title, lines, full=None, note=None):
    """One cell of the contents grid: icon, title, an optional small note, then lines of links."""
    href = href if href.startswith("https://") else f"#{href}"
    tip = f' title="{html.escape(full)}"' if full else ""
    body = (f"<br/><sub>{note}</sub>" if note else "") + "".join(f"<br/>{line}" for line in lines)
    return (f'<td align="center" valign="top" width="33%"><a href="{href}"{tip}><img src="assets/icons/{icon}.svg" width="40" alt=""/></a>'
            f'<br/><a href="{href}"{tip}><b>{html.escape(title)}</b></a>{body}</td>')


def contents(tops, children, count):
    """The table of contents as a grid of cards, with Contributing and Citation below. A section with `card_of` has no
    card of its own: the card of the section it names links to it, after that section's own subsections."""
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

    def guests(node):
        return [f'<a href="#{n["id"]}">{html.escape(n.get("short", n["title"]))}</a>' for n in tops if n.get("card_of") == node["id"]]

    cells = [card("foundations", "foundations", f"{ROMAN[2]}. Foundations", [], "Overview and Foundations",
                  note="Definitions · Channels · Levels")]
    for node in tops:
        if "card_of" in node:
            continue
        lines = ([links(node)] if links(node) else []) + guests(node)
        cells.append(card(node["id"], node["icon"], numbered(node), lines, node["title"]))
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
    # the header of docs/readme-intro.md names these files
    badge.path("Paper (PDF)", "primary", name="header-paper", height=30, size=13, bold=True)
    badge.path("Project website", "outline", name="header-website", height=30, size=13, bold=True)
    badge.path(f"DOI {DOI}", "outline", name="header-doi")
    badge.path(f"{papers} papers", "gold", name="header-papers")
    badge.path("MIT License", "outline", name="header-license")
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
            color = GROUP_TINTS.get(top_of.get(node["id"]), "grey")
            used = [g["name"] for g in node.get("groups", []) if any(e.get("group") == g["name"] for e in own)]
            if len(used) >= 2:
                # the paper's own divisions of this section, in its order, one short list each
                sub = "#" * min(level + 1, 6)
                for name in used:
                    parts.append(f"{sub} {name}\n")
                    parts.extend(render_entry(e, {}, badge, color) for e in own if e.get("group") == name)
                    parts.append("")
                rest = [e for e in own if e.get("group") not in used]
                if rest:
                    parts.append(f"{sub} Other Works\n")
                    parts.extend(render_entry(e, {}, badge, color) for e in rest)
                    parts.append("")
            else:
                # one division or none: a single list, without a tag that every entry would share
                parts.extend(render_entry(e, {}, badge, color) for e in own)
                parts.append("")
        for child in children.get(node["id"], []):
            emit(child)

    for top in tops:
        emit(top)
    parts.append((ROOT / "docs" / "readme-footer.md").read_text(encoding="utf-8").rstrip())
    parts += ["", "<!-- badge images -->", *badge.definitions()]
    return "\n".join(parts) + "\n", badge.files


def validate_local_links(content):
    anchors = set(re.findall(r'<a id="([^"]+)"', content))
    content = re.sub(r"```.*?```", "", content, flags=re.S)
    for target in re.findall(r"\]\(([^\s)]+)\)", content) + re.findall(r'<a href="([^"]+)"', content):
        if target.startswith("#") and target[1:] not in anchors:
            raise ValueError(f"Broken anchor: {target}")
        if not target.startswith(("https://", "#", "mailto:")) and not (ROOT / target.split("#")[0]).exists():
            raise ValueError(f"Missing local link: {target}")
    for target in re.findall(r'<img[^>]+src="([^"]+)"', content) + re.findall(r"^\[b-[^\]]+\]: (\S+)$", content, flags=re.M):
        if not target.startswith("https://") and not (ROOT / target).is_file():
            raise ValueError(f"Missing image: {target}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validate the data and require README.md to match the generated output")
    args = parser.parse_args()
    sections, by_id = load_sections()
    entries = load_entries(by_id)
    content, badges = build(sections, entries)
    output = ROOT / "README.md"
    folder = ROOT / BADGE_DIR
    if args.check:
        on_disk = {f.name: f.read_text(encoding="utf-8") for f in folder.glob("*.svg")} if folder.is_dir() else {}
        if on_disk != badges:
            raise ValueError(f"{BADGE_DIR} is stale. Run python3 scripts/build_readme.py")
        validate_local_links(content)
        if output.read_text(encoding="utf-8") != content:
            raise ValueError("README.md is stale. Run python3 scripts/build_readme.py")
        print(f"OK: {len(entries)} entries in {len(sections)} sections; schema, unique sources, local links, images, anchors, and generated README checked.")
    else:
        folder.mkdir(parents=True, exist_ok=True)
        for stale in folder.glob("*.svg"):
            if stale.name not in badges:
                stale.unlink()
        for name, svg in badges.items():
            (folder / name).write_text(svg, encoding="utf-8")
        validate_local_links(content)
        output.write_text(content, encoding="utf-8")
        print(f"Generated README.md with {len(entries)} entries.")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, TypeError, FileNotFoundError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)
