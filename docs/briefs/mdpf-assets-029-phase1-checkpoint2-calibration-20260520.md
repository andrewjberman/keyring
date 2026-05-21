# MDPF_ASSETS.029 Phase 1 — checkpoint 2: RPS-vs-crosswalk calibration measurement

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-20
**TO:** MDPF_ASSETS.029 Phase 1 (GO'd, ab6d2a87c)
**Checkpoint:** 2 (calibration measurement — per CTO~B's HYBRID seam ruling)
**Routed to:** 1.0.0_SA_CTO~B (direct — ratify the calibration form) + 2.0.0_SA_COO~B
**Non-mutating:** all reads; no S3 write; crosswalk computed in-process only.

---

## TL;DR

- **Step 1 — the crosswalk re-materializes cleanly for a historical date.**
  2026-02-13: `partner_custody_total` (Schwab-only) = $1,460,354,796.78, off
  silver/fees + silver/allocations; the certified-aua cross-check self-skips
  when no certification exists (pre-2026-03-11) — no abort.
- **Step 2 — the RPS-vs-crosswalk delta DRIFTS; it is not a stable $ or %.**
  Over the 2026-01-16→05-19 overlap it grows ~linearly from $16.6M/1.18% to
  $56.2M/3.41%.
- **Recommended calibration form: linear-in-time fit.** The $-form fit is the
  tighter one (R² 0.854 vs 0.786). Deep-tail (2025-12-23→01-15) calibration is
  a short backward extrapolation — a bounded ~$6.6M–$14.5M uplift on RPS.
- **HARD STOP — CTO~B ratifies the form before the 97-sweep.**

---

## Step 1 — crosswalk re-materialization (historical date)

`build_custodian_crosswalk()` → 10,470 accounts, 0 conflicts, from 1,860
silver/fees partitions. `compute_partner_custody_total("2026-02-13")`:

| field | value |
|-------|-------|
| certified_aua (recomputed, full BD book, liability-excluded) | $1,599,953,116.08 |
| aua_certification cross-check | self-skipped (no cert before 2026-03-11) — no abort |
| **partner_custody_total (Schwab-only)** | **$1,460,354,796.78** (5,710 accts) |
| custody decomposition | Schwab $1,460.4M / ByAll Accounts $132.8M / unmatched $5.7M / DST $1.1M |

Confirmed: the crosswalk runs cleanly for a historical date — silver/fees +
silver/allocations, no certification dependency.

## Step 2 — the RPS-vs-crosswalk delta, daily over the overlap

Overlap window 2026-01-16→2026-05-19: 82 dates; **79 measured, 3 errored**
(see caveats). `delta = crosswalk_partner_custody_total − RPS_market_value_sum`.

| statistic | delta ($) | delta (% of crosswalk) |
|-----------|-----------|------------------------|
| mean | $36.2M | 2.381% |
| std | $12.7M | 0.762% |
| min | $15.8M | 1.128% |
| max | $57.4M | 3.538% |

| sample date | crosswalk | RPS | delta | delta % |
|-------------|-----------|-----|-------|---------|
| 2026-01-16 | $1,412.9M | $1,396.2M | $16.6M | +1.178% |
| 2026-03-19 | $1,458.0M | $1,414.8M | $43.1M | +2.959% |
| 2026-05-15 | $1,648.8M | $1,592.6M | $56.2M | +3.411% |

**The delta is NOT stable** — neither a fixed $ offset nor a fixed %. It
**drifts strongly upward**, ~linearly. This is structurally expected: RPS omits
cash-only / new / recently-closed accounts (per CTO~B's ruling, ~368 accounts);
as the 49F book grows and account churn accumulates, the omitted set — and the
delta — grows.

## The calibration fits

| form | intercept @ 2026-01-16 | slope | R² |
|------|------------------------|-------|-----|
| **delta $** | $14,796,793 | +$343,246 / day | **0.854** |
| delta % | 1.1449% | +0.01982 pp / day | 0.786 |

The **$-form fit is empirically tighter** (R² 0.854 vs 0.786). CTO~B's prior
("a % is likelier robust — the gap scales with book size") is directionally
reasonable for far extrapolation, but in-sample the $ form wins and the
deep-tail extrapolation here is *short* (≤24 days), so the tighter in-sample
fit is the better pick.

**Deep-tail calibration** (2025-12-23→2026-01-15, the ~24 dates the crosswalk
cannot reach — RPS calibrated by backward extrapolation of the $ fit):

| date | days from 01-16 anchor | calibration uplift on RPS |
|------|------------------------|---------------------------|
| 2026-01-15 | −1 | +$14.45M (+1.125%) |
| 2026-01-02 | −14 | +$9.99M (+0.867%) |
| 2025-12-23 | −24 | +$6.56M (+0.669%) |

The uplift is small (~$6.6M–$14.5M on a ~$1.4B base, ≤1.1%) and the
extrapolation is short. At the 2026-01-16 join, calibrated-RPS = RPS + fitted
delta ≈ crosswalk by construction → **~0 seam at the deep-tail/crosswalk-native
boundary**, matching the ~0 seam the HYBRID gives at the 05-19/05-20 boundary.

## Recommendation (for CTO~B to ratify)

1. **97-sweep basis:** crosswalk-native for 2026-01-16→2026-05-19 (79 of the
   97 dates — 3 need a fix, see caveats); RPS + calibration for 2025-12-23→
   2026-01-15 (~18 dates).
2. **Calibration form:** linear-in-time **delta-$ fit** (intercept $14.80M @
   2026-01-16, slope +$343,246/day), applied as `crosswalk_equiv = RPS +
   (a + b·days_from_2026-01-16)` for the deep-tail dates only.
3. The fit is re-anchored at sweep time on the then-final overlap series.

## Caveats / open items

- **3 silver/allocations partitions errored** — 2026-01-26, 01-28, 02-05 carry
  a different schema (columns `Portfolio Group` / `Original Account Number` /
  `Relationship ID` instead of `account_id`). They are inside the
  crosswalk-native span — the sweep needs a column-mapping fix or a
  roll-forward from the adjacent date. Flagged for a small pre-sweep fix.
- **Fit residual:** R² ~0.79–0.85 leaves a ~$12.7M residual std. The deep-tail
  calibrated values carry ~±$12M uncertainty — ~0.9% on a ~$1.4B base, within
  the "smoothed/estimated" tolerance Andrew granted.
- **Still pending CTO~B (from the checkpoint-2 scratch-batch brief, 3d1d14fd8):**
  ruling on the 1a-series anomaly (the ~$80–100M spike across 2026-05-15→05-19)
  — that gates the 97-sweep alongside this calibration ruling.
- **Andrew-vs-allocations flag (raised separately):** the HYBRID reintroduces
  silver/allocations, which Andrew's 2026-05-20 directive spoke against —
  recommended a quick Andrew confirm; CTO~B's call.

## Status

**HARD STOP after checkpoint 2.** The 97-sweep does not run until CTO~B
ratifies (a) the calibration form above and (b) the 1a-anomaly handling.
