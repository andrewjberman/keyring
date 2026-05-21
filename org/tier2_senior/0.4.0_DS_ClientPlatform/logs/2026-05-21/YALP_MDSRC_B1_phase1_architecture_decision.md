# YALP_MDSRC.B1 Phase 1 — architecture decision + build plan — 2026-05-21

**Agent:** 0.4.0_DS_ClientPlatform (base lane)
**TO:** YALP_MDSRC.B1.ds-smartx-rest-model-portfolio-performance-pull
**Branch:** CLOUD
**Status:** Phase 1 IN PROGRESS — GO received (CTO+COO converged ruling: Path A, standalone sibling). Producer read, comp mandate run, architecture decided. Build is the next work block.

## Ruling received (COO 2026-05-21 00:51Z)

Path A — hybrid by cadence. SmartX `performance/models/performance` feeds the 7
monthly+ periods (1M/MTD/QTD/1Q/YTD/1Y/SI) of `model_portfolio_benchmarks.json`
`model` field; `model.pkl`/yang retained for the daily periods (1D/WTD) + the daily
`model_portfolio_timeseries.json`. MANDATORY Q8 labeling — the cadence-source split
must be explicit in the artifact. SXPL_RESTIN.002 gate dissolved — B1 is a standalone
sibling; reuse the SmartX ROPC-JWT auth as CODE reuse (import `mint_token`), not a
delivery dependency. Portal-wiring still gated on Andrew Q8 (build + validate only).

## Producer characterized

`infra/aws/lambda/v2_portal/yang_pipeline/portfolios/yang-model-portfolio-benchmarks/lambda_function.py`
— runs in the YangDataPipeline Step Functions. Loads `data.pkl -> return_daily`,
computes per-(model, period) `model` / `index_benchmark` / `etf_benchmark` returns
via `calculate_period_returns`, writes `model_portfolio_benchmarks.json` +
`benchmark_returns.json` + `model_portfolio_timeseries.json`.

NOTE — discrepancy flagged: the B1 TO / PRD §5.2 frame the `model` column as
`model.pkl`-sourced; the actual producer docstring + code source the `model` returns
from `data.pkl -> return_daily` (the "Term" index_names), not `model.pkl`. Does not
change B1 (Path A swaps the monthly+ `model` values to SmartX regardless of the prior
yang source) — flagged for the record / the v0.4 amendment.

## Compiler mandate (Phase 1)

| Run | Result |
|-----|--------|
| `comp-iam service yang-model-portfolio-benchmarks` | IAM role `yang-pipeline-lambda-role`; 3 ops (s3:GetObject x2, s3:PutObject) all GRANTED. **No `secretsmanager:GetSecretValue`** — relevant to the architecture choice below. |
| `comp-pipescript io` | N/A — yang Lambda is not a gold-tier comp-pipescript node (BD-gold IDs only); producer read directly. |

## Architecture decision (the TO's "split vs dual-input" call — DECIDED)

**Architecture A — standalone SmartX-pull sibling + dual-input yang producer.**

- A standalone SmartX-pull component (the CTO-ruled "sibling") pulls
  `performance.smartxadvisory.com/models/performance` monthly for the 5 portal
  models, computes the 7 monthly+ period model returns, and writes an S3 sidecar
  artifact (proposed `s3://opal-data-portal-v2/json/benchmarks/_smartx_model_monthly.json`).
  It owns the SmartX ROPC-JWT auth (imports `mint_token`, reads `smartx/credentials/*`).
- `yang-model-portfolio-benchmarks` becomes a DUAL-INPUT producer: reads `data.pkl`
  (as today) + the SmartX sidecar; for the 7 monthly+ periods it uses the sidecar's
  SmartX `model` value, for 1D/WTD it keeps the yang value. Each period in the
  artifact carries an explicit `model_source` label (`smartx_realized` |
  `yang_design`) — the MANDATORY Q8 cadence-source split.

**Why A over inline-in-yang (B):** CTO ruled "standalone sibling, not a ride."
Architecture A keeps the SmartX auth + internet egress in the sibling; the yang
producer only adds an `s3:GetObject` on the sidecar — already GRANTED on
`yang-pipeline-lambda-role`, so NO iam.tf change to the yang role and no VPC/egress
change to the yang Lambda. Inline-in-yang (B) would need Secrets Manager perm +
egress on the yang role and couple the yang pipeline to SmartX availability — the
opposite of "standalone sibling."

## Build plan (next work block)

1. Build the standalone SmartX-pull sibling — pulls `performance/models/performance`
   for the 5 models, computes the 7 monthly+ period returns, writes the sidecar.
   Reuses `mint_token` (code reuse). Decide Lambda-vs-scheduled-script + cadence.
2. Modify `yang-model-portfolio-benchmarks` to the dual-input shape + `model_source`
   labels.
3. comp-iam re-check on the sibling (new Secrets Manager + egress); deploy via AE
   (Lambda terraform) per CLAUDE.md Rule for Lambda code.
4. Verify the sidecar + the dual-sourced artifact; RAVC2 to COO CC CTO. Portal-wiring
   held for Andrew Q8.

## Next Steps

| Recipient | Item |
|-----------|------|
| **DS Base (self)** | Build the standalone SmartX-pull sibling + the dual-input yang producer modification per Architecture A. |
| **COO 2.0.0** | Architecture A decided + documented (per the TO's "make + document the call"). Will surface the AE Lambda-deploy coordination + RAVC2 on completion. |
