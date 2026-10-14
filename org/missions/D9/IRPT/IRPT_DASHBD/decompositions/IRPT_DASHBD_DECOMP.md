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
  "thread_account": "acct#89d0916a (49 Financial, Schwab master 08335338; Black Diamond relationship 22596361 in blackdiamond/49f/_ops/taxsma_roster.json), with the roster's other four active accounts as the round-1 sample",
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
platinum `address("irpt","49financial","platinum","reporting","account=acct#89d0916a","series.json.gz")` ->
`s3://opal-data-49financial/irpt/49financial/platinum/reporting/account=acct#89d0916a/series.json.gz` (and `manifest.json`);
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
| `DB-b-6` | E3, FWD-8 enrichment (PRD v0.6 ruling 25): name the leg behind the 1,498.38 USD flow residual on acct#89d0916a -- an in-kind leg valued differently, or a leg classed internal here and external at the vendor -- from the LANDED responses (Schwab silver, Black Diamond bronze); no vendor call. Read cell, one record. | LOCAL | none | D |

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
REALIZED once each is dispositioned: S22 (acct#89d0916a 06-25, the short-account income sign) is fixed and re-measured, and the other
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

## 19. ROUND 19, WORKSTREAM B (2026-10-07 ~10:2xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's round-18 analysis @62026ca511 as ruled in msg 308)

Round 18 is closed: DB-b-27 and DB-b-28 merged @0f304c6405; CVO compile ADJUDICATION_v6 @01ab2f9950, ARMED 0. On the gross basis 3,279 of
9,078 graded segments are UNEXPLAINED; 2,299 of them span the 2025-01-09 closure and 980 do not. The analysis's E1 asked for BD's
closure-day contribution from BD's own record; the landed pull holds only segment ranges (no daily data), so the issuer handed it back
(msg 307). The CTO ruled (msg 308): E2 is cut now over the 980; E1 is REPLACED by E1', an Opal-side test of BD's day count, no BD pull.
If E1' leaves most of the 2,299 unexplained, the split-range BD pull goes on Andrew's list as a per-use vendor act.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-29` | E1': the 2,299 closure segments recomputed on Opal's side with 2025-01-09 held (accrual, zero price return); count within 0.35 pp; the served figure unchanged | LOCAL (no vendor call; the gold read runs on the laptop under the standing rule) | DB-b-27 (merged) | B19a |
| `DB-b-30` | E2: the 980 non-closure UNEXPLAINED segments against the closed set with named evidence; final UNEXPLAINED and its share of 9,078 | LOCAL | DB-b-27 (merged) | B19b |
| (E3) | `account_class_daily` | SERVED | six-class values in `_shared/etf_classification.py` | waiting, not cut |

fanout: 2 of 2 chains, cap 8, reason: E1' and E2 read disjoint segment sets of the merged GROSS record. Workers 0.9.0_WK_IRPT_DASHBD~14 and ~15, each in its own worktree.

## 20. ROUND 20, WORKSTREAM B (2026-10-07 ~11:1xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's round-19 analysis @b402b7b2e3 and its E1 method ruling msg 400)

Round 19 is closed: DB-b-29 @33949e002d (E1' refuted the day-count hypothesis: 0 of 2,299) and DB-b-30 @5831f348b8; CVO compile
ADJUDICATION_v7 @e475d95687, ARMED 0. The split-at-2025-01-09 BD pull is listed for Andrew (2,299 accounts, 2,299 calls, 4,598 ranges)
and is NOT in this issuance. E1 asked for BD's booking dates, which the landed pull does not hold; the issuer handed it back (msg 399)
and the CTO ruled the method (msg 400): a Modified Dietz of Opal's dated flows over BD's own totals, with a midpoint negative control and
a flow-totals guard.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-31` | E1: measure the 226 inferred FLOW_TIMING segments (Dietz over BD's bmv/emv/netAdditions with Opal's dated flows; midpoint control; flows_match guard); the UNEXPLAINED count on a measured basis | LOCAL (S3 reads only) | DB-b-30 (merged) | B20a |
| `DB-b-32` | E2: the 754 non-closure UNEXPLAINED segments re-read with Opal's served series (readable since the fence join) against the closed set | LOCAL (S3 reads only) | DB-b-30 (merged) | B20b |
| (E3) | `account_class_daily` | SERVED | six-class values in `_shared/etf_classification.py` | waiting, not cut |
| (split BD pull) | BD's own figures either side of 2025-01-09 for the 2,299 closure segments | WORLD (vendor call) | Andrew's per-use word | not cut |

fanout: 2 of 2 chains, cap 8, reason: E1 and E2 read disjoint segment sets (226 and 754) of the merged round-19 record. Workers 0.9.0_WK_IRPT_DASHBD~16 and ~17, each in its own worktree.

## 21. ROUND 21, WORKSTREAM B (2026-10-07 ~11:4xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's round-20 analysis @58f3ed0501, msg 421)

Round 20 is closed: DB-b-31 @8e4c07ce7e, DB-b-32 @00d950283a. The CVO's read is taken: the Modified Dietz rule does not discriminate
(measured 22, midpoint control 19, overlap 3), so the 22 are not counted and UNEXPLAINED stays 3,279 of 9,078. FWD-8's thread is HELD on
Andrew's per-use word for the split BD pull (2,299 accounts, 2,299 calls, 4,598 ranges); no further no-vendor cell is cut against it.
The E3 gate has opened: `_shared/etf_classification.py` carries the six-class values (@63fa1a2e32).

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-33` | E1: `account_class_daily` and its contract for 49F, built beside the served producer and run locally over 50 accounts x 5 trading days; classes sum to the account within 1e-9; unclassified its own class; six classes plus unclassified only | SERVED (gold producer; no S3 write in this cell) | the six-class values (open) | B21 |
| (release) | upload of the producer, its first gold write and schedule under rule 13 | SERVED | DB-b-33 merged; never-widen halves | cut after B21 drains |
| (FWD-8) | the split BD pull | WORLD (vendor call) | Andrew's per-use word | held |

fanout: 1 of 1 chains, cap 8, reason: one build cell; its release follows it. Worker 0.9.0_WK_IRPT_DASHBD~18 in its own worktree.

## 22. ROUND 22, WORKSTREAM B (2026-10-07 ~12:1xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's round-21 analysis @214a0ef324, msg 448)

Round 21 is closed: DB-b-33 @75717e8580 (account_class_daily built and run locally; REMEDIATION_v7 @d116b31dba). W18-S2 RULED: release
as is, the unclassified share of value shown beside the class breakdown with its reason; single-stock and money-market coverage is ASKED
of MDPF_SECCLASS through the laptop, then the table is re-run. The release is the smallest change: the existing reporting-gold function
also emits account_class_daily; its role writes one more prefix; the schedule is unchanged.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-34` | E1 prep: handler + bundle + role + declaration (W18-S1) + tests; local release run (returns DELTA=0, class identity, unclassified share); the never-widen packet | SERVED (source only; no apply) | DB-b-33 (merged) | B22 |
| (apply) | safe-apply of the reporting-gold root, the first fire, the after-read (CTO criteria 2-3) | SERVED | DB-b-34 merged; both halves signed; the dell2 terraform kit | the issuer's act |
| (FWD-8) | the split BD pull | WORLD | Andrew's per-use word | held |

fanout: 1 of 1 chains, cap 8, reason: one prep cell; the apply follows it. Worker 0.9.0_WK_IRPT_DASHBD~19 in its own worktree.

## 23. ROUND 23, WORKSTREAM B (2026-10-07 ~13:4xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's round-22 analysis @a1873a8be7, msg 615)

Round 22 is closed: DB-b-34 @d48052d79b (the account_class_daily release prepared; REMEDIATION_v8 @372500963a). Both never-widen halves
are given (CTO @9816b17511, COO @13363d403b); the apply waits only on the dell2 terraform kit, and this seat sets the source-map pins at
the apply (ruling msg 600). FWD-8 stays held on Andrew's split-pull word. The analysis takes PRD backlog B2 (FWD-4).

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-35` | E1: account_activity_daily, account_lot_realized, account_lot_unrealized_daily for 49F, built and run locally; one account-window ties to the cent; each realized lot ties to its closing transaction; builder names | LOCAL (no S3 write) | none | B23 |
| (class release apply) | safe-apply of reporting-gold with the pins | WORLD | the terraform kit | the issuer's act |
| (FWD-8) | the split BD pull | WORLD | Andrew's per-use word | held |

fanout: 1 of 1 chains, cap 8, reason: one build cell. Worker 0.9.0_WK_IRPT_DASHBD~20 in its own worktree.

## 24. ROUND 24, WORKSTREAM B (2026-10-07 ~15:1xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's round-23 analysis @9f285400cf, msg 745)

Round 23 is closed: DB-b-35 @a8df9a5880 (the activity and lot tables built locally; REMEDIATION_v9 @8a5b7c61e6). FWD-4 is NOT shown: the
activity identity ties on 52 of 91 account-windows; 39 fail, most by cents, one (acct#f0faa651) by ~1.1M; the passing window exercised no
realized gain and no flow. W20-S1 and W20-S3 ride the release packet. The release of these tables waits on E2 and has its own halves.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-36` | E1: diagnose W20-S2 -- the ~1.1M window term by term, a transaction-type census (unsigned types), the 39 gaps classed ROUNDING (<= 0.05, stated before the run) or MISSING-TERM | LOCAL | DB-b-35 (merged) | B24 |
| `DB-b-37` | E2: fix the named cause; re-grade the same 91 accounts; one window with realized gain and a flow ties to the cent | LOCAL | DB-b-36 | B24 |

fanout: 1 of 1 chains, cap 8, reason: E2 fixes what E1 names, so one worker queue. Worker 0.9.0_WK_IRPT_DASHBD~21 in its own worktree.

## 25. ROUND 25, WORKSTREAM B (2026-10-07 ~17:2xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's round-24 analysis @99580aac8c, msg 899)

Round 24 is closed: DB-b-36 and DB-b-37 @f71fd042c1 (REMEDIATION_v10 @f7bd5e9a6c). FWD-4 is exercised locally on one window (realized
gain and both flows, gap 0.0075) and not served; 55 of 91 windows tie, 32 of the 36 misses are ROUNDING. The release of the activity and
lot tables follows E1 under its own halves, carrying W20-S1 and W20-S3.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-38` | E2: the lot-lag bound measured (W21-S5); LEG_LAG_DAYS set from the distribution with its percentile | LOCAL | DB-b-37 (merged) | B25 |
| `DB-b-39` | E1: the 4 non-rounding windows read against lot events and fixed through the rule; the 91 windows re-run (W21-S4) | LOCAL | DB-b-38 | B25 |
| `DB-b-40` | E3: the pandas option once per process; the served classify_and_sum hardened against None in source (W21-S6) | LOCAL | DB-b-39 (write set) | B25 |

fanout: 1 of 2 chains, cap 8, reason: E1 re-runs with E2's LEG_LAG_DAYS (a data edge); E3 has no data edge but edits the same producer file as both, so it runs last in the one queue (cut by write set). Worker 0.9.0_WK_IRPT_DASHBD~22 in its own worktree.

## 26. ROUND 26, WORKSTREAM B (2026-10-07 ~20:5xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's round-25 analysis @3543da2f4d, msg 1079)

Round 25 is closed: DB-b-38..40 @5ffd7b740d (REMEDIATION_v11 @80d6ea4ef3). The round-24 sample ties except for rounding: 58 of 91
within one cent, 33 within 0.05, 0 missing a term. FWD-4 grades REALIZED only when a person reads the served tables; the next act is
their release.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-41` | E1: release prep for the activity and lot tables in the served reporting-gold function (contracts complete with keys and basis_source; source names into sources.json; handler, bundle, role; never-widen packet covering the whole next apply of the root, the unapplied class release included) | WORLD (paths floor; the analysis classes it SERVED) | DB-b-40 (merged) | B26-1 |
| `DB-b-42` | E2 criterion (2): can a served input to classify_and_sum carry a repeated index label; refuse with a named reason if so | LOCAL | DB-b-40 (merged) | B26-2 |

E2 criterion (1) (the None hardening tested on pandas 2.2.3) is NOT cut: dell2 has Python 3.14 with pandas 3.0.6 only and downloads are
barred; the environment is requested from the laptop through 1.0.0_SA_CTO~DELL2, and the cell is cut when it lands.

fanout: 2 of 2 chains, cap 8, reason: no data edge between E1 and E2, and the write sets are disjoint (E1: handler, terraform, activity producer, sources.json, contracts; E2: account_return_daily.py and its None test file). Workers 0.9.0_WK_IRPT_DASHBD~23 and ~24, each in its own worktree.

### 26a. Round 26 amendment (2026-10-07 ~21:1xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2 msg 1092)

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-43` | E2 criterion (1): the None-hardening test (`tests/test_account_return_daily_none.py`) run on the served layer's pandas 2.2.3 by LAPTOP RELAY: the test and the producer at pin b65c14f4df, relayed by 0.0.0_AB_MSTR~DELL2, the result returned as a FILE (pandas version printed beside the pytest summary). An issuer act, no worker; graded by the issuer on the returned file | LOCAL | DB-b-40 (merged) | B26-3 |

The pandas 2.2.3 kit goes through the package route in parallel (4.0.0_SA_CRO~D2 intake, then 1.0.0_SA_CTO~DELL2). If DB-b-42 changes
`classify_and_sum` (verdict CAN), the relay re-runs at the drain's pin.

### 26b. Round 26, WORKSTREAM BD (the FWD-8 Black Diamond thread; its own issuance) (2026-10-07 ~21:4xZ, issuer 2.0.0_SA_COO~D2, on Andrew's per-use word relayed by 0.0.0_AB_MSTR~DELL2 msg 1103)

FWD-8's split Black Diamond pull, listed since round 20 and held on Andrew's word, is cut. The word (record @5ef6d33141) is for ONE
read-only pull: 2,299 accounts, 2,299 calls, 4,598 date ranges, each closure segment of `CLOSURE_ALIGN_E1P.json` split at 2025-01-09
(round-19 analysis @b402b7b2e3 section 2). Expected outcome, both branches, as stated there: (A) the split figures tie within 0.35 pp on
most of the 2,299, naming BD's closure-day booking as the cause; (B) they do not, and the residue read widens.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-44` | the split pull's plan and runner, built and planned OFFLINE (no vendor call) | LOCAL | DB-b-29 (merged) | B26-4 |
| (issuer act) | `run --go` of the plan: the LIVE pull, once, under the word | WORLD (vendor call) | DB-b-44 | B26-4 |
| (next cell) | the tie-out of the split figures against Opal's, branches A/B graded | LOCAL | the landed pull | B26-4, cut when the pull lands |

fanout: 1 more chain (B26-4), worker 0.9.0_WK_IRPT_DASHBD~25 in its own worktree; disjoint from DB-b-41's write set.

## 27. ROUND 27, WORKSTREAM BD (2026-10-07 ~23:5xZ, issuer 2.0.0_SA_COO~D2, on laptop 1.0.0_SA_CTO msg 106630 via 0.0.0_AB_MSTR~DELL2 msg 1145)

DB-b-44 is closed (@35a0fc34d4). Its live run aborted on dell2 before any vendor call: this box's user cannot read
`blackdiamond/49f/session` (abort record @e39ea3dcca). The laptop CTO ruled: a task order to a fresh laptop `0.7.0_AE_CloudOps~I`, the
pair signed by dell2's CTO and COO, the GO by the laptop CTO.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-45` | the split BD pull run ONCE on the laptop (at most one sweep); records returned as files and graded on dell2 | WORLD (vendor call, S3 writes under a new prefix) | DB-b-44 (merged) | B26-4 |
| (next cell) | the tie-out of the split figures, branches A/B graded | LOCAL | DB-b-45 | B26-4, cut when the records return |

fanout: 1 of 1 chains, cap 8, reason: one run of one plan. Seat 0.7.0_AE_CloudOps~I (laptop), not a worker.

## 28. ROUND 27, WORKSTREAM B (2026-10-08 ~02:1xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2 msg 1184, correcting its round-26 analysis @0ae2f15e5c)

Round 26 is closed (DB-b-41, -42, -44 VALID; ADJUDICATION_v11/v12). The round-26 analysis cut no round 27; on the issuer's ask the CTO
corrected it: S31 needs its own run and S32 waits on DB-b-43, so neither graduates at DB-b-45's drain. S31 is cut now.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-46` | S31: the extended handler over the whole 49F population for one trading day, wall and peak per stage against 900 s / 2048 MB, the per-account tail; a breach reported with its size | LOCAL | DB-b-41 (merged) | B27 |

fanout: 1 of 1 chains, cap 8, reason: one measurement. Worker 0.9.0_WK_IRPT_DASHBD~26 in its own worktree.

## 29. ROUND 28, WORKSTREAM B (2026-10-08 ~07:3xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's round-27 analysis @7fa28c7d6d, msg 1222)

Round 27 is closed: DB-b-46 @acb7066605 (ADJUDICATION_v13 @d640bc455f). S31 measured BREACH: the lots stage refuses on 87 realized lot
ids repeated within a day (175 rows, 36 accounts, distinct lots) and peaks at least 2,759.5 MB against 2,048 MB. Rulings: the key is the
smallest measured column set; batch first, raise memory only if the batched peak on pandas 2.2.3 still breaches.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-47` | E1: the realized-lot key measured on the 175 rows; contracts + stage use it; true duplicates still refuse | LOCAL | DB-b-46 (merged) | B28 |
| `DB-b-48` | E2(1): the lots stage batched; the full day re-run at two batch sizes, lots peak flat | WORLD (handler path floor; applies nothing) | DB-b-47 (the stage must not refuse) | B28 |
| (issuer act) | E2(2): the batched run on pandas 2.2.3 -- the laptop carries pandas 2.3.3 (MSTR msg 1136), so it runs on dell2 when the Python 3.12 kit lands, with DB-b-43 | LOCAL | DB-b-48 | B28 |

fanout: 1 of 1 chains, cap 8, reason: E2 measures the stage only once E1 stops its refusal, and both edit the same producer. Worker 0.9.0_WK_IRPT_DASHBD~27 in its own worktree.

## 30. ROUND 28, WORKSTREAM BD (2026-10-08 ~13:5xZ, issuer 2.0.0_SA_COO~D2, the tie-out cell named in section 27)

DB-b-45 is complete @3efc66cf42: the one split Black Diamond pull ran on dell2 at 12:37:21Z after the secrets grant applied (11:33:48Z);
2,299 of 2,299 landed under pull=split20261007, 0 FAILED. The tie-out grades FWD-8's two branches (round-19 analysis section 2).

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-49` | the split tie-out: BD's two halves against Opal's served returns for the 2,299 segments; branch A (> half tie on both halves within 0.35 pp) or B; the recompose control | LOCAL | DB-b-45 (complete) | B26-4 |

fanout: 1 of 1 chains, cap 8, reason: one comparison over one landed pull. Worker 0.9.0_WK_IRPT_DASHBD~28 in its own worktree.

## 31. ROUND 29, WORKSTREAMS BD + B (2026-10-08 ~19:0xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's round-28 analysis @e9b17e6e75, msg 1428)

Round 28 is closed: DB-b-47 + DB-b-48 merged @24d088b96e, DB-b-49 @a556d87e79 (round-close-check MAY-CLOSE). FWD-8 reads BRANCH B:
the divergence is after 2025-01-10. S34 (440 accounts whose BD halves do not recompose) gates any Opal repair. No vendor call is owed.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-50` | E1: class S34's 440 accounts (closed cause set + named other); trace the 724.16 pp outlier; the overlap with the 1,834 right-half misses | LOCAL | DB-b-49 (merged) | B29-1 |
| `DB-b-51` | E2: the right-half gap's shape for the 1,528 misses outside S34, Opal's components only; top driver; the 2,220 left-half ties as control | LOCAL | DB-b-49 (merged; the population is DB-b-49's per-row flag, not DB-b-50's output) | B29-2 |
| `DB-b-52` | E3 (W27-S2): the full run over 7,604 accounts <= 750 s; the chosen batch size set as the producer's default | LOCAL | DB-b-48 (merged) | B29-3 |

fanout: 3 of 3 chains, cap 8, reason: three independent reads -- E1 and E2 take fixed populations from DB-b-49's record, E3 edits only the lots producer. Workers 0.9.0_WK_IRPT_DASHBD~29, ~30, ~31, one worktree each.

## 32. ROUND 30, WORKSTREAMS BD + B (2026-10-08 ~21:1xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's round-29 analysis @72ae174b3c, msg 1630, E1 recast by msg 1641)

Round 29 is closed: DB-b-50 @8de470994a, DB-b-51 @1ee0fd9e99, DB-b-52 @50a0ebae91 (round-close-check MAY-CLOSE). S34 is closed: 437 of 440
were round 18's fee add-back. The lead is the advisory fee: Opal's served return is gross of FEE-MANAGEMENT (external flow), BD's is
net. The analysis's E1 (net gap minus BD's add-back drag) is an identity on the record (max 1.8e-12, 0 of 1,527 within 0.35 pp), so it
is recast against an Opal-side drag; the CTO adopted the recast (msg 1641).

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-53` | E2: Schwab fee-row census for the 1,528, the producer's classing from source lines, one account traced; per-day fee table | LOCAL | DB-b-49 (merged) | B30-1 |
| `DB-b-54` | E1 (recast): net-basis gap vs Opal-side daily-compounded fee drag; CONFIRMED iff >= 80% within 0.35 pp | LOCAL | DB-b-53 (its fee table) | B30-1 |
| `DB-b-55` | E3 (W31-S2): p95 of >= 5 full runs at the default batch <= 750 s, or the default lowered | LOCAL | DB-b-52 (merged) | B30-2 |

fanout: 2 of 2 chains, cap 8, reason: E1 consumes E2's fee table (one chain, one worker in order); E3 is independent. Workers 0.9.0_WK_IRPT_DASHBD~32 (DB-b-53 then DB-b-54) and ~33, one worktree each, cut from box/dell2.

### 32 addendum -- ROUND 30 AMENDMENT 1 (2026-10-08 ~21:3xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ruling on row S35, msg 1660)

Row S35 (3.0.0_SA_CVO, 21:17Z) corrects W30-S1 and the advisory-fee lead. Opal's served return is gross BY DESIGN (fee_amount null,
FEE_RAIL_UNUSED). The right-half gap was the tie-out's ADDITIVE fee add-back: compounding it moves the median from +0.567 pp to
+0.043 pp and tied from 0 to 1,334 of 1,527.

