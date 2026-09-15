#!/usr/bin/env python3
"""Validate the curated catalog and generate the GitHub reading list (stdlib only)."""

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
REPO = "https://github.com/Always-On-Agent/awesome-always-on-personal-ai"
SITE = "https://always-on-agent.github.io"
CATEGORIES = [
    ("surveys", "Surveys & Foundations", "Orient yourself in personal, proactive, and persistent assistance.", [
        ("surveys", "Surveys & Roadmaps"), ("foundations", "Foundations of Personal & Proactive Assistants")]),
    ("sensing", "Sensing & Context Awareness", "Notice relevant changes and decide what to observe, when, and at what cost.", [
        ("context", "Multimodal & Digital Context Understanding"), ("streaming", "Streaming Perception & Event Detection"), ("adaptive", "Adaptive & Efficient Sensing")]),
    ("memory", "Memory & Personalization", "Keep personal context useful, current, and correctable across interactions.", [
        ("personal", "Personal, Episodic & Semantic Memory"), ("modeling", "User Modeling & Personalization"), ("commitments", "Persistent Tasks & Commitments"), ("lifecycle", "Memory Management, Updating & Forgetting")]),
    ("action", "Proactive Action & Continuous Execution", "Choose whether to wait, ask, communicate, prepare, or execute, and follow up on the result.", [
        ("initiative", "Initiative, Timing & Interruptibility"), ("continuation", "Monitoring, Follow-up & Task Continuation"), ("execution", "Tool Use, Execution & Feedback")]),
    ("systems", "Integrated Systems & Applications", "Study how sensing, memory, and action work together in real service settings. These are research systems; their demonstrated scope varies.", [
        ("daily", "Situated Daily Assistance"), ("conversation", "Conversation & Meeting Assistance"), ("digital", "Digital Workspace & Personal Services"), ("physical", "Physical Assistance & Collaboration")]),
    ("evaluation", "Benchmarks & Datasets", "Evaluate component capabilities, intervention timing, continuing tasks, and outcomes over time.", [
        ("sensing", "Sensing & Streaming Understanding"), ("memory", "Long-Term Memory & Personalization"), ("proactive", "Proactive Assistance & Continuing Tasks"), ("longitudinal", "End-to-End & Longitudinal Evaluation")]),
    ("products", "Products", "User-facing products with capabilities relevant to always-on assistance. Descriptions reflect official documentation, not independent end-to-end evaluations. Availability can depend on plan, platform, region, or hardware.", [
        ("wearables", "Wearables & Ambient Devices"), ("apps", "Desktop & Mobile Assistants"), ("hosted", "Cloud & Messaging Assistants")]),
    ("tools", "Tools & Infrastructure", "Developer building blocks for personal state, continuing operation, and governed integrations. Open source is an attribute, not a separate research category.", [
        ("memory", "Memory & Personal Data Infrastructure"), ("runtime", "Background Runtimes & Event Scheduling"), ("integrations", "Integrations, Permissions & Observability")]),
]
SUBCATEGORIES = {key: {s for s, _ in subs} for key, _, _, subs in CATEGORIES}


def is_single_line(value):
    return isinstance(value, str) and bool(value.strip()) and not any(c in value for c in "\n\r")


