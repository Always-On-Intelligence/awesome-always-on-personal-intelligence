# Contributing

Thank you for helping keep this reading list accurate and useful.

## Suggest a resource

Use the [resource suggestion form](https://github.com/Always-On-Intelligence/awesome-always-on-personal-intelligence/issues/new?template=resource.yml) if you prefer not to edit JSON. Include a primary source and one sentence on how the work relates to always-on personal intelligence.

## Add or correct an entry

1. Read [the scope and structure notes](docs/taxonomy.md) and search the data for the work.
2. Add one record to the matching file: `data/research.json` for works cited in the survey, `data/products.json` for products, or `data/tools.json` for developer tools.
3. Regenerate and validate the README:

```bash
python3 scripts/build_readme.py
python3 scripts/build_readme.py --check
```

Python 3.9 or newer is enough; no packages are required. Commit the data change together with the regenerated README.

## Research entries

```json
{
  "id": "egolife",
  "section": "sec-3-5-2",
  "group": "Continuous and triggered capture: coverage and cost",
  "title": "EgoLife: Towards Egocentric Life Assistant",
  "year": 2025,
  "venue": "CVPR",
  "links": {"paper": "https://arxiv.org/abs/2503.03803", "code": "https://github.com/EvolvingLMMs-Lab/EgoLife"},
  "tags": ["L2"]
}
```

- `id`: unique lowercase kebab-case string.
- `section`: the id of the survey section that discusses the work, from `data/sections.json` (for example `sec-3-3-1` for Whether to Observe: Triggering and Wake-Up).
- `group` (optional): one of the group names listed for that section, such as a paragraph of a space subsection or a group of a benchmark table. The README shows the group's short tag.
- `venue` and `year`: the acceptance venue and its year when the work has one; otherwise `arXiv` and the year of the first preprint. Product pages and documentation use the organization as the venue.
- `links`: HTTPS URLs keyed by `paper`, `blog`, `docs`, `website`, `project`, `code`, or `data`. Prefer the arXiv abstract page, then the DOI or official page. Add code only from the official repository.
- `tags` (optional): up to two channel tags (`S→A`, `S→M`, `M→A`, `A→S`, `M→S`, `A→M`), a loop-closure level (`L0` to `L5`), and `Product`.

The README renders each entry as:

```
- **`Venue Year`** Title. [[paper](URL)] [[code](URL)] `M→S`
```

## Products and tools

`data/products.json` has one record per product:

```json
{
  "id": "muse",
  "section": "products-digital",
  "title": "Muse",
  "org": "Meta",
  "links": {"website": "https://muse.ai/"},
  "tags": ["L3"],
  "sources": ["metamuse2026", "musedesign2026"],
  "checked": "2026-10-05"
}
```

- `section`: `products-wearable`, `products-digital`, `products-physical`, or `products-devices`.
- `links`: only the product's most official page, such as its product or feature page; never a blog post. Use an official help page only when no product page exists.
- `tags` (optional): channel tags and the loop-closure level the survey gives the product.
- `sources`: the survey citation keys merged into this record; leave it empty for a curated addition.
- `checked`: the date you opened the official page (`YYYY-MM-DD`).

Developer tools in `data/tools.json` keep a one-sentence `description`, a `group` (`memory`, `runtime`, or `integrations`), their website, code, and docs links, and the `checked` date.

## Curation principles

- Place each work once, under the survey section that discusses it. Lists run from the newest work to the oldest.
- Add a channel tag only when the work supplies or uses that channel.
- Keep titles exact and leave out rankings, promotional wording, and affiliate links.
- Report corrections, moved links, and discontinued products with a source.

## Checks

`--check` validates the data schema, unique IDs and sources, section names, dates, local links, images, anchors, and whether the README matches the data. It runs offline, so it cannot confirm that external pages are available. For an optional network audit, run `python3 scripts/check_links.py`; review restricted or transient results before removing a link.
