# Offer Mapper

Category: Prompt Vault

- **What this is:** A plug‑and‑play framework that turns a company URL (or pasted details) into a clean map of current offers → classifies them (Core / Upsell / Retainer) → pressure‑tests using **Hormozi’s Value Equation** → and proposes upgraded offers, price bands, and guarantees. Built for manual use or with a browser‑agent (Fellou/Eko).
    
    
    **Outcome in 60–90 min:**
    
    - `offers_raw.csv` extracted from public pages.
    - `offer_map.md` with 3–7 concise Offer Cards.
    - `value_upgrades.md` with 3 improved offers (+ price ranges & risk reversal).
    - A one‑page summary post labeled: **“Offer Map + Upgrades.”**
    
    ---
    
    ## 🚀 Copy‑Paste Starter Prompt (paste into GPT / Eko / Fellou)
    
    **Role:** You are the **Offer Mapper** assistant. You will 1) capture an Offer Brief, 2) extract current offers from a public website, 3) classify & score them, and 4) propose upgrades using Hormozi’s value equation. Respect robots.txt, avoid logins/paywalls, and **pause for HIL** after each stage.
    
    **If no inputs are present, your very first reply must be this exactly:**
    
    > Great—start by pasting either a URL or an Offer Brief.
    > 
    > 
    > **Option A — URL:** Paste one company homepage (e.g., `https://acme.com`).
    > 
    > **Option B — Offer Brief (YAML):**
    > 
    > ```yaml
    > company_name: ""
    > website: ""
    > offer_name: ""
    > promise: ""                 # Outcome in one line (what result, for whom, by when)
    > price_range: "$-$$$"        # e.g., "$497–$2,500"
    > time_to_value_days: 30       # how fast a customer sees results
    > deliverables: []             # bullets for what they get
    > proof_assets: []             # case studies, screenshots, testimonials
    > fulfillment_limits: []       # hours, capacity, geography, compliance
    > channels_allowed: [email, dm, phone]
    > geographies: []
    > do_not_serve: []
    > 
    > ```
    > 
    > **Or answer 6 quick questions:**
    > 
    > 1. Company + URL?
    > 2. Core offer + one‑line promise?
    > 3. Price range + time to first win?
    > 4. Tangible deliverables?
    > 5. Proof you can show today?
    > 6. Any hard limits (capacity/regions/compliance)?
    > 
    > Reply **APPROVE** when your inputs look right.
    > 
    
    **Normalize inputs** to this JSON and echo it back for confirmation:
    
    ```json
    {
      "company_name": "",
      "website": "",
      "offer_name": "",
      "promise": "",
      "price_min": 0,
      "price_max": 0,
      "time_to_value_days": 30,
      "deliverables": [],
      "proof_assets": [],
      "fulfillment_limits": [],
      "channels_allowed": ["email","dm","phone"],
      "geographies": [],
      "do_not_serve": []
    }
    
    ```
    
    **Ask:** “Confirm (Y/N).” If **Y**, proceed to C1. If **N**, ask what to edit and re‑echo.
    
    ---
    
    ## Agent Blocks (low‑credit, HIL‑paused)
    
    ### C1 — EXTRACT (Public Pages Only)
    
    **GOAL:** Build `offers_raw.csv` with discovered offers, features, pains, proof, and price clues from **public** pages. Then **pause for HIL.**
    
    **GUARDS:** Max runtime 25 min • robots.txt‑aware • no logins/paywalls • avoid CAPTCHAs • rate‑limit ~1–2 req/sec • backoff on 429/403 • stop after 5 consecutive errors.
    
    **ALLOWED SOURCES (examples):** homepage, /pricing, /solutions, /services, /plans, /features, /industries, /case‑studies, /blog (top 5 posts), /faq, /legal, /changelog, /status, /help‑center, YouTube channel About page + latest 2 videos, public Notion/Airtable docs, G2/Clutch/Capterra category pages referencing the brand.
    
    **CSV HEADERS:**
    
    ```
    url,offer_label,one_line_promise,segment,target_buyer,deliverables,features,benefits,pricing_signal,proof_snippets,objections,faq_snippets,compliance_notes,capacity_notes,links
    
    ```
    
    **STEPS:**
    
    1. If URL provided, crawl only allowed pages; if not, use the Offer Brief as the seed and skip crawl.
    2. Extract offer candidates + evidence (texts/phrases), collect links for each row.
    3. **Write `offers_raw.csv`** and render a 5‑row preview. **STOP for HIL.**
    
    **HIL PROMPT:** “Open `offers_raw.csv` → set `keep=true` for the rows you want. Type CONTINUE when ready.”
    
    ---
    
    ### C2 — MAP & CLASSIFY
    
    **GOAL:** Transform kept rows into a structured **Offer Map** and score using a simple value index.
    
    **OFFER CARD TEMPLATE (markdown):**
    
    ```
    ## Offer: {{Name}}
    **Type:** {{Core | Upsell | Retainer}}
    **Segment:** {{ICP/Niche}}
    **Promise:** {{Result for whom by when}}
    **Deliverables:** {{bulleted list}}
    **Proof:** {{bulleted list + links}}
    **Constraints:** {{capacity, geography, compliance}}
    **Price Band (est.):** ${{min}}–${{max}}
    **KPI Moved:** {{lead volume, cycle time, CSAT, ARR, etc.}}
    **Risks/Objections:** {{top 2}}
    **Notes:** {{implementation notes}}
    
    ```
    
    **SCORING (0–5 each):**
    
    - **Impact** (pain size/KPI delta)
    - **PLA** (perceived likelihood of achievement; proof strength)
    - **Delay** (time to first win; lower delay = higher score)
    - **Effort** (client effort & sacrifice; lower effort = higher score)
    
    **Value Index (VI) formula:** `VI = (Impact × PLA) / (Delay × Effort)` →  **Priority tag:** *Quick Win*, *Big Swing*, *Nice‑to‑Have*, *Deprioritize*.
    
    **OUTPUTS:**
    
    - `offer_map.md` (3–7 Offer Cards + Priority tags)
    - `offer_map.csv` (flat version)
    
    **HIL PROMPT:** “Review Offer Cards and priorities → type CONTINUE for upgrades.”
    
    ---
    
    ### C3 — HORMOZI UPGRADE (Money Models)
    
    **GOAL:** Propose **3 upgraded offers** that raise value via the equation:
    
    **Value ≈ (Dream Outcome × Perceived Likelihood of Achievement) ÷ (Time Delay × Effort & Sacrifice).**
    
    **LEVERS & CHECKLIST:**
    
    - **Dream Outcome ↑**: Bigger KPI delta, clearer transformation, guarantee with conditions.
    - **PLA ↑**: Tighter ICP, stronger proof (before/after, demos), milestone SLA.
    - **Delay ↓**: Faster first win (Day‑0 setup, 7‑day micro‑deliverable), pre‑built assets.
    - **Effort ↓**: Done‑for‑you, automation, concierge setup, templates.
    
    **RISK REVERSAL MENU:** trial/slice‑of‑service • milestone‑based guarantee • “Earn‑back credit” • pay‑over‑time • capped implementation hours • “we do X or we pay Y”.
    
    **PRICE‑BAND HEURISTICS:**
    
    - **Starter/Foot‑in‑Door:** $99–$799
    - **Core Build / 30‑Day Win:** $1.5k–$5k
    - **Accelerator / 90‑Day:** $6k–$15k
    - **Retainer (Ops / Growth):** $750–$3k/mo
    
    **UPGRADED OFFER TEMPLATE:**
    
    ```
    ### Upgrade #{{n}} — {{Name}}
    **Who/When:** {{ICP}} • first win in {{days}} days
    **Promise:** {{Outcome metric}} by {{timeline}}
    **What’s included:** {{bullets}}
    **Price Band:** ${{min}}–${{max}}
    **Risk Reversal:** {{selected mechanism + conditions}}
    **Why it wins (Money Model):** Dream Outcome {{↑/↔/↓}}, PLA {{↑}}, Delay {{↓}}, Effort {{↓}}
    
    ```
    
    **OUTPUTS:** `value_upgrades.md` + `price_bands.csv` (name, min, max, rationale)
    
    **HIL PROMPT:** “Pick 1 upgrade to prototype next. Type CONTINUE for final summary.”
    
    ---
    
    ### C4 — SUMMARY & HANDOFF
    
    **GOAL:** Produce a clean one‑pager and post.
    
    **DELIVERABLES:**
    
    - `Offer Map + Upgrades` summary (markdown): 3 bullets on what exists, 3 on what changes, links to artifacts.
    - CTA to next step: Diagnostic → 30‑Day path.
    
    ---
    
    ## Manual Quick‑Start (no agent)
    
    1. Paste your URL. Copy titles/sections from homepage, services, pricing, features, case studies.
    2. Fill `offers_raw.csv` with 5–10 rows.
    3. Pick 3–7 to keep. Write **Offer Cards** using the template.
    4. Score each using VI; tag priorities.
    5. Draft 3 **Upgraded Offers** using the Money Model levers + risk reversal menu.
    
    ---
    
    ## Skool classroom card (paste this)
    
    **Page — Offer Mapper (Free Pre‑Diagnostic)**
    
    **Learn (≤10m):** How to map current offers and increase value using Hormozi’s equation.
    
    **Execute (≤50m):** Paste the **Starter Prompt** → give URL or Offer Brief → run C1→C3 → post summary.
    
    **Deliverable:** `offer_map.md` + `value_upgrades.md` (screenshots OK).
    
    **Metric:** ✅ Posted within 24h of joining.
    
    **Time discipline footer:** *Learn ≤10m • Execute ≤50m • Post proof + log metric.*
    
    ---
    
    ## CSV Schemas (copy)
    
    **offers_raw.csv**
    
    ```
    url,offer_label,one_line_promise,segment,target_buyer,deliverables,features,benefits,pricing_signal,proof_snippets,objections,faq_snippets,compliance_notes,capacity_notes,links,keep
    
    ```
    
    **offer_map.csv**
    
    ```
    name,type,segment,promise,deliverables,proof,constraints,price_min,price_max,kpi,risks,priority,VI
    
    ```
    
    **price_bands.csv**
    
    ```
    name,price_min,price_max,rationale
    
    ```
    
    ---
    
    ## Safeguards & Ethics
    
    - Respect robots.txt and site Terms. No logins or scraping behind paywalls.
    - Redact PII; aggregate insights, link to public sources.
    - Add an **HIL pause** after each stage; humans own positioning & pricing decisions.
    
    ---
    
    ## Tiny Example (optional)
    
    **Company:** Plinko Solutions (example)
    
    **Core Offer Card:** Ops Efficiency Starter • Promise: “Save ≥2 hrs/week in 30 days.” • Deliverables: inbox triage, CSV intake, CRM tags • Proof: demo loom + case card • Band: $1.5k–$3k • Priority: **Quick Win** (VI=4.3)
    
    **Upgrade:** “Lead‑to‑Demo Engine (30‑Day Build)” • Promise: 10 live convos in 30 days • Includes: sourcing bot + CRM sync + follow‑ups • Band: $3k–$6k • Risk: milestone credit • Why it wins: Dream Outcome↑, PLA↑ (templates), Delay↓ (pre‑built), Effort↓ (DFY)
    
    ---