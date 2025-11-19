# Context Dictionary

Category: Resources

TL;DR It’s how we keep the agent scaffold plug and play so you do little thinking on setting them up.

This comes to life after you complete the Lab Cards week by week.

### What it is (plain-English)

The **Context Dictionary** is your single source of truth for everything an agent needs to act like a smart teammate: who you serve, what you sell, how you talk, where data lives, and what *never* to do. Think of it as a compact “company brain” the scaffold reads before it runs.

### Why it matters

- **Faster, safer outputs:** Agents stop guessing and start executing inside your rules.
- **Governed learning:** As run-logs and approvals accumulate, you enrich the same context—not 20 scattered prompts.
- **Reusability:** One dictionary → many workers (deterministic flows, browser agents, voice agents) with consistent tone, offers, and KPIs.

---

## What’s inside (minimum viable fields)

You can copy these sections into one Notion page (or `context-dictionary.json`) and keep them updated. Alternatively, complete the Lab Cards in the actual roadmaps to have the most effective outcome:

1. **Identity & Audience**
- `brand.name`, `brand.voice` (tone, do/don’t phrases)
- `audience.icp` (who we help), key pains, desired outcomes
1. **Offers & Proof**
- `offer.core` (promise, price band, guarantee)
- `social_proof` (mini case blurbs, approved claims)
1. **KPI & Guardrails**
- `kpi.primary` (hours saved, revenue, error-rate)
- `guardrails.never_do` (PII rules, legal no-gos)
- `budgets` (max tokens/run, max runs/day)
1. **Systems & Access**
- `systems` (CRM, helpdesk, calendar, file store)
- `endpoints` (read/write capability notes)
- `data_sources` (where truth lives: Sheet tabs, Notion DBs)
1. **Process Short-cuts**
- `checklists` (SOP snippets the agent can follow)
- `faq & objection library` (approved answers/snippets)
- `edge_cases` (how to fail safely; fallback message)
1. **Routing Hints (optional but powerful)**
- `channel_prefs` (email > sms? LinkedIn allowed?)
- `tone_switches` (formal for legal, casual for social)
- `selectors` (CSS/XPath hints for browser agents)
- `scoring` (what makes a “qualified” lead/opportunity)

---

## How it works with the Agent Scaffold (the handshake)

**Agent Scaffold = your reliability spine**

*Preflight → Orchestrate (n8n) → HIL gate → Deterministic fallback → Run-log → Budgets.*

Here’s the flow:

1. **Preflight pulls context**
    
    The scaffold’s first node loads the **Context Dictionary** and validates required fields (offer, KPI, channel rules).
    
2. **Planner builds a plan using context**
    
    The agent plans steps using your **SOP checklists**, **guardrails.never_do**, and **budgets**. If any required field is missing, it stops and asks for HIL approval (no silent improvising).
    
3. **Tools are whitelisted from `systems`**
    
    Only the systems you listed are callable. Everything else is out-of-scope by design.
    
4. **HIL gate enforces risk & tone**
    
    If the action touches customers or money, the scaffold routes a preview (draft email, outreach list, proposal snippet) for human approval—using your **brand.voice** and **faq/objections**.
    
5. **Deterministic fallback if anything’s off**
    
    If a website DOM changed or an API rate-limits, the scaffold jumps to your **edge_cases** play (e.g., “Log incident, send safe holding message, retry in 30m”).
    
6. **Run-log enriches the dictionary over time**
    
    Each run appends outcome, cost, time, approvals, and common objections. You promote new learnings back into `faq`, `checklists`, or `edge_cases`—so the next run starts smarter.
    

---

## Where it lives (and how to keep it clean)

- **Primary home:** Link Hub → “Context Dictionary” page (or `/08_Snippets/context-dictionary.json` in your Pack).
- **Edit rules:** Only the owner or ops lead edits; agents *read* it. Use change-notes (“what changed, why”).
- **Update cadence:**
    - Day-0 setup (non-negotiable)
    - After every greenlighted win (add proof + objection learned)
    - Weekly during cohort (5-minute hygiene pass)

