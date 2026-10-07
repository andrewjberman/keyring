# IRPT_DASHBD -- L5 decomposition -- workstream B (backend) -- round 1 -- v0.1

**v0.1** (2026-09-30 ~15:5xZ, `2.0.0_SA_COO~P`, on PRD v0.2 @84cff9014b, ADMITTED with both L4-R halves signed: ratified-text
`3.0.0_SA_CVO` @9914eab4f4, brief half by CRO authorship; CTO 103251/103257/103260/103263/103264). Round 1 builds THE THREAD (PRD
section 2, FWD-1): one 49 Financial account end to end, B's hops 1-4 and the served file's read route; F's hop 5 is `2.0.0_SA_COO~D`'s
under C-LEASE and is not decomposed here. Workstream F has its own decomposition; this document declares B's cells only.

```json
{
  "project": "IRPT_DASHBD",
  "directive": "D9",
  "fabric": "laptop",
  "workstream": "B_backend",
  "issuer": "2.0.0_SA_COO~P",
  "round": 1,
  "decomp_version": "0.1",
  "prd_ref": "org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md@84cff9014b",
  "prd_version": "v0.2",
  "brief_ref": "docs/briefs/reporting-dashboard-backend-brief-20260930.md@0ee065b116",
  "endpoint_ref": "org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_REPORTING_DASHBOARD_20260930.md@9a3afb2f9c",
  "endpoint_outcomes": ["FWD-1","FWD-2","FWD-3","FWD-4","FWD-5","FWD-6","FWD-7","FWD-8","FWD-9","FWD-10"],
  "round1_outcomes_in_scope": ["FWD-1", "FWD-8", "FWD-9"],
  "cells_round1": 4,
  "cell_id_shape": "DB-b-<n> (workstream B); workstream F's decomposition uses its own prefix",
  "executors": "0.4.0_DS_ClientPlatform~S (the DS-lane cells, rule 13) and 0.9.0_WK_IRPT_DASHBD~<slot> (the Lambda/Terraform cells)",
  "thread_account": "0027265115 (49 Financial, Schwab master 08335338; Black Diamond relationship 22596361 in blackdiamond/49f/_ops/taxsma_roster.json), with the roster's other four active accounts as the round-1 sample",
  "cut_head": "stated in the issuance commit"
}
```

## 0. What the thread is, and what is owned elsewhere

Hop 1 (silver -> gold `account_return_daily` under its contract, the guard applied) and hop 2 (gold -> platinum `series.json.gz` +
`manifest.json`) are B's by the PRD; hop 3 (the served file -> the signed-in page) crosses the seam: the FILE is B's and the read
route that hands it to the page is B's (the page is F's, hop 4-5). Owned elsewhere and consumed, never built here: the holdings
price return (IRPT_BCKEND's `holdings_performance_daily`, C-GUARD); the canonical classes (MDPF_SECCLASS; no class table in round 1);
the news tables; the Black Diamond pulls already landed in bronze (the tie-out oracle, C-TIEOUT); the registry (LGIC; a policy row is
added, never a typed key).

## 1. ROUND 1, WORKSTREAM B (2026-09-30 ~15:5xZ, issuer 2.0.0_SA_COO~P, on PRD v0.2 section 2 and ADDENDUM v0.2 rulings 11-14)

**Builder output at the cut (rule 30; `lib/opal_naming.py` at HEAD, 15:4xZ, no refusal):**
gold `address("irpt","49financial","gold","account_return_daily","date=2026-09-29")` ->
`s3://opal-data-49financial/irpt/49financial/gold/account_return_daily/date=2026-09-29`;
`address("irpt","49financial","gold","dim_return_method","method_version=1")` ->
`s3://opal-data-49financial/irpt/49financial/gold/dim_return_method/method_version=1`;
platinum `address("irpt","49financial","platinum","reporting","account=0027265115","series.json.gz")` ->
`s3://opal-data-49financial/irpt/49financial/platinum/reporting/account=0027265115/series.json.gz` (and `manifest.json`);
names `name("irpt","49financial","reporting-publish","lambda")` -> `irpt-49f-reporting-publish-lambda`,
`("irpt","49financial","reporting-publish","daily")` -> `irpt-49f-reporting-publish-daily`,
`("irpt","49financial","reporting-publish","role")` -> `irpt-49f-reporting-publish-role`,
`("irpt","49financial","reporting-read","lambda")` -> `irpt-49f-reporting-read-lambda`.

**Where IRPT_BCKEND's producer runs today (the PRD's round-1 reading, section 4 row 1):** as a scheduled Lambda that packages the DS
producer UNEDITED (`infra/aws/terraform/investor-reporting/holdings-performance/lambda.tf`; `lambda-source-map.json` entry
`irpt-holdings-performance-lambda` with `staged_from` pins for `data/assets/scripts/gold/irpt_holdings_performance/*`,
`lib/opal_naming.py`, `lib/trading_calendar.py` and the registry files). So the adapter is a DS-lane gold script beside it, run ad hoc for
the round-1 sample (a QA run; the scheduled fire is a round-2 cell under its own ledger, exactly as IB-er-203 followed IB-er-202), and
the publisher is a Lambda with its own root and schedule (C-MORATORIUM: its own cron, never success-of-upstream).

