# Yield-Curve 1Y-Ago Missing Tenors — Root Cause

**archetype:** DIAGNOSE

Andrew-direct macro-page investigation (CTO TO 20260601T190331Z + AMPLIFY 190612Z). Joining 0.5.0_AE_OpalETL (lead). Macro Yield Curve panel: the 1-year-ago curve is suddenly missing tenors.

## Verdict

ROOT CAUSE = intermittent FRED fetch failure + non-atomic partial overwrite of a single combined artifact. NOT a TF-module / artifact-path swap (Andrew's amplified hypothesis), and NOT a 1Y-ago artifact repoint (CTO hypothesis #1).

`json/macro/yield_curve_fred.json` carries EMPTY tenor arrays (`[]`) for whichever DGS series the daily FRED fetch failed on. `ingest_yield_curve_fred.py`:
- `fetch_series` — single `requests.get`, NO retry; returns `None` on any RequestException / non-200 / missing observations.
- `fetch_all_treasury_yields` — writes `[]` for a failed series.
- `run()` — uploads whatever it got, overwriting the prior good artifact.

Because the yield curve is ONE combined JSON (vs the regular FRED path's per-series CSVs), a partial fetch regresses the good tenors. FE `getOneYearAgoValue()` (YieldCurveTab.tsx) returns null for an empty array -> the tenor drops from the red 1Y-ago line.

## Evidence — S3 version history (empty set varies day-to-day)

| Version | Size | full | EMPTY tenors |
|---|---|---|---|
| 2026-01-15 (frozen) | 676 KB | 10/10 | none |
| 2026-05-27 | 607 KB | 9/10 | 3Y |
| 2026-05-30 | 540 KB | 8/10 | 20Y, 30Y |
| 2026-05-31 (now) | 471 KB | 7/10 | 1M, 3Y, 10Y |

`DGS10` (10Y) empty is impossible as a real FRED data-gap (most-published series) -> proves fetch-failure, not data-absence. The 7 populated tenors (3M/1Y/2Y/5Y/7Y/20Y/30Y) each have 497 obs; 1Y-ago resolves cleanly at 2025-06-02 (1-day diff, within the FE's +-7d window).

## Two findings this resolves

1. **CTO<->Andrew missing-set mismatch** ({1M,3Y,10Y} vs {1M,3Y,20Y,30Y}): nobody parsed wrong — the missing set genuinely changes each day. May30 had {20Y,30Y} empty (matches Andrew); May31 has {1M,3Y,10Y} (CTO + me). Andrew viewed ~May30.
2. **"All of a sudden" onset = 2026-05-21**, commit `fae806585` (daily-fold). The artifact had been frozen-complete since Jan-15 (no deployed runner). Reviving the runner — a correct staleness fix — EXPOSED the latent partial-overwrite bug that was always in the code.

## Architecture note (corrects the framing)

The Yield Curve panel is two-source by design:
- **Current + 1M Ago** <- Yang PKL macro data (`getMacroData()`, Treasury Yields group, monthly).
- **1Y Ago ONLY** <- FRED `yield_curve_fred.json`.

So "current full / 1Y-ago partial" is expected two-source behavior, not an artifact swap. Only the 1Y-ago curve is affected by the FRED empties.

## Proposed in-pattern fix (NOT yet applied — surfaced for CTO GO)

`infra/aws/lambda/fred-data-ingestion/ingest_yield_curve_fred.py`:
1. **Retry + backoff** in `fetch_series` (3 attempts; transient 5xx/timeout — FRED's 120 req/min limit is not the issue at 10 sequential requests).
2. **No-regression upload guard** — after retries, if any tenor is still empty: merge-preserve the prior S3 artifact's series for that tenor (RECOMMENDED — the 1Y-ago curve reads HISTORICAL observations that never change retroactively, so carrying forward prior real obs is honest and satisfies Andrew's data-honesty bar; zero fabrication), OR fail-closed (skip upload, keep yesterday's good artifact).

Split with AE OpalETL (lead): DS authors code fix; AE owns deploy (fred-pipeline TF + lambda zip). ds-commit-gate + `comp-pipescript io` on any edit.

## Files Modified

| File | Change |
|------|--------|
| (none) | Read/trace + diagnosis only. No edits — surfaced root-cause + proposed fix for CTO GO per instruction. |

## Compiler Tools

| Tool | Result | Note |
|------|--------|------|
| `comp-lambdamap check` | DRIFT in seeking-alpha only (3 WRONG_SOURCE_DIR); fred-data-ingestion CLEAN | Formally refutes the TF/source_dir-path-swap hypothesis for the yield-curve lambda. |
| `comp-trace yield_curve --direction both` | No node matching `yield_curve` (artifact key not graphed) | Trace done manually instead: ingest -> S3 json/macro/yield_curve_fred.json -> apiRequest -> yield-curve.ts -> YieldCurveTab getOneYearAgoValue -> 1Y-ago line. |

`comp-pipescript io` deferred to the edit phase (no gold/producer script edited yet; this lambda is not a gold-tier pipeline script).

## Next Steps

1. [CTO] GO/NO-GO on the proposed fix shape (retry + merge-preserve vs fail-closed) before I edit.
2. [AE OpalETL] Coordinate split — confirm I author the code fix, AE deploys; share what AE already found to avoid overlap.
3. [DS self] On GO: implement fix in `ingest_yield_curve_fred.py`, ds-commit-gate, write devops brief, hand to AE for deploy.
