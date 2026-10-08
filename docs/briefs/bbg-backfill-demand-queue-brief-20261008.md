---
title: "L1 BRIEF -- the market-data demand queue: every backfill and daily pull, counted in cells, routed to Bloomberg or Yahoo Finance by surface, inside known reserves"
date: 2026-10-08
author: 4.0.0_SA_CRO~Z (site Z)
status: L1 brief, NEW
for: DELL1's 1.0.0_SA_CTO (step 2, /endpoint --forward), via 0.0.0_AB_MSTR~Z -> DELL1's 0.0.0_AB_MSTR
companion: the DELL2 CRO's analysis of ADVI_COTBKF and the Cottonwood ADVI/IRPT surfaces (Andrew-direct; obtained by DELL1's MSTR)
project: NONE-YET (DELL1's CTO registers it at L3)
tags: [backfill, demand-queue, bloomberg, bbg, yfinance, yahoo-finance, cells, quota, reserves, daily-capacity, BQL, rate-limit, security-resolution, rivalfunds, positioning, ADVI, IRPT, COTBKF, cottonwood, SECCLASS, SECHIST, AMGT_CORPUS, induction, bbg_budget]
---

# L1 BRIEF -- the market-data demand queue

Find me by: backfill queue, demand queue, Bloomberg quota, Bloomberg cells, daily capacity, BQL blocked, Yahoo Finance
rate limit, yfinance, security resolution, which vendor per surface, reserves, fixed daily quota, where the quota goes.

## Andrew's words, verbatim

Record: `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20261008_18xxZ_BACKFILL_DEMAND_QUEUE_PROJECT_BRIEF_TO_DELL1.md`.

> "there is a lot of backfill that is being required shortly, for the rivalfunds ops, for the "Positioning" performance
> views, for the backfill on ADVI and IRPT surfaces as new clients come in bringing in more securities that are summarily
> classified and ingested. We need to start understanding our demand ops as it relates to these surfaces because we may
> need to start being more clever with how we script these ingestions, truly pulling in whatever we actually truly need,
> and developing our reserves."

> "Yes we are going to need a backfill demand queue project ... there are multiple layers to it that we need to account
> for, e.g. resolving securities, whether we go to BBG or YFinance and associated methodology per surface, api rate
> limiting on yfinance and cell limits and management on BBG as well as tracking daily jobs that we have to account for
> as fixed quota utilization, and where that quota is going. This needs to be built out into a full project ... the
> project is going to get set up on that box and proceeded."

His unit: **"cells" as in every row and column/field as a single cell.**

---

## PART I -- THE OUTCOME TERRITORY

### I.0 The candidate thread (one journey, end to end)

**One new Cottonwood security arrives, and its history lands without anyone hand-running a pull.** A Cottonwood account
brings a security Opal has never priced. The security is resolved to one identity, routed to Bloomberg or Yahoo Finance
by the rule for the surface that needs it, queued with its cell cost, drawn inside the day's spare capacity after the
fixed daily jobs, and the ADVI/IRPT surface that asked for it shows its history. Coarse grain: one firm (Cottonwood), one
new security, the history depth that surface needs. It becomes FWD-1 at L2. The DELL2 CRO's analysis is the detail of
this journey's Cottonwood half.

### O1 -- An operator sees, in cells, what every job pulls each day and what it costs

An operator opens one view and reads, for every recurring pull on every box, the cells it drew, by vendor and by
channel (Bloomberg BQL, Bloomberg reference/history, Yahoo Finance), and which surface it fed. The fixed daily load is
known before any backfill is planned.

### O2 -- An operator sees how much capacity is left today, and the reserve that is never spent

An operator reads, per vendor channel, the day's fixed load, what backfills have drawn, and what remains above a reserve
that production pulls are guaranteed. A backfill cannot spend the reserve.

### O3 -- A backfill request is queued with its cost, not run by hand

Anyone who needs history (a project, a new client, a new surface) adds a request stating the securities, fields and
dates; the queue prices it in cells, says when it will finish at today's spare capacity, and draws it in daily slices.
Nobody runs an ad hoc pull that can exhaust a channel.

### O4 -- A security is resolved once, to one identity, before anything is pulled for it

A security arriving from a custodian, a fund's holdings or a client file is matched to one identity (ticker, CUSIP,
FIGI, Bloomberg security) once, and every surface's request for it uses that identity. A security that cannot be
resolved is named with its reason, not pulled under a guess.

### O5 -- Each surface's history comes from a stated vendor by a stated rule

For each surface, an engineer can read which vendor serves which field (Bloomberg, Yahoo Finance, or the custodian's own
file), why, and the fallback. A field that a cheaper source already serves is not pulled from Bloomberg.

### O6 -- The same history is pulled once and shared

When two surfaces need the same security's prices over overlapping dates, the queue pulls the union once and both read
it. Re-pulling unchanged history every day stops.

### O7 -- Yahoo Finance is called inside its limits and fails loudly when refused

Yahoo Finance pulls are paced, batched and retried by one shared rule, and a throttled or empty answer is a named
failure, never an empty price series served as real.

### O8 -- A daily job pulls only what its surface reads

An owner can see, per job, which pulled fields no surface reads, and the queue's accounting shows the cells saved when
they stop being pulled.

### O9 -- A new client's onboarding cost is known before it starts

When a new firm or a large account is about to be ingested, an operator reads how many new securities it brings, the
cells to backfill them, and how many days of spare capacity that takes.

---

## PART II -- WHERE THE BOUNDARY SITS

### II.1 This project OWNS

- The demand ledger: every market-data pull, in cells, by vendor channel, job and surface (O1, O8).
- The reserve and the capacity accounting (O2).
- The queue: request, price, schedule, slice, draw, record (O3, O6, O9).
- The routing rule per surface, Bloomberg versus Yahoo Finance versus custodian file (O5).
- One pacing rule for Yahoo Finance (O7).

### II.2 It RELIES ON and does not own

- **Security identity and classification**: MDPF_SECCLASS (classification, the new-security classifier), the
  `etf-classifications` canonical table, `lib/research/identity/crosswalk.py` (AMGT), the Black Diamond ticker resolver
  (`data/black_diamond/scripts/classification/resolve_tickers.py`, seven methods) and the ticker override lists
  (`data/*/scripts/*/lib/ticker_overrides.py`). O4 is a requirement on these, not a second resolver.
- **The producers**: every pipeline that pulls today (Part IV) keeps its own code; the queue schedules and accounts for
  them.
- **The Bloomberg Terminal and its sign-in** (`integrations/bloomberg/`, `0.0.3_BG_BBGTerminal`).
- **The consuming surfaces**: ETFS_RIVALS, the ETF Positioning and IRPT performance views, ADVI and IRPT client surfaces,
  AMGT_CORPUS and AMGT_RESAPP, MDPF model portfolios.
- **ADVI_COTBKF** (Cottonwood): its operations are the DELL2 CRO's companion analysis.

### II.3 NOT this scope -- named so no decomposition re-opens it

- Buying more Bloomberg capacity or a BQL entitlement (Andrew's spend decision; `READ_HERE.md` section 4).
- Changing what any surface shows.
- Other vendors (YCharts, FactSet, custodian feeds), except as a named source in O5's routing table. Whether the queue
  later covers them is a question for Andrew.
- Rewriting Yang's model notebooks. The queue can report their cost and propose an incremental pull; the change is the
  owner's.

---

## PART III -- THE QUALITATIVE BAR

- An engineer planning a backfill can say, before running it, how much of today's capacity it takes and on which
  channel, and the answer matches what the run then draws.
- No production pull is blocked by a backfill again. The 2026-10-05 block (a backfill exhausting the Bloomberg BQL
  channel before the 07:00 ET production pull) is the case this prevents.
- Andrew can point at any surface and be told what it costs per day, what it would cost to backfill, and what of that is
  not read.
- A new client's securities appear on their surfaces with history without anyone remembering to run something.

No number in this part is a target. The capacity of each Bloomberg channel is not known (Part VII).

---

## PART IV -- THE SUBSTRATE: what exists, measured

### IV.1 The daily fixed load on site Z (measured 2026-10-08)

Full table: `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/BBG_DAILY_DEMAND_INVENTORY_20261008.md`.

| Job | Cells per day | Channel | Surface |
|---|---|---|---|
| Models PKL notebooks (07:00) | ~802,000 | history (+ ~560 reference) | portal performance, correlation, valuation, macro, positioning, factor pages |
| AMGT_CORPUS induction (09:00, 7 days) | ~132,000 | history ~124,000 + reference ~7,300 | Security Analysis research, scores, dossiers |
| Rival funds holdings | ~12,000 | BQL (749 rows x 16 columns) | Rival Funds page |
| Rival funds enrichment | ~6,400 to 12,300 | reference + history | Rival Funds |
| ETF leg, price leg, constituents leg | ~5,000 | reference + history | ETF Positioning; AMGT Lead Panel; constituents: no reader found |
| **Total** | **~957,000** | | |

Two jobs are about 98% of it, and both re-request unchanged history daily: the model notebooks re-pull series back to
1989 and 2020, and induction re-fetches yearly history since 2016 for 96 names (95 of 96 identical day over day).

### IV.1a The backfill demand already in the pipeline (measured and estimated 2026-10-08)

Full file: `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/BBG_BACKFILL_DEMAND_PIPELINE_20261008.md`. M = measured, E = estimated.

| Backfill | Surface | Cells | Channel | Kind |
|---|---|---|---|---|
| ACWI + IWM holdings history: ~4,233 rows per date (M) x 189 dates (M) x 16 columns | Rival Funds page | **~12.8 million (E)**, then ~67,700 a day once in the daily leg | **BQL**, the channel that blocked | one-time, then daily |
| Cottonwood client price history (MDPF_SECHIST): 1,319 securities, 2,317,534 security-days (M) | ADVI/IRPT Cottonwood surfaces | **2.32 to 4.64 million (E)** at 1 to 2 fields | history | per onboarding; no code yet |
| Rival funds year of closes: 742 securities x 251 days (M) | Rival Funds security dialog (FWD-24) | **184,600 owed (M)**, about 10 mornings at the 20,000 cap | history | one-time, then daily top-up |
| Positioning depth fill for new Opal ETF holdings | ETF Positioning performance views | 5,858 on the first run (M), about 530 per new holding | history | per new holding |
| Black Diamond, 49 Financial, Inflection onboarding | ADVI/IRPT | **not sized: no price census exists** | | per onboarding |
| IRPT daily fund sector and country spread | IRPT | not sized; about 36,000 cells per broad fund-day if built as a BQL look-through (E) | BQL | daily, if built |

Three findings from it:
- **The largest backfill by far is on the channel that already blocked.** ACWI + IWM is about 4.4 times the 2.92 million
  cells that exhausted BQL on 2026-10-05, so it cannot run as one job under any reserve; at the observed floor it is
  more than four days of the whole channel.
- **Classifying a new client's securities costs no Bloomberg cells.** An AI classifier fills them, reusing Rival Funds
  GICS. The Bloomberg cost of onboarding is history, not classification.
- **Overlap is real (M):** 1,009 security pulls cover 852 distinct securities; Rival Funds shares 81 with Positioning and
  74 with AMGT, held in three separate stores: about 39,000 duplicate cells one-time (E). Two August Positioning backfills
  (330,966 cells) have no authorizing record found.

The two research passes measured the AMGT daily draw differently: about 132,000 cells a day (induction, including its
yearly history) in IV.1 and 74,255 (the model-block refresh alone) plus 2,089 (the 30-day price window) here. Both agree
that 95 of 96 history objects repeat day over day. The PRD should measure it once on one definition.

### IV.2 The one measured ceiling (2026-10-05)

About 182,807 BQL holdings rows, **2.92 million cells**, between 05:3xZ and 06:55Z exhausted the Bloomberg BQL/Excel
daily capacity; every BQL query then returned "Daily Capacity, request is blocked". The reference/history channel kept
working. One run's draw is unknown, so 2.92 million is a floor.
Record: `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/BBG_CELL_TRACKING_RECONSTRUCTION_20261005_BLOCK_20261008.md`.

### IV.3 The budget machinery that exists

`data/etfs/scripts/rivalfunds/bbg_budget.py` and `bbg_budget.json`: a daily ceiling of 150,000 and a production reserve
of 30,000, in "rows", with a per-day JSON-lines ledger. Findings: it covers the rival-funds producers only; its unit
mixes rows returned, points requested and calls (the pacer note,
`org/tier0_utility/0.0.3_BG_BBGTerminal/deliverables/MDPF_SECHIST_PACER_20261007.md`); the two big daily jobs are not on
it; the AMGT_CORPUS fire records nothing. **The ledger and its reserve are the right shape and the wrong scope.** The
CTO's standing ruling (msg 31939) keeps "returned records" as its unit until Andrew chooses cells, and then changes every
producer at once.

### IV.4 Yahoo Finance is already a production source

| Where | What |
|---|---|
| `infra/aws/lambda/bd-pipeline/bd-price-update/lambda_function_v2.py` | daily price update for Black Diamond assets: `yf.download` in batches of 50, 2 s between batches (its own note: "to avoid rate limiting") |
| `infra/aws/lambda/historical-prices-scheduler/` | starts an EC2 daily (09:00 ET) to fetch prices with yfinance |
| `data/*/scripts/gold/build_canonical_prices_v2.py` (BD, COT; INF has the same lib) | Yahoo Finance is tier 2 of the canonical price hierarchy, after transaction-observed prices and before interpolation |
| `data/*/scripts/silver/backfill_yahoo_prices*.py`, `fetch_historical_prices_yfinance.py` | history backfills |
| `infra/aws/scripts/ingest_market_data_yfinance.py` | index prices to `s3://opal-data-market-yf/` |
| `data/yang_macros_re/adapters/yahoo_finance_adapter.py`, the volatility fetcher Lambda | macro and volatility |

Findings: each caller paces itself (or does not); there is no shared limit, no shared failure rule, and no record of
what Yahoo Finance was asked for in total.

### IV.5 Security resolution that exists

Several resolvers, each scoped to one pipeline: the Black Diamond resolver (seven methods in priority order, confidence
per method), the ticker override and correction dicts copied per firm (BD, COT, INF), the `etf-classifications`
DynamoDB canonical table with a scheduled classifier, MDPF_SECCLASS's new-security classifier Lambda, and AMGT's
crosswalk. **O4's requirement is that a request reaching the queue already carries one resolved identity.**

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

- The capacity of each Bloomberg channel (BQL/Excel; reference/history; intraday) is measured or stated by Bloomberg.
  Without it, O2's reserve is a guess.
- Every box that calls Bloomberg or Yahoo Finance reports to one ledger (site Z holds the Terminal; DELL1 and DELL2 run
  ingestion; the laptop plans).
- Each producer can be scheduled by the queue, or at least reports its draw to it.
- Andrew decides whether cells become the ledger's unit (CTO ruling 31939), and whether vendors beyond Bloomberg and
  Yahoo Finance join the queue.
- The resolvers in IV.5 agree on one identity per security, or the queue names the disagreement.

---

## PART VI -- STATUS, NOT OUTCOME-BEARING

Measured 2026-10-08 on site Z.

- The demand known in the backfill pipeline is in the companion file
  `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/BBG_BACKFILL_DEMAND_PIPELINE_20261008.md` (rival funds' year of closes,
  holdings history for short funds, positioning performance history, per-onboarding security history for ADVI/IRPT).
- The 07:00 ET Bloomberg vehicle exited 50 on 2026-10-08 (Terminal connection down); data for 2026-10-07 came from manual
  runs at 12:07Z and 12:09Z.
- ETFS_RIVALS PRD v0.19 (FWD-24) already plans a daily "history owed" step for its own securities, paced inside the
  budget: the first producer-side instance of this queue's idea.

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- **No Bloomberg channel's capacity is known.** 2.92 million BQL cells is a floor from one incident, and nothing is known
  for reference and history.
- The daily inventory covers site Z only. The laptop, DELL1 and DELL2 were not measured.
- Yahoo Finance's actual limits were not measured; the batches of 50 with 2 s gaps are one caller's own choice.
- "Fields nobody reads" are candidates from a code read, not proven by usage.
- The cell counts were measured by a research subagent of this seat and spot-checked (schedules, totals arithmetic), not
  re-derived line by line.
- The Cottonwood operations (ADVI_COTBKF) are deliberately left to the DELL2 CRO's companion analysis.

---

## REFS TO CARRY

```
  BRIEF PATH        docs/briefs/bbg-backfill-demand-queue-brief-20261008.md
  PROJECT           NONE-YET (DELL1's CTO registers it)
  EXISTING PRD      NONE
  COMPANION         the DELL2 CRO's ADVI_COTBKF / Cottonwood analysis (via DELL1's MSTR)
  SIBLING PROJECTS  ETFS_RIVALS (FWD-24), MDPF_SECCLASS, MDPF_SECHIST, ADVI_COTBKF, IRPT_* , AMGT_CORPUS, NFRA_CTLPLN (boxes)
  PRIOR ART         bbg_budget.py/.json and its ledger; the pacer note; the BD ticker resolver and override dicts;
                    the yfinance producers in IV.4; etf-classifications table; ETFS_RIVALS FWD-24's history-owed step
  EVIDENCE          BBG_DAILY_DEMAND_INVENTORY_20261008.md; BBG_BACKFILL_DEMAND_PIPELINE_20261008.md;
                    BBG_CELL_TRACKING_RECONSTRUCTION_20261005_BLOCK_20261008.md (all in org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/)
  MEASURED AT       2026-10-08 ~18:xx-20:3xZ, site Z
```
