# REVIEW -- validate_sl_nightly_gate.py

- script: `data/cot/scripts/gold/validate_sl_nightly_gate.py`
- verdict: **issues-found**
- runs_in_incremental: False
- findings: 4

## Finding 1 -- [high/other/both]
- **Location:** `validate_sl_nightly_gate.py:35-38 (JONES_ACCOUNT_ID / JONES_EXPECTED_CASH_MV / FIRM_MV_BASELINE), consumed in check_jones:69-99 and check_firm_mv:152-160`
- **Mechanism:** This validator was cloned from the 49F/bd ADVI_ROLLUP pipeline with only S3_BUCKET swapped to opal-data-cot; the gate fixtures were NOT re-derived for Cottonwood. JONES_ACCOUNT_ID='z0817905851', JONES_EXPECTED_CASH_MV=21060.0, and FIRM_MV_BASELINE=15_900_000.0 are 49F/bd values (they appear nowhere else in the entire cot tree -- only in this file). check_jones() looks up account z0817905851 in the cot shadow; check_firm_mv() compares cot firm MV against a 49F AUM baseline of $15.9M.
- **Failure scenario:** Run `python3 validate_sl_nightly_gate.py` against opal-data-cot: Assertion 1 returns 'no rows in shadow parquet' because Cottonwood account z0817905851 does not exist in the cot shadow -> permanent FAIL, so the 3-nightly gate can never reach 3/3 and SL-P2 PROMOTE is permanently blocked (or, if a cot account by that id did exist, its cash MV would be compared to an unrelated $21,060 target). Assertion 3 compares Cottonwood's firm MV to a 49F $15.9M baseline -- if cot AUA is below $15.9M it always FAILs, if above it always PASSes, so the check is meaningless for cot either way.
- **Proposed fix:** Re-derive all three fixtures for Cottonwood (a real cot account id + its expected cash MV, and cot's actual pre/post-fix firm-MV baseline), or delete the file as a dead 49F import if the SL nightly gate does not apply to the cot firm.

## Finding 2 -- [medium/empty-null-handling/both]
- **Location:** `check_pure_sleeve:110-149 (except->{} at 123-126; None->continue at 136-138; all_pass default True at 127/149)`
- **Mechanism:** Assertion 2's all_pass is initialized True and only ever set False on an explicit delta breach. If the silver/allocations read fails (NoSuchKey / wrong date / missing 'account_market_value' column) the except clause sets alloc_mv={}; every sampled account then resolves silver_mv=None -> logs a WARN 'cannot compare' and `continue`s, never touching all_pass. Same when the pure-sleeve `sample` is empty (a firm with no uln_sleeve_apportion rows): the loop body never runs. Either way check_pure_sleeve returns True (PASS) having compared ZERO accounts.
- **Failure scenario:** The auto-detected shadow date_str has no matching silver/allocations/{date}.parquet (date-convention skew, or the cot silver partition simply isn't present for that day) -> alloc read raises -> alloc_mv={} -> all 3 sampled accounts log 'cannot compare' -> check_pure_sleeve returns True. Assertion 2 is reported as PASS in the 'N/3 PASS' tally while it validated no MV parity at all, letting a vacuous nightly count toward authorizing the PROMOTE gate.
- **Proposed fix:** Require at least one successfully-compared account for Assertion 2 to PASS: track a compared-count and return False (or a distinct NOT-VALIDATED state) when it is zero, instead of defaulting all_pass=True; treat an empty sample and an unavailable alloc parquet as non-PASS.

## Finding 3 -- [low/other/both]
- **Location:** `_latest_shadow_date:54-61`
- **Mechanism:** list_objects_v2 returns at most 1000 keys per page in lexicographic ASCENDING order and IsTruncated/ContinuationToken is not handled. Keys are 'gold/timeseries/holdings_lots_shadow/YYYY-MM-DD.parquet', so the first page holds the OLDEST 1000 dates. `keys.sort(reverse=True); keys[0]` then picks the max WITHIN the first page only, which is an old date, not the true latest.
- **Failure scenario:** After ~1000 daily shadow emissions accumulate (~2.7 years), invoking the validator without --date returns e.g. the 1000th-oldest date instead of today's; the gate then validates a stale shadow parquet and renders a PASS/FAIL for the wrong day while claiming 'Auto-detected latest shadow date'.
- **Proposed fix:** Paginate the listing (get_paginator('list_objects_v2')) and take the max across all pages, or list with StartAfter to walk to the tail; do not rely on a single un-paginated first page.

## Finding 4 -- [low/type-issue/both]
- **Location:** `check_jones:75, check_pure_sleeve:103, check_firm_mv:153 (`shadow[shadow["is_open"]]`)`
- **Mechanism:** The three checks boolean-mask on the raw is_open column with no fillna/astype. The producer of this shadow (B_01.holdings_lots.py) itself defensively coerces `df['is_open'].fillna(False).astype(bool)` (line 1226), which is direct evidence is_open can carry NA / object dtype in this lineage. If the persisted shadow's is_open is nullable-boolean or object-with-NaN, `df[mask]` raises ValueError 'cannot mask with non-boolean array containing NA / non-bool values'.
- **Failure scenario:** A shadow parquet where any is_open cell is pd.NA (or the column persisted as object with a NaN) -> the very first `shadow[shadow["is_open"]]` in check_jones raises ValueError -> main() propagates an uncaught exception and the gate exits with a traceback instead of a verdict. (Contingent on the persisted dtype, which I could not verify against the served artifact.)
- **Proposed fix:** Mask with `shadow["is_open"].fillna(False).astype(bool)` in all three checks to match the producer's own is_open contract, rather than assuming a clean numpy-bool column.