DB-b-54 is SUPERSEDED. DB-b-53 is RE-CUT IN PLACE as the replacement cell (the gate admits one issuance per round: a re-cut modifies, it adds no file). Its earlier face, the fee census, is withdrawn; worker ~32 was stopped by the issuer and its branch is not drained. DB-b-55 stands.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-53` (re-cut) | the add-back compounded in the tie-out reader (a unit test that adjacent ranges chain); the full 9,078-segment 49F tie-out re-graded on the compounded basis, before/after and share within 0.35 pp; remaining misses named from the closed set | LOCAL | none open (round 18's record and pulls landed) | B30-3 |

fanout: 2 of 2 live chains (B30-2 DB-b-55 running, B30-3 DB-b-53 re-cut), cap 8, reason: the replacement reads round 18's landed inputs only. Worker 0.9.0_WK_IRPT_DASHBD~34, cut from box/dell2.

## 33. ROUND 31, WORKSTREAM BD (2026-10-09 ~00:3xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's round-30 analysis @4cfe197b0c, msg 1965)

Round 30 is closed: DB-b-53 re-cut @1698740c8d (compounded tie-out 7,459 of 9,078 within 0.35 pp) and DB-b-55 @495789d6ec (batch 1000
adopted). DB-b-54 is superseded. ~32's branch is CLOSED under S35: its commits are kept by the local tag `closed/wk-IRPT_DASHBD-32`
(ffb214d212), not drained.

The compounded basis carries an unexplained regression (181 within -> outside) and two named residues (UNEXPLAINED 1,203; FLOW_TIMING 370).

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-57` | E1: the 181 within -> outside, one traced cause each; a compounding defect fixed in a new module with within >= 7,459 | LOCAL | DB-b-53 re-cut (merged) | B31-1 |
| `DB-b-58` | E2: the 1,203 UNEXPLAINED classed; the top classes to 80% fixed or carried as named causes | LOCAL | DB-b-53 re-cut (merged) | B31-2 |
| `DB-b-59` | E3: the 370 FLOW_TIMING graded at flow-start and flow-end, the swing per segment, nothing adopted | LOCAL | DB-b-53 re-cut (merged) | B31-3 |

fanout: 3 of 3 chains, cap 8, reason: three disjoint populations over the same landed records; each writes only its own folder (a fix is a new module there). Workers 0.9.0_WK_IRPT_DASHBD~35, ~36, ~37, one worktree each, cut from box/dell2.

## 34. ROUND 32, WORKSTREAM BD (2026-10-09 ~01:0xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's rounds 30-31 analysis @fe8e06016b, msg 2007, on ADJUDICATION_v16)

Rounds 30 and 31 are closed and compiled together. Within 0.35 pp: round 18 additive 5,416; round 30 compounded 7,459; round 31 daily-mean
fee base 8,088 (reached twice, independently). The CTO's rulings:
- `tieout_compound_v2.py` is the reader of record;
- the tie-out reader adopts flow-START (served values unchanged).

ISSUER RULING: the tie-out code path is `org/missions/D9/IRPT/IRPT_DASHBD/tieout/`. It is project-owned, never served, and outside every
deploy lane.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-60` | E1: the reader of record at `tieout/tieout_reader.py`; the fee-base writer census = 1 (~35's v2 and ~36's classifier import it); re-grade 8,088 held | LOCAL | DB-b-57, DB-b-58 (merged) | B32-1 |
| `DB-b-61` | E2: FLOW_CONVENTION = "start" in the reader; full re-grade; every IN->OUT named | LOCAL | DB-b-60 (it edits DB-b-60's reader) | B32-1 |
| `DB-b-62` | E3: LARGE_FLOW_DAY 170 traced by sub-class, each fixed or named | LOCAL | DB-b-58 (merged) | B32-2 |

fanout: 2 of 2 chains, cap 8, reason: E2 edits the reader E1 creates (one chain, one worker in order); E3 reads round 31's records only. Workers 0.9.0_WK_IRPT_DASHBD~38 (DB-b-60 then DB-b-61) and ~39, cut from box/dell2.

## 35. ROUND 33, WORKSTREAM BD (2026-10-09 ~01:3xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's round-32 ADDENDUM 1 @78928255f6, on ADJUDICATION_v17)

Round 32 is closed: the reader of record is `tieout/tieout_reader.py` (one fee-base writer), and flow-start gives 8,315 of 9,078. The CTO's
rulings:
- adopt both W39-S1 reader fixes;
- measure the activity-and-lot release on the SERVED pandas 2.2.3 by one ad-hoc QA invoke, or report the measured refusal; a kit request
  follows only a refusal.

Issuer pre-read at cut (no invoke): the deployed function `irpt-49f-reporting-gold-lambda` was last modified 2026-10-03 on layer
`irpt-performance-native-layer:1`. Its declared package (lambda-source-map) does NOT list `account_activity_lots.py`. DB-b-64 reads the
deployed bytes and takes the branch rule.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-63` | E1: both W39-S1 fixes in the reader of record; 9,078 re-graded, within >= 8,315; every IN->OUT named | LOCAL | DB-b-61, DB-b-62 (merged) | B33-1 |
| `DB-b-64` | E2: the served pandas 2.2.3 read -- deployed package + layer; one dry_run invoke only if the lots producer is packaged, else a measured REFUSED | WORLD | none open | B33-2 |
| `DB-b-65` | E3: NEAR_ZERO_BALANCE 153 traced by sub-class, each fixed or named | LOCAL | DB-b-58 (merged) | B33-3 |

fanout: 3 of 3 chains, cap 8, reason: disjoint surfaces -- E1 edits the reader, E2 reads the deployed function, E3 reads round 31's records. Workers 0.9.0_WK_IRPT_DASHBD~40, ~41, ~42, cut from box/dell2.

## 36. ROUND 34, WORKSTREAM BD (2026-10-09 ~02:0xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's round-33 ADDENDUM 2 @47c849d75b, msg 2116, on ADJUDICATION_v18)

Round 33 is closed. The reader of record gives 8,385 of 9,078, of which the near-zero 79 are pending a shim-free re-run (row S36). The
served function runs pandas 2.2.3 but packages no lots producer, so the read was REFUSED (measured). The kit request (laptop
NFRA_CTLPLN.TO-CT-k-2 AMENDMENT 10) is in transit.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-66` | E1: repair the two callers (~35 crossover_e1, ~39 large_flow_e3; each passes its own test) and re-run DB-b-65 shim-free on the reader's own mean | LOCAL | DB-b-63, DB-b-65 (merged) | B34-1 |
| `DB-b-67` | E2: the lots peak on the pandas 2.2.3 kit, FITS/BREACH against 2,048 MB, beside 3.0.6; decides the activity-and-lot release | LOCAL | DB-b-64 (merged) + the kit's arrival | B34-2 |
| `DB-b-68` | E3: FLOW_TIMING_AFTER_FEE_BASE 116 traced, status under the reader of record | LOCAL | DB-b-63 (merged) | B34-3 |

fanout: 3 of 3 chains, cap 8, reason: disjoint surfaces. Workers 0.9.0_WK_IRPT_DASHBD~43 and ~45 spawn now; ~44 spawns when the kit lands and the issuer writes its path to `deliverables/2.0.0_SA_COO~D2/relay/KIT_PATH_PY312_PANDAS223.txt`. All cut from box/dell2.

## 37. ROUND 35, WORKSTREAM B (2026-10-09 ~02:5xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's round-34 ADDENDUM 3 @fde009aab3, on ADJUDICATION_v19)

Round 34 is closed: tie-out 8,433 of 9,078, and the pandas 2.2.3 kit read FITS (1,500.7 of 2,048 MB). The CTO ruled the withheld
activity-and-lot release's S31 and S33 MET; S32 is MET only on a read the packet carries; the release proceeds to its never-widen pair,
COO half first.

Issuer pre-read: 6 of the round-26 packet's 19 file-list rows are stale at HEAD (handler.py, account_activity_lots.py, lib/opal_naming.py,
three registry files), so the packet is RE-CUT at HEAD before any half is signed.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-69` | the release ask: the S32 read on the kit (classify_and_sum vs the tested version; returns old pin vs HEAD; DB-b-43 on 2.2.3), one full kit run's refusal count for S33, and the packet re-cut at HEAD with both halves UNSIGNED | WORLD | DB-b-67 (merged) + the kit (relay @7aea38af1e) | B35-1 |

fanout: 1 of 1 chains, cap 8, reason: one packet over one release. Worker 0.9.0_WK_IRPT_DASHBD~46, cut from box/dell2. On its drain the issuer reads the packet and signs or withholds the COO half; the CTO signs its half on it.


## 38. ROUND 36, WORKSTREAM B (2026-10-09 ~03:5xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's round-35 ADDENDUM 4, on ADJUDICATION_v20 @e9d4ac3755, and PRD v0.8 FWD-11 @e8b44a8379, amended @3eb7dbcf36)

**Where round 35 left things.**
- Round 35 is closed MAY-CLOSE.
- The activity-and-lot release is signed on both halves: COO @cbad72eb7b, CTO @75acbfcb50.
- The rollback anchor is recorded @3285eae1a5.
- Row S37 holds the W23-S1 bucket-admission read.

**FWD-11 (Andrew-direct ~03:3xZ):** every client firm, each through its own adapter. Each firm's served release later goes under its own
never-widen pair.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-70` | E1, FWD-4: the 49F R35 release APPLY (pins, rebuild, plan 0/3/0, safe-apply, dry_run under 85%, A1 to A6 on the first fire, A4 DELTA=0 before any second fire) | WORLD | both halves (given) | B36-1 |
| `DB-b-71` | E2, FWD-11: Cottonwood's adapter returns, offline on a sample, tied out against its own reported source (Commonwealth, PRD v0.8 @3eb7dbcf36) | LOCAL | none | B36-2 |
| `DB-b-72` | E3, FWD-11: Inflection's adapter returns from Orion, offline on a sample, tied out against its own reported source; lots NO_LOTS until Eclipse lots are shown populated | LOCAL | none | B36-3 |

**fanout:** 3 of 3 chains, cap 8. Reason: three independent cells (one release, two firm adapters) with disjoint write surfaces.
Workers 0.9.0_WK_IRPT_DASHBD~47, ~48 and ~49, each cut from box/dell2.


## 39. ROUND 37, WORKSTREAM B (2026-10-09 ~05:3xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's round-36 ADDENDUM 5, on ADJUDICATION_v21 @37daf4f637, PRD v0.9 @e8f96f579c)

**Where round 36 left things.**
- Round 36 is closed. The R35 release was applied, then rolled back (CTO msg 2393: the sizing refused on a lot-key repeat, and four members
  sat at older pins). The rollback is read live; the ledger is CLOSED.
- Cottonwood's tie-out is NOT MEASURABLE, carried by ADVI_COTBKF (ADDENDUM 5).
- The ratified Orion taxonomy governs, and a proposal cell follows.
- Consolidation (ruling @ca5f74553d, PRD v0.9): IRPT_CUSTDY (@185805a565) and ~P's performance scope (@4bfb22b033) were handed to this issuer.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-73` | E1, FWD-4: the realized-lot key extended to separate the 2026-10-07 repeats; the population re-size on the 2.2.3 kit (10-06, 10-07), 0 refusals | WORLD | none | B37-1 |
| `DB-b-74` | E2, FWD-4: the R37 release packet with EVERY member pinned at HEAD bytes, sizing from DB-b-73; halves UNSIGNED | WORLD | DB-b-73 | B37-1 |
| `DB-b-75` | E3, FWD-11: Inflection's Orion custody-master registry row (W49-S1) | WORLD (registry path floor) | none | B37-2 |
| `DB-b-76` | E4, FWD-11: Inflection gross vs Orion gross, like for like, with fees sliced supervised/unsupervised and billed/unbilled (Andrew @669ab7d677) | LOCAL | none | B37-3 |
| `DB-b-77` | E5, FWD-11: the rule-24 amendment proposal for the two departing Orion flow classes (W49-S3) | LOCAL | none | B37-4 |

**Not cut this round, with the condition that un-parks each:**

| item | waits on |
|---|---|
| the svc-custody-statement mint landing, and CU-g-2a (the first real retained Performance client statement, which carries E-P9's persist reads) | a 0.7.0_AE_CloudOps seat free for this project. ~DELL2 holds orders on other projects, so the seating check refuses it (one project per Tier-2 seat instance). Asked of 0.0.0_AB_MSTR~DELL2 |
| CU-g-6 (the PROD render) | Andrew's word (open-calls row dell2-20261008T192510Z-0347): it is a client-facing PROD page |

**fanout:** 4 of 4 chains, cap 8. Reason: one release chain (E1 then E2) and three independent Inflection cells with disjoint write
surfaces. Workers 0.9.0_WK_IRPT_DASHBD~50 to ~54, cut from box/dell2. ~51 is spawned when DB-b-73 drains.


## 40. ROUND 38, WORKSTREAM B (2026-10-09 ~06:5xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's round-37 ADDENDUM 6 @fb5579ddfc, on ADJUDICATION_v22 @153e101791)

**Where round 37 left things.**
- Round 37 is closed.
- The R37 release pair is signed: COO @9395a9c1bc, CTO @e64eb96736.
- The taxonomy proposal is ADOPTED as additive keys.
- Orion's gross is to land as silver.
- The fee slices print PARTIAL.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-78` | E1, FWD-4: the R37 apply. Pins, root restore, plan 0/3/0, safe-apply, a population dry_run under 85% gating the first fire, A1 to A7 | WORLD | both halves | B38-1 |
| `DB-b-79` | E3, FWD-11: Orion's gross TWR landed as silver at address() output, with as_of (W53-S1) | WORLD | DB-b-75 (drained) | B38-2 |
| `DB-b-80` | E2, FWD-11: the taxonomy keys and 48 header; the adapter reads them; the tie-out on both bases from the landed gross (W49-S3, W54-S1) | WORLD (served-data path floor) | DB-b-79 | B38-2 |
| `DB-b-81` | E4, FWD-11: the fee slices with COMPLETE/PARTIAL and denominators (W53-S2) | LOCAL | none | B38-3 |

**Carried, not cut:**
- the svc-custody-statement mint and CU-g-2a on `0.7.0_AE_CloudOps~DB2`, waiting on IB-pr-385 and release 6 being live;
- FWD-8's tolerance, at Andrew's word;
- CU-g-6, at Andrew's word (row 0347).

**fanout:** 3 of 3 chains, cap 8. Reason: the release, the Orion gross chain (DB-b-79 then DB-b-80), and the fee slices, with disjoint write
surfaces. Workers `0.9.0_WK_IRPT_DASHBD~55`, ~57 and ~58 are cut from box/dell2; ~56 is spawned on DB-b-79's drain.


## 41. ROUND 39, WORKSTREAM B (2026-10-09 ~08:5xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's round-38 ADDENDUM 7, on ADJUDICATION_v23 @ab9ad6b27a)

**Where round 38 left things.**
- Round 38 is closed.
- The R37 activity-and-lot release is LIVE (`ciTGx5UV`), verified A1 to A7 on 2026-10-07.
- W49-S3 is CLOSED (the taxonomy keys landed).

**The enrichment list:**
- **E1** (the 11:41Z fire's A1-A7; any SKIPPED line is a BLOCKING row that day) and **E2** (the fire's REPORT duration against 765 s) are the
  issuer's own reads at close, not cells. A worker cannot hold for the fire.
- **E3** is the one cell:

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-82` | E3, FWD-11: a readable billed/unbilled flag for Inflection's fee slices where a source exists (W53-S2) | LOCAL | none | B39-1 |

**Carried, not cut:**
- FWD-8's tolerance (Andrew's word);
- the three foreign-tax members (measured when a sample carries them);
- the svc-custody-statement mint and CU-g-2a on `~DB2` (they wait on IB-pr-385 and release 6 being live);
- CU-g-6 (Andrew's word, row 0347).

**fanout:** 1 of 1 chains, cap 8. Reason: one cell, and the round's other two items are the issuer's reads. Worker
`0.9.0_WK_IRPT_DASHBD~59`, cut from box/dell2.


## 42. ROUND 40, WORKSTREAM B (2026-10-09 ~09:0xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's round-39 ADDENDUM 8, ruling W53-S2)

**Where round 39 left things.**
- Round 39 is closed.
- The inferred billing flag (562 of 562) is ACCEPTED, on the condition that every consumer shows its basis; Orion's own flag wins where it is
  readable.

**The enrichment list:**
- **E1** (the 11:41Z fire's A1-A7 and REPORT duration against 765 s) is the issuer's read at close.
- **E2** is the one cell:

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-83` | E2, FWD-11: the fee slices with a per-account basis, measured where Orion reads and inferred elsewhere (W53-S2) | LOCAL | DB-b-82 (drained) | B40-1 |

**Carried:** FWD-8's tolerance; the foreign-tax members; the mint and CU-g-2a on `~DB2`; CU-g-6.

**fanout:** 1 of 1 chains, cap 8. Reason: one cell. Worker `0.9.0_WK_IRPT_DASHBD~60`, cut from box/dell2.


## 43. ROUND 41, WORKSTREAM B (2026-10-09 ~09:5xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ADDENDUM 9 and 9.1, msg 3011)

**Where round 40 left things.**
- Round 40 is closed.
- Both preconditions of the svc-custody-statement mint hold: IB-pr-385 is live in IB-pr-390 (07:49Z), and release 6b is live at tdpterTM
  (09:32Z).
- The CTO placed the mint and CU-g-2a (absorbed from IRPT_CUSTDY) in round 41.

**The enrichment list:**
- **E1** (the 11:41Z R37 fire's A1-A7 and REPORT against 765 s) is the issuer's read; a SKIPPED line or an over-line duration is a BLOCKING
  row.
- **E2 to E4** are cells:

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-84` | E2, FWD-12: the svc-custody-statement mint landing, by 0.7.0_AE_CloudOps~DB2 under the pair (COO @a319fc74b8, CTO msg 2440) | WORLD | the pair; IB-pr-385 and 6b live | B41-1 |
| `DB-b-85` | E3, FWD-12: the statement runner and its offline test (CU21-AC3) | LOCAL | none | B41-2 |
| `DB-b-86` | E4, FWD-12: the first real retained Performance client statement and the other-firm refusals, by ~DB2 | WORLD | DB-b-84, DB-b-85 | B41-1 |

**Supersession.** IRPT_CUSTDY TO-CU-g-2a is superseded by DB-b-85 and DB-b-86 (its AMENDMENT 1 named that recut).

**Carried:** FWD-8's tolerance; CU-g-6 (Andrew's word, row 0347).

**fanout:** 2 of 2 chains, cap 8. Reason: the AE seat's mint then apply, and the worker's offline build. Worker `0.9.0_WK_IRPT_DASHBD~61` is cut
from box/dell2; `0.7.0_AE_CloudOps~DB2` takes DB-b-84 now and DB-b-86 after both drains.


## 44. ROUND 42, LOT-KEY CHAIN (2026-10-09 ~12:0xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ADDENDUM 10, msg 3225)

**Where things stand.**
- The 11:41Z R37 fire logged LOTS_SKIPPED 2026-10-08 (row S40, BLOCKING).
- Returns and class landed. R37 stays live (Branch B, not rolled back).
- The CTO placed the lot-key cell FIRST in round 41.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-87` | E5, FWD-4: the 10-08 repeat pairs read, decided by the producer's rule, both kit days re-sized with the full lots stage | WORLD (served-producer path floor) | none | B41-3 |
| `DB-b-88` | E6, FWD-4: the R37 packet delta, the producer re-pinned and released, ONE 2026-10-08 lots backfill | WORLD | DB-b-87 (EXTEND_KEY) | B41-3 |

**Why round 42, not 41.** The issuance gate keys ONE issuance per round (round 41 already holds DB-b-84 to DB-b-86), and a second workstream needs its own lane. So the issuer re-points this chain to round 42 as its first and only cell set, which keeps the CTO's "first". Round 41's held items (the mint at leg R on the laptop ARN; DB-b-86 on ~P2's IB-pr-405) continue unchanged.

**fanout:** 1 of 1 chains (DB-b-87 then DB-b-88), cap 8. Workers `0.9.0_WK_IRPT_DASHBD~62` now, and ~63 on DB-b-87's drain.


## 45. ROUND 43, WORKSTREAM B (2026-10-09 ~12:2xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ADDENDUM 10.1, msg 3257)

**Where things stand.**
- IRPT_BCKEND's owned read IB-pr-405 (`persist_inputs`) is drained @2f6fe31ad8.
- The CTO placed the runner re-cut in its own round, since round 42 is already issued.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-89` | E1, FWD-12: the statement runner re-cut onto IB-pr-405; a fixture run with table access removed; 0 direct table clients | LOCAL | IB-pr-405 (drained) | B43-1 |

**DB-b-86 (round 41) is HELD** by its AMENDMENT 1 until three reads: IB-pr-405 LIVE (CodeSha256), the mint's leg R closed, and DB-b-89
drained.

**fanout:** 1 of 1 chains, cap 8. Worker `0.9.0_WK_IRPT_DASHBD~64`, cut from box/dell2.


## 46. ROUND 44, WORKSTREAM B (2026-10-09 ~12:5xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ADDENDUM 11, msg 3288; CVO ADJUDICATION_v25 @5f365678bf)

**Why these are new cells.** ADDENDUM 11's riders sit on cells that are already complete (DB-b-87, DB-b-89), so they are cut as new cells. Item 4 (S41,
the proof schema) went to the tooling owner via MSTR; there is no DASHBD cell for it.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-90` | E1, FWD-4: the realized-key uniqueness check on the FINAL rows, after every rewrite, with a rewrite-repeat test (W62-S1) | WORLD (served-producer floor) | DB-b-87 | B44-1 |
| `DB-b-91` | E2, FWD-4: a skipped lots day stated as "lots not computed for <date>: <reason>" in a status record the listing ignores (S40) | WORLD (served-handler floor) | none | B44-2 |
| `DB-b-92` | E3, FWD-12: verify-persisted checks the persisted object's sha256 (W64-S1) | LOCAL | DB-b-89 | B44-3 |

**Release.** DB-b-90 and DB-b-91 change served code. They reach the Lambda in a later R37 delta release, which the issuer asks the CTO to place
once they drain. DB-b-88 (in flight) releases DB-b-87's key and backfills 2026-10-08. W62-S1's emit_day duplicate check already refuses by name
meanwhile.

**fanout:** 3 of 3 chains, cap 8. Workers `0.9.0_WK_IRPT_DASHBD~65`, ~66 and ~67, cut from box/dell2.


## 47. ROUND 45, WORKSTREAM B (2026-10-09 ~13:3xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ADDENDUM 11.1, msg 3362, @43bbe32935)

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-93` | E1, FWD-12: the runner accepts the seat-authored selection file (derived id, or `selection_source: file`) | LOCAL | none | B45-1 |

