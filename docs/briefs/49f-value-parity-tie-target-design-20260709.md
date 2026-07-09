# 49F value-parity TIE-TARGET -- pre-staged design (ready to demonstrate once the freeze clears)

**Status:** DESIGN ready; DEMONSTRATION blocked on live (non-frozen) BD data --
gated behind 0.6.0_AE_PartnerETL's ADVI_BDAPIMIG freeze-root fix. Per CTO's
073142Z disposition (decomposition-reconcile, not exact-tie) + COO's
083510Z ask to pre-stage so turnaround collapses to near-zero once the gate
clears. Author: 0.4.0_DS_ClientPlatform~A.

## Recap: why an exact tie is unsound

`cert.gold_aua` (`C_02.client_performance.py:307`, `SUM(total_aua)` at the
latest date) is an **account-level derived AUA**, not a positions sum. It
differs from `SUM(gold/canonical/holdings/{date}.market_value)` by
construction. CVO~B + CTO + I independently confirmed (2026-07-09) an exact
tie would cry-wolf on every normal day.

## The reconcile formula

```
gold_aua == positions.market_value + known_gap(date)      [within tolerance]
```

where `positions.market_value` = `SUM(gold/canonical/holdings/{date}.market_value)`
(the SAME anchor the Terraform config already defines for 49F:
`gold/canonical/holdings/{date}.parquet`, column `market_value`) and
`known_gap(date)` is a DECOMPOSED, EXPLAINED quantity -- not a fixed offset,
not a rough ~5% assumption. The guard fires only when the ACTUAL gap deviates
from its EXPECTED decomposition beyond tolerance -- a real divergence, not
the expected daily gap itself.

## What `known_gap` actually decomposes into -- CORRECTED from the original framing

**The original framing (CTO's message, CVO~B's routing) assumed reusing
`E_00.decompose_aua_gap.py` / `E_05.gap_by_pricing_source.py` /
`E_07.account_gap_buckets.py` as-is.** I traced these scripts directly
(2026-07-09) and found they decompose a **DIFFERENT gap** than the one this
guard needs:

