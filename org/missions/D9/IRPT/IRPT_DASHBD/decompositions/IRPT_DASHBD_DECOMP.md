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
