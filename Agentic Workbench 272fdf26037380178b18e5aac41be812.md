# Agentic Workbench

Category: Prompt Vault

## What it is

Agentic Workbench turns any messy request into a safe, repeatable browser-agent plan with built-in governance: automatic **request scoring**, **readiness gates (R/Y/G)**, **ROI math**, and **run-logs**. You paste the Workbench **system prompt** into a GPT project (works on any paid LLM); every time you ask for an agentic plan, it returns (A) a polished brief, (B) a runcard, and (C) a compact Fellou-ready block that also includes one-row **RUN_LOG** and **ROI_UPDATE** lines to paste into Sheets. No extra tooling required.

## Why it matters

- **Deterministic planning → fewer retries.** Semantic selectors, explicit waits, budgets, stop rules.
- **Score → gate → ship.** Request Quality Score (RQS) + Readiness R/Y/G stop you from “sending it” with missing context.
- **Proof on autopilot.** Hours saved, cost, approvals, incidents, and payback are logged every prompt—fuel for your ROI snapshots and case cards.

## Setup (5 minutes)

1. **Create a GPT project** → paste the “Agentic Workbench (v2) — System Prompt” below as the System message.
2. **Make/confirm two Sheets**
    - Paste this into [Fellou.ai](http://Fellou.ai) to create for you
    
    ```jsx
    meta:
      name: ROI-Logged RunCard v1
      version: 1.3.0
      owner: {{YOUR_NAME}}
      description: >
        Executes a governed task and auto-logs before/after + cost metrics into a Google
        Sheets ROI Tracker with live ROI/payback math. Idempotent and HIL-gated.
    
    permissions:
      - google.sheets: read_write
      - google.drive: read_only
      - http: outbound
    
    goal: <business outcome, 1 sentence>
    
    scores:
      rqs_0_100: <int>
      readiness: "<Green|Yellow|Red>"
    
    scope:
      allowed_domains: [<derive from URLs/text>]
      disallowed_domains: [youtube.com/shorts, tiktok.com, ads.*]
      auth_context: <public|requires_login|cookies_available?>
    
    inputs:
      sources: [<urls/files from request or inferred defaults>]
      constraints: [no PII, respect robots, rate-limits]
    
    budgets: { max_runtime_min: 20, max_clicks: 120, max_pages: 50 }
    
    reliability:
      hil_gate: true
      stop_rules: ["budget_exceeded","2_selector_misses","redteam_fail","hil_not_approved"]
      rollback_plan: "If extraction misses sections, re-run only missed segments"
      failure_tests: ["no target headings","blocked embeds","0 assets captured"]
    
    output_contract:
      type: <markdown|json|zip>
      shape: <schema/headings>
      must_include: [<task-specific checklist>]
    
    eko_hints:
      selectors: ["getByRole()", "getByLabel()", "text='Toggle'"]
      wait_strategy: "element-visible for targets; network-idle before capture"
      pagination: "deterministic loop (next button or infinite-scroll sentinel)"
      expand_toggles: true
      retry_policy: "2x with exponential backoff"
    
    prioritization:
      method: "Impact × Frequency × Ease (1–5 each)"
      backlog:
        - task: "<sub-task>"
          impact: <1-5>
          frequency: <1-5>
          ease: <1-5>
          ife: <impact*frequency*ease>
    
    roi_assumptions:
      hourly_rate_usd: 35
      rev_per_hour_usd: 100
      implementation_cost_usd: 0
      reallocation_rate: 0.50            # % of saved hours reallocated to revenue work
      runs_per_week: 5
    
    kpi_plan:
      kpi: <hours_saved|cycle_time|error_rate|revenue>
      baseline: <value or 'unknown'>
      target: <value or 'infer'>
    
    roi_logging:
      sink: "sheets"                      # sheets|webhook
      spreadsheet_id: "{{ROI_SHEET_ID}}"
      tabs:
        runlog: "RunLog"
        calcs: "ROI_Calcs"
        config: "Config"
      schema:
        runlog_columns: [
          "timestamp_iso",                # A
          "run_id",                       # B
          "task_name",                    # C
          "kpi",                          # D
          "n_items",                      # E
          "minutes_before",               # F  — measured baseline per item
          "minutes_after",                # G  — measured after per item
          "minutes_saved",                # H  =F-G (per item)
          "hours_saved",                  # I  =H/60 * n_items
          "hourly_rate_usd",              # J  from assumptions
          "tokens_in",                    # K
          "tokens_out",                   # L
          "api_cost_usd",                 # M  (tool-reported)
          "rev_per_hour_usd",             # N  from assumptions
          "reallocation_rate",            # O  from assumptions
          "runs_per_week",                # P  from assumptions
          "notes"                         # Q
        ]
      bootstrap:                          # creates tabs + named ranges if missing
        create_if_missing: true
        named_ranges:
          - { name: "CFG_HOURLY_RATE", tab: "Config", a1: "B1", value_from: "roi_assumptions.hourly_rate_usd" }
          - { name: "CFG_REV_PER_HOUR", tab: "Config", a1: "B2", value_from: "roi_assumptions.rev_per_hour_usd" }
          - { name: "CFG_IMPLEMENTATION_COST", tab: "Config", a1: "B3", value_from: "roi_assumptions.implementation_cost_usd" }
          - { name: "CFG_REALLOCATION_RATE", tab: "Config", a1: "B4", value_from: "roi_assumptions.reallocation_rate" }
          - { name: "CFG_RUNS_PER_WEEK", tab: "Config", a1: "B5", value_from: "roi_assumptions.runs_per_week" }
        calcs_tab_formulas:
          # Put headers in A1:F1 on ROI_Calcs; formulas start at row 2 and auto-fill
          - a1: "A2"
            formula: |
              =LET(
                L, RunLog!A:Q,
                mins_saved_per_item, INDEX(L,,8),
                items, INDEX(L,,5),
                hourly, INDEX(L,,10),
                revph, INDEX(L,,14),
                realloc, INDEX(L,,15),
                runs_wk, INDEX(L,,16),
                api_cost, INDEX(L,,13),
                weekly_hours_saved, (mins_saved_per_item/60)*items*runs_wk,
                annual_cost_savings, weekly_hours_saved*hourly*52,
                annual_rev_uplift, weekly_hours_saved*realloc*revph*52,
                annual_benefit, annual_cost_savings+annual_rev_uplift,
                impl_cost, Config!B3,
                roi_pct, IF(impl_cost=0, , (annual_benefit/impl_cost)*100),
                payback_days, IF(annual_benefit=0, , impl_cost/(annual_benefit/365)),
                HSTACK(weekly_hours_saved, annual_cost_savings, annual_rev_uplift, annual_benefit, roi_pct, payback_days)
              )
          - headers:
              tab: "ROI_Calcs"
              row: 1
              values: ["Weekly Hrs Saved","Annual Cost Savings ($)","Annual Rev Uplift ($)","Annual Benefit ($)","ROI (%)","Payback (days)"]
    
    run_plan:
      - id: preflight
        do:
          - check.budgets: { max_runtime_min: "@budgets.max_runtime_min" }
          - assert.hil_on: { flag: "@reliability.hil_gate" }
          - hydrate.config.from_sheet: { sheet: "@roi_logging.spreadsheet_id", tab: "Config", on_missing: "create" }
      - id: acquire_inputs
        do:
          - load.sources: "@inputs.sources"
          - derive.allowed_domains: true
      - id: execute_task
        do:
          - browse.extract.transform: { allowed_domains: "@scope.allowed_domains" }
      - id: compute_metrics
        do:
          - measure.time_per_item:
              kpi: "@kpi_plan.kpi"
              minutes_before: "@kpi_plan.baseline?~unknown"
              minutes_after: "<auto-measured or user-supplied>"
          - compute.delta:
              minutes_saved: "=minutes_before - minutes_after"
              hours_saved: "=minutes_saved/60 * n_items"
      - id: hil_gate
        when: "@reliability.hil_gate == true"
        do:
          - hil.request_approval: { summary: "KPI deltas + sample output", timeout_min: 10 }
          - on.reject: { goto: "rollback" }
      - id: write_outputs
        do:
          - emit.contract: "@output_contract"
      - id: log_run
        do:
          - if: "@roi_logging.sink == 'sheets'"
            then:
              - sheets.append_row:
                  spreadsheet_id: "@roi_logging.spreadsheet_id"
                  tab: "@roi_logging.tabs.runlog"
                  columns: "@roi_logging.schema.runlog_columns"
                  values:
                    timestamp_iso: "<now_iso>"
                    run_id: "<uuid>"
                    task_name: "<human-name-of-task>"
                    kpi: "@kpi_plan.kpi"
                    n_items: "<int>"
                    minutes_before: "<float>"
                    minutes_after: "<float>"
                    minutes_saved: "=minutes_before - minutes_after"
                    hours_saved: "=minutes_saved/60 * n_items"
                    hourly_rate_usd: "@roi_assumptions.hourly_rate_usd"
                    tokens_in: "<int>"
                    tokens_out: "<int>"
                    api_cost_usd: "<float>"
                    rev_per_hour_usd: "@roi_assumptions.rev_per_hour_usd"
                    reallocation_rate: "@roi_assumptions.reallocation_rate"
                    runs_per_week: "@roi_assumptions.runs_per_week"
                    notes: "<free text>"
          - sheets.ensure_calcs:
              spreadsheet_id: "@roi_logging.spreadsheet_id"
              tab: "@roi_logging.tabs.calcs"
              apply_formulas: true
      - id: readiness_update
        do:
          - compute.readiness:
              rules:
                green: "HIL=ON AND baseline_known AND budgets_set AND expected_roi_pct >= 100"
                yellow: "HIL=ON AND budgets_set AND baseline_known"
                red: "ELSE"
          - set.scores.readiness: "<Green|Yellow|Red>"
      - id: rollback
        do:
          - revert.partial_changes: true
          - note: "Rollback triggered due to @reliability.stop_rules"
    
    observability:
      runlog_fields: ["run_id","kpi","hours_saved","api_cost_usd","tokens_in","tokens_out","readiness"]
      alerts:
        on_fail: ["#ops-alerts"]
        on_budget_close: ["#ops-alerts"]
    
    notes:
      - "Drop your Google Sheets ID into roi_logging.spreadsheet_id."
      - "This card will build missing tabs/ranges and keep ROI_Calcs live as you run."
    
    ```
    

## Automatic scoring & gates (built into the prompt)

- **Request Quality Score (RQS 0–100)**
    
    20 goal clarity • 15 sources/URLs • 10 auth context • 15 constraints/policy • 10 budgets requested • 15 KPI/ROI target • 10 success criteria • 5 path hint.
    
    **Thresholds:** RQS ≥ 70 = proceed; 50–69 = **Yellow** (ask for 1-line clarifier in A)); < 50 = **Red** (force conservative defaults + tight budgets).
    
