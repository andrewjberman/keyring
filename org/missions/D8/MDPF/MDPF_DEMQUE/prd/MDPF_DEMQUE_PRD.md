# MDPF_DEMQUE -- the backfill demand queue: every history backfill priced, ranked and drawn within the Bloomberg and Yahoo budgets, never crowding out a production pull

```json
{
 "project": "MDPF_DEMQUE",
 "directive": "D8",
 "fabric": "dell1",
 "prd_version": "v0.3",
 "step": 4,
 "brief_ref": "docs/briefs/bbg-backfill-demand-queue-brief-20261008.md@91f5c90ec2",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7", "FWD-8", "FWD-9"],
 "status": "DRAFT"
}
```

**Author:** `1.0.0_SA_CTO~DELL1` (L2-L4), 2026-10-08.
**Briefs:** organisation-wide L1 `docs/briefs/bbg-backfill-demand-queue-brief-20261008.md` @91f5c90ec2 (`4.0.0_SA_CRO~Z`); Cottonwood
research `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261008_COTTONWOOD_YAHOO_PRICE_BACKFILL_STRUCTURE.md` @e112184d3b
(`4.0.0_SA_CRO~DELL2`).
**Andrew's words:**
- ~19:1xZ (dell2, record @489e1cd24c, `org/tier1_exec/2.0.0_SA_COO~C2/deliverables/ANDREW_DIRECT_20261008_191xZ_DELL_YAHOO_EGRESS_AND_PRICE_BACKFILL_STRUCTURE_TO_CRO.md`):
  "DELL boxes can call yahoo all they want ... The greater issue is resolutin of the ticker with yahoo, specifically the methodology of
  how that can be locked in ... a process of securities that cannot be mapped to yahoo successfully, also how we handle corporate
  actions needs to be threaded into that, particualrly retroactively ... you have to be gentle with it ... we keep a "ranking" on the
  importance of being able to pull that backfill."
- ~19:3xZ (dell1 MSTR, record @cf7005c305): "All of this needs to get wrapped up into a registered project which will be run on this
  device."
