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

- **[2026/10]** Synced with the latest draft, now titled *Always-On Personal Intelligence: A Roadmap Towards Continuing, Self-Evolving Loops*: **{{WORK_COUNT}} cited works**, the revised memory policy subsections, and the new product rows of the loop-closure table.
- **[2026/10]** The list now follows the survey's structure and terms: its section numbers and titles, and within each module, space, operating conditions, policy, coupling, and evaluation.
- **[2026/09]** The collection became a reading list of the works cited in our survey, with code links where available.

---

<a id="overview"></a>
## Overview

The promise of always-on personal intelligence lies in a **continuing, self-evolving loop**. A continuing loop sustains service and preserves relevant personal state across interactions. Its two properties, **operational continuity** and **state durability**, form the foundation of always-on personal intelligence. Building on it, a **self-evolving loop** revises the assistant using its own operating experience.

> [!IMPORTANT]
> **The survey connects Sensing, Memory, and Action through six directed coupling channels. Shared operating conditions, such as privacy and authority, govern the modules, and an implementation of models and scaffolding realizes them.**

| Channel | What it supplies | Difficulty | Covered in |
|:--:|:--|:--:|:--:|
| **S→A** | Current context, events, and execution state, as the situation to act on and to decide whether, when, and how to act | Basic | [§5](#sec-5) |
| **S→M** | Sensed evidence, as new material to retain and to decide what to admit, integrate, or correct | Moderate | [§4](#sec-4) |
| **M→A** | Retained personal state, as action content and to choose timing, effector, or commitment | Moderate | [§5](#sec-5) |
| **A→S** | Intentions, plans, and execution state, as expected effects to check and to decide what to observe | Moderate | [§3](#sec-3) |
| **M→S** | Retained priors, as background for interpretation and to guide sampling, attention, or compression | High | [§3](#sec-3) |
| **A→M** | Action context, trajectories, outcomes, and feedback, as task history to retain and to decide what to integrate or correct | High | [§4](#sec-4) |

The synthesis finds the thinnest support for two channels: memory guiding sensing (M→S) and action outcomes returning to memory (A→M).

**How to read the list.** Sections and titles follow the survey, and each work appears once, under the section where the survey discusses it. A channel tag such as `M→S` marks a work discussed under that coupling channel. In Section 6, `L0` to `L5` give a system's level in the loop-closure table, and `Product` marks product rows.

<div align="center">
<img src="assets/roadmap.png" width="95%" alt="Overview of the roadmap: the continuing loop, the module chapters, the system-level review, and HALO"/>
<br>
<em><b>Figure 1.</b> Overview of the roadmap. This roadmap is organized into four parts. We first define always-on personal intelligence as a continuing loop that connects Sensing, Memory, and Action through six directed channels (Section 2). We then review each module by its space, conditions, policy, coupling, and evaluation (Sections 3 to 5). Next, we examine integrated systems, their bottlenecks, and their levels of loop closure (Section 6). Finally, we audit existing systems with HALO in read and run modes (Section 7).</em>
</div>
