# Revenue Spine - Proposal Acceleration

Category: Playbooks

**Who this is for:** Construction & trades (GCs, remodelers, specialty subs).

**Note:** Same scaffold works in any industry—swap scope items, proof, and terms.

**Promise:** Send clear, on-time proposals, follow up like clockwork, and close faster—tracked in your **[ROI Tracker]** and **[Run-Log]**.

This is significantly easier to do with the 30 day roadmap as you’re provided with Run Cards, Agent Cards, and Lab Cards that help you bridge gaps without a heavy ideation lift. 

The below is meant to be simple to keep illustrative.

---

## Agent Scaffold (your “digital team”)

```
Inputs →  Estimator/Scoper → Proposal Writer → QA Gate → Sender → Scheduler
           │                  │                  │         │         │
           └──────────── Logger ←────────────────┴─────────┴─────────┘
                                 ↑
                           Compliance Sentinel

```

**Roles (plain English):**

- **Estimator/Scoper:** pulls notes, photos, drawings; lists line-items, allowances, exclusions, dates.
- **Proposal Writer:** turns scope into a branded, plain-English proposal with price bands/options.
- **QA Gate (HIL):** you approve/reject with reason tags (scope wrong, pricing off, missing docs).
- **Sender:** packages PDF/link, adds proof (reviews, project pics), and sends.
- **Scheduler:** books a review call, sets auto-reminders (3-touch cadence).
- **Logger:** writes every step to **Run-Log** (time, cost, pass/fail, reasons).
- **Compliance Sentinel:** enforces **Never-Do**, insurance/licensing notes, payment terms, and version control.

**Lives in:** n8n (flows), Fellou (agent runs), Kafka/Brainbase (when you need rock-solid reliability).

**Memory:** **Context Pack** in **[Link Hub]** (templates, price bands, proof/portfolio, terms, FAQs).

**Policy:** **Access/Policy Matrix** (caps, data rules, mandatory fields checklist).

---

## The Proposal Spine (qualified lead → signed scope)

1. **Aim (14-day win)**
    
    Pick 1 KPI: **time-to-proposal (TTP)**, **time-to-signature (TTS)**, or **proposal win-rate**. Add a $/margin target.
    
2. **Minimum Inputs (no guessing)**
    
    Client details, site/address, scope bullets, photos/drawings, desired start window, budget band, constraints (permits, access). **Mandatory fields or no send.**
    
3. **Price Bands (good/better/best)**
    
    Offer 2–3 clear options with inclusions/exclusions so clients can choose speed vs. scope.
    
4. **Proof Pack (trust quickly)**
    
    Insert 1–2 relevant photos, a short testimonial, and a one-line safety/insurance note.
    
5. **Follow-Up Rhythm (3 touches over 10 days)**
- **T1 (Send + Next Step):** “Here’s your proposal + a 10-min review link.”
- **T2 (Clarify + Option Nudge):** “Quick video walkthrough attached—option B reduces timeline by ~X days.”
- **T3 (Close the Loop):** “Hold this slot or release it? Happy to adjust allowances.”
1. **Version Control**
    
    Every edit stamps **v1, v2, v3** with change notes. No silent changes.
    
2. **Measurement (what gets logged)**
    
    TTP, TTS, opens/views, replies, revisions, won/lost reason. Push to **[ROI Tracker]** weekly.
    

---

## 14-Day Rollout (copy-paste checklist)

**Day 0–2 (Foundation)**

- Choose KPI + target → **[ROI Tracker]**
- Build **Mandatory Fields Checklist** (client, site, scope, photos, budget band, dates)
- Load **Context Pack**: proposal template, price bands, proof pack, terms (deposit, progress draws), FAQs
- Turn **HIL=ON**; set caps; attach **Never-Do** (no promises on permits/schedule beyond disclaimers)

**Day 3–5 (First Pass)**

