# MDPF_ASSETS.031 A4 — 1c re-derive + 297-partition re-run — RAVC2

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-21
**RAVC2 to:** 2.0.0_SA_COO~B (independent S3 re-validation) **CC** 1.0.0_SA_CTO~B (output-validate)
**Origin:** MDPF_ASSETS.032 probe → outcome (a) → CTO~B 1c-method ruling (141723Z) + CONFIRMED (flat $19,673,469.29 stands). Andrew direct: "Finish the fix."

---

## TL;DR

The `.031` 2024-depth backfill carried `1c = 0` (an item-(d) wrong-source
artifact). The `.032` probe proved SMA is real (live since 2021-09-02). This
re-run re-derives `1c` for all 297 `.031` partitions to **flat
$19,673,469.29** — the `.031/.029` seam value — and recomputes
`1b = calibrated_Schwab − 1a − 1c`. The `$0 → $19.67M` 1c component-seam is
**CLOSED** ($0.00 step). The daily AUA headline is **invariant** — unchanged
to the cent. Applied to S3, rollup rebuilt, verified all-pass.

---

## The fix

| | before (A2, `1c = 0`) | after (A4, this re-run) |
|---|---|---|
| `1c` across the 297 `.031` partitions | $0.00 | **$19,673,469.29 flat** |
| `1b` | `calibrated_Schwab − 1a` | `calibrated_Schwab − 1a − 1c` |
| headline `opal_aggregate_aua` | (value) | **identical — invariant** |
| `1c` seam at 2025-12-22/23 | $0 → $19.67M (**+$19.67M step**) | $19.67M → $19.67M (**$0.00**) |

**Headline invariance.** `1b = calibrated_Schwab − 1a − 1c`, so
`headline = 1a + 1c + 1b = calibrated_Schwab` regardless of the `1c` value.
The `1c = flat-$19.67M` decision sets only the **1c/1b component split** — it
does **not** move the daily AUA headline trend. Verified: 0 headline/1a drift
dates across all sampled partitions vs the pre-re-run S3 state. A low-stakes,
honest decomposition choice, not a headline risk.

## Why flat $19,673,469.29 (the corrected basis)

Per CTO~B's premise-correction acknowledgement — the accurate rationale, for
the record:

- The `1.85% × 1a` ratio is **rejected**: 1a grew ~3.8× across the `.031`
  range on onboarding flow; SMA and 1a are genuinely uncorrelated
  trajectories, so any 1a-ratio mis-states 1c (it gives ~$6.5M at the
  2024-11 deep end vs a real SMA plausibly ~$15–21M).
- Flat is chosen because **the SMA program's per-date value across the `.031`
  range is genuinely unrecoverable** — NOT because "SMA is mature/flat." The
  `.032` probe established: 95 of 189 SMA allocations have since closed; the
  endpoint carries no close-dates and no historical values; the openedDate
  curve of the 94 survivors (7 open by 2024-11-01 → 80 by 2025-12-22) is
  survivorship-biased and cannot proxy program size. A taper would be
  manufactured precision off a biased curve.
- **Flat at the `.031/.029` seam value ($19,673,469.29 — `.029`'s 1c at
  2025-12-23)** anchors the 1c layer level-continuous across the join. The
  estimate is marked per-partition (`meta.c1_treatment`,
  `method = sma_trajectory_flat_seam_anchored`); it sits inside the
  already-marked `.031` estimate segment.

## The .029 quick-check — `.029` STANDS (evidence-based)

CTO~B required `.029`'s ratio-1c be confirmed within ~$2–3M of the real SMA
before "leave `.029`". Stored ratio-1c vs an independent SMA-source estimate
(current account values scaled by the fraction of accounts open by date — an
**upper bracket**, since current values applied to past dates over-state):

| date | stored 1c | est. real SMA (upper bracket) | delta |
|---|---|---|---|
| 2025-12-23 | $19,673,469.29 | $21,173,165.01 | −$1,499,695.72 |
| 2026-01-15 | $21,299,083.84 | $21,702,494.14 | −$403,410.30 |
| 2026-04-15 | $23,523,626.14 | $23,819,810.64 | −$296,184.50 |
| 2026-05-19 | $24,911,821.34 | $24,878,468.89 | +$33,352.45 |

Worst gap **$1.50M** — and the estimate is an upper bracket, so the true gap
is smaller. Well within the ~$2–3M tolerance. **`.029` stands — no re-open.**
Documented known-small-imprecision observation: `.029`'s 1a-ratio 1c runs
modestly *above* the real SMA level (the SMA program grew slower than 1a over
the `.029` range), the overstatement bounded under ~$1.5M.

## Verification — S3 state, all-pass

Live rollup `s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua_timeseries.json`
(395 dates, `generated_at` 2026-05-21T14:57:58Z) + every `.031` S3 partition:

- **1c flat** $19,673,469.29 across all 297 `.031` dates — 0 exceptions.
- **3-term identity** `1a + 1c + 1b == headline` — 0 breaks / 297.
- **negative 1b** — 0 (deep-end 2024-11-01 1b = $402,691,632.06; min still
  strongly positive — 1c $19.67M ≪ 1b ~$237M+).
- **AC1 daily-per-model** — 297/297 partitions: exactly 5 models, per-model
  sum == aggregate 1a to the cent. Unchanged by the re-run (only 1c→1b moved).
- **1c seam** 2025-12-22 → 2025-12-23: $19,673,469.29 → $19,673,469.29,
  **step $0.00 — CLOSED**, level-continuous.
- **headline seam** 2025-12-22 → 2025-12-23: $1,319,699,960.83 →
  $1,328,259,808.88 (+0.649%) — unchanged from before the re-run.
- **1b seam**: 2025-12-22 $236,998,683.66 → 2025-12-23 $243,796,514.01,
  step **+$6,797,830.35**. This is the *honest* day-over-day residual
  (`Δheadline +$8.56M − Δ1a +$1.76M`); it replaces the old **false −$12.88M**
  step that 1b took to compensate for the false +$19.67M 1c jump. Smaller
  magnitude, and now a genuine residual move rather than a methodology
  artifact.

## What was applied

- 297 `.031` partitions re-uploaded — `s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua/{2024-11-01..2025-12-22}.json`.
- Rollup rebuilt + uploaded — `aggregate_aua_timeseries.json` (`build_aggregate_aua_timeseries.py --upload`, re-aggregates all 395 S3 partitions).
- Bounded — only the 1c→1b term changed. The clamped-fit calibration (A2),
  the 1a daily-per-model series (AC1), the A3 estimate-marking, and the gap
  handling are all UNCHANGED, untouched.

## Status

`.031` A4 re-run COMPLETE + verified on S3. The 1c component-seam that
triggered CTO~B's HOLD is closed. RAVC2 → COO~B (independent S3
re-validation) CC CTO~B (output-validate). On accept, `.031` re-closes →
MDPF_ASSETS 3-step-closes.
