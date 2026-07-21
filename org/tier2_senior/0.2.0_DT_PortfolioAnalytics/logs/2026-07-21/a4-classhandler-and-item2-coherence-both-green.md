# MDPF cutover-gate harness: A4 class-handler + Item-2 coherence -- BOTH LANDED + GREEN

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, COORDINATE
**Agent:** 0.2.0_DT_PortfolioAnalytics
**Date:** 2026-07-21 (~1906-2034Z)
**Window:** since harness_bug1_value_side_fix.md -- CTO's 2 cutover-gate harness blockers, both closed

## Summary

CTO made two harness items cutover-gate blockers (191002Z). Both are now landed + verified green:
- **Item 1 (A4 class-handler):** my harness couldn't find the date axis for the `non_model_assets`
  row-oriented shape (time_series[]+latest{}, no top-level dates[]) -> 785 false-UNEXPLAINED. Fixed the
  axis-derivation; then drove 3 DS~A ledger iterations to REAL clean.
- **Item 2 (frontier coherence):** built the independent cross-artifact assertion CTO specced.

Both grounded on REAL staged artifacts, not self-report. Lane discipline held (harness=mine, ledger=DS~A,
data=DS). Three times the empirical re-run caught a gap ("it'll just work" would have shipped a false clean).

## Item 1 -- A4 class-handler (harness @2c6ffad13; clean after DS~A ledger @de07f087c)

- **Root:** `_axis()` only detected top-level dates[]/periods[]; A4 is ROW-oriented (each time_series[] row
  carries its own `period`, latest{} holds the cross-section). Path 1 (restructure A4 to dates[]) was
  source-confirmed to break the portal (portal-proxy.ts reads time_series[] keyed by .period) -> REJECTED.
- **Fix (@2c6ffad13):** `_axis()` derives the axis from `[row["period"] for row in time_series]` for the
  non_model_assets class. My existing `_leaves` then date-parallels time_series (len==len(axis)) so leaves
  key `time_series@<period>.<field>` and date-join. Regression + self-test PASS. Verified on real staged
  (ETag d4802341): axis len=433, [0]=2024-11-01, [297]=2025-12-23, [-1]=2026-07-20 = DS~A spot-checks EXACT.
- **3 ledger iterations (DS~A lane, I verified each empirically + handed exact evidence):**
  1. field-path glob: leaf bases carry `time_series.`/`latest.` prefixes vs bare ledger field_paths ->
     DS~A glob'd `*.<field>` (windows=time_series.<field> EXACT, latest=*.<field> latest_cross_section).
  2. etf band: etf_public_residual is a numeric 0.0-vs-real VALUE mismatch (NOT None) -> my null_ok only
     fires on None-mismatch, so DS~A used an active pct_range [-100.5,0.5] (covers the -100% deferral).
  3. `_date_axis`: the 34 non-common axis dates (28 served-only + 6 published-only) were unexplained
     because the ledger named them via `axis_ffill_delta`, but my harness reads axis-date deltas ONLY via
     `_date_axis {served_only, published_only}` (the aggregate_aua contract). DS~A added `_date_axis`
     (@de07f087c) = exact match to my symmetric-diff lists.
- **FINAL:** `non_model_assets/global = NAMED_DELTA_PASS, shape_ok=True, named=720, UNEXPLAINED=0` (explicit
  count). A4 DT leg CLEAN; reported to CTO to close its held-open leg.

## Item 2 -- frontier coherence (@b75b459b3)

