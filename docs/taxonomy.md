# Scope and structure

This reading list accompanies *Always-On Personal Intelligence: A Roadmap Towards Continuing, Self-Evolving Loops*. It collects the works the survey discusses and arranges them by the survey's chapters, titles, and terms.

## Scope

A continuing loop sustains service and preserves relevant personal state across interactions. Its two properties, operational continuity and state durability, form the foundation of always-on personal intelligence. A self-evolving loop extends it by revising the assistant using its own operating experience. Scheduled and event-driven operation qualify; continuous recording or model execution is not required.

The list includes component methods, benchmarks, and partial systems when the survey uses them as methods or evidence. Inclusion does not mean that a work meets the full always-on definition.

## Structure

The list starts directly with the survey's module chapters and follows its titles and terms. `data/sections.json` records the sections in reading order:

| Section | Parts |
|:--|:--|
| Sensing, Memory, Action | Space, operating conditions, policy, coupling across the loop, and evaluation, with the survey's subsections |
| Applications, System Bottlenecks, and Loop Closure | Applications and bottlenecks by domain, shared conditions and implementation, levels of loop closure, self-evolution in deployed loops |
| Trends and Open Problems | Local policies, coordination, self-evolution and recursive revision, longitudinal evaluation |
| Related Surveys | Capability-focused and concurrent system-level surveys |
| Products & Tools | One line per product the survey discusses, with its official page, by wearable, digital, and physical domain; devices and platforms; a few curated products; and developer tools |

The README's Foundations section summarizes the survey's definitions, coupling channels, and loop-closure levels without a reading list. Works the survey cites only in its Introduction or Foundations, such as textbooks and early visions, are left out, apart from the related surveys and device pages.

## Placement

Research works and products are kept apart. The survey's product sources (official pages, documentation, and blogs) are merged into one record per product, which links only the product's most official page and never a blog post, under its interaction domain. Each research work appears once, under the section where the survey treats it most directly:

1. A related survey discussed in the survey's positioning goes to Related Surveys.
2. A system in the application landscape table goes to its domain under Applications and Bottlenecks; a system in the loop-closure table goes to Levels of Loop Closure.
3. A benchmark in a module's benchmark table goes to that module's Benchmarks and Evaluation Settings.
4. Other works go to the subsection that discusses them, preferring evaluation, then self-evolution, then policy, then space and operating conditions, then coupling.

## Tags

| Tag | Meaning |
|:--|:--|
| Grouping tags such as `Continuous`, `Profile`, `Deferred`, `Recall baselines`, `Wearable` | The survey's own grouping inside a section: what starts observation or action, the kind of memory, a benchmark-table group, or a system's domain |
| `S→A`, `S→M`, `M→A`, `A→S`, `M→S`, `A→M` | The survey discusses the work under that coupling channel |
| `L0` to `L5` | The system's level in the loop-closure table: session local, retained state, state-guided decision, unrequested action, attributed outcomes, governed revision |
| `Product` | A published study of a product from the loop-closure table's product rows |

## Maintenance

- Research entries: newest first, then by title, within each section.
- Products and tools: by group, then by title.
- Sections without entries are omitted from the README.
- Source data: `data/sections.json` (sections in reading order, with the survey's groupings and their tags), `data/research.json`, `data/products.json`, and `data/tools.json`. Framing text: `docs/readme-intro.md` and `docs/readme-footer.md`. `README.md` is generated.
