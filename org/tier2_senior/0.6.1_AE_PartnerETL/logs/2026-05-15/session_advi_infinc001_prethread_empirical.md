# Session Log — ADVI_INFINC-001 Pre-Thread Empirical (silver/transactions dual-writer)
**Agent:** 0.6.1_AE_PartnerETL
**Date:** 2026-05-15
**Trigger:** CTO inbox message — data-hazard-urgent pre-thread fact-find

## Summary

CTO requested a fast S3 empirical to set the opening of thread ADVI_INFINC-001:
is the `s3://opal-data-inf/silver/transactions/` dual-writer hazard ACTIVE or LATENT?

VERDICT: **ACTIVE.** Partitions alternate writer/schema; writers do not share a key
convention; the Lambda will clobber the gold-chain full-history file on a D+1 lag.

## Empirical

S3 listing `silver/transactions/` last 8 partitions + downloaded/inspected 5:

| Partition | Rows | Cols | Date col | Span | Writer |
|-----------|------|------|----------|------|--------|
| 2026-05-15.parquet | 1,296,229 | 37 | transDate | 2020-05-26..2026-05-14 | #2 gold-chain REST (06:14Z, 32.5MB) |
| 2026-05-14.parquet | 4,501 | 31 | trans_date | NaT | #3 inf-api-txn Lambda (13:00Z) |
| 2026-05-13.parquet | 20,212 | 31 | trans_date | NaT | #3 inf-api-txn Lambda (13:00Z) |
| 2026-05-11.parquet | 138 | 31 | trans_date | NaT | #3 inf-api-txn Lambda (13:00Z) |
| 2026-05-08.parquet | 437 | 43 | trans_date | — | #3 older schema variant (15:41Z batch) |

Findings:
1. Schemas DISJOINT — writer #2 camelCase (`transDate`/`accountId`/`transAmount`/`noUnits`/`transTypeId`); writer #3 snake_case (`trans_date`/`account_id`/`trans_amount`/`units`), no equiv for assetId/transTypeId. Consumer KeyErrors on one or the other.
2. Third schema variant — 05-08 is 43 cols; Lambda's own schema drifted 43->31.
3. Scheduled clobber — writer #2 writes one `{run_date}.parquet`=full history; writer #3 writes per-date `{D}.parquet` D+1 13:00. Lambda overwrites today's 32.5MB/1.3M-row snapshot tomorrow.
4. Latent bug — `trans_date` 100% NaT on all writer-#3 partitions.

## INFINGE.005b Intent Finding

