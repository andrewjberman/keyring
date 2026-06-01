# Benchmark / Peers — Yang-Source-of-Truth Audit (Andrew-direct, 2026-06-01)

**Owner:** 1.0.0_SA_CTO (framework + consolidation) · **Drive:** 2.0.0_SA_COO ·
**Independent verify:** 3.0.0_SA_CVO
**Status:** OPEN — quarantine-first, full-team. Supersedes routine work for the
benchmark/peers data surfaces until CVO sign-off.

## Trigger
Andrew-direct 2026-06-01. Symptoms on the Model-Portfolios portal tabs:
- **Benchmark tab:** 1M numbers BROKEN, 1Q numbers SUSPECT.
- **Peers tab:** UST model shows NO 1M peers data.
Andrew sought a first revert via 0.4.0_DS base (commit 80224d674) **but there
may be others** — this audit is the comprehensive pass.

## GOVERNING PRINCIPLE (Andrew sovereign)
**Yang's PKL files are the SINGLE SOURCE OF TRUTH for all Benchmark-tab data.**
Every number displayed must be reproducible from raw Yang PKL via an audited,
documented transform. No cross-source (e.g. SmartX) substitution into Benchmark
math. All wiring must be Terraform-managed with rigid deploy-ops such that every
change is identifiable to the minute (commit + deploy record).

## Established forensic baseline (CTO, minute-level)
SmartX-override injection into the Benchmark producer, then revert:
| commit | time (ET) | what |
|---|---|---|
| 48c651f1d | 2026-05-21 14:09:58 | NEW smartx-model-monthly-pull lambda (B1 infra) |
| 84128c245 | 2026-05-21 14:17:25 | benchmark producer made DUAL-INPUT (yang+smartx) |
| 9f6357634 | 2026-05-22 11:05:03 | model return SmartX-realized end-to-end (B4) |
| **80224d674** | **2026-06-01 09:41:02** | **REVERT B1/B3 -> pure-yang** (deploy 09:50:46 yang@447e1bbb) |
Root cause (per revert msg): SmartX 1M=last-complete-calendar-month + MTD=partial-
current-month vs yang trailing-calendar-day windows -> cross-period spread
subtraction. ADJACENT methodology commits also in audit scope: MDLP_RVVALT
2026-05-04 (model_portfolio_timeseries emit e2f0a8077; duration-matched RFR
2c18f0c06; weekend-drop 1c80f15e7; holiday-drop cdc2271c4); SI-annualization
flips 2026-04-13 (bc6f4ccb6/62985fcf0). YALP_MDSRC was CLOSED at the B-series
ship — the change rode project close, which is why "there may be others."

## Known data-flow surfaces (CTO recon)
- Benchmark: FE `portal/src/api/endpoints/benchmarks.ts` -> S3
  `opal-data-portal-v2/json/benchmarks/{benchmark_returns,model_portfolio_benchmarks,model_portfolio_timeseries}.json`
  <- lambda `yang-model-portfolio-benchmarks` <- raw `opal-data-portal-v2/benchmarks/data_YYYYMMDD_v1.pkl`.
- Peers: FE `PeersTab.tsx` -> S3 `json/peers/peer_performance.json`
  <- lambda `yang-generate-peer-performance` <- `uploads/Models Performance vs Peers YYYYMM.xlsx`.
  NOTE: Peers input is an UPLOADED xlsx, NOT the Yang PKL — UST-no-1M may be a
  source-data gap or a separate logic/path issue; classify in WS-2/WS-3.

## Workstreams
- **WS-0 QUARANTINE** (AE CloudOps lead + COO): freeze the benchmark/peers
  writers (disable EventBridge schedules via TF; 0-diff plan, surface before
  apply) so no scheduled run overwrites S3 mid-audit; SNAPSHOT current S3 state
  (all benchmark/peers JSON + the source PKL) to an evidence prefix; confirm
  deployed code == pure-yang revert (comp-pipescript deployed MATCH).
- **WS-1 SOURCE-OF-TRUTH** (DS-CP base): locate + document the canonical Yang
  PKL(s) — schema, series, coverage, generation provenance. The reference set.
- **WS-2 NUMBER VALIDATION** (DS-CP base + ~B): recompute EVERY Benchmark number
  {model_ret, benchmark_ret, spread} x {1D,WTD,MTD,1M,1Q,YTD,1Y,3Y,SI} x 5 models
  {UST,ST,INT,LTC,LTA} independently from raw PKL; compare to lambda output AND
  FE display; flag every mismatch. Same for Peers incl. the UST-1M gap.
- **WS-3 METHODOLOGY AUDIT** (AE OpalETL explains + DS-CP validates): audit every
  transform on raw Yang numbers — period-window defs, sqrt(252) annualization,
  weekend/holiday filtering, duration-matched RFR, SI annualization, slugify.
  Each: correct? documented? AE OpalETL authored several — owns the walkthrough.
- **WS-4 CHANGE FORENSICS + DEPLOY-OPS RIGOR** (AE CloudOps): to-the-minute
  timeline of EVERY change to benchmark/peers lambdas + TF + source-map + deploy
  records; confirm the revert is COMPLETE (no other swap remains); flag ANY
  non-TF-managed / manual / console change (incl. the unmanaged opal-data-portal-v2
  bucket policy already surfaced). Output = the "every change to the minute" ledger.
- **WS-5 INDEPENDENT VERIFY** (CVO): verify-channel over WS-2 (number validity)
  + WS-4 (change completeness); final sign-off gate before un-quarantine.

## Coordination
COO drives + write-partitions lanes. CTO consolidates + reports to Andrew + owns
the source-of-truth ruling. CVO is sole verify-state writer. Catch-up: each lane
reports current-state to CTO so the team converges on one picture (Andrew direct:
"ask them to update you on our work to get up to speed").
