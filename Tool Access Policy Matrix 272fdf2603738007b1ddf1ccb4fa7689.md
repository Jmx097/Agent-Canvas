# Tool Access/Policy Matrix

Category: Core

At the time of this program going live, there are dozens of approaches to this. Typically, the lower your budget for monthly operating costs, the higher the technical know-how needed.

# Core Stack: n8n • Fellou.ai • Kafka/Brainbase

Any of these three can hold as the “spine” of your automation stack. There’s a CSV below with other tools that can be used.

For this program, the roadmaps are all with https://fellou.ai/ since it is the most novel tool without any tutorials on the market.

. https://n8n.io/ & https://make.com/ tutorials will be available through automation specialists I’ve had the pleasure of working closely with over the years, there’s many mastery classes on no code development, and over time, updated templates will be added to support using it here.

Each approach does come with its own set of pros and cons.

https://brainbaselabs.com/ is one full production suite for Agentic Browsing that comes out the box with a full GUI and onboarding experience, which the other tools all lack.

We also have proprietary access to research-based AI digital employees that are in full production with various private legal and real estate firms through https://whyt.io/, which are under development simply because they’re too powerful to mass-distribute. 

If you want to fast track through everything for the most, reach out and we can demo digital organization charts that make sense for you.

---

## n8n — Orchestrator & Proof Engine

**What it is:** Visual workflow builder that makes the bones of your system visible. Great for mapping the real steps, wiring APIs, and proving idempotent flows fast.

**Why it matters here:** It’s where you make the tech think in steps. Perfect for *conceptualizing the tech working* and shipping baseline wins before any agentic flair.

**Best for**

- Deterministic flows (intake → validate → transform → write-back)
- Idempotency, retries/backoff, dead-letter tabs
- Telemetry (run-log rows: run_id, path, step, status, tokens, cost, ms)

**Pros**

- Free/self-hostable; visual; easy to review in coaching/labs
- Strong for QA, fallback lanes, and incident hygiene
- Low risk: deterministic first, agent overlay later

**Cons / Risks**

- Requires discipline: env-keys, run-log schema, error handling
- Long, messy canvases without naming/versioning standards

**Policy & Access**

- Scope least-privilege API tokens; rotate quarterly
- **Required:** run-logging ON, HIL gate upstream/downstream, rollback playbook
- Budget: per-flow cost caps and step limits documented in Config

**Where to learn:**
https://www.skool.com/the-ai-entrepreneur-circle-5658/about?ref=44c264a6664e4f4c9e5bd6b756d4d956

https://www.skool.com/ai-automation-incubator/about?ref=44c264a6664e4f4c9e5bd6b756d4d956

https://www.skool.com/makerschool/about?ref=44c264a6664e4f4c9e5bd6b756d4d956

---

## Fellou.ai — Agentic Browser Workbench (Non-Technical)

**What it is:** A governed browser-agent lab that lets non-technical users try agentic patterns safely. We’re on the **$200/mo** plan.

**Why it matters here:** Lets you **learn cheaply** what an agent *could* do before you fund the robust, production version.

**Best for**

- Rapid experiments with DOM interaction and “human-in-the-loop” approvals
- Drafting outreach, summaries, enrichments with hard cost/step limits
- Pattern discovery (what to automate next)

**Pros**

- Fast idea→attempt loop; approachable for non-devs
- Built-in guardrails (max steps/spend, allow-listed tools, HIL checkpoints)
- Great for show-and-tell: short Looms, red-team tests, A/B vs deterministic

**Cons / Risks**

- Not your final uptime layer—expect occasional DOM drift/CAPTCHA friction
- Context creep: needs strict context packs and “never do” lists
- Token costs can spike if budgets aren’t enforced (hence the $200/month plan)

**Policy & Access**

- **HIL required** for any outbound action (send/post/click-buy)
- Preflight prompt must declare: goal, tools, max steps, max tokens/cost, don’ts
- Store secrets outside prompts; pass by reference; scrub logs of PII
- Budget: daily run caps + per-run token/cost ceilings

**Where to learn**

https://www.skool.com/citizen-developer-1179/about

---

## Kafka / Brainbase Labs — Production-Grade, Dependable Backbone

**What it is:** A streaming backbone and dependable execution substrate used when reliability and scale matter (think queues, backpressure, replay, and exactly-once semantics when designed right).

**Why it matters here:** This is what you graduate to when the experiment becomes a **digital worker** with SLAs.

**Best for**

- High-volume pipelines, ordering, and durable event logs
- Separating concerns: producers (apps/agents) → topics → consumers (workers)
- Observability & incident response (replay, dead-letter, lag metrics)

**Pros**

- Uptime and resilience: handles bursts, retries, and failure isolation
- Clear contracts via topics and schemas; easier audits and change control
- Scales with you; easier multi-team collaboration

**Cons / Risks**

- Heavier lift to set up correctly (schemas, partitions, retention)
- Overkill for tiny, short-lived flows; ops overhead if unmanaged

**Policy & Access**

- Topic-level ACLs; schema registry required; retention & compaction defined
- Consumer groups monitored (lag alerts), dead-letter topics provisioned
- Rollback & replay run-books; RTO/RPO targets documented
- Budget: infra cost envelope per environment; cost telemetry on stream

**When to reach for it**

- “This runs every day without me” production lanes
- Anything tied to customer SLAs or money movement

---

## Why these three (and not just a pile of tools)?

- **Separation of concerns:** n8n proves the flow → Fellou explores agentic gains → Kafka/Brainbase scales the reliable worker.
- **Compounding dependability:** Higher-cost, higher-rigor layers (Kafka/Brainbase) **pay back** via fewer incidents, safer deploys, cleaner audits, and predictable throughput.
- **Operator clarity:** Each layer has a single story: *show it works* (n8n), *see if it’s worth it* (Fellou), *make it endure* (Kafka/Brainbase)

---

## Rules of the Road (pin these)

1. **HIL ON by default.** Outbound actions require approval in-app or via form.
2. **Budgets before buttons.** Set run caps and token/cost ceilings before first run.
3. **Deterministic fallback exists** (and is tested) before any agent goes live.
4. **Everything logs.** If it didn’t log run_id/step/status/cost, it didn’t happen.
5. **Red-team monthly.** DOM drift, 429s, PII traps, empty states, CAPTCHA handling.
6. **Escalate to Kafka/Brainbase** when you need reliability, replay, or SLAs.

---

Non-exhaustive resource:

https://docs.google.com/spreadsheets/d/10IIAK0x5CYEKhBDIz0AF6W9cQw5JSE6diQxxIsStb84/edit?gid=0#gid=0