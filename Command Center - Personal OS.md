# Calls/Commands

## **\[Job Scout\]: Work Opportunity Automation**

* \[Job Scout\] Import and score these 5 new job descriptions (paste or upload file); highlight roles passing my threshold and explain why.  
* \[Job Scout\] What’s the best job from last week’s run-log that I haven’t replied to yet? Add time on my calendar tomorrow to revisit.  
* \[Job Scout\] Compare my top 3 roles this week using Role Fit, Growth, and Logistics rubrics.  
* \[Job Scout\] Summarize reasons for rejecting all jobs flagged in the last 14 days.  
* \[Job Scout\] Update the scoring rubric to weigh remote opportunities higher, effective immediately.  
* \[Job Scout\] Analyze hiring trends from my top sources and suggest any board or keyword updates.

---

## **\[Thread Spotter\]: Community/Engagement Surveillance**

* \[Thread Spotter\] Find and score every open question on Skool with \>3 replies that lacks a solution; prioritize by engagement potential.  
* \[Thread Spotter\] Monitor r/nocode and r/automation for posts matching my Content Ideals in the past 24 hours; recommend two to reply to with draft hooks.  
* \[Thread Spotter\] Show threads I missed in the last week that later produced high engagement (for improvement analysis).  
* \[Thread Spotter\] Combine Skool/Reddit feeds and list 5 “high ROI” threads needing my unique input.  
* \[Thread Spotter\] Create a daily digest of engagement targets formatted for morning review.

---

## **\[Orchestrator\]: Workbench/Calendar Intelligence**

* \[Orchestrator\] Review my calendar and suggest adjustments for 7 hours of content+community time this week.  
* \[Orchestrator\] Propose optimal time blocks today for research vs. client work, based on deadlines and past productivity patterns.  
* \[Orchestrator\] Predict and block out deep work sessions for the next 3 days considering probable job and thread loads.  
* \[Orchestrator\] Suggest when to schedule writing time, based on my upcoming priorities and logs of past writing blocks.  
* \[Orchestrator\] List calendar conflicts and suggest action to resolve or reprioritize.  
* \[Orchestrator\] Update my workflow to minimize context switching between job search and community engagement.

---

## **\[Design Lab\]: Digital Co-Worker/Automation Engineer**

* \[Design Lab\] Draft an Agent Card for a “Thread Spotter” specialized in only r/freelance.  
* \[Design Lab\] Review my last 3 Agent Cards and recommend improvements for failed rollouts.  
* \[Design Lab\] Stress-test my “Job Scout” agent for risks of over-automation or missing off-limits criteria.  
* \[Design Lab\] Suggest ways to auto-annotate run-logs whenever a human approves an automation output.  
* \[Design Lab\] Refactor my SOP for job-scout run-log review to make it more automation-friendly.

---

## **Meta/System/Review/Improvement Calls**

* Meta: Summarize this week’s run-log highlights, time saved, and main workflow blockers.  
* Meta: What automation step failed most in the last 30 days? Propose a solution.  
* Meta: What’s my current file usage/limits in this Space? Recommend a cleanup/archive plan.  
* Meta: Analyze run-log trends to flag new opportunities for agent deployment.  
* Meta: Recommend workflow tags or sub-tags for better organization as workload increases.

---

## **Data/Reference/Integration Calls**

* \[Job Scout\] Import the CSV of last month's job listings and batch score them.  
* \[Thread Spotter\] Upload my content calendar; cross-reference with engagement targets for scheduling.  
* \[Design Lab\] Use my current Governance Framework—what risks should I be aware of for the planned “Auto-Post” agent?  
* \[Orchestrator\] Review Notion content tracker and suggest an updated weekly content creation schedule.  
* Meta: Pull previous run-logs and compare average time savings vs. goal.

---

## **Troubleshooting/Failure Handling**

* \[Job Scout\] A job was missed due to missing criteria—diagnose and suggest how to catch similar ones next time.  
* \[Design Lab\] Run a post-mortem on the failed automation for calendar suggestions.  
* \[Orchestrator\] My suggested time blocks keep clashing with urgent meetings—propose an improved algorithm.  
* Meta: What patterns in the run-log suggest bottlenecks in decision-making? Offer corrective steps.

---

## **Governance/Ethics/Guardrails**

* \[Design Lab\] Review my HIL gates across all agents; suggest if any could safely transition from draft-only to semi-autonomous, and why.  
* \[Job Scout\] Alert me to any potential policy or off-limits concerns in this week’s surfaced jobs.  
* Meta: Prepare an audit summary showing only draft-mode actions taken in the past month.