---

## Copy-ready starter schema (drop into Notion or JSON)

```json
{
  "brand": {
    "name": "Plinko Solutions",
    "voice": {
      "style": ["approachable", "direct", "ROI-first"],
      "do": ["plain English", "show math", "short paragraphs"],
      "dont": ["jargon", "over-promising", "cold-DM vibes"]
    }
  },
  "audience": {
    "icp": "SMB owners & lean teams (real estate, agencies, ops-heavy services)",
    "pains": ["manual admin", "stalled proposals", "thin pipeline"],
    "outcomes": ["hours back", "more replies/calls", "faster close"]
  },
  "offer": {
    "core": {
      "name": "30-Day Co-Pilot",
      "promise": "Ship 2–3 quick-win automations + 1 governed agent",
      "price_band": "$497–$1,997",
      "guarantee": "Hit $500 value or route to rescue lane"
    },
    "proof": ["Saved 10–20 hrs/wk typical", "Case cards added weekly"]
  },
  "kpi": { "primary": "hours_saved_per_week", "secondary": "replies_or_calls_booked" },
  "guardrails": {
    "never_do": ["send without HIL", "touch PII outside CRM", "scrape paywalled content"],
    "budgets": { "max_tokens_per_run": 80000, "max_runs_per_day": 50 }
  },
  "systems": {
    "crm": { "name": "GHL", "write": true },
    "sheets": { "roi_tracker": "ROI Tracker!A:Z", "run_log": "Run Log!A:Z" },
    "calendar": { "name": "Google Calendar", "bookings_allowed": true }
  },
  "data_sources": {
    "icp_sheet": "ICP!A:F",
    "past_clients_csv": "drive:/reactivation/past_clients.csv"
  },
  "checklists": {
    "reactivation_touch": [
      "Load 25–30 contacts",
      "Draft Touch #1 using brand.voice",
      "Route for HIL approval",
      "Send & log outcomes"
    ]
  },
  "faq": {
    "pricing_pushback": "Acknowledge → restate value → offer quick-win trial slot."
  },
  "edge_cases": {
    "low_quality_list": "Stop. Flag for list cleaning micro-play before outreach.",
    "api_429": "Backoff 15m, retry x3, then HIL."
  },
  "routing": {
    "channels": ["email", "sms (opt-in only)"],
    "tone_switches": { "legal": "formal", "social": "conversational" }
  }
}

```

---

## Examples: how the scaffold uses it (three common plays)

**A) Reactivation Touch #1 (agent drafts, you approve)**

1. Read `data_sources.past_clients_csv`
2. Generate 3 draft emails using `brand.voice` + `offer.core.promise`
3. Stop at HIL with a diff vs FAQ; on approve, send & **log replies**

**B) Lead list build (browser agent)**

1. Use `routing.selectors` to scrape targets; score by `audience.pains` cues
2. Validate against `guardrails.never_do` (no paywalls, no PII)
3. Write to Sheet + **log Δtime, Δcost**

**C) Proposal follow-up (deterministic fallback first)**

1. Pull open deals from `systems.crm`
2. If missing proposal link → deterministic “nudge template”
3. Else draft personalized follow-up; HIL; send; **log outcome**

---

## Governance & hygiene (non-negotiables)

- **HIL stays ON** for outreach, pricing, and any customer-visible copy.
- **Budgets enforced** from the dictionary (no ad-hoc overrides in the flow).
- **Run-log or it didn’t happen:** every run records `run_id, path, step, status, tokens, cost, ms, approver`.

---

## What to expect (success signals)

- First week: fewer clarifying questions from the agent; drafts feel “on-brand” out of the gate.
- By day 10: run-logs show shorter cycles; fewer HIL edits (quality ↑).
- By day 30: dictionary grows (new FAQ, objections, selectors), and your second agent comes online faster because it reuses the same context.

---

You now have a living “company brain” feeding a governed scaffold. That’s how we get speed **and** safety—consistently.