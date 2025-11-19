# NicheSnap (ICP Brief Builder)

Category: Prompt Vault

- Runbook
    
    # Niches & ICP Briefs — Free Pre‑Diagnostic (Free Access)
    
    ### 🚀 Copy‑Paste Starter Prompt (paste into GPT / Eko / Fellou)
    
    **Role:** You are the *Niches & ICP Briefs* assistant. Help the user surface and rank 5 ICPs based on their current **Offer Brief**. Respect robots.txt, avoid logins/paywalls, and pause for HIL before ranking.
    
    **If no Offer Brief is present, your very first reply must be this exactly:**
    
    > Great—before we research niches, paste your Offer Brief using this template.
    > 
    > 
    > ```yaml
    > offer_name: ""
    > promise: ""                 # Outcome in one line (what result, for whom, by when)
    > price_range: "$-$$$"        # e.g., "$497–$2,500"
    > time_to_value_days: 30       # how fast a customer sees results
    > channels_allowed: [email, dm, phone]  # what outreach you can run now
    > proof_assets: [case_study, demo, testimonial] # what proof you can show
    > do_not_serve: []             # who you will avoid for now
    > geographies: [US, CA]        # target regions (optional)
    > compliance_constraints: []   # e.g., HIPAA, FINRA, legal
    > quick_win_examples: []       # 1–3 examples of a 30‑day win you can ship
    > 
    > ```
    > 
    > **Or answer these 8 quick questions:**
    > 
    > 1. What’s the offer called?
    > 2. What specific result do you promise, for whom, in what timeframe?
    > 3. What price range will you charge?
    > 4. How fast can you deliver a visible win?
    > 5. Which channels can you use today (email/DM/phone)?
    > 6. What proof can you show (case study, demo, testimonials)?
    > 7. Any groups you should *not* serve yet?
    > 8. Any compliance or region limits?
    > 
    > Paste it here and say **APPROVE** when it looks right.
    > 
    
    **Normalize the Offer Brief** to this JSON before any research and echo it back:**
    
    ```json
    {
      "offer_name": "",
      "promise": "",
      "price_min": 0,
      "price_max": 0,
      "time_to_value_days": 30,
      "channels_allowed": ["email", "dm", "phone"],
      "proof_assets": [],
      "do_not_serve": [],
      "geographies": [],
      "compliance_constraints": [],
      "quick_win_examples": []
    }
    
    ```
    
    **Ask:** “Confirm this Offer Brief (Y/N).” If **Y**, proceed to C1. If **N**, ask what to edit and re‑echo.
    
    ---
    
    **What this is:** A copy‑paste framework (Notion/Skool ready) your members can use *before* the diagnostic to research markets, surface 5 promising ICPs, and rank them with a simple, ROI‑aware score. Works manually or with a browser‑agent (Fellou/Eko).
    
    **Outcome in 60–90 min:**
    
    - A CSV of 20–30 niche candidates.
    - 5 ICP briefs auto‑generated (or templated) and **ranked**.
    - 3 starter outreach angles per ICP.
    - A one‑page post labeled: **“5 ICPs ranked.”**
    
    ---
    
    ## Story beats (to match your demo language)
    
    - **Establishing:** Founder guessing niches.
    - **Subject × Perspective:** Agent scrapes public websites (no logins).
    - **Subject × Action:** Auto‑build ICP briefs (template below).
    - **Perspective × Action:** Run‑Log notes: *“5 ICPs ranked.”*
    - **Unique:** Right niche surfaced in minutes, with proof links.
    
    ---
    
    ## Quick Start (Manual — 45 min)
    
    **Start here if you’re not using an agent.**
    
    0) **Write your Offer Brief first** (use the YAML above). Keep it in your page as a reference.
    
    **Use if you don’t want to run an agent.**
    
    1. **Define offer constraints (5 min):** Price, time to value, proof you can show in 30 days, channels you can operate (email/DM/phone).
    2. **Create a Candidate Niches table (copy):**
    
    | Niche | Buyer role(s) | Avg deal size (guess) | Pain signals seen | Data access | Competition notes | Channels viable | 30‑day win idea | Sources |
    | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    1. **Search for signals (20 min):** Use free sources (list below). Look for: *pain in the open*, *buying triggers*, *budget clues*, *data availability*, *timeline urgency.* Add sources/links.
    2. **Score (10 min):** For each niche, 0–5 scale:
        - **Impact** (pain size, TAM proxy)
        - **WTP** (willingness‑to‑pay; price anchors visible?)
        - **Access** (emails/sites/directories available? CSV‑able?)
        - **Fit** (your proof/skills/assets match?)
        - **Effort** (lower is better; compliance, list building friction)
        
        **Score = (0.35×Impact) + (0.25×WTP) + (0.20×Access) + (0.15×Fit) − (0.15×Effort)**
        
    3. **Shortlist top 5** and fill the **ICP Brief** template (below). Post your ranked list + links.
    
    ---
    
    ## Agent Mode (Fellou/Eko) — Copy‑paste Blocks
    
    **Budget‑safe, free‑web only, robots.txt‑aware.**
    
    ### C1 — SOURCING & SIGNALS (Low‑credit)
    
    **INPUT:** The normalized **Offer Brief JSON** above (treat as constraints for search & scoring).
    
    **GOAL:** Produce `icp_candidates.csv` (20–30 rows) with signals + links. Then **pause for HIL approval.**
    
    **GUARDS:**
    
    - Max runtime 25 min; respect robots.txt; no logins/paywalls; no CAPTCHAs.
    - Rate‑limit: 1–2 req/sec; backoff on 429/403; stop on 5 consecutive errors.
    
    **ALLOWED SITES (examples):** Google advanced search, G2, Capterra, Clutch, Trustpilot, BBB, Glassdoor (public pages), YouTube case studies, vendor Pricing/Changelog/Status/Help‑center pages, gov/open data, Indeed (public job results pages), ProductHunt, GitHub READMEs, public Notion docs.
    
    **OUTPUT COLUMNS (CSV):**
    
    `niche,parent_vertical,buyer_roles,avg_deal_size_est,top_pain_quotes,buying_triggers,budget_clues,data_access_notes,channels_viable,compliance_flags,competition_notes,30d_win_idea,sources,impact_0_5,wtp_0_5,access_0_5,fit_0_5,effort_0_5,score`
    
    **STEPS:**
    
    1. Generate 3–5 parent verticals from the offer constraints.
    2. For each vertical, discover 5–10 sub‑niches via allowed sites using operators (`intitle:"case study"`, `site:clutch.co "[vertical]"`, `site:help.* OR /status OR /changelog`, `"pricing" + [tool]`, `"RFQ" OR RFP + [industry]`).
    3. Extract buyer roles, pain quotes, triggers (hiring, regulation, seasonality), budget clues (price pages, ACV mentions), data accessibility (directories/exports), channel viability (can we reach them?), competition notes, and a 30‑day win idea.
    4. Score with the formula above. **Write `icp_candidates.csv`** and **STOP for HIL.**
    
    **HIL PROMPT:** “Open the CSV → tick the KEEP column for any niches you want advanced. Then type CONTINUE.”
    
    ---
    
    ### C2 — BRIEF BUILDER & RANKER
    
    **GOAL:** Transform kept rows into 5 formatted ICP briefs + ranked CSV.
    
    **INPUT:** Filtered rows from `icp_candidates.csv` (KEEP==TRUE).
    
    **STEPS:**
    
    1. Cluster similar niches; keep the strongest rep.
    2. For each, fill the **ICP Brief** (below) using only CSV + allowed pages. Add 3 outreach angles and 3 asset ideas.
    3. Recompute **Score** and create a **Priority Matrix** tag: *Quick Win* (high score, low effort), *Big Swing* (high‑high), *Nice‑to‑Have*, *Deprioritize*.
    4. Output `icp_briefs.md` (all 5) + `icp_top5.csv` (ranked). Log: **“5 ICPs ranked.”**
    
    **DELIVERABLES:**
    
    - `icp_candidates.csv` → HIL
    - `icp_briefs.md` + `icp_top5.csv` → post summary + links
    
    ---
    
    ## ICP Brief — Pasteable Template
    
    ```
    # ICP: {{Niche name}}
    **Buyer roles:** {{titles}}
    **Deal size & cycle (est.):** ${{ACV}} • {{cycle}}
    **Where they hang out:** {{forums, directories, events}}
    
    ## Pain & Triggers (evidence)
    - Top pains (quotes or paraphrase + links)
    - Triggers (hiring spikes, regulation, seasonality, tech changes)
    
    ## Success Criteria (how they decide)
    - Must‑haves, objections, risks
    - Compliance/data constraints
    
    ## Stack & Data Access
    - Common tools (CRMs, inboxes, billing)
    - Public lists/directories (CSV‑able?)
    
    ## 30‑Day Win (small but real)
    - What we’d ship in 30 days
    - KPI to move & how to measure
    
    ## Messaging Angles (3)
    1. {{Angle #1}}
    2. {{Angle #2}}
    3. {{Angle #3}}
    
    ## Asset Ideas (3)
    - {{Asset 1}} (lead magnet or micro‑tool)
    - {{Asset 2}}
    - {{Asset 3}}
    
    ## Scorecard
    Impact {{0–5}} • WTP {{0–5}} • Access {{0–5}} • Fit {{0–5}} • Effort {{0–5}} → **Score {{calc}}** → **Priority: {{Quick Win / Big Swing / …}}**
    
    **Sources:**
    - {{link 1}}
    - {{link 2}}
    
    ```
    
    ---
    
    ## CSV Schemas (quick copy)
    
    **icp_candidates.csv** (headers):
    
    ```
    niche,parent_vertical,buyer_roles,avg_deal_size_est,top_pain_quotes,buying_triggers,budget_clues,data_access_notes,channels_viable,compliance_flags,competition_notes,30d_win_idea,sources,impact_0_5,wtp_0_5,access_0_5,fit_0_5,effort_0_5,score,keep
    
    ```
    
    **icp_top5.csv** (headers):
    
    ```
    rank,niche,buyer_roles,priority,score,30d_win_idea,top_angle,sources
    
    ```
    
    **Run‑Log row (for your wall‑of‑proof):**
    
    ```
    run_id,step,status,items,cost_est,ms,notes
    2025‑NICHES‑001,C2,OK,5,~$0.00,680000,"5 ICPs ranked"
    
    ```
    
    ---
    
    ## Free demo sources (no account)
    
    - Google advanced search (`site:clutch.co`, `site:g2.com`, `site:trustpilot.com`, `"case study" + industry`)
    - Clutch, G2, Capterra category + reviews pages
    - Trustpilot/BBB complaints (pain text)
    - Product “Pricing/Changelog/Status/Help” pages (budget & change signals)
    - Gov/open‑data portals (vendor/contract lists)
    - Indeed public job result pages (hiring = demand)
    - YouTube case studies and conference talks
    - GitHub READMEs (for dev‑tool niches)
    - Public Notion docs and Airtable bases shared by companies
    
    *(If a page requires login/paywall or disallows crawling, skip it.)*
    
    ---
    
    ## Priority Matrix (how to tag results)
    
    - **Quick Win:** High Score, Low Effort → start here for 30‑day ROI proof.
    - **Big Swing:** High Score, High Effort → roadmap item after quick win.
    - **Nice‑to‑Have:** Low impact, low effort → optional extras.
    - **Deprioritize:** Low impact, high effort → avoid.
    
    ---
    
    ## Skool classroom card (paste this)
    
    **Page — Niches & ICP Briefs (Free Pre‑Diagnostic)**
    
    **Learn (≤10m):** Why a tight Offer Brief + one best‑fit ICP multiplies ROI; how to spot pain, budget, and access in public data.
    
    **Execute (≤50m):** Paste the **Starter Prompt** into GPT/Eko/Fellou → it will ask for your **Offer Brief** → run C1→C2 → fill 5 ICP Briefs.
    
    **Deliverable:** Post `icp_top5.csv` + `icp_briefs.md` (or screenshots) titled **“5 ICPs ranked.”**
    
    **Metric:** ✅ Posted within 24h of joining.
    
    **Time discipline footer:** *Learn ≤10m • Execute ≤50m • Post proof + log metric.*
    
    ---
    
    ## Safeguards & Ethics
    
    - Respect robots.txt and site Terms. No logins or scraping behind paywalls.
    - Redact PII; aggregate insights, link to sources.
    - Add an **HIL pause** before ranking; humans own the final call.
    
    ---
    
    ## (Optional) Tiny example
    
    **Niche:** Property‑management SMBs (100–1,000 doors)
    
    **Buyer roles:** Owner/GM; Ops Manager
    
    **Top pains:** fragmented maintenance tickets; missed renewals (links)
    
    **30‑day win:** CSV intake → inbox triage → CRM tags; KPI: response‑time ↓ 30%
    
    **Score:** Impact 4.5, WTP 3.5, Access 4, Fit 5, Effort 2 → **Score 4.5 (Quick Win)**
    
    ---
    
    ### How to present it (for your demo)
    
    - Show the Candidate CSV → HIL checkbox → the 5 Briefs → Priority tags.
    - Close with the run‑log line **“5 ICPs ranked.”**
    - Invite them into the diagnostic to route to a 30‑Day path.