def load_entries():
    entries = []
    seen_ids = set()
    seen_papers = set()
    for filename in ("research.json", "products.json", "tools.json"):
        path = ROOT / "data" / filename
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, list) or not data:
            raise ValueError(f"{filename}: expected a nonempty array")
        for entry in data:
            if not isinstance(entry, dict):
                raise ValueError(f"{filename}: each entry must be an object")
            name = entry.get("id", "<missing id>")
            for field in ("id", "category", "subcategory", "title", "description"):
                value = entry.get(field)
                if not is_single_line(value):
                    raise ValueError(f"{name}: invalid {field}")
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or name in seen_ids:
                raise ValueError(f"{name}: invalid or duplicate id")
            seen_ids.add(name)
            category = entry["category"]
            if category not in SUBCATEGORIES or entry["subcategory"] not in SUBCATEGORIES[category]:
                raise ValueError(f"{name}: unknown category/subcategory")
            expected_file = "products.json" if category == "products" else "tools.json" if category == "tools" else "research.json"
            if filename != expected_file:
                raise ValueError(f"{name}: belongs in {expected_file}")
            links = entry.get("links")
            if not isinstance(links, dict) or not links:
                raise ValueError(f"{name}: missing links")
            for label, url in links.items():
                if label not in {"paper", "code", "project", "data", "website", "docs"}:
                    raise ValueError(f"{name}: unknown link type {label}")
                if not isinstance(url, str):
                    raise ValueError(f"{name}: URL must be a string")
                parsed = urlsplit(url)
                if parsed.scheme != "https" or not parsed.netloc or any(c in url for c in '<>"') or any(c.isspace() for c in url):
                    raise ValueError(f"{name}: invalid HTTPS URL {url}")
            if filename == "research.json":
                year = entry.get("year")
                if type(year) is not int or not 1900 <= year <= date.today().year:
                    raise ValueError(f"{name}: invalid year")
                if not is_single_line(entry.get("venue")):
                    raise ValueError(f"{name}: research needs a venue")
                paper = links.get("paper")
                if not paper:
                    raise ValueError(f"{name}: missing primary paper URL")
                normalized = re.sub(r"v\d+$", "", paper.rstrip("/").replace("/pdf/", "/abs/").removesuffix(".pdf"))
                if normalized in seen_papers:
                    raise ValueError(f"{name}: duplicate paper; choose one primary home")
                seen_papers.add(normalized)
            else:
                checked_text = entry.get("checked", "")
                if not isinstance(checked_text, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", checked_text):
                    raise ValueError(f"{name}: checked must use YYYY-MM-DD")
                checked = date.fromisoformat(checked_text)
                if checked > date.today():
                    raise ValueError(f"{name}: future verification date")
                if category == "products" and any(not is_single_line(entry.get(field)) for field in ("status", "form_factor")):
                    raise ValueError(f"{name}: product needs status and form_factor")
            tags = entry.get("tags", [])
            if not isinstance(tags, list) or len(tags) > 2 or any(not is_single_line(t) for t in tags):
                raise ValueError(f"{name}: use at most two nonempty tags")
            entries.append(entry)
    return entries


def md(value):
    value = html.escape(str(value), quote=False)
    for char in "|[]\\*_`":
        value = value.replace(char, f"&#{ord(char)};")
    return value


def code_span(value):
    value = str(value)
    delimiter = "`" * (max((len(run) for run in re.findall(r"`+", value)), default=0) + 1)
    return f"{delimiter} {value} {delimiter}"


def markdown_url(url):
    for char in "()|\\`":
        url = url.replace(char, f"%{ord(char):02X}")
    return url


def resource_links(entry, exclude=()):
    return " · ".join(f"[{label.title()}]({markdown_url(url)})" for label, url in entry["links"].items() if label not in exclude)


def render_entry(entry):
    links = entry["links"]
    primary = next((k for k in ("paper", "website", "code", "project", "docs") if k in links), next(iter(links)))
    reference = f"**[{md(entry['title'])}]({markdown_url(links[primary])})**"
    if entry["category"] == "products":
        availability = f"{md(entry['status'])}<br><sub>Checked {entry['checked']}</sub>"
        return f"| {reference}<br><sub>{md(entry['form_factor'])}</sub> | {md(entry['description'])} | {availability} | {resource_links(entry)} |"
    label = code_span(f"{entry['venue']} {entry['year']}") + " " if "year" in entry else ""
    reference = label + reference
    extra = resource_links(entry, (primary,))
    if extra:
        reference += " · " + extra
    tags = " ".join(code_span(tag) for tag in entry.get("tags", []))
    suffix = f" {tags}" if tags else ""
    return f"- {reference}<br>\n  {md(entry['description'])}{suffix}\n"


def build(entries):
    research_count = sum(e["category"] not in {"products", "tools"} for e in entries)
    counts = Counter(e["category"] for e in entries)
    header = (ROOT / "docs" / "readme-intro.md").read_text(encoding="utf-8").rstrip()
    header = header.replace("{{RESEARCH_COUNT}}", str(research_count)).replace("{{PRODUCT_COUNT}}", str(counts["products"])).replace("{{TOOL_COUNT}}", str(counts["tools"]))
    parts = ["<!-- Generated by scripts/build_readme.py. Edit data/*.json or docs/readme-intro.md. -->", header, '<a id="contents"></a>\n## Browse the collection\n']
    for key, title, _, _ in CATEGORIES:
        if counts[key]:
            parts.append(f"- [{title}](#{key}) · **{counts[key]}**")
    parts.append("\nEntries have one primary home. Research is ordered by year, newest first, then by title; products and tools are alphabetical within each group. See the [scope and taxonomy](docs/taxonomy.md) for inclusion rules and cross-cutting themes.\n")
    for key, title, description, subs in CATEGORIES:
        if not counts[key]:
            continue
        parts.append(f'---\n\n<a id="{key}"></a>\n## <img src="assets/icons/{key}.svg" width="28" height="28" alt=""/> {title}\n\n{description}\n')
        if key == "evaluation":
            parts.append(f"**From our survey — [HALO: Harness for Always-on Loop Oversight]({SITE}/#halo).** A protocol for source-based review and scoped execution. The survey reports a read-mode review of 31 configurations; run mode describes a protocol rather than new benchmark results.\n")
        if key == "products":
            parts.append("[Source notes and availability details](docs/product-sources.md) · A capture or recall feature alone does not establish a complete continuing loop.\n")
        for sub, subtitle in subs:
            selected = [e for e in entries if e["category"] == key and e["subcategory"] == sub]
            if not selected:
                continue
            parts.append(f'<a id="{key}-{sub}"></a>\n### {subtitle}\n')
            if key == "products":
                parts.append("| Product / form | Relevant capability | Availability | Sources |\n|:--|:--|:--|:--|")
            for entry in sorted(selected, key=lambda e: (-e.get("year", 0), e["title"].casefold())):
                parts.append(render_entry(entry))
            parts.append("")
        parts.append("[↑ Back to collection](#contents)\n")
    parts.append((ROOT / "docs" / "readme-footer.md").read_text(encoding="utf-8").rstrip())
    return "\n".join(parts) + "\n"


def validate_local_links(content):
    anchors = set(re.findall(r'<a id="([^"]+)"', content))
    for label, target in re.findall(r"\[([^\]]*)\]\(([^\s)]+)\)", content):
        if target.startswith("#") and target[1:] not in anchors:
            raise ValueError(f"Broken anchor: {target}")
        if not target.startswith(("https://", "#")) and not (ROOT / target.split("#")[0]).exists():
            raise ValueError(f"Missing local link: {target}")
    for target in re.findall(r'<img[^>]+src="([^"]+)"', content):
        if not target.startswith("https://") and not (ROOT / target).is_file():
            raise ValueError(f"Missing image: {target}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validate catalog and require README to match generated output")
    args = parser.parse_args()
    entries = load_entries()
    content = build(entries)
    validate_local_links(content)
    output = ROOT / "README.md"
    if args.check:
        if output.read_text(encoding="utf-8") != content:
            raise ValueError("README is stale. Run python3 scripts/build_readme.py")
        print(f"OK: {len(entries)} entries; schema, unique papers, local links, images, anchors, and generated README checked.")
    else:
        output.write_text(content, encoding="utf-8")
        print(f"Generated README.md with {len(entries)} entries.")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, TypeError, FileNotFoundError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)
