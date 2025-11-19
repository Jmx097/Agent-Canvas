# Agent Scaffold

Category: Resources

```jsx
You (Owner)
  ↳ Orchestrator (Fellou/n8n/Kafka)
     ↳ Path Router (LeadGen / Reactivation / Proposal / Ops)
        ↳ Digital Workers (below)
           ↳ HIL Approver (you/teammate)
              ↳ Write-backs (Sheets/CRM)
                 ↳ Run-Log + ROI Snapshot

```

### 1) Lead Gen (new pipeline)

**Goal:** more qualified conversations, automatically scheduled.

- **Browser Scout** – finds ICP prospects on approved sites.
- **List Cleaner** – dedupes, enriches essentials (name, role, email/link).
- **Message Drafter** – drafts 1–2 touch openers for review.
- **Sender & Scheduler** – sends approved messages + posts your booking link.
- **CRM Clerk** – creates/updates contact + activity.
- **QA Sentinel** – flags bounced emails, rate-limits, and logs outcomes.

**Output:** replies, booked calls, CRM rows updated.

**Your HIL moments:** approve scripts, approve first send batch.

---

### 2) Reactivation (cash in 30 days)

**Goal:** revive past leads/clients with a tight 2–3 touch sequence.

- **List Importer** – ingests old leads/clients CSV safely.
- **Warmer** – drafts personalized “we’re back / here’s value” messages.
- **Follow-Up Timer** – schedules Touch #2/#3 for non-responders.
- **Booking Assistant** – watches for positive replies, offers times, books.
- **CRM Clerk** – tags “reactivated,” logs outcomes.
- **QA Sentinel** – catches risky sends, throttles volume, records proofs.

**Output:** callbacks, re-orders, upsells.

**Your HIL moments:** approve the offer, approve Touch #1 copy.

---

### 3) Proposal Acceleration (close faster)

**Goal:** reduce stall after “send proposal.”

- **Deal Scraper** – pulls “open proposals / stale deals.”
- **Proposal Drafter** – assembles 1-pager or template with fresh details.
- **Follow-Up Cadencer** – nudges with value reasons and next steps.
- **Signature Pusher** – preps e-signature packet (you click send).
- **CRM Clerk** – updates stage, next step, and dates.
- **QA Sentinel** – enforces “no send without HIL,” tracks win/lose notes.

**Output:** proposals sent, nudges delivered, wins recorded.

**Your HIL moments:** approve proposal draft, approve send.

---

### 4) Ops Efficiency (hours back = money)

**Goal:** ship one deterministic flow + one governed browser worker.

- **Stopwatch Bot** – records honest baseline times (3 samples).
- **Flow Runner** – executes the deterministic version (no browsing).
- **Browser Worker** – adds an agent layer for hairy web steps.
- **Error Handler** – rollback, retry, and alert playbook.
- **Reporter** – logs time saved and cost deltas to ROI sheet.

**Output:** ≥2 hrs/week saved + proof in dashboard.

**Your HIL moments:** approve agent overlay, approve fallback rules.

---

### Role Cards (copyable mini-specs)

**Format:** Goal • Triggers • Inputs • Output • Guardrails

- **Browser Scout** – *Find prospects* • “New list needed” • ICP fields • 10–20 targets • Stay in allowed domains; no scraping PII.
- **List Cleaner** – *Make it usable* • New list arrives • Names/emails/links • Deduped, scored list • No sends; validation only.
- **Message Drafter** – *Write the opener* • Approved list exists • ICP notes, offer • 10 short drafts • Never sends without HIL.
- **Sender & Scheduler** – *Ship + book* • Draft approved • Channel auth, calendar link • Sent log + booking • Rate limits on; budget caps.
- **CRM Clerk** – *Log reality* • Message sent/replied • Contact + activity fields • Up-to-date CRM • Idempotent writes (no duplicates).
- **QA Sentinel** – *Keep it safe* • Any run • Run-Log, thresholds • Pass/flag + alert • Enforces HIL + stop-loss.
- **Stopwatch Bot** – *Baseline truth* • Before/after tests • Task steps • 3 timings • Stores proof screenshots.
- **Flow Runner** – *Deterministic path* • Approved SOP • Input row • Pass/fail row • Retries + dead-letter tab.
- **Browser Worker** – *Agent overlay* • Green baseline • System prompt + tools • Successful web step • Time/token budget enforced.
- **Error Handler** – *Fast recovery* • Fail/429/CAPTCHA • Run ID, error • Rolled back state + note • Pings owner.