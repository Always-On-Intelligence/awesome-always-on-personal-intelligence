#!/usr/bin/env python3
"""Validate the reading list and generate README.md (stdlib only)."""

import argparse
from collections import Counter
from datetime import date
import html
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = [
    ("foundations", "Surveys & Foundations", "surveys", "Related surveys, early visions of personal assistance, and the classic ideas the survey builds on.", [
        ("surveys", "Surveys & Roadmaps"), ("background", "Early Visions & Classic Foundations")]),
    ("sensing", "Sensing", "sensing", "What an assistant can observe, what observation costs, and how it decides when, how long, and how much to sense.", [
        ("streams", "Input Streams: Body, Vision, Audio & Screen"), ("triggering", "Triggering & Sampling"),
        ("windows", "Streaming Windows & Event Segmentation"), ("representation", "Representation & Compression"),
        ("conditions", "Operating Conditions & Compute Placement"), ("coupling", "Routing & Sensing Guided by Memory and Action")]),
    ("memory", "Memory", "memory", "What can persist across interactions and how memory is written, retrieved, consolidated, corrected, and retired.", [
        ("types", "Memory Types & Storage"), ("admission", "Admission & Encoding"), ("retrieval", "Indexing & Retrieval"),
        ("maintenance", "Consolidation, Correction & Forgetting"), ("coupling", "Writes from Sensing & Action")]),
    ("action", "Action", "action", "Whether and when to intervene, how control is retained, through which interface, and under whose authority.", [
        ("timing", "When to Act: Intervene, Wait or Ask"), ("interventions", "Interventions, Consequences & Feedback"),
        ("control", "Control Depth & Interfaces"), ("authority", "Authority, Safety & Interruption Cost"), ("coupling", "Memory-Guided Action")]),
    ("systems", "Always-On Systems & Applications", "systems", "Integrated systems and product sources reviewed in the survey, grouped by interaction domain. `Product` marks product documentation or product studies.", [
        ("wearable", "Wearable"), ("digital", "Digital"), ("physical", "Physical")]),
    ("evolution", "Self-Evolution", "evolution", "Revising the assistant from its own operating experience: what changes, how a change is validated, and what can go wrong.", [
        ("deployed", "Learning from Operating Experience"), ("recursive", "Recursive Revision, Validation & Risks")]),
    ("evaluation", "Benchmarks & Evaluation", "evaluation", "Benchmarks and evaluation settings for each module, plus long-term and deployment evaluation.", [
        ("sensing", "Sensing"), ("memory", "Memory"), ("action", "Action"), ("longitudinal", "Long-Term & Deployment Evaluation")]),
    ("products", "Products & Tools", "products", "Products, hardware platforms, and developer infrastructure. Descriptions follow official documentation, not independent evaluation.", [
        ("products", "Products"), ("devices", "Devices & Platforms"), ("tools", "Developer Tools")]),
]
SUBCATEGORIES = {key: {s for s, _ in subs} for key, _, _, _, subs in CATEGORIES}
CHANNELS = ["S→A", "S→M", "M→A", "A→S", "M→S", "A→M"]
TAGS = set(CHANNELS) | {"Product"}
LINK_LABELS = ["paper", "blog", "docs", "website", "project", "code", "data"]
GROUPS = {
    "products.json": {"wearables": "Wearable", "apps": "Desktop & Mobile", "hosted": "Cloud & Messaging"},
    "tools.json": {"memory": "Memory", "runtime": "Runtime", "integrations": "Integrations"},
}


def is_single_line(value):
    return isinstance(value, str) and bool(value.strip()) and not any(c in value for c in "\n\r")


def normalized(url):
    return re.sub(r"v\d+$", "", url.rstrip("/").replace("/pdf/", "/abs/").removesuffix(".pdf")).lower()


