# Scope and taxonomy

This reading list accompanies *Always-On Personal AI: A Roadmap Towards Continuing, Self-Evolving Loops*. It collects the works cited in the survey and arranges them by the survey's chapters.

## Scope

An always-on personal assistant sustains assistance **between explicit requests** and retains **usable personal state across interactions**. Scheduled and event-driven operation qualify; continuous recording or model execution is not required. Self-evolution extends this continuing loop by revising the assistant from its own operating experience.

The list includes component methods, benchmarks, and partial systems when they supply relevant methods or evidence. Inclusion does not mean that a work meets the full always-on definition.

## Sections

| Section | What it collects | Survey chapter |
|:--|:--|:--|
| Surveys & Foundations | Related surveys, early visions of personal assistance, and classic foundations | Introduction, Foundations |
| Sensing | What starts observation, operating conditions, and sensing policy: triggering, windows, segmentation, compression, placement, routing | Sensing |
| Memory | What persists (retrospective, profile, prospective), and how memory is admitted, retrieved, consolidated, corrected, and retired | Memory |
| Action | What starts an action, whether and when to act, control depth, interfaces, and authority | Action |
| Always-On Systems & Applications | Integrated systems and product sources, grouped by wearable, digital, and physical domains | Applications and Loop Closure |
| Self-Evolution | Revisions from operating experience, their validation, and their risks | Applications and Loop Closure, Trends |
| Benchmarks & Evaluation | Module benchmarks and long-term or deployment evaluation | Evaluation sections, Trends |
| Products & Tools | Products, hardware platforms, and developer infrastructure | Mapping the Literature and curated additions |

Each work has one home. A benchmark sits under Benchmarks even when it studies memory or sensing, and a system from the application tables sits under Systems. Methods sit in the module subsection where the survey discusses them. The `Product` tag marks product documentation and product studies inside Systems.

## Six channels

| Channel | What it supplies | Difficulty | Covered in |
|:--:|:--|:--:|:--|
| S→A | Current context, events, and execution state for deciding whether, when, and how to act | Basic | Action |
| S→M | Sensed evidence for deciding what to admit, integrate, or correct | Moderate | Memory |
| M→A | Retained personal state that shapes action content, timing, and commitments | Moderate | Action |
| A→S | Intentions, plans, and execution state whose expected effects must be checked | Moderate | Sensing |
| M→S | Retained priors that guide sampling, attention, compression, and interpretation | High | Sensing |
| A→M | Action context, outcomes, and feedback to retain, integrate, or correct | High | Memory |

A channel tag marks a work that the survey discusses under that channel, such as a row of a coupling table or an application table. A work can support one channel and leave the others untested.

## Levels and evidence

The survey's loop-closure levels run from session-local response (L0) through retained state (L1), state-guided decisions (L2), unrequested action (L3), and attributed outcomes (L4) to governed revision (L5). L3 is where a service becomes always-on. The list does not assign these levels to entries; a level needs evidence for a specific configuration, which the survey's tables and HALO review provide.

## Ordering and maintenance

- Research entries: newest first, then by title, within each subsection.
- Products and tools: by group, then by title.
- Empty subsections are omitted.
- Source data: `data/research.json`, `data/products.json`, and `data/tools.json`. Framing text: `docs/readme-intro.md` and `docs/readme-footer.md`. `README.md` is generated.
