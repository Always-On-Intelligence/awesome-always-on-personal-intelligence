# Scope and taxonomy

This reading list accompanies *Always-On Personal AI: A Roadmap towards a Continuing and Self-Evolving Loop*. Its navigation follows the survey's Sensing–Memory–Action framework while giving systems, evaluations, products, and developer infrastructure distinct entry points.

## Inclusion

An always-on personal assistant provides opportunities for assistance **between explicit requests** and carries **usable personal state across interactions**. Scheduled and event-driven operation qualify; uninterrupted recording or model execution is not required.

We include three kinds of relevance:

1. **Continuing personal assistance:** systems that connect ongoing service with retained personal state.
2. **Enabling methods:** a concrete contribution to continuing sensing, personal memory, intervention timing, task resumption, outcome feedback, or governed updates. The description must name that contribution.
3. **Evaluation and implementation resources:** benchmarks, datasets, products, and tools that make these capabilities observable or practical.

Long context, a long individual task, generic RAG, a one-off tool call, or a product's use of the word “agent” is insufficient by itself. Broad agent research is included selectively where its relevance can be stated concretely. A study can be relevant without establishing a full always-on loop.

## Primary homes

| Category | Primary contribution |
|:--|:--|
| Surveys & Foundations | Orientation, concepts, and foundational personal-assistance architectures |
| Sensing & Context Awareness | Context acquisition, streaming understanding, adaptive observation |
| Memory & Personalization | Durable personal state, user models, commitments, memory lifecycle |
| Proactive Action & Continuous Execution | Initiative, timing, task continuation, execution, and feedback |
| Integrated Systems & Applications | An assistant architecture studied in a concrete service setting |
| Benchmarks & Datasets | A dataset, benchmark, evaluation environment, or assessment protocol |
| Products | A maintained interface for end users, including clearly labeled previews |
| Tools & Infrastructure | Reusable components for developers |

Use one primary home per work. A benchmark paper belongs in Evaluation even when it contributes to memory or sensing. A method's implementation belongs in its paper's links. A separately maintained developer library or end-user product may have a distinct resource record with a different description and purpose.

Systems use the paper's four application families. Products use their principal delivery form: wearable/ambient device, desktop/mobile interface, or hosted/messaging interface. A multi-surface product appears once under its principal use; the form-factor field records additional supported surfaces.

## Cross-cutting themes

Use at most two useful tags per entry. Themes such as `Self-evolution`, `Privacy`, `User control`, `Wearable`, `Digital`, and `Physical` can cross category boundaries. Open-source availability is expressed through a code link; it is not a separate class of research evidence.

**Self-evolution** concerns feedback-derived changes to future behavior. Where a paper demonstrates only part of this process, say so. Storing a preference, running one reflection, or showing an unvalidated code edit does not establish the survey's full governed self-evolution requirements.

## Five coupling channels

| Channel | What crosses the boundary |
|:--|:--|
| S → M | Observations become durable memory |
| M → A | Retained context informs intervention or execution |
| A → S | Actions or unresolved outcomes change subsequent observation |
| M → S | Memory guides what to observe or how to interpret it |
| A → M | Attributed outcomes inform memory or persistent policy revision |

These channels describe dependencies across categories. A source may support one connection and leave the others untested.

## Levels and evidence

The paper's cumulative levels distinguish durable state (L1), state-informed decisions (L2), continuing operation (L3), outcome feedback (L4), and governed policy revision (L5), above the session-local reference baseline (L0).

We do not automatically assign these levels to repository entries. A level requires evidence for the relevant configuration, not a marketing claim or a system name. Product documentation describes features; research papers may report experiments; code exposes mechanisms. These sources answer different questions.

HALO is the survey's assessment protocol. The survey uses its read mode to inspect existing configurations; its run mode specifies scoped execution and outcome assessment. The repository does not present that protocol as a newly measured leaderboard.

## Ordering and maintenance

- Research entries: descending year, then title within each subcategory.
- Products and tools: alphabetical within each subcategory.
- Product availability: official source, bounded status, and a last-checked date.
- Empty subcategories: omitted until there is real material to include.
- Source data: `data/research.json`, `data/products.json`, and `data/tools.json`.
- Generated presentation: `README.md`; editable framing: `docs/readme-intro.md` and `docs/readme-footer.md`.