- ~22:4xZ (dell1 CTO, record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_224xZ_BACKFILL_QUEUE_ENDPOINT_CONFIRMED_PRIORITY_BBG_YAHOO_ONLY.md`):
  "1.) Yes. 2.) Production daily pulls includes ETF Positioning. Then Current clients and new client onboarding. Then rival funds
  history (which I think we can handle on BBG even if it takes a week or two of daily little jobs to get the majority of it out of the
  way). Then research pages. Then finally former clients last. 3.) Only BBG and Yahoo for now."
**Placement:** dell1 (Andrew ~19:3xZ). Bloomberg draws execute at site Z, where the Terminal is (C-SITES). COO lane: to be seated.
**Sign-off:** `3.0.0_SA_CVO` (dell1) signs the ratified-text half; the brief half is accepted because the CROs wrote the briefs.

## ENDPOINT (step 2, /endpoint --forward)

Ratified by Andrew ~22:4xZ ("1.) Yes."). Source: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_BACKFILL_DEMAND_QUEUE_20261008.md`.

```
FWD-1  A new Cottonwood client security gets its price history onto the client's page without anyone running a pull
       DONE WHEN  EXERCISED -- one real security, traced from arrival to the page
       ACCEPT     a named security a living Cottonwood client holds, with no history before, has its daily prices value that client's
                  holdings on the client's pages for the dates the backfill fills; those prices agree with the prices the client
                  actually traded at; and no person ran a pull by hand
       AMENDED    v0.3 (L10 round 1, CTO adjudication record CTO_ADJUDICATION_MDPF_DEMQUE_20261009T0108Z.md): no page shows
                  per-security daily prices, so the consumer is the client's backfilled holding values and performance, built by
                  ADVI_COTBKF (dell2) from these prices. Id unchanged; the outcome is narrowed to its real consumer, not retired.
       SOURCE     site Z brief I.0 (the candidate thread); dell2 research s.1 (lock against trade prices), s.6 (living client first)

FWD-2  Anyone can see, in cells, what every daily job pulls, from which vendor, for which page
       DONE WHEN  EXERCISED -- a real day read back
       ACCEPT     for a chosen day, a person reads every recurring market-data pull on every box, how many cells (one row times one
                  field) it drew from each vendor, which page it fed, and which of the pulled fields no page uses; the day's figures
                  can be checked against what the jobs actually received
       SOURCE     site Z brief O1, O8; Andrew "counting off the basis of cells", "where that quota is going"

FWD-3  A backfill can never stop a production pull
       DONE WHEN  EXERCISED -- shown on purpose
       ACCEPT     a person can read, per vendor channel, today's fixed daily load, what backfills have used, and what is left above a
                  reserve kept for production; a backfill big enough to reach the reserve stops at it, and the next morning's
                  production pulls all run
       SOURCE     site Z brief O2, Part III (the 2026-10-05 block); Andrew "developing our reserves"

FWD-4  A request for history is priced and scheduled before it runs, including a new client's onboarding
       DONE WHEN  EXERCISED -- one real request
       ACCEPT     someone asks for history on a set of securities, fields and dates, and is told before anything runs what it costs
                  and the day it will finish; the same is shown for a new firm or large account before its onboarding starts; and
                  what the run then uses is close to what was quoted
       SOURCE     site Z brief O3, O9

FWD-5  Each security is identified once, and what cannot be identified is listed with its reason and the dates it covers
       DONE WHEN  EXERCISED -- one real run read
       ACCEPT     a security arriving from a custodian, a fund or a client file is matched to one identity before anything is pulled
                  for it, and every page asking for it uses that one identity; a security that cannot be matched, or is matched only
                  for part of the time it was held, appears on a list with its reason and the dates still open
       SOURCE     site Z brief O4; dell2 research s.2, s.5; Andrew "resolution of the ticker ... how that can be locked in", "a process
                  of securities that cannot be mapped", "unresolved indexing on time period(s)"

FWD-6  Each page's history comes from a stated vendor by a stated rule
       DONE WHEN  APPLIED -- the rule is written and in force
       ACCEPT     for each page, a person can read which vendor supplies which figure (Bloomberg, Yahoo Finance, or the custodian's
                  own file), why, and what is used when that vendor fails; a figure a cheaper source already supplies is not taken
                  from Bloomberg
       SOURCE     site Z brief O5; Andrew "whether we go to BBG or YFinance and associated methodology per surface"

FWD-7  Yahoo Finance is used gently and reliably, and its prices stay right through splits and mergers
       DONE WHEN  EXERCISED -- a multi-day run read
       ACCEPT     every Yahoo request follows one shared pace, stops for the day when Yahoo pushes back and resumes where it stopped;
                  a refused or empty answer is reported as a failure, never shown as real prices; and a split or merger, including
                  one Yahoo records later, leaves a held position valued at the price it actually traded at
       SOURCE     site Z brief O7; dell2 research s.3, s.4; Andrew "be gentle with it", "corporate actions ... particularly
                  retroactively"

FWD-8  The same history is pulled once and shared
       DONE WHEN  EXERCISED -- shown on purpose
       ACCEPT     when two pages need the same security's prices over the same dates, it is pulled once and both pages show it, and
                  unchanged history is not pulled again the next day
       SOURCE     site Z brief O6, IV.1a (overlap measured)

FWD-9  What is pulled first follows how much it matters
       DONE WHEN  EXERCISED -- one real day's order read
       ACCEPT     when there is not enough room for everything, the securities that matter most to clients we still serve are pulled
                  first; an unmatchable fund held only by a client who is gone, by name and by account, is not pursued; and a person
                  can see the order and why each item sits where it does
       SOURCE     Andrew (Yahoo record) "we keep a 'ranking' on the importance ... that is not a priority to get"; dell2 research s.6
```

**Settled by Andrew (~22:4xZ).** FWD-9's order: (1) production daily pulls, which INCLUDE ETF Positioning; (2) current clients and
new-client onboarding; (3) Rival Funds history, on Bloomberg, as small daily jobs over a week or two until the majority is done;
(4) research pages; (5) former clients last. The queue meters **Bloomberg and Yahoo only**, for now; other vendors stay named as
sources in FWD-6's per-page rule.

## STARTING STATE (measured 2026-10-08, file:line)

- **One budget exists, for one family only.** `data/etfs/scripts/rivalfunds/bbg_budget.py:5-14,95-99` gates a backfill at
  `ceiling - reserve - spent(today)`; `bbg_budget.json` holds `daily_ceiling_rows 150000`, `production_reserve_rows 30000` and per-fund row
  estimates (ACWI 2198, IWM 1979). The unit is rows, and the rival-funds producers are the only callers (brief IV.3).
- **One measured ceiling.** 2026-10-05: about 2.92M BQL cells exhausted the BQL/Excel daily capacity; the reference/history channel kept
  working (brief IV.2; `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/BBG_CELL_TRACKING_RECONSTRUCTION_20261005_BLOCK_20261008.md`). A floor,
  not a ceiling.
- **The backfill demand in the pipeline** (brief IV.1a): ACWI + IWM holdings history about 12.8M BQL cells (E); Cottonwood price history
  1,319 securities, 2.32-4.64M cells (E); rival year of closes 184,600 (M); Positioning depth fill 5,858 first run (M).
- **The Bloomberg production pull** is `integrations/bloomberg/pipeline/etf_daily_pull.py` (740 lines), run at site Z at 07:00 ET
  (MDPF_SECHIST).
- **Yahoo is already a production source, paced per caller:** `infra/aws/lambda/bd-pipeline/bd-price-update/lambda_function_v2.py:6-9,46`
  (batches of 50, `BATCH_DELAY = 2`); `infra/aws/scripts/ingest_market_data_yfinance.py`; `data/yang_macros_re/adapters/yahoo_finance_adapter.py`.
  No shared limit, failure rule or total exists (brief IV.4).
- **Resolvers exist per pipeline:** `data/black_diamond/scripts/classification/resolve_tickers.py` (838 lines, seven methods),
  `lib/research/identity/crosswalk.py` (1,606 lines), the `etf-classifications` table (10,834 rows, measured 20:3xZ by
  this seat's outcome check), and the per-firm ticker override lists (brief IV.5).

## CONTRACTS

**C-CELL -- the unit is the cell.** One row times one field, on every vendor ledger (Andrew ~18:3xZ, "counting off the basis of cells").
It supersedes the interim "returned records" unit (msg 31939). Every producer on the ledger changes unit together at build time, never
one alone. `bbg_budget.json`'s row figures convert at the switch; the conversion is printed, not assumed.

**C-METER -- Bloomberg and Yahoo only.** The ledger meters those two vendors (Andrew ~22:4xZ). Bloomberg is metered per channel (BQL and
reference/history separately, because only BQL blocked on 2026-10-05). Other vendors appear only as named sources in C-ROUTE.

**C-RESERVE -- production is never crowded out.** (v0.2, CVO finding F1.) Per Bloomberg channel there are two figures. The CEILING
is the day's capacity, seeded from the measured floor on capacity (2.92M BQL cells on 2026-10-05) and re-measured from the ledger.
The RESERVE is what production needs: the measured BQL draw of the tier-1 production pulls plus a stated margin, re-measured from the
ledger. The backfill allowance is CEILING minus RESERVE, minus what has already been drawn that day. A backfill draw that would cross
into the reserve stops at it and resumes the next day. If the allowance measures at or near zero, that is a finding reported with its
numbers, never a silent stall: FWD-4's finish dates and FWD-9's tier 3 depend on it. The
production pulls (C-PRIORITY tier 1) never draw against the backfill allowance. Buying capacity or entitlement is Andrew's spend
decision and is out of scope.

**C-PRIORITY -- the order is Andrew's (~22:4xZ).** (1) production daily pulls, including ETF Positioning; (2) current clients and
new-client onboarding; (3) Rival Funds history on Bloomberg, sliced into small daily jobs, about a week or two for the majority;
(4) research pages; (5) former clients last. Within a tier, the ranking follows dell2 research s.6. A fund that cannot be matched and is
held only by a client who is gone, by name and by account, is not pursued (Andrew's Yahoo record). Each item carries its tier and its
reason on a row a person can read.

**C-QUOTE -- priced before it runs.** A request names securities, fields and dates. Before any draw it gets a cell cost per channel and
a finish date computed from the allowance above the reserve. The run records its actual draw beside the quote.

**C-IDENTITY -- one identity, resolved before the queue.** The existing resolvers (STARTING STATE) feed the queue; none is replaced and
no second resolver is built. A client security's mapping is LOCKED, per date range, only when its prices agree with the client's own
trade prices (dell2 research s.1). A lock with no trade prices to check carries the claim `held`, not `measured`. A security that cannot
be matched, or is matched for only part of its holding period, goes on the unresolved list with its reason and its open date ranges.

**C-PRICES -- stored as traded.** Prices are kept as traded, with splits and dividends held apart, so a later correction (including one
Yahoo records after the fact) is re-derived and never re-pulled (dell2 research s.3).

**C-YAHOO -- one gentle pace.** Every Yahoo caller that the queue drives goes through one shared pacing rule. A refusal, rate-limit or
empty answer is recorded as a FAILURE and is never stored as a price. On push-back the draw stops for the day and resumes where it
stopped. Corporate actions are threaded in, including retroactively (Andrew ~19:1xZ). Yahoo egress from the Dell boxes runs under
Andrew's record @489e1cd24c.

**C-ROUTE -- one vendor rule per page.** For each consuming page: which vendor supplies which figure, why, and the fallback when it
fails. A figure a cheaper source already supplies is not taken from Bloomberg.

**C-ONCE -- pull once, share.** The same security, field and dates are pulled once and shared across pages; unchanged history is not
re-pulled daily. The two daily jobs that re-request unchanged history (brief IV.1: model notebooks, induction) are reported with their
cost. Changing them is their owners' change; the queue proposes an incremental pull.

**C-PRODUCERS -- producers keep their code.** The queue schedules and accounts; it does not absorb or rewrite a producer. MDPF_SECHIST
keeps the Bloomberg pull and supplies its price-need file as an input. ADVI_COTBKF's ranked need list is an input contract: a file at a
fixed path, key namespace stated. The Yahoo price backfill agreed for MDPF_SECHIST (dell2 msg 1456) is part of this project.

**C-SITES -- which acts run where.** Bloomberg draws run at site Z (the Terminal and its sign-in, `integrations/bloomberg/`). Every box
that calls Bloomberg or Yahoo writes its draws to the one ledger. Yahoo draws may run on either Dell. Planning, quoting and ranking run on
dell1. A Bloomberg act is a site Z act: the decomposition names its executor there, and site Z's own gates bind it.

**C-PILOT -- 50 securities first.** A 50-security living-client pilot (dell2 research s.7 item 3) measures the lock error rate, the
tolerance band and Yahoo's response before the first full session.

**C-HOMES -- addresses come from the builder (CLAUDE.md rule 30).** Builder output, `lib/opal_naming.py address()` (run 2026-10-08):
- `address("bloomberg","global","bronze","demand_ledger","dt=<date>")` -> `s3://opal-data-assets/bloomberg/global/bronze/demand_ledger/dt=<date>`
- `address("bloomberg","global","silver","demand_ledger","dt=<date>")` -> `s3://opal-data-assets/bloomberg/global/silver/demand_ledger/dt=<date>`
- `address("yahoo",...)` REFUSED: "source 'yahoo' is not a systems.json key". **Registry gap:** a `yahoo` row in
  `infra/logic/registry/systems.json` is needed before the Yahoo ledger home is named.
The decomposition picks the ledger home from builder output only. No hand-typed address lands.

## BOUNDARY

Owns: the demand ledger, the reserve, the queue (request, price, schedule, slice, draw, record), the per-page vendor rule, the Yahoo
pacing rule, the unresolved list (brief II.1). Relies on and does not own: MDPF_SECCLASS and the resolvers (identity); every producer;
the Bloomberg Terminal and its sign-in at site Z; the consuming pages; ADVI_COTBKF (brief II.2). Not this scope: buying capacity, changing
what any page shows, metering other vendors, rewriting the model notebooks (brief II.3).

## OPEN ITEMS (for L5, not blocking admission)

1. The AMGT daily draw has two measurements (about 132,000 cells vs 74,255 + 2,089). Measure it once, on C-CELL's definition (brief IV.1a).
2. The Black Diamond, 49 Financial and Inflection onboarding draws are unsized: no price census exists (brief IV.1a).
3. Two August Positioning backfills (330,966 cells) have no authorising record (brief IV.1a). Name them on the ledger; do not re-run them.
4. The `yahoo` systems.json registry row (C-HOMES).
5. ADVI_COTBKF's need-list path and key namespace, agreed with dell2 before the pilot.

## SURFACE MANIFEST (step 4 -> step 5)

| id | outcome_ref | surface | claim | verb | bound |
|---|---|---|---|---|---|
| S01 | FWD-2, FWD-3 | the one demand ledger, in cells, per vendor channel, job and page | measured (`bbg_budget.py:5-14`: rows, rival-funds only) | build | C-CELL; C-METER; C-HOMES |
| S02 | FWD-3 | the per-channel reserve and the backfill allowance | measured (`bbg_budget.json`: 150,000 / 30,000 rows) | amend | C-RESERVE; ceiling from the 2.92M floor, reserve = production draw + margin |
| S03 | FWD-4, FWD-9 | the queue: request, quote, rank, slice, schedule, record | held | build | C-QUOTE; C-PRIORITY |
| S04 | FWD-5 | the unresolved list, with reason and open date ranges, fed by the existing resolvers | measured (`resolve_tickers.py`; `crosswalk.py`) | build | C-IDENTITY; no second resolver |
| S05 | FWD-1, FWD-7 | the shared Yahoo pacer and failure rule | measured (`lambda_function_v2.py:46`, per-caller pacing) | build | C-YAHOO; C-PRICES |
| S06 | FWD-6 | the per-page vendor rule table | held | build | C-ROUTE |
| S07 | FWD-8 | the pull-once share across pages | measured (brief IV.1a: 1,009 pulls cover 852 securities) | wire | C-ONCE |
| S08 | FWD-1 | the Cottonwood thread: one new living-client security, from arrival to the client's page | held | read | C-PILOT first; trade-price agreement |
| S09 | FWD-3, FWD-9 | the Bloomberg draw at site Z under the queue | measured (`etf_daily_pull.py`, 07:00 ET at site Z) | wire | C-SITES; C-PRODUCERS |

## BRIEF COVERAGE

| Brief heading | Carried | Consuming sections |
|---|---|---|
| site Z I.0 thread, O1-O9 | the Cottonwood thread; nine outcomes | ENDPOINT |
| site Z II.1-II.3 boundary | owns, relies on, not this scope | BOUNDARY |
| site Z IV.1-IV.5 substrate | daily demand, backfill pipeline, ceiling, budget machinery, Yahoo callers, resolvers | STARTING STATE; S01-S09 |
| site Z Part VII, capacity unknown | reserve from the measured floor; spend is Andrew's | C-RESERVE |
| dell2 research s.1-s.7 | lock against trade prices; unresolved by period; as-traded prices; Yahoo pacing; ranking; pilot | C-IDENTITY, C-PRICES, C-YAHOO, C-PRIORITY, C-PILOT |
| Andrew ~22:4xZ | priority order; meter BBG and Yahoo only | C-PRIORITY, C-METER |

## Provenance

GROUNDED ON: both briefs (@91f5c90ec2, @e112184d3b); the ratified endpoint; Andrew's records (@489e1cd24c, @cf7005c305 and the ~22:4xZ
record); file reads at the paths cited in STARTING STATE (2026-10-08); `lib/opal_naming.py address()` run 2026-10-08. NOT READ: the brief's
evidence files (their figures are the brief's, marked M or E as it marks them); any open task order; site Z's Bloomberg ledger files.

## PRIOR ART TO CARRY

`data/etfs/scripts/rivalfunds/bbg_budget.py` + `bbg_budget.json` (the right shape, the wrong scope); the pacer note
(the MDPF_SECHIST pacer note cited in v0.1 exists in no tree: CVO finding F2, measured 0 of 74,316 files; removed); `lambda_function_v2.py`'s batch pacing;
`resolve_tickers.py`'s seven methods; `crosswalk.py`; `integrations/bloomberg/READ_HERE.md` (two-phase budgeted sign-in).
