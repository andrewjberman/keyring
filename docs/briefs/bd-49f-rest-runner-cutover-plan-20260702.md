# ADVI_BDAPIMIG.P1 — bd 49F REST-runner cutover plan (retire the dead scrape path)

**Author:** 0.6.0_AE_PartnerETL | **Date:** 2026-07-02 | **Project:** ADVI_BDAPIMIG.P1 (WS-2a bd-side)
**Status:** PLAN — CTO arch-gate (GATE-1) before the served-critical cron cutover; DS + 0.7.0~A cross-lane asks below.
**Authority:** Andrew-direct sovereign RATIFIED 2026-07-02T182117Z ("we absolutely should be using the cookie-REST path") via COO GO (182053Z/182508Z). Top-parallel.

## Diagnosis (grounded — why the freeze recurred despite the interim being built)

The Phase-1 interim (A keepalive / B bd-49f-runner / C freshness-probe) SHIPPED + was CVO-accepted
2026-06-25 (tags bd-v2.33/34/35). But **the CUTOVER never happened** — grounded live 2026-07-02:
- **`bd-49f-runner-daily` EventBridge cron = DISABLED** (`cron(0 2 * * ? *)`). The working cookie-REST
  runner never runs. (Lambda bd-49f-runner itself = Active, last-mod 06-25.)
- **All 6 scrape crons = ENABLED + primary:** bd-{allocation,transaction,realized,unrealized,fees,
  asset}-pipeline-trigger (`cron 21:38-22:15 UTC MON-FRI`) -> SSM -> EC2 Playwright runner.ts UI-export
  login, which is DEAD (SS&C email-OTP MFA 30s nav-timeout to bd3). They boot, fail login, land nothing,
  and their SSM exit-0 masks the failure (false-advance).

So the dead scrape path stayed primary; the durable runner stayed dark. Enabling the runner + retiring
the scrapes is the never-completed cutover.

## Two gaps that would break a naive cutover (must fix BEFORE enabling the runner)

1. **transactions 14-day window ERRORs on BD.** cot_bronze_ingest `TABLE_DATE_MODE[transactions]=(Custom,14)`.
   Grounded 2026-07-02: a 14-day txn run returns DataMining `status=Error` (2x); a 3-day window COMPLETES.
   The heavy 14d restatement query exceeds BD's limit. -> the runner's txn pull would FAIL every night.
   **FIX (DS lane — cot_bronze_ingest.py is DS-owned shared code): chunk the txn restatement window into
   <=3-day sub-pulls** (e.g. 5x rolling 3-day) so the full 14d restatement coverage is preserved without
   the heavy-query error. Firm-agnostic (helps cot too). Also applies to `realized` if it grows.
2. **txn/realized/unrealized silver has NO auto-trigger.** opal-data-bd S3 notifications = only
   `ProcessAllocationFiles` (allocations xlsx -> silver) + `GoldLayerPricesTrigger` (silver/prices -> gold).
   txn/realized/unrealized silver was produced by the SCRAPE SSM job's INLINE merge. The runner (B) lands
   BRONZE only. Disabling the scrapes strands those 3 tables' silver. **FIX (DS lane + AE infra): wire the
   bronze-complete -> silver trigger** — cot_bronze_ingest already emits `bronze/{date}/_BRONZE_COMPLETE.json`
   on all-table success; add an S3/EventBridge trigger on that sentinel -> a silver-merge invocation that runs
   merge-daily-incremental.py for all 4 tables (the cot pattern). (AE builds the trigger infra; DS owns the
   merge logic + confirms zero-change ingest.)

## Cutover sequence (no-strand, per COO "prove durable BEFORE retire")

1. **[DS]** (a) chunk the txn window in cot_bronze_ingest; (b) wire/confirm the bronze-complete->silver trigger
   for all 4 tables. Re-upload the shared script to opal-data-bd/code/bronze/ + opal-data-cot/code/bronze/.
2. **[AE / me]** ENABLE `bd-49f-runner-daily` (Terraform, `safe-apply`) — runs in PARALLEL with the (failing)
   scrapes. NO double-write risk: the scrapes fail login and land nothing, so forwardfill_v2/{table} has a
   single writer (the runner). Time the runner ahead of the bd silver+gold stage.
3. **[AE / me + CVO]** prove N nightlies durable: `comp-freshness chain bd` = PASS on the SCHEDULED run
   (not manual), no manual re-auth (cookie auto-remints via 0.7.0~A's i-0fa1846f box @00:00Z). C's per-table
   absence alarm egress-verified against the runner path.
4. **[0.7.0~A LEADS]** after N proven, RETIRE the scrape path: disable the 6 pipeline-trigger crons + decommission
   the EC2 scrape boxes (bd-allocations/transactions/fees/assets) + update EC2_MANIFEST.json. Destructive =
   separate GO. Per-table, no double-write.

## Folded bd follow-ups (WS-2 durable scope, per COO)

- transactions 14d chunking = gap #1 above (this cutover's blocker).
- fees frozen by same dead login BUT separate infra (bronze/fees/, Fees_OpalCapital_Daily template, NOT in
  cot_bronze_ingest TABLE_QUERY_TYPE) -> needs its own REST template + a bd-49f-runner fees leg (or a sibling).
- D_00.portal_aggregates.py:748-749 nna period keyed off run-date not data_as_of -> DS finding (routed 162632Z).
- D_00f advisor_nna_canonical writes ~13min AFTER D_04 header (transient header-fresh/advisor-stale window) ->
  ordering, non-blocking.

## Lane split (Andrew/COO)
- **AE (me):** the REST-ingest pull PATH — runner cron enable/timing, the bronze->silver trigger INFRA, the
  per-table alarm coverage, the parallel-run verify. RAVC CTO (GATE-1) on the productionize commit.
- **DS (0.4.0):** cot_bronze_ingest txn-chunk + the silver merge/trigger logic + zero-change confirm.
- **0.7.0~A:** cookie/login-box durability (i-0fa1846f) + LEADS the scrape-box retire (after N-nightly proof).

## Compiler tools (mandate)
comp-blast cot_bronze_ingest (before the DS script change); comp-iam service bd-49f-runner (SM get + s3 put
opal-data-bd) + comp-iam gaps after any iam.tf; comp-pipescript deployed before enable; comp-freshness chain bd
as standing nightly-health evidence.