- Feed 5–10 qualified requests → **Estimator/Scoper**
- **Proposal Writer** drafts → **QA Gate** approves → **Sender** ships T1
- Log TTP, opens, replies in **Run-Log**

**Day 6–10 (Iterate & Multiply)**

- Ship T2/T3 to non-responders
- Save **5 Golden Samples** (clean scope, tight options, clear terms)
- Tighten template based on questions you get repeatedly

**Day 11–14 (Scale Safely)**

- Raise daily proposal cap **only if**: **TTP ≤ 48h**, **QA first-pass ≥ 80%**, **errors = 0 material**
- Add quick **video walkthrough** step (60–90s loom) for top quotes
- Publish a **Case Card** with before/after and timeline

**Success (hit one):** **TTP ≤ 48h**, **Win-rate +10 pts**, or **$X in signed work**.

---

## Quality > Quantity (proposal rulebook)

**Targets before scaling:**

- **QA First-Pass Approvals:** ≥ **80%**
- **Proposal Error Rate:** **0** material errors (scope/price/address)
- **Open-to-Reply:** ≥ **35%**
- **Review-Call Book Rate:** ≥ **25%** of sends
- **Win-Rate:** +**10 pts** vs. baseline
- **Revisions per Win:** ≤ **2**

**Auto-brakes:**

- QA <80% → pause volume; fix template/checklist
- Open <35% (3 days) → change subject/preview; add 1-line outcome lead
- Errors >0 → freeze sends; root-cause (scope capture? math? template?)
- Revisions >2 on avg → add price-band explanation and “assumptions & exclusions” page

---

## Guardrails that prevent bad output

- **HIL stays ON:** Agent drafts → *You approve* → Send
- **Mandatory fields or no send** (block incomplete proposals)
- **Never-Do:** no hard promises on permits/subtrade availability; no “fixed start date” without deposit; no hidden exclusions
- **Plain English:** 200–400 words; bullets over paragraphs; one page + appendix if needed
- **Terms light but clear:** deposit %, progress draws, change-order policy, validity date, scheduling window
- **Compliance:** license/insurance statement; WSIB/COI on request (or your regional equivalent)

---

## Construction-specific notes (swap for your industry as needed)

- Include **site constraints** (access, hours, staging) and **assumptions** (material lead times).
- Offer **option B** that shortens timeline (materials or crew strategy).
- Add **change-order** paragraph (how price/time changes are handled).
- If public bid: track **bid deadline**, **addenda**, **RFI** timestamps in Run-Log.

---

## Operator Routine (20 minutes/day)

1. Check **Run-Log**: TTP, QA %, opens, replies
2. Approve today’s drafts (tag rejections: scope, price, terms, proof)
3. Book review calls for hot proposals (Scheduler)
4. Update **Context Pack** with one new Q&A or proof line
5. Update **[ROI Tracker]** (wins, $ signed, time saved)

---

## What you need

- **Mandatory Fields Checklist**, **Proposal Template**, **Price Bands**, **Proof Pack**
- **Terms page** (deposit, draws, validity, change orders)
- **Channel:** email + calendar link; optional 60–90s video walkthrough
- **Time block:** 20–30 min/day to approve drafts
- **Sheets:** **[Run-Log]**, **[ROI Tracker]**, **[Access/Policy Matrix]**, **[Case Card]**

---

### Start-Here Fill-Ins (paste into Notion)

- **KPI:** ___ (TTP / TTS / Win-rate) | **Target:** ___
- **Mandatory fields link:** ___ | **Template link:** ___
- **Price bands (G/B/B):** ___ / ___ / ___
- **Proof pack (review + photo):** ___
- **Terms (deposit %, draws, validity):** ___
- **HIL:** ON ✅ | **Daily proposal cap:** ___ | **QA target:** ≥ 80%
- **Follow-up cadence:** T1 send → T2 day ___ → T3 day ___
- **Golden Samples link:** ___ | **Case Card link:** ___

> Built for construction. Swap scope, proof, and terms—and this proposal engine works in any industry.
>