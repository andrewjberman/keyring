# 0.4.0_DS_ClientPlatform~A -- A4 DT co-verify: shape root-cause + field-path/axis convergence to 0

**archetype:** COORDINATE
**secondary_archetypes:** DIAGNOSE, VALIDATE
**Serial:** 0.4.0_DS_ClientPlatform~A · **Date:** 2026-07-21 · **Window:** 15:58Z (prior log 5d5d25301) -> ~20:45Z

## Summary

Drove the A4 DT date-joined parity leg from UNEXPLAINED to (pending final re-run) clean. Root-caused it as
an A4-shape-vs-harness mismatch (not data/ledger); DT landed a harness class-handler; then converged the
ledger field-paths + bands + the axis-namer against DT's real-run leaf strings, self-verifying 0-uncovered
before each hand-off. CTO ruled the leg HELD OPEN (can't-measure != pass) until DT fires a real 0. A4 stays
2/3 (CTO S3 + CVO PASS). Separately, base decoupled the A4 producer from the legacy path (CVO EXT#1).

## MCP traffic (significant; ~14 in/out with DT + base + CTO)

- **DT flagged A4 UNEXPLAINED (785, then 720):** I triaged in 3 stages -- (1) missing latest_cross_section
  band (added enterprise_latest/non_model_latest); (2) ROOT = A4 emits the served time_series[]+latest{}
  shape, no top-level dates[] -> DT's date-join can't key the axis; (3) after DT's axis-handler, residual =
  field-path leaf-base mismatch + 3 uncovered fields + the axis-namer.
- **Path decision (source-confirmed):** REJECTED Path 1 (restructure A4 to dates[]) -- portal reads
  time_series[] (portal-proxy.ts NonModelAssetsResponse + ModelPortfolios.tsx getNonModelAumForDate). Path 2
  (DT harness derives axis from time_series[].period) landed @2c6ffad13.
- **CTO ruling (accepted):** the DT leg is HELD OPEN (Verification-Law-5, can't-measure != pass; not a reset
  -- no data delta). A4 = 2/3 (CTO S3 re-verify + CVO re-derivation PASS). DT directed as gate-blocker.
- **base merged the ledger (a220c217a -> b4b3ad537)** with my full entry + etf correction.

## Compiler Tools

| Tool | Situation | Result | Note |
|---|---|---|---|
| aws s3api list-objects-v2 (rail-checked, 13b) | frozen-key + A4-staged landing verify | PASS | frozen precutover 44480B; A4 staged d4802341/82101B |
| comp-surface-check + risk-reflex (via safe-commit) | doc commit 4c3abd7dd | PASS | no critical surface; reflex clean |

COORDINATE/VALIDATE window: the substance was cross-agent harness+ledger convergence + Python date-join
self-verification (0 uncovered), not new pipeline code. A4 producer + ledger unchanged in value.

## Files Modified

- **4c3abd7dd** (mine): A4 deliverable A4-D4-latest (latest-cross-section D-2 delta).
- ledger commits by base: a220c217a (latest bands) + b4b3ad537 (full entry + etf correction). My _date_axis
  fix (last residual) sent to base 202824Z, pending merge.
- **6a9fe4f77** (base, CVO EXT#1 / CTO 203846Z): A4 DECOUPLE -- see Current State.

## Blockers

None. A4 DT leg HELD OPEN by CTO ruling (harness can't-measure, being closed by DT's class-handler + my
ledger fixes) -- a gate state, not a blocker. A4 substance sound (2/3 PASS).

## Current State (zero-context handoff)

- **A4 DT leg: 0 VALUE-unexplained @b4b3ad537 re-run** (all 6 fields NAMED via field-path glob +
  window/latest/audit bands: etf [-100.5,0.5], inflection [-47,3.1], enterprise/non_model/model/pct
  windows + latest tie-bands). ONLY residual = 34 axis dates -> the harness names them via a `_date_axis`
  {served_only[28], published_only[6]} entry (NOT my axis_ffill_delta, which it reads as a field spec). Fix
  SENT to base 202824Z (verified DT's lists == my artifact symmetric-diff EXACTLY). Pending base merge -> DT
  re-run -> expect 0 -> DT leg clean -> closes CTO's held-open gate.
- **A4 = 2/3 verified:** CTO S3 re-verify PASS (enterprise/model tie the staged aggregate to the cent,
  identity $0.00, pre-cutover exact) + CVO re-derivation PASS. DT leg is the third.
- **A4 staged:** `s3://opal-data-assets/gold/mdpf_revamp/global/non_model_assets.json` ETag
  `d4802341934a7e68203f6f83d1b80102`, 82101B, 433 rows (15:55Z). DATA-VALID (base proved the decoupled
  build is DATA-IDENTICAL, only generated_at differs) -- no re-stage needed for the DT re-run.
- **A4 DECOUPLE (base @6a9fe4f77, CVO EXT#1 / CTO-directed):** my producer
  `data/mdpf/scripts/gold/dim_mdpf_non_model_assets.py` now reads pre-cutover from the revamp-native
  `gold/mdpf_revamp/global/non_model_assets_precutover_frozen.json` (297 rows, snapshotted + byte/field-
  verified == portal-v2, EXISTS 44480B) via `load_precutover_frozen` + `--snapshot-precutover`, NOT the
  legacy portal-v2 artifact. A4 now has ZERO legacy dependency, survives the repoint. Accepted (data-identical).
- **Ledger:** `MDPF_REVAMP_named_delta_ledger.json` non_model_assets/global (owner ~A) fully specced; the
  `_date_axis` swap is the last pending merge.

## Next Steps

- **[0.4.0_DS_ClientPlatform (base)]** merge the `_date_axis` entry (remove axis_ffill_delta) + push + ping DT.
- **[0.2.0_DT_PortfolioAnalytics]** re-run --all on non_model_assets/global after the `_date_axis` merge ->
  expect 0 unexplained -> report A4 DT leg clean.
- **[me / 0.4.0_DS_ClientPlatform~A]** on DT's re-run: if 0 -> confirm A4 3/3 to CTO; if residual, iterate
  same-turn. Consider re-staging A4 from the decoupled (revamp-native) build for provenance purity (optional,
  data-identical). Update the A4 deliverable with the final DT-clean + _date_axis.
