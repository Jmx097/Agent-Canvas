# Detailed Previews

---

# Card 0 — Orientation & Guardrails

**Goal**

Set clear rules so Fellou can help without risk. KPI = replies and booked calls.

**Steps**

- Turn **HIL ON** (human approves every send).
- Set daily send cap (start 20–30).
- Set budget caps (API + domains).
- Define success: reply rate %, calls/week.

**Inputs**

[Access/Policy Matrix] · [KPI Dashboard] · [Calendar Link]

**Output**

One-page guardrail note: caps, KPI, roles.

**Proof & Metric**

Post a screenshot of caps + HIL ON.

✅ Metric: Guardrails saved (Y/N)

---

# Card 1 — ICP & Farm Area

**Goal**

Pick who you serve, where, and price bands so messages land.

**Steps**

- Choose **niche** (buyers, sellers, landlords, investors).
- Define **geo farm** (city/ZIPs).
- Add **price bands** and property types.
- List target **roles** (owner, landlord, HOA, PM).
- Note **channels** (email, SMS, call, DM).

**Inputs**

[ICP Worksheet] · [Airtable Base]

**Output**

ICP record saved with geo + roles + bands.

**Proof & Metric**

Post ICP screenshot.

✅ Metric: ICP approved (Y/N)

---

# Card 2 — Offer & Messaging Pack

**Goal**

Create one clear offer and three scripts that feel human.

**Steps**

- Write 1 **core offer** (pain → outcome → time → proof).
- Draft 3 scripts: **email / SMS / VM**.
- Add **objection notes** and compliant claims.
- Map merge tags (first name, area, property type).

**Inputs**

[Messaging Pack] · [Compliance Notes]

**Output**

3 scripts + 1 offer card, ready to test.

**Proof & Metric**

Paste your 3 scripts.

✅ Metric: Offer clarity (1–10) ≥ 8

---

# Card 3 — Data Foundations

**Goal**

Stand up clean storage so nothing breaks at launch.

**Steps**

- Create base tables: **Prospects, Outreach, Replies, Bookings**.
- Map required fields (email, source, status, notes).
- Connect **Tally form** → Airtable.
- Set sheet exports for daily CSV.

**Inputs**

[Airtable Base] · [Tally Form] · [Sheets Export]

**Output**

Working base + sample row in each table.

**Proof & Metric**

Post screenshot of tables.

✅ Metric: 4 tables live (Y/N)

---

# Card 4 — Sender Setup

**Goal**

Make sure sends land and bookings route to your calendar.

**Steps**

- Warm or whitelist sender domain.
- Add signature and sender name.
- Connect **booking link** and time windows.
- Test deliverability to 2 personal emails.

**Inputs**

[Domain/Warmup Notes] · [Booking Link]

**Output**

Sender OK + 2 test emails delivered.

**Proof & Metric**

Post 2 inbox screenshots.

✅ Metric: 2/2 delivered (Y/N)

---

# Card 5 — Prospect Miner Workbench (50/day)

**Goal**

Pull 50 leads/day with context you can use.

**Steps**

- Pick sources (directories, MLS alt, Google, maps, lists).
- Define **must-have** fields (role, email, geo, note).
- Save to **Prospects** with “Source” and “Confidence.”
- Export daily CSV to /exports/date.csv.

**Inputs**

[Prospect Miner Spec] · [Airtable Base] · [Sheets Export]

**Output**

50 fresh rows with context notes.

**Proof & Metric**

Attach CSV (≥50).

✅ Metric: 50 rows, ≥80% complete (Y/N)

---

# Card 6 — Fellou Agent Setup

**Goal**

Have Fellou draft, not blast—always stop for approval.

**Steps**

- Paste **system prompt** + tool list.
- Set budgets and **stop points** for HIL.
- Map fields to draft templates.
- Test on 5 sample contacts.

**Inputs**

[Fellou Project] · [Messaging Pack] · [Access/Policy Matrix]

**Output**

5 drafted messages queued for approval.

**Proof & Metric**

Post 1 raw draft + 1 approved edit.

✅ Metric: HIL stop works (Y/N)

---

# Card 7 — n8n Orchestrator

**Goal**

Wire the flow: Preflight → Draft → Approve → Send → Log.

**Steps**

- Build nodes: **Fetch → Draft → Approve → Send → Write-back**.
- Add error lane + retry rules.
- Log **tokens, cost, status** to Airtable.
- Run a dry test on 5 leads.

**Inputs**

[n8n Flow] · [Airtable Base] · [Fellou Project]

**Output**

Working flow run with logs.

**Proof & Metric**

Screenshot of success run + Airtable write-back.

✅ Metric: 5/5 processed (Y/N)

---

# Card 8 — Launch Touch #1

**Goal**

Ship the first wave safely and measure response.

**Steps**

- Approve 20–30 drafts.
- Send in 2–3 batches.
- Tag replies and bounces.
- Add quick notes on tone and fit.

**Inputs**

[Messaging Pack] · [n8n Flow] · [KPI Dashboard]

**Output**

Outreach log + replies captured.

**Proof & Metric**

Post counts: sent/replies/bounces.

✅ Metric: Reply rate ≥ 3–5%

---

# Card 9 — Touch #2 + Booking Flow

**Goal**

Follow up cleanly and move replies to calls.

**Steps**

- Draft Touch #2 from reply status.
- Human approves; send.
- If positive, push **booking link** + hold.
- Confirm event and notes saved.

**Inputs**

[Messaging Pack] · [Booking Link] · [Airtable Base]

**Output**

Follow-ups sent + booked calls logged.

**Proof & Metric**

Post # of second touches + bookings.

✅ Metric: Book rate on replies ≥ 25%

---

# Card 10 — A/B: Deterministic vs Agentic

**Goal**

Prove where Fellou wins vs. simple templates.

**Steps**

- Split 20 leads each: **Deterministic** vs **Agentic**.
- Keep same list + send windows.
- Track time, cost, approvals, replies.
- Summarize lift and risks.

**Inputs**

[KPI Dashboard] · [Run Log] · [Messaging Pack]

**Output**

One-page A/B summary with a decision.

**Proof & Metric**

Attach the A/B table.

✅ Metric: Chosen lane + reason (Y/N)

---

# Card 11 — KPI Dashboard & Proof

**Goal**

Show outcomes and time saved in one view.

**Steps**

- Update tiles: volume, replies, calls, wins, hours saved.
- Export **ROI slide** and **Case Card**.
- Note 3 learning points to keep.

**Inputs**

[KPI Dashboard] · [ROI Tracker] · [Case Card Template]

**Output**

PDF slide + case card posted.

**Proof & Metric**

Upload both files.

✅ Metric: ROI ≥ 2–5× target (Y/N)

---

# Card 12 — Scale Plan

**Goal**

Grow safely: more volume, new sources, or new channel.

**Steps**

- Pick **one**: raise daily cap, add source, add channel.
- Update guardrails and costs.
- Set next 14-day targets.
- Schedule review date.

**Inputs**

[Access/Policy Matrix] · [Prospect Miner Spec] · [KPI Dashboard]

**Output**

14-day scale plan saved.

**Proof & Metric**

Post plan + calendar review.

✅ Metric: Plan approved (Y/N)

---

want me to do the **Free Cohort (cards 1–5)** in the same sub-page format next?