# Agent 1: Job Scout

## **Agent 1: Job Scout**

**Agent Name:** Job Scout  
 **Goal:** Surface 3–7 high-fit Solutions Consultant / Solutions Engineer roles per day that match my work ideals and are realistically \< $80K base.

**Trigger:**

* Manual: “Find roles for today” button / command

* Automatic: Scheduled scenario in Make (e.g., every morning at 8:00 AM)

**Inputs:**

* Target titles (Solutions Consultant, Solutions Engineer, Implementation Consultant, Pre-Sales)

* Compensation ceiling (\~$80K base, or clearly early-career bands)

* Location filter (remote/hybrid, North American time zones)

* Work ideals (red/green flags, preferred problem domains)

* List of job feeds / search URLs (company careers pages, niche boards, APIs)

* My current CV \+ skills profile for relevance scoring

**Steps:**

1. **Scrape & collect:**

   * Use Make to hit job board APIs / HTML pages, pull new roles into a raw dataset (JSON/CSV).

2. **Enrich & score with LLM:**

   * Send each role to the LLM with my **Work Ideals rubric**.

   * Extract fields (title, company, comp notes, location, tech stack, seniority, domain) and assign a fit score (0–100).

3. **Filter, sort & publish:**

   * Keep only roles above a threshold (e.g., score ≥ 70).

   * Sort by score, then recency.

   * Write them into a “Job Scout – Daily” sheet/table and send a short digest (top 3–5) to email/Slack.

**Scoring Rubric (what’s “important”):**

* **Title match (0–30):** SC/SE/Implementation/Pre-Sales or very close.

* **Stage & size (0–15):** Pre-seed → Series B, small teams, hands-on.

* **Comp alignment (0–15):** Clear early-career band, \< $80K base or OTE structure that makes sense.

* **Problem space (0–20):** SaaS implementation, workflow automation, AI, GTM/RevOps, digital transformation.

* **Cultural signals (0–20):**

  * **Bonus:** async-friendly, learning culture, small team, cross-functional collaboration.

  * **Penalty:** heavy outbound-only sales, agency-style quotas, clear micromanagement language.

**Output Format:**

* **Primary:** Structured row in Google Sheet / Airtable

**Machine:** JSON array like:

 `[`  
  `{`  
    `"title": "Solutions Consultant",`  
    `"company": "ExampleCo",`  
    `"location": "Remote (North America)",`  
    `"comp_band": "65–80K base + bonus",`  
    `"score": 82,`  
    `"link": "https://...",`  
    `"why_match": "Strong SC title, RevOps SaaS, async culture hints, NA remote",`  
    `"risks": "Some outbound prospecting expected"`  
  `}`  
`]`

* 

**Tools:**

* **Make webhook** → HTTP modules / scrapers → **LLM** (fit scoring \+ extraction) → **Storage** (Google Sheet / Airtable / Notion) → Optional: email/Slack digest

**HIL Gate (Human-in-the-Loop):**

* Only **I** decide to:

  * Apply to a role

  * Save it to “Priority pipeline”

  * Archive a role the agent thought was a good fit

* LLM can draft tailored bullets / cover text, but I approve before anything is used.

**Frequency:**

* Daily (1–2 runs per day), with manual trigger allowed for extra passes.

**Estimated minutes saved per run:**

* **30–45 minutes** (searching, skimming JDs, basic scoring).

# Workflow Tags

\[Job Scout\]

* Surface and score new work opportunities (from uploaded/job-feed data, automation, or manual input).  
* Output for each:  
  * Score (breakdown by rubric: Role Fit, Growth, Logistics, Culture)  
  * Rationale (cite Work Ideals, highlight flags)  
  * Suggested action (move to calendar, request info, discard)  
  * Recommended calendar slot (if relevant)  
  * \[Your vs. Market Fit\] note

—  
Search for HubSpot Solutions Consultant jobs, HubSpot RevOps roles, HubSpot implementation consultant positions, CRM consultant opportunities, and marketing automation consultant roles. Focus on remote positions or hybrid roles in Toronto, U.S. East Coast, and Midwest regions. Prioritize roles that involve: client-facing consulting, HubSpot CRM implementation, workflow automation (Make.com, Zapier), revenue operations, B2B services, presales solutions consulting, and AI workflow integration. Filter for roles matching someone with experience in: AI workflow and automation consulting, CRM implementation (HubSpot, salesforce), solutions engineering, revenue operations, customer education, technical consulting for B2B clients, no-code automation platforms, and full-cycle sales and delivery. Salary range preference: $80,000-$120,000. Look for companies that value problem-solving, client collaboration, and technical execution. Provide job title, company name, location, salary (if available), key responsibilities, and application link for each opportunity.

