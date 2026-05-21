# MDPF_ASSETS.031 — RAVC2: 2024-depth v0.9 backfill COMPLETE (the final MDPF TO)

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-21
**TO:** MDPF_ASSETS.031 — 2024-depth v0.9 backfill
**Status:** COMPLETE — 297 partitions swept, rollup rebuilt, verified.
**RAVC2 to:** 2.0.0_SA_COO~B (direct) + 1.0.0_SA_CTO~B (separate send)

---

## TL;DR

The v0.9 historical `aggregate_aua` series now reaches **2024-11-01**. 297 new
v0.9 partitions (2024-11-01 → 2025-12-22) materialized via the proven `.029`
mechanism on CTO~B's ratified clamped calibration; rollup rebuilt to span
2024-11-01 → 2026-05-20. **AC1 daily-per-model granularity proven per-partition
(297/297); the `.031/.029` seam is SMOOTH (+0.649%) — the clamped fit
eliminated the artifact step.** On accept, MDPF_ASSETS 3-step-closes.

---

## Calibration (CTO~B-ratified, governing)

Per CTO~B's definitive ruling: the **clamped linear delta-$ fit** —
`lift(d) = max(0, 14,796,793 + 343,246·days_since(2026-01-16))`.
- 2024-11-01 → ~2025-12-03 (~265 days): `lift = 0` — RPS uncalibrated
  (= Option A; the genuinely-unanchored deep tail).
- 2025-12-04 → 2025-12-22 (13 partition dates): the `.029`-ratified line
  tapering 0 → ~$6.2M — seam-continuity, so the `.031/.029` join is seamless.

`calibrated_Schwab = RPS_whole + lift`; `1c = 0` (item-(d): SMA absent from the
SmartX history for the range); `1b = calibrated_Schwab − 1a`; 49F-only (no
Inflection 2a pre-2026-05-15).

## The sweep (AC3)

- **297 v0.9 `aggregate_aua/{date}.json` partitions** for 2024-11-01 →
  2025-12-22 — new-key writes (no pre-existing partitions in that range),
  built from scratch in the structure identical to the `.029` partitions.
- 11 dates RPS-roll-forwarded (no exact RPS partition — nearest prior, the
  `.029` pattern). Non-business / year-end dates: honest gaps, no synthetic
  fill (the range has no aum-timeseries point → no partition).
- **Rollup** `aggregate_aua_timeseries.json` rebuilt — 395 dates, 2024-11-01 →
  2026-05-20, 0 nulls; `meta.backfill_methods` records both `.029` + `.031`.

## Verification (Phase 3)

| check | result |
|-------|--------|
| **AC1 — daily-per-model 1a, proven per-partition** | **297/297 PASS** — every partition carries 5 model-cohort `by_model` entries; per-model sum == aggregate 1a **to the cent**. Read at full grain from `aum-timeseries.json by_model`. Proven by re-reading every `.031` S3 partition, not asserted. |
| 49F identity `1a+1c+1b == partner_custody_total` | **0 breaks / 297** |
| negative 1b | **0 / 297** |
| `methodology_version` | **v0_9 — all 297** |
| **`.031/.029` seam** (2025-12-22 → 12-23) | **+$8,559,848 / +0.649% — SMOOTH.** The clamped fit's `.029`-line strip makes the join continuous; the ~$6.56M artifact step a hard truncation would have planted is GONE. |
| headline series | continuous **$776.17M (2024-11-01) → $1,748.03M (2026-05-20)**, 0 nulls |
| headline day-over-day > 5% | **2**, both known-real — see below |
| 1c | all 0 across the 297 (item-(d): SMA absent for the range) |

**The 2 headline >5% moves — both real, neither a `.031` artifact:**
1. **2025-04-08 → 04-09, +5.2%** — April-2025 market volatility. Verified: the
   RPS partitions for both days carry the **same ~4,250 accounts / ~58k
   positions** — identical holdings re-valued, not a partial-partition
   artifact; 1a is smooth through it. RPS reflects both net-new-asset change
   and the mark-to-market line — a +5.2% day in the most volatile market in
   years (Andrew-confirmed) is well within plausible. Kept faithfully — no
   synthetic smoothing (it is real data).
2. **2026-05-15 → 05-18, +5.7%** — the Inflection 2a-layer onset (a
   `.029`-era structural step, previously CTO~B-confirmed expected). Outside
   the `.031` range; unchanged by `.031`.

**Per-component series-walk:**
- **1a** — 2 day-over-day >5% moves, sourced verbatim from `aum-timeseries.json`
  (the AC1 full-grain source); plausible onboarding-era growth in the small
  2024 book ($354M → $1.08B over the range). `.031` reflects the source
  faithfully (no `.031` 1a-smoothing was directed — the `.029` 05-15..05-19
  smoothing was `.029`-specific and outside this range).
- **1c** — all 0 (item-(d)).
- **1b** — 18 day-over-day >5% moves. 1b is the residual (`calibrated_Schwab −
  1a`) on a ~$229–457M base; a $-move that is <3% of the ~$800M–1.3B headline
  is >5% of the smaller 1b base — so 1b shows more >5% moves than the headline
  purely from the smaller denominator. The identity holds (0 breaks) and 1a is
  the smooth model layer — this is the residual faithfully carrying RPS's real
  market + net-new variation (April-2025 volatility + the rapid-onboarding
  era), **not leakage**. Flagged for CTO~B output-validation per the
  series-walk discipline.

## Marking (AC2)

Per CTO~B's governing ruling — the whole `.031` range marked as the 2024-depth
extension; per-partition metadata records the lift applied. Every `.031`
partition's `meta` carries: `estimate_tier: "2024_depth_extension"`;
`estimate_note` (RPS-uncalibrated best-estimate, not a to-the-cent reconciled
partition — distinct from `.029`/`.028`); `calibration` block (model, params,
`lift_applied`, `regime` = `uncalibrated_deep_tail` | `029_line_seam_strip`,
`rps_source_date`); `c1_treatment` (value 0 + the item-(d) basis). The rollup's
`meta.backfill_methods` records `mdpf_assets_031_v0_9_2024depth`. The
data-layer marking is complete; **chart-surfacing** the estimate segment (a
portal render change to visually distinguish it) is a portal-lane follow-on if
COO~B/CTO~B want the visible-on-chart flag — the data carries what such a
render needs (`estimate_tier` per partition / the `.031` date range).

## Non-destructive (AC4)

The 297 partition writes are **new keys** (2024-11-01 → 2025-12-22 had no
prior partitions) — no overwrite, nothing to back up. The rollup overwrite was
preceded by a local backup (`.runtmp/mdpf031/backup/aggregate_aua_timeseries.pre031.json`);
versioned bucket; no object deleted.

## Status

**MDPF_ASSETS.031 COMPLETE.** The MDPF v0.9 line is fully extended —
`.028` + `.029` + `.030` + `.031` — the Daily AUA chart's v0.9 series now
spans 2024-11-01 → present, one continuous trend, the 2024-depth segment
marked best-estimate. On RAVC-accept, MDPF_ASSETS 3-step-closes.
