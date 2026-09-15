# Literature curation notes

Initial literature pass: **2026-09-15**. This is a selected reading list accompanying the survey, rather than a search-complete bibliography.

## Source and scope

The initial candidates came from the companion manuscript's `custom.bib`, `position_refs.bib`, and the discussions in `sec/02_foundations.tex`, `sec/04_sensing.tex`, `sec/05_memory.tex`, `sec/06_action.tex`, `sec/07_integrated_systems.tex`, and `sec/08_halo.tex`. The existing repository README provided a second check for directly relevant entries worth retaining. Candidate bibliography entries were checked against primary paper pages; their presence in a BibTeX file alone did not establish a venue or implementation link.

The list includes enabling components as well as complete assistants. Each description states the contribution at its reported scope. In particular, streaming video understanding, long-term question answering, and successful completion of one task are useful components but do not by themselves demonstrate a continuing personal service.

### Primary homes

- **Surveys & Foundations:** field overviews and a small set of historical or architectural foundations.
- **Sensing:** observation, streaming understanding, and efficient or selective capture.
- **Memory:** retained user state, personalization, memory operations, and experience reuse.
- **Action:** initiative, intervention timing, background preparation, and execution feedback.
- **Integrated Systems:** assistant implementations connecting several components in a concrete service setting.
- **Benchmarks & Datasets:** resources whose primary contribution is evaluation, even when they include a baseline assistant.

One work has one full literature entry. Ego4D, Ego-Exo4D, EgoLife, TeleEgo, LoCoMo, and LongMemEval therefore appear only under evaluation. A paper about a system can coexist with the corresponding maintained product or developer tool when the entries describe different artifacts.

The `commitments` memory subcategory is reserved for substantive methods on pending intentions and task state. It is currently empty: the first pass covers prospective memory through TriggerBench, PM-Bench, and StreamMemBench in evaluation instead of duplicating their entries.

`Self-evolution` marks research on revising reusable guidance or policies through experience, or benchmarks explicitly studying such evolution. Memory organization, personal-content updates, and training a memory policy use more specific tags. The tag does not assign a HALO closure level or certify validated improvement during an always-on deployment. `Longitudinal` can refer to ordered episodes, recorded histories, simulations, or field deployments; descriptions identify the setting where it materially affects interpretation.

## Metadata and link policy

- Titles follow primary sources, with TeX removed, readable Unicode for π / Pro², and obvious spacing errors normalized.
- The year follows the verified publication venue when one is recorded; entries labeled `arXiv` use the first preprint year. A revised preprint does not automatically get the revision year.
- Venue labels come from publisher pages, author copies, or explicit publication information on arXiv. Otherwise the entry remains labeled `arXiv`.
- Paper links point to arXiv, a publisher, or an author/institutional copy. Code, project, and data links are copied from primary sources and kept separate from the paper.
- Links were checked during this pass; availability and product state can change. This note records the initial curation, rather than claiming an ongoing monitoring service.

### Corrections relative to the initial README / bibliography

- ProAgent uses the current title ending in **“in the Wild”**.
- LlamaPIE follows the ACL Anthology title capitalization. The turn-taking study *Large Language Models Know What To Say But Not When To Speak* is **Findings of EMNLP 2024**.
- Memento is labeled **IEEE VRW 2026**; A-MEM **NeurIPS 2025**; LightMem, ReasoningBank, ACE, and ProPerSim **ICLR 2026**, based on primary publication information.
- StreamBridge is labeled **NeurIPS 2025**, Vinci2 **ECCV 2026**, and ProAssist **EMNLP 2025**.
- EgoTrigger and ProMemAssist gained primary paper links. ProAgentBench's complete arXiv identifier is **2602.04482**. WearVox uses the full title ending in **“for Wearables”**.
- LoCoMo uses its actual paper title, *Evaluating Very Long-Term Conversational Memory of LLM Agents*, and names the dataset in the description.
- The Always-On Agents survey's arXiv metadata omits spaces in several places; the display title restores them. AssistantX uses the published IROS title with plural **“Environments”**.

## Deliberately omitted from this initial pass

- General coding, web, and robotics benchmarks such as AgentBench, WebArena, Mind2Web, and Xperience-10M are not used to fill categories. Their broader coverage can be added later with a clear connection to continuing personal assistance.
- General agent exemplars such as Voyager and Generative Agents are deferred to keep the first pass focused. ReAct and CoALA remain explicitly marked as enabling foundations.
- The original README's audio-visual, auto-research, and world-modeling style-reference surveys are omitted where their connection to this repository is mainly organizational.
- Hardware specification pages, vendor announcements, and implementation-only repositories belong in Products or Tools & Infrastructure rather than the paper list.
- Optional code or project links that were not established from a primary source were omitted, rather than inferred from a paper name. No selected paper was retained with an unresolved primary-source URL.