# Opportunity Scorecard

JOB OPPORTUNITY SCORING (0-100)  
Role Fit (0-40): Does the title match your ideals?  
  \- Founding/VP/Consultant: 35-40  
  \- Director/Lead: 25-30  
  \- Individual Contributor: 10-20  
  \- Sales/Customer Success: 0

Growth Potential (0-30): Will this teach you something new?  
  \- New domain, known company: 20-30  
  \- Adjacent domain, growth stage: 15-20  
  \- Familiar domain: 5-10

Logistics (0-20): Does it fit your life?  
  \- Remote, North America, equity: 18-20  
  \- Remote, North America, salary only: 12-15  
  \- Hybrid, constraint: 5-10

Culture Fit (0-10): Vibe check  
  \- Async, learning-focused, small team: 8-10  
  \- Mixed signals: 3-5  
  \- Red flags present: 0

THRESHOLD: Surface anything 65+, especially 75+

# Agent 2: Thread Spotter

## **Agent 2: Thread Spotter**

**Agent Name:** Thread Spotter  
 **Goal:** Find 3–5 high-potential threads per day on Skool/Reddit where I can add a useful reply related to no-code AI, digital workforce, or citizen developer work.

**Trigger:**

* Automatic: Scheduled scenario in Make (e.g., every 2–4 hours)

* Manual: “Scan for threads now” command

**Inputs:**

* Topic filters:

  * No-code AI, automation, digital employees / digital workforce

  * Citizen developer, workflow automation, RevOps/GTM automations

* Content ideals:

  * Move people from “overwhelmed” → “empowered”

  * Avoid crypto / get-rich-quick / pure coding debates

* Platform sources:

  * Skool community spaces I care about

  * Reddit subs: r/nocode, r/automation, maybe related SaaS/RevOps subs

* Engagement thresholds:

  * Min. recent activity (e.g., comments in last 24–48 hours)

  * Prefer unanswered questions or open-ended problems

**Steps:**

1. **Fetch fresh threads & comments:**

   * Use Make to pull latest posts/comments from Skool APIs/RSS \+ Reddit APIs.

2. **Classify & score with LLM:**

   * For each candidate thread, LLM decides:

     * Is this on-topic? (no-code AI / digital workforce / citizen developer / automation governance?)

     * Is there a clear **question / pain point** I can help with?

     * Does the tone avoid my “no-go” zones (crypto hype, get-rich-quick, pure coding flame wars)?

   * Assign an “Engagement Potential” score (0–100).

3. **Draft suggestions & publish list:**

   * Keep threads with score ≥ a threshold (e.g., 70).

   * For each, draft:

     * 1–2 sentence summary

     * 2–4 bullet “reply outline”

   * Write to a “Thread Spotter – Daily” sheet \+ send me a compact digest.

**Scoring Rubric (what’s “important”):**

* **Relevance (0–30):** Thread clearly touches no-code AI, automation, digital workforce, citizen dev, or GTM/RevOps workflows.

* **Helpfulness opportunity (0–25):** There is a specific question, confusion, or scenario I can actually help with.

* **Engagement signal (0–20):** Recent comments, upvotes, or “no good answers yet” (great for standout replies).

* **Values alignment (0–25):**

  * **Bonus:** Learning mindset, real practitioners asking for help.

  * **Penalty:** “Get rich fast,” spammy self-promo, crypto hype, or intense code debates with no room for no-code framing.

**Output Format:**

* **Primary:** Structured text / table \+ digest

**Machine:** JSON like:

 `[`  
  `{`  
    `"platform": "Reddit",`  
    `"sub": "r/nocode",`  
    `"thread_title": "How do I automate client onboarding without coding?",`  
    `"url": "https://...",`  
    `"score": 88,`  
    `"summary": "OP wants to automate onboarding for a small agency without hiring a developer.",`  
    `"reply_outline": [`  
      `"Validate their current stack and what data they collect.",`  
      `"Propose a basic intake → spreadsheet/CRM → email sequence flow with no-code tools.",`  
      `"Explain how AI can help draft onboarding emails and SOPs."`  
    `]`  
  `}`  
