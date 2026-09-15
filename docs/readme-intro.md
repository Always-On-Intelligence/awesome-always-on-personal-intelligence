<div align="center">

<img src="assets/banner.png" width="100%" alt="Always-On Personal AI: A Roadmap towards a Continuing and Self-Evolving Loop"/>

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![Paper](https://img.shields.io/badge/Paper-Working_Draft-355774)](https://always-on-agent.github.io/assets/always-on-personal-ai.pdf) [![Website](https://img.shields.io/badge/Website-Always--On_Agent-66816d)](https://always-on-agent.github.io/) [![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-b88465)](CONTRIBUTING.md) [![GitHub](https://img.shields.io/badge/GitHub-Repository-355774?logo=github)](https://github.com/Always-On-Agent/awesome-always-on-personal-ai)

A curated collection of research, systems, products, and building blocks for personal AI that stays useful across interactions.

**[Research](#sensing)** &nbsp; · &nbsp; **[Systems](#systems)** &nbsp; · &nbsp; **[Products](#products)** &nbsp; · &nbsp; **[Benchmarks](#evaluation)** &nbsp; · &nbsp; **[Contribute](CONTRIBUTING.md)**

<sub>{{RESEARCH_COUNT}} research resources · {{PRODUCT_COUNT}} products · {{TOOL_COUNT}} developer tools</sub>

</div>

<a id="news"></a>
## News

- **2026-09-15** — Introduced an eight-category collection, a dedicated product directory, and structured contribution guidelines alongside the current survey draft.

<a id="overview"></a>
## What makes personal AI always-on?

**Always-on personal AI sustains assistance between explicit requests and retains usable personal state across interactions.** It can wake on a schedule or a relevant event, carry unfinished commitments forward, and decide when to act, ask, or stay silent. Continuous operation does not require continuous recording or inference.

Our survey organizes this behavior around **Sensing**, **Memory**, and **Action**. Governed **self-evolution** adds a further requirement: using attributed outcomes to propose, validate, and durably commit changes to future behavior.

<p align="center">
  <img src="assets/loop.svg" width="100%" alt="Sensing, Memory, and Action are connected by five directed channels: Sensing to Memory, Memory to Action, Action to Sensing, Memory to Sensing, and Action to Memory. Privacy, resources, uncertainty, and user authority constrain the loop."/>
</p>

<details>
<summary><b>Explore the full survey framework and reading guide</b></summary>

<p align="center"><img src="assets/survey-framework.png" width="100%" alt="Full survey overview: functional modules, integrated systems, loop closure, and HALO oversight."/></p>

- **New to the topic?** Start with [Surveys & Foundations](#surveys), then [Integrated Systems](#systems).
- **Studying a mechanism?** Explore [Sensing](#sensing), [Memory](#memory), and [Action](#action).
- **Building an assistant?** Browse [Tools & Infrastructure](#tools) and [Benchmarks & Datasets](#evaluation).
- **Looking for something to use?** Go directly to [Products](#products).
- **Studying feedback and self-evolution?** Follow the `Self-evolution` tags and the [five-channel guide](docs/taxonomy.md).

This collection includes enabling methods and partial systems as well as continuing assistants. Inclusion does not imply that a work demonstrates every capability of a full always-on loop.

</details>