- **Readiness Gate (R/Y/G)**
    
    **Green** (all true): baseline present • KPI named • budgets set • HIL=ON. **Yellow** (missing one). **Red** (missing ≥2 or RQS<50).
    
- **Backlog Prioritization (IFE)**
    
    Each sub-task gets **Impact × Frequency × Ease** on 1–5; plan sorts by score (ties break to lower risk).
    
- **Run Quality Score (post-run 0–100)**
    
    Pass ratio (40) + selector stability (20) + budget adherence (20) + HIL approvals (20). Included as `notes` if you feed results back.
    

## ROI math (auto-computed per request with defaults you can override)

- **Direct savings:** `hours_saved_per_week × hourly_rate × 52`.
- **Revenue uplift (conservative):** `hours_saved_per_week × 0.5 × rev_per_hour × 52`.
- **Payback:** `implementation_cost / ((savings + uplift)/365)`.
    
    Defaults when missing: hourly_rate = $35; rev_per_hour = $100; implementation_cost = $0 for plan-only.
    

## How to use it (tiny)

Ask anything (“scrape and normalize 50 PM companies”, “QA red/amber issues on our G2 page”, etc.). The Workbench returns **A/B/C**. In **C**, copy the two CSV lines into your Sheets:

- **RUN_LOG_ROW** → paste to `Run_Log`.
- **ROI_UPDATE** → paste to `ROI_Tracker`.
    
    Ship the plan in Fellou; your governance is already attached.
    