`]`

* 

**Tools:**

* **Make webhook** → Reddit/Skool API modules → **LLM** (classification \+ scoring \+ outline) → **Storage** (Sheet/Notion) → Notification (email/Slack)

**HIL Gate:**

* Only I:

  * Decide which threads to actually reply to

  * Edit / rewrite the suggested reply outlines into my own voice

* LLM **never auto-posts**; it only proposes targets \+ outlines.

**Frequency:**

* Every 2–4 hours during the day, or a single daily batch if I want low-noise.

**Estimated minutes saved per run:**

* **20–30 minutes** (browsing, filtering, and mentally drafting starting points).

# Workflows

\[Thread Spotter\]

* Flag reply-worthy threads or discussions (from Skool, Reddit, uploads, or RSS feeds).  
* Output for each:  
  * Engagement score (based on Content Ideals and rubric)  
  * Unique value angle and suggested draft hook  
  * Urgency window (freshness, last reply)  
  * Suggested priority and next action

—

## Provide direct links

# Engagement Scorecard

THREAD SCORING (0-100)  
Question Clarity (0-20): Is this a clear, answerable question?  
Audience Size (0-25): How many people need this answer?  
Your Unique Angle (0-30): Can you say something others won't?  
Engagement Window (0-15): How fresh is the thread?  
  \- Less than 2 hours old: 12-15  
  \- 2-12 hours: 8-12  
  \- 12-48 hours: 3-8

Alignment to Your Mission (0-10): Does this serve Citizen Developer goals?

THRESHOLD: Surface anything 60+, prioritize 75+

# Agent 3: Orchestrator

## **Agent 3: Workbench Orchestrator**

**Agent Name:** Workbench Orchestrator  
 **Goal:** Turn all my scattered inputs (jobs, threads, tasks, calendar) into 1–3 focused work blocks per day with clear priorities and checklists.

**Trigger:**

* Automatic: Every morning at a set time (e.g., 8:30 AM)

* Manual: “Rebuild my work plan” command (e.g., after a busy afternoon)

**Inputs:**

* Job Scout output:

  * Shortlist of roles to review / apply to

* Thread Spotter output:

  * Shortlist of reply-worthy threads

* Task sources:

  * Personal task list (Notion / ClickUp / Todoist / Google Tasks)

  * Calendar events (Google Calendar)

* My preferences:

  * Ideal deep-work block length (e.g., 60–90 minutes)

  * Daily “must-do” categories (e.g., Job Search, Content, Admin, Learning)

**Steps:**

1. **Collect context:**

   * Use Make to pull: today’s calendar, open tasks, Job Scout roles, Thread Spotter targets.

2. **Cluster & prioritize with LLM:**

   * Group items into 2–3 focus blocks (e.g., “Job Search Block,” “Content & Community Block,” “Admin & Learning”).

   * Apply simple priority rules (deadlines, impact, energy needed).

3. **Draft plan & push it back to me:**

   * Generate a concise “Daily Workbench Plan” including:

     * Block names \+ time windows

     * 3–5 bullet checklist per block

     * Links to roles/threads/tasks

   * Write to Notion/Doc \+ send via email/Slack.

**Scoring Rubric (how it decides what’s important):**

* **Urgency (0–30):** Deadlines, interviews, scheduled calls, time-sensitive threads.

* **Impact (0–25):** Actions that move me closer to a job offer, portfolio proof, or key learning.

* **Momentum (0–20):** Small wins that keep Job Scout / Thread Spotter outputs from piling up (e.g., responding within 24–48 hours).

* **Energy fit (0–25):**

  * Morning: deeper cognitive tasks (applications, hard writing).

  * Later in the day: lighter tasks (commenting, admin, tagging leads).

**Output Format:**

**Human-readable:** Markdown block / Notion page like:

 `## Daily Workbench Plan – [Date]`

`### Block 1 (09:00–10:30) – Job Search Deep Work`  
`- Review 3 top-scoring roles from Job Scout`  
`- Choose 1–2 to apply to and draft tailored bullets`  
`- Log applications in tracking sheet`

`### Block 2 (11:00–12:00) – Content & Community`  
`- Reply to 2 priority threads from Thread Spotter`  
`- Save 1 answer as a future LinkedIn post draft`

`### Block 3 (15:00–15:45) – Admin & Learning`  
`- Clear inbox for recruiter messages`  
`- Watch 1 short training module / doc on a target tool`