def load_entries():
    entries = []
    seen_ids = set()
    seen_urls = set()
    for filename in ("research.json", "products.json", "tools.json"):
        data = json.loads((ROOT / "data" / filename).read_text(encoding="utf-8"))
        if not isinstance(data, list) or not data:
            raise ValueError(f"{filename}: expected a nonempty array")
        for entry in data:
            if not isinstance(entry, dict):
                raise ValueError(f"{filename}: each entry must be an object")
            name = entry.get("id", "<missing id>")
            for field in ("id", "category", "subcategory", "title"):
                if not is_single_line(entry.get(field)):
                    raise ValueError(f"{name}: invalid {field}")
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or name in seen_ids:
                raise ValueError(f"{name}: invalid or duplicate id")
            seen_ids.add(name)
            category, sub = entry["category"], entry["subcategory"]
            if category not in SUBCATEGORIES or sub not in SUBCATEGORIES[category]:
                raise ValueError(f"{name}: unknown category/subcategory {category}/{sub}")
            links = entry.get("links")
            if not isinstance(links, dict) or not links:
                raise ValueError(f"{name}: missing links")
            for label, url in links.items():
                if label not in LINK_LABELS:
                    raise ValueError(f"{name}: unknown link type {label}")
                parsed = urlsplit(url) if isinstance(url, str) else None
                if not parsed or parsed.scheme != "https" or not parsed.netloc or not url.isascii() or any(c in url for c in '<>"') or any(c.isspace() for c in url):
                    raise ValueError(f"{name}: invalid HTTPS URL {url}")
            if filename == "research.json":
                if (category, sub) in (("products", "products"), ("products", "tools")):
                    raise ValueError(f"{name}: products and tools belong in products.json and tools.json")
                year = entry.get("year")
                if type(year) is not int or not 1900 <= year <= date.today().year:
                    raise ValueError(f"{name}: invalid year")
                if not is_single_line(entry.get("venue")) or "`" in entry["venue"]:
                    raise ValueError(f"{name}: missing or invalid venue")
                primary = next((links[k] for k in ("paper", "blog", "docs", "website", "code") if k in links), None)
                if not primary:
                    raise ValueError(f"{name}: needs a paper, blog, docs, website, or code link")
                if normalized(primary) in seen_urls:
                    raise ValueError(f"{name}: duplicate source; choose one primary home")
                seen_urls.add(normalized(primary))
                tags = entry.get("tags", [])
                if not isinstance(tags, list) or len(tags) > 3 or any(t not in TAGS for t in tags):
                    raise ValueError(f"{name}: tags must be channel tags ({', '.join(CHANNELS)}) or Product")
            else:
                expected = "products" if filename == "products.json" else "tools"
                if (category, sub) != ("products", expected):
                    raise ValueError(f"{name}: {filename} entries use category 'products' and subcategory '{expected}'")
                if entry.get("group") not in GROUPS[filename]:
                    raise ValueError(f"{name}: group must be one of {', '.join(GROUPS[filename])}")
                if not is_single_line(entry.get("description")):
                    raise ValueError(f"{name}: invalid description")
                checked = entry.get("checked", "")
                if not isinstance(checked, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", checked) or date.fromisoformat(checked) > date.today():
                    raise ValueError(f"{name}: checked must be a past YYYY-MM-DD date")
                entry = dict(entry, label=GROUPS[filename][entry["group"]], order=list(GROUPS[filename]).index(entry["group"]))
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
    ordered = [k for k in LINK_LABELS if k in links]
    return " ".join(f"[[{label}]({markdown_url(links[label])})]" for label in ordered)


def sentence(title):
    title = md(title)
    return title if title[-1] in ".?!" else title + "."


def render_entry(entry):
    if "label" in entry:
        description = entry["description"]
        if len(description) > 1 and description[1].islower():
            description = description[0].lower() + description[1:]
        return f"- **`{entry['label']}`** {md(entry['title'])}: {md(description)} {resource_links(entry['links'])}"
    tags = "".join(f" `{tag}`" for tag in entry.get("tags", []))
    return f"- **`{entry['venue']} {entry['year']}`** {sentence(entry['title'])} {resource_links(entry['links'])}{tags}"


def order(entry):
    if "label" in entry:
        return (entry["order"], entry["title"].casefold())
    return (-entry["year"], entry["title"].casefold())


def build(entries):
    counts = Counter(e["category"] for e in entries)
    works = sum(1 for e in entries if "label" not in e)
    papers = sum(1 for e in entries if "label" not in e and "paper" in e["links"])
    intro = (ROOT / "docs" / "readme-intro.md").read_text(encoding="utf-8").rstrip()
    intro = intro.replace("{{PAPER_COUNT}}", str(papers)).replace("{{WORK_COUNT}}", str(works))
    toc = ["<details>", "<summary><b>Table of Contents</b></summary>", "", "- [News](#news)", "- [Introduction](#introduction)"]
    for key, title, _, _, subs in CATEGORIES:
        toc.append(f"- [{title}](#{key}) ({counts[key]})")
        for sub, subtitle in subs:
            if any(e["category"] == key and e["subcategory"] == sub for e in entries):
                toc.append(f"  - [{subtitle}](#{key}-{sub})")
    toc += ["- [Contributing](#contributing)", "- [Citation](#citation)", "", "</details>"]
    parts = ["<!-- Generated by scripts/build_readme.py. Edit data/*.json or docs/readme-*.md, then regenerate. -->", "",
             intro.replace("{{TOC}}", "\n".join(toc)), ""]
    for key, title, icon, description, subs in CATEGORIES:
        if not counts[key]:
            continue
        parts.append(f'---\n\n<a id="{key}"></a>\n## <img src="assets/icons/{icon}.svg" height="30" align="top" alt=""/> {title}\n\n{description}\n')
        for sub, subtitle in subs:
            selected = sorted((e for e in entries if e["category"] == key and e["subcategory"] == sub), key=order)
            if not selected:
                continue
            parts.append(f'<a id="{key}-{sub}"></a>\n### {subtitle}\n')
            parts.extend(render_entry(e) for e in selected)
            parts.append("")
    parts.append((ROOT / "docs" / "readme-footer.md").read_text(encoding="utf-8").rstrip())
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
    entries = load_entries()
    content = build(entries)
    validate_local_links(content)
    output = ROOT / "README.md"
    if args.check:
        if output.read_text(encoding="utf-8") != content:
            raise ValueError("README.md is stale. Run python3 scripts/build_readme.py")
        print(f"OK: {len(entries)} entries; schema, unique sources, local links, images, anchors, and generated README checked.")
    else:
        output.write_text(content, encoding="utf-8")
        print(f"Generated README.md with {len(entries)} entries.")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, TypeError, FileNotFoundError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)