---

# Agentic Workbench (v2) — System Prompt ✅ copy this into your GPT project

You are **Agentic Prompt Workbench (v2)**.

### MISSION

Turn any messy user request into a compact, Eko-aware prompt chain that Fellou can execute reliably, with **automatic scoring (RQS & R/Y/G), ROI math, and one-row run/ROI outputs** appended for Sheets.

### OUTPUT — emit **exactly** these 3 blocks (in order):

**A) POLISHED BRIEF (AGENTIC_BRIEF_v2 · YAML)**

```yaml
goal: <business outcome, 1 sentence>
scores:
  rqs_0_100: <int>
  readiness: <Green|Yellow|Red>   # based on baseline/KPI/budgets/HIL
scope:
  allowed_domains: [<derive from URLs/text>]
  disallowed_domains: [youtube.com/shorts, tiktok.com, ads.*]
  auth_context: <public|requires_login|cookies_available?>
inputs:
  sources: [<urls/files from request or inferred defaults>]
  constraints: [no PII, respect robots, rate-limits]
budgets: { max_runtime_min: 20, max_clicks: 120, max_pages: 50 }
reliability:
  hil_gate: true
  stop_rules: ["budget_exceeded","2_selector_misses","redteam_fail","hil_not_approved"]
  rollback_plan: "If extraction misses sections, re-run only missed segments"
  failure_tests: ["no target headings","blocked embeds","0 assets captured"]
output_contract:
  type: <markdown|json|zip>
  shape: <schema/headings>
  must_include: [<task-specific checklist>]
eko_hints:
  selectors: ["getByRole()", "getByLabel()", "text='Toggle'"]
  wait_strategy: "element-visible for targets; network-idle before capture"
  pagination: "deterministic loop (next button or infinite-scroll sentinel)"
  expand_toggles: true
  retry_policy: "2x with exponential backoff"
prioritization:
  method: "Impact × Frequency × Ease (1–5 each)"
  backlog:
    - task: "<sub-task>"
      impact: <1-5>
      frequency: <1-5>
      ease: <1-5>
      ife: <impact*frequency*ease>
roi_assumptions:
  hourly_rate_usd: <number or 35>
  rev_per_hour_usd: <number or 100>
  implementation_cost_usd: <number or 0>
kpi_plan:
  kpi: <hours_saved|cycle_time|error_rate|revenue>
  baseline: <value or 'unknown'>
  target: <value or 'infer'>

```

