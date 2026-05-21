# MDPF_ASSETS.031 (prospective) — 2024-depth backfill: calibration feasibility/method probe

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-21
**Status:** SPECULATIVE PRE-STAGE — not a dispatched deliverable. `.031` does
not exist yet; CTO~B is carrying the 2024-depth extension decision to Andrew.
This probe is productive-standby work (COO~B-sanctioned) — it is decision-useful
for that pending greenlight call and is the Phase-0 method scoping if `.031`
ships.
**Routed to:** 1.0.0_SA_CTO~B (the 2024-depth decision owner) + 2.0.0_SA_COO~B

---

## TL;DR

- A 2024-depth extension of the MDPF v0.9 series is **data-feasible back to
  2024-11-01** (RPS reaches 2024-01-12, but the SmartX 1a series floors at
  2024-11-01 — the binding limit). The `.031` range would be
  **2024-11-01 → 2025-12-22** (~285 business days, before `.029`'s 2025-12-23).
- **The calibration has NO ground-truth anchor anywhere in that range.** The
  crosswalk (silver/allocations) floors at 2026-01-16 — so the entire `.031`
  span is fully out-of-sample for any RPS-vs-crosswalk calibration.
- `.029`'s linear delta-$ fit **goes structurally invalid** out there:
  extrapolated to 2024-11-01 it yields **delta_$ ≈ −$136.6M** — a negative
  gap, impossible (RPS undershoots the crosswalk; the gap is ≥ 0 always).
- **Verdict:** feasible, but a `.031` deep-tail series is necessarily a
  **best-estimate**, not a reconciled-to-the-cent series like `.029`. If
  greenlit, `.031` ships with an explicitly-estimated calibration + a wider,
  marked uncertainty band.

---

## (a) Data depth — the floor is 2024-11-01

| input | earliest | note |
|-------|----------|------|
| RPS Schwab-whole (`opal-data-bd/schwab/silver/rps`) | 2024-01-12 | deep |
| SmartX 1a series (`aum-timeseries.json` aggregate) | **2024-11-01** | the binding floor — 43 entries in 2024 (2024-11-01 1a $353.8M → 2024-12-31 $386.75M) |
| crosswalk (`silver/allocations`) | 2026-01-16 | the calibration-anchor limit |

So the `.031` range is **2024-11-01 → 2025-12-22**. Pre-2024-11-01 is
unreachable — RPS exists but there is no model (1a) series, so 1b =
Schwab − 1a − 1c is not computable. (Same 1a-bound finding as the `.029`
checkpoint-1 brief.)

## (b) The calibration problem — no in-range anchor

`.029`'s calibration (linear delta-$, `delta_$(d) = 14,796,793 +
343,246·days_since(2026-01-16)`) was fitted on the **2026-01-16 → 2026-05-19
crosswalk-vs-RPS overlap** (R² 0.85 in-sample). The `.031` range
(2024-11-01 → 2025-12-22) contains **zero** crosswalk partitions — the
crosswalk simply does not exist before 2026-01-16. Every `.031` date is
out-of-sample, and the nearest fitted anchor (2026-01-16) is ~285–725 days away.

**The `.029` fit extrapolates to a structurally impossible value:**
- At 2024-11-01: `days_since(2026-01-16) ≈ −441` →
  `delta_$ = 14,796,793 − 343,246·441 ≈ −$136.6M`.
- A negative delta means calibrated_Schwab < RPS. But the RPS-vs-crosswalk gap
  is RPS *undershooting* (missing cash-only / new / recently-closed accounts,
  ~368 of them in May 2026) — it is **≥ 0 by construction**. A negative
  calibration is just wrong out-of-sample.
- The linear *%* form fails the same way: `delta% = 1.1449 + 0.01982·days`
  crosses 0 around 2025-11 and goes negative before.

The `.029` linear fit was honest *in-sample*; linear extrapolation 285–725 days
past the data is not.

## (c) Calibration-form options for `.031` (for CTO~B/Andrew to rule)

The gap shrinks going back (the book was ~$354M of 1a in 2024-11 vs ~$1.35B
now — ~1/4 the size; proportionally fewer churning/missing accounts). It
asymptotes toward a small floor near 0, never negative. Candidate forms:

| option | form | trade-off |
|--------|------|-----------|
| **A — RPS uncalibrated** | calibrated_Schwab = RPS (no lift) for the `.031` range | Simplest + bounded error: the gap was only ~1.13% even at the 2026-01-16 overlap *start*, and shrinks backward toward 0. The deep-tail 1b is then RPS − 1a − 1c with a ≤~1% (declining) understatement, explicitly marked. No false precision. |
| **B — saturating/asymptotic lift** | a multiplicative gap that decays from ~1.13% (at 2026-01-16) toward a ~0 floor going back (e.g. exponential or book-size-scaled) | Closer to the true shape, but every parameter is itself unanchored — it is a model fitted to one endpoint + a zero-floor assumption. More machinery, not obviously more accurate than A. |
| C — extend the crosswalk back | re-derive silver/allocations pre-2026-01-16 | NOT available — allocations does not exist before 2026-01-16; out of reach. |

**Recommendation:** Option A (RPS uncalibrated, marked) for a `.031` deep tail
— the gap is small + bounded there, A introduces no unanchored parameters, and
the understatement is honest + marked. B is available if CTO~B wants the
shape-correction; C is impossible. **Whichever — the `.031` series is a
best-estimate, materially less precise than `.029`'s crosswalk-anchored
series; that should be explicit if Andrew greenlights it.**

## (d) Other `.031` Phase-0 items (flagged, not resolved here)

- **1c (SMA) for 2024:** `aum-timeseries.json` carries no SMA series; `.029`
  ratio-estimated 1c at 1.85% of 1a. If the SMA program had not launched by
  2024-11, 1c = 0 for the early `.031` dates — `.031` Phase 0 must determine
  the SMA-program start date before applying any 1c estimate.
- **2a (Inflection):** Inflection data starts ~2026-05-15 — so the **entire
  `.031` range is 49F-only** (1a + 1b + 1c, no 2a). Clean — no Inflection
  synthesis, consistent with `.029`'s pre-2026-05-15 handling.
- **Partition floor:** as with `.029`, year-end/holiday dates with no
  aggregate_aua partition would be honest gaps.

## Recommendation to CTO~B (for the Andrew decision)

The 2024-depth extension is **feasible to 2024-11-01** but the calibration is
**unanchored** — there is no crosswalk ground truth in-range, so a `.031`
series is a best-estimate, not a to-the-cent reconciliation. That is the key
fact for Andrew's greenlight call: `.031` would extend the Daily AUA chart
~13.5 months further with a *visibly-marked estimated* deep tail. If that
trade (more history, lower precision, explicit estimation markers) is
acceptable, `.031` is buildable — recommend Option A. If Andrew wants only
reconciled-to-the-cent history, the series correctly stops at `.029`'s
2025-12-23 floor.

This probe stands as `.031` Phase-0 method scoping if greenlit; no further
work pending the decision.
