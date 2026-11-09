<div align="center">

<img src="assets/banner.gif" width="100%" alt="Always-On Personal Intelligence: A Roadmap Towards Continuing, Self-Evolving Loops"/>

<p>
  <a href="https://always-on-intelligence.github.io/Always-On_Personal_Intelligence.pdf"><img src="https://img.shields.io/badge/Paper-PDF-355774?style=for-the-badge&logo=adobeacrobatreader&logoColor=white" alt="Paper (PDF)"/></a>
  <a href="https://always-on-intelligence.github.io/"><img src="https://img.shields.io/badge/Project-Website-66816D?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Project website"/></a>
</p>

<p>
  <a href="https://doi.org/10.20944/preprints202611.0793.v1"><img src="https://img.shields.io/badge/DOI-10.20944%2Fpreprints202611.0793.v1-8B692E?style=flat-square" alt="DOI 10.20944/preprints202611.0793.v1"/></a>
  <a href="https://github.com/Always-On-Intelligence/awesome-always-on-personal-intelligence/stargazers"><img src="https://img.shields.io/github/stars/Always-On-Intelligence/awesome-always-on-personal-intelligence?style=flat-square&logo=github&color=B88465" alt="GitHub stars"/></a>
  <img src="https://img.shields.io/badge/Papers-{{PAPER_COUNT}}-355774?style=flat-square" alt="{{PAPER_COUNT}} papers"/>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-8C8C8C?style=flat-square" alt="MIT License"/></a>
</p>

<sub>Contributions are welcome</sub>

</div>

{{TOC}}

---

<a id="overview"></a>
## Overview

Always-on personal intelligence demands more than episodic, task-driven agents. To remain always-on, it requires a **continuing loop** that sustains assistance between requests, retains personal context, and carries unfinished commitments forward. To grow more personal over time, this loop can also become **self-evolving**, revising how it works based on past experience.

> [!IMPORTANT]
> **The survey organizes always-on personal assistants into three functional modules, Sensing, Memory, and Action, connected by six directed channels that pass information between them. These modules operate under real-world limits, from battery life to privacy and user permissions, and run on models and the scaffolding around them.**

<div align="center">
<img src="assets/roadmap.png" width="95%" alt="Overview of the roadmap: the continuing loop, the module chapters, the system-level review, HALO, and the open problems"/>
<br>
<em><b>Figure 1.</b> Overview of the roadmap. This roadmap is organized into five parts. We first define always-on personal intelligence as a continuing loop that connects Sensing, Memory, and Action through six directed channels. We then review each module by its space, conditions, policy, coupling, and evaluation. Building on these reviews, we examine integrated systems, their bottlenecks, and their levels of loop closure, and audit existing systems with HALO in read and run modes. Finally, we discuss the open problems in always-on personal intelligence.</em>
</div>

**How to read the list.** Sections and titles follow the survey's module chapters, and each work appears once, under the section where the survey discusses it. Long sections are divided into the survey's own sub-categories: the paragraphs of its text, the groups of its benchmark tables, or its open problems, and a work the survey cites sits under the one that cites it. Every work the survey cites is listed: works cited only in its Introduction or Foundations are under [Background](#background), and works added by the daily scan, which the survey does not cite yet, sit where they fit its framework. Each list runs from the newest work to the oldest, except the application and loop-closure lists, which run from the highest loop-closure level (`L5`) down. A channel tag such as `M→S` marks a work discussed under that coupling channel, `L0` to `L5` give a system's level in the loop-closure table, and `Product` marks a published study of a product. Products are listed separately under [Products](#products), one line per product with its official page.

---

<a id="foundations"></a>
## <img src="assets/icons/foundations.svg" height="30" align="top" alt=""/> Foundations

Always-on personal intelligence is personal assistance that maintains two core properties for the same user. **Operational continuity** is the ability to keep operating between explicit requests and to decide when to act or wait. **State durability** is the ability to preserve user-specific state for later use and to carry unresolved commitments across interaction boundaries. The **continuing loop**, the foundation of always-on personal intelligence, provides both properties through the recurring operation of Sensing, Memory, and Action.

Its **self-evolving extension** uses operating experience to make durable revisions to the assistant's **mechanism**, the model weights and the scaffolding that decide how it works, and later steps use the revised mechanism. Storing that the user prefers reminders at their workstation is a state update, while editing the timing rule to wait until they are back there is a revision. A claim of self-evolution that rests on outcome feedback needs a chain of evidence with five steps: record, outcome, attribution, revision, and later use.

Within each module, the survey distinguishes its **space**, what the module can do and represent, from the **local policy** that chooses among these options. Six directed **coupling channels** each carry information from one module to another for the receiving module to use:

| Channel | Information flow | Difficulty | Covered in |
|:--:|:--|:--:|:--:|
| **S→A** | Current context and observed execution state that inform Action's decisions | Basic | [Action](#sec-5) |
| **S→M** | Observations that Memory uses to create or update records | Moderate | [Memory](#sec-4) |
| **M→A** | Retained personal information and pending commitments that inform Action's decisions | Moderate | [Action](#sec-5) |
| **A→S** | Action plans and execution state that guide what Sensing observes and checks | Moderate | [Sensing](#sec-3) |
| **M→S** | Retained information that guides what Sensing observes and how it interprets new observations | High | [Sensing](#sec-3) |
| **A→M** | Action context and immediate results that Memory uses to maintain task history | High | [Memory](#sec-4) |

Difficulty is the survey's qualitative rating. Basic marks the S→A path that every agent system has, and High marks channels whose errors are hard to detect and correct.

Every module and channel works under **shared conditions**, the limits set by the user and the world: privacy, user authority, safety, resource budgets, availability, and uncertainty. Within these limits, each runs on an **implementation**, the models and the scaffolding around them, such as prompts, tools, memory stores, and the harness that runs the loop.

Systems differ in how completely they close this loop. The six levels are cumulative, and L3 is the first always-on level, because from L3 on both properties hold:

| Level | An assistant reaches it when |
|:--:|:--|
| **L0** Session local | It responds within one session and keeps nothing across interactions (the baseline) |
| **L1** Retained state | It carries information across sessions: one session writes a memory that a later session can read |
| **L2** State-guided decision | Its stored records change later decisions about what to sense or how to act, while it still acts only as requested |
| **L3** Unrequested action | It decides for itself whether or when to act without a request, and waiting is one of its choices. Acting at a time or condition the user fixed stays at L2 |
| **L4** Attributed outcomes | It links outcome evidence that arrives after a decision, from the world or the user, to that decision, so that it can check or correct its assistance |
| **L5** Governed revision | It revises its mechanism only within the shared conditions: a control applies them to every revision before it takes effect, and the revisions that pass carry over into later runs |

The survey's synthesis reveals the thinnest support for two channels: Memory guiding Sensing (M→S), and action outcomes returning to Memory (A→M). These gaps motivate two research priorities: keeping sensing open to unexpected change for reliable operation, and attributing outcomes to earlier decisions for self-evolution.
