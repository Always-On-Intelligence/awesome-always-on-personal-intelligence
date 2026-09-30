<div align="center">

<img src="assets/banner.png" width="100%" alt="Always-On Personal AI: A Roadmap Towards Continuing, Self-Evolving Loops"/>

<p>
  <b>A chapter-aligned reading list for always-on personal AI:<br/>
  sensing, memory, action, integrated systems, self-evolution, and evaluation.</b>
</p>

<p>
  <img src="https://img.shields.io/badge/Paper-Coming_Soon-355774?style=for-the-badge&logo=arxiv&logoColor=white" alt="Paper coming soon"/>
  <a href="https://always-on-agent.github.io/"><img src="https://img.shields.io/badge/Project-Website-66816D?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Project website"/></a>
</p>

<p>
  <a href="https://github.com/Always-On-Agent/awesome-always-on-personal-ai/stargazers"><img src="https://img.shields.io/github/stars/Always-On-Agent/awesome-always-on-personal-ai?style=flat-square&logo=github&color=B88465" alt="GitHub stars"/></a>
  <img src="https://img.shields.io/badge/Papers-{{PAPER_COUNT}}-355774?style=flat-square" alt="{{PAPER_COUNT}} papers"/>
  <img src="https://img.shields.io/badge/Last_Update-September_2026-66816D?style=flat-square" alt="Last update September 2026"/>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-8C8C8C?style=flat-square" alt="MIT License"/></a>
</p>

<sub>Continuously updated · Contributions are welcome</sub>

</div>

{{TOC}}

---

<a id="news"></a>
## News

- **[2026/10]** Updated to the latest survey draft: **{{WORK_COUNT}} cited works**, with sections that follow its revised chapter structure.
- **[2026/09]** The collection became a chapter-aligned reading list of the works cited in our survey, with code links where available.
- **[2026/09]** We released the first curated collection with a product directory and developer tools.

---

<a id="introduction"></a>
## Introduction

Personal AI is moving from answering isolated requests toward providing sustained assistance. An always-on assistant keeps working between requests and keeps personal state across interactions, so unfinished commitments carry forward. Our survey organizes this behavior around three functional modules, **Sensing**, **Memory**, and **Action**, and the six directed channels that carry information between them.

> [!IMPORTANT]
> **Always-on personal AI runs a continuing loop: it sustains assistance between requests and retains personal state across interactions. Self-evolution extends this loop by revising the assistant from its own operating experience.**

| Channel | What it supplies | Difficulty |
|:--:|:--|:--:|
| **S→A** | Current context, events, and execution state for deciding whether, when, and how to act | Basic |
| **S→M** | Sensed evidence for deciding what to admit, integrate, or correct | Moderate |
| **M→A** | Retained personal state that shapes action content, timing, and commitments | Moderate |
| **A→S** | Intentions, plans, and execution state whose expected effects must be checked | Moderate |
| **M→S** | Retained priors that guide sampling, attention, compression, and interpretation | High |
| **A→M** | Action context, outcomes, and feedback to retain, integrate, or correct | High |

Evidence is thinnest for the two high-difficulty channels, memory guiding sensing (M→S) and action outcomes returning to memory (A→M). Entries below carry a channel tag where the survey discusses them under that channel.

<div align="center">
<img src="assets/roadmap.png" width="95%" alt="Overview of the roadmap: the continuing loop, the module chapters, the system-level review, and HALO"/>
<br>
<em><b>Figure 1.</b> Overview of the roadmap. Sensing, Memory, and Action are connected by six directed channels under shared conditions. Each module chapter covers space, conditions, policy, coupling, and evaluation, followed by the system-level review and the HALO audit.</em>
</div>
