# 0.6.0_AE_PartnerETL — 06-17 cot platinum-freeze chain-state determination (DS-flagged, COO-dispatched)
**archetype:** DIAGNOSE

## Window
06-17 ~1450Z. DS (0.4.0_DS) flagged (144943Z) + COO dispatched (145149Z item 2): cot platinum served
artifacts mtime-frozen 2026-06-09 while silver pull advances daily. DETERMINE (a) intentional snapshot-
advance gating vs (b) gold-trigger gap. Read-only, no test gold-run (compute discipline). In-lane: the cot
bronze->silver->gold EventBridge/SSM state machine = AE infra (gold scripts stay DS lane). RAVC2 COO, CC CTO.

## Determination: (b) BROKEN silver->gold trigger, causally DOWNSTREAM of the BD snapshot freeze (end-to-end stale)
Verified on live state:
- cot-silver-complete EventBridge rule (ENABLED) event pattern = S3 Object Created, suffix "silver_complete.json",
  bucket opal-data-cot -> target Lambda cot-bd-session-trigger (gold-run branch). (cot-bronze-complete is the
  sibling: suffix _BRONZE_COMPLETE.json -> same Lambda silver branch; that one DOES fire -> silver runs nightly.)
- silver_complete.json has NEVER been emitted: no silver/{date}/ structure exists at all (incl. 6/9). The 6/9
  platinum was the INITIAL manual buildout gold run, not event-triggered. The event-driven silver->gold chain
  has never fired in production.
- The silver-run SSM doc opal-cot-silver-run DOES call `cot_silver_merge.py --finalize` nightly (emit IS wired):
    cot_silver_merge.py --table transactions && allocations && realized && unrealized && --finalize
  BUT emit_silver_sentinel writes silver_complete.json only when EVERY TABLE_CONFIG table has
  silver/{table}/{run_date}.parquet. The CurrentDay snapshot tables write their BD-STAMPED date (allocations 6/5,
  unrealized 6/9, holdings 6/8), NOT {run_date} -> the all-tables-{run_date} gate can never pass -> sentinel
  suppressed (WARN) -> gold never triggers.
- COMPOUNDING BUG (separate): holdings is MISSING entirely from the silver-run chain (only transactions/
  allocations/realized/unrealized + finalize). cot_holdings.parquet + cot_incremental_manifest_holdings.json
  frozen at the 6/9 17:59 initial load. holdings is the COT-AUA source of truth.

## Causality (full picture for Andrew's COT-feed call)
BD "Current Day" snapshot frozen (6/5-6/9) -> silver snapshot tables pinned to BD-stamped date != run_date ->
emit_silver_sentinel all-tables-{run_date} gate fails -> silver_complete.json never emitted -> cot-silver-complete
never fires -> gold-run never invoked -> platinum frozen 6/9. COT served data is ~8d stale END-TO-END
(BD source -> bronze -> silver-snapshot -> gold/platinum). NOT intentional (a): no explicit "skip gold on
unchanged snapshot" logic exists; the sentinel simply cannot emit while snapshot tables are date-stale.

## Fix (cross-lane; NOT executed -- read-only determination per COO; gated on Andrew's BD expected-vs-stall call)
- The chain is structurally fragile: assumes CurrentDay tables advance daily (BD-stamped == run_date).
- AE (mine, infra): SSM doc opal-cot-silver-run -- add `--table holdings` to the chain.
- DS (cot_silver_merge.py): emit_silver_sentinel gate on each table's LATEST/BD-stamped partition, not strictly
  {run_date}.parquet -> sentinel emits when CurrentDay tables carry BD-stamped != run_date. This is the real unblock.
- Sequencing: BD-expected -> platinum-frozen ~correct (no new data) but the fix lets the chain auto-resume on
  unfreeze; BD-stalled -> BD-fix priority + this fix auto-recovers. Recommended COO hold behind Andrew's call.

## Evidence (live)
- platinum/firm/{header_metrics,timeseries_chart,timeseries_overview,cumulative_chart,dashboard,mix_summary,
  clients-tab-slim}.json + gold/platinum/firm/{cohort_a_summary,cash_coverage_summary}.json all mtime 2026-06-09 18:26-27.
- silver/ has only table prefixes (no {date}/) + compacted parquets: cot_holdings.parquet/cot_transactions.parquet/
  cot_allocations.parquet frozen 6/9; incremental manifests for txn/alloc/realized/unrealized advance to 06-16 22:0x,
  holdings manifest frozen 6/9.
- EventBridge: cot-bd-session-daily / cot-bronze-complete / cot-session-complete / cot-silver-complete all ENABLED.

## Compiler Tools
No comp-* tool run. Why (gate): read-only live-state chain diagnosis on opal-data-cot (separate firm; comp-pipescript
is bd-only) via aws s3 ls/cp/head-object, aws events describe-rule/list-targets-by-rule, aws ssm get-document,
aws lambda get-function-configuration, aws cloudwatch get-metric-statistics -- no code/infra change, no comp trigger.

## MCP traffic
- Inbound: DS platinum-freeze flag (144943Z) + COO GO (145149Z: GLDINC SS4c + cot-platinum determine).
- Outbound: ACK->DS (145035Z); RAVC2 determination->COO (145519Z, +GLDINC SS4c ACK) + cross-lane fix note->DS (145530Z).

## Blockers / Next
- None blocking. cot-platinum fix held behind Andrew's BD expected-vs-stall call (cross-lane AE+DS when GO'd).
- NEXT: ADHC_GLDINC.SS4c (COO GO 84e57c68a) -- periodic-oracle re-validation; pull CVO cert cvo_1330Z + the 3 TO unknown-unknowns.