- E_00/E_05 compare `gold_mv` (positions_cube x canonical_prices, an
  independent position-level valuation) against `silver_mv`
  (`silver/allocations`, BD's own custodian-reported market value) --
  **NOT** `gold_aua` (C_02's account-derived total_aua) against
  `positions.market_value`. Different pair of quantities entirely, despite
  overlapping vocabulary ("gold", "gap").
- **`silver/allocations` is the SAME feed currently frozen** (this session's
  other finding) -- so E_00/E_05, run as-is today, would decompose against a
  degenerate/empty silver side. They cannot be reused unmodified; they need
  either (a) repointing at `positions.market_value` as the comparison
  baseline instead of `silver_mv`, or (b) waiting until BOTH silver/allocations
  AND the tie-target question are live -- but (b) conflates two problems
  needlessly. Recommend (a).

**Traced the REAL construction of `gold_aua` instead** (`C_02.client_performance.py`
-> `load_performance_partitions()` -> `C_00.canonical_performance.py` ->
`B_03.account_gains.py`):
- `B_03:222` -- `aua_current = h_current.groupby('account_id')['market_value'].sum()`
  where `h_current = _read_s3(canonical_holdings_key(date_str))` -- this is
  **the exact same `gold/canonical/holdings/{date}.parquet`** the value-parity
  anchor already reads. At THIS layer, account-level `aua_current` is a pure,
  unfiltered positions sum -- no cash-flow/override/valuation-source
  adjustment happens here (contrary to CVO~B's original characterization).
- `C_00.main()` then joins `account_gains` to `accounts_dimension`
  (`acct_dim = accts[dim_cols].drop_duplicates('account_id')`) before
  producing the `client_performance` output C_02 consumes.

**Working hypothesis for `known_gap`'s real composition (needs live-data
confirmation, listed in priority order):**
1. **Account-coverage gap** -- accounts present in `canonical_holdings`
   (contributing to `positions.market_value`) but ABSENT from
   `accounts_dimension` (dropped by the C_00 join) never reach `total_aua`.
   This is the most likely primary driver given the join structure traced
   above -- directly analogous to E_00's own "gold_only"/"silver_only"
   account-coverage buckets, just on a different axis (holdings-vs-dimension,
   not gold-vs-silver).
2. **Timing/vintage skew** -- if `account_gains` for the served date lags the
   `canonical_holdings` partition for the same nominal date (an incremental-
   pipeline vintage mismatch, the same CLASS of issue the inf AUA thread
   surfaced tonight), gold_aua could reflect a slightly earlier or later
   positions snapshot than the anchor.
3. **Relationship-level exclusions** -- `write_aua_certification`'s own
   `LIABILITY_TYPES` exclusion (CreditCard/Mortgage/Loans, `C_02:295,325-326`)
   applies to `certified_aua`, not `gold_aua`/`total_aua` -- confirmed NOT a
   factor for THIS specific comparison (gold_aua has no liability exclusion
   applied), but worth naming so it isn't wrongly invoked as an explanation.

**This is a hypothesis ranking, not a demonstrated decomposition** -- the
DEMONSTRATION step (below) confirms or corrects it against live data.

## The demonstration plan (run once BD's export resumes + a few live days accumulate)

1. Pick a recent date where BOTH `gold/canonical/holdings/{date}.parquet` and
   a fresh `client_performance.parquet` total_aua exist.
2. Compute `positions.market_value` (direct sum, matches Terraform anchor)
   and `gold_aua` (`total_aua` sum at that date) -- confirm the gap magnitude
   is stable/explicable day-over-day (not wildly swinging, which would
   suggest a timing/vintage bug rather than a structural account-coverage
   gap).
3. Adapt `E_00.decompose_aua_gap.py`'s account-level join methodology
   (its `acct.merge(..., how='outer')` + `gold_only`/`silver_only` coverage
   split, `E_00.py:174,196-199`) to compare `canonical_holdings` accounts
   against `accounts_dimension` accounts directly -- reusing the SHAPE of
   E_00's analysis, pointed at the right pair. Quantify: how much of the
   gap is "gold_only" accounts (in holdings, absent from account_gains/
   dimension) vs. a smaller residual.
4. If account-coverage explains the gap to within a declared tolerance
   (recommend starting narrow, e.g. 0.1-0.5% of AUA, tightened once the
   decomposition is proven stable across several days) -- that decomposition
   IS `known_gap(date)`, computed fresh each day, not a fixed constant.
5. If a residual remains unexplained after account-coverage, investigate
   timing/vintage (hypothesis 2) before concluding the reconcile is unsound.

## The guard implementation shape (once demonstrated)

`value_parity_reader.py` already has a CERT-MODE path (`_run_cert_mode`,
built for 49F specifically -- `VP_CERT_KEY_TPL` set) with a 3-part design:
position-parity (exact-match) + cert-gap-drift (banded) + broken-cert guard.
The decomposition-reconcile fits naturally as an EXTENSION of the existing
cert-gap-drift concept: instead of comparing `gap_pct` against a static
`VP_CERT_GAP_EXPECTED`/`VP_CERT_GAP_TOLERANCE` baseline (currently unset,
UNVERIFIABLE), compute the EXPECTED gap FRESH each run from the account-
coverage decomposition (step 3-4 above) and compare the ACTUAL served gap
against that computed expectation, banded by a declared tolerance. This
reuses the existing cert-mode plumbing (`_read_cert`, `_anchor_sum`) --
the new piece is a `_expected_gap(as_of)` function implementing the
demonstrated decomposition, called in place of the static
`VP_CERT_GAP_EXPECTED` constant.

## Explicit dependency on the freeze-fix

None of steps 1-5 can run meaningfully while `silver/allocations` is empty
AND `certified_aua` is degenerate -- not because the reconcile needs
`certified_aua` directly (it doesn't; the reconcile is gold_aua vs positions,
orthogonal to the cert/silver axis), but because **the served figure itself
is currently a frozen 3-week-old hold**, and demonstrating a "does today's
served figure reconcile" check against a value that isn't actually today's
requires the served plane to be live first. Once 0.6.0's freeze-root fix
lands and `write_aua_certification` resumes computing `certified_aua` live,
this design is ready to demonstrate immediately -- no further design work
needed, only live-data execution of steps 1-5.

## Open item for CTO (flag, not decided here)

The account-coverage-gap hypothesis (my #1) would mean the "known gap" is
really a DATA-COMPLETENESS issue (accounts_dimension missing accounts that
genuinely hold assets) rather than a benign, expected methodology difference.
If confirmed, that may warrant its own fix (closing the accounts_dimension
coverage gap) independent of the value-parity guard -- the guard would then
be validating against a gap that itself represents a data quality issue,
which is worth naming explicitly once demonstrated rather than quietly
building a tolerance band around a real completeness problem.