The bibliography contains many more recent candidates. Their omission is a scope choice for the first release, not a judgment about quality or relevance.

## Primary-source ledger

The citation keys below map the public data entries back to the companion manuscript. The linked primary page is the source for the displayed work; additional author or publisher records used for venue verification are listed after the ledger.

| Entry ID | Manuscript citation key | Primary source |
| --- | --- | --- |
| `proactive-dialogue-survey` | `deng2023proactivesurvey` | [Paper](https://arxiv.org/abs/2305.02750) |
| `agent-memory-survey` | `zhang2024memorysurvey` | [Paper](https://arxiv.org/abs/2404.13501) |
| `egocentric-procedural-ai-survey` | `egoproceduralsurvey2025` | [Paper](https://arxiv.org/abs/2511.13261) |
| `always-on-agents-survey` | `alwaysonagents2026` | [Paper](https://arxiv.org/abs/2606.30306) |
| `digital-colleague-survey` | `digitalcolleaguesurvey2026` | [Paper](https://arxiv.org/abs/2606.14502) |
| `coala` | `coala2024` | [Paper](https://arxiv.org/abs/2309.02427) |
| `sensecam` | `sensecam2006` | [Paper](https://www.microsoft.com/en-us/research/publication/sensecam-retrospective-memory-aid/) |
| `mixed-initiative-interfaces` | `horvitz1999mixedinitiative` | [Paper](https://www.microsoft.com/en-us/research/publication/principles-mixed-initiative-user-interfaces/) |
| `chainstream` | `chainstream2024` | [Paper](https://arxiv.org/abs/2412.15240) |
| `omniparser` | `omniparser2024` | [Paper](https://arxiv.org/abs/2408.00203) |
| `videollm-online` | `videollmonline2024` | [Paper](https://arxiv.org/abs/2406.11816) |
| `streaming-vlm` | `streamingvlm2025` | [Paper](https://arxiv.org/abs/2510.09608) |
| `flash-vstream` | `flashvstream2024` | [Paper](https://arxiv.org/abs/2406.08085) |
| `moshi` | `moshi2024` | [Paper](https://arxiv.org/abs/2410.00037) |
| `personal-vad` | `personalvad2020` | [Paper](https://arxiv.org/abs/1908.04284) |
| `egotrigger` | `egotrigger` | [Paper](https://arxiv.org/abs/2508.01915) |
| `wearable-contextual-ai-architecture` | `aria2power` | [Paper](https://arxiv.org/abs/2512.16045) |
| `deepwear` | `deepwear2020` | [Paper](https://arxiv.org/abs/1712.03073) |
| `kirigami` | `kirigami2024` | [Paper](https://mynkgoel.github.io/pdfs/kirigami.pdf) |
| `memgpt` | `memgpt2023` | [Paper](https://arxiv.org/abs/2310.08560) |
| `memorybank` | `memorybank2023` | [Paper](https://arxiv.org/abs/2305.10250) |
| `a-mem` | `amem2025` | [Paper](https://arxiv.org/abs/2502.12110) |
| `mirix` | `mirix` | [Paper](https://arxiv.org/abs/2507.07957) |
| `memos-paper` | `memos` | [Paper](https://arxiv.org/abs/2507.03724) |
| `memory-os` | `memoryos2025` | [Paper](https://arxiv.org/abs/2506.06326) |
| `personalized-agents-human-feedback` | `pahf2026` | [Paper](https://arxiv.org/abs/2602.16173) |
| `user-as-code` | `userascode2026` | [Paper](https://arxiv.org/abs/2606.16707) |
| `lightmem` | `lightmem2025` | [Paper](https://arxiv.org/abs/2510.18866) |
| `memory-r1` | `memoryr1` | [Paper](https://arxiv.org/abs/2508.19828) |
| `reasoning-bank` | `reasoningbank2025` | [Paper](https://arxiv.org/abs/2509.25140) |
| `agentic-context-engineering` | `ace2025` | [Paper](https://arxiv.org/abs/2510.04618) |
| `memprivacy` | `memprivacy2026` | [Paper](https://arxiv.org/abs/2605.09530) |
| `memq` | `memq2026` | [Paper](https://arxiv.org/abs/2605.08374) |
| `jitai-design-principles` | `nahumshani2018jitai` | [Paper](https://academic.oup.com/abm/article/52/6/446/4733473) |
| `when-to-speak` | `umair2024llmwhennottospeak` | [Paper](https://arxiv.org/abs/2410.16044) |
| `proactive-agent` | `luproactiveagent2024` | [Paper](https://arxiv.org/abs/2410.12361) |
| `mmduet` | `mmduet2024` | [Paper](https://arxiv.org/abs/2411.17991) |
| `communication-policy-evolution` | `cpe2026` | [Paper](https://arxiv.org/abs/2606.14314) |
| `proactor` | `proactor2026` | [Paper](https://aclanthology.org/2026.acl-long.832/) |
| `proact` | `proact2026` | [Paper](https://arxiv.org/abs/2605.25971) |
| `ask-before-plan` | `askbeforeplan2024` | [Paper](https://arxiv.org/abs/2406.12639) |
| `know-no` | `knowno2023` | [Paper](https://proceedings.mlr.press/v229/ren23a.html) |
| `code-as-monitor` | `codeasmonitor2025` | [Paper](https://arxiv.org/abs/2412.04455) |
| `react` | `yao2023react` | [Paper](https://arxiv.org/abs/2210.03629) |
| `vinci` | `vinci` | [Paper](https://arxiv.org/abs/2412.21080) |
| `visionclaw` | `visionclaw2026` | [Paper](https://arxiv.org/abs/2604.03486) |
| `ai-for-service` | `ai4service` | [Paper](https://arxiv.org/abs/2510.14359) |
| `promemassist` | `promemassist` | [Paper](https://arxiv.org/abs/2507.21378) |
| `memento-ar` | `mementoar2026` | [Paper](https://arxiv.org/abs/2601.17622) |
| `proagent` | `proagent` | [Paper](https://arxiv.org/abs/2512.06721) |
| `contextagent` | `contextagent` | [Paper](https://arxiv.org/abs/2505.14668) |
| `pro2assist` | `pro2assist2026` | [Paper](https://arxiv.org/abs/2605.04227) |
| `llamapie` | `llamapie` | [Paper](https://aclanthology.org/2025.findings-acl.710/) |
| `socialmind` | `socialmind` | [Paper](https://arxiv.org/abs/2412.04036) |
| `lts-voiceagent` | `ltsvoiceagent2026` | [Paper](https://arxiv.org/abs/2601.19952) |
| `pask` | `pask2026` | [Paper](https://arxiv.org/abs/2604.08000) |
| `pitch-daily-planning` | `lunchnow2025` | [Paper](https://arxiv.org/abs/2509.24073) |
| `propersim` | `propersim` | [Paper](https://arxiv.org/abs/2509.21730) |
| `knowact-guiclaw` | `knowactguiclaw2026` | [Paper](https://arxiv.org/abs/2607.12625) |
| `ouroboros` | `ouroboros2026` | [Paper](https://arxiv.org/abs/2608.08311) |
| `healthclaw` | `healthclaw2026` | [Paper](https://arxiv.org/abs/2607.13940) |
| `assistantx` | `assistantx` | [Paper](https://arxiv.org/abs/2409.17655) |
| `micobot` | `micobot2026` | [Paper](https://arxiv.org/abs/2508.05535) |
| `collaborative-vlas` | `collaborativevla2026` | [Paper](https://arxiv.org/abs/2606.12475) |
| `ego4d` | `ego4d2022` | [Paper](https://arxiv.org/abs/2110.07058) |
| `ego-exo4d` | `egoexo4d2024` | [Paper](https://arxiv.org/abs/2311.18259) |
| `egolife` | `egolife` | [Paper](https://arxiv.org/abs/2503.03803) |
| `teleego` | `teleego2025` | [Paper](https://arxiv.org/abs/2510.23981) |
| `wearvox` | `wearvox2026` | [Paper](https://arxiv.org/abs/2601.02391) |
| `ovo-bench` | `ovobench2025` | [Paper](https://arxiv.org/abs/2501.05510) |
| `locomo` | `locomo2024` | [Paper](https://arxiv.org/abs/2402.17753) |
| `longmemeval` | `longmemeval2024` | [Paper](https://arxiv.org/abs/2410.10813) |
| `memoryagentbench` | `memoryagentbench2025` | [Paper](https://arxiv.org/abs/2507.05257) |
| `memconflict` | `memconflict2026` | [Paper](https://arxiv.org/abs/2605.20926) |
| `op-bench` | `opbench2026` | [Paper](https://arxiv.org/abs/2601.13722) |
| `ipi-bench` | `ipibench2026` | [Paper](https://arxiv.org/abs/2605.27074) |
| `proagentbench` | `proagentbench` | [Paper](https://arxiv.org/abs/2602.04482) |
| `pro2bench` | `pro2bench2026` | [Paper](https://arxiv.org/abs/2606.04970) |
| `triggerbench` | `triggerbench2026` | [Paper](https://arxiv.org/abs/2606.23459) |
| `pm-bench` | `pmbench2026` | [Paper](https://arxiv.org/abs/2607.12385) |
| `pi-bench` | `pibench2026` | [Paper](https://arxiv.org/abs/2605.14678) |
| `sentinelbench` | `sentinelbench2026` | [Paper](https://arxiv.org/abs/2606.05342) |
| `streammembench` | `streammembench2026` | [Paper](https://arxiv.org/abs/2606.14571) |
| `past-bench` | `pastbench2026` | [Paper](https://arxiv.org/abs/2608.04003) |
| `evomembench` | `evomembench2026` | [Paper](https://arxiv.org/abs/2605.18421) |
| `proassist` | `proassist2025` | [Paper](https://arxiv.org/abs/2506.05904) |
| `streambridge` | `streambridge` | [Paper](https://arxiv.org/abs/2505.05467) |
| `vinci2` | `vinci2` | [Paper](https://arxiv.org/abs/2607.11523) |
| `lightmem-ego` | `lightmemego2026` | [Paper](https://arxiv.org/abs/2607.11487) |

### Additional publication records

- [EgoTrigger author preprint](https://arxiv.org/abs/2508.01915) records acceptance as an ISMAR 2025 TVCG paper.
- [ProMemAssist author copy](https://kevinpjk.github.io/assets/pdf/promemassist_uist_2025.pdf) records UIST 2025.
- [SocialMind author copy](https://yanzhenyu.com/assets/pdf/SocialMind-IMWUT25.pdf) records IMWUT, volume 9, issue 1, March 2025.
- [Kirigami author copy](https://mynkgoel.github.io/pdfs/kirigami.pdf) records IMWUT, volume 8, issue 1, March 2024.
- [ProAssist ACL Anthology record](https://aclanthology.org/2025.emnlp-main.605/) records EMNLP 2025.
- [DeepWear author copy](https://saumaypushp.github.io/files/DeepWear.pdf) identifies IEEE TMC, volume 19, issue 2, 2020; the arXiv preprint began in 2017.
- [EgoLife CVPR record](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_EgoLife_Towards_Egocentric_Life_Assistant_CVPR_2025_paper.html) records CVPR 2025.



## Bounded cross-review — 2026-09-15

A second pass checked the README introduction against the manuscript's definition, scanned primary homes and duplicate identities, and revisited the most ambiguous self-evolution labels. It did not repeat the full paper-by-paper literature search.

- **A-MEM:** Replaced `Self-evolution` with `Memory organization`. The [primary abstract](https://arxiv.org/abs/2502.12110) describes revising existing notes, links, and contextual attributes as new memories arrive. This is memory-state evolution; it does not establish governed revision of the operating policy.
- **PAHF:** Replaced its `Self-evolution` tag with `User feedback`. The [primary abstract](https://arxiv.org/abs/2602.16173) describes clarification, preference retrieval, and correction of explicit per-user memory. The catalog now labels that demonstrated personalization mechanism directly.
- **ProAgent:** Replaced its `Self-evolution` tag with `Personalization`. Its [primary abstract](https://arxiv.org/abs/2512.06721) and the manuscript's Sensing discussion describe on-demand perception and persona-conditioned assistance. The existing description already states the retained-persona mechanism without asserting validated policy evolution.
- **Memory-R1:** Replaced `Self-evolution` with `Policy learning`. The [primary abstract](https://arxiv.org/abs/2508.19828) describes fine-tuning a memory manager and answer agent using outcome-driven reinforcement learning. A learned policy is relevant infrastructure but does not by itself demonstrate later autonomous policy revision during service.
- **Ouroboros:** Made the description explicitly say *coding agent*. It remains a scoped example of reviewed runtime revision, as discussed in the manuscript, rather than being presented as a general personal assistant deployment.
- **WearVox:** Kept the year **2025**: its [arXiv submission history](https://arxiv.org/abs/2601.02391) records December 25, 2025 despite the identifier beginning with `2601`.

The README introduction is consistent with the manuscript and required no factual change. No duplicate paper identities or clearly incorrect primary categories were identified in this bounded pass. The research resource count remains **89**; `Self-evolution` labels decreased from **14** to **10**. The remaining tags describe an explicit evolution research topic or evaluation target, not certified full loop closure.
