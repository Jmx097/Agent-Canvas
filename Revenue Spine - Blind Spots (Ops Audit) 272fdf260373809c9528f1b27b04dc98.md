# Revenue Spine - Blind Spots (Ops Audit)

Category: Playbooks

**What this is:** A non-technical, governed “ops co-pilot” that handles document filing and research under **Human-In-Loop (HIL)** review. It watches inboxes/portals/drives, files what arrives, summarizes what matters, and drafts clean, cite-aware memos you approve in minutes.

**Promise:** Fewer filing errors, faster research, cleaner audit trails—tracked in **[ROI Tracker]** and **[Run-Log]**.

This is significantly easier to do with the 30 day roadmap as you’re provided with Run Cards, Agent Cards, and Lab Cards that help you bridge gaps without a heavy ideation lift. 

The below is meant to be simple to keep illustrative.

---

## The Agent Scaffold (your digital team)

```
Inputs → Intake/Archivist → Filer/Indexer → Researcher → QA Gate → Draft/Deliver
           │                   │               │           │           │
           └──────────── Logger ←──────────────┴───────────┴───────────┘
                              ↑
                       Compliance Sentinel
                         (rules, caps, PII)

```

**Roles (plain English):**

- **Intake/Archivist:** pulls new docs from email, e-filing receipts, client portals.
- **Filer/Indexer:** names, tags, and files by Matter → Phase → Doc-Type; checks duplicates/versions.
- **Researcher:** runs targeted research (statutes, regs, cases, agency guidance), extracts quotes + cites.
- **QA Gate (HIL):** you approve/reject with reason tags (wrong matter, weak source, missing cite).
- **Draft/Deliver:** assembles a 1-pager brief or issue memo; attaches source list.
- **Logger:** writes every step to **[Run-Log]** (time, cost, pass/fail, reasons).
- **Compliance Sentinel:** enforces **Never-Do**, step/budget caps, masking/redaction, retention rules.

---

## Blind Spots We Fix (where fatigue hides)

- **Doc sprawl & versions:** “Which PDF is final?” → Auto-naming, dedupe, version notes.
- **Lost time on sorting:** Inbox → Matter folder without manual drag-drop.
- **Citation drift:** Pulls primary sources + pin cites, flags low-confidence secondary links.
- **Deadline drift:** New filings trigger reminders and checklists (service, calendar, follow-ups).
- **Knowledge gaps:** Quick, cite-aware memos to brief partners or clients in minutes.

---

## Two Core Plays (copy-paste ready)

### A) Smart Filing Spine (always-organized matters)

**Inputs:** authorized mailbox(es), e-file receipts, client upload folder, Matter list, naming rules.

**Steps:**

1. Intake → detect matter ID/client name.
2. Filer/Indexer → rename `YYYY-MM-DD_MATTER_DOC-TYPE_v1.pdf`, apply tags (phase, privilege).
3. Duplicate/version check → keep newest; archive prior; write version note.
4. Missing-piece scan → if complaint found, ask for proof of service; if order found, start deadline checklist.
5. QA Gate → you approve batch; corrections train the rules.
    
    **Output:** Zero-inbox filing, searchable tags, checklists auto-spawned.
    

### B) Deep Research Spine (fast, cite-aware answers)

**Inputs:** question in plain English + jurisdiction/scope + “must-include” sources.

**Steps:**

1. Researcher → plan search, prefer primary law; collect 3–5 on-point authorities.
2. Extract rule/standard, holding, key quotes; capture citations/links.
3. Draft/Deliver → 1-page memo: **Issue / Rule / Analysis / Sources**.
4. QA Gate → you confirm cites & add judgment; agent records edits for next time.
    
    **Output:** A tight brief with sources, ready to review or send.
    

---

## Guardrails (keep it safe & tight)

- **HIL stays ON:** agent drafts → *you approve* → file/send.
- **Step caps:** max pages/run, max sources/memo, max runs/day.
- **Data boundaries:** no client PII to external models; mask names; keep files in your drive.
- **Never-Do list:** no behind-login scraping, no confidential uploads, no advice without cites, no first-touch client sends.
- **Audit trail:** Run-Log + version notes + source list on every memo.
- **US-only focus:** set jurisdiction defaults; require explicit opt-in to expand.

---

## 14-Day Rollout (simple & proven)

**Day 0–2 (Foundation)**

- Set KPI + $ target → **[ROI Tracker]**
- Add **naming rules**, **matter map**, **Never-Do**, and **jurisdiction defaults** to **[Access/Policy Matrix]**
- Turn **HIL=ON**; set **step/budget caps**

**Day 3–5 (First Pass)**

- Wire 1 mailbox + 1 client folder → run **Smart Filing** on 25–50 docs
- Approve batch in **QA Gate**; log fixes → **[Run-Log]**

**Day 6–10 (Research Live)**

- Ship 3 research requests using the **Deep Research** template
- Save **5 Golden Samples** (great memos with cites) for the Writer to mirror

**Day 11–14 (Scale Safely)**

- Add second mailbox or practice area
- Publish a **Case Card** (before/after screenshots, time saved, error reduction)

**Success (hit one):**

- Filing SLA ≤ **24h** for all inbound docs
- Research memo cycle **< 30 min** (was 2–3h)
- QA first-pass ≥ **80%**, zero material filing errors

---

## Quality Targets (earn your scale)

- **QA first-pass approvals:** ≥ **80%**
- **Material error rate:** **0** (matter, version, cite)
- **Research sources:** ≥ **3** primary; note secondary for context
- **Time saved per memo:** **60–75%**
- **Daily caps:** start 15–25 filings/day; 2–3 memos/day → **+20%/day** only when green

**Auto-brakes:**

- QA <80% → pause volume; fix rules/templates
- Any material error → freeze sends; root-cause & add checklist
- Weak sources → require 1 more primary and a pin cite

---

## Daily 20-Minute Operator Routine

1. Review **Morning Digest** (new filings, deadlines, research results)
2. Approve filing batch; tag any corrections (train rules)
3. Submit/approve 1–2 research requests
4. Update **Context Pack** with 1 new “keeper” cite or template line
5. Log gains in **[ROI Tracker]**

---

## Start-Here Fill-Ins

- **KPI:** ___ (Filing SLA / Memo time / Error rate) | **$ Target:** ___
- **Practice/Jurisdiction:** ___ (e.g., CA civil, NY commercial)
- **Naming rules link:** ___ | **Matter map link:** ___
- **Never-Do link:** ___ | **Access/Policy Matrix link:** ___
- **Daily caps:** filings ___ / day | memos ___ / day
- **Golden Samples link:** ___ | **Case Card link:** ___

---

**Notes:** Built for U.S. legal ops; swap terms/sources and this co-pilot works in other industries (finance, healthcare, compliance).