**DB-b-86 (round 41)** is BLOCKED by its AMENDMENT 3 on the Cottonwood returns gold (ADVI_COTBKF, COTBKF ADDENDUM 11.2), DB-b-93, and the
laptop's hop3 file.

**fanout:** 1 of 1 chains, cap 8. Worker `0.9.0_WK_IRPT_DASHBD~68`, cut from box/dell2.


## 48. ROUND 46, WORKSTREAM B (2026-10-09 ~13:4xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ADDENDUM 12, msg 3371, @77e60c3d2b)

Rounds 42 and 44 are MAY-CLOSE (CVO ADJUDICATION_v26 @fbc76ab42d). The CTO ruled DB-b-90 and DB-b-91 release TOGETHER as ONE gold Lambda release
after `yIAQjspL`, under one pair (item 5).

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-94` | E1, FWD-4: the release packet -- the member census over live yIAQjspL (exactly DB-b-90's and DB-b-91's members), both branches, rollback, two UNSIGNED halves | WORLD | DB-b-90, DB-b-91 (drained) | B46-1 |

The apply is a later cell, after both halves are signed. DB-b-92 rides the runner (item 3); its sha256 limb stays dormant.

**fanout:** 1 of 1 chains, cap 8. Worker `0.9.0_WK_IRPT_DASHBD~69`, cut from box/dell2.


## 49. ROUND 47, WORKSTREAM B (2026-10-09 ~14:1xZ, issuer 2.0.0_SA_COO~D2, on the R44 CTO half @fa8d2c2961 and ADDENDUM 13.1, msg 3413)

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-95` | E1, FWD-4: apply the R44 release (DB-b-90 + DB-b-91, ONE gold Lambda release over yIAQjspL) under the signed pair | WORLD | DB-b-94, both halves | B47-1 |
| `DB-b-96` | E2, FWD-11: sources.json carries valuation_source / fee_treatment / price_basis; the returns manifest reads them, with an absent arm (W66-S1) | WORLD (served-producer floor) | none | B47-2 |
| `DB-b-97` | E3, FWD-4: the backfill path clears landed days from the lots status record (W69-S2) | WORLD (served-handler floor) | DB-b-91 | B47-3 |

**Isolation.** DB-b-95 builds at its own worktree base (handler blob `7c9bb9dcdc5b`) and does not merge box/dell2 before the build, so DB-b-97's
handler edit cannot ride the R44 release. DB-b-96 and DB-b-97 ship later under their own pairs. ADVI_COTBKF's CB-al-2 mint is held until DB-b-96
drains (ADDENDUM 13.1).

**fanout:** 3 of 3 chains, cap 8. Workers `0.9.0_WK_IRPT_DASHBD~70`, ~71 and ~72, cut from box/dell2.


## 50. ROUND 48, WORKSTREAM B (2026-10-09 ~14:2xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ADDENDUM 14, msg 3416)

Round 47 is already issued, so the CTO's FWD-8 cell is cut in its own round.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-98` | E1, FWD-8: classify the 510 UNEXPLAINED outside segments of TIEOUT_COMPOUND_V2 by a declared reason set (rule-24 record) or file defects; the counts sum to 990 | LOCAL | none | B48-1 |

The tolerance is Andrew's word (open call 2f53, REC 0.35pp); this cell runs regardless.

**fanout:** 1 of 1 chains, cap 8. Worker `0.9.0_WK_IRPT_DASHBD~73`, cut from box/dell2.


## 51. ROUND 49, WORKSTREAM B (2026-10-09 ~15:1xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ADDENDUM 15, msg 3492, and ADDENDUM 13.2, msg 3501)

Round 48 is MAY-CLOSE, and FWD-8 is NOT REALIZED: 197 DEFECT segments, and every reason is inferred.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-99` | E1, FWD-8: classifier threshold sensitivity, pre-registration, per-reason claim and robustness | LOCAL | DB-b-98 | B49-1 |
| `DB-b-100` | E2, FWD-8: the 74 W73-S1 DEFECT segments -- a producer fix with a test, or a Black Diamond-side two-sided read | WORLD (producer floor) | DB-b-98 | B49-2 |
| `DB-b-101` | E3, FWD-8: the 123 W73-S2 DEFECT segments -- the same | WORLD (producer floor) | DB-b-98 | B49-3 |
| `DB-b-102` | E4, FWD-11: method_version from the firm's sources entry, never a default 2 (ADVI_COTBKF's CB-al-2 waits on it) | WORLD (producer floor) | DB-b-96 | B49-4 |

**Shared write surface.** DB-b-100, DB-b-101 and DB-b-102 may each touch `account_return_daily.py`. They are cut in parallel and drained one at a
time, each re-graded after the last drain. A conflict is resolved at the drain, by the issuer, in the worker worktree. Producer fixes ship later
under their own pairs.

**fanout:** 4 of 4 chains, cap 8. Workers `0.9.0_WK_IRPT_DASHBD~74` to ~77, cut from box/dell2.


## 52. ROUND 50, WORKSTREAM B (2026-10-09 ~15:2xZ, issuer 2.0.0_SA_COO~D2, on the R44 CTO half AMENDMENT 1, msg 3550, @b758031ba2)

Round 49 is already issued, so the CTO's sizing ruling is cut in its own round.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-103` | E1, FWD-4: ONE dry-run backfill of 2026-10-08 on live oNgy4rnr; under 85% closes R44 ledger leg S1, over either rolls back to yIAQjspL | WORLD | DB-b-95 | B50-1 |

Monday 2026-10-12 07:41 ET stays the acceptance, kept as a row with that clock.

**fanout:** 1 of 1 chains, cap 8. Worker `0.9.0_WK_IRPT_DASHBD~78`, cut from box/dell2.


## 53. ROUND 51, WORKSTREAM B (2026-10-09 ~15:2xZ, issuer 2.0.0_SA_COO~D2, on laptop 4.0.0_SA_CRO's naming ruling, MSTR msg 3555)

Rule 30 conformance of DB-b-91's status key. It is inside the issuer's own decomposition, a repair of a drained cell.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-104` | E1, FWD-4: the lots status key is built by `address()`, never a typed suffix, with its bytes unchanged | WORLD (served-handler floor) | DB-b-97 | B51-1 |

It rides the next gold release with DB-b-97 (CTO ADDENDUM 16 item 1).

**fanout:** 1 of 1 chains, cap 8. Worker `0.9.0_WK_IRPT_DASHBD~79`, cut from box/dell2.


## 54. ROUND 52, WORKSTREAM B (2026-10-09 ~15:5xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ADDENDUM 16 item 1 and ADDENDUM 17, msg 3583)

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-105` | E1, FWD-4: the R45 release packet -- DB-b-97 + DB-b-104 over live oNgy4rnr, census = handler.py only, memory headroom stated, halves UNSIGNED | WORLD | DB-b-97, DB-b-104 | B52-1 |
| `DB-b-106` | E2, FWD-8: Black Diamond's own transaction / posting dates read against Opal's for the 475 FLOW_TIMING + INCOME_DATE segments | LOCAL | DB-b-99 | B52-2 |

FWD-8 stays NOT REALIZED until DB-b-106 drains and the DEFECT classes (DB-b-100, DB-b-101) are dispositioned.

**fanout:** 2 of 2 chains, cap 8. Workers `0.9.0_WK_IRPT_DASHBD~80` and ~81, cut from box/dell2.


## 55. ROUND 53, WORKSTREAM B (2026-10-09 ~16:0xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ADDENDUM 18, msg 3598)

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-107` | E1, FWD-4: ONE dry run on live oNgy4rnr on the heaviest lots day of the last 90 (denominator printed), read against the 85% lines | WORLD | DB-b-103 | B53-1 |

Over the line means a pair for a producer fix (preferred) or a memory change with its own before/after. Monday 07:41 ET stays the acceptance.

**fanout:** 1 of 1 chains, cap 8. Worker `0.9.0_WK_IRPT_DASHBD~82`, cut from box/dell2.


## 56. ROUND 54, WORKSTREAM B (2026-10-09 ~16:4xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's containment ruling @0e8209c33c, AMENDMENT 2)

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-108` | E1, FWD-8: the 14 code files carrying 49F account numbers -- literals to acct#<sha8> tokens, run-time ids from IRPT_PRIVATE_EVIDENCE_DIR | LOCAL | none | B54-1 |

The client-data rule binds every worker prompt from this issuance on: evidence with account ids or client figures is written OUTSIDE the repo.

**fanout:** 1 of 1 chains, cap 8. Worker `0.9.0_WK_IRPT_DASHBD~83`, cut from box/dell2.


## 57. ROUND 55, WORKSTREAM B (2026-10-09 ~17:0xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ADDENDUM 20 and ADDENDUM 19 item 2)

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-109` | E1, FWD-4: the memory-step packet -- setting only, 2048 up one step, before/after heaviest-day dry run; apply before Mon 07:41 ET | WORLD | DB-b-107 | B55-1 |
| `DB-b-110` | E2, FWD-4: per-stage peak memory on the kit day; cut the largest stage's peak, output byte-equal; ships in R45 | WORLD (producer floor) | DB-b-107 | B55-2 |
| `DB-b-111` | E3, FWD-8: the 990 outside segments re-graded on ONE restated convention, pre-registered; CONVENTION within 0.35pp | LOCAL | DB-b-99/100/101/106 | B55-3 |

The client-data rule binds every worker prompt: evidence with account ids or client figures stays outside the repo.

**fanout:** 3 of 3 chains, cap 8. Workers `0.9.0_WK_IRPT_DASHBD~84` to ~86, cut from box/dell2.


## 58. ROUND 56, WORKSTREAM B (2026-10-09 ~17:2xZ, issuer 2.0.0_SA_COO~D2, on the signed memory-step pair, CTO half msg 3789)

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-112` | E1, FWD-4: memory_size 2048 -> 3008 on the gold Lambda (setting only), then the 10-08 dry run under 3008 against 85%; over means 2048 again | WORLD | DB-b-109, both halves | B56-1 |

It lands before R45 (R45 CTO half, condition 2) and before Monday 07:41 ET.

**fanout:** 1 of 1 chains, cap 8. Worker `0.9.0_WK_IRPT_DASHBD~87`, cut from box/dell2.


## 59. ROUND 57, WORKSTREAM B (2026-10-11 ~03:1xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ruling msg 3940)

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-113` | E1, FWD-4: the R45 never-widen packet refreshed at the new source bytes -- census from each member's live pin, one kit day live-pinned vs HEAD with five hashes equal, halves UNSIGNED | WORLD | DB-b-105, DB-b-110 | B57-1 |

The R45 pair signed on the DB-b-105 packet is void for the apply. The apply itself is a later cell, after both halves re-sign and Monday's R44 acceptance (W78-S1).

**fanout:** 1 of 1 chains, cap 8. Worker `0.9.0_WK_IRPT_DASHBD~88`, cut from box/dell2.


## 60. ROUND 58, WORKSTREAM B (2026-10-11 ~03:5xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ADVI_COTBKF round-54 analysis @0ac41554df, row ADVI_COTBKF-D2-W66-S1)

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-114` | FWD-11: the rule-24 record (four postulates, word-boundary token census) deciding the return_basis and method_version values Cottonwood's positions-based returns state; lands no value (ADVI_COTBKF's re-stamp and CB-al-2 wait on it) | LOCAL | DB-b-102 | B58-1 |

A producer or contract edit, if the record calls for one, is a later cell cut after DB-b-113 drains: it would move an R45 member.

**fanout:** 1 of 1 chains, cap 8. Worker `0.9.0_WK_IRPT_DASHBD~89` (worker-light), cut from box/dell2.


## 61. ROUND 59, WORKSTREAM B (2026-10-11 ~04:2xZ, issuer 2.0.0_SA_COO~D2, on row IRPT_DASHBD-D2-W88-S3 under 1.0.0_SA_CTO~DELL2's msg 3999)

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-115` | FWD-11: the reporting-gold handler passes the declared source entry to every emit_day call, so the returns manifest states method row 2 and its three method fields, never absent; tested; no deploy | WORLD (producer floor) | DB-b-96, DB-b-102, DB-b-113 | B59-1 |

The refreshed R45 packet (DB-b-113) stays UNSIGNED: it is refreshed once more at the handler's new bytes after this cell drains.

**fanout:** 1 of 1 chains, cap 8. Worker `0.9.0_WK_IRPT_DASHBD~90` (worker-light), cut from box/dell2.


## 62. ROUND 60, WORKSTREAM B (2026-10-11 ~04:1xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ruling msg 4036, row IRPT_DASHBD-D2-W89-S1)

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-116` | FWD-11: one measurement -- every field of the written dim row 3 (income basis included) read against the Cottonwood adapter, verdict ROW3_TRUE or ROW3_FALSE; the dim row 3 partition read at the builder address with a positive control (ADVI_COTBKF's mint waits on it) | LOCAL | DB-b-114 | B60-1 |

True: the stamp is method_version 3. False: a new method row is proposed under rule 24 in a later cell.

**fanout:** 1 of 1 chains, cap 8. Worker `0.9.0_WK_IRPT_DASHBD~91` (worker-light), cut from box/dell2.


## 63. ROUND 61, WORKSTREAM B (2026-10-11 ~04:4xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's msgs 3940, 3999 and 4029)

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-117` | E1, FWD-4: the R45 never-widen packet, second refresh, at the bytes after the handler fix -- four members from their live pins, five output hashes equal on one kit day, every manifest compared field by field against the live one, halves UNSIGNED | WORLD | DB-b-113, DB-b-115 | B61-1 |

Both earlier R45 packets are superseded. The apply is a later cell, after both halves sign this packet and Monday's R44 acceptance (W78-S1).

**fanout:** 1 of 1 chains, cap 8. Worker `0.9.0_WK_IRPT_DASHBD~92`, cut from box/dell2.


## 64. ROUND 62, WORKSTREAM B (2026-10-11 ~04:4xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ruling msg 4060)

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-118` | FWD-11: the thresholds a method row states carry a per-value claim (measured / inferred / held / absent) in the producer's thresholds input and the dim_return_method row; rule-24 record first, then the change with tests; no S3 write (ADVI_COTBKF's Cottonwood row 3 waits on it) | WORLD (producer floor) | DB-b-116 | B62-1 |

It drains after DB-b-117: it moves an R45 member, and R45 is built from its pinned commits without this change.

**fanout:** 1 of 1 chains, cap 8. Worker `0.9.0_WK_IRPT_DASHBD~93`, cut from box/dell2.


