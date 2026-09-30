# Scope and structure

This reading list accompanies *Always-On Personal AI: A Roadmap Towards Continuing, Self-Evolving Loops*. It collects the works cited in the survey and arranges them by the survey's own sections, numbers, and titles.

## Scope

A continuing loop sustains service and preserves relevant personal state across interactions. Its two properties, operational continuity and state durability, form the foundation of always-on personal AI. A self-evolving loop extends it by revising the assistant using its own operating experience. Scheduled and event-driven operation qualify; continuous recording or model execution is not required.

The list includes component methods, benchmarks, and partial systems when the survey uses them as methods or evidence. Inclusion does not mean that a work meets the full always-on definition.

## Structure

`data/sections.json` mirrors the survey's numbered sections:

| Section | Parts |
|:--|:--|
| 1 Introduction | Positioning and Related Surveys |
| 2 Definitions and Foundations | Continuing and self-evolving loops, functional modules, coupling channels, operating conditions, operating regimes, mapping the literature |
| 3 Sensing, 4 Memory, 5 Action | Space, operating conditions, policy, coupling across the loop, and evaluation, with the survey's subsections |
| 6 Applications, System Bottlenecks, and Loop Closure | Applications and bottlenecks by domain, shared conditions and implementation, levels of loop closure, self-evolution in deployed loops |
| 7 HALO | Read mode, run mode, limitations |
| 8 Trends and Open Problems | Local policies, coordination, self-evolution and recursive revision, longitudinal evaluation |

Products & Tools follows as a curated addition; it is not part of the survey.

Inside a section, entries can carry the survey's own grouping: the paragraphs of the space subsections (continuous, triggered, and on-demand sensing; retrospective, profile, and prospective memory; reactive, deferred, and proactive action), the questions of the operating-conditions subsections, the groups of the benchmark tables, and the domain rows of the loop-closure table.

## Placement

Each work appears once, under the section where the survey treats it most directly:

1. A related survey discussed in Section 1.1 stays there.
2. A system in the application landscape table goes to its domain in Section 6.1; a system in the loop-closure table goes to Section 6.3.
3. A benchmark in a module's benchmark table goes to that module's Benchmarks and Evaluation Settings.
4. Other works go to the subsection that discusses them, preferring evaluation, then self-evolution, then policy, then space and operating conditions, then coupling, then the remaining chapters.

## Tags

| Tag | Meaning |
|:--|:--|
| `S→A`, `S→M`, `M→A`, `A→S`, `M→S`, `A→M` | The survey discusses the work under that coupling channel |
| `L0` to `L5` | The system's level in the loop-closure table: session local, retained state, state-guided decision, unrequested action, attributed outcomes, governed revision |
| `Product` | A product row of the loop-closure table |

## Maintenance

- Research entries: newest first, then by title, within each section or group.
- Products and tools: by group, then by title.
- Sections without entries are omitted from the README.
- Source data: `data/sections.json`, `data/research.json`, `data/products.json`, and `data/tools.json`. Framing text: `docs/readme-intro.md` and `docs/readme-footer.md`. `README.md` is generated.