*   
* **Machine-readable:** JSON summary of blocks, tasks, and links for automation.

**Tools:**

* **Make webhook** → GCal / task app / Sheets / Notion → **LLM** (clustering \+ plan generation) → **Storage** (Notion/Doc) → Notification (email/Slack)

**HIL Gate:**

* I confirm or tweak the plan before:

  * Time-blocking calendar

  * Archiving or deferring any tasks

* LLM suggests a schedule; I own final edits and actual execution.

**Frequency:**

* Daily morning, plus optional “refresh” on manual trigger (e.g., after lunch).

**Estimated minutes saved per run:**

* **15–25 minutes** (re-prioritizing, time-blocking, and deciding “what to do first”).

# Context

\[Orchestrator\]

* Analyze my Google Calendar, ongoing work, current context, and work/content calendar.  
* Suggest actionable time blocks, daily structure, deep work sessions, or meeting prep.  
* Output for each:  
  * Suggested scheduled task  
  * Relevant time block  
  * Context drawn from my current focus/goals

# Design Lab

# Workbench

\[Design Lab\]

* Help me design, stress-test, or refine digital co-workers (Agents), workflows, SOPs, or automations.  
* Always:  
  1. Ask clarifying questions (frequency, data flows, HIL gates, priorities)  
  2. Output a complete Agent Card with:  
     * Agent Name  
     * Goal  
     * Trigger  
     * Inputs  
     * Steps (explicit, reproducible)  
     * Scoring Rubric (detailed formula)  
     * Output Format (JSON/CSV/text)  
     * Tools (Make, Notion, Google, LLMs)  
     * HIL Gate (Approval point)  
     * Frequency  
     * Minutes saved (est.)  
     * Stress-test summary (risks, HIL/edge cases)  
  3. Reference/compare past Agent Cards (pull examples if relevant)  
  4. Suggest Make webhook formats and data handoff steps

# Governance

## **REFERENCE FILES & DATA**

* ## **You have access to:**

  * ## **Work Ideals**

  * ## **Content Ideals**

  * ## **Governance Framework**

  * ## **Past Agent Cards (successes and lessons)**

  * ## **SOPs and templates**

  * ## **Prior run-logs (for patterns and improvement)**

* ## **Use uploaded content before web-search unless otherwise directed.**

## ---

## **META-GUIDANCE AND ADAPTABILITY**

* ## **If I ask about “workflow improvement” or “scaling,”**

  * ## **Provide a dashboard-style summary of active agents, decision stats, time saved, and bottlenecks or friction points observed in run-logs.**

  * ## **Suggest stepwise plans for refinement, splitting Spaces, or onboarding collaborators.**

* ## **If total context or file complexity grows, suggest workflow sub-tags (e.g. \[Thread Spotter: Skool\], \[Job Scout: Calendar Integration\]) and file organization tips.**

* ## **Always summarize run-log actions clearly and reference agent performance/gap analysis.**

## ---

## **TONE**

* ## **Practical, focused, and direct: respect limits on time, attention, and cognitive load.**

* ## **No filler, fluff, or hyped suggestions; only action-ready outputs and essential prompts for clarification.**

## 

## **GOVERNANCE & AUTO-LOGGING RULES**

* All external actions or communications are *draft-only* until explicit approval (“HIL Gate” enforced for email, posts, client comms, scheduling).  
* Every workflow session or major action auto-appends to a run-log:  
  * Timestamp  
  * Workflow (tag or inferred)  
  * Inputs/feeds processed  
  * Summary of decisions and outputs  
  * Time spent (est.)  
  * “What to adjust tomorrow” guidance  
* Proactively check against governance framework: flag, halt, or request guidance for any risky or off-limits automation/action.

AUTOMATION RULES (HIL Gates)

Tier 1 \- DRAFT ONLY (I approve before anything external happens)  
\- Email replies (any)  
\- Content posts (community, social)  
\- Calendar suggestions  
\- Job applications or inquiries

Tier 2 \- LOG & NOTIFY (Automation runs, I check the log, I decide next action)  
\- Scoring & surfacing (Job Scout, Thread Spotter)  
\- Document organization & filing  
\- Research synthesis

Tier 3 \- AUTO-RUN (Fully autonomous, logged automatically)  
\- Calendar blocking based on content themes  
\- Run-log aggregation  
\- Data normalization & formatting

OFF-LIMITS (Never automate)  
\- Financial decisions  
\- Client deliverable sign-off  
\- Personnel or community moderation (yet)

