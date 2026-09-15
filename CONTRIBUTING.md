# Contributing

Thank you for helping maintain a focused collection of always-on personal AI work.

## Suggest a resource

Use the [resource suggestion form](https://github.com/Always-On-Agent/awesome-always-on-personal-ai/issues/new?template=resource.yml) if you prefer not to edit JSON. Include a primary source and one sentence explaining its relevance to ongoing personal assistance.

## Add or correct an entry

1. Read [the scope and taxonomy](docs/taxonomy.md) and search the existing data for the work.
2. Choose one primary home: `data/research.json`, `data/products.json`, or `data/tools.json`.
3. Add an entry matching the existing schema. Keep the title exact, the description to one factual sentence, and tags to at most two. Verify the year and venue; use `arXiv` for a preprint when no published venue has been confirmed.
4. Link primary sources: the paper, official repository, project page, or official documentation. Add code/data links only when verified.
5. For a product, record its principal form factor, bounded availability status, and the date when you actually checked the official source. Add evidence to `docs/product-sources.md` for material capability or availability claims.
6. Regenerate and validate:

```bash
python3 scripts/build_readme.py
python3 scripts/build_readme.py --check
```

Python 3.10+ is sufficient; no packages are required. Commit both source-data changes and the generated README.

## Entry fields

Common fields: `id`, `category`, `subcategory`, `title`, `description`, `links`, and `tags`.

- IDs: unique lowercase kebab-case strings.
- Research: additionally `year` and a verified `venue`; `links.paper` is required.
- Products: additionally `form_factor`, `status`, and `checked` in `YYYY-MM-DD` format.
- Tools: additionally `checked` in `YYYY-MM-DD` format.
- Link keys: `paper`, `code`, `project`, `data`, `website`, or `docs`; use HTTPS URLs.
- Category/subcategory values: listed in `CATEGORIES` in `scripts/build_readme.py`.

## Curation principles

- Explain the always-on relevance; generic agent capability alone is insufficient.
- Choose one primary home per paper. Do not copy the same entry into multiple sections.
- Describe demonstrated mechanisms and evaluated settings without implying a complete continuing loop.
- Distinguish a research prototype, commercial product, and developer tool.
- Report corrections and discontinued or restricted products with sources.
- Keep speculative features, unsupported rankings, affiliate links, and promotional language out of entries.

## Checks

The repository check validates data structure, unique IDs and paper URLs, category names, dates, local files and images, README anchors, and generated-content consistency. It runs without network access; a passing check does **not** establish that external pages are available or their claims are correct. Contributors must check their primary sources.

For an optional network audit, run `python3 scripts/check_links.py`. Its report distinguishes confirmed HTTP failures from access restrictions and transient network errors; review those results before removing a link.
