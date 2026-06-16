# SEAMS — 2026-06-16 session integration deep-dive (NFRA_GCONTR load + YANG_SITTW.TO-4 + doc-sync + §5)
**archetype:** VALIDATE

Five seams shipped this session. Ground-truth re-checked against LIVE/DEPLOYED/SERVED state at ~1955Z
(StaticTable read of live Iceberg, served S3 objects, deployed Lambda CodeSha256, live EventBridge rule,
current portal/src). Not from in-session memory.

---

## SEAM 1: derive_runner --load-contracts (fe645e103) -> globgrph.graph_contracts  (scale: MESO)
**Side A:** in-VPC Fargate `--stamp-ratified peers,aum` load. **Side B:** graph_contracts Iceberg table (Nessie main).
**Boundary:** append peers+aum rows, ratified_at = real Nessie hash; benchmark SKIP (already-present); period_defs intact.
**Contract source:** CVO YAML (org/tier1_exec/3.0.0_SA_CVO/contracts/graph_contracts.yaml) + COO combined GO.

| Axis | Verdict | Evidence | Delta |
|---|---|---|---|
| MECHANICAL | PASS | live StaticTable (contract_engine, status ok): 3 rows; benchmark SKIPPED (ratified_at 6f21c75ca + pd=11 UNCHANGED); peers+aum appended | - |
| DECLARATIVE | PASS | ALL 3 rows placeholder_pin=FALSE — ratified_at is a real hash (a7bc0aed/6f21c75ca), NOT 'PENDING-CTO-COO-SIGNOFF'. The fe645e103 prefix-gate's claim ("recognizes PENDING-* + stamps real hash") is true in the live row | believed-pre-fix: exact-gate would have stamped the placeholder; live: real hash |
| SEMANTIC | PASS | peers pd=9 + aum pd=4 keys byte-match the CVO YAML (writer yang-pipeline-lambda-role / smartx-ingestion-lambda-role correct); CVO INDEPENDENTLY byte-verified GREEN vs live table | - |
**Verdict: SOUND.** The dry-run write-count discriminator (write=0 expected) caught a stale image BEFORE any write — no bogus pin ever landed.

## SEAM 2: opal-market-overview-tiered-generator -> all-returns.json -> FE (PerformanceHeatMap/ExecutiveSummary)  (scale: MACRO)
**Boundary:** additive `TTW` key in period_returns (decimal); FE ALL_PERIODS whitelist key='TTW'.

| Axis | Verdict | Evidence | Delta |
|---|---|---|---|
| MECHANICAL (producer->artifact) | PASS | deployed CodeSha256=jfjSJDQ... MATCHES my zip; served all-returns.json mtime 19:09:48Z, TTW present 71/71 tickers | - |
| MECHANICAL (artifact->FE) | PASS (DEV) | PerformanceHeatMap.tsx:32 + ExecutiveSummary.tsx:72 ALL_PERIODS include 'TTW' (key matches producer exactly); portal on DEV | PROD promote pending (DT) |
| SEMANTIC | PASS | served TTW == independent DynamoDB trailing-10-session calc (5/5, 0 mismatch); existing periods byte-unchanged (Phase-2 old-vs-new); §5 trap avoided (trading-day-counted, NOT PERIOD_CALENDAR_DAYS) | - |
**Verdict: SOUND on DEV.** Residual: DEV->PROD promote (DT lane), producer-live-first satisfied.

## SEAM 3: yang-model-portfolio-benchmarks -> model_portfolio_benchmarks.json + benchmark_returns.json -> FE (BenchmarkHeatmap/ReturnVolatilityScatter)  (scale: MACRO)
**Boundary:** additive `TTW` (percent) {model+index+ETF + index_spread/etf_spread + 3 vols}; FE ALL_PERIODS key='TTW'.

| Axis | Verdict | Evidence | Delta |
|---|---|---|---|
| MECHANICAL (producer->artifact) | PASS | deployed CodeSha256=DLYgGbEN... MATCHES my zip; served model_pb + benchmark_returns mtime 19:14:38-39Z, TTW in periods array + every model | - |
| MECHANICAL (artifact->FE) | PASS (DEV) | BenchmarkHeatmap.tsx:54 + ReturnVolatilityScatter.tsx:49 now include 'TTW' (DE-B commit 700ec9b4 on DEV); key matches producer | PROD promote pending (DT) |
| SEMANTIC | PASS | served TTW == data.pkl trailing-10-session recompute (15/15 legs + 5/5 index_spread, 0 mismatch); etf_returns.json untouched as scoped; existing periods intact | - |
**Verdict: SOUND on DEV.** Residual: DEV->PROD promote.

## SEAM 4: §5 cross-pod shared-computation (TO-2 market-overview TTW <-> TO-3 model-portfolio TTW)  (scale: MESO, SEMANTIC)
**Boundary:** the §5 binding — one TTW definition (10 trading sessions, TOTAL-return) IDENTICAL across both pods.

| Axis | Verdict | Evidence | Delta |
|---|---|---|---|
| SEMANTIC | PASS | BOTH producers compound a TOTAL-return daily field. TO-3 verified on its OWN merits (not by analogy): data.pkl return_daily `return` col is total (MSCI ACWI +1.006pp div gap); .X_BMK tracks the TR-blend of constituents within 0.02pp vs price-blend 0.12-0.57pp. -> a dividend-payer on both pages agrees | - |
**Verdict: SOUND.** Residual: model/.X_ETF legs not constituent-testable (constituents absent from return_daily) -> routed to CVO BMKAUD value-check lane (non-gating; within-page-consistent + cross-page-moot per 0.4.0_DE).

## SEAM 5: infra docs (AWS_INFRASTRUCTURE_MANIFEST + deploy.sh) -> live infrastructure-monitor-daily rule  (scale: MICRO, DECLARATIVE)
**Boundary:** the recorded cron vs the live EventBridge schedule.

| Axis | Verdict | Evidence | Delta |
|---|---|---|---|
| DECLARATIVE | PASS | live rule ScheduleExpression=cron(0 13 ? * MON-FRI *) ENABLED; docs synced to cron(0 13) at c1148c100 (verified against live BEFORE editing) -> record == territory | was: docs said cron(0 14) (stale); now parity |
**Verdict: SOUND.** Knowledge parity restored (CVO authored, owned-paths routed to my lane, I committed).

---

## Knowledge-parity deltas corrected this session
- graph_contracts ratified_at: a placeholder-as-hash defect was PREVENTED at the loader (fe645e103) -> live rows carry real hashes (no parity gap shipped).
- infra-monitor schedule doc 14->13 UTC drift CLOSED (c1148c100).
- Banked: the globgrph CodeBuild-from-S3-zip staleness gotcha + the Yang return_daily total-return basis (2 memories) -> fabric knowledge parity on two non-obvious facts.

## Overall verdict
All 5 seams SOUND on all evaluated axes against live ground truth. Producer/load/doc legs fully landed +
verified; the only open residuals are owned-by-others and non-gating: (1) the TO-4 FE DEV->PROD promote
(DT, producer-live-first satisfied), (2) the model/.X_ETF deep-value basis (CVO BMKAUD lane). No broken or
UNVERIFIED seam on my side.

## Compiler Tools
Live-state sweep via pyiceberg/boto3 direct reads (StaticTable, get_object, get_function_configuration,
describe-rule) + portal grep — the sharpest ground-truth for each axis (deployed artifact, not source).
Session deploy-time comp-* runs (comp-iam/comp-blast/build-and-upload/safe-apply, dry-run discriminator)
are in logs 8fa2d9e0b + the GCONTR ledger 9e098c2a5.
