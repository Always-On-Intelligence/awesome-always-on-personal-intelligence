# Curation notes

Last full pass: **2026-09-29**.

## Source

The reading list collects every work cited in the survey chapters: Introduction, Foundations, Sensing, Memory, Action, Integrated Systems, HALO, Trends, and Conclusion. Product documentation and hardware pages cited in the survey are included as sources. The product and tool directories extend this with curated entries checked against official pages.

## Placement

Each work has one home, chosen from where the survey discusses it:

- Rows of the application landscape and loop-closure tables go to **Always-On Systems & Applications**, grouped by the table's domain. Systems at the governed-revision level go to **Self-Evolution**.
- Rows of the module benchmark tables go to **Benchmarks & Evaluation**. Rows that only describe a method's own test stay with the method.
- Methods go to the module subsection that cites them: its space, operating conditions, policy decision, or coupling channel.
- Works from the self-evolution discussions go to **Self-Evolution**, and surveys to **Surveys & Foundations**.
- Hardware pages from the survey's literature map go to **Devices & Platforms**.

Channel tags come from the survey's coupling sections and the channel columns of its application table.

## Metadata

- **Titles** follow the arXiv or publisher title. Where the arXiv metadata drops spaces or differs from the published title, the published title is kept.
- **Venues** follow the acceptance venue and its year when one exists: the survey bibliography first, then DBLP proceedings records, ACL Anthology DOIs (to separate main-conference and Findings papers), and OpenReview decisions. Otherwise the entry is labeled `arXiv` with the year of the first preprint. Some labels are therefore newer than the survey's bibliography.
- **Paper links** point to the arXiv abstract page when one exists, otherwise to the DOI or an official or author page.
- **Code links** come from the previous hand-curated pass, the survey bibliography, or the repository linked on the paper's Hugging Face page. Only repositories under a `github.com/owner/repo` path are used.

Links were checked during this pass. Availability and product state can change, so please report broken or moved links.