**The reading behind the read route (hop 3):** the page today reads served IRPT JSON through a per-function Lambda that registers
`ROUTES = {ROUTE_KEY: OPERATION}` and resolves the viewer's selection through the `_scope` enforcer before any S3 read
(`infra/aws/lambda/investor-reporting/holdings/entry.py:38-55, :136-150`, function `irpt-holdings`). The series read mirrors that shape
under its own function; adding a route inside another function's boundary is the W88-S1 trap (IRPT_BCKEND) and is not taken.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-1` | FWD-1 hop 1, FWD-8, FWD-9: the 49 Financial adapter `data/assets/scripts/gold/irpt_reporting/account_return_daily.py` + its `sources.json` declaration (Schwab `dim_position`, `dim_balance`, `fact_trn` with the ratified 187-code table read as DATA from `org/tier1_exec/4.0.0_SA_CRO/deliverables/SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811.json`, the flow classes of `c00_flow_ledger.py` read as data, no import of `c02_twr_engine.py`); C-METHOD daily TWR with end-of-day external flows, income on receipt, `V` = `dim_balance.net_mv_plus_cash` (C-VALUE verified); C-GUARD against `holdings_price_return` read from IRPT_BCKEND's gold; the tolerance, large-flow share and plausibility band MEASURED from the five sample accounts' own distribution and written to `dim_return_method` (method_version 1, Account365, `income_basis cash_when_received`, `fee_basis GROSS_ONLY`, `flow_convention END` pending DB-b-3); the two contract files `org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json` (rule-24 record per ADDENDUM ruling 12: `history_scope`, `day_quality`, per-column `<col>_reason`, `return_basis` closed) and `org/standards/IRPT_DASHBD_DIM_RETURN_METHOD_CONTRACT.json`; the `reporting_policies.json` rows for the two tables (S17); the gold emitted for the five sample accounts over their full history (2024-07-09 .. the frontier) at the builder's addresses; ledger `irpt-dashbd-account-return-daily-49f-r1-20260930` | WORLD (new gold objects; nothing served reads them) | none | A |
| `DB-b-2` | FWD-1 hop 2, FWD-9: the platinum publisher `irpt-49f-reporting-publish-lambda` on `irpt-49f-reporting-publish-daily` (Terraform root `infra/aws/terraform/investor-reporting/reporting-publish/`, source `infra/aws/lambda/investor-reporting/reporting-publish/`, packaged through `lambda-source-map.json` + `build-and-upload.sh` like `irpt-holdings-performance-lambda`), reading gold `account_return_daily` + `dim_return_method` and writing per account `series.json.gz` (columnar arrays: date, value, total_return_daily, return_basis, day_quality, external_flow, income, holdings_price_return, method_version, as_of, first_data_date, drawdown_episodes by the `irpt-narrative` rule; class arrays absent and declared optional until `account_class_daily` exists) and `manifest.json` (method version, as-of, coverage summary, byte sizes), under `org/standards/IRPT_DASHBD_SERIES_CONTRACT.json` (C-SEAM, B the only writer); ONE local `--upload` run for the five sample accounts writes the files at the builder's addresses (WORLD: new platinum keys, nothing served reads them); the Terraform plan printed (the apply is the issuer's under its own ledger); size and build time printed; ledger `irpt-dashbd-reporting-publish-49f-r1-20260930` | WORLD (new platinum objects; a new Lambda + schedule planned) | DB-b-1 (reads its gold) | B |
| `DB-b-3` | FWD-8 (ADDENDUM ruling 11, C-TIEOUT, C-FLOWTIME): the tie-out harness over the FIVE sample accounts against Black Diamond's own `performancePeriod` returns ALREADY LANDED in bronze (`s3://opal-data-assets/blackdiamond/49f/bronze/reporting_performance/<pull date>/reporting_performance_<relationship>_<period end>.json`, pull dates 2026-07-17, 08-30, 08-31, 09-01; roster `blackdiamond/49f/_ops/taxsma_roster.json` maps `bd_internal_id` -> `schwab_account`): NO vendor call. For every (account, period) the oracle carries: Opal's daily-TWR link over the same window under the three flow-timing conventions (START, END, MIDPOINT), the absolute difference, and per disagreeing day its stated reason (flow timing, missing price, income date, `day_quality`); summary median / p90 / max; the PROPOSED `tieout_tolerance` and the winning convention, written into `IRPT_DASHBD_DIM_RETURN_METHOD_CONTRACT.json` and the `dim_return_method` row (C-FLOWTIME); record `deliverables/0.4.0_DS_ClientPlatform~S/tieout/TIEOUT_49F_BLACKDIAMOND_R1.json` + one page md for the CTO's ruling | LOCAL (a measurement; one gold row's field moves under DB-b-1's ledger, re-opened as leg M1) | DB-b-1 | A |
| `DB-b-4` | FWD-1 hop 3: the read route `irpt-49f-reporting-read-lambda` (source `infra/aws/lambda/investor-reporting/reporting/entry.py`, root `infra/aws/terraform/investor-reporting/reporting-read/`) that hands the signed-in page the thread account's `series.json.gz` and `manifest.json` after the `_scope` enforcer covers the account (mirrors `holdings/entry.py`'s shape; its own function, never a route added inside another function's boundary); the Terraform plan printed (the apply is the issuer's); a local invoke against the REAL S3 objects proves the bytes and the refusal branch | WORLD (a new served function planned; no apply in the cell) | DB-b-2 (reads its objects) | B |