## 65. ROUND 63, WORKSTREAM B (2026-10-11 ~05:1xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's R45 refresh 2 half, condition 1, msg 4126)

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-119` | E1, FWD-4: every reader of the returns manifest named with file and line, counted over scopes with their denominators, each graded on a key it does not know; a strict reader is a STOP before the R45 apply | LOCAL | DB-b-117 | B63-1 |

The R45 apply is a later cell: both halves are signed; it waits on this census and on Monday's R44 acceptance (W78-S1).

**fanout:** 1 of 1 chains, cap 8. Worker `0.9.0_WK_IRPT_DASHBD~94` (worker-light), cut from box/dell2.


## 66. ROUND 64, WORKSTREAM B (2026-10-11 ~05:2xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ruling msg 4143, row IRPT_DASHBD-D2-W93-S3)

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-120` | FWD-11: the dim_return_method contract lists method row 3; tieout_tolerance_proposed takes the same per-value claim as the five thresholds and lands typed; contract 0.5.0; rule-24 record first (one cell before ADVI_COTBKF's Cottonwood mint) | LOCAL | DB-b-118 | B64-1 |

**fanout:** 1 of 1 chains, cap 8. Worker `0.9.0_WK_IRPT_DASHBD~95`, cut from box/dell2.


## 67. ROUND 65, WORKSTREAM B (2026-10-11 ~08:1xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ruling msg 4459)

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-121` | FWD-11: one read-only cell before any build -- what the reporting read needs per firm and whether Cottonwood has it; whether the page's year-to-date needs the reporting summary once performance answers; what DB-b-86's hop3 reads of the Cottonwood returns gold | LOCAL | none | B65-1 |

The build's shape (one reporting-read function per firm, or one map) is the CTO's ruling on this cell's two lines. DB-b-86 stays BLOCKED on its
hop3 file; the Cottonwood returns gold it waited on was minted by ADVI_COTBKF on 2026-10-11.

**fanout:** 1 of 1 chains, cap 8. Worker `0.9.0_WK_IRPT_DASHBD~96`, cut from box/dell2.


## 68. ROUND 66, WORKSTREAM B (2026-10-11 ~10:0xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ruling msg 4634)

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-122` | FWD-11: method row 3 states income ABSENT by design with its reason (the positions-based method does not separate income); row 2 unchanged and a test shows it; contract 0.6.0; rule-24 record first; the never-widen packet for rewriting the one served object (Cottonwood dim_return_method, method_version=3) -- no S3 write in this cell | LOCAL | DB-b-120 | B66-1 |

The rewrite of the served object is a LATER act under a signed pair (COO half and CTO half on the packet this cell writes), verified by
2.0.0_SA_COO~C2's read-back; it is not cut here. The R45 gold release is built from its four source-map PINS, so this cell's change to the
producer on trunk does not move that release or its signed packet. FWD-11 for the reporting read stays parked
(`deliverables/2.0.0_SA_COO~D2/FWD11_REPORTING_READ_PARKED_20261011.md`).

**fanout:** 1 of 1 chains, cap 8. Worker `0.9.0_WK_IRPT_DASHBD~97`, cut from box/dell2.


## 69. ROUND 67, WORKSTREAM B (2026-10-11 ~10:3xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2 msg 4723 and the signed pair)

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-123` | FWD-11: the APPLY of DB-b-122's packet -- one overwrite of exactly two keys (Cottonwood dim_return_method, method_version=3) so the served method row states income ABSENT; ledger first, capture first (it is the rollback), the ETags as listed or the act stops, column diff before and after, the mint's verify, ledger closed | SERVED | DB-b-122; CTO half @59da96c840; COO half @2995b0bff4 | B67-1 |

The pair covers the two Cottonwood keys and nothing else (CTO half condition 5): no run of the producer for any other firm. The two new
columns reach 49 Financial's served method row 2 only through a later release of the gold producer under its own pair, which names those
columns and their readers; that is NOT the R45 release already signed (built from its four pins) and is not cut here.
2.0.0_SA_COO~C2 reads the object back after the drain.

**fanout:** 1 of 1 chains, cap 8. Worker `0.9.0_WK_IRPT_DASHBD~98`, cut from box/dell2.


## 70. ROUND 68, WORKSTREAM B (2026-10-11 ~13:5xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ROUND-68 ANALYSIS @0005d9fd9a)

The analysis answers the L10 slug for rounds 55 to 67 (REMEDIATION_v27 @806d057711), which had been held behind one blocked order
(DB-b-86, superseded @34e0d00eff). Its ENRICHMENT LIST, section 4, one cell per item:

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-124` | list item 1: the present state of the nine rows compiled before today, each closed with its evidence or confirmed open; the two ARMED rows with their disarm (read-only) | LOCAL | none; FIRST and ALONE | A |
| `DB-b-125` | list item 2: the thresholds file carries a claim per threshold, is tracked at the handler's path, and is hashed against the served copy (row W85-S1 and a new row) | WORLD (the gate's floor: the grant names a path under infra/aws/lambda; nothing is deployed) | DB-b-124 | B |
| `DB-b-126` | list item 3: R45 presented again on current bytes with its sources.json named; DB-b-115's manifest fields read; what the release changes for 49 Financial's method row named for a new pair (rows W88-S1, W88-S3) | LOCAL | DB-b-124 | C |
| `DB-b-127` | list item 4: the Cottonwood adapter's two stale statements; method row 3 read for a sentence false for Cottonwood; one counts-only read of the account-id join (rows W89-S1, W96-S3) | LOCAL | DB-b-124 | D, first |
| `DB-b-128` | list item 5: the income reason reworded for the method, with its small packet (row D2-S13) | LOCAL | DB-b-127 (the same producer file) | D, second |
| `DB-b-129` | list item 6: the 244 UNEXPLAINED tie-out segments classed by cause, the remainder printed (row W86-S2) | LOCAL | DB-b-124 | E |

