# Offer — We Build Your Governed AI Twin (in 14 Days)

**Why this works (public proof):**

- Klarna’s AI assistant now handles ~⅔ of service chats, doing the work of ~700 FTEs, cutting resolution time from 11→2 minutes, and reducing repeat contacts by 25%. That’s governed, measurable automation in the wild. ([Klarna](https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/?utm_source=chatgpt.com))
- Salesforce’s CEO says AI now does ~30–50% of the company’s work; support volumes handled by agent tech have surged (Agentforce). The “agentic enterprise” is no longer theory. ([Bloomberg](https://www.bloomberg.com/news/articles/2025-06-26/salesforce-ceo-says-30-of-internal-work-is-being-handled-by-ai?utm_source=chatgpt.com))
- CarMax used Azure OpenAI to summarize 100k+ reviews, turning multi-year manual work into days—proof that well-scoped content/ops tasks compound fast. ([Microsoft](https://www.microsoft.com/en/customers/story/1501304071775762777-carmax-retailer-azure-openai-service?utm_source=chatgpt.com))

---

## What we build (and why it’s safer)

A **governed AI Twin** for one revenue-adjacent workflow (you choose: Lead Reactivation, Proposal Follow-Up, or Collections/Ops). It drafts, you approve, it logs everything.

- **Human-in-the-loop approvals** via n8n’s Wait/Resume URL (one-click Approve/Reject). No auto-sending. ([n8n Docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.wait/?utm_source=chatgpt.com))
- **Structured Outputs** (JSON Schema) so drafts are machine-readable and dependable. ([OpenAI](https://openai.com/index/introducing-structured-outputs-in-the-api/?utm_source=chatgpt.com))
- **Email safety**: create **Gmail drafts** only (or your ESP), never fire without human approval. ([n8n Docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/?utm_source=chatgpt.com))
- **Security posture**: OWASP LLM Top-10 patterns (prompt-injection resistance + data boundaries). ([OWASP](https://owasp.org/www-project-top-10-for-large-language-model-applications/?utm_source=chatgpt.com))

---

## The 14-Day Build (done for you)

**Day 1–2 — Diagnostic & Win Pick**

We map one “low-effort/high-impact” play in your funnel (Reactivation, Proposal, or Ops). You’ll see baseline KPIs and a target money slide (time saved → Net ROI). (McKinsey’s macro view supports the productivity upside; we focus on your tiny, provable slice.) ([McKinsey & Company](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-economic-potential-of-generative-ai-the-next-productivity-frontier?utm_source=chatgpt.com))

**Day 3–7 — Build the Spine**

- System prompt + guardrails, a 10-snippet Context Pack
- n8n flow: Preflight → Model (Structured JSON) → **Gmail Draft** → **Wait for Approve/Reject** → Log to Sheet/Notion ([n8n Docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.wait/?utm_source=chatgpt.com))
- Run-Log schema with tokens, cost, status, replies, booked calls, revenue

**Day 8–10 — Pilot & Tune**

We run 20–50 safe drafts against your list, tune tone/fields, and tighten approvals.

**Day 11–14 — Prove It**

You get: ROI dashboard, 1-page Case Card (Problem → Fix → KPI Δ), and a handoff video. We also add your “kill switch” and budget caps.

---

## What you walk away with

- A **click-to-approve Twin** that produces on-brand drafts for one workflow
- **Run-Log + ROI math** (time saved, costs, replies, booked calls)
- **Case Card** you can show clients/bosses
- Optional: a second template path scoped for your next workflow

---

## Packages & economics

- **DWY PROMO**: ***First 500 members only*** for [Delegat8](https://delegat8.com/) — Governed AI Twin: Starter Plan 
**$997 setup + $497/month**
    
    ### One-line promise
    
    We install and run a **draft-only, approval-first AI Twin** for one revenue-adjacent workflow (you choose: **Lead Reactivation**, **Proposal Follow-Up**, or **Collections/Ops Reminders**), then send you a **weekly ROI snapshot** that proves it’s paying for itself.
    
    ---
    
    ## What’s included
    
    ### Setup (one time, $997)
    
    - **10-min diagnostic** → pick your fastest “money slide.”
    - **Context Pack** (FAQs, value props, 3 golden examples), **System Prompt + Guardrails** (refusal policy, tone, boundaries).
    - **Orchestration build** (n8n/Make): Preflight → Model (structured JSON) → **Gmail Draft only** → **Approve/Reject** link → Run-Log (Sheet/Notion).
    - **Safety defaults**: draft-only, budget caps, human-in-the-loop, injection/PII rules.
    - **Baseline metrics** + “Case Card” shell (Problem → Fix → KPI delta).
    
    ### Monthly (managed, $497)
    
    - **Operations**: we run/tune the Twin, monitor costs/errors, maintain guardrails.
    - **Throughput**: up to **120 runs/month** (≈6 per business day) in your chosen workflow.
    - **Weekly ROI snapshot**: time saved, replies, booked calls, revenue; updated **Case Card**.
    - **Support**: async Slack/DM support, 1 mini-tuning each week (tone, fields, targeting).
    - **Fair-use API budget included**: up to **$30/mo** model spend; you approve any top-ups.
    
    > Add a second workflow (+$200/mo) after month 1. Pause/cancel anytime; you keep the build.
    > 
    
    ---
    
    ## How it’s delivered (14-day timeline)
    
    - **Day 1–2**: Diagnostic + asset grab → confirm workflow & baseline KPI.
    - **Day 3–7**: Build & connect → first drafts landing in Gmail (draft-only).
    - **Day 8–10**: Pilot (20–50 controlled runs) → tone/accuracy tuning.
    - **Day 11–14**: ROI snapshot + Case Card v1 → “uncap” options (still HITL).
    
    ---
    
    ## Three offer variants (pick one now, add more later)
    
    ### A) Lead Reactivation Twin (B2B services)
    
    - **What it does**: Re-opens stalled deals; drafts “polite nudge + next step.”
    - **Economics (sample)**: 200 old leads → 10 replies → 2 calls → 1 close at $1,500.
        - **Monthly cost**: $497 + small API. **Payback**: 1 win = 3×–5× fee.
    - **Proof mechanics**: replies/booked calls logged; time saved on drafting/follow-ups.
    
    ### B) Proposal Follow-Up Twin (agencies/consultants)
    
    - **What it does**: Drafts recap + concession + CTA; 2nd/3rd touch you approve.
    - **Economics (sample)**: 15 open proposals/mo → +10–20% lift = +1 extra win at $3k–$15k.
        - **Payback**: 1 saved/accelerated win covers months of fees.
    - **Proof mechanics**: win-rate delta tracked; calendar & CRM notes synced.
    
    ### C) Collections / Ops Reminder Twin (SMB professional services)
    
    - **What it does**: Gentle invoice reminders & “send us X” checklists.
    - **Economics (sample)**: 80 overdue → 10–20% faster recovery; $2k–$5k cash pulled forward.
        - **Payback**: single batch often covers the month.
    - **Proof mechanics**: recovery % and days-to-pay trendline.
    
    > We keep all messages draft-only until you trust the outputs. Approve/Reject in one click; everything is logged.
    > 
    
    ---
    
    ## What we need from you (15–30 minutes total)
    
    - CRM/export or spreadsheet of targets (emails + light context).
    - Three “golden example” messages, value props, and your signature block.
    - A Google account (for Gmail Drafts) and a Sheet/Notion page we can write to.
    
    ---
    
    ## SLAs & guardrails
    
    - **Time-to-first-draft**: within **72 hours** of kickoff.
    - **Weekly cadence**: ROI snapshot every Friday by 2pm ET.
    - **Safety**: no auto-send; HIL approval links; budget caps; run-log + audit trail.
    - **If we miss** a weekly snapshot: next month’s fee is discounted **25%**.
    
    ---
    
    ## Simple ROI math (drop this into your post/DM)
    
    - **Time ROI** = (minutes saved × hourly rate) ÷ 60
    - **Net ROI** = Time ROI + Revenue Lift − (497 + API)
    - **Break-even examples**
        - Save 6 hours/week at $85/hr = **$2,040/mo** time ROI → net > $1.5k after fees.
        - Close one $1,500 deal from reactivation → net > $900 after fees.
    
    ---
    
    ## Upsells (only if/when you want them)
    
    - **Second workflow** (+$200/mo)
    - **Browser agent add-on** for enrichment/light research (+$150/mo)
    - **Voice/phone follow-up draft** (auto-dialer scripting) (+$100/mo)
    
    ---
    
    ## Cancellation & ownership
    
    - Month-to-month. Cancel anytime before next billing.
    - You **own** the prompts, flows, and Notion/Sheet dashboards. We remove our keys, you retain the stack.

**DFY**

**Starter Build — $2,500**

- 1 governed AI Twin (one workflow)
- n8n orchestration, Structured Outputs, Gmail draft safety
- Run-Log + ROI dashboard + Case Card

**Growth Build — $5,000**

- Everything in Starter, plus a second workflow OR a basic browser agent add-on (site research, light enrichment) with the same HITL controls

> Typical outcomes from similar public deployments: lowered handling time and higher self-service/first-pass resolution (see Klarna; Capgemini’s CX study cites double-digit AHT and FCR improvements). We anchor your build to a conservative, workflow-level goal. (Klarna)
> 

---

## Three example plays (and how the math can pencil)

1. **Lead Reactivation Twin (B2B services)**
    - Inputs (example): 200 stale leads, 25% reply on warm re-open, 20% book, 20% close, $1,500 LTV per deal → ~5 closes = **$7.5k uplift**. Time saved: 6 hrs/week drafting/follow-ups.
    - Why safer: all messages pre-approved; logs prove cost per reply and time ROI.
    - Public analog: reactive AI assistance improves speed & accuracy of routine comms (Klarna CS deflection/handle-time). ([OpenAI](https://openai.com/index/klarna/?utm_source=chatgpt.com))
2. **Proposal Follow-Up Twin (agencies/consultants)**
    - Inputs: 15 active proposals/month; baseline follow-ups = 1; Twin adds 2 smart nudges + a recap; +10–20% win-rate lift is common in disciplined follow-up research; you see the delta in booked calls and time saved.
    - Structure: JSON-clean drafts → Approve → send → Run-Log. (Structured outputs reduce rework and breakage.) ([OpenAI](https://openai.com/index/introducing-structured-outputs-in-the-api/?utm_source=chatgpt.com))
3. **Collections / Ops Reminder Twin (pro services/SMB)**
    - Inputs: 80 overdue invoices; Twin drafts polite reminders + checklists; even a modest uplift improves cash conversion cycle and trims AHT.
    - Reference: process-level improvements (AHT ↓12–16%, FCR ↑31%) are reported in CX transformations using AI assist + workflow. Your twin is a narrow, provable slice. ([Capgemini](https://www.capgemini.com/wp-content/uploads/2025/03/20th-March-Customer-service-transformation-CRI_Final.pdf?utm_source=chatgpt.com))

*(Numbers above are examples—your baseline + pilot will set the real targets.)*

---

## Risks we remove (the “governed” bit)

- **Rogue sends?** Impossible—drafts only until you uncap. (Gmail Drafts + HITL). ([n8n Docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/?utm_source=chatgpt.com))
- **Messy outputs?** Structured JSON Schema or the run fails gracefully. ([OpenAI Platform](https://platform.openai.com/docs/guides/structured-outputs?utm_source=chatgpt.com))
- **Injection attempts?** We implement OWASP LLM controls in the prompt & flow. ([OWASP](https://owasp.org/www-project-top-10-for-large-language-model-applications/Archive/0_1_vulns/Prompt_Injection.html?utm_source=chatgpt.com))

---