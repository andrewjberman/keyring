# Brief #1 -- Where we have been and how we scaled (November 2025 to October 2026)

Author: 4.0.0_SA_CRO~2026, 2026-10-04. Order: Andrew-direct 2026-10-04 ~19:4xZ, recorded verbatim at
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261004_194xZ_BRIEF1_WHERE_WEVE_BEEN_ONE_YEAR_SCALE_ONE_PAGER.md`.
Audience: Andrew, presenting to management. Companion one-page view: `YEAR_ONE_ONE_PAGER.html` in this folder (FILE).
Data cut: both repositories through 2026-10-03 (Eastern), all branches, merges excluded.

Claim labels used throughout: **measured** = read from git, a deploy tag or a deploy-ledger file; **inferred** = an
interpretation (for example, a schedule in infrastructure code read as "in production"). Every date in the tables
carries its evidence in the research files listed in section 9.

## 1. Bottom line

- **Volume:** 60,101 commits in under eleven months across the two repositories (57,098 workspace, 3,003 portal).
  Monthly volume went from 164 in December 2025 to 18,656 in September 2026, 114 times higher. Peak week: Sep 28,
  7,198 commits (measured).
- **Who built it:** Andrew alone from Nov 12, 2025 to Mar 1, 2026 (3,073 commits). An AI agent organization made its
  first commit on Mar 2, 2026 and has written 97 to 100% of commits every month since April (measured).
- **What exists now:** 17 portal pages in the navigation, 3 partner firms live on the portal plus a demo tenant,
  34 scheduled pipeline setups (up from 5 in February 2026), 199 tagged production releases of the portal since
  Feb 26, and about 2,816 cloud resources in the dependency graph, including 232 Lambdas (graph built 2026-10-04,
  not a direct AWS read).
- **What the growth is made of:** product-build commits (frontend, back end, data) rose about 15 times, from 136 in
  December to 2,038 in September. Most of the added volume is coordination and controls (49% of the year): task
  orders, governance records, audit logs and tooling that let dozens of agents work in parallel without breaking
  production. Present the total as activity, not output (section 8).

## 2. Commit volume, month over month (measured)

Both repositories, all branches, merges excluded. The kind of work is inferred from the files each commit touched,
using the same rules as the Daily Operating Report (`daily_reports/scripts/commit_census.py`).

| Month | All | Workspace | Portal | Product build | Plan, test, deliver | Coordination and controls | Unclassified | By Andrew | By agents | Agent seats | Agent identities |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Nov 2025 (from Nov 12) | 86 | 19 | 67 | 75 | 0 | 0 | 11 | 86 | 0 | 0 | 0 |
| Dec 2025 | 164 | 58 | 106 | 136 | 0 | 0 | 28 | 164 | 0 | 0 | 0 |
| Jan 2026 | 1,226 | 838 | 388 | 1,059 | 13 | 0 | 154 | 1,226 | 0 | 0 | 0 |
| Feb 2026 | 1,597 | 1,250 | 347 | 1,383 | 30 | 4 | 180 | 1,597 | 0 | 0 | 0 |
| Mar 2026 | 1,414 | 1,175 | 239 | 976 | 76 | 259 | 103 | 230 | 1,184 | 37 | 37 |
| Apr 2026 | 3,837 | 3,354 | 483 | 1,836 | 263 | 1,388 | 350 | 74 | 3,763 | 48 | 59 |
| May 2026 | 6,542 | 6,274 | 268 | 1,394 | 744 | 3,554 | 850 | 44 | 6,498 | 33 | 58 |
| Jun 2026 | 4,638 | 4,544 | 94 | 1,100 | 571 | 2,406 | 561 | 2 | 4,636 | 24 | 42 |
| Jul 2026 | 7,779 | 7,700 | 79 | 1,613 | 2,121 | 3,345 | 700 | 0 | 7,779 | 24 | 58 |
| Aug 2026 | 10,558 | 10,418 | 140 | 1,198 | 4,697 | 4,277 | 386 | 1 | 10,557 | 21 | 104 |
| Sep 2026 | 18,656 | 18,039 | 617 | 2,038 | 4,276 | 12,056 | 286 | 471 | 18,185 | 23 | 796 |
| Oct 2026 (to Oct 3) | 3,604 | 3,429 | 175 | 567 | 813 | 2,172 | 52 | 0 | 3,604 | 7 | 152 |

- "By Andrew" counts commits under Andrew's own git identity (opalinvest.com / opalcapital.com addresses). September's
  471 are under that identity, not under an agent serial.
- "Agent seats" counts standing agent roles (base serials, worker subagents excluded). "Agent identities" counts
  every distinct agent author string, including the disposable worker agents introduced on Sep 3 (771 so far).

## 3. How the build accelerated

| Phase | Months | What happened | Commits |
|---|---|---|---|
| Founder build | Nov 2025 to Feb 2026 | Andrew alone: news scanner, Market Overview and seven more analysis pages live by Jan 4, Advisor Intelligence on 49 Financial data, every Lambda moved under Terraform | 3,073 |
| Agents join | Mar to Apr 2026 | Agent organization from Mar 2; the portal deploys itself on every production push from Mar 23; first three partner firms live Apr 15 to 29 | 5,251 |
| An operating fabric | May to Jul 2026 | Model portfolios daily for every partner; the Opal gateway brings Teams, email and data into Claude; a deploy record for every cloud change; Schwab becomes 49 Financial's source of record | 18,959 |
| Scale | Aug to Oct 3, 2026 | A ten-step workflow with disposable worker agents; the Daily Operating Report; the Investor Reporting backend deployed | 32,818 |

Supporting growth curves (measured from git at each month end unless noted):

| Measure | Start | Now |
|---|---|---|
| Terraform files (infrastructure as code) | 4 (Dec 2025) | 550 (Oct 4) |
| Lambda source folders in the repo | 6 (Nov 2025) | 94 (Sep) |
| Terraform setups with a schedule | 5 (Feb 2026) | 34 (Oct 4) |
| Gold-layer data scripts | 43 (Feb 2026) | 403 (Oct 4) |
| Data domains with pipeline scripts | 1 (Nov 2025) | 11 (Sep) |
| In-house compiler tools | 4 (Apr 2026) | 98 (Sep) |
| Agent skills | 15 (May 2026) | 85 (Oct 4) |
| Agent role folders | 32 (Mar 2026) | 129 (Oct 4) |
| Portal production releases per month | 4 (Feb 2026) | 49 peak (Apr 2026) |
| Deploy-ledger records per month | 137 (Jun 2026, from Jun 12) | 562 (Sep) |
| Decisions recorded in the ledger | 140 (May 2026) | 617 (Sep) |
| Active project codes per month | 25 (Mar 2026) | 136 peak (Jul), 73 (Sep) |

Active projects peaked in July and fell while output rose: once the ten-step workflow and one-project-per-seat rule
arrived (September), the work moved into fewer, deeper projects.

## 4. Portal pages (built date measured; production date measured from deploy tags from Feb 26, 2026, a bound before)

| Page | Area | Built | In production | Status today |
|---|---|---|---|---|
| Market Overview (first page) | Insights | 2025-11-18 | by 2026-01-04 | Live, all partners |
| Model Portfolios | Insights | 2025-11-25 | by 2026-01-04 | Live, all partners |
| Positioning | Analysis | 2025-11-25 | by 2026-01-04 | Live |
| Factor Tilts | Analysis | 2025-12-04 | by 2026-01-04 | Live |
| Valuations | Analysis | 2025-12-05 | by 2026-01-04 | Live |
| Correlations | Analysis | 2025-12-05 | by 2026-01-04 | Live, Opal internal |
| Macroeconomics | Analysis | 2025-12-05 | by 2026-01-04 | Live |
| Capital Market Assumptions | Analysis | 2025-12-23 | by 2026-01-04 | Replaced by Investment Philosophy 2026-08-11 |
| Secure sign-in (4 pages) | Account | 2025-12-29 | by 2026-01-04 | Live |
| Advisor Intelligence | Insights | 2026-01-15 | by 2026-02-17 (Dev users); all internal 2026-04-01 | Live; partner editions below |
| Portfolio Management | Tools | 2026-01-19 | open 2026-02-25 | Live, internal |
| Data Refresh | Admin | 2026-01-19 | open 2026-02-25 | Live, admins |
| Trade Submission | Tools | 2026-01-20 | open 2026-02-25 | Live |
| Attribution | Analysis | 2026-02-09 | by 2026-02-17 | Live |
| Security Scanner | Tools | 2026-03-05 | 2026-03-05 | Live, internal |
| Ticket Center | Tools | 2026-07-14 | 2026-07-15 | Live, internal |
| Investment Philosophy | Analysis | 2026-08-11 | 2026-08-11 | Live, all partners |
| Investor Reporting (+ print view) | Insights | 2026-09-10 | 2026-09-15 | Internal preview |
| Security Analysis | Tools | 2026-09-11 | 2026-09-17 | Internal preview |
| Rival Funds (mcp.opalinvest.dev/rivalfunds) | Research site | 2026-09-30 | 2026-09-30 | Live behind company sign-in |
| Daily Operating Report (mcp.opalinvest.dev/sprint) | Operations site | 2026-08-28 | 2026-08-28 | Live behind company sign-in |

Partner editions of Advisor Intelligence: 49 Financial 2026-04-15, Inflection 2026-04-24, demo tenant 2026-05-28,
Cottonwood 2026-06-09 (all measured from deploy tags). Retired along the way: Business Overview/Asset Management,
Market Update, Causality Engine, Advisor Drilldown, the Client Detail sub-page and Submit a Request.

## 5. Partners

| Partner | Onboarded | Data platform | What was built for them |
|---|---|---|---|
| 49 Financial | Data present from 2025-11-18 (relationship predates the repos); live on the portal 2026-04-15 | Schwab (source of record since 2026-07-14), Black Diamond before | Black Diamond pipeline (Jan 13); Advisor Intelligence (Jan 15) and its own edition; partner sign-in (Mar 4); model-portfolio feeder (May 18); daily Opal ETF ownership (Jun 25); Schwab ingest verified (Jul 14) and Schwab-based Advisor Intelligence (Aug 19); Tax SMA work; Investor Reporting backend (Sep 10) |
| Inflection Wealth Management | Registered 2026-04-21; live on the portal 2026-04-24; onboarding complete 2026-05-22 | Orion, Orion Eclipse | Orion pipeline with about six years of history (May 7); Eclipse models (May 14); model-portfolio feeder (May 18); own Advisor Intelligence edition; daily Opal ETF ownership (Jun 23); two users signed in on production (Jun 29); Teams analyst started (Sep 30) |
| Cottonwood Capital Advisors | Registered, given access and smoke-tested 2026-04-29 | Black Diamond | Black Diamond pipeline (schedules Jun 9); Advisor Intelligence v1 (Jun 22); daily Opal ETF ownership (Jun 25); three users signed in on production (Jun 29); model portfolios (Jul); Opal Satellites on Positioning (Aug 26 to 28) |
| Demo tenant | Built 2026-05-21; live 2026-05-28 | Copy of 49 Financial data with personal details replaced | A safe environment for prospects |

Prospects named in the records but not signed: Canterbury and Ausdale. Data vendors brought in during the year:
Schwab and SmartX (from the start), FRED (Dec), Black Diamond (Jan), Seeking Alpha (Jan), Orion (Apr), Eclipse (May),
YCharts (May), Bloomberg (live intake Jul 15), Lusha (prospecting), Microsoft 365 (Teams, Outlook, SharePoint).

## 6. Pipelines (first code measured; "in production" is inferred unless a first run is cited)

| Pipeline | Serves | First code | In production |
|---|---|---|---|
| News scanner | Opal internal, portal | before 2025-11-18 | 2025-11-22 (production verification) |
| SmartX ingest | Opal | 2025-11-18 | 2026-01-03 |
| Black Diamond chain | 49 Financial | 2026-01-13 | 2026-02-12 (scheduled orchestration) |
| Seeking Alpha research scraper | Opal | 2026-01-22 | 2026-02-17 |
| Market prices for Market Overview | Portal | 2026-02-13 | 2026-02-23 |
| Orion chain | Inflection | 2026-04-21 | 2026-05-07 (first scheduled run) |
| Eclipse models | Inflection | 2026-05-14 | 2026-08-04 (own schedules) |
| Model portfolios (all partners) | All firms | 2026-05-18 | 2026-05-18 (schedule enabled, measured) |
| YCharts and FRED market data | Portal | 2026-05-21 / 2026-02-19 | 2026-05-21 |
| Black Diamond chain | Cottonwood | 2026-06-08 | 2026-06-09 |
| Opal ETF ownership per partner, monthly ownership report | All firms | 2026-06-23 | 2026-06-25 |
| Schwab custodian ingest | 49 Financial | 2025-11-18 | 2026-07-14 (first scheduled runs verified, measured) |
| ETF net assets | Opal ETFs | 2026-05-15 | 2026-07-13 (moved to the cloud) |
| Schwab-based Advisor Intelligence | 49 Financial | 2026-07-12 | 2026-08-19 (applied, measured) |
| ETF Positioning producer | Opal ETFs | 2026-08-24 | 2026-08-25 (first scheduled run proven, measured) |
| Opal Satellites | Cottonwood | 2026-08-27 | 2026-08-27 |
| Investor Reporting backend | All firms | 2026-09-10 | 2026-09-10 (cloud deploy, measured); not yet in client use |
| Research harvest | Opal research | 2026-09-11 | 2026-09-14 |
| Rival funds daily | Opal research | 2026-09-30 | Planned, not applied |

## 7. Systems

| System | Live | What it is |
|---|---|---|
| Portal in production | 2026-01-04 (inferred) | The advisor and client portal behind CloudFront |
| Terraform | 2026-02-02 pilot; all 43 Lambdas 2026-02-03 | Cloud resources defined in versioned code |
| AI agent organization | 2026-03-02 | Agent roles (CTO, COO, CVO, CRO, engineers) that plan, build and check work |
| Portal auto-deploy | 2026-03-23 | Every production push validates, builds, publishes and tags itself |
| Agent message broker | 2026-03-26 | How agents register, report status and hand off work |
| Compiler tools and dependency graph | 2026-04-07 (code) | In-house tools to search and map code and cloud before changing them |
| Governance layer and decision ledger | 2026-05-22 | A supervising agent and a numbered record of Andrew's decisions |
| Deploy record for every cloud change | 2026-06-12 | A change opens a record and closes only with proof |
| Opal gateway | 2026-06-23 | Teams, email and Opal data inside Claude, under each person's own access |
| Cross-device agent bus | 2026-07-02 (inferred) | Two machines running two agent teams in parallel |
| Bloomberg intake | 2026-07-15 | Bloomberg terminal data flowing in automatically |
| Daily Operating Report | 2026-08-28; nightly in the cloud from 2026-09-11 | mcp.opalinvest.dev/sprint |
| Ten-step workflow with worker agents | 2026-09-03 | One owner per step; disposable workers do the build steps |
| One naming standard | 2026-09-15 | Every storage home and resource name generated from one canon |
| Opal tool index and Opal Analyst | 2026-09-25 (inferred) | One catalog of Opal data for Claude, and a Teams-facing analyst |
| End of Day Teams assistant | 2026-10-02 | Drafts the End of Day post; sends only on Andrew's approval |

## 8. What not to claim (read before presenting)

- **Commits are activity, not output.** Say "the build rate rose 114 times" only next to the mix. Product-build
  commits rose about 15 times; the rest is coordination and control work.
- **Production dates before Feb 26, 2026 are bounds.** Portal deploy tags start that day; Jan 4, 2026 is the first
  recorded production release, and an earlier release cannot be ruled out.
- **Most pipeline "in production" dates are when a schedule entered the infrastructure code**, not a confirmed first
  run. Rows marked measured above cite a verified run or an applied change.
- **The news scanner and the 49 Financial relationship predate the repositories.** Their dates are the earliest git
  evidence, not their true start.
- **Investor Reporting and the research pack are not yet in client use.** Both are internal previews.
- **Many projects show "closed 2026-08-25"** in the registry. That is a bulk clean-up, not a delivery date.
- **Cloud footprint figures come from the dependency graph** built 2026-10-04, not a direct AWS read.
- **Not covered:** the opal_ai and mcportal repositories (not checked out on this machine) and the separate tradeops
  fabric.

## 9. Sources, method and how to rebuild

- Census and page: `build_year_one.py` (FILE) in this folder. It reuses `daily_reports/scripts/commit_census.py`
  `classify()` unchanged, reads `events.json` (FILE) for the curated events, computes every number the page states,
  and writes `YEAR_ONE_ONE_PAGER.html` (FILE) and `year_one_data.json` (FILE). Rebuild with
  `python build_year_one.py --until YYYY-MM-DD`.
- Research files with per-row evidence (commit hashes, deploy tags, ledger files): `research_portal_pages.md`,
  `research_partners_pipelines.md`, `research_systems.md` (FILES, this folder). Twenty-nine key dates were re-checked
  against git, tags or the ledger by this seat; all matched.
- Email recon (Andrew's Outlook, read-only, addendum ~20:0xZ): PENDING. The gateway's mail tools have not loaded in
  this session yet. Findings will be added as dated, non-personal facts only.
- Publishing: the one-pager is a local file today. Where it is published (an Opal route such as the /sprint site, or a
  private claude.ai page) is Andrew's call; nothing has been published.
