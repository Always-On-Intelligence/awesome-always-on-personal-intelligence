# Scope and structure

This reading list accompanies *Always-On Personal Intelligence: A Roadmap Towards Continuing, Self-Evolving Loops*. It collects the works the survey discusses and arranges them by the survey's chapters, titles, and terms.

## Scope

Always-on personal intelligence is personal assistance that maintains two core properties for the same user. Operational continuity is the ability to keep operating between explicit requests and to decide when to act or wait, and state durability is the ability to preserve user-specific state for later use and to carry unresolved commitments across interaction boundaries. The continuing loop of Sensing, Memory, and Action provides both, and its self-evolving extension revises how the assistant works from operating experience. What counts is who decides whether to act: an assistant that acts only at a time or condition the user fixed carries out an earlier request. Continuous recording or model execution is not required.

The list includes component methods, benchmarks, and partial systems when the survey uses them as methods or evidence. Inclusion does not mean that a work meets the full always-on definition.

## Structure

The list follows the survey's chapters, titles, and terms, and it lists every work the survey cites. Products and Featured Industry Blogs come first, the research sections follow in the survey's order, and Background closes the list. `data/sections.json` records the sections in this reading order:

| Section | Parts |
|:--|:--|
| Products | One line per product the survey discusses, with its official page, by wearable, digital, and physical domain; devices and platforms; and a few curated products |
| Featured Industry Blogs | Engineering articles from organizations whose models and assistants are widely used, selected by the maintainers for how closely they match the survey's framing |
| Sensing, Memory, Action | Space, shared conditions, policy, coupling across the loop, and evaluation, with the survey's subsections |
| Applications, System Bottlenecks, and Loop Closure | Applications and bottlenecks by domain, shared conditions and implementation across modules, levels of loop closure, self-evolution in deployed loops |
| Trends and Open Problems | Sustaining the continuing loop; authority, privacy, and safety; self-evolution and recursive revision; longitudinal evaluation and real deployment |
| Related Surveys | Capability-focused and concurrent system-level surveys |
| Background | Works the Introduction and Foundations build on, and the earlier systems in the survey's map of the literature |

Long sections are divided into the survey's own sub-categories, kept as `groups` in `data/sections.json`: the paragraph headings of a subsection, the group rows of a module's benchmark table, the open problems of a Trends and Open Problems part, or the citation groups of the survey's related-survey paragraph. A work the survey cites goes under the sub-category that cites it, and works the survey does not cite yet go where they fit. A section whose works fall into fewer than two sub-categories is shown as one list.

The README's Foundations section summarizes the survey's definitions, coupling channels, and loop-closure levels. Works the survey cites only in its Introduction or Foundations, such as early visions, textbooks, and cognitive architectures, are listed under Background. Background and Featured Industry Blogs have no card of their own in the contents: a `card_of` field in `data/sections.json` names the section whose card links to them, Related Surveys and Products.

## Placement

Research works and products are kept apart. The survey's product sources (official pages, documentation, and blogs) are merged into one record per product, which links only the product's most official page and never a blog post, under its interaction domain. Each research work appears once, under the section where the survey treats it most directly:

1. A related survey discussed in the survey's positioning goes to Related Surveys.
2. An engineering article that the maintainers select for Featured Industry Blogs goes there. The section is curated: an article qualifies when its publisher's models or assistants are widely used and it describes the architecture of always-on assistants itself, not one product's launch. Other blog posts go to the subsection that discusses their topic.
3. A system in the application landscape table goes to its domain under Applications and Bottlenecks; a system in the loop-closure table goes to Levels of Loop Closure.
4. A benchmark in a module's benchmark table goes to that module's Benchmarks and Evaluation Settings.
5. Other works go to the subsection that discusses them, preferring evaluation, then self-evolution, then policy, then space and shared conditions, then coupling.

## Tags

| Tag | Meaning |
|:--|:--|
| `S→A`, `S→M`, `M→A`, `A→S`, `M→S`, `A→M` | The survey discusses the work under that coupling channel |
| `L0` to `L5` | The system's level in the loop-closure table: session local, retained state, state-guided decision, unrequested action, attributed outcomes, governed revision |
| `Product` | A published study of a product from the loop-closure table's product rows |

## Maintenance

- Research entries: newest first, then by title, within each section or sub-category. The lists under Applications and Bottlenecks and Levels of Loop Closure run from the highest loop-closure level down, then newest first; works without a level come last.
- Products: one table per subsection, with a row per company, ordered by product name.
- Sections without entries are omitted from the README.
- Source data: `data/sections.json` (sections in reading order, with the survey's groupings and their tags), `data/research.json`, and `data/products.json`. Framing text: `docs/readme-intro.md` and `docs/readme-footer.md`. `README.md` is generated.
