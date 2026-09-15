# Product and infrastructure source notes

Checked: **2026-09-15**.

These notes record the primary sources used for the product and tool entries. Product descriptions summarize documented capabilities, not independently measured performance or proof of a complete always-on loop. Availability is qualified by the official page's rollout, platform, and plan wording. No products were purchased or tested for this curation.

The survey's digital-service discussion supplied ChatGPT Pulse, Claude Cowork, Muse, and Windows Recall; its bibliography supplied Ray-Ban Meta and PLAUD NotePin. Omi, screenpipe, OpenClaw, and Lindy extend coverage of wearable memory, desktop history, and continuing personal assistance. Developer infrastructure is maintained separately in `data/tools.json`.

## Products

### Omi

- **Capabilities:** The [official product page](https://www.omi.me/pages/product) describes conversation transcription, generated summaries and tasks, searchable memories, and evening recaps. It also links the [official open-source project](https://github.com/BasedHardware/omi).
- **Availability:** Companion apps are offered for download. The product page offers ordering, while the [homepage](https://www.omi.me/) exposes pre-order and out-of-stock labels. The [shipping guide](https://help.omi.me/en/articles/12017447-omi-device-orders-shipping-what-to-expect) describes order processing with exceptions during pre-order cycles. The catalog therefore says hardware stock varies.
- **Boundary:** Capture must be started; neither uninterrupted capture nor complete autonomous task execution is assumed. Future brain-interface claims are excluded.

### Ray-Ban Meta

- **Capabilities:** The [manufacturer FAQ](https://www.ray-ban.com/uk/c/frequently-asked-questions-ray-ban-meta-smart-glasses) documents visual questions, voice interaction, and creating or reviewing reminders through glasses paired with a phone and Meta AI app.
- **Availability:** The same FAQ lists retail availability in supported countries and limits AI features by country and language. The catalog does not treat hardware availability as equivalent to every AI feature being enabled.
- **Boundary:** Camera-grounded interaction and reminders do not imply continuous visual recording or a persistent autobiographical memory service.

### PLAUD NotePin

- **Capabilities:** The [product page](https://www.plaud.ai/products/plaud-notepin) describes wearable recording and the transcription/summarization app experience. The [recording instructions](https://support.plaud.ai/hc/en-us/articles/50841183397273-Start-recording) specify a physical long press to start or stop an in-person recording, local recording storage, and later transfer to the app.
- **Availability:** A purchasable product page with shipping information was present. Recording is manually started.
- **Boundary:** This entry concerns conversation capture and later recall. It does not claim spontaneous intervention or continuous day-long monitoring. NotePin and NotePin S are distinct devices; this entry is for NotePin.

### Windows Recall

- **Capabilities:** Microsoft's [Recall guide](https://support.microsoft.com/en-US/Windows/Ai/Ai-Features/retrace-your-steps-with-recall) describes searching previous screen activity. Its [privacy and control documentation](https://support.microsoft.com/en-us/windows/privacy/privacy-and-control-over-your-recall-experience) documents opt-in periodic snapshots, local processing/storage, pause, filtering, and deletion controls.
- **Availability:** The privacy documentation explicitly labels Recall a preview exclusive to supported Copilot+ PCs; additional hardware and Windows Hello requirements apply.
- **Boundary:** Recall does not record audio or continuous video. Searchable screen history alone is not proactive assistance.

### screenpipe

- **Capabilities:** The [official site](https://screenpipe.com/) describes screen/audio history that can be searched and provided to connected agents. The [screen-history documentation](https://docs.screenpi.pe/search-screen-history) explains event-driven capture, accessibility text with OCR fallback, local SQLite storage, and search.
- **Availability:** The site offers a desktop download and links the [open-source repository](https://github.com/screenpipe/screenpipe).
- **Boundary:** Raw capture/search is local by default. Optional cloud AI, transcription, sync, or connected workflows may send data elsewhere. The entry does not promise that every AI or automation runs locally.

### Claude Cowork

- **Capabilities:** The [official product page](https://claude.com/product/cowork) describes delegated work across selected folders and tools, unattended recurring tasks, and reviewable results.
- **Availability:** The page provides desktop downloads and says a paid plan is required, with web/mobile rollout wording and mobile beta status. Individual capabilities can have additional plan or administrator controls.
- **Boundary:** This is a vendor description of configured task execution. It is not evidence that the system continuously observes all desktop activity or autonomously completes every task.

### ChatGPT Pulse

- **Capabilities:** OpenAI's [September 25, 2025 announcement](https://openai.com/index/introducing-chatgpt-pulse/) describes nightly research informed by memory, chat history, feedback, and optional connected apps, followed by personalized visual briefings.
- **Availability:** The announcement was accessible at this check and describes a Pro/mobile preview at launch. This source does not establish the current account-level Pulse rollout, so the catalog explicitly marks current access unconfirmed.
- **Related current feature:** The [Scheduled Tasks help article](https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt), updated in August 2026, describes recurring work, monitoring, and supported event triggers with plan and app restrictions. These capabilities should not be silently attributed to Pulse.

### Muse

- **Capabilities:** Meta's [September 8, 2026 launch announcement](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/) describes continued work after the app closes, retained personal context, and user approval for sensitive actions. [How We Designed Muse](https://introducing.muse.ai/) explicitly describes persistent conversational memory, scheduled/event-driven work, and selective notifications.
- **Availability:** The launch announcement says Muse is rolling out in the US on iOS, Android, and the web, and describes WhatsApp messaging. AI-glasses support is future availability and is not listed as shipped.
- **Boundary:** These are product/design claims. No claim of empirically validated self-evolution or complete loop closure is made.

### OpenClaw

- **Capabilities:** The [official FAQ](https://docs.openclaw.ai/help/faq/what-is-openclaw) describes a personal assistant run on user-managed infrastructure with durable memory, messaging access, and reminders. The [heartbeat documentation](https://docs.openclaw.ai/gateway/heartbeat) details periodic agent turns and configuration-dependent notification behavior.
- **Availability:** The [project site](https://openclaw.ai/) and [repository](https://github.com/openclaw/openclaw) provide the software. Setup, model/provider access, connected accounts, and a running host are the user's responsibility.
- **Boundary:** Listed under cloud/messaging assistants because of its interaction surface; it is explicitly self-hosted, not a vendor-hosted subscription assistant. Capabilities depend on configuration.

### Lindy

- **Capabilities:** The [official documentation](https://docs.lindy.ai/) describes inbox triage, meeting preparation, notes, and follow-ups. The [meeting-prep guide](https://docs.lindy.ai/features/meeting-assistant/meeting-prep) explains briefs based on upcoming meetings and prior context.
- **Availability:** The [pricing page](https://www.lindy.ai/pricing) offers paid plans and a trial entry point.
- **Boundary:** The catalog does not repeat marketing claims about hours saved, perfect recall, or universal autonomy. The included scope is connected workplace assistance.

## Tools and infrastructure

These are building blocks. Inclusion means a documented mechanism is relevant to continuing assistance, not that installing a component produces an always-on personal agent.

| Entry | Primary evidence | Relevant mechanism |
| --- | --- | --- |
| Mem0 | [Official introduction](https://docs.mem0.ai/introduction) | Memory persists across sessions, tools, and runs; save/search interfaces and self-hosting are documented. |
| Letta | [Memory and dreaming](https://docs.letta.com/configuration/memory) | Editable persistent memory and background consolidation of prior conversations. The current documentation uses MemFS; earlier API material describes memory blocks. |
| Graphiti | [Official repository](https://github.com/getzep/graphiti), [documentation](https://help.getzep.com/graphiti/getting-started/welcome) | Incremental temporal graphs, fact validity/history, and provenance to source episodes. |
| MemOS | [Official repository](https://github.com/MemTensor/MemOS) | Memory lifecycle APIs, asynchronous ingestion, and correction from feedback. Vendor benchmark numbers are not included in the catalog. |
| LangGraph | [Persistence documentation](https://docs.langchain.com/oss/python/langgraph/persistence) | Checkpoints for resumable execution and stores for cross-thread context. Persistence across process restarts requires a persistent backend. |
| Temporal | [Workflow execution](https://docs.temporal.io/workflow-execution) | Execution history and recoverable workflow state for work that spans failures or long waits. |
| Inngest | [Events and triggers](https://www.inngest.com/docs/features/events-triggers) | Asynchronous functions started by application events, webhooks, and recurring schedules. |
| Composio | [Triggers documentation](https://docs.composio.dev/docs/triggers) | User-account connections and app-event delivery; some providers use polling rather than immediate push. |
| Model Context Protocol | [Official introduction](https://modelcontextprotocol.io/introduction) | Shared interfaces for data sources and tool access. The protocol does not itself supply scheduling, memory, or blanket authorization. |
| Langfuse | [Observability documentation](https://langfuse.com/docs/observability/overview) | Agent traces and evaluation/monitoring signals for inspecting failures and resource use. |

## Maintenance

- Recheck product availability before changing status or adding claims about new features.
- Prefer current support documentation over launch promises for availability. Keep launch-only evidence explicitly dated.
- Attach a primary source to any new claim; use paper entries for research evaluations and these notes for vendor-reported capabilities.
- Record meaningful capability and availability changes, rather than replacing an old claim solely because a homepage was redesigned.