**No served write in the round** (DB-b-125 is classed WORLD by the gate's path floor and writes nothing served). DB-b-126 and DB-b-128 each end in a packet; each apply is a later act under a newly signed pair, and
(row W87-S1, analysis section 3) names an applier the gates admit, not a worker. The R45 apply still waits on Monday 2026-10-12 07:41 ET's
R44 acceptance fire as well as on the new pair.

**Parked, by the analysis's section 2 item 1:** the Cottonwood half of FWD-11 un-parks when IRPT_BCKEND's holdings gold has minted one
Cottonwood partition; the superseded cell DB-b-86 is re-cut then (carrier: `deliverables/2.0.0_SA_COO~D2/FWD11_REPORTING_READ_PARKED_20261011.md`).
The Inflection half and FWD-12 (49 Financial) do not wait on it and are not in this round's list.

**Rule 24:** the records' words (CLOSED_BY_EVIDENCE / STILL_OPEN / NOT_ESTABLISHED; READ / RUN) are measurement vocabularies local to these
cells. DB-b-125's claims use the producer's existing THRESHOLD_CLAIMS vocabulary and mint no value. DB-b-128 carries its own four-postulate
record before it changes a served word.

**fanout:** 1 of 5 chains now (A), then up to 3 at a time, cap 8. Workers `0.9.0_WK_IRPT_DASHBD~99` to `~104`, each cut from box/dell2.

## 71. ROUND 69, WORKSTREAM B (2026-10-11 ~16:0xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2 msg 5263 and the signed pair)

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-130` | FWD-11: the APPLY of DB-b-128's packet (sha256 6fbce1ff...d064) -- one overwrite of exactly two keys (Cottonwood dim_return_method, method_version=3) so the served income reason is worded for the method; ledger first, capture first (the captured version ids are the rollback), the ETags as listed or the act stops, column diff before and after, the mint's verify, ledger closed | SERVED | DB-b-128; COO half @34cc62f4f7; CTO half @34a6a32212 | B69-1 |

The applier is `0.7.0_AE_CloudOps~CB2`, named by the CTO (msg 5263), and not a worker (row IRPT_DASHBD-D2-W87-S1). The pair covers the two
Cottonwood keys and nothing else. A denied put is the stop branch: no role is widened, the CTO names another applier.
2.0.0_SA_COO~C2 reads the object back after the act.

**fanout:** 1 of 1 chains, cap 8. Seat `0.7.0_AE_CloudOps~CB2`, on box/dell2 at or after 780ba55bde.

## 72. ROUND 70, WORKSTREAM B (2026-10-11 ~16:3xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ROUND-69 ANALYSIS @90cb3e774b)

The analysis is titled ROUND 69; this issuance is numbered 70 because round 69 is the one apply order cut on the CTO's msg 5263 minutes
before the analysis arrived. Its ENRICHMENT LIST (section 4) is the rectangle, one cell per item.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-131` | FWD-11: item 1 -- the thresholds file inside the LIVE function's package read by content, and ONE recent 49 Financial daily returns manifest: top-level key names and the count of long digit runs, no value kept; the five values compared with the tracked file (rows W100-S3, W100-S2) | LOCAL | none | B70-1 |
| `DB-b-132` | FWD-11: item 2 -- both manifest writers serve the five thresholds and their claims only, through one function (row W100-S3) | LOCAL | none to start; DRAIN after DB-b-130 | B70-2 |
| `DB-b-134` | FWD-11: item 4 -- `method_version_of` refuses an entry naming a positions-based row with no declared valuation source (row W103-S1) | LOCAL | DB-b-132 (same file, same worktree) | B70-2 |
| `DB-b-133` | FWD-11: item 3 -- the contract's two prose lines worded for the method; the tracked Cottonwood build manifest's stale text corrected or its lane refusal recorded (rows W103-S2, W102-S1) | LOCAL | none to start; DRAIN after DB-b-130 | B70-3 |
| `DB-b-135` | FWD-12: item 5 -- the custodian's two-sided dollar read for the 90 unclassed tie-out segments, classed by cause, counts only (row W104-S1) | LOCAL | DB-b-129 (drained) | B70-4 |

No served object is rewritten in this round (analysis section 2 item 3): removing a prior version is a delete and Andrew's act, asked only
with DB-b-131's count in hand. No producer upload of method row 2 before DB-b-132 lands. FWD-11's Cottonwood half and FWD-12 stay parked
(`deliverables/2.0.0_SA_COO~D2/FWD11_REPORTING_READ_PARKED_20261011.md`).

**fanout:** 4 of 4 chains, cap 8. Workers `0.9.0_WK_IRPT_DASHBD~105` (DB-b-131), `~106` (DB-b-132 then DB-b-134, one worktree), `~107`
(DB-b-133), `~108` (DB-b-135), each cut from box/dell2.

## 73. ROUND 71, WORKSTREAM B (2026-10-11 ~16:5xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ruling msg 5375)

DB-b-131 found the 24-key thresholds object in the live package and in a daily returns manifest. The CTO ruled three things on it; each is
a cell (its items 1 and 2 are one read).

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-136` | FWD-11: items 1 and 2 -- the 49 Financial manifests the live package writes, counted per prefix by key listing (no bodies) with first and last dates; and each of the ten readers of a returns manifest read for whether it passes the thresholds object or the whole manifest onward | LOCAL | DB-b-131 | B71-1 |
| `DB-b-137` | FWD-11: item 3 -- R45 presented once more as REFRESH 4 with today's producer (DB-b-128, DB-b-132, DB-b-134), so the first run after it stops writing the 24 keys; a packet, no apply; REFRESH 3's halves stand until REFRESH 4's are signed | LOCAL | DB-b-132, DB-b-134 | B71-2 |

No served object is rewritten or deleted. With DB-b-136's two answers the CTO takes the question to Andrew.

**fanout:** 2 of 2 chains, cap 8. Workers `0.9.0_WK_IRPT_DASHBD~109` (DB-b-136) and `~110` (DB-b-137), each cut from box/dell2.

## 74. ROUND 72, WORKSTREAM B (2026-10-11 ~17:1xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ROUND-71 ANALYSIS @a15e967740)

The analysis lists three cells. Its items 1 and 2 are the CTO's msg 5375, already issued as round 71 (DB-b-136, DB-b-137, section 73)
and running; the analysis says that message "stands as its first two". Item 3 is new and is this round's one cell.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-138` | FWD-12: item 3 -- the tie-out's flow-timing class (51 segments, closing under START for 50 and MID for 48) contradicts round 68's refutation of FLOW_TIMING: shown as CONTESTED, each read against the custodian's own transaction rows and placed in an outcome with a rule; the tie-out's state summed to 244 and not called closed (row W108-S2) | LOCAL | DB-b-135 | B72-1 |

The issuer reads the analysis's "two results" as the START and MID results of that one class (51 segments); the 31 accrual-class
segments contradict no refutation. The COO half on REFRESH 4 (the analysis's item 2) is this seat's own act when DB-b-137 drains.

**fanout:** 1 of 1 chains, cap 8. Worker `0.9.0_WK_IRPT_DASHBD~111`, cut from box/dell2.

## 75. ROUND 73, WORKSTREAM B (2026-10-11 ~18:0xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2 msg 5496)

Both halves on R45 REFRESH 4 are signed (COO @598347202e, CTO @e969a090cc) with the pinned 24-key thresholds file still in the package.
The CTO's half asks one cell of "your next issuance".

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-139` | FWD-11: the thresholds file inside the function's package becomes a file of the five values and their claims -- the kit run on that file compared with REFRESH 4's run, and the packet for the swap as its own release AFTER REFRESH 4's apply; no apply (rows W100-S2, W100-S3) | LOCAL | DB-b-137 | B73-1 |

Also from the CTO's half, not a cell: one after-read is added to REFRESH 4's apply (the first manifest written after the release is read
for six key names and no long digit run); it rides the apply order when that is cut, after Monday's fire.

**fanout:** 1 of 1 chains, cap 8. Worker `0.9.0_WK_IRPT_DASHBD~112`, cut from box/dell2.

## 76. ROUND 74, WORKSTREAM B (2026-10-11 ~18:5xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ROUND-74 ANALYSIS @d8b69fa413)

The analysis answers REMEDIATION_v30 @dbf7c2e292 for rounds 71 to 73 and lists ONE cell.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-140` | FWD-12: the 18 segments (a subset of the 51 contested) where the custodian's flow rows do not reproduce the served flow day by day, on 50 flow days: each read day by day and placed under a cause with a rule, or under no cause with why; the tie-out's state restated and not called closed (row W111-S1) | LOCAL | DB-b-138 | B74-1 |

After it the project's next acts are two applies, in order: R45 REFRESH 4 (both halves signed; waits for Monday 2026-10-12 07:41 ET's
fire and an AE applier, with the CTO's added after-read of the first manifest), then the thresholds-file swap (its pair is signed only
after REFRESH 4's first fire is read, CTO msg 5589).

**fanout:** 1 of 1 chains, cap 8. Worker `0.9.0_WK_IRPT_DASHBD~113`, cut from box/dell2.

## 77. ROUND 75, WORKSTREAM B (2026-10-11 ~19:5xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ROUND-75 ANALYSIS @06b01d9b88)

The analysis answers REMEDIATION_v31 @ac4a24a07d: row D2-W111-S1 does not close on one worker's read. Three items.

**Item 1 is the issuer's own act and carries no order:** five of the 50 differing days, chosen by this seat across 5 of the 18
segments, both sides read fresh from S3: each transaction id counted once reproduces the served day flow to the cent on 5 of 5; the
naive sum on 0 of 5 (`deliverables/2.0.0_SA_COO~D2/RERUN_FIVE_DAYS_ROW_W111_S1.md`). By the analysis's rule that closes row D2-W111-S1.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-141` | item 2: every reader in the repo of the Black Diamond transactions copy, each read for whether it sums amounts and whether it keys on the transaction id, with what it serves; nothing corrected (row W113-S2) | LOCAL | DB-b-140 | B75-1 |
| `DB-b-142` | item 3: the ledger comparison re-read at the cent over all 51 contested segments with each id counted once; the one fee row classed by the method's own rule for a flow, cited from the code (row W113-S3) | LOCAL | DB-b-140 | B75-2 |

**fanout:** 2 of 2 chains, cap 8. Workers `0.9.0_WK_IRPT_DASHBD~114` (DB-b-141) and `~115` (DB-b-142), each cut from box/dell2.

## 78. ROUND 76, WORKSTREAM B (2026-10-11 ~20:1xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ruling msg 5721)

Round 75 is drained @fc42bbcab0 (round-close MAY-CLOSE). The CTO ruled one read-only cell on the ORIGINAL store and one re-derivation.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-143` | the ORIGINAL Black Diamond transactions store's shape on one day, counts only (once per id, or once per id and portfolio group); only if it repeats, every reader of it in the workspace, portal, opal_ai and mcportal, denominator per tree, each classed as keyed on the id or not with what it serves and its owner; nothing corrected (rows W113-S2, W114-S1) | LOCAL | DB-b-141 | B76-1 |
| `DB-b-144` | "59 of 90 tie, 31 do not" re-derived with each transaction id counted once, beside the naive count, before that number is shown again (row W114-S1) | LOCAL | DB-b-142 | B76-2 |

A reader that sums without the id and SERVES something goes to the CTO as one row naming its owner; correcting it is its owner's.

**fanout:** 2 of 2 chains, cap 8. Workers `0.9.0_WK_IRPT_DASHBD~116` (DB-b-143) and `~117` (DB-b-144), each cut from box/dell2.

## 79. ROUND 77, WORKSTREAM B (2026-10-11 ~20:4xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ROUND-76 ANALYSIS @d70feb6d15)

The analysis answers REMEDIATION_v32 @305103f259 with four items. Its item 2 and the first half of item 1 were already issued as round
76 on the CTO's msg 5721 (DB-b-143 running; DB-b-144 drained: 59 of 90 becomes 89 of 90 with each id counted once). The rest:

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-145` | item 1, second half: the scripts behind the figures the tie-out records quote are tracked in the project's folder with their hashes, or the figure is listed as withdrawn; no client data enters the tree (row W114-S1) | LOCAL | DB-b-144 | B77-1 |
| `DB-b-146` | item 3: the shared code table's class for the one "Other Fee" row beside the method's rule; agreement closes row W113-S3, disagreement is a row against the table (rows W113-S3, W115-S1) | LOCAL | DB-b-142 | B77-2 |
| `DB-b-147` | item 4: what CONTESTED still means for the 51 now that their flows reproduce, grouped, with what would close each; a proposal, not a ruling; the tie-out not closed | LOCAL | DB-b-142, DB-b-144 | B77-3 |

The issuer tracks its own re-run script itself (`deliverables/2.0.0_SA_COO~D2/rerun_five_days.py`, in this issuance's commit).

**fanout:** 3 of 3 chains, cap 8. Workers `0.9.0_WK_IRPT_DASHBD~118`, `~119`, `~120`, each cut from box/dell2.

## 80. ROUND 78, WORKSTREAM B (2026-10-11 ~21:1xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2 rulings msg 5835 and msg 5827)

Round 77 is drained @f09dfcb6d9 (round-close MAY-CLOSE). Two rulings, three cells.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-148` | FWD-12: msg 5835 -- the tie-out's class set as two questions (does the segment reconcile; which timing did the other system use, classed only where exactly one timing closes, otherwise not determined), returned as a Rule 24 proposal: four postulates, a word-boundary census of each new token, the 51 placed by subtraction, and for the 3 whether any timing closes | LOCAL | DB-b-147 | B78-1 |
| `DB-b-149` | msg 5827 -- the two price paths that take a median over un-deduplicated rows and serve a price: what each serves and to whom, and whether the median moves on one day with each transaction id counted once; counts only, no price written | LOCAL | DB-b-143 | B78-2 |
| `DB-b-150` | msg 5827 -- the ids repeating INSIDE one portfolio group in the original store (590 on 2026-10-06): counts by cause on the non-money, non-account columns, or stated unexplained; whether a dedupe on the id alone drops a real row | LOCAL | DB-b-143 | B78-3 |

DB-b-148 is a PROPOSAL: no class is applied in any record until the CTO rules on it.

**fanout:** 3 of 3 chains, cap 8. Workers `0.9.0_WK_IRPT_DASHBD~121`, `~122`, `~123`, each cut from box/dell2.

## 81. ROUND 79, WORKSTREAM B (2026-10-11 ~21:3xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ROUND-78 ANALYSIS @0ffc0f24e6)

The analysis answers REMEDIATION_v33 @7c237a67ec with a five-item list. Items 2 and 5 were issued as round 78 on the CTO's msgs 5827
and 5835 (DB-b-149, DB-b-150, DB-b-148, running). **Item 1 is the issuer's own act and carries no order**
(`deliverables/2.0.0_SA_COO~D2/ISSUER_RUNS_ROUND78_ITEM1.md`: the tracked recount script run once by this seat reads 89 of 90, which by
the analysis's rule closes row D2-W114-S1; five of the 33 readers re-read by this seat, five agree). The rest:

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-151` | item 3: the copy against the original on the three sampled days, metadata and row counts only; whether the original was rewritten after the copy was taken; and all 42 figures named with the store each was read from (row W116-S2) | LOCAL | DB-b-143, DB-b-145 | B79-1 |
| `DB-b-152` | item 4: the two withdrawn figures marked withdrawn in the 244 record, by the serial that owns it (row W118-S1) | LOCAL | DB-b-145 | B79-2 |
| `DB-b-153` | item 4: the one withdrawn figure marked withdrawn in the 18 record, by the serial that owns it (row W118-S1) | LOCAL | DB-b-145 | B79-3 |

**fanout:** 3 of 3 chains, cap 8. Workers `0.9.0_WK_IRPT_DASHBD~124` (DB-b-151), and the record-owning serials `~104` (DB-b-152) and
`~113` (DB-b-153), each in a fresh worktree cut from box/dell2.

## 82. ROUND 80, WORKSTREAM B (2026-10-11 ~21:5xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2 msgs 5878 and 5886)

Rounds 78 and 79 are fully drained (round-close MAY-CLOSE on both). Two rulings came back on what they returned:

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-154` | msg 5878: the severity of row W122-S1 -- of the 34 moved medians, how many are the final served price, how many of those assets are held on a served account-day, the two over 1 percent by the same test, and whether the script path runs today. Read-only, counts only; the pipeline is dell1's (its row ADVI_FIRMBKTS-D1-S32, parked) and the read is sent to its CTO through 0.0.0_AB_MSTR~DELL2 | LOCAL | DB-b-149 | B80-1 |
| `DB-b-155` | msg 5886: the proposal's first axis renamed for what it measures (a restatement closing, since END is served and closes in 0 of 51); two tokens with their census, none containing RECONCILES; by the serial that owns the record | LOCAL | DB-b-148 | B80-2 |

**fanout:** 2 of 2 chains, cap 8. Workers `0.9.0_WK_IRPT_DASHBD~125` (DB-b-154) and the record-owning serial `~121` (DB-b-155), each in a
fresh worktree cut from box/dell2.

## 83. ROUND 81, WORKSTREAM B (2026-10-11 ~22:0xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2 msg 5937)

Row D2-W124-S1 (round 79: the original store rewritten after the copy; two sampled days now hold 0 rows) was carried to the store's
owner the same hour. 1.0.0_SA_CTO~DELL1 measured no id lost (5,580 of 5,580 present, re-attributed to other days) and named the open
half as this project's. Round 80 (DB-b-154, DB-b-155) is running; this ruling arrived after its issuance, so it is cut as its own round.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-156` | msg 5937: does any reader the tie-out or the served dashboard uses key on the file's day and not the transaction's own date; for the two sampled days, the ids' own dates against the files they now sit in. Read-only, counts only. The row closes on it | LOCAL | DB-b-151 | B81-1 |

**fanout:** 1 of 1 chain, cap 8. Worker `0.9.0_WK_IRPT_DASHBD~126`, in a fresh worktree cut from box/dell2.

## 84. ROUND 82, WORKSTREAM B (2026-10-11 ~22:2xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2 msg 5955)

The CTO accepted the renamed first axis and its two tokens and, on row D2-W121-S4, removed TIMING_END (a value that cannot occur).

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-157` | msg 5955: the proposal record carries the class set as ruled -- TIMING holds three values, the three retired tokens are listed together, the ruling is recorded; by the serial that owns the record | LOCAL | DB-b-155 | B82-1 |

**fanout:** 1 of 1 chain, cap 8. Worker `0.9.0_WK_IRPT_DASHBD~121` (worker-light), in a fresh worktree cut from box/dell2.

## 85. ROUND 83, WORKSTREAM B (2026-10-11 ~22:4xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ROUND-83 ANALYSIS @3f7c91e682)

Rounds 78 to 82 are terminal and MAY-CLOSE. The analysis: END, the served flow convention, closes in 0 of 51; START 50, MID 48, both
47. END is refuted as the other system's convention; between START and MID the data does not decide; matching the other system is not
a proof of accuracy. Its section 3 lists what the CTO needs before it writes the addendum. All read-only; counts and bands only. The
served convention stays END.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-158` | item 1: the accounts and flow-bearing days behind the 51, printed (ruling 24's bar) | LOCAL | DB-b-157 | B83-1 |
| `DB-b-159` | item 2: the size of a change both ways, per account-day and per served window, on a private copy; END reproduced first as the control | LOCAL | none | B83-2 |
| `DB-b-160` | item 3: how the guard's two flags move under START and MID, and the fallback days that move with them | LOCAL | DB-b-159 (its private table) | B83-2 |
| `DB-b-161` | item 4: what the custodian and Black Diamond publish about when a flow arrives, quoted with source and time; public reads only | LOCAL | none | B83-3 |

Item 5 (the 39 that close under no timing: 31 accrual-class, 8 unclassed) is not a cell: it is a required member of every record of
this round, checked by each criterion, so no number is quoted without it.

**fanout:** 3 of 3 chains, cap 8. Workers `0.9.0_WK_IRPT_DASHBD~127` (DB-b-158), `~128` (DB-b-159), `~130` (DB-b-161) now; `~129`
(DB-b-160) when DB-b-159 has drained.

## 86. ROUND 84, WORKSTREAM B (2026-10-11 ~23:3xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2 msg 6130)

Round 83 is terminal and MAY-CLOSE; its answer is PRD v0.10 and v0.11 (no flow-timing winner; END kept by default). One cell follows
from the reviewer's second note, a read and not a ruling.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-162` | msg 6130: on the 234 flow-bearing days, a count by when the deposited cash was first invested (same day, next trading day, later, never in the window), under a rule written and committed before the count, on a copy. Picks no convention | LOCAL | DB-b-158 | B84-1 |

**fanout:** 1 of 1 chain, cap 8. Worker `0.9.0_WK_IRPT_DASHBD~131`, in a fresh worktree cut from box/dell2.

## 87. ROUND 85, WORKSTREAM B (2026-10-11 ~23:5xZ, issuer 2.0.0_SA_COO~D2, the issuer's own cell)

Round 84 is terminal and MAY-CLOSE. Its worker left the counting scripts private because the tracked copies failed the lint gate, so
the five counts have no tracked producer; by the CTO's round-77 rule (row D2-W118-S1) such a figure is not quotable. Ruled by the
issuer inside its own decomposition: one cell closes it.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-163` | the scripts behind FLOW_DAYS_FIRST_INVESTED.json tracked, gate-clean by formal edits only, and re-run from the tracked copies to reproduce the counts; the rule and the record unchanged | LOCAL | DB-b-162 | B85-1 |

**fanout:** 1 of 1 chain, cap 8. Worker `0.9.0_WK_IRPT_DASHBD~131` (worker-light), the serial that owns the folder.

## 88. ROUND 86, WORKSTREAM B (2026-10-12 ~13:3xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ROUND-86 ANALYSIS @976ca0db4d section 3)

Rounds 84 and 85 are terminal and MAY-CLOSE. The analysis cuts nothing and fixes this project's next act: R45 REFRESH 4's apply, under
its signed pair (COO half @598347202e, CTO half @e969a090cc), after Monday's scheduled fire. That fire ran at 11:41Z 2026-10-12 on
oNgy4rnr: 318.1 s of the 765 s line, 1,607 MB of the 2,556.8 MB line (CloudWatch REPORT, read by the issuer; row D2-W78-S1's acceptance
read, PASS). The pair's condition 3 is met. The apply is the issuer's cell, ruled inside its own decomposition; its applier is the
dell2 cloud-ops seat (the pair's condition 6).

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-164` | the pair's apply: the gold Lambda release over live oNgy4rnr from the packet's four pins, ledger first, one targeted safe-apply, one dry-run invoke read against the 85 percent lines | WORLD | both halves SIGNED; the Monday acceptance fire read | R86-1 |

**fanout:** 1 of 1 chain, cap 8. No worker: the order goes to `0.7.0_AE_CloudOps~IB2` (first sent to `~DELL2`, unread; reseated 2026-10-12).

## 89. ROUND 87, WORKSTREAM B (2026-10-13 ~12:3xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ROUND-87 ANALYSIS @f55d3aa598 section 3 and msg 6897)

R45 REFRESH 4 was applied 2026-10-12 13:58:42Z (DB-b-164, live i2r7CbVr) and its first scheduled fire (2026-10-13 11:41Z) was read CLEAN by the issuer at 12:14Z
(`l5_read.py` b19ea40d71; REPORT 216.7 s of 765 s, 1,385 MB of 2,556.8 MB, 0 errors, the three added keys, six thresholds keys, `method_version` 2); ledger
`irpt-dashbd-r45-refresh4-20261012` closed @db605d794c. That is round-87 item 1. Item 2, the thresholds-file swap's pair, is signed: packet
`0.9.0_WK_IRPT_DASHBD~112/NEVER_WIDEN_PACKET_GOLD_PACKAGE_THRESHOLDS_FILE.md` sha256 `2ed4e840ef56...`, COO half @7c9ad9d0f0, CTO half @c5e183273f (the CTO's
msg 6900: name the AE applier in the order; the scheduled-site read closes the ledger). The apply is the issuer's cell, ruled inside its own decomposition; its applier is the dell2
cloud-ops seat `0.7.0_AE_CloudOps~IB2` (the pair's condition 6; it applied REFRESH 4).

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-165` | the pair's apply: the gold Lambda release over live i2r7CbVr with ONE staged file re-pinned (the thresholds file, 24-key blob to the tracked six-key file), ledger first, one targeted safe-apply, one dry-run invoke read against the 85 percent lines | WORLD | both halves SIGNED; REFRESH 4's first fire read (met) |

**fanout:** 1 of 1 chain, cap 8. No worker: the order goes to `0.7.0_AE_CloudOps~IB2`. The first-fire read after THIS release (the pair's condition 4) is the issuer's open ledger leg.

## 90. ROUND 88, WORKSTREAM B (2026-10-13 ~13:3xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ROUND-88 ANALYSIS @e53edd32d7 section 4 and msg 6931)

Round 87 is terminal and MAY-CLOSE; the CTO's after-read of the swap is PASS @bc4c810b8f. Black Diamond's published flow timing is read (`BD_FLOW_TIMING_HELP_READ_20261013.md`
@e2274fcdd4): additions at the start of the day, withdrawals and no-addition days at the end; the alternative, on request, is all flows at the end. The analysis fixes two items.

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| 1. ledger leg L7: the first scheduled fire after the swap (2026-10-14 11:41Z), read with `l5b_read.py`; close `irpt-dashbd-thresholds-swap-20261013` or restore rollback `8ELUDq...` the same session | the issuer's own act, no cell | FWD-8 (the thresholds the page reads) | the 11:41Z fire | none |
| 2. the tie-out decided by computing both flow conventions over the stored tie-out set, graded at 0.35 pp, with the reader's known 50 of 51 (START) and 0 of 51 (END) as controls | `DB-b-166` | FWD-8 / C-FLOWTIME | the stored per-segment tables of `~108` (read, never edited) | R88-1 |

`DB-b-166` is a read, LOCAL: zero vendor calls and zero secret reads (the stored responses already hold Black Diamond's figures; a window the stored set cannot decide is a surprise row, and
the issuer decides about any new vendor read), no served byte moves. The decision rule is written in the criterion before the count: `BD_DEFAULT` iff only the vendor-default convention ties
some flow segment the all-end one misses and the reverse never happens; `END` the mirror; `BOTH_TIE_INDISTINGUISHABLE` iff no segment tells them apart; `MIXED_NEITHER_DECIDES` iff each misses a
segment the other hits. The last two are not a FAIL of the cell; they are a surprise row and a wider window. The negative arm is the convention not chosen missing at least one flow segment.

**fanout:** 1 of 1 chain, cap 8. Worker `0.9.0_WK_IRPT_DASHBD~132` (worker), a new slot.

## 91. ROUND 89, WORKSTREAM B (2026-10-13 ~14:0xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ROUND-89 ANALYSIS @8208cabf27 section 4 and msg 6956)

Round 88 is terminal (MAY-CLOSE; the CVO's ADJUDICATION_v52 @50d8780e32 dismissed the one row). The PRD addendum v0.12 decision 11a reads the tie-out under `BD_DEFAULT`; the 12 segments neither
convention closes still owe a stated reason (FWD-8's ACCEPT). The analysis fixes three items.

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| 1. ledger leg L7, carried: the 2026-10-14 11:41Z fire, read with `l5b_read.py`; close `irpt-dashbd-thresholds-swap-20261013` or restore rollback `8ELUDq...` the same session | the issuer's own act, no cell | FWD-8 (the thresholds the page reads) | the 11:41Z fire | none |
| 2. a stated reason for each of the 12, from a closed list written before the read, each reasoned segment recomputed with its cause corrected and closing within 0.35 pp | `DB-b-167` | FWD-8 | `~132`'s tracked module and the stored tables of `~108` (read, never edited) | R89-1 |
| 3. the FWD-8 grade read, per account and window, by the issuer in its drain-end, citing the cells that already proved the label and guard clauses | the issuer's own act, no cell | FWD-8 | cell `DB-b-167` drained | R89-1 |

`DB-b-167` is a read, LOCAL: zero vendor calls and zero secret reads, no served byte moves. **The closed list, in the order a segment is tested (the first reason whose single correction re-closes the
segment at 0.35 pp takes it): `MISSING_PRICE`, `FLOW_ABSENT_ONE_SIDE`, `FLOW_ON_NON_TRADING_DAY`, `INCOME_OFF_FLOW_DAY`, `BD_ACCRUED_INCOME`, `UNEXPLAINED`.** The first four are the analysis's list. `BD_ACCRUED_INCOME`
is the issuer's one addition, inside its own decomposition: the issuer's design read (counts only) found that 5 of the 12 sit in the earlier ruled class of that name (worker ~108's accrual identity,
`UNCLASSED_90.json`) and the other 7 are in that record's remainder; leaving the cause off the list would call five segments UNEXPLAINED that the record already explains. A reason is shown by a count or by
day offsets from the stored rows, never asserted; a segment whose single correction does not close it is not given that reason (it stays `UNEXPLAINED`; a segment closed only by two corrections together is
reported as `combined_only`, still `UNEXPLAINED`). `UNEXPLAINED` above zero is counted per account, makes FWD-8 unmet for that account, and goes in a surprise row. The rule file (each reason's test and its
correction, stated so another seat would count the same way) is committed before the read; its bytes are bound by hash in the record.

**fanout:** 1 of 1 chain, cap 8. Worker `0.9.0_WK_IRPT_DASHBD~133` (worker), a new slot.

## 92. ROUND 90, WORKSTREAM B (2026-10-13 ~14:5xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ROUND-90 ANALYSIS @d573cb1cb8 section 3 and msg 6986)

Round 89 is terminal (MAY-CLOSE; the CVO's REMEDIATION_v36 @46e9beb3fd: FWD-8 NOT REALIZED, row `IRPT_DASHBD-D2-W133-S1` owed to the CTO). The PRD addendum v0.13, decision 11b, reads FWD-8 at two grains
(a window that agrees within 0.35 pp meets the clause; a window outside it meets FWD-8 only if every differing day carries a stated reason that re-closes the window), counts all 90 stored segments (the 2 with no
flow day included), and routes the day read through IRPT's existing per-account call (`bd_adapter.adapt`: `performancePeriod` and `performanceSeries`, daily cumulative returns), which needs no per-use word. The analysis fixes four items.

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| 1. ledger leg L7, carried: the 2026-10-14 11:41Z fire, `l5b_read.py`; close `irpt-dashbd-thresholds-swap-20261013` or restore rollback `8ELUDq...` the same session | the issuer's own act, no cell | FWD-8 | the 11:41Z fire | none |
| 2a. BUILD the day-grain read of the 7: plan (offline), the live runner (never run by a worker), the analysis, a self-test | `DB-b-168` | FWD-8 | `~133`'s module (read) | R90-1 |
| 2b. the issuer's live pull: ONE `performanceSeries` request per account for each of the 7 segments, read-only, written only to a private folder, never to S3 | the issuer's own act, no cell | FWD-8 | `DB-b-168` drained | R90-1 |
| 2c. READ the 7 at day grain: each differing day gets a reason from round 89's closed list (the day rule committed before the read), the cause corrected and the window re-closed at 0.35 pp, else its days stay UNEXPLAINED by offset and size | `DB-b-169` | FWD-8 | the pull of 2b | R90-1 |
| 3. the 2 no-flow segments by a tracked cell (the accrual correction closes both; the uncorrected control misses both) | `DB-b-170` | FWD-8 | `~133`'s module and rule (read) | R90-2 |
| 4. the FWD-8 grade at the grains of 11b, in the drain-end | the issuer's own act, no cell | FWD-8 | `DB-b-169`, `DB-b-170` drained | R90-1 |

**Decisions inside this decomposition (the issuer's, stated):** (a) the day-differs line is `0.01` pp (one basis point) of daily return, a number the criterion fixes before the read; (b) day figures are offsets from the segment start and sizes in pp, never dates with an account
(the repo carries no client data); (c) the day read is built and run in three steps because a worker holds no credential: the worker builds, the issuer pulls, a second worker reads; (d) the pull's responses live only in the private folder of `~134`.
The vendor read is a POST of a request body the estate already builds, read-only, 7 accounts, one request each; it needs no per-use word (CLAUDE.md, Agent Autonomy; PRD 11b) and no credential is printed or written anywhere.

**fanout:** 2 of 2 chains, cap 8. Workers `0.9.0_WK_IRPT_DASHBD~134` (`DB-b-168`), `~136` (`DB-b-169`, spawned after the issuer's pull) and `~135` (`DB-b-170`).

## 93. ROUND 91, WORKSTREAM B (2026-10-13 ~15:5xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ROUND-91 ANALYSIS @3a44c65c3e section 3 and msg 7032)

Round 90 is terminal (MAY-CLOSE; the CVO's REMEDIATION_v37 @322f6b77f8; row `IRPT_DASHBD-D2-W136-S1` owed to the CTO). The analysis decides PRD 11b's open reading: a window whose stated reason, once corrected, re-closes it within 0.35 pp has met the day clause, so no day read is owed
for the 7 windows reasoned at window grain; the day read is owed only where no window reason closes, which is the 7 (23 days). The next read is the ROWS: a whole-number multiple of income is the signature of a booking difference.

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| 1. ledger leg L7, carried: the 2026-10-14 11:41Z fire, `l5b_read.py`; close `irpt-dashbd-thresholds-swap-20261013` or restore rollback `8ELUDq...` the same session | the issuer's own act, no cell | FWD-8 | the 11:41Z fire | none |
| 2. the ledger-row read of the 23 days: for each differing day, the served side's income and flow rows against Black Diamond's landed transaction rows for the same account and day (and the adjacent trading days), under a closed list written before the read, a reason taken only if correcting that row re-closes the window within 0.35 pp | `DB-b-171` | FWD-8 | `~136`'s record (the 23 days) and the stored tables of `~108` (read) | R91-1 |
| 3. the FWD-8 grade at the grains of 11b as ruled, in the drain-end | the issuer's own act, no cell | FWD-8 | `DB-b-171` drained | R91-1 |

**Decisions inside this decomposition (the issuer's, stated):** (a) the closed list is the CTO's, verbatim: `BD_INCOME_PER_LOT`, `DUPLICATE_ROW`, `BOOKING_DATE_DIFFERS`, `MISSING_IN_LEDGER`, `UNEXPLAINED`; (b) "through IRPT's existing per-account call" is read as: no new vendor call is needed, because Black Diamond's transactions for these accounts are
already landed in `s3://opal-data-assets/blackdiamond/49financial/silver_legacy/transactions/` (the store the earlier tie-out cells read; read90 kept 12 columns of it) and the served side's rows are in the estate's own store the gold producer reads; the cell therefore makes ZERO vendor calls and reads S3 (GET/LIST) only, and a row the landed store cannot show is a surprise
row, on which the issuer decides about a vendor read; (c) the criterion binds the 23 days and the per-account counts to `~136`'s committed record, so the population cannot drift; (d) rows are described by counts, multiples and day offsets, never by security, lot, account or amount in the repo.

**fanout:** 1 of 1 chain, cap 8. Worker `0.9.0_WK_IRPT_DASHBD~137` (`DB-b-171`).


## 94. ROUND 92, WORKSTREAM B (2026-10-13 ~16:4xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ROUND-92 ANALYSIS @a862a037f3 section 3 and msg 7063)

Round 91 is terminal (MAY-CLOSE; the CVO's REMEDIATION_v38 @5e23f18556; row `IRPT_DASHBD-D2-W137-S1` owed to the CTO). The analysis rules: (1) Reading B of `BD_INCOME_PER_LOT` (at least two income rows whose sum is a whole multiple of the served income) is the reading of record, and it takes no day; (2) a day on which
our inputs are whole but Black Diamond computes differently is a tie-out disagreement, recorded with its reason or `UNEXPLAINED`; the served figure stands and no `day_quality` member is added; (3) one more read, built on the measured pattern (on 8 of the 12 multiple-income days the gap equals minus the served income over the prior value): a new reason written before the read.

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| 1. ledger leg L7, carried: the 2026-10-14 11:41Z fire, `l5b_read.py`; close `irpt-dashbd-thresholds-swap-20261013` or restore rollback `8ELUDq...` the same session | the issuer's own act, no cell | FWD-8 | the 11:41Z fire | none |
| 2. the `BD_EXCLUDES_SERVED_INCOME` read over the 23 days: test (the gap is minus the served income over the prior value, within 0.01 pp), correction (remove that income from the served day's return and recompute the window), taken only if the window re-closes within 0.35 pp; the other days re-tested under the full list, Reading B included, after those days are corrected | `DB-b-172` | FWD-8 | `~137`'s module, rule addendum and record (read) | R92-1 |
| 3. the FWD-8 grade in the drain-end; if any account stays open, its days go to the CTO once more and the next ruling is on the endpoint (accept FWD-8 with those accounts named as known oracle gaps: a DONE WHEN change, carried to Andrew as a card) | the issuer's own act, no cell | FWD-8 | `DB-b-172` drained | R92-1 |

**Decisions inside this decomposition (the issuer's, stated):** (a) the closed list of this cell is the analysis's new reason FIRST, then round 91's four with `BD_INCOME_PER_LOT` read as Reading B, then `UNEXPLAINED`: `BD_EXCLUDES_SERVED_INCOME`, `BD_INCOME_PER_LOT`, `DUPLICATE_ROW`, `BOOKING_DATE_DIFFERS`, `MISSING_IN_LEDGER`, `UNEXPLAINED`;
(b) "the same stored rows" is read as the same two S3 stores `~137` read (the day test itself needs only the stored daily table and the stored gold income); the cell imports `~137`'s module by path, does not edit it, and re-reads the rows for the re-test of the other days; (c) the measured "8 of 12" is the worker's, not verified by this seat: the cell records the number of days its test holds on and whether it equals 8;
(d) counts, offsets and sizes only in the repo.

**fanout:** 1 of 1 chain, cap 8. Worker `0.9.0_WK_IRPT_DASHBD~138` (`DB-b-172`).


## 95. ROUND 93, WORKSTREAM B (2026-10-13 ~17:0xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ROUND-93 ANALYSIS and msg 7081)

Round 92 is terminal (MAY-CLOSE; the CVO's REMEDIATION_v39 @063bf7a3df; row `IRPT_DASHBD-D2-W138-S1` asks for the endpoint card). The analysis accepts `BD_EXCLUDES_SERVED_INCOME` as a stated reason, decides account 5 by ONE number (PRD 11b: a window inside 0.35 pp after its reasoned days are corrected meets the clause and its remaining days are not graded one by one), and sends the
endpoint question (FWD-8 accepted with named exceptions) to Andrew as one card. Nothing else is cut until he answers.

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| 1. ledger leg L7, carried: the 2026-10-14 11:41Z fire, `l5b_read.py`; close `irpt-dashbd-thresholds-swap-20261013` or restore rollback `8ELUDq...` the same session | the issuer's own act, no cell | FWD-8 | the 11:41Z fire | none |
| 2. account 5's corrected window: the window return after its 4 reasoned days are corrected (the 3 UNEXPLAINED days stay as served), by the window method of `RULE_EXCL.md` section 5 unchanged, against 0.35 pp; one figure, read from stored local files | `DB-b-173` | FWD-8 | `~138`'s rule and record, `~134`'s pull, the stored tables (read) | R93-1 |

`DB-b-173` takes the DIRECT-ACT path (one cell, LOCAL, a few dozen product lines, no L2, L4-R, L8 to L10): one order, a worker executes, it drains, the close is the issuer's own run of the figure. It reads local files only: zero S3, zero vendor calls.
**Decision inside this decomposition (the issuer's, stated):** the figure is `|G_c - R_c| * 100` for the fifth account of the round-90 plan order, with `G_c = G` (no Black Diamond-side correction is taken for that account) and `R_c` the product of the corrected served daily returns; the uncorrected gap is printed beside it as the negative arm.

**fanout:** 1 of 1 chain, cap 8. Worker `0.9.0_WK_IRPT_DASHBD~139` (`DB-b-173`, direct act).


## 96. ROUND 94, WORKSTREAM B (2026-10-13 ~19:3xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ROUND-94 ANALYSIS section ENRICHMENT LIST and msgs 7181 and 7192; PRD v0.14 @6d694ed9a5, ADMITTED)

FWD-8 is REALIZED WITH NAMED RESIDUE (accounts 1 and 6; the laptop ruling @51f07538ea and the CTO's msg 7104). Andrew-direct ~19:0xZ: the default performance report, on the baseline of the Black Diamond 49 Financial Performance Report he supplied; PRD v0.14 adds FWD-21 (any client at any firm opens ONE default
performance report, on the Performance tab and as the export, in one Opal Shape). The baseline's structure (not its data) is `deliverables/1.0.0_SA_CTO~DELL2/BD_FINANCIAL_PERFORMANCE_REPORT_BASELINE_SCHEMA_20261013.md`; the PDF is client data and stays off the repo. Vendor-agnostic (Andrew ~18:2xZ, `ANDREW_DIRECT_20261013_182xZ_VENDOR_AGNOSTIC_OPAL_SHAPE_IN_GOLD.md`).
Second to O1/O2; takes no seat from IRPT_ANLREQ; every cell is LOCAL or DEV-only and none touches the gold Lambda. Cottonwood and Inflection samples follow once 49 Financial's reads true and are NOT built here.

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| 1. the contract `org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json` (one member per baseline table, column and row; each names its Opal gold source or `ABSENT` with its reason; vendor-free; a `document` layout; folds in FWD-20's map where it exists) and its gap table | `DB-b-174` | FWD-21 | LOCAL | none | R94-1 |
| 2. one 49 Financial multi-account household built into the contract shape from gold, writes nothing served; unsourced = ABSENT, never zero; the proof read is balance identities, not figures | `DB-b-175` | FWD-21 | LOCAL | `DB-b-174` | R94-1 |
| 3a. the Performance tab renders the contract shape in the baseline's section order (DEV-only portal candidate; new files only; the mount is the issuer's hookup at the merge) | `DB-b-176` | FWD-21 | LOCAL | `DB-b-174` (shape); fixture-driven | R94-1 |
| 3b. the export document renders the same shape in the same order (DEV-only portal candidate; new files only) | `DB-b-177` | FWD-21 | LOCAL | `DB-b-176` (the shared view model) | R94-1 |
| 3c. the smoke fixes: the export status chain read to the failing call and the modal widened (S20); FDRXX to CASH (S21); YTD from the first measured day, labeled (S22) | `DB-b-178` | FWD-21 | LOCAL | none | R94-2 |
| 4. ledger leg L7, carried: the 2026-10-14 11:41Z fire; `l5b_read.py` | the issuer's own act, no cell | FWD-8 | the fire | none |

**Decisions inside this decomposition (the issuer's, stated):** (a) the CTO's "Performance tab and the export in one portal candidate" is cut as FOUR cells by write set: the tab and the export document are NEW files in disjoint directories (`dashboard/report/` and `render/performance/report/`), the smoke fixes own the existing files they touch
(`export/ExportModal.tsx`, the YTD label files), and every one-line mount of a new component into an existing file is the issuer's hookup in ONE merge commit (dispatch Step 5); the merged result goes to the CTO as one candidate; (b) the contract is the shape both renderers and the sample share, so it carries a `document` layout (how a filled report lays out);
(c) a `member` is a baseline table cell, a chart, a cover field or a convention (the checker derives the required set from the baseline's structure: 117 members, no extras); (d) FDRXX: the cell reads where the class is assigned; if the assignment is in a producer or gold script (outside DEV-only scope) it files a row naming the file and line and changes nothing there; (e) counts and synthetic fixtures only in the repo; the household chosen for the sample is referenced by hash.

**fanout:** 2 of 2 chains, cap 8. Workers `0.9.0_WK_IRPT_DASHBD~140` (`DB-b-174`) and `~144` (`DB-b-178`) now; `~141` (`DB-b-175`) after `DB-b-174` drains; `~142` (`DB-b-176`) after `DB-b-174`; `~143` (`DB-b-177`) after `DB-b-176`.

## 97. ROUND 95, WORKSTREAM B (2026-10-13 ~22:0xZ, issuer 2.0.0_SA_COO~D2, on the CTO's ruling msg 7289 after row W141-S3; round 94 is still executing, this round is its own issuance because the gate admits one issuance per round)

**Why a new round.** Gold `account_activity_daily` holds four trading days, so no report window opens from it. The CTO rules: every window figure `account_return_daily` can derive comes from it; what only activity holds reads ABSENT until IRPT_BCKEND backfills activity (queued to `2.0.0_SA_COO~P2`). One cell is cut, in its own round:

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `DB-b-179` re-source 36 window members of the performance report contract (the value summaries' beginning, ending, net additions, net gain, and the account returns, for QTD, YTD, 12M and since inception) to `account_return_daily`; contract 0.2.0, the 0.1.0 bytes in its `lineage`; the gap table regenerated | FWD-21 | LOCAL | `DB-b-174` | R95-1 |

`DB-b-175` (the household sample) is stopped and re-seated after `DB-b-179` drains, reading windows from `account_return_daily`. The records of `DB-b-175`, `DB-b-176` and `DB-b-177` bind to the contract's bytes; the checker accepts the 0.1.0 bytes through the lineage, so no record is re-made. **fanout:** 1 of 1 chain, cap 8. Worker `0.9.0_WK_IRPT_DASHBD~145` (`DB-b-179`). Round 94 stays open until its orders are terminal; round 96 carries the FDRXX class cell.

## 98. ROUND 96, WORKSTREAM B (2026-10-13 ~23:5xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2 msgs 7349 and 7258)

Rounds 94 and 95 are terminal (MAY-CLOSE; packets with the CVO). Round 94 built FWD-21's pieces but mounted none: nothing serves a filled report, so a mount has no data. The CTO rules (msg 7349): (2) render the real 49 Financial sample locally (HTML and PDF, private folder) as round 96's first cell so Andrew can read it; (1) the served FilledReport (platinum object and route, IRPT_BCKEND's) comes AFTER his read, so a layout he changes is not built into a route twice. Also (msg 7258): FDRXX to CASH in the gold classifier, keyed on the money-market type, under a never-widen pair with a count of the holdings that move.

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| 1. the real sample rendered through the tab and export components into a local HTML (tab), HTML and PDF (export) in `C:/dev/_irpt_private_evidence_20261009/fwd21_sample/`, never in the repo | `DB-b-180` | FWD-21 | LOCAL | `DB-b-175`, `DB-b-176`, `DB-b-177` (drained) | R96-1 |
| 2. FDRXX to CASH, cell A: the rule in `etf_classifier.py` keyed on the canonical row's `sub_asset_class`, its tests and mutant, and the count of canonical rows and served holdings that move | `DB-b-181` | FWD-8 class label, FWD-21 | LOCAL | none | R96-2 |
| 3. FDRXX to CASH, cell B: the apply by `0.7.0_AE_CloudOps~IB2` under a signed never-widen pair, ledger first | the issuer's own act and a later WORLD order, no cell yet | the same | WORLD | `DB-b-181` drained, the count read, both halves signed | R96-2 |
| 4. ledger leg L7 (held until the 2026-10-14T11:41Z fire) | the issuer's own act, no cell | FWD-8 | the fire | none |

**Decisions inside this decomposition (the issuer's, stated):** (a) the render is CLIENT DATA: it lives only in the private folder, the record carries paths, hashes and counts, and the checker verifies the files by their absolute paths and refuses any output inside the repo; (b) the render harness is tracked (it holds no data), the outputs are not; (c) cell A's cash class value must be one the canonical table already uses: if none exists the worker stops with a row and the issuer rules the vocabulary; (d) cell B is a separate order because it is a WORLD act that needs the count, the pair and the AE applier, like `DB-b-164` and `DB-b-165`.

**fanout:** 2 of 2 chains, cap 8. Workers `0.9.0_WK_IRPT_DASHBD~146` (`DB-b-180`) and `~147` (`DB-b-181`).

## 99. ROUND 97, WORKSTREAM B (2026-10-14 ~00:1xZ, issuer 2.0.0_SA_COO~D2, on worker ~146's row W146-S1; round 96 is still executing, the gate admits one issuance per round)

`DB-b-180` (the local render of the real sample) stopped before any output: the real sample and the components do not agree on the shape of a filled report. The report contract's `document` layout (0.2.0) never said how a filled report names its accounts or keys its per-account values; the builder (`~141`) wrote top-level `household`, `rows`, `values`, `windows`, account entries `{account_key, last_four}` and bare per-account maps; the components (`~142`, tested) read top-level `household` and `values`, account entries `{account_id, last4, first_data_date, window_status}` and `{"by_row": {...}}`. The components' own note asked for exactly this clarification. The issuer rules inside its own decomposition: the contract adopts the tested reading, the builder conforms.

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| 1. contract 0.3.0 states `document.filled_report` (the shape the components read), the builder emits it, the real sample rebuilt (same household), the regenerated build record still passing round 94's DB94-2-AC1 | `DB-b-182` | FWD-21 | LOCAL | `DB-b-175`, `DB-b-176`, `DB-b-179` (drained) | R97-1 |

Then `DB-b-180` (round 96, worker `~146`) is re-seated to render the rebuilt sample; its order needs no change (the checker's digit rule was fixed in `5d0a8c2f95`, row W146-S3). **Decisions inside this decomposition (the issuer's, stated):** (a) the components are the reference because they are built, tested and in a branch the CTO's review will read; changing them would re-open three drained cells, while the builder is one file; (b) the household stays the same (the order asserts the household reference hash), so Andrew's sample does not change under him; (c) the records bound to the contract's bytes stay valid through the lineage (0.1.0, 0.2.0, 0.3.0).

**fanout:** 1 of 1 chain, cap 8. Worker `0.9.0_WK_IRPT_DASHBD~148` (`DB-b-182`).

## 100. ROUND 98, WORKSTREAM B (2026-10-14 ~00:5xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2 msg 7383; the FDRXX pair is SIGNED on both halves at packet sha256 cfc1dd8d, CTO half @d3b576bb67)

The CTO signed the pair and ruled its four questions: (1) the C_06 history discontinuity is ACCEPTED; (2) CASH_USD is a later counted pair, not this release; (3) the pair alone is NOT enough, because Andrew's smoke was on an Inflection client's Investor Reporting holdings page and the COO half says that page's snapshot path is not covered: read where that page gets a position's class, and if it is a separate copy, one rule there under its own pair; (4) the silver label is accepted. Andrew's smoke item closes only on that page reading CASH.

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| 1. the apply: ONE S3 object (`etf_classifier.py`) from the live bytes to `e340e07f4e`'s, by the AE applier under the signed pair, ledger first, tests and import smoke before, no chain run in flight, L3 (the first D_04 run read) open for the issuer | `DB-b-183` | FWD-8 class label, FWD-21 | WORLD | the pair (both halves SIGNED) | R98-1 |
| 2. a READ of where the IR holdings page gets a position's class, whether it shares the gold classifier or its table, and whether it needs its own rule | `DB-b-184` | FWD-8 class label | LOCAL | none | R98-2 |
| 3. CASH_USD as its own counted pair | the issuer's own act, no cell yet | the same | WORLD | a count, then the pair | none this round |
| 4. a rule at the IR holdings page's own class source, if `DB-b-184` finds a separate copy | a later cell, under its own pair | the same | WORLD | `DB-b-184` | next round |
| 5. ledger leg L7 (held until the 2026-10-14T11:41Z fire) | the issuer's own act, no cell | FWD-8 | the fire | none |

**Decisions inside this decomposition (the issuer's, stated):** (a) the apply is a WORLD order to `0.7.0_AE_CloudOps~IB2`, modeled on `DB-b-165`, because the pair's condition 6 names an AE seat and not a worker; (b) the read is a separate LOCAL cell on its own chain, so the apply does not wait on it and the page's answer does not wait on the apply; (c) the read proposes a rule but writes none, since a rule at a second copy moves served classes and needs its own count and pair; (d) CASH_USD is not cut: the CTO ruled it a later counted pair, and cutting it uncounted would be the unbounded act; (e) the pair's condition 7 (the first D_04 run after the upload READ before the ledger closes) is the issuer's open leg L3, not a cell.

**fanout:** 2 of 2 chains, cap 8. Applier `0.7.0_AE_CloudOps~IB2` (`DB-b-183`) and worker `0.9.0_WK_IRPT_DASHBD~149` (`DB-b-184`).

## 101. ROUND 99, WORKSTREAM B (2026-10-14 ~01:2xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2 msgs 7399 and 7401; round 98 is still executing, the gate admits one issuance per round)

The FDRXX apply (`DB-b-183`) is KNOWN-HELD on ledger `secclass-e97-c06-d04-rolling-rederive-sc1-20261012` (dell1's, HELD-SOVEREIGN-GATED; the CTO ruled it blocks because its held reads are on the outputs the release changes; FB-j-3 does not). The CVO's row W147-S3 (ARMED, disarm owner this seat) names the other cash path: the synthetic sweep-cash ticker `CASH_USD` still serves fixed_income before any row is read. The CTO orders it as its own counted pair, written now so both applies run in ONE window after the hold closes, FDRXX first, then CASH_USD; W147-S3 disarms on the second's after-read.

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| 1. `CASH_USD` serves the cash class in `classify` and `classify_with_identity`; tests updated and a mutant; the count of served positions that move; the consumers that treat it as fixed income on purpose | `DB-b-185` | FWD-8 class label, FWD-21 | LOCAL | none | R99-1 |
| 2. the CASH_USD never-widen packet and COO half, from the cell's record | the issuer's own act after `DB-b-185` drains | the same | WORLD | `DB-b-185` | none |
| 3. the CASH_USD apply by the AE applier, in the same window as `DB-b-183`, after the hold closes | a later WORLD order | the same | WORLD | both pairs SIGNED, `DB-b-183` applied | next round |

**Decisions inside this decomposition (the issuer's, stated):** (a) one cell, because the change is two lines and the work is the count and the consumers; (b) the CASH_USD release is a SECOND release of the same S3 object, so `DB-b-183` is amended to upload the pin's bytes (`e340e07f4e`, sha256 `e7385264...`) from a detached worktree if the shared tree has moved on, and the CASH_USD apply will pin its own bytes; (c) round 96's checker `p96_round96.py` bound the classifier to the working file's hash, so it is amended to accept the pin's hash as well (no gate limb graded: a check file); (d) a consumer that depends on `CASH_USD` being fixed_income is a finding the pair prices, not a patch.

**fanout:** 1 of 1 chain, cap 8. Worker `0.9.0_WK_IRPT_DASHBD~150` (`DB-b-185`).

## 102. ROUND 100, WORKSTREAM B (2026-10-14 ~01:5xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2 msg 7422)

Round 99's count found the synthetic ticker `CASH_USD` on none of 1,314,777 lots; the CTO ruled the CASH_USD change reverted (done @0f8d33c431, row S25 disarms W147-S3). What the snapshot does hold is 11 lots whose ticker is `CASH` (Black Diamond's own cash line). Nobody has read how those classify, or what each page serves for them; Andrew's smoke note reads "Cash as a ticker should be CASH". The FDRXX apply (`DB-b-183`) is unchanged and waits on SC-e-97.

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| 1. a READ of the 11 CASH lots: the canonical row for the ticker CASH, the gold classifier's answer, the class the Advisor Intelligence and Investor Reporting pages serve, and whether Andrew's note is a class, a ticker or a display label | `DB-b-186` | FWD-8 class label | LOCAL | none | R100-1 |

**Decisions inside this decomposition (the issuer's, stated):** (a) one read cell and no change, because the CTO ordered a read and the answer decides whether a rule, a display mapping or nothing is owed; (b) the checker anchors the count (11 lots in 1,314,777 rows of the 2026-10-09 snapshot) on this seat's own read, so a worker that reads a different object fails and says why; (c) the Investor Reporting rule for canonical rows typed Cash is `2.0.0_SA_COO~P2`'s (CTO msg 7410), so this cell proposes nothing there and reads only what that page serves for these lots.

**fanout:** 1 of 1 chain, cap 8. Worker `0.9.0_WK_IRPT_DASHBD~151` (`DB-b-186`).

## 103. ROUND 101, WORKSTREAM B (2026-10-14 ~02:4xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2's ROUNDS 99-100 ANALYSIS ENRICHMENT LIST, msgs 7451 and 7465; rounds 99 and 100 CLOSED, round 98 still open on the held FDRXX apply)

FWD-21 moves from one rendered sample toward the three firms. The CTO's list is cut as five cells. Two issuer findings shape it. (1) **The absent count is 62, not 73:** of the contract's 117 members the real sample fills 55 and holds the absent form on 62 (46 the contract itself sources ABSENT, 16 sourced from gold but unfilled for lack of history); the 44 and 73 carried in earlier notes counted the per-row members only. The checker recomputes the set from the sample. (2) **Item 3 cannot be built from gold:** `s3://opal-data-cot/irpt/` and `s3://opal-data-inf/irpt/` list EMPTY (the issuer's own read, 2026-10-14), so no C-SHAPE table exists for Cottonwood or Inflection and the builder has nothing to read; PRD S13, the adapters, is unbuilt. The CTO agreed (msg 7465): item 3 becomes one read cell that also names the gold IRPT_BCKEND already builds for those firms as candidate adapter inputs (an adapter reuses it, never re-pulls beside it); the adapters and the two households follow in round 102.

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| 1. the three render defects (an absent reason prints once per section, the footer reads the household's last measured date, each chart draws or says why) fixed in the components and the real sample re-rendered, the PDF read as an image page by page | `DB-b-187` | FWD-21 | LOCAL (portal branch only, never pushed) | none | R101-1 |
| 2a. the 62 ABSENT members classified (a) mappable now, (b) derivable by a ratified rule, (c) truly absent | `DB-b-188` | FWD-21 | LOCAL | none | R101-2 |
| 2b. the builder fills every (a) member, takes `--firm`, same household, nothing else moves | `DB-b-189` | FWD-21 | LOCAL | `DB-b-188` | R101-2 |
| 3. a READ of what Cottonwood and Inflection hold against the eight C-SHAPE tables and which of it is existing gold | `DB-b-190` | FWD-21, FWD-2 | LOCAL | none | R101-3 |
| 4. the section-by-section check of the re-rendered 49 Financial report by a seat other than the builders (mechanical record, plus a JUDGMENT criterion the CVO grades at L9) | `DB-b-191` | FWD-21 | LOCAL | `DB-b-187`, `DB-b-189` | joins R101-1 and R101-2 |
| 5. the portal candidate: ONE `cand/dell2/<slug>` branch from origin/PROD carrying the report components and their hookups, run on the 5174 dev build, registered as a client-facing approval row only after item 4 passes | the issuer's own act after the round drains, no cell | FWD-21 | the issuer | items 1 and 4 | none |

**Decisions inside this decomposition (the issuer's, stated):** (a) `DB-b-187` works in a portal worktree cut from the branch carrying both components (`wk-IRPT_DASHBD-143-portal`); the harness is copied into its own folder, the round-96 files stay as they were; (b) the checker anchors on the real sample's bytes (sha256 `76a48793...`) and recomputes the absent set, the chart members, the absent-reason repeat counts and the footer from the files, so a worker's record cannot assert its own pass; (c) `DB-b-189` writes its sample to a NEW private path and leaves the old one untouched, so Andrew's current read is not moved under him; (d) the section check's judgment criterion is carried on the cell and is the CVO's alone (`DB101-5-J1`); (e) Cottonwood and Inflection households and the check on their renders wait for round 102; (f) YCharts: none is called (the CTO's hold, msg 7440, lifted at 02:23Z but no cell here needs it; a benchmark that would need a live pull reads ABSENT).

**fanout:** 3 of 2 chains, cap 8, reason: by the edge rule `DB-b-187` and `DB-b-188` meet at the join `DB-b-191`, but they share no file and no data; `DB-b-190` is the second chain. Workers `0.9.0_WK_IRPT_DASHBD~152` (`DB-b-187`), `~153` (`DB-b-188`) and `~155` (`DB-b-190`) now; `~154` (`DB-b-189`) after `DB-b-188` drains; `~156` (`DB-b-191`) after `DB-b-187` and `DB-b-189` drain. portal_ref: `wk-IRPT_DASHBD-143-portal` for `~152`; `wk-IRPT_DASHBD-152-portal` for `~156`.

**ERRATUM to section 103 (issuer, 2026-10-14 ~03:4xZ).** Two statements above were wrong and are corrected here, not edited in place. (1) "`s3://opal-data-cot/irpt/` and `s3://opal-data-inf/irpt/` list EMPTY" read the registry's `bucket` field; gold lives at the `lib/opal_naming.py address()` bucket: `s3://opal-data-cottonwood/irpt/cottonwood/gold/` holds `account_return_daily` (3,325 daily partitions from 2013), `dim_return_method` (v3), `holdings` and the holdings performance tables; `s3://opal-data-inflection/irpt/inflection/gold/` holds the holdings tables and no `account_return_daily`. `DB-b-190` is re-seated to read the real prefixes against the contract schema hashes (its first record, BLOCKED, is void). (2) "The absent count is 62, not 73" counted a per-account map whose every entry is absent as filled; at member grain the sample holds 73 absent members of 117 (44 filled; 46 after `DB-b-189`). `DB-b-188` is re-seated to classify the 11 missing members; `DB-b-191` counts at member grain. Neither error changes a cell's purpose.

## 104. ROUND 102, WORKSTREAM B (2026-10-14 ~03:5xZ, issuer 2.0.0_SA_COO~D2, on 1.0.0_SA_CTO~DELL2 msgs 7486, 7490 and 7494; round 101 is still executing, the gate admits one issuance per round)

The CTO ruled round 102 (msg 7490): the Cottonwood adapter first (`account_dim` plus the household key, `account_return_daily` by the same method), the benchmark-source read, Inflection in round 103. After the issuer's bucket error was found (erratum to section 103: Cottonwood's gold at the `address()` bucket already holds `account_return_daily`), the CTO HELD the two Cottonwood build cells until `DB-b-190`'s re-read reports which tables exist and which are off-contract, and re-bases round 102 on that (msg 7494); the benchmark read does not depend on it and runs now.

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| 1. a READ of where the four Opal model benchmark returns come from, whether a dated daily model series exists in gold, and what the 32 benchmark members can be filled from | `DB-b-192` | FWD-21 | LOCAL | none | R102-1 |
| 2. the Cottonwood tables that are missing or off-contract, built to the contracts (cells cut by the CTO's re-based list) | later cells in this round's rectangle, held | FWD-21, FWD-2 | LOCAL, then WORLD for the apply | `DB-b-190` (re-read) | held |

**Decisions inside this decomposition (the issuer's, stated):** (a) round 102's rectangle is the CTO's re-based list; this issuance covers the one cell the CTO released, and the held build cells join the round by a recut once the CTO re-bases (stated here so the round does not look covered when it is not); (b) the read is read-only with no YCharts call (the benchmark producer is MDPF's, not YCDGEN's); (c) the checker anchors the plan to the evidence: a compounding plan needs a dated daily series, a mapping plan needs none and keeps since-inception and the chart absent.

**fanout:** 1 of 1 chain, cap 8, reason: one read cell; the held cells are not cut. Worker `0.9.0_WK_IRPT_DASHBD~157` (`DB-b-192`).

## 105. ROUND 103 (the issuance for the CTO's ROUND-102 ANALYSIS), WORKSTREAM B (2026-10-14 ~05:0xZ, issuer 2.0.0_SA_COO~D2, on `CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_102_20261014.md` @9f4d4ea591 and rulings 7508, 7511)

**Numbering.** The CTO's analysis names this "round 102"; round 102 already carries the one issuance of `DB-b-192` (section 104), and the gate admits one issuance per round, so the enrichment list is issued as round 103. The CTO's "round 103" (the Cottonwood household rendered, then Inflection) follows as round 104; the CTO is told.

The CVO graded round 101's judgment criterion PASS (L9, `ADJUDICATION_v62.md`). The list is cut as four cells, each with its own write set:

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| 1. the render fix: percents at their stored scale (a test pins 1.5 to read 1.5%), client-safe wording with a word-list check, every omission said in words, the holdings table in the baseline's orientation, the header's firm title from the registry; 49F re-rendered and every PDF page read as an image | `DB-b-193` | FWD-21 | LOCAL (portal branch only, never pushed) | none | R103-1 |
| 2. the model benchmark windows: the builder reads the served dated series, compounds QTD, YTD, 12 months and since the household's first day, fills the 32 benchmark members and the 12-month chart; the contract states the new source (0.4.0, the 0.3.0 bytes in lineage) | `DB-b-194` | FWD-21 | LOCAL | none | R103-2 |
| 3. a READ of why Cottonwood's `account_return_daily` stops at 2026-06-22 (producer, DESIRED against APPLIED, trading days since, what a resume needs) | `DB-b-195` | FWD-21, FWD-2 | LOCAL | none | R103-3 |
| 4. the Cottonwood adapter's first table: `account_dim` and the household key, a contract, an adapter, tests and a read-only dry run on Cottonwood's own silver prefix; nothing written to AWS | `DB-b-196` | FWD-21, FWD-2 | LOCAL (the apply is a later WORLD order under a pair) | none | R103-4 |

**Decisions inside this decomposition (the issuer's, stated):** (a) the four cells share no file: the render fix owns the two component directories and the tests directory; the benchmark cell owns the performance report contract and its own folder; the read owns only its folder; the adapter owns the new `account_dim` contract, the new `adapters/` directory and its test file; the sample builder lives in each worker's own folder; (b) the render fix renders the round-101 filled sample (so it does not wait on the benchmark cell); a final re-render of the report with the benchmark figures is the issuer's step after both drain; (c) the benchmark cell edits the performance report contract (the previous contract edits, rounds 95 and 97, were worker cells under the same rule): records bound to the 0.3.0 bytes stay valid through the lineage, while the round-94 gap-table checks (`DB94-1`, `DB94-6`) compare the gap table's totals with the contract and are superseded by this change, as `DB99-1` is by the revert (the issuer reads them as historical); (d) landing the model series in the report's gold, and any write to Cottonwood's gold (the `account_dim` table and a resume of `account_return_daily`), are later rounds under never-widen pairs: this round writes nothing to AWS; (e) the issuer's grant decision for the adapter cell: a read of `s3://opal-data-assets/blackdiamond/cottonwood/` only, never another firm's prefix; (f) rows held with the issuer (CTO's list): W152-S3 (the sheet height set inline because `print.css` is outside the grant) is RULED acceptable until the document is wired into the app's print stack, and is carried to that hookup; W155-S9 (the registry's bucket field disagrees with `address()`) is routed to 0.0.0_AB_MSTR~DELL2 for the LGIC registry's owner (the registry is LGIC's, `infra/logic/registry/`).

**fanout:** 4 of 4 chains, cap 8. Workers `0.9.0_WK_IRPT_DASHBD~158` (`DB-b-193`, portal_ref `wk-IRPT_DASHBD-152-portal`), `~159` (`DB-b-194`), `~160` (`DB-b-195`), `~161` (`DB-b-196`).

## 106. ROUND 104, WORKSTREAM B (2026-10-14 ~06:0xZ, issuer 2.0.0_SA_COO~D2, on `CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_104_20261014.md` @267f2b547a; the CVO graded round 103's `DB103-1-J1` FAIL on its wording clause, orientation MET)

The CTO's enrichment list is cut as five cells; the applies of items 3 and 4 are round 105, after the CTO's and this seat's halves of each never-widen pair.

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| 1. the render cell, J1's remedy: an unheld class prints the baseline's dash (ASCII-safe in source), every kind note names its figure, a chart title says what it draws, the before-fee line follows its member; 49F re-rendered, every PDF page read as an image; J1 re-graded at L9 | `DB-b-197` | FWD-21 | LOCAL (portal branch only, never pushed) | none | R104-1 |
| 2. contract 0.4.1 (the percent-points sentence and a `unit_scale` field on every percent member) and the `absent_kind` proposal with its four-postulate record and word-boundary token census; no code reads the field | `DB-b-198` | FWD-21 | LOCAL | none | R104-2 |
| 3a. the model daily series into the report's gold: the table's contract, a producer module, offline tests and the never-widen packet (keys, rollback, no other key moves); nothing written | `DB-b-199` | FWD-21 | LOCAL (the apply is a later WORLD order) | none | R104-3 |
| 3b. Cottonwood `account_dim` and the household key into its `address()` gold: the never-widen packet; nothing written | `DB-b-200` | FWD-21, FWD-2 | LOCAL (the apply is a later WORLD order) | none | R104-4 |
| 4. who rewrote Cottonwood's manifests on 2026-10-11 (a read), then the return-gold resume packet onto a schedule (the backfill 2026-06-23 to T-1 by the trading calendar, the EventBridge rule, the keys, the rollback); nothing written | `DB-b-201` | FWD-21, FWD-2 | LOCAL (the apply is a later WORLD order) | none | R104-5 |

**Decisions inside this decomposition (the issuer's, stated):** (a) the five cells share no file: the render cell owns the component and test directories; the contract cell owns the performance report contract and its folder; the series-gold cell owns a new contract, a new producer module and its tests; the two packet cells own only their folders; (b) `unit_scale`, not a rename of `unit`: the components and every checker key on `unit == "percent"`, so the ruling's intent (a consumer can reject a fraction) is met by an added field; (c) until the `absent_kind` proposal is accepted the render recognises an unheld class by the builder's one fixed phrase inside ONE function that the field replaces; (d) the COO halves of the two gold-write packets and of the resume packet are the issuer's act after each packet drains, then the CTO's halves, then round 105's apply orders to an AE applier; (e) the resume cell's input question is part of its read: Cottonwood's return gold is produced from a Commonwealth snapshot pinned at 2026-06-23, so a resume cannot read newer input unless one exists, and the packet states the block instead of promising a backfill; (f) a gold-write cell never writes, so each is LOCAL, and the WORLD apply is cut only under a signed pair.

**fanout:** 5 of 5 chains, cap 8. Workers `0.9.0_WK_IRPT_DASHBD~162` (`DB-b-197`, portal_ref `wk-IRPT_DASHBD-158-portal`), `~163` (`DB-b-198`), `~164` (`DB-b-199`), `~165` (`DB-b-200`), `~166` (`DB-b-201`).

## 107. ROUND 105, WORKSTREAM B (2026-10-14 ~12:3xZ, issuer 2.0.0_SA_COO~D2, on `CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_105_20261014.md` @9edfbc0784, msg 7595; the CVO graded round 104's `DB104-1-J1` FAIL on clause 1, orientation MET; pivot packet O3: one 49 Financial account rendered as the default performance report)

The CTO's four cells are cut as THREE orders and ONE direct act. The disclosure page and the absent kind are RELEASE GATES: no rendered report reaches a client, and every render stays in the private evidence folder.

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| 2 (data half). Carrier A: `{"absent": "<words>", "kind": "<KIND>"}`, the closed set NO_SOURCE_YET, INSUFFICIENT_HISTORY, SOURCE_BREAK; NOT_HELD leaves the axis (an unheld class is the text value `UNHELD`, printed as the baseline's dash); contract 0.4.2; the sample builder writes `kind` and fills the activity members that another table of the same report already prints; the cross-table rule | `DB-b-202` | FWD-21 | LOCAL (private sample only) | none | R105-A |
| 1 + 2 (view half). The render remedy: the view reads `kind` (the keyword inference `absentKindOf` is deleted), a note never claims a reason for a figure the report prints, a section note names its account, slot names become client words or the line is dropped, an asterisk prints only with its footnote, one sentence per note; 49 Financial re-rendered privately, every page read as an image; J1 re-graded at L9 | `DB-b-203` | FWD-21 | LOCAL (portal branch only, never pushed) | `DB-b-202` (its sample and contract) | R105-A |
| 3. The model windows by build-time READ: the DB-b-199 producer is reworked into a reader of the served object (renamed, not `market_topic_daily`), compounding QTD, YTD, 12M and since-household-inception, each value carrying `source` (key and VersionId) and `data_as_of`; the series contract carries the claim fields; the retired contract and module are removed; nothing is written | `DB-b-204` | FWD-21 | LOCAL | none | R105-B |
| 4. A READ of the 49 Financial template set for the disclosure page text: path, page, byte count, no copy into the repo; if it is absent, ONE call for Andrew through the CTO | `DB-b-205` | FWD-21 | LOCAL | none | R105-C |

**Decisions inside this decomposition (the issuer's, stated):** (a) the CTO's cell 2 is split at the seam between data and view: the builder, the contract and the cross-table rule are `DB-b-202`; the portal view that reads `kind` and the deletion of `absentKindOf` ride `DB-b-203`, because both touch the report components, and the view needs the new sample; the two orders are ONE chain for ONE worker slot (the second is `staged` until the first drains); (b) `check_sample_shape` and `is_absent` are the ISSUER's check library (`checks/r97`): round 105's check file carries their kind-aware forms, so the worker's sample is graded by the issuer's own rule, and the cross-table rule is a function of that file; (c) the unheld class value is the TEXT `UNHELD` inside a `by_row` map of asset classes (a text is already a figure of the shape), and contract 0.4.2 carries the print rule "a by_row asset-class entry holding the text UNHELD prints the baseline's dash"; (d) the cross-table pairs the check pins are the ones the CVO found, each verified against the round-104 sample before the cut: `act.beginning_value`, `act.net_gain` and `act.ending_value` (household and account grain) against `pvs.last_12_months.*` and `avs.last_12_months.*`; the remedy is to FILL the activity members from the same window figure, and the members that stay absent keep their true kind (`INSUFFICIENT_HISTORY` where the activity table is short); (e) `DB-b-205` is the issuer's DIRECT ACT, not a worker cell: the template set was "sent last week" to Andrew, so the read goes through the gateway's mail and file tools, which a worker does not have; the result is a record and one row under `deliverables/2.0.0_SA_COO~D2/`; (f) the applies of the model windows, `account_dim` and the Cottonwood resume are NOT in this round (the CTO: Cottonwood and Inflection wait behind the 49F thread); (g) the rows held with the CTO (W158-S1, S4, S6) are disarmed by row D2-S29, not by this decomposition.

**fanout:** 2 of 3 chains, cap 8, reason: R105-C is the issuer's direct act with no worker. Workers `0.9.0_WK_IRPT_DASHBD~167` (`DB-b-202`, then `DB-b-203`, portal_ref `wk-IRPT_DASHBD-162-portal`) and `~168` (`DB-b-204`).

## 108. ROUND 106, WORKSTREAM B (2026-10-14 ~14:3xZ, issuer 2.0.0_SA_COO~D2, on `CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_106_20261014.md` @b05c8f07a9, msg 7683; the CVO graded round 105's `DB105-2-J1` FAIL on two remaining instances: the holdings household Net Gain row that the report prints elsewhere, and two chart notes that claim "needs more history" for figures the report prints)

The CTO's three cells are cut as TWO orders and ONE issuer act. The disclosure page stays a release gate on Andrew's call a252 and is not graded.

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| 1 + 2 (data half). The DB-b-204 reader wired into the builder (it replaces `~159`'s `model_series`), the count of the 32 benchmark members filled printed; the holdings household Net Gain (four windows) filled from the figure the value summary prints; the split columns Contributions, Withdrawals and Income are `NO_SOURCE_YET`; contract 0.4.3 (text only: a window the account did not span prints words, never the dash); the sample passes the whole-document rule | `DB-b-206` | FWD-21 | LOCAL (private sample only; one S3 GET of the served series and the builder's reads) | none | R106-A |
| 2 (view half). The render remedy: an absent chart takes no kind note and never claims a reason (a computed "Chart not drawn in this report; the values are in the table on page N", or the slot is dropped); the split columns in plain words ("Opal does not split net additions into contributions, withdrawals and income yet."); a window the account did not span in words, never the dash, with a test; 49 Financial re-rendered privately, every page read as an image; J1 re-graded at L9 | `DB-b-207` | FWD-21 | LOCAL (portal branch only, never pushed) | `DB-b-206` (its sample and contract) | R106-A |
| 3. The WHOLE-DOCUMENT absent-vs-printed rule, replacing round 105's six hand-picked pairs: every absent cell keyed (measure, entity, window), searched against every other cell of the document, the denominator and the unmapped count printed, an unmapped key FAILS, a planted mutant caught | `DB-b-208` | FWD-21 | LOCAL | none | R106-B |

**Decisions inside this decomposition (the issuer's, stated):** (a) `DB-b-208` is the issuer's OWN check, not a worker cell: the rule lives in the issuer's check file `checks/r106/p106_round106.py` as `whole_document_scan`, with its grammar, denominator, unmapped count, planted mutant and a real red arm (on the round-105 sample it finds exactly the CVO's four page-7 conflicts, 0 unmapped); (b) the rule runs on the sample's cells, which are exactly the cells the export prints (the render check proves every contract member prints in both HTMLs), and it treats ending value as ONE figure at as_of across the value summaries, the activity table and the holdings row; (c) a chart is not a figure: it is exempt from the key rule and graded in the render by its note, whose page N the render check COMPUTES from the export (the page of the table that prints the chart's values); (d) the holdings household Net Gain row is filled, not re-explained: `hold.net_gain_*` for last 12 months, YTD, QTD and since inception takes the same value as `pvs.<window>.net_gain` (mtd has no value-summary twin and stays absent); (e) the CTO's "an absent chart takes no kind" is read as a VIEW rule: the data keeps the absent form `{absent, kind}` the shape requires, and the view never prints a kind note for a chart; (f) the dash prints in exactly the cells holding the text UNHELD: the render check counts dash-only elements and requires equality; (g) the two orders are one chain for ONE worker slot (the second is `staged` until the first drains); (h) the applies and Cottonwood stay out of this round (unchanged from round 105).

**fanout:** 1 of 2 chains, cap 8, reason: R106-B is the issuer's own check with no worker. Worker `0.9.0_WK_IRPT_DASHBD~169` (`DB-b-206`, then `DB-b-207`, portal_ref `wk-IRPT_DASHBD-167-portal`).

## 109. ROUND 107, WORKSTREAM B (2026-10-14 ~15:2xZ, issuer 2.0.0_SA_COO~D2, on `CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_107_20261014.md` @4aedf6a687, msg 7700; the CVO graded round 106's `DB106-2-J1` FAIL on two single lines, every round-105 count fixed: the page-5 chart pointer names the wrong page for the household's totals, and the page-6 foot note calls the household allocation unavailable above a filled Allocation column)

The CTO's one cell is cut as ONE order and ONE issuer act. The disclosure page stays a release gate on Andrew's call a252; nothing else is cut until J1 passes.

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| The render cell: the page-5 chart pointer reads "Chart not drawn in this report; the period totals are in the table on page N" with N computed (the household's 12-month totals print in the Portfolio Value Summary); the page-6 foot note drops the household-allocation clause (the class half stays; no 100 percent household row is added); the repeated split-column line collapses to one household-level sentence plus "the same applies to each account"; every note and every member cell carries the keys the note-level rule reads (`data-note`, `data-note-keys`, `data-note-page`, `data-entity`); 49 Financial re-rendered privately, every page read as an image; the CVO re-reads pages 5 and 6 and any page the fix moves | `DB-b-209` | FWD-21 | LOCAL (portal branch only, never pushed) | none (it re-renders the round-106 sample) | R107-A |
| The NOTE-LEVEL extension of the whole-document rule: every note carries the member keys it names; a note that claims absence of a key a printed cell carries FAILS; a note that points to "page N" FAILS unless page N prints a cell carrying its entity and member, N computed from the render, never typed; two planted mutants (a pointer to the wrong page, a note naming a printed figure); the denominator counts cells AND notes | `DB-b-210` | FWD-21 | LOCAL | none | R107-B |

**Decisions inside this decomposition (the issuer's, stated):** (a) `DB-b-210` is the issuer's OWN check, in `checks/r107/p107_round107.py` (`note_rule`, `mutate_pointer`, `mutate_absent_note`, with a 9-arm synthetic self-test that includes both planted mutants); (b) the rule reads a CONVENTION the render emits, pinned in that file's header: every note element carries `data-note="absent"|"pointer"` and `data-note-keys="<member>|<entity>;..."` (a pointer also `data-note-page`), every non-chart member element carries `data-entity` (`household`, the last four characters of the account id, or `class:<asset class>`); the note-level rule FAILS a note phrase that sits outside every keyed element, so no note can escape it by being unkeyed; (c) three virtual members (`hold.class_rows.ending_value`, `.net_gain`, `.return`) let the foot note name the class-row cells that no contract member holds, so the class half of that note is keyed and never silently skipped; (d) chart 3 (ending value and net additions) points to the Portfolio Value Summary and its members are `pvs.last_12_months.net_additions` and `pvs.last_12_months.ending_value`; the two allocation charts keep their tables (`hold.allocation`, `act.ending_value.account`), which the CVO accepted; (e) round 106's render check stays as it is and still passes against its own recorded render (its record binds immutable files under `fwd21_sample_r106/`); (f) the data cell is NOT re-run: round 107 re-renders the round-106 sample, so the worker's record names that sample's hash.

**fanout:** 1 of 2 chains, cap 8, reason: R107-B is the issuer's own check with no worker. Worker `0.9.0_WK_IRPT_DASHBD~170` (`DB-b-209`, portal_ref `wk-IRPT_DASHBD-169-portal`).

## 110. ROUND 108, WORKSTREAM B (2026-10-14 ~16:0xZ, issuer 2.0.0_SA_COO~D2, on `CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_108_20261014.md` @4d26563910, msg 7729; the CVO graded round 107's `DB107-1-J1` PASS, 6 of 6 acceptance criteria PASS: the 49 Financial default performance report is complete except for the disclosure page, a release gate on Andrew's call a252)

The CTO's two cells are cut as TWO orders on TWO independent chains. The 49F disclosure composition is NOT cut until Andrew names the file (a252). The Inflection render (a sample household through the whole-document rules) is round 109, once these land.

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| 1. The Inflection adapter's first tables: `account_dim` and the household key, from Inflection's silver under Inflection's own key prefixes only (never another firm's prefix, never the Orion master prefix), counts of accounts and households, the schema hash equal to the gold contract's (C-ADAPTERS), a private dry-run table, nothing written to S3 | `DB-b-211` | FWD-2 | LOCAL (reads only; the dry-run table is private) | none | R108-A |
| 2. Two reads that decide Inflection's coverage words (PRD line 294): whether Orion's returns include dividends, measured against one account's transactions; whether Eclipse tax lots are populated (else the lots members carry `NO_LOTS` with plain words) | `DB-b-212` | FWD-2 | LOCAL (reads only) | none | R108-B |

**Decisions inside this decomposition (the issuer's, stated):** (a) the two cells share no file: the adapter cell owns a new module, its tests and its folder; the reads cell owns only its own folder and script; (b) the grant of the S3 reads is by PREFIX, which the order's bounds name: `s3://opal-data-assets/orion/inflection/` and `s3://opal-data-assets/eclipse/inflection/` (LIST and GET only); the Orion master prefix `orion/4698/` is another place and is not granted; the checker refuses any other s3:// literal, any other firm's name and any write-call token in the adapter and the read script; (c) the adapter reuses the SAME Arrow schema as the account_dim contract (round 103's Cottonwood adapter is the pattern), so the schema hash is the contract's by construction and the checker recomputes it from the module and from the dry-run table; (d) the dry-run table is a private parquet whose schema, row count and household count the checker recounts, so the record cannot misstate the counts; (e) the Orion dividend question is answered on ONE account named only by the sha256 of its id, chosen by a deterministic rule, with `NOT_ESTABLISHED` an honest answer and the Eclipse lots answer carrying its plain words when absent; (f) nothing here applies or writes; the `account_dim` apply for any firm needs the upload path and a signed pair (round 105, section 4).

**fanout:** 2 of 2 chains, cap 8, reason: two independent cells with disjoint write sets. Workers `0.9.0_WK_IRPT_DASHBD~171` (`DB-b-211`) and `~172` (`DB-b-212`).

## 111. ROUND 109, WORKSTREAM B (2026-10-14 ~17:2xZ, issuer 2.0.0_SA_COO~D2, on `CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_109_20261014.md` @a80ef4f7c7, msg 7762, and the CTO's ruling on row D2-S34, msg 7760; the CVO's round-108 slug is `ADJUDICATION_v68.md` @963438b352)

The CTO's three cells are cut as ONE issuer direct act (done first), TWO orders in one chain and ONE independent order. FWD-2 and FWD-21 move on the render (cell 2); neither is met by this round.

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| 1. The W171-S4 read gate: enumerate the 4 alien Orion silver objects; another firm's data is a STOP to the CTO, Inflection's own surplus lets the render proceed with the guard state named | `DB-b-213` | FWD-2 | LOCAL (a read) | none | R109-0 (the issuer's direct act; DONE, result below) |
| 2a. The Inflection SAMPLE (data half): one household built in memory from Inflection's own silver by the round-108 adapter, the household return from Orion's client-keyed `fact_performance` with its source, the household ending value, an account return `NO_SOURCE_YET` in plain words, lots `NO_SOURCE_YET` in plain words (the coverage member `NO_LOTS`), the split columns as for 49 Financial; the sample passes the whole-document rule; the guard state named | `DB-b-214` | FWD-2, FWD-21 | LOCAL (reads; the sample is private) | `DB-b-213` | R109-A |
| 2b. The RENDER: that sample through the 49 Financial layout and the whole-document and note-level rules, in the Inflection firm title, with the Inflection words printed; the CVO grades J1 | `DB-b-215` | FWD-2, FWD-21 | LOCAL (portal branch only, never pushed) | `DB-b-214` | R109-A |
| 3. The ACCOUNT-RETURN derivation (the method of the existing daily TWR engine as a pure function, from Orion positions and transactions under Inflection's prefix, labelled Opal-computed) and the TIE-OUT read (accounts aggregated per client against Orion's client return: the gap distribution per window; no tolerance assumed; the CTO rules it on this read); nothing written | `DB-b-216` | FWD-2 | LOCAL (reads; private tables) | none | R109-B |

**The cell-1 result (the issuer's direct act, `deliverables/2.0.0_SA_COO~D2/ALIEN_READ_R109.json`, script `checks/r109/alien_read_r109.py`):** the guard reads FAIL (expected 4997, landed 5001, matched 4997, missing 0, alien 4). The four alien objects are `fact_assets` and `fact_positions` partitions for 2026-08-06 and 2026-09-29: every account in each (948 and 966) is inside Inflection's own account set (0 outside), they sit under `orion/inflection/silver/`, carry `_source` orion and have no bronze object for their dates. They are Inflection's own surplus: NO STOP to the CTO; the render proceeds with the guard state named. The guard's repair is the Orion pipeline owner's.

**Decisions inside this decomposition (the issuer's, stated):** (a) the TWR "existing engine" `account_return_daily.py` is the Schwab firm adapter around a shared method (its header: one adapter per firm, every Schwab code in `sources.json`), bound to Schwab's declared source and S3 readers, so the Inflection cell does NOT edit it or its `sources.json`: it implements the method as a small pure function in a new Inflection adapter (`r_t = (V_t - F_t) / V_(t-1) - 1`, F_t summed over every partition day after t-1 up to t, none when a value is missing), and the checker tests that function against its own independent computation on a synthetic week with a closed day that carries a deposit; the engine file is hashed and must be unchanged at HEAD; (b) the derived table has the account_return_daily contract's schema (same hash) and the label `OPAL_COMPUTED`; it is a private parquet, never written to S3; (c) the tie-out's denominator is every household of the round-108 dry run (320): each has one row per window in a private gaps file (a gap in basis points, or a reason in words), and the checker recounts the bins (under 5, 5 to 25, 25 to 100, 100 or more) from that file; (d) the Inflection sample uses the SAME account_dim adapter and the SAME household rule recomputed by the checker (the lowest sha256 of the household id among households of 2 or more accounts), and the split columns, the fee basis and the disclosure page stay as for 49 Financial; (e) the render check is round 107's clauses with the firm title read from the registry (Inflection Wealth Management), plus the two plain-word sentences and the guard state; (f) account pages for Inflection read the NO_SOURCE_YET words until the CTO rules a tolerance on cell 3's read; no derived account figure is rendered this round.

**fanout:** 2 of 2 chains, cap 8, reason: R109-0 is the issuer's own direct act with no worker; R109-A is two orders for one slot (215 depends on 214); R109-B is independent. Workers `0.9.0_WK_IRPT_DASHBD~173` (`DB-b-214`, then `DB-b-215`, portal_ref `wk-IRPT_DASHBD-170-portal`) and `~174` (`DB-b-216`).

**Amendment 1 to section 111 (issuer 2.0.0_SA_COO~D2, 2026-10-14 ~17:4xZ, on worker row W173-S1, BLOCKING, and the shape rule):** cell `DB-b-214` is amended: (a) the household return stays ABSENT `NO_SOURCE_YET`, as the contract sources every `pvs.<w>.return_cumulative` (no sibling contract carries a household-grain return; returns do not add across accounts), so the table row's "household return from Orion's client-keyed `fact_performance` with its source" is NOT done this round: filling a member the contract sources ABSENT would change what the contract says for every firm and is the CTO's decision (surfaced to the CTO with the round-109 drain-end); my order required a fill the issuer's own shape rule refuses, an issuer error; (b) `as_of` is the newest `fact_positions` date on or before the last date of the served model series (the report is T-1 and every source exists at `as_of`; the first build's as_of was one day past the series and left 33 members SOURCE_BREAK); (c) the criterion `DB109-1-AC1` and its record fields change accordingly (`household_return_note`, `as_of`, `benchmark_data_as_of`, `benchmark_members`). Cell `DB-b-216` is unchanged.

## 112. ROUND 110, WORKSTREAM B (2026-10-14 ~19:2xZ, issuer 2.0.0_SA_COO~D2, on `CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_110_20261014.md` @e0c72e187d, msg 7812; the CVO graded round 109's `DB109-2-J1` FAIL on four counts, `ADJUDICATION_v69.md` @d6fee3fc43; the CTO's ruling: household returns come from Orion's client grain, account returns stay NO_SOURCE_YET until the derivation's tie-out is ruled, and the shared as-of fix and two reads are routed to this project)

The CTO's three cells are cut as ONE issuance: the Inflection render remedy as ONE chain of three orders (contract, sample, render), the shared as-of fix as one order, and the two reads as two orders. FWD-2 and FWD-21 move on the Inflection render; neither is met by this round. Andrew's P1 (the performance reporting tab functional for all clients at all firms, internal 15 November) is the frame.

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| 1a. The CONTRACT 0.5.0: the equivalence map (members that name the same quantity for the same entity: the household ending value in six members, the account ending value in six, so the gain/loss Ending Value and the overview's compare as one figure) and the household return sourced from Orion's client grain for Inflection only (every other firm stays ABSENT); every earlier live criterion still passes | `DB-b-217` | FWD-2, FWD-21 | LOCAL (a contract file in a branch) | none | R110-A |
| 1b. The Inflection SAMPLE v3: each account's own first-data date and window statuses, its own since-inception benchmark (the CVO's count 1), the gain/loss Ending Value filled (count 2), not-spanned benchmark cells in not-spanned words (count 3), the household return from Orion's client grain with its source, the custodian number's real last four as the label (W173-S9) | `DB-b-222` | FWD-2, FWD-21 | LOCAL (reads; the sample is private) | `DB-b-217` | R110-A |
| 1c. The RENDER of that sample: not-spanned words printed, one reason per cell (count 4), the gain/loss Ending Value printed, the real last four after "ending", the plural lot sentence where a note covers several accounts; every page read; the CVO regrades J1 | `DB-b-223` | FWD-2, FWD-21 | LOCAL (portal branch only, never pushed) | `DB-b-222` | R110-A |
| 2. The SHARED AS-OF FIX: a date-only value never shows an invented clock; the helpers `create5pmETDate` and `formatDataAsOfCompact` and the display paths print "as of October 14, 2026"; a clock prints only when the source supplies a real timestamp; tests re-pin the 5 PM cases and add the before-5-PM negative case; one candidate branch, client-facing, Andrew approves | `DB-b-219` | Andrew's P1 (no FWD id) | LOCAL (a branch cut from the last PROD release, never pushed) | none | R110-B |
| 3a. READ: is the Black Diamond holdings file's date the close the holdings reflect, or the pull day? | `DB-b-220` | FWD-2 | LOCAL (a read) | none | R110-C |
| 3b. READ: Cottonwood's `holdings_performance_daily`: producer, channel, why it has no schedule (DESIRED vs APPLIED), input frontier, what a scheduled fire needs, who writes Cottonwood's irpt holdings | `DB-b-221` | FWD-2 | LOCAL (a read; nothing written to AWS) | none | R110-D |

**Decisions inside this decomposition (the issuer's, stated):** (a) the equivalence map is two classes, `ENDING_VALUE_HOUSEHOLD` (`pvs.qtd|ytd|last_12_months|since_inception.ending_value`, `hold.ending_value`, `act.ending_value.household`) and `ENDING_VALUE_ACCOUNT` (`avs.*.ending_value` over the four windows, `glr.ending_value`, `act.ending_value.account`); each is one quantity at one entity (the ending value as of the report date), and the rule is: all printed or all absent, agreeing where printed; the checker compares through the contract's `equivalences` list, with a planted pair as its control; (b) the household return is the contract's `firm_sources.inflection` (Orion `fact_performance`, client grain, newest partition only, percent points, claim "reported by the platform"), not a new sibling contract: the member's `source` stays ABSENT for every other firm, so no other firm's figure moves; the windows Orion does not carry stay absent with a reason; (c) `check_sample_shape_k` of the round-105 check gains an optional `firm` argument (the ABSENT-source refusal skips a member the contract sources for that firm), and the round-109 sample check accepts the 0.4.3 contract bytes it built against, so the earlier criteria keep reading PASS on their own records; DB-b-217 re-runs the 14 earlier live criteria before and after (DB104-2-AC1 and DB104-3-AC1 pin the contract at 0.4.1 and have read FAIL since the 0.4.2 bump: superseded, named here, not a regression of this round); (d) the account label is the custodian number's real last four characters as stored (the CTO's rule), and the checker refuses the ordinal; the private sample may hold real last fours (private folder, counts and words only in the repo); (e) the as-of fix is cut from the last PROD release and never from DEV, and the issuer (not the worker) names the candidate branch `cand/dell2/<slug>` at the worker's tip and registers the approval row once the worker reports; the exact string Andrew saw ("as of 5 PM ET, October 14") is produced by no formatter on PROD (the closest is "October 14th, 2026, 5:00p ET"), so the order fixes every display path that prints a 5 PM clock for a date-only value and the CTO is told which page showed it only if the worker finds one; (f) the two reads use independent evidence only (a read of the Black Diamond date against a close series that does not derive from the file; an unreadable schedule plane is recorded as unread, never as zero); (g) the CVO's reading (b) (two accounts print a zero ending value) is not fixed: the render report counts such accounts and the CVO regrades.

**fanout:** 4 of 4 chains, cap 8, portal_ref: `wk-IRPT_DASHBD-173-portal` for slot ~175 (the branch carrying round 109's Inflection render, local) and `6a5926fc` (the last PROD release) for slot ~176, reason: R110-A is three orders for one slot (222 depends on 217, 223 on 222); R110-B, R110-C and R110-D are independent with disjoint write sets. Workers `0.9.0_WK_IRPT_DASHBD~175` (`DB-b-217`, then `DB-b-222`, then `DB-b-223`), `~176` (`DB-b-219`), `~177` (`DB-b-220`) and `~178` (`DB-b-221`).