Read closed TO `ADVI_INFINGE.005b.txn-v2-lambda-migration.md`. "inf-api-txn owns
TXN end-to-end" decommissioned only the ORCHESTRATOR transactions DimSpec (writer #1)
via the REPLACE pattern on `bronze/orion-api/{date}/transactions.csv`. 005b never
references `convert_transactions_to_silver.py` / gold-chain `INF_API_SILVER_TXN`
(writer #2). Root cause = scope gap: no project held all 3 writers in view. 005b
also spec'd silver target `silver/api_dims/transactions/{date}/data.parquet` — the
Lambda is now writing the contested `silver/transactions/{date}.parquet` instead.

## RAVC2 Sent
- CTO: S3 empirical (verdict ACTIVE) + INFINGE.005b intent follow-up
- COO: CC of both

## Compiler Tools
None run — this was a read-only S3 fact-find (s3api list + parquet inspect), no
script/Lambda/portal edit. comp-* tools not applicable to an empirical pull.

## Post-Empirical: COO ACK + State Correction

COO ACK'd (20260515T145343Z). Empirical corroborates topology for the 4th time.
**Andrew ruled NO thread** — ADVI_INFINC-001 will not be created. Path is:
CTO writes transaction-silver consolidation PRD -> COO decomposes -> scoped TO
lands in my task_orders/. Watch task_orders/, not a thread.

Clobber confirmed steady-state (not a cliff) — txn_cache_reader source-selects
latest canonical partition by mtime+col-check, shielded consumers land on fresh
gold-chain write. No interim action.

## My Lane Prep (read-only — feeds the inbound TO)

**Scope:** inf-api-txn Lambda restructure — stop its silver/transactions write;
preserve/reroute the aggregator-quorum sentinel. Design direction: REST-only
single canonical writer (CSV-unique fields have zero consumers, swept).
Decommission-not-rewire. Cleanest option to weigh: move sentinel emission onto
gold-chain INF_API_SILVER_TXN + retire inf-api-txn entirely.

**`infra/aws/lambda/inf-pipeline/inf-api-txn/lambda_function.py`** — 3 steps:
- Step 1: `pull_inflection_transactions_v2.main()` -> `bronze/orion-api/{date}/transactions.csv`
- Step 2: `build_transactions(snap)` -> `_s3.put_object` `silver/transactions/{date}.parquet` (lines 92-108) — THIS is writer #3, the contested write to kill.
- Step 3: sentinel `_s3.put_object` `silver/_silver_complete/{date}/transactions.json` (lines 110-126) — body: status/snapshot_date/lambda/rows/silver_key/completed_at. THIS must be preserved/rerouted.

**Sentinel consumer — `infra/aws/lambda/inf-silver-aggregator/lambda_function.py`:**
- S3 ObjectCreated trigger on `silver/_silver_complete/` prefix.
- Quorum = 9 canonical dims (`DIM_LIST_DEFAULT`): tax, performance, billing,
  **transactions**, accounts_v2, unified_account_dim, representatives, assets_v2,
  positions_daily. Sentinel path `silver/_silver_complete/{date}/{dim}.json`.
- Idempotency marker `_AGGREGATOR_FIRED.json` on first quorum hit.
- => If inf-api-txn is retired with no replacement sentinel writer, the
  `transactions` dim never reports -> quorum stalls at 8/9 -> aggregator never
  fires. The sentinel emission CANNOT just be deleted; it must move.

**Design open question for the TO:** if the `transactions` sentinel moves onto
gold-chain INF_API_SILVER_TXN, confirm INF_API_SILVER_TXN runs BEFORE the
aggregator quorum (silver tier) and is not itself gated by the aggregator —
otherwise circular. To verify when TO lands.

## TO-4 Sub-Question SETTLED (CTO asked, answered read-only)

CTO + COO both ACCEPTED the two RAVC2s. CTO posed the TO-4 design sub-question:
"was the Lambda ever correctly writing silver/api_dims/transactions/, and does
anything read that path?" — decides retire-entirely vs point-back-to-spec.

Probe:
- `aws s3 ls s3://opal-data-inf/silver/api_dims/transactions/ --recursive` => EMPTY.
  Prefix never existed. silver/api_dims/ has accounts_v2/assets/billing/performance/
  positions_mv/representatives/tax_*/household*/activity — NO transactions/.
- `grep -rln "api_dims/transactions"` data/ + infra/aws/lambda/ => ZERO hits.

CONCLUSION: inf-api-txn NEVER wrote the 005b-spec'd silver/api_dims/transactions/
path. Dead spec, never implemented. Lambda wrote the contested
silver/transactions/{date}.parquet from day one. => RETIRE-ENTIRELY (no artifact
to point back to). Confirms COO lean.

TO-4 shape designed (fed to CTO/COO for PRD):
1. Kill Lambda silver-write (lambda_function.py:92-108) = removes writer #3.
2. Move sentinel silver/_silver_complete/{date}/transactions.json emission onto
   gold-chain INF_API_SILVER_TXN (aggregator needs all 9 dims or stalls 8/9).
3. Retire inf-api-txn Lambda + EventBridge cron + IAM role.
4. Verify bronze consumers before killing the bronze pull (TO acceptance step).
Risk to settle in-TO: INF_API_SILVER_TXN must run pre-aggregator, not be
aggregator-gated, else sentinel move is circular.

## BRANCH FLIP — Andrew chose AMALGAMATE (CTO 20260515T150140Z)

Andrew flipped the gate AFTER my retire-entirely design: verbatim "anything that
is unique we want to keep because may use it in the future." => AMALGAMATE, not
REST-only. Amalgamated silver/transactions = REST spine + ALL Custom-Report-unique
columns left-joined by txn id.

TO-4 REVISED (supersedes retire-entirely design above):
- KEEP Step 1 bronze pull — now REQUIRED join enrichment source. Not decommissioned.
- REMOVE Step 2 only (lambda_function.py:92-108 silver-write) — kills writer #3.
- KEEP Step 3 sentinel ON THE LAMBDA — no move to gold chain. Semantics shift
  "txn silver done" -> "txn bronze done". Circular-dep risk now MOOT.
- inf-api-txn TRIMMED (bronze-pull + sentinel), NOT retired. Cron + IAM stay.

Implementation detail flagged to CTO+COO: Step 3 sentinel body (lines 114-121)
uses `rows`/`silver_key` from removed Step 2 — must be revised to bronze-derived
row count + drop/repoint silver_key. Design exact body in the TO.

Relayed branch flip to COO (150251Z) — COO's 150215Z ACK predated the flip and
was still decomposing retire-entirely; corrected before COO authored a wrong TO.

## Status
Pre-thread empirical closed. State corrected (no thread; amalgamate branch).
TO-4 = trim inf-api-txn. CTO+COO both informed + branch-flip relayed to COO.
Standing by for amalgamate-final PRD -> decomposed TO-4 in task_orders/.
