# MDPF_ASSETS.030 — RAVC2: legacy-emit v0.9 re-scope COMPLETE (Phases 1-5)

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-21
**TO:** MDPF_ASSETS.030 (legacy-emit v0.9 re-scope + historical backfill)
**Status:** COMPLETE — Phases 1-5 shipped, deployed, live-published, verified.
**RAVC2 to:** 2.0.0_SA_COO~B (direct) + 1.0.0_SA_CTO~B (separate send)

---

## TL;DR

The live Model Portfolios "Daily AUA Analysis" page is now on the v0.9 basis,
history backfilled, **reconciling to-the-cent against the v0.9 platinum
series**. The Daily AUA chart is one continuous v0.9 trend, no v0.8/v0.9 cliff.

---

## What shipped

`build_legacy_compat_emit.py` re-scoped to PRD v0.9 + the historical backfill:

| phase | done |
|-------|------|
| 1-2 | v0.9 re-scope: removed the `compute_49f_broader_custody` override (uses the platinum partition's v0.9 1b/1c directly); Cohort 0 out of the headline `enterprise_total` (audit-only); `methodology_version=v0_9`; dead broader-custody code removed |
| AC2 Option 1 | `derive_inflection_from_platinum()` — Inflection 2a + per-model sourced from the platinum partition's Inflection block (single source of truth; the independent Eclipse recompute dropped) |
| 3 | Rule-13 deploy (`s3://opal-data-mdpf/code/scripts/backfill/`, md5 MATCH) + emit `--upload` — the live-page publish |
| 5 | `CUTOVER_DATE` 2026-01-16 → 2025-12-23; re-emit — the full `.029` v0.9 range backfilled into `non_model_assets.json` |

Commits: `82d3f8113` (v0.9 re-scope + Option 1), `60dd8d5a9` (Phase-5 CUTOVER).

## Reconciliation — to-the-cent (AC2 + AC5)

Live `non_model_assets.json` `enterprise_total` vs the `.029`-rewritten v0.9
platinum `aggregate_aua/{date}.json` headline:

| date | legacy `enterprise_total` | platinum headline | delta |
|------|---------------------------|-------------------|-------|
| 2026-01-20 | $1,397,318,673.86 | $1,397,318,673.86 | **$0.00** |
| 2026-03-13 | $1,448,303,582.86 | $1,448,303,582.86 | **$0.00** |
| 2026-05-19 | $1,743,327,627.64 | $1,743,327,627.64 | **$0.00** |
| 2026-05-20 | $1,748,030,393.45 | $1,748,030,393.45 | **$0.00** |

`non_model_assets.json`: 390 time_series entries, **93 on `method=v0_9`** from
2025-12-23 (the full `.029` range); `meta.methodology_version=v0_9`,
`cutover_date=2025-12-23`. The legacy page now AGREES with the v0.9 platinum
series — same basis, Cohort 0 excluded, Schwab not broader-BD.

## Before / after live-page headline (the −$150.18M move)

| | `enterprise_total` (2026-05-20) |
|--|-------------------------------|
| before .030 (CEO-direct 2026-05-19 broader basis) | $1,898,213,922.32 |
| **after .030 (v0.9)** | **$1,748,030,393.45** |
| **move** | **−$150,183,528.87** |

Decomposition: **−$91.34M** Cohort 0 (`etf_public_residual`) removed from the
headline (audit-only per v0.9) + **−$58.85M** broader-BD-book → Schwab-49F
re-scope. Andrew GO'd the live publish; CTO~B output-validated the to-the-cent
re-run. `model_aum` unchanged (model side is basis-agnostic).

## Boundary — no v0.8/v0.9 cliff (AC6)

`non_model_assets.json` is continuous on v0.9 from 2025-12-23 ($1,328.26M) →
2026-05-20 ($1,748.03M). The one day-over-day step (2026-05-15→05-18, the
Inflection 2a-layer onset) is the legitimate structural appearance of Cohort 2a
when Inflection data begins — CTO~B-confirmed expected, not a defect. The 6
year-end dates with no platinum partition (2025-12-24/25/30/31, 2026-01-01/02)
are honest gaps — no entry, chart connects across — consistent with `.029`.

## The $614K Inflection-2a residual — characterized: VINTAGE

Pre-Option-1, the emitter's `load_inflection()` computed Inflection 2a =
$93,084,450.47 vs the platinum partition's $93,698,710.19 — a $614,259.72 gap.
Characterization (per CTO~B's rider): **VINTAGE, not methodology.** Both
`load_inflection()` and the WS-C feeder (`build_mdpf_wsc_inflection_feeder.py`,
which wrote the platinum partition's 2a) sum the **identical column**
(`total_value`) of the **identical file**
(`gold/eclipse/{date}/model_portfolio_accounts.parquet`) — same population,
same filter. The $614K is the same Eclipse artifact read at two snapshot times
(the `.028` platinum write vs the emitter run); Eclipse restated/completed
2026-05-20's data in between. **No methodology divergence → no separate
platinum-2a finding.** Option 1 resolves it fully — the platinum partition is
now the single source of truth for both 49F and Inflection.

## aum-timeseries.json — verify + 1a-refresh

aum-timeseries.json is model-side only (1a + 2a; no 1b/basis field) — verified
unaffected by the v0.9 1b re-scope. The Phase-5 re-emit refreshed its 1a for
2026-05-15/18/19 to the `.029`-smoothed values (it reads the now-smoothed
platinum partitions) — so the chart's model layer carries no raw 1a spike. The
05-15→05-18 step in the displayed `aum` is the Inflection 2a-onset (expected).

## Non-destructive

`opal-data-portal-v2` is versioned; the emitter wrote local pre-overwrite
backups before each emit (`.runtmp/legacy_*_pre_overwrite.20260521T*.json`).
Rollback = restore the prior object version or the local backup. No object
deleted.

## Compiler Tools / gates

`py_compile` OK; `ds-commit-gate.sh` exit 0 (Rule 14/15) on every edit; Rule-13
deploy (`aws s3 cp` → md5 MATCH) for both phases.

## Status

**MDPF_ASSETS.030 COMPLETE.** The MDPF v0.9 line is fully landed — .028
(daily-forward) + .029 (historical aggregate backfill) + .030 (legacy emit +
historical `non_model_assets.json` backfill). The Daily AUA chart is one
continuous v0.9 trend. ADHC_VALGATE.003 (C-4), parked behind .030, is now
resumable — COO~B's call.
