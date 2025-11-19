# Revenue Spine - Reactivation

Category: Playbooks

**Who this is for:** Property services (HVAC, plumbing, electrical, cleaning, landscaping, roofing, pest, etc.).

**Note:** Same scaffold works in any industry—swap the segment labels, offer, and sources.

**Promise:** Re-open stalled quotes, no-shows, and cold accounts—book more callbacks with less manual work. Tracked in your **[ROI Tracker]** and **[Run-Log]**.

This is significantly easier to do with the 30 day roadmap as you’re provided with Run Cards, Agent Cards, and Lab Cards that help you bridge gaps without a heavy ideation lift. 

The below is meant to be simple to keep illustrative.

---

## Agent Scaffold (your “digital team”)

```jsx
Inputs →  Archivist/Researcher → Qualifier → Writer → QA Gate → Scheduler
            │                     │           │        │          │
            └────── Logger  ←─────┴───────────┴────────┴──────────┘
                                   ↑
                             Compliance Sentinel

```

**Roles (plain English):**

- **Archivist/Researcher:** pulls past quotes/leads from CRM, inbox, spreadsheets; fills gaps; captures prior-context (job type, date, quote #).
- **Qualifier:** bins by **recency & value** (Hot 0–90d, Warm 3–12m, Cold 12–36m, Dormant 36m+); checks consent/channel & ICP fit (service area, job size).
- **Writer:** drafts T1/T2/T3 reactivation touches using your **Context Pack** + prior notes.
- **QA Gate (HIL):** you approve/reject with reason tags (off-tone, wrong segment, too pushy, missing context).
- **Scheduler:** offers booking link/callback windows; passes warm replies to your calendar/dispatcher.
- **Logger:** records every step in **Run-Log** (time, cost, pass/fail, reason).
- **Compliance Sentinel:** enforces **Never-Do**, opt-outs, suppression lists, and send caps.

**Lives in:** n8n (flows), Fellou (agent runs), Kafka/Brainbase (when you need production-grade reliability).

**Memory:** **Context Pack** in **[Link Hub]** (services, service area, proof, objection notes, tone, templates).

**Policy:** **Access/Policy Matrix** (caps, spend, data rules, suppression lists).

---

## The Reactivation Spine (silent list → booked callbacks)

1. **Aim (14-day win)**
    
    Pick one KPI: **callbacks booked**, **positive replies**, or **revenue from re-opened jobs**. Add a simple $ target.
    
2. **Segment Map (who/when/how)**
- **Hot (0–90d):** “We quoted X on [date]—ready when you are.”
- **Warm (3–12m):** “Seasonal check—quick way to save/avoid failure.”
- **Cold (12–36m):** “Still relevant? Free 5-min estimate refresh.”
- **Dormant (36m+):** “We cleaned your file—want a no-cost tune-up snapshot?”
    
    Use the last consented channel (email/SMS/phone/DM).
    
1. **Offer & Hooks (easy yes)**
    
    One low-friction re-engagement offer + 3 angles: **seasonal timing**, **proof/case**, **quick win** (estimate refresh, maintenance check, tune-up credit).
    
2. **List Sources (where your past leads live)**
    
    CRM “stalled/closed-lost,” unbooked quotes, no-shows, web form fills, voicemail inbox, old estimate PDFs. Start with **50–150** contacts.
    
3. **Context Pack (what the agent must know)**
- Last touch summary (date, channel, service)
- Quote/estimate reference + objection noted (price, timing, scope)
- Current flagship offer line + proof (before/after, reviews)
- Do/Don’t list; approved templates **by segment & channel**
1. **Guardrails ON (accuracy > volume)**
    
    **HIL=ON**, daily send caps, step caps, **suppression lists**, strict opt-outs, and **Never-Do** (no scraping behind logins, no attachments on T1, no promises you can’t deliver).
    
2. **Agentic Browsing (supervised worker)**
    
    Confirms they’re still active at the same property/company, pulls a **fresh line** from their site/Google listing/LinkedIn to personalize, drafts, then **stops for approval**.
    
3. **Reactivation Rhythm (3 touches over 7–10 days)**
- **T1 (Context + Value):** “We quoted **[service]** on **[date]**—here’s a 30-sec update that reduces cost/risk.”
- **T2 (Proof + One Q):** “Since then, we did **[result]** for **[similar customer]**. Want a **10-min check-in**?”
- **T3 (Close the Loop):** “Still relevant or close the file? A quick **yes/no** is perfect. Opt-out anytime.”
1. **Measurement (what gets logged, improves)**
    
    Run-Log: sends, replies, opt-outs, bounces, bookings, reasons. **ROI Tracker:** hours saved, jobs re-opened, revenue recovered.
    

---

## 14-Day Rollout (copy-paste checklist)

**Day 0–2 (Foundation)**

- KPI + $ target → **[ROI Tracker]**
- Export lists; build **Suppression** (unsubs, dead domains, duplicates, competitors)
- Fill **Segment Map + Offer + Context Pack** → **[Link Hub]**
- Turn **HIL=ON**; set **caps/steps/budgets**; attach **Never-Do** & Compliance notes

**Day 3–5 (First Pass)**

- Load **50–150** contacts; auto-bin segments
- Run **Archivist → Qualifier → Writer** → **QA Gate** → send **T1**
- Log all sends/replies in **Run-Log**

**Day 6–10 (Iterate & Multiply)**

- Send **T2/T3** to engaged
- Add one **new reactivation source** (no-shows, closed-lost >$X)
- Save **5 Golden Samples** per segment; train Writer to mirror

**Day 11–14 (Scale Safely)**

- Raise caps only if **Approval ≥70%** and **Opt-out ≤0.2%**
- Turn on **Scheduler** (self-booking/callback windows)
- Export a **Case Card** (before/after, screenshots, re-opened $)

**Success (hit at least one):** **8+ re-opened conversations**, or **3+ callbacks**, or **$1,000 recovered**.

---

## Quality > Quantity (reactivation rulebook)

- **Approval (HIL):** ≥ **70%** first-pass
- **Positive Reply Rate:** **6–12%** (warmer lists reply more)
- **Bounce Rate (email):** ≤ **2%** (older lists need hygiene)
- **Opt-out/Spam:** ≤ **0.2%** / 1,000 sends
- **Show Rate:** ≥ **50%** of booked callbacks show
- **Re-open → SQL:** **25–40%**

**Daily caps (earn scale):** Days 1–3: **20–30** T1/day → Days 4–7: **40–60**/day if green → Week 2+: **+20%/day max**

**Auto-brakes:**

Approval <70% → pause & fix templates/context • Bounce >2% → verify/remove stale domains; switch to phone/SMS/form • Opt-out >0.2% → stop; soften copy; widen spacing; confirm consent • PRR <6% (3 days) → rewrite first line (12–18 words) with a concrete **because-line** tied to their last context.

---

## Guardrails that prevent bad output

- **HIL stays ON:** Agent drafts → *You approve* → Send
- **Reject with reason tags:** wrong segment / off-tone / too salesy / missing prior-context
- **Never-Do:** no behind-login data; no T1 attachments; no pressure language
- **Length & tone:** 70–110 words; one idea; one ask; cite **prior touch** + **one fresh proof**
- **Compliance (US/CA basics):** clear identity, easy opt-out, honor within 24h; consent checks for SMS/email

---

## The **Orchard** Model (revive → nurture → rotate → harvest)

- **Revive:** load past quotes/leads with last-touch + objection notes; confirm consent
- **Nurture:** 3-touch cadence; spot-check **10%** profiles & drafts
- **Rotate:** weekly change **segment**, **template**, **micro-offer** (e.g., “pre-season tune-up”)
- **Harvest:** daily goal = **2–3 warm replies** or **1–2 callbacks** at current cap
- **Weekly 30-min:** update winning lines, prune stale segments, add a new source (no-shows last quarter)

---

## Simple QA Score (1–5⭐ per draft)

**Prior-Context • Clarity • Value • Trust • Compliance**

**Send only 4–5⭐.** 3⭐ = rewrite. 1–2⭐ = fix segment/template.

---

## Operator Routine (20 minutes/day)

1. Check **Run-Log** KPIs (Approval, PRR, Bounce, Opt-out, Show Rate)
2. Approve drafts (tag rejections)
3. Add 20–30 reactivation records (rotate segments)
4. Update **Context Pack** (one winner line or objection)
5. Log outcomes → glance **[ROI Tracker]**

---

## What you need

- **Segment Map** (Hot/Warm/Cold/Dormant), **Suppression List**, **Consent Notes**
- **Offer:** one-line re-engagement + one proof (review/testimonial/before-after)
- **Channels:** inbox/phone/DM you control
- **Time block:** 20–30 min/day for approvals
- **Sheets:** **[ROI Tracker]**, **[Run-Log]**, **[Access/Policy Matrix]**, **[Case Card]**

---

### Start-Here Fill-Ins (paste into Notion)

- **KPI:** ___ | **$ Target:** ___
- **Segments in scope:** Hot / Warm / Cold / Dormant (circle)
- **Offer (1 line):** ___ | **Quick Win (refresh/tune-up/credit):** ___
- **Channel per segment:** Hot ___ | Warm ___ | Cold ___ | Dormant ___
- **HIL:** ON ✅ | **Send cap/day:** ___ | **Max pages/run:** ___
- **PRR floor:** ≥ ___% | **Bounce ceiling:** ≤ 2% | **Opt-out ceiling:** ≤ 0.2%
- **Suppression list link:** ___ | **Golden Samples link:** ___
- **Reactivation sources loaded:** CRM / Inbox / No-shows / Closed-Lost / Other ___
- **Context Pack link:** ___ | **Review time (daily 20m):** **:**

> Built for property services. Plug in your trade, area, and offer—and you can run this same system in any market.
>