# MDPF_ASSETS.029 Phase 1 — Checkpoint 3: 97-partition v0.9 backfill COMPLETE

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-20
**TO:** MDPF_ASSETS.029 Phase 1 (GO'd ab6d2a87c; seam resolved — Andrew Option B)
**Status:** COMPLETE — 97 partitions re-materialized v0.9, rollup rebuilt, verified.

---

## TL;DR

The full historical `aggregate_aua` series is now on the PRD v0.9 basis. 97
partitions (2025-12-23 → 2026-05-19) re-materialized; the rollup rebuilt; **all
98 S3 partitions carry `methodology_version=v0_9`**; **the −$100.77M v0.8→v0.9
cliff is GONE** — the series is continuous into the .028 daily-forward tail
with a +$4.70M residual seam. Non-destructive throughout (versioned bucket +
local backup of all 98 prior objects).

## Mechanism (as executed)

Andrew Option B + CTO~B's ratified calibration:

| v0.9 term | source |
|-----------|--------|
| **1a (model)** | `aum-timeseries.json` daily series, RULING #1 smoothing applied (see below) |
| **Schwab 49F whole** | `schwab/silver/rps` `sum(market_value)` + the linear delta-$ calibration |
| **1c (SMA)** | ratio-estimate `0.0184769 × 1a` (calibrated to the 2026-05-20 feeder) |
| **1b (non-model)** | `calibrated_Schwab − 1a − 1c` (v0.9 SMA-exclusive residual) |

**Calibration** (CTO~B-ratified linear delta-$ fit, NOT a flat K — the
RPS-vs-crosswalk gap drifts 1.18%→3.41%): `calibrated_Schwab(d) = RPS_whole(d)
+ delta_$(d)`, `delta_$(d) = 14,796,793 + 343,246 × days_since(2026-01-16)`.
Applied as a 2-parameter model to all 97 dates — partitions stay RPS-derived;
the measured crosswalk values were NOT substituted (the withdrawn HYBRID stays
set aside). The 79-date overlap measurement (brief 325aaeb81) fitted the 2
parameters; nothing else from the crosswalk entered the backfill.

**RULING #1 — 1a smoothing** (8 partitions marked, visible in `meta`):
- 2026-05-15 / 05-18 / 05-19 — `_1a_adjustment: interpolated_anomaly` + `_1a_raw`.
  The ~$80–100M aum-timeseries spike (round-trip +7.5%/−5.4%) linear-
  interpolated between the 05-14 and 05-20 trend anchors.
- 5 partition-dates with no 1a point (2025-12-27, 01-26, 01-28, 02-05, 04-03) —
  `_1a_adjustment: rollforward_1a` + `_1a_rollforward_source`.
- 2026-01-14 (concentrated inflow) and 04-02 (duration-ordered market move)
  corroborated REAL via `by_model` decomposition — kept, not smoothed.

**Construction:** v0.8 partition as template; the 49financial block patched to
v0.9 (model_aua / sma_aua / non_model_aua / total_aua / partner_custody_total);
`by_model` 5 model-cohort entries rescaled where 1a changed; Inflection
partner preserved verbatim (v0.9 re-scoped only 49F); `aggregate` recomputed;
`methodology_version = v0_9`; every partition carries `meta.calibration`
(model, params, source, extrapolated flag, RPS-carry-forward flag) — estimation
visible, never silent.

## Full-series reconciliation

| check | result |
|-------|--------|
| S3 partitions, all v0.9 | **98 / 98** `methodology_version=v0_9` |
| 49F identity `1a+1c+1b == partner_custody_total` | holds to the cent — **0 breaks / 98** |
| negative 1b | **0 / 98** |
| 1b range (historical) | $208M → $306M, monotone-ish |
| headline series | continuous **$1,328.26M (2025-12-23) → $1,748.03M (2026-05-20)** |
| day-over-day 49F (49f-only) > 5% | **0** |
| headline day-over-day > 5% | **1** — the 2026-05-15→05-18 Inflection 2a-layer onset (+5.7%); a real structural step (Inflection data begins there), NOT a backfill artifact — confirmed expected per CTO~B |
| rollup `aggregate_aua_timeseries.json` | rebuilt, 98 dates, 0 nulls, uploaded |

## Boundary check — the v0.8→v0.9 cliff

| | headline |
|--|----------|
| v0.8 2026-05-19 (pre-backfill, full-BD-book) | $1,848,801,032.18 |
| **v0.9 2026-05-19 (backfilled)** | **$1,743,327,627.64** |
| v0.9 2026-05-20 (.028 daily-forward) | $1,748,030,393.45 |

Pre-backfill the series stepped −$100.77M at the 05-19/05-20 cutover (v0.8
history vs the .028 v0.9 tail). **Post-backfill that cliff is GONE** — 05-19 →
05-20 is now **+$4.70M** (the documented residual seam — one day of book
movement + RPS-calibration ratio noise; bounded, well under CTO~B's $15M
threshold).

## Deployed verification

- `s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua/{date}.json` — 97
  re-materialized partitions written (2026-05-20 untouched — already v0.9 from
  .028). All 98 verified `methodology_version=v0_9`.
- `s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua_timeseries.json` —
  rollup rebuilt from the 98 v0.9 partitions, uploaded; `meta.backfill_methods
  = ["mdpf_assets_029_v0_9_rps_calibrated"]`.
- **Non-destructive:** the bucket is versioned; all 98 prior objects were
  backed up locally before any write (`.runtmp/mdpf029_scratch/backup_partitions/`)
  — rollback = restore the prior object version or the local backup. No object
  deleted.

## Notes / open items

- **1c estimated** (ratio-of-1a) — Andrew/CTO~B accepted; ~1.5% of the 49F
  total; `meta.c1_estimate` records the method.
- **Deep-tail (2025-12-23 → 01-15)** — `meta.calibration.extrapolated=true`;
  the calibration is back-extrapolated ≤24 days (~±$12.7M residual std).
- **2024-depth extension** — separate Andrew decision (CTO~B carrying); the
  linear delta-$ fit does NOT extrapolate to 2024-11 (goes negative ~440 days
  back) — fresh calibration treatment needed if that extension is greenlit.
- **`.030`** (legacy-emit v0.9, the chart's `non_model_assets.json`) can now
  proceed — it reads these v0.9 partitions; the historical basis is settled.
- Reproducibility: each partition self-documents via `meta.calibration` +
  the `_1a_*` markers; the mechanism + parameters are in this brief and the
  checkpoint-1/2 briefs. Backfill tooling held in `.runtmp/mdpf029_scratch/` —
  can be committed as a permanent artifact if COO~B/CTO~B want it.

## Status

**MDPF_ASSETS.029 Phase 1 COMPLETE.** The historical `aggregate_aua` series is
on the v0.9 basis, continuous, cliff removed. RAVC2 to COO~B CC CTO~B.