**Chain read.** M = 2: chain A = `DB-b-1` -> `DB-b-3` (the DS lane's queue: the adapter, then the measurement over its gold); chain
B = `DB-b-2` -> `DB-b-4` (a worker's queue: the publisher, then the read route over its objects). Chain B's first criterion reads chain
A's gold, so its worker is spawned when `DB-b-1` reports the gold landed (the spawn is the GO; nothing waits on a message). N = 2, K = 8.
Write sets are disjoint: `DB-b-1`/`DB-b-3` write under `data/assets/scripts/gold/irpt_reporting/`, `org/standards/IRPT_DASHBD_ACCOUNT_*`,
`org/standards/IRPT_DASHBD_DIM_*`, `infra/logic/registry/reporting_policies.json` and the gold keys; `DB-b-2`/`DB-b-4` write under
`infra/aws/lambda/investor-reporting/{reporting-publish,reporting}/`, `infra/aws/terraform/investor-reporting/{reporting-publish,reporting-read}/`,
`org/standards/IRPT_DASHBD_SERIES_CONTRACT.json`, `lambda-source-map.json` and the platinum keys. The two applies (publisher + schedule;
read function + route) are the issuer's served acts after the drains, each under its own ledger and, for the read route, both halves.

**Battery (the COO minimum before decomposing):** `comp-blast` -- RUN: the four cells write NEW keys and NEW functions only; 0
existing readers of any written key (comp-estate places `account_return_daily` in 0 of 135 chains; the platinum prefix is new).
`comp-routes` -- RUN as a reading: no existing route moves; `DB-b-4` adds one under its own function, so the static route table gains a
row at the apply, never a modified one. `comp-cache` -- DECLARED-NOT-APPLICABLE: no CloudFront or cache surface is touched in round 1.
`comp-pipescript overlap` -- DECLARED-NOT-APPLICABLE: the adapter shares no output key with any gold script (its table is new).

**Seating.** `DB-b-1` and `DB-b-3` go to `0.4.0_DS_ClientPlatform~S` (rule 13; its IRPT_BCKEND order TO-IB-pr-263 is superseded
@ed0be5b557, so the instance holds one project). `DB-b-2` and `DB-b-4` go to `0.9.0_WK_IRPT_DASHBD~1` (a new project's first slot),
spawned on the DS report that the gold landed. Andrew's seating of `2.0.0_SA_COO~P` on this backend beside IRPT_BCKEND is the PRD's
section 5 (the register row says so).

**Carried, not cut (the enrichment backlog, PRD section 3 B1-B8):** `account_class_daily`; activity and lots; `account_transaction`;
`market_topic_daily` and its scope row; the Inflection and Cottonwood adapters; `account_dim` and the household files; the C-LABEL switch;
the scheduled fire of the adapter (round 2, its own ledger, as IB-er-203 was to IB-er-202).

fanout: 2 of 2 chains, cap 8.

## 2. ROUND 2, WORKSTREAM B (2026-10-02 ~05:0xZ, issuer 2.0.0_SA_COO~P, on the CTO's round-1 analysis @57304c750b)

**Source:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_1_B_20261002.md` (msg 104053), its enrichment
list section 3 read as this round's rectangle. PRD v0.6 @aabc054e89, both halves current. Round 1's drain-end record @cdd81865b6.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-5` | E1, FWD-1 (the served leg): apply both planned roots -- `infra/aws/terraform/investor-reporting/reporting-publish/` (7 to add; the Lambda `irpt-49f-reporting-publish-lambda`, its roles and policies, schedule `irpt-49f-reporting-publish-daily` `cron(15 8 ? * MON-FRI *)` America/New_York, the production trigger; the gold it reads is T-1) and `infra/aws/terraform/investor-reporting/reporting-read/` (8 to add; `irpt-49f-reporting-read-lambda`, read-only on `opal-data-49financial/irpt/49financial/platinum/reporting/*`, its route on the IRPT API) -- under ONE packet with both never-widen halves and ONE ledger. THE ISSUER'S SERVED ACT, not a worker order (as round 1 said of both applies). Acceptance: workstream F's signed-in page fetches one account's series through `GET /api/scoped/investor-reporting/reporting/{account_id}/{which}` -- that fetch is FWD-1's real run (F's hop, `2.0.0_SA_COO~D` under C-LEASE). | WORLD | round 1 (merged @9000ce5a08) | C |
| `DB-b-6` | E3, FWD-8 enrichment (PRD v0.6 ruling 25): name the leg behind the 1,498.38 USD flow residual on 0027265115 -- an in-kind leg valued differently, or a leg classed internal here and external at the vendor -- from the LANDED responses (Schwab silver, Black Diamond bronze); no vendor call. Read cell, one record. | LOCAL | none | D |

**E2 is a row, not a cell** (the analysis): the retention family for `series.json.gz` (row W1-S1) goes to the registry's owner as
row `IRPT_DASHBD-S12`. **Carried, not cut:** like-day tie-out windows (Andrew's per-use vendor word, ruling 23); FWD-8's tolerance
(his). **Hygiene at the drain, not a cell:** the worker worktree's empty staging directories; the worktree and branch are removed on
Andrew's word (a recursive delete).

**Chain read.** M = 2 and independent: chain C = `DB-b-5` (the issuer's act; no worker), chain D = `DB-b-6` (one worker). N = 1
worker, K = 8. Write sets: `DB-b-5` writes AWS resources and `org/critical_paths/` only; `DB-b-6` writes one record under
`deliverables/0.9.0_WK_IRPT_DASHBD~1/`. `DB-b-6` is under the size floor and LOCAL: DIRECT-ACT (`<direct_act>true</direct_act>`; no
L8-L10; its close is the issuer's read of the record).

**Battery:** `comp-blast` -- RUN as a reading of the two saved plans: 15 resources to add, 0 to change, 0 to destroy; no existing
reader of any written key moves. `comp-routes` -- the static route table gains ONE row at the read root's apply (its own function);
no existing route is modified. `comp-cache` -- DECLARED-NOT-APPLICABLE (no CloudFront surface). `DB-b-6` touches no served surface.

**Seating.** `DB-b-6` -> `0.9.0_WK_IRPT_DASHBD~1` (the slot's queue is empty; its worktree DIR `C:\Users\AndrewBerman\Desktop\wk-irpt-dashbd-1`
is re-based on CLOUD at the spawn). `DB-b-5` is `2.0.0_SA_COO~P`'s own act.

fanout: 1 of 2 chains, cap 8, reason: chain C is the issuer's served act, so one worker covers the only worker chain.

## 3. ROUND 3, WORKSTREAM B (2026-10-02 ~06:5xZ, issuer 2.0.0_SA_COO~P, on the CTO's round-2 analysis @f5fbeaa543)

**Source:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_2_B_20261002.md` (msg 104097), section 2 read
as this round's rectangle: FWD-1 is live as of 2026-09-28; round 3 makes it current every trading day. Margin interest is RULED no
change (Opal's internal class stands; a stated methodology difference). Round 2's drain-end record @fde5518653.

**Builder output at the cut (rule 30, `lib/opal_naming.py` at HEAD, no refusal):** `name("irpt","49financial","reporting-gold",<kind>)`
-> `irpt-49f-reporting-gold-lambda`, `irpt-49f-reporting-gold-role`, `irpt-49f-reporting-gold-policy`, `irpt-49f-reporting-gold-daily`;
the scope-less source-map key `name("irpt", None, "reporting-gold", "lambda")` -> `irpt-reporting-gold-lambda` (row W1-S2's form).

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-7` | E1, FWD-1 current: the adapter `data/assets/scripts/gold/irpt_reporting/account_return_daily.py` packaged UNEDITED as a scheduled function on the holdings-performance pattern (own source dir `infra/aws/lambda/investor-reporting/reporting-gold/`, own root `infra/aws/terraform/investor-reporting/reporting-gold/`, `staged_from` pins). Each fire emits every trading day after the newest landed partition through T-1 by `lib/trading_calendar.py` (bounded), and no-ops on a non-trading day. The fire time is READ from the inputs' measured landing times (three Schwab silver prefixes + the holdings-performance gold the guard reads, whose producer fires 07:30 ET), before the publisher's 08:15 ET. Built, run locally once against the real inputs (no write), planned; NOT applied. | WORLD (a new scheduled function planned; artifact upload) | none | D |
| `DB-b-8` | E2, FWD-1 current: apply the planned `reporting-publish` root with its 08:15 ET schedule, re-planned at a tree carrying the policy-selector fix (row IRPT_BCKEND-S263), under its own packet with both halves. THE ISSUER'S SERVED ACT, not a worker order. Acceptance: the next morning the page reads "Data through" the new T-1 date with no seat starting either run. | WORLD | DB-b-7 SERVED | D |
| `DB-b-9` | E3 (ADDENDUM 1 A4): foreign tax paid (FTP/FC/WD, FTR/FC/WD) to internal. THIS CELL MEASURES AND PREPARES; nothing in it is served: (a) every reader of the CRO's code table and each served reader's delta if the two codes move; (b) the adapter's override retirement as a PATCH (never applied in the cell: retiring it before the table moves would put foreign tax back into F_t); (c) the adapter's output shown unchanged with the patch and the edited table together. The table edit is `4.0.0_SA_CRO`'s; the served move (table + engine read + patch) is ONE issuer packet with both halves after the drain. | SERVED (prep only) | none | E |

**Chain read.** M = 2: chain D = `DB-b-7` -> `DB-b-8` (the publisher waits on a served adapter clock); chain E = `DB-b-9`. N = 1 worker:
the laptop disk reads 96 percent used (11 GB free, `df` 06:5xZ), so no second worktree is provisioned; `DB-b-9` queues behind `DB-b-7`
on slot `~1`. Write sets are disjoint: `DB-b-7` writes `infra/aws/lambda/investor-reporting/reporting-gold/`,
`infra/aws/terraform/investor-reporting/reporting-gold/` and the source map's new entry; `DB-b-9` writes records and one `.patch` under
its deliverables folder only.

**Battery:** `comp-blast` -- `DB-b-7` creates new resources and writes NEW gold partitions only through its later apply; no existing
reader moves at the cut. `comp-schedule` -- the new schedule is read from measured landings and placed between the 07:30 ET producer
and the 08:15 ET publisher; the publisher's schedule stays planned and unapplied until `DB-b-7` is served. `comp-routes`,
`comp-cache` -- DECLARED-NOT-APPLICABLE (no route or cache surface). `DB-b-9` -- a census over the code table's readers (49F,
Inflection and Cottonwood each carry an `a05_ref_txn_classification.py`), read-only.

**Seating.** `DB-b-7`, then `DB-b-9` -> `0.9.0_WK_IRPT_DASHBD~1` (worktree DIR `C:\Users\AndrewBerman\Desktop\wk-irpt-dashbd-1`,
fast-forwarded to CLOUD at the spawn). `DB-b-8` is `2.0.0_SA_COO~P`'s own act.

fanout: 1 of 2 chains, cap 8, reason: disk at 96 percent (11 GB free) admits no second worktree; chain E queues behind chain D on slot ~1.


## 4. ROUND 4, WORKSTREAM B (2026-10-02 ~15:2xZ, issuer 2.0.0_SA_COO~P, on ANDREW-DIRECT ~13:2xZ card 4, record @0abef798f7)

Andrew approved ONE Black Diamond pull for the like-day windows of the five round-1 accounts (relayed by 1.0.0_SA_CTO msg 104263:
"cut it as an IRPT_DASHBD cell under Rule 27, with no seat calling the vendor outside it"). FWD-8 is then graded on agreement over the
like-day pairs (PRD v0.6 ruling 23).

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-10` | FWD-8: Opal's gap-free segments from the served reporting gold; ONE performancePeriod request per mapped account (at most 5) carrying those segments; the tie-out on like day sets | WORLD (one vendor read on Andrew's per-use word; 0 served bytes) | none | F |

fanout: 1 of 1 chains, cap 8, reason: one worktree (disk 7.3 GB free); DB-b-10 queues on the shared worktree DIR behind
IRPT_BCKEND TO-IB-pr-297 (slot 101), then runs on slot ~1.


## 5. ROUND 5, WORKSTREAM B (2026-10-02 ~18:3xZ, issuer 2.0.0_SA_COO~P, on CTO RULINGS batch 178 @2a537cbad4, msg 104324)

Andrew's IR fold-in (14:5xZ; `CTO_FOLD_IN_IRPT_THREE_BRIEFS_20261002.md` section 1) is this round's enrichment list for IRPT_DASHBD:
P-2 (every 49 Financial account) and P-3 (one per-client summary), with P-1 (under 2 s, a window change computes nothing on the
backend) as the acceptance. P-4 is IRPT_BCKEND's IB-pr-298. P-6 (retire PATH A for 49 Financial) lands in the same window as P-2's
served move. P-5 waits on Andrew's population vendor word. Enrichments only; no ENDPOINT change.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-11` | P-2: the 49 Financial holdings population declared as the reporting gold's account set; the producer and publisher MEASURED at that scale against the 900 s Lambda limit; the backfill planned; the widening built (nothing served) | WORLD (two served handlers' source; no deploy) | none | G |
| `DB-b-12` | P-3: `publisher.build_client_summary` -- one summary per directory client (YTD, QTD, 1Y, 3Y, SI precomputed; series name per account), its address from `opal_naming.address()`, a local dry run (nothing served) | WORLD (the served publisher's module; no deploy) | none | H |

Then, the issuer's acts: the backfill and deploy packet for P-2 (both halves), the summary's contract and read route for P-3 (to
1.0.0_SA_CTO), ~D's page, P-6's retirement in the same window, and the P-1 walk.

fanout: 1 of 2 chains, cap 8, reason: one worktree (disk 7.0 GB free); DB-b-11 then DB-b-12 on slot ~1, after IRPT_BCKEND IB-pr-298.


## 6. ROUND 6, WORKSTREAM B (2026-10-02 ~19:2xZ, issuer 2.0.0_SA_COO~P, on CTO RULINGS batch 181 @57e16650b5 and batch 182 @ff0acc0bc5)

FWD-8's tolerance is ruled at 0.35 pp per like-day window. Of round 4's 14 pairs, 11 are within it and 3 are beyond. FWD-8 grades
REALIZED once each is dispositioned: S22 (0027265115 06-25, the short-account income sign) is fixed and re-measured, and the other
two carry a stated reason. The tolerance is written into `dim_return_method` by its producer. The ruling says "the next round-4
cell"; GATE (x) refuses a new file into rounds 4 and 5, so this is ROUND 6 (IRPT_BCKEND row S267).

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-13` | FWD-8: the producer books a short's paid dividend as negative income (S22); the two other pairs' reasons measured; `emit_method_row` carries tieout_tolerance 0.0035 citing batch 181; re-measured from the stored BD responses with 0 vendor calls (nothing served) | WORLD (the reporting gold producer's source; no deploy) | DB-b-10 (merged) | I |

Then the issuer's acts: re-pin and redeploy the reporting gold with the fix, rewrite the affected account-days, and the method row's
served write, under one packet with both halves. Then FWD-8 goes back to 3.0.0_SA_CVO.

fanout: 1 of 1 chains, cap 8, reason: one worktree (disk 7.6 GB free); queued on slot ~1 after DB-b-11 and DB-b-12.


## 7. ROUND 7, WORKSTREAM B (2026-10-02 ~23:0xZ, issuer 2.0.0_SA_COO~P, inside its decomposition)

DB-b-11 (merged @0637b0787d) measured P-2 and filed three rows naming this seat. W1-S14: the landed history can never gain the
population without a backfill mode. W1-S12: the publisher's newest-partition account set drops 885 population accounts. W1-S13: the
shard fan-out needs the publish role to invoke its own function. One build cell; ROUND 7 under GATE (x) (IRPT_BCKEND row S267).

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-14` | P-2: the reporting gold's guarded backfill mode (an explicit event, chunk <= 25 trading days, refuses otherwise); the publisher's account UNION over the gold's history; `lambda:InvokeFunction` on the publish function itself (nothing served) | WORLD (two served handlers' source and a role policy's text; no deploy) | DB-b-13 (the S22 producer fix the backfill must run) | G |

Then P-2's packet (both halves): the producer re-pin with S22 and the method row, the gold and publisher deploys, the 23-chunk
backfill, the shard fan-out, the summary's contract and route (1.0.0_SA_CTO), P-6's retirement of 49 Financial PATH A in the same
window, and the P-1 walk with 2.0.0_SA_COO~D.

fanout: 1 of 1 chains, cap 8, reason: one worktree; queued on slot ~1 after DB-b-13.


## 8. ROUND 8, WORKSTREAM B (2026-10-03 ~00:1xZ, issuer 2.0.0_SA_COO~P, on CTO RULINGS batch 193 @ff04f71e47, msg 104467)

Batch 193 answers row W1-S18. C-VALUE is the account's EQUITY, `net_mv_plus_cash + margin_balance`, one rule for every account, as a
new `method_version`. It re-measures all 14 pairs, the population figure and the guard, and re-reads S22. FWD-8 is graded on the
re-measured pairs at 0.35 pp. GATE (x) refuses a new file into round 7, so this is ROUND 8 (IRPT_BCKEND row S267).

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-15` | FWD-8: the source declaration's value becomes equity; `METHOD_VERSION` is raised and its basis written by `emit_method_row`; all 14 pairs re-measured with Black Diamond's accrual stated, 0 vendor calls; S22 DISARMED or RESTATED; the population figure (6,685 of 7,570 positive on 2026-10-01) and C-GUARD's census re-measured; accounts with zero margin are unmoved (nothing served) | WORLD (the reporting gold producer's source; no deploy) | DB-b-13 (merged @9a169d31ad) | H |

Its write surface (the producer, its sources.json and a new test) is disjoint from DB-b-14's (the two reporting Lambdas and the
publish role). DB-b-14 was terminal at this issuance (@a8da9ba299), so DB-b-15 takes the one worktree after DB-b-14's drain.

Then the P-2 packet carries the new `method_version` with S22 and the backfill. The publisher refuses a file of mixed
`method_version` (`publisher.py:173`), so every landed day is rewritten under the new version before the first publish after the
deploy. The method row's two new columns need the `dim_return_method` contract's schema bump (row W1-S19). Row W1-S20, the
margin-interest adjustment credit's classification, is RULED by CTO batch 195 (@8dcb24b212): it is RETURN, so the 06-25 pair carries a
stated non-defect reason, and S20 is disarmed.

**PARKED CELL, P-5's tie-out (ANDREW-DIRECT ~00:4xZ 2026-10-03, card 2, record @fec2dc7266, relayed by 1.0.0_SA_CTO msg 104484).**
ONE Black Diamond performance pull for the 49 Financial population, scoped to Opal's gap-free segments and graded against
`tieout_tolerance` 0.35 pp with stated reasons (batches 181 and 195). It is the only vendor call this word licenses; no seat calls
Black Diamond outside it. Owner: 2.0.0_SA_COO~P. Un-park condition: P-2 has published every 49 Financial account on the new
`method_version` (batch 193). That is a served act of the P-2 packet, so the cell is cut in the first tick after that publish is
read back, as the next round GATE (x) admits.

fanout: 1 of 1 chains (H: DB-b-15 on slot ~2; chain G's DB-b-14 terminal), cap 8, reason: one open cell; slot ~1's worktree is removed at its drain and slot ~2 gets its own.


## 9. ROUND 9, WORKSTREAM B (2026-10-03 ~01:2xZ, issuer 2.0.0_SA_COO~P, on CTO RULINGS batch 197 @7563d60e68, msg 104491)

Batch 197 answers round 5's P-3 ask:
- (a) the per-client summary gets its OWN versioned contract, `org/standards/IRPT_DASHBD_CLIENT_SUMMARY_CONTRACT.json` 0.1.0;
- (b) the read route serves it ONLY when the scope enforcer covers every account it names; partial coverage is
  `OBJECT_NOT_COVERED`.

The issuer adds the act the ruling assumes: no served code writes `summary.json` today (`build_client_summary` is called only by
tests), so the publisher must write it. Two cells, disjoint from each other and from DB-b-15. ROUND 9 under GATE (x) (row S267).

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-16` | P-3 (a)+(b): the summary contract 0.1.0 (window_status with its four-postulate record and census; unpublished_account_ids kept); the read route's summary GET served only on full per-account coverage, declared in the reporting-read Terraform (nothing served) | WORLD (the served read Lambda's source and its route text) | DB-b-12 (merged) | I |
| `DB-b-17` | P-3 served path: the publisher's summaries pass writes every directory client's summary.json from all its published accounts, measured against 900 s and sharded by client if needed (nothing served) | WORLD (the served publisher's source; possibly its role's text) | DB-b-12, DB-b-14 (merged) | J |

Then the P-2 packet carries all of it with the backfill:
- DB-b-15's method version;
- DB-b-14's backfill, union and fan-out;
- DB-b-16's route and contract;
- DB-b-17's summaries pass and its trigger;
- P-6's retirement;
- the P-1 walk with 2.0.0_SA_COO~D.

fanout: 3 of 3 chains (H: DB-b-15 on slot ~2, running; I: DB-b-16 on slot ~3; J: DB-b-17 on slot ~4), cap 8, reason: disjoint write surfaces, disk 35 GB free.


## 10. ROUND 10, WORKSTREAM B (2026-10-03 ~02:3xZ, issuer 2.0.0_SA_COO~P, inside its decomposition)

Every build cell P-2 carries is merged (DB-b-13 to DB-b-17). Three rows bind the packet itself:
- W1-S19 and W2-S3: the method row carries four columns the `dim_return_method` contract does not declare;
- W4-S1: the publish artifact does not package `ids.py` or the firm registry.
The gold artifact is also pinned before DB-b-13's and DB-b-15's producer. One readiness cell closes all of it and proves the three
packages from the map without building, so the packet's builds are mechanical. ROUND 10 under GATE (x) (row S267).

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-18` | P-2, P-3: `dim_return_method` contract 0.3.0 (columns equal the emitted row; method_version 2 recorded); the three reporting map entries re-pinned to the merged blobs; the publish entry stages the four members the read entry already stages; a rehearsal materializes and imports each package (nothing built or uploaded) | WORLD (a standards contract and three package manifests; no deploy) | DB-b-15, DB-b-16, DB-b-17 (merged) | K |

Then the P-2 packet, both halves:
1. build and upload the three artifacts;
2. apply the gold, publish (with IAM) and read (with route) roots;
3. backfill every landed day under method_version 2, in chunks of at most 25 trading days, each rolled back per key on the
   versioned bucket;
4. the method row's served write, with the contract's schema_hash re-read;
5. the publish fan-out over every account;
6. the summaries pass and its trigger;
7. 2.0.0_SA_COO~D's picker on the summary route and P-6's retirement of PATH A for 49 Financial, in the same window (asked of
   ~D at 02:13Z);
8. the P-1 walk.

fanout: 1 of 1 chains, cap 8, reason: one open cell; worker 0.9.0_WK_IRPT_DASHBD~5 in its own worktree.


## 11. ROUND 11, WORKSTREAM B (2026-10-03 ~03:1xZ, issuer 2.0.0_SA_COO~P, on the CTO's L10 analysis of rounds 2-9 @e1e0be5ba0, msg 104517; PRD v0.7)

The analysis's enrichment list is this issuance's rectangle:

| # | item | how this issuance covers it |
|---|---|---|
| E1 | The P-2 packet, carrying W1-S12, S13, S14, S18, S19 with W2-S3, W4-S1, W4-S2 | IN FLIGHT as the issuer's act. DB-b-18 is merged @65a788ebf1. The three artifacts are built and uploaded @28480036ad, and the summaries trigger is written @7fc1014933. The plans read gold 0/1/0, publish 1/2/0 and read 1/1/0. P-6's mechanism goes to 1.0.0_SA_CTO, because PATH A's performance route has readers beyond the tab (print, export, method notes); its retirement lands in P-2's window. |
| E2 | W1-S17's build cell | `DB-b-19` below, risk LOCAL. It never holds E1. |
| E3 | P-5's one Black Diamond population pull | PARKED, as in section 8. It is cut in the first tick after P-2's publish of every 49 Financial account is read back. |
| -- | S15 and S19 | At the P-2 drain, not cells. S15 names both reporting routes in `routes.json`. S19 is the issuer's amendment: DB-7-AC1 counts kept organic landings, floor 10. |

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-19` | FWD-8's income field (PRD ruling 27): `dividend_interest_share_quantity` declared; a DIV debit admitted as income only when that quantity is negative; 38 debits (822.51) measured in, the zero-share row out, return DELTA=0 (nothing served) | LOCAL | DB-b-15 (merged) | L |

fanout: 1 of 1 chains, cap 8, reason: one build cell; E1 is the issuer's packet and E3 is parked on P-2's publish.

## 12. ROUND 12, WORKSTREAM B (2026-10-04 ~22:3xZ, issuer 2.0.0_SA_COO~P, on ANDREW-DIRECT ~22:0xZ "all recs approved" card 2, @66f1e98e98, msg 105003)

E3 / P-5 is un-parked. Its un-park condition holds: P-2 published every 49 Financial account, and ledger irpt-p2-window-20261003
closed 14/14. Andrew's card 2 lifts his 2026-10-03 data-collection hold for this ONE pull only. The tooling read found no
population script; the round-4 like-day pull is capped at five accounts. One account is one request, because each account's
gap-free segments are its own dateRanges, so the pull is about 7,570 requests. The issuer asked 1.0.0_SA_CTO to rule the run's
shape (pace, abort rule, one bearer, landing).

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-20` | P-5 build: bd_population_pull_e3.py (population from the served gold, xref mapping, unmapped with reasons, one request per mapped account) and its OFFLINE plan; pull refuses without --go, on a plan-hash mismatch, on a second pull, and without the CTO's shape ruling file | LOCAL (no vendor call; DRY_RUN=1) | none | B12 |
| (the run) | the ONE live pull, then the tie-out graded at 0.35 pp with stated reasons | WORLD | DB-b-20 and the CTO's shape ruling | the issuer's act after the ruling |

fanout: 1 of 1 chains, cap 8, reason: one build cell; the live run is the issuer's single act after the shape ruling. Worker
0.9.0_WK_IRPT_DASHBD~6 in its own worktree.

## 13. ROUND 13, WORKSTREAM B (2026-10-05 ~00:4xZ, issuer 2.0.0_SA_COO~P, on 1.0.0_SA_CTO RULINGS batch 248, msg 105044)

The ONE pull's first run (DB-b-20's script, launched by the issuer at 23:4xZ) aborted at call 19 of 5,252 on HTTP 401, and 18
responses landed. Batch 248 rules that the completion run over the accounts not yet answered is the SAME pull, with the cause read
first. The issuer's cause read made 2 vendor calls in the licensed complement:
- the session minted a fresh opaque bearer;
- account 14292051 answered 200 with it and landed (19 landed now).

That is class (a), a bearer expiry after about 18 calls. The completion mode re-mints every 10 calls.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-21` | P-5: completion mode (complement only, both denominators printed, bearer re-minted every 10 calls, same pace and abort rule) and its offline completion plan | LOCAL (no vendor call) | DB-b-20 (merged) | B13 |
| (the run) | the completion run over the complement (~5,233), then the 0.35 pp tie-out grade from the landed responses | WORLD | DB-b-21 | the issuer's act |

fanout: 1 of 1 chains, cap 8, reason: one build cell; the completion run is the issuer's act. Worker 0.9.0_WK_IRPT_DASHBD~7 in its
own worktree.

## 14. ROUND 14, WORKSTREAM B (2026-10-05 ~01:5xZ, issuer 2.0.0_SA_COO~P, on 1.0.0_SA_CTO RULINGS batches 249 and 250, msgs 105079 and 105082)

The sequential completion (DB-b-21) is vendor-latency bound, at about 12 s per call. It made 127 calls and landed 125, then aborted
on a second transport error (URLError): its retry budget was one per run. 144 of 5,252 have landed. Batch 249 rules a concurrent
shape: one coordinator and ONE shared bearer at the proven sign-in rate, 2 workers ramping to 6, 2 req/s aggregate. Batch 250 rules
one retry per call, a twice-failed account recorded FAILED and not fatal, the abort set, and one sweep over the FAILED set. The
ledger window was extended to 9 h before the relaunch (@df045ab288).

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-22` | P-5: the concurrent completion (coordinator-owned shared bearer, ramp, rate cap, per-call retry, FAILED record, abort set, sweep) and its offline plan carrying the ruling values | LOCAL (no vendor call) | DB-b-21 (merged) | B14 |
| (the run) | the concurrent completion over the complement (~5,108), the one sweep, then the 0.35 pp tie-out grade from the landed responses | WORLD | DB-b-22 | the issuer's act |

fanout: 1 of 1 chains, cap 8, reason: one build cell; the run is the issuer's act. Worker 0.9.0_WK_IRPT_DASHBD~8 in its own worktree.

## 15. ROUND 15, WORKSTREAM B (2026-10-05 ~07:3xZ, issuer 2.0.0_SA_COO~P, on the CTO's round-15 analysis @b09cafb7a4 and RULINGS batch 258)

The enrichment list is E1-E4:
- **E1** is the issuer's act. Batch 258 rules that the relaunch is the same pull. The ledger window was extended to 15 h first, and
  the DB-b-22 runner was relaunched detached at 07:14:45Z (pid 18184) over the complement (3,240 accounts), outside the session's
  2 h job cap.
- **E2** (the tie-out grade) is cut after E1 completes.
- **E3** and **E4** run in parallel now.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| (E1, the issuer) | complete the ONE pull; one FAILED sweep if batch 250 holds; the ledger closes on the S3 count vs 5,252 | WORLD | DB-b-22 (merged) | the issuer's act |
| `DB-b-23` | E3 / S23: routes.json declares both live reporting routes; the census still passes | LOCAL | none | B15a |
| `DB-b-24` | E4 / W7-S1: commit the shape ruling (bearer line -> batches 248-249) and the first pull record | LOCAL | none | B15b |
| (E2) | the 0.35 pp tie-out grade per account and segment | LOCAL | E1 | cut after E1 |

fanout: 2 of 2 chains, cap 8, reason: E3 and E4 are independent; E2 waits on E1. Workers 0.9.0_WK_IRPT_DASHBD~9 and ~10, each in its own worktree.

## 16. ROUND 16, WORKSTREAM B (2026-10-05 ~10:5xZ, issuer 2.0.0_SA_COO~P, on relaunch 2's silent stop)

Relaunch 2 (detached, 07:14Z) landed 848 accounts (S3 2,860 of 5,252). About 10:27Z its workers died on an uncaught
http.client.RemoteDisconnected on the bearer-mint path, and the record read complete with aborted null while 2,384 were never
requested. Relaunch 3 started 10:44:00Z (pid 43456) over the re-derived complement of 2,392, under the same rules. The runner is fixed
in one cell. Round 15 is complete: DB-b-23 @487429cb60, DB-b-24 @28efce5b4d.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-25` | P-5: the runner never stops silently (mint retry once, abort on a worker crash, complete only when the queue is empty) | LOCAL (no vendor call) | DB-b-22 (merged) | B16 |
| (E2) | the 0.35 pp tie-out grade | LOCAL | E1 (the pull) | cut after E1 |

fanout: 1 of 1 chains, cap 8, reason: one runner fix; the pull itself is the issuer's act. Worker 0.9.0_WK_IRPT_DASHBD~11 in its own worktree.

## 17. ROUND 17, WORKSTREAM B (2026-10-05 ~16:1xZ, issuer 2.0.0_SA_COO~P, the CTO's round-15 item E2)

E1 is COMPLETE: the ONE Black Diamond pull holds 5,252 of 5,252 accounts, after relaunch 3 (2,382), run 4 over the complement of 10
(9) and the batch 250 sweep (1; residue 0). Ledger P1 closed @54cbe5a477. DB-b-25 (the runner never stops silently) landed as a direct
act @98d439936a. E2 is now cut: the tie-out, which is ledger leg G1.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-26` | FWD-8 / P-5: the 0.35 pp tie-out over 9,082 segments, reasons from C-TIEOUT's classes or UNEXPLAINED, counts only | LOCAL (no vendor call) | E1 (complete) | B17 |

fanout: 1 of 1 chains, cap 8, reason: one grade over landed data. Worker 0.9.0_WK_IRPT_DASHBD~12 in its own worktree.

## 18. ROUND 18, WORKSTREAM B (2026-10-07 ~08:5xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's round-15..17 analysis @e363a194ed, msg 157)

Rounds 15-17 are closed: DB-b-23..26 terminal and VALID, ledger irpt-dashbd-e3-bd-population-pull-20261004 CLOSED, CVO compile
@88435e28a1 (ARMED 0). W12-S1 is RULED: the E2 tie-out compares on ONE gross basis, BD's own reported fee added back per segment; no
FEES reason; tolerance 0.35 pp and the closed set unchanged. The enrichment list is E1-E3:
- **E1** and **E2** are one chain: E2 reads E1's record.
- **E3** (`account_class_daily`, backlog B1, FWD-3) WAITS and is not cut: the CTO cuts it only once
  `infra/aws/lambda/v2_portal/_shared/etf_classification.py` carries the six-class values. Measured at 3dd25927f2: it still carries
  'fixed_income', 'equity', 'other' (last change 96f17cdbe9). Workstream F waits on E3's served table.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-27` | E1 / W12-S1: re-grade E2 on the gross basis; `bd_fee_addback` and `bd_gross_return` per segment; no net-of-fee Opal figure | LOCAL (no vendor call) | DB-b-26 (merged) | B18 |
| `DB-b-28` | E2: the residue -- UNEXPLAINED after E1, the +1-day segments over 2025-01-09, their overlap, each against the closed set | LOCAL | DB-b-27 | B18 |
| (E3) | `account_class_daily` and class contribution for 49F | SERVED | six-class values in `_shared/etf_classification.py` | waiting, not cut |

fanout: 1 of 1 chains, cap 8, reason: E2 consumes E1's record, so one worker queue; E3 waits on its named condition. Worker 0.9.0_WK_IRPT_DASHBD~13 in its own worktree.
