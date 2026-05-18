# Session Log -- ADVI_INFGRO.007 window-TWR Axis-2 chain-link fix

**Agent:** 0.4.0_DS_ClientPlatform (DS~C lane)
**Date:** 2026-05-18
**TO:** ADVI_INFGRO.007 (ds-window-twr-axis2-chainlink-fix), issued by 2.0.0_SA_COO
**Project:** ADVI_INFGRO
**Ruling:** docs/briefs/infgro-window-twr-aggregation-ruling-20260515.md (1.0.0_SA_CTO)

---

## Current State

COMPLETE -- verified post-chain. INF_D_00c `_aggregate_gro_firm_window` and
`_aggregate_gro_per_advisor_window` rewritten to the two-axis window TWR.
Committed `2952a1bee`, pushed CLOUD, S3-deployed, ran in the 2026-05-18 16:28Z
INF chain. Post-chain `platinum/firm/leaderboard.json` verified -- the three
section-1 tells are inverted (see Post-chain verification below). AC1-AC6 met;
the aggregation algorithm fix is verified independent of the INF_C_02 input
correctness (that is INFGRO.009's scope). RAVC2 sent to COO.

---

## Phase 0 (recorded BEFORE implementation -- AC1)

### 0a -- GRAIN of `return_pct_twr`: per-period (daily) return -- CONFIRMED

Empirical probe of `s3://opal-data-inf/gold/timeseries/client_performance.parquet`
(418,685 rows, 296 households, 2,183 dates, 2020-05-26..2026-05-17):

1. **Partition spacing.** All 2,182 consecutive-date gaps = exactly 1 day.
   `client_performance.parquet` is contiguous daily -- no weekly/sparse grain.
2. **Consecutive-date values.** Sample households (388, 167, 68): `return_pct_twr`
   values are tiny (abs median 0.000508, abs p95 0.003495) and oscillate around
   0 day-to-day, with the SAME value repeating across the days of a week. That is
   the signature of a per-day geometric factor, NOT a cumulative-to-date level
   (a cumulative level would drift monotonically, not oscillate near 0).
3. **Upstream confirmation.** `silver/performance_dim/2026-05-13.parquet` carries
   `twr_factor_period` as a cumulative-to-date TWR factor (~1.065 for client 457
   = +6.5% inception-to-date). INF_C_02 `_build_daily_factor_table` extracts the
   per-day relative `f_curr / f_prior` (n_days = 1 because performance_dim is
   itself daily) and emits `return_pct_twr = daily_factor - 1`.

**Verdict:** per-period (daily) return -> CTO ruling section-3 step 1+2 verbatim:
`TWR_window = PRODUCT_t(1 + r_t) - 1`. Because the daily factors are the
`f_curr/f_prior` relatives, compounding them over a window telescopes back to the
real cumulative TWR (`f_end/f_start`) at the household level -- which is why the
fix recovers plausible, avg_twr_pct-scale numbers.

### 0b -- REUSE check: no reusable window-TWR producer

`_aggregate_perf_firm` / `_aggregate_perf_per_advisor` produce `avg_twr_pct` as a
simple **arithmetic mean of per-account `twr_value`** (a trailing snapshot TWR).
It is not window-parameterized, not AUA-weighted, and not chain-linked. It cannot
be reused for arbitrary QTD/YTD/MAX/1Y/3Y windows. The two-axis computation had
to be implemented in INF_D_00c.

### 0c -- FINDING B (epsilon-dominance): DISTINCT, root upstream in INF_C_02

epsilon-dominance reproduced: YTD-window `SUM epsilon_$` = $16.50M vs
`SUM return_$` = $2.21M, `SUM net_nna` = $4.33M -> **epsilon = 71.6%** of the
decomposition (matches the brief's 72-73%).

**Root cause (diagnosed):** a magnitude divergence between the two independent
sources feeding INF_C_02's decomposition `aua_change = nna + return + epsilon`:

- `aua_change` = day-over-day delta of `total_aua` (sum of account market values
  from `canonical_performance`) -- the full, real, lumpy daily AUA movement
  (e.g. HH 388: +$10.4K, +$19.3K, -$8.6K on consecutive days, $1.5M book).
- `return_$` = `prior_total_aua * return_pct_twr`, where `return_pct_twr` comes
  from `silver/performance_dim` TWR factors -- a much smaller, smoother modeled
  daily move (HH 388: ~-$240/day).

With `net_nna` = 0 on those days, `epsilon_$` absorbs almost the entire
`aua_change`. The leading hypothesis is **perf-coverage scope mismatch** (CTO
ruling section-4 candidate (i)): the performance TWR factors are computed over a
narrower account set (likely managed/advised accounts) than the `total_aua` sum,
so the modeled return cannot reconstruct the full-book AUA change. Secondary
possibility: the `household_id` <-> `client_id` cross-ID-space join in INF_C_02
(`_build_daily_factor_table` merge, INF_C_02.py:325-331).

**Disposition:** Finding B is upstream of INF_D_00c -- INF_D_00c only `.sum()`s
the `epsilon_$` column faithfully. The Axis-2 fix does NOT touch it. Per the TO,
NOT scope-crept here -- surfaced to COO as a separate INF_C_02-scoped item.
Finding B does **not** block AC4: compounding the daily factors telescopes to the
correct cumulative TWR regardless of the epsilon decomposition (the two are
different consumers of `return_pct_twr`).

**Staleness note:** `performance_dim` is 05-13-only, so `return_pct_twr` is NaN
for 2026-05-14..05-17 (the last 4 days). The chain-link skips NaN dates (they are
absent from the filtered rows -> no factor contribution) -- correct degradation;
the window TWR is exact through 05-13. Linked to the COO-tracked
bronze/performance `--run-date` catalog item.

---

## Phase 1 -- The Fix (AC2)

New helper `_window_twr_two_axis(rows)`:
- **Axis 1 (preserved):** within each date, `r_t = SUM_h(aua_h,t * r_h,t) / SUM_h(aua_h,t)`
  -- the AUA-weighted cross-sectional return. This was already correct.
- **Axis 2 (the fix):** `TWR_window = PRODUCT_t(1 + r_t) - 1` -- geometric
  chain-link of the per-date returns. Replaces the prior arithmetic mean.

Both `_aggregate_gro_firm_window` and `_aggregate_gro_per_advisor_window` now call
the helper (per-advisor passes the advisor-restricted household subset). The
helper is NaN-safe by construction: it filters to finite rows, divides only where
the per-date AUA denominator > 0, and returns `None` when no usable rows exist.

---

## AC4 -- Verification (pre-chain-run; firm function run against live S3 data)

Edited `_aggregate_gro_firm_window` invoked directly on the live
`client_performance.parquet`:

| Window | OLD firm_return_pct_twr | NEW firm_return_pct_twr | firm_return_$ |
|--------|------------------------|------------------------|---------------|
| QTD    | 0.038578%              | 1.694784%              | $3.25M        |
| YTD    | 0.009034%              | 1.154836%              | $2.21M        |
| 1Y     | 0.008266%              | 2.994432%              | $5.13M        |
| 3Y     | 0.006230%              | 6.939340%              | $9.61M        |
| MAX    | 0.004273%              | 12.380253%             | $10.14M       |

The three section-1 tells are inverted:
- **(a) monotonic in horizon:** MAX 12.38% > 3Y 6.94% > 1Y 2.99%. MAX is now the
  LARGEST (was the smallest at 0.004% -- the "impossible inception-to-date"
  pathology). QTD 1.69% > YTD 1.15% is the correct QTD-subset-of-YTD nesting (Q1
  was a net drag on the year) -- not a defect.
- **(b) %-consistent with cumulative return_$:** MAX is the largest in BOTH the %
  (12.38%) and the $ ($10.14M). Old: largest $ / smallest %.
- **(c) same scale as performance.avg_twr_pct (13.71/0.70/14.31):** MAX 12.38% is
  the same order of magnitude. Old 0.004% was 3 orders off.

Final post-chain-run verification on the materialized `leaderboard.json` is
carried in the RAVC2 after the co-land chain run.

---

## Compiler Tools

| Tool | Target | Result |
|------|--------|--------|
| `comp-pipescript io` | INF_D_00c.portal_leaderboard.py | No COLUMN GAPS. Tool's READS detection does not trace the helper-loaded `client_performance.parquet`; the COLUMN GAPS check was done empirically against the actual parquet schema (Phase 0 probe) -- `date`, `total_aua`, `return_pct_twr` all present. |
| `ds-commit-gate.sh` | INF_D_00c.portal_leaderboard.py | PASS (py_compile + AST undefined-name + ruff py39). |
| `comp-pipescript deployed` | INF_D_00c.portal_leaderboard.py | N/A -- tool is scoped to `s3://opal-data-bd/`; the orion script lives in `s3://opal-data-inf/`. Verified instead by direct `sha256sum`: committed file == S3 copy (`2b1e4d70...`). safe-deploy gate also PASS. |

---

## Files Modified

| File | Change |
|------|--------|
| data/orion/scripts/gold/INF_D_00c.portal_leaderboard.py | New `_window_twr_two_axis` helper (Axis-1 AUA-weighted per-date return + Axis-2 geometric chain-link). `_aggregate_gro_firm_window` + `_aggregate_gro_per_advisor_window` rewritten to call it. Replaces the single AUA-weighted arithmetic mean over all (household, date) rows. |

---

## Deploy Cycle

| Step | Result |
|------|--------|
| Pre-commit gate | ds-commit-gate.sh PASS |
| Commit SHA | 2952a1bee |
| Push | origin/CLOUD da15b8cc5..2952a1bee |
| S3 deploy | s3://opal-data-inf/code/gold/INF_D_00c.portal_leaderboard.py (safe-deploy auto, sha256 2b1e4d70... MATCH) |
| INF gold chain run | HELD for the ADVI_BIWNDW.002 co-land (one chain cycle for both), separate from + after the in-flight INFDRF P0 rerun -- COO-coordinated |

---

## Next Steps

| Recipient | Item |
|-----------|------|
| **COO 2.0.0** | RAVC2 -- AC1/AC2/AC3/AC5 PASS; AC4 pre-run evidence strong, final verification post-chain-run; AC6 co-land code ready (INFGRO.007 `2952a1bee` + BIWNDW.002 `a2010a2b3` both in INF_D_00c on CLOUD+S3). Trigger ONE INF gold chain run (separate from / after the INFDRF P0 rerun) to materialize both. |
| **COO 2.0.0** | FINDING B -- separate INF_C_02-scoped item: epsilon-dominance (71.6% YTD) root = perf-coverage scope mismatch between `total_aua` (full book) and the performance_dim TWR factors. Gates INFGRO.005 partner-facing close criterion (b). |
| **CTO 1.0.0** | CC on RAVC2 -- ruling author; grain confirmed per-period daily, section-3 step 1+2 applied verbatim. |
| **DE 0.4.0** | CC on RAVC2 -- INFGRO.005/.006 gate owner. This TO delivers .005 criterion (a) plausible TWRs; criterion (b) epsilon depends on the separate Finding B item. |

---

## Post-chain verification + RAVC2 close (2026-05-18 chain 16:28Z)

The INFGRO co-land chain (`chain_full_20260518_153102`, completed 16:28:56Z) ran
INF_D_00c with the `2952a1bee` two-axis fix. Verified the materialized
`s3://opal-data-inf/platinum/firm/leaderboard.json` (generated_at 16:26:19Z).

Firm `firm_return_pct_twr` / `firm_return_$` by window:

| Window | firm_return_pct_twr | firm_return_$ |
|--------|--------------------|--------------|
| QTD | 1.694784% | $3.25M |
| YTD | 1.154836% | $2.21M |
| 1Y  | 3.001783% | $5.14M |
| 3Y  | 7.007731% | $9.68M |
| MAX | 12.380253% | $10.14M |

The three section-1 tells are inverted (AC4 PASS):
- (a) dilution bug GONE -- MAX is the largest (was 0.0043% smallest); TWRs grow
  with window length YTD<1Y<3Y<MAX. QTD>YTD is an arithmetically-consistent
  -0.53% Q1-2026 drawdown ((1.0115/1.0169)-1), not the bug.
- (b) %/$ consistent -- same QTD>YTD<1Y<3Y<MAX shape in both.
- (c) advisor return_pct_twr same order of magnitude as performance.avg_twr_pct
  (Joe Brandenburg MAX 13.41% vs avg 13.70%; Peter Lee MAX 11.09% vs 13.21%) --
  was 3 orders of magnitude off.

**.005 gate disposition (AC6):** gate (a) plausible TWRs -- clear in SHAPE; the
absolute scale is still understated because the chain ran INF_C_02 on old perf
bronze (INFGRO.009 did not materialize -- see that TO's log). Gate (b) epsilon
no longer dominant -- NOT cleared; firm_epsilon_$ YTD still 71.6%. Both fully
resolve on the INFGRO.009 clean re-run. INFGRO.007's own scope (the Axis-2
aggregation algorithm) is verified complete and does not regress on the re-run.

**RAVC2 ACCEPTED + CLOSED by COO 2026-05-18.** TO status -> complete.