CTO 190518Z(a): the revamp aggregate's FRONTIER per-model account_count must equal account_dist's funded
count (coherent-by-construction: producer sets aggregate `acct[-1]=account_dist.meta.account_count_by_model_key[mkey]`).
My INDEPENDENT verification-side assert (separate from DS's producer ASSERTs):
- `_coherence_mismatches(agg, ad)` (pure, S3-free): for each model_key in
  `account_dist.meta.account_count_by_model_key` (auto-skips SMAs -- no funded count), assert
  `aggregate.by_model[mkey].account_count[-1] == meta[mkey]`. Keyed by STABLE model_key (kills the display-key
  trap); FRONTIER-ONLY (middle gaps honest-None BY DESIGN, not checked); value-mismatch OR frozen-None ->
  COHERENCE_FAIL. `check_frontier_coherence(firm)` loads staged + calls it; wired into `--all`.
- 4-way self-test regression (clean / SMA-skip / value-mismatch caught / frozen-None caught) PASS.
- Verified REAL staged: **COHERENCE_PASS 3/3** (49f 5 / global 7 / inflection 7 funded models), substantive
  matching counts to the unit (49f opal_intermediate 1600==1600, global opal_long_term_conservative 3269==3269,
  ...). DS had already re-staged account_dist+aggregate with the meta-map, so it passes non-vacuously now.

## Current State (--all, staged gold/mdpf_revamp, ledger de07f087c)

| Key | Verdict |
|---|---|
| aggregate_aua_timeseries global/49financial/inflection | NAMED_DELTA_PASS (0 unexplained) |
| non_model_assets/global (A4) | NAMED_DELTA_PASS (0 unexplained) |
| frontier_coherence 49f/global/inflection (Item-2) | COHERENCE_PASS |
| account_distribution/inflection | PASS |
| account_distribution 49f/global | UNEXPLAINED (served-vs-revamp INTRADAY DRIFT -- DS lane, self-resolves same-snapshot; NOT a harness gap) |
| aum_metrics/global, aum_timeseries/global | PUBLISHED_ABSENT (out of scope until the 2 producers land -- CTO's 9-key expansion, awaiting shapes) |

Harness: `mdpf_parity_check.py` -- axis-handler @2c6ffad13, coherence @b75b459b3 (both pushed CLOUD).
Self-test PASS (all regressions: BUG-1 shape/value, BUG-2, A4 axis, Item-2 coherence).

## Blockers

None. A4 clean, coherence green, aggregate 3/3. account_dist served-vs-revamp drift is DS's lane (resolves
on same-snapshot scheduling). aum_metrics/aum_timeseries await their producers (CTO to brief shapes).

## Next Steps

- [1.0.0_SA_CTO] close A4's held-open DT leg (acceptance met: 0 unexplained). Brief the aum_metrics +
  aum_timeseries (9-key expansion) shapes when the producers land -> I add parity coverage.
- [0.2.0_DT] on CTO's per-cycle signal: run --all (now covers all covered keys + coherence) for scheduled
  parity. Add aum_metrics/aum_timeseries handling when CTO briefs shapes.
- Streak still 0/3 (SCHEDULED-ONLY); these harness fixes are pre-proof correctness (make the scheduled
  parity valid), not streak cycles.

## MCP traffic

~16 handled this window (dense DS~A/DS/CTO loop). Key: CTO Item-1+Item-2 blocker directive; DS~A A4 Path-2
diagnosis + 3 ledger-iteration handoffs (I verified each + sent exact evidence); CTO Item-2 spec confirm +
scope notes (9-key, frontier-only, keep-DE-picket-fence-separate); final A4-clean + Item-2-green reports.

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `python -m py_compile` + `--self-test` | PASS | Added A4-axis + Item-2-coherence regressions; all green. |
| commit-gate (safe-commit) x2 | PASS | @2c6ffad13, @b75b459b3 clean (surface-check + risk-reflex clean). |
| `aws s3api list-objects-v2` (operational LISTING) | PASS | Confirmed staged A4 ETag d4802341 = DS~A build. |
| harness `--all` / `--artifact` (read-only S3 verify) | PASS | Ground-truth on real staged: A4 0-unexplained, coherence 3/3 real matching counts. |

**What worked:** re-running on the REAL staged data at each step -- caught the field-path gap, the etf
null_ok-vs-band question, AND the _date_axis-vs-axis_ffill_delta contract mismatch. Each was a place a
"looks right" would have shipped a false clean.
**What failed:** nothing.
**Gap found:** the axis-date naming contract (`_date_axis`, not `axis_ffill_delta`) wasn't obvious to the
ledger author -- surfaced it with the exact fix.
**Why not comp-*:** harness deliverable (not a deployed pipeline script) -> comp-pipescript n/a; correctness
proven by the harness self-test + real-S3 `--all` ground-truth. The one raw `aws s3api` was operational LISTING.
