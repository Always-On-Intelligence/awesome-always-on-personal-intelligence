<div align="center">

# Awesome Always-On Personal AI

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Paper](https://img.shields.io/badge/Paper-Draft-blue.svg)](#)
[![Project](https://img.shields.io/badge/Project-GitHub-4c1.svg)](https://github.com/choiszt/awesome-always-on-personal-ai)
[![GitHub stars](https://img.shields.io/github/stars/choiszt/awesome-always-on-personal-ai?style=social)](https://github.com/choiszt/awesome-always-on-personal-ai/stargazers)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/choiszt/awesome-always-on-personal-ai/pulls)

**Always-On Personal AI: A Survey of Streaming Context, Persistent Memory, and Adaptive Action**

</div>

This repository accompanies the survey draft and tracks papers, systems, datasets, benchmarks, and infrastructure for always-on personal AI: assistants that continuously observe context, maintain personal memory, decide when to wait or respond, and act through digital or embodied tools.

## Taxonomy

- [Background and Surveys](#background-and-surveys)
- [Streaming Context and Egocentric Perception](#streaming-context-and-egocentric-perception)
- [Personal Memory and User Modeling](#personal-memory-and-user-modeling)
- [Proactive Interaction and Decision Gating](#proactive-interaction-and-decision-gating)
- [Agentic Action: Tools, GUI, Web, and Embodied Agents](#agentic-action-tools-gui-web-and-embodied-agents)
- [World Models and Anticipation](#world-models-and-anticipation)
- [Outcome Feedback and Self-Improvement](#outcome-feedback-and-self-improvement)
- [Benchmarks and Datasets](#benchmarks-and-datasets)
- [Open-Source Systems and Infrastructure](#open-source-systems-and-infrastructure)
- [Safety, Privacy, and Governance](#safety-privacy-and-governance)

## Channel Tags

- `write`: observations become durable memory
- `gating`: memory changes answer/remind/wait/action choices
- `anticipation`: action changes what the system senses next
- `memory-prior`: memory guides sensing before extraction
- `outcome-feedback`: delayed outcomes change future memory or policy updates

## Entry Format

```text
- [Title](paper-link) (Venue/Year) [[code](code-link)] [[data](data-link)]
  - Tags: stage, channel, modality, environment, horizon
  - Relevance: one sentence explaining why this belongs in the survey.
```

## Background and Surveys

- [Audio-Visual Intelligence in Large Foundation Models](https://arxiv.org/abs/2605.04045)
  - Tags: survey, multimodal, audio-visual, foundation-models
  - Relevance: Broad survey style for organizing multimodal perception and benchmarks.
- [AI for Auto-Research: Roadmap & User Guide](https://arxiv.org/abs/2605.18661)
  - Tags: survey, agentic-workflows, research-agents, lifecycle
  - Relevance: Useful template for lifecycle-style organization and resource curation.
- [Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond](https://arxiv.org/abs/2604.22748)
  - Tags: survey, world-models, agents, anticipation
  - Relevance: Frames agents through prediction, simulation, and self-revision.
- [A Survey on Proactive Dialogue Systems: Problems, Methods, and Prospects](https://arxiv.org/abs/2305.02750) (IJCAI 2023)
  - Tags: survey, proactive-dialogue, decision-gating
  - Relevance: Core survey for proactive conversational agents and system-initiated interaction.
- [A Survey on the Memory Mechanism of Large Language Model-based Agents](https://arxiv.org/abs/2404.13501)
  - Tags: survey, memory, LLM-agents
  - Relevance: Surveys memory design, evaluation, and applications for LLM agents.
- [LLM Agent Memory: A Survey from a Unified Representation--Management Perspective](https://openreview.net/forum?id=KPs1EgGKcT)
  - Tags: survey, memory-representation, memory-management
  - Relevance: Organizes memory systems around representation and lifecycle management.
- [GUI Agents: A Survey](https://aclanthology.org/2025.findings-acl.1158.pdf)
  - Tags: survey, GUI-agents, multimodal-agents
  - Relevance: Surveys agents that operate graphical interfaces across web, desktop, and mobile.

## Streaming Context and Egocentric Perception

- [Ego4D: Around the World in 3,000 Hours of Egocentric Video](https://arxiv.org/abs/2110.07058) (CVPR 2022)
  - Tags: dataset, egocentric-video, streaming-context, episodic-memory, forecasting
  - Relevance: Large-scale first-person video benchmark covering past memory, present understanding, and future prediction.
- [Ego-Exo4D: Understanding Skilled Human Activity from First- and Third-Person Perspectives](https://arxiv.org/abs/2311.18259)
  - Tags: dataset, egocentric-video, exocentric-video, multimodal, skilled-activity
  - Relevance: Multiview, multimodal dataset for skilled activity understanding and cross-view reasoning.
- [TeleEgo: Benchmarking Egocentric AI Assistants in the Wild](https://teleai-uagi.github.io/TeleEgo/)
  - Tags: benchmark, egocentric-assistants, live-in-the-wild, long-term-memory
  - Relevance: Evaluates real-time correctness and memory persistence for egocentric AI assistants.
- [WearVox: An Egocentric Multichannel Voice Assistant Benchmark](https://arxiv.org/abs/2601.02391)
  - Tags: benchmark, wearable-audio, voice-assistant, smart-glasses
  - Relevance: Targets voice interaction under wearable, egocentric audio conditions.

## Personal Memory and User Modeling

- [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) (UIST 2023)
  - Tags: memory, reflection, planning, social-agents
  - Relevance: Classic memory-reflection-planning architecture for agents with persistent experience records.
- [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560)
  - Tags: memory, virtual-context, agent-runtime
  - Relevance: Introduces OS-inspired memory tiers and control flow for long-context agent operation.
- [Memory Matters: The Need to Improve Long-Term Memory in LLM-Agents](https://ojs.aaai.org/index.php/AAAI-SS/article/view/27688)
  - Tags: position, long-term-memory, LLM-agents
  - Relevance: Motivates long-term memory as a central missing component for autonomous agents.
- [Position: Episodic Memory is the Missing Piece for Long-Term LLM Agents](https://arxiv.org/abs/2502.06975)
  - Tags: position, episodic-memory, long-term-agents
  - Relevance: Argues for episodic memory properties as a foundation for long-horizon agents.
- [How Memory Management Impacts LLM Agents: An Empirical Study of Experience-Following Behavior](https://arxiv.org/abs/2505.16067)
  - Tags: evaluation, memory-management, agent-behavior
  - Relevance: Studies how memory design choices affect long-term agent behavior.
- [Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents](https://arxiv.org/abs/2601.01885)
  - Tags: memory-management, tool-use, self-improvement
  - Relevance: Treats memory operations as agent actions: store, retrieve, update, summarize, and discard.

## Proactive Interaction and Decision Gating

- [A Survey on Proactive Dialogue Systems: Problems, Methods, and Prospects](https://arxiv.org/abs/2305.02750) (IJCAI 2023)
  - Tags: proactive-dialogue, system-initiative, decision-gating
  - Relevance: Baseline reference for dialogue systems that lead conversation toward system-side goals.
- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366)
  - Tags: feedback, reflection, agent-learning
  - Relevance: Uses verbal feedback to update future behavior across trials.
- [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://arxiv.org/abs/2310.11511)
  - Tags: retrieval-gating, self-reflection, critique
  - Relevance: Useful for thinking about when agents should retrieve evidence and critique outputs.
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
  - Tags: reasoning, acting, tool-use
  - Relevance: Canonical reasoning-action interleaving pattern for LLM agents.

## Agentic Action: Tools, GUI, Web, and Embodied Agents

- [WebArena: A Realistic Web Environment for Building Autonomous Agents](https://arxiv.org/abs/2307.13854)
  - Tags: benchmark, web-agents, tool-use, long-horizon
  - Relevance: Self-hosted web benchmark for realistic web task completion.
- [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://arxiv.org/abs/2404.07972)
  - Tags: benchmark, GUI-agents, desktop-agents, multimodal-agents
  - Relevance: Evaluates agents on real computer tasks across operating systems and applications.
- [Mind2Web: Towards a Generalist Agent for the Web](https://arxiv.org/abs/2306.06070)
  - Tags: benchmark, web-navigation, grounding
  - Relevance: Large-scale web navigation dataset for grounding user goals into website actions.
- [AgentBench: Evaluating LLMs as Agents](https://arxiv.org/abs/2308.03688)
  - Tags: benchmark, LLM-agents, multi-environment
  - Relevance: Early multi-environment benchmark for evaluating LLM agent capabilities.
- [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291)
  - Tags: embodied-agent, lifelong-learning, skill-library
  - Relevance: Demonstrates open-ended skill acquisition and persistent action knowledge in Minecraft.

## World Models and Anticipation

- [Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond](https://arxiv.org/abs/2604.22748)
  - Tags: survey, world-models, anticipation, self-revision
  - Relevance: Anchor reference for prediction and simulation as agent capabilities.
- [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291)
  - Tags: embodied-agent, exploration, skill-memory
  - Relevance: Connects action, exploration, and accumulated skills over long horizons.
- [Ego4D: Around the World in 3,000 Hours of Egocentric Video](https://arxiv.org/abs/2110.07058)
  - Tags: egocentric-video, forecasting, episodic-memory
  - Relevance: Includes future forecasting tasks that align with anticipation in always-on assistants.

## Outcome Feedback and Self-Improvement

- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366)
  - Tags: reflection, feedback, self-improvement
  - Relevance: Turns task feedback into verbal memory for future attempts.
- [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442)
  - Tags: reflection, memory-consolidation, planning
  - Relevance: Uses reflection over stored experience to affect later plans.
- [Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents](https://arxiv.org/abs/2601.01885)
  - Tags: memory-actions, feedback, long-horizon
  - Relevance: Learns when to store, retrieve, update, summarize, and discard memories.

## Benchmarks and Datasets

- [Ego4D](https://ego4d-data.org/)
  - Tags: dataset, benchmark, egocentric-video, multimodal
  - Relevance: Daily-life first-person video benchmark suite.
- [Ego-Exo4D](https://ego-exo4d-data.org/)
  - Tags: dataset, benchmark, egocentric-video, exocentric-video, skilled-activity
  - Relevance: Paired first-person and third-person video for skilled human activities.
- [TeleEgo](https://teleai-uagi.github.io/TeleEgo/)
  - Tags: benchmark, egocentric-assistant, memory-persistence
  - Relevance: Live-in-the-wild personal assistant benchmark.
- [WebArena](https://webarena.dev/)
  - Tags: benchmark, web-agents, reproducible-environment
  - Relevance: Realistic self-hosted web environments and tasks.
- [OSWorld](https://os-world.github.io/)
  - Tags: benchmark, desktop-agents, multimodal-agents
  - Relevance: Open-ended computer-use tasks with execution-based evaluation.
- [Xperience-10M](https://huggingface.co/datasets/ropedia-ai/xperience-10m)
  - Tags: dataset, robotics, egocentric-video, action
  - Relevance: Large-scale robot experience dataset relevant to always-on perception-action systems.

## Open-Source Systems and Infrastructure

- [Letta](https://github.com/letta-ai/letta)
  - Tags: memory-runtime, agents, infrastructure
  - Relevance: Open-source agent framework evolved from MemGPT.
- [mem0](https://github.com/mem0ai/mem0)
  - Tags: memory-infrastructure, personalization, agents
  - Relevance: Practical memory layer for personalized AI applications.
- [Zep](https://github.com/getzep/zep)
  - Tags: memory-infrastructure, knowledge-graph, agents
  - Relevance: Long-term memory service for agent and chatbot applications.
- [Graphiti](https://github.com/getzep/graphiti)
  - Tags: memory-infrastructure, temporal-knowledge-graph
  - Relevance: Temporal graph memory for dynamic agent state.
- [OpenHands](https://github.com/All-Hands-AI/OpenHands)
  - Tags: software-agents, tool-use, coding
  - Relevance: Open-source agent platform for software engineering tasks.

## Safety, Privacy, and Governance

- [Ego4D Privacy and Ethics](https://ego4d-data.org/docs/privacy/)
  - Tags: privacy, egocentric-data, de-identification
  - Relevance: Reference point for privacy handling in large-scale first-person data collection.
- [OSWorld](https://os-world.github.io/)
  - Tags: evaluation, sandboxing, execution-based-evaluation
  - Relevance: Illustrates controlled environments for evaluating computer-use agents.
- [Awesome AI Auto-Research](https://github.com/worldbench/awesome-ai-auto-research)
  - Tags: awesome-list, research-agents, resource-curation
  - Relevance: Reference style for organizing a broad agentic research resource.
- [Awesome Agentic World Modeling](https://github.com/matrix-agent/awesome-agentic-world-modeling)
  - Tags: awesome-list, world-models, agents
  - Relevance: Reference style for a taxonomy-driven awesome repository.
