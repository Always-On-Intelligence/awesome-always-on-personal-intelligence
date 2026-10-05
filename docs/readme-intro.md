<div align="center">

<img src="assets/banner.png" width="100%" alt="Always-On Personal Intelligence: A Roadmap Towards Continuing, Self-Evolving Loops"/>

<p>
  <b>The reading list of <i>Always-On Personal Intelligence: A Roadmap Towards Continuing, Self-Evolving Loops</i>,<br/>
  arranged by the survey's own sections.</b>
</p>

<p>
  <img src="https://img.shields.io/badge/Paper-Coming_Soon-355774?style=for-the-badge&logo=arxiv&logoColor=white" alt="Paper coming soon"/>
  <a href="https://always-on-intelligence.github.io/"><img src="https://img.shields.io/badge/Project-Website-66816D?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Project website"/></a>
</p>

<p>
  <a href="https://github.com/Always-On-Intelligence/awesome-always-on-personal-intelligence/stargazers"><img src="https://img.shields.io/github/stars/Always-On-Intelligence/awesome-always-on-personal-intelligence?style=flat-square&logo=github&color=B88465" alt="GitHub stars"/></a>
  <img src="https://img.shields.io/badge/Papers-{{PAPER_COUNT}}-355774?style=flat-square" alt="{{PAPER_COUNT}} papers"/>
  <img src="https://img.shields.io/badge/Last_Update-October_2026-66816D?style=flat-square" alt="Last update October 2026"/>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-8C8C8C?style=flat-square" alt="MIT License"/></a>
</p>

<sub>Continuously updated · Contributions are welcome</sub>

</div>

{{TOC}}

---

<a id="news"></a>
## News

- **[2026/10]** Products now have one line each, linking the official product page instead of documentation or blog posts: **{{PRODUCT_COUNT}} products**, kept apart from the research works and grouped by wearable, digital, and physical domain.
- **[2026/10]** The list starts directly with the modules, without section numbers. Each list runs from the newest work to the oldest, related surveys sit near the end, and background works such as textbooks are left out.
- **[2026/10]** Synced with the latest draft, now titled *Always-On Personal Intelligence: A Roadmap Towards Continuing, Self-Evolving Loops*: **{{WORK_COUNT}} research works**, the revised memory policy subsections, and the new product rows of the loop-closure table.
- **[2026/10]** The list follows the survey's chapters, titles, and terms: within each module, space, operating conditions, policy, coupling, and evaluation.
- **[2026/09]** The collection became a reading list of the works cited in our survey, with code links where available.

---

<a id="overview"></a>
## Overview

The promise of always-on personal intelligence lies in a **continuing, self-evolving loop**. It must sustain assistance between requests, retain personal context, and carry unfinished commitments forward. Self-evolution extends the continuing loop through self-revisions from operating experience.

> [!IMPORTANT]
> **The survey connects Sensing, Memory, and Action through six directed coupling channels. These modules operate under real-world conditions, such as privacy and authority, and are realized by an implementation of models and scaffolding.**

<div align="center">
<img src="assets/roadmap.png" width="95%" alt="Overview of the roadmap: the continuing loop, the module chapters, the system-level review, and HALO"/>
<br>
<em><b>Figure 1.</b> Overview of the roadmap. We first define always-on personal intelligence as a continuing loop that connects Sensing, Memory, and Action through six directed channels. We then review each module by its space, conditions, policy, coupling, and evaluation. Next, we examine integrated systems, their bottlenecks, and their levels of loop closure. Finally, we audit existing systems with HALO in read and run modes.</em>
</div>

**How to read the list.** Sections and titles follow the survey's module chapters, and each work appears once, under the section where the survey discusses it. Each list runs from the newest work to the oldest. Tags show the survey's own groupings: what starts observation or action, which kind of memory, a benchmark group, or a system's domain. A channel tag such as `M→S` marks a work discussed under that coupling channel, `L0` to `L5` give a system's level in the loop-closure table, and `Product` marks a published study of a product. Products are listed separately under [Products & Tools](#products), one line per product with its official page.

---

<a id="foundations"></a>
## <img src="assets/icons/foundations.svg" height="30" align="top" alt=""/> Foundations

A **continuing loop** sustains service and preserves relevant personal state across interactions. Its two properties, **operational continuity** and **state durability**, form the foundation of always-on personal intelligence. A **self-evolving loop** builds on it and revises the assistant using its own operating experience. Within each module, the survey distinguishes its **space**, the information and capabilities available to it, from the **local policy** that selects and uses them. Six directed **coupling channels** carry information between the modules:

| Channel | What it supplies | Difficulty | Covered in |
|:--:|:--|:--:|:--:|
| **S→A** | Current context, events, and execution state, as the situation to act on and to decide whether, when, and how to act | Basic | [Action](#sec-5) |
| **S→M** | Sensed evidence, as new material to retain and to decide what to admit, integrate, or correct | Moderate | [Memory](#sec-4) |
| **M→A** | Retained personal state, as action content and to choose timing, effector, or commitment | Moderate | [Action](#sec-5) |
| **A→S** | Intentions, plans, and execution state, as expected effects to check and to decide what to observe | Moderate | [Sensing](#sec-3) |
| **M→S** | Retained priors, as background for interpretation and to guide sampling, attention, or compression | High | [Sensing](#sec-3) |
| **A→M** | Action context, trajectories, outcomes, and feedback, as task history to retain and to decide what to integrate or correct | High | [Memory](#sec-4) |

Systems differ in how much of the loop they close. Each level keeps the capabilities of the levels below it:

| Level | A service reaches it when |
|:--:|:--|
| **L0** Session local | It serves within one session, without retention across interactions (the reference baseline) |
| **L1** Retained state | Information from one interaction is still available in a separate, later interaction |
| **L2** State-guided decision | A stored record changes a later Sensing or Action decision |
| **L3** Unrequested action | It decides for itself whether or when to act at a step that no request starts, and waiting counts as an outcome |
| **L4** Attributed outcomes | Outcome evidence from outside a decision is linked to that decision and used to check or correct assistance |
| **L5** Governed revision | Its revisions persist into later runs, and the shared conditions are applied to every revision path before a revision takes effect |

The synthesis finds the thinnest support for two channels: memory guiding sensing (M→S) and action outcomes returning to memory (A→M).
