# Curation notes

Last full pass: **2026-10-05**, against the survey draft of the same date, with the section structure of that draft.

## Source

The reading list collects every work cited in the survey chapters: Introduction, Foundations, Sensing, Memory, Action, Applications and Loop Closure, HALO, Trends, and Conclusion. Product documentation and hardware pages cited in the survey are included as sources. The product and tool directories extend this with curated entries checked against official pages.

## Placement

The list follows the survey's module chapters and titles, recorded in `data/sections.json`. Each work appears once, under the section where the survey treats it most directly, and each list runs from the newest work to the oldest. Works cited only as background in the survey's Introduction or Foundations are left out. The rules are in [the scope and structure notes](taxonomy.md#placement).

## Metadata

- **Titles** follow the arXiv or publisher title. Where the arXiv metadata drops spaces or differs from the published title, the published title is kept.
- **Venues** follow the acceptance venue and its year when one exists: the survey bibliography first, then DBLP proceedings records, ACL Anthology DOIs (to separate main-conference and Findings papers), and OpenReview decisions. Otherwise the entry is labeled `arXiv` with the year of the first preprint. Some labels are therefore newer than the survey's bibliography.
- **Paper links** point to the arXiv abstract page when one exists, otherwise to the DOI or an official or author page.
- **Code links** come from the previous hand-curated pass, the survey bibliography, or the repository linked on the paper's Hugging Face page. Only repositories under a `github.com/owner/repo` path are used.

Links were checked during this pass. Availability and product state can change, so please report broken or moved links.
