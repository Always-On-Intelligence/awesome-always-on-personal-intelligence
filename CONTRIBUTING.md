# Contributing

Thank you for helping keep this reading list accurate and useful.

## Suggest a resource

Use the [resource suggestion form](https://github.com/Always-On-Agent/awesome-always-on-personal-ai/issues/new?template=resource.yml) if you prefer not to edit JSON. Include a primary source and one sentence on how the work relates to always-on personal assistance.

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
- `section`: the id of the survey section that discusses the work, from `data/sections.json` (for example `sec-3-3-1` for 3.3.1 Whether to Observe: Triggering and Wake-Up).
- `group` (optional): one of the groups listed for that section, such as a paragraph of a space subsection or a group of a benchmark table.
- `venue` and `year`: the acceptance venue and its year when the work has one; otherwise `arXiv` and the year of the first preprint. Product pages and documentation use the organization as the venue.
- `links`: HTTPS URLs keyed by `paper`, `blog`, `docs`, `website`, `project`, `code`, or `data`. Prefer the arXiv abstract page, then the DOI or official page. Add code only from the official repository.
- `tags` (optional): up to two channel tags (`S→A`, `S→M`, `M→A`, `A→S`, `M→S`, `A→M`), a loop-closure level (`L0` to `L5`), and `Product`.

The README renders each entry as:

```
- **`Venue Year`** Title. [[paper](URL)] [[code](URL)] `M→S`
```

## Products and tools

Products and tools use the sections `products-list` and `products-tools`, and keep a one-sentence `description`, a `group` (`wearables`, `apps`, or `hosted` for products; `memory`, `runtime`, or `integrations` for tools), and the date you `checked` the official source (`YYYY-MM-DD`). Record the sources behind capability and availability claims in [docs/product-sources.md](docs/product-sources.md).

## Curation principles

- Place each work once, under the survey section that discusses it.
- Add a channel tag only when the work supplies or uses that channel.
- Keep titles exact and leave out rankings, promotional wording, and affiliate links.
- Report corrections, moved links, and discontinued products with a source.

## Checks

`--check` validates the data schema, unique IDs and sources, section names, dates, local links, images, anchors, and whether the README matches the data. It runs offline, so it cannot confirm that external pages are available. For an optional network audit, run `python3 scripts/check_links.py`; review restricted or transient results before removing a link.