**B) EXECUTION PLAN (RUNCARD · Markdown)**

- **Preflight**: auth check • expand toggles • set viewport • confirm budgets & HIL.
- **Red-team mini-suite (run first)**: ① empty state ② oversized page/long DOM ③ 429/timeout → expect fallback. **STOP + HIL** on any fail.
- **Steps (numbered)**: each includes **target • action • selector/wait • fallback** (semantic locators only).
- **Assembler**: build artifact per `output_contract` exactly.
- **Stop rules**: **budget exceeded • 2 consecutive selector misses • red-team fail • HIL not approved**.

**C) FELLOU RUN — PASTE THIS (≤400 tokens)**

- **GOAL**:
- **BUDGETS + STOP**: runtime=, clicks=, pages=; stop=[budget_exceeded,2_selector_misses,redteam_fail,hil_not_approved]
- **DO (imperative, compact)**: numbered steps with role/text/label selectors + explicit waits; include pagination exit.
- **RED-TEAM (first)**: list quick checks.
- **OUTPUT**: schema (fields) + **one tiny sample record**.

Then append **two single-line CSV payloads** for Sheets (exact headers included):

```
RUN_LOG_ROW (CSV)
ts,run_id,agent,path,prompt_hash,rqs,readiness,budgets_runtime_min,budgets_clicks,budgets_pages,hil_on,redteam_ok,status,steps_ok,selector_miss,stop_rule,tokens_in,tokens_out,est_cost,ms,pages,assets,errors
<ISO8601>,<short-id>,<"Fellou">,<path_or_n/a>,<hash5>,<0-100>,<G|Y|R>,<int>,<int>,<int>,true,<T|F>,<planned>,<0>,<0>,<none>,<~>,<~>,<~>,<~>,<~>,<~>,<none>

```

```
ROI_UPDATE (CSV)
date,run_id,kpi,baseline_value,after_value,delta_value,hours_saved_wk,hourly_rate,est_cost_savings_annual,revenue_uplift_annual,implementation_cost,payback_days,notes
<YYYY-MM-DD>,<same-run-id>,<kpi>,<n|?>,<n|?>,<calc>,<calc>,<rate>,<calc>,<calc>,<cost>,<calc>,<RQS & gate summary>

```

### STYLE GUARDRAILS

Deterministic language only. Prefer role/label/text selectors. Always include waits & pagination exits. Shrink steps when budgets are tight; keep rollback specific.

### RESPONSE CONTRACT (must follow)

Emit **A**, **B**, **C** in that order—nothing else. If critical inputs are missing, infer safe defaults and proceed with **tight budgets**.

### SELF-CHECK BEFORE ANSWERING

- Budgets + STOP rules present? [Y/N]
- Role/text/label selectors + waits? [Y/N]
- Red-team before main flow? [Y/N]
- Output schema + one tiny sample? [Y/N]
    
    If any “N”, fix and re-emit.
    

---