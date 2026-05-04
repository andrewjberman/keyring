# Session Log — DS~C SL-P1c Shadow Emission Root Cause Investigation

**Agent:** 0.4.0_DS_ClientPlatform~C
**Date:** 2026-05-04
**Session type:** Root cause investigation (shadow stopped emitting 2026-04-22)
**TO:** ADVI_ROLLUP.SL-P1c.b01-denominator-fix

---

## Summary

Full two-phase root cause identified for shadow emission stopping on 2026-04-22.
Shadow has not emitted since 2026-04-21 (last file at `gold/timeseries/holdings_lots_shadow/2026-04-21.parquet`).

---

## Shadow Emission Timeline

| Date | Holdings Lots | Shadow | Code on S3 |
|------|--------------|--------|------------|
| 2026-04-21 | Produced 00:26:14Z | Produced 00:26:17Z | HLOT2b (`8a3dc16c`) |
| 2026-04-22 | Produced 00:26:07Z | MISSING | HLOT2b (`8a3dc16c`) |
| 2026-04-23 through 2026-04-29 | Produced nightly | MISSING | HLOT2b / bond-classify |
| 2026-04-30 | Produced 11:59:20Z | MISSING | Fix B+C (`01d18398`) |

---

## Phase 1 Root Cause: pandas 2.3.3 `is_in_axis` ValueError (2026-04-22 to 2026-04-30)

### What changed: 74dbad2ba (HLOT2b, uploaded 2026-04-21T18:55Z)

Commit 74dbad2ba fixed `_build_authoritative_reopen_lots` to correctly derive CUSIPs
via `bd_assets_dim` ticker join, allowing the function to produce `silver_unrealized_reopen`
and `canonical_holdings_reopen` lots that previously produced zero.

**Effect on df passed to _build_uln_sleeve_lots:**

| Date | `silver_unrealized_reopen` lots (sleeve) | `canonical_holdings_reopen` lots (sleeve) | FIFO open set |
|------|------------------------------------------|-------------------------------------------|---------------|
| 2026-04-21 | 0 | 0 | 9,407 pairs |
| 2026-04-22 | 609 | 99 | 10,109 pairs |

The 708 new reopen lots were drawn from the same ULN source (`silver/unrealized/2026-04-22`)
that the sleeve shadow reads. These entries are the same (acct_id, asset_name) pairs as
non-cash ULN positions for sleeve accounts.

### The pandas bug

Pre-Fix-C code in `_build_uln_sleeve_lots` (lines 955-961):
```python
_fifo_sleeve = df[df['account_id'].astype(str).str.strip().isin(sleeve_accounts)]  # no .copy()
fifo_mv_by_acct = (
    _fifo_sleeve.groupby(_fifo_sleeve['account_id'].astype(str).str.strip())['market_value']
    #           ^--- pandas Series key, NOT a column name string
    .sum().to_dict()
)
```

On pandas 2.3.3, using a Series as a groupby key on a DataFrame that was sliced (not copied)
triggers an `is_in_axis` ValueError. This ValueError was caught by the outer try/except at
lines 2836-2854:
```python
try:
    ...
    uln_lots = _build_uln_sleeve_lots(...)
    ...
except Exception as e:
    print(f"  [ULN sleeve shadow pass failed] {e} -- shadow artifact not produced")
```

The exception was printed but swallowed — the shadow was not stored in `df.attrs` and not
written. EC2 nightly logs contain the exact error string but are not accessible locally.

### Why 2026-04-21 succeeded

The 2026-04-21 nightly ran with the same HLOT2b code on S3 (uploaded 18:55Z April 21, before
the 00:26Z nightly). However, the 2026-04-21 snapshot used `silver/unrealized/2026-04-20.parquet`
(delta=1, since 2026-04-21.parquet does not exist). The 2026-04-20 ULN data produced zero
`silver_unrealized_reopen` lots for sleeve accounts, leaving `df` in the shape that did NOT
trigger the pandas groupby Series bug. The 2026-04-22 ULN (larger, different partition) did.

**Fix C (040c81b4f, 2026-05-01)** resolved this by adding `.copy()` and switching to
string column key `'_acct_norm'`:
```python
_fifo_sleeve = df[...].copy()
_fifo_sleeve['_acct_norm'] = _fifo_sleeve['account_id'].astype(str).str.strip()
fifo_mv_by_acct = _fifo_sleeve.groupby('_acct_norm')['market_value'].sum().to_dict()
```

---

## Phase 2 Root Cause: Fix B non_cash_target_mv = 0 (2026-05-01+)

### Fix C resolves the exception — but Fix B makes the shadow empty

Fix B (7c9f1b13c) changed `non_cash_target_mv` to:
```python
fifo_covered_mv = fifo_mv_by_acct.get(acct_id, 0.0)
non_cash_target_mv = max(account_mv - cash_mv - fifo_covered_mv, 0.0)
```

**Empirical result for 2026-04-22 data:**

| Metric | Value |
|--------|-------|
| Sleeve accounts with any FIFO lots | 598 of 598 |
| Accounts where `non_cash_target_mv = 0` | 551 of 594 |
| Accounts where `fifo_covered_mv > account_mv` (overcoverage) | 198 |
| Accounts with `non_cash_target_mv > $1` | 2 (z0822280961: $2.70; z0820198251: $67.30) |

The 598-account sleeve cohort has full FIFO lot coverage (from BD transaction history, which
includes `linear_interpolation` lots plus the new `silver_unrealized_reopen`/`canonical_holdings_reopen`
lots added by HLOT2b). Total FIFO MV per account ≈ `account_mv - cash_mv` for 98% of accounts.

Subtracting total FIFO MV from `account_mv - cash_mv` leaves essentially $0 for all accounts.
`_build_uln_sleeve_lots` → `rows_out = []` → returns `pd.DataFrame()` → shadow not stored → not written.

### ULN veto coverage at 2026-04-22

| Metric | Value |
|--------|-------|
| ULN non-cash (acct, asset) pairs for sleeve | 6,662 |
| Vetoed by FIFO open set | 6,496 (97.5%) |
| Not vetoed (pass) | 166 |
| Accounts with at least 1 passing row | 78 |
| Passing lots with prices | 163 |
| Passing lots missing price | 3 (`None`, `NORTH CAROLINA ST LTD OBLIG 5% 05/01/2030`) |

### Why the denominator fix (Fix B part 2) is correct

Fix B correctly changed `total_unit_cost` from all non-cash positions to non-vetoed only:
```python
# CORRECT (Fix B kept): denominator uses only non-vetoed positions
total_unit_cost = float(grp_nc_pass['unit_cost'].sum())
```

The SL-P1b ITERATE finding was that the denominator included vetoed positions, giving
non-vetoed positions a fractionally small weight. This part of Fix B is correct.

### What is wrong: the non_cash_target_mv formula

The intent was to subtract FIFO-covered MV from the apportionment target. But `fifo_covered_mv`
= total FIFO MV for the entire account (BD transactions + reopen lots), which equals the full
non-cash MV for sleeve accounts. Nothing remains for the shadow.

**Proposed correction:**
```python
# Revert to pre-Fix-B target formula (just remove cash):
non_cash_target_mv = max(account_mv - cash_mv, 0.0)
# Keep Fix B's denominator correction (non-vetoed only):
total_unit_cost = float(grp_nc_pass['unit_cost'].sum())
```

This apportions the full non-cash MV among non-vetoed ULN positions, weighted by unit_cost.
Non-vetoed positions get their fair share (eliminating the SL-P1b fractional-weight bug),
while vetoed positions (already covered by FIFO) contribute nothing to the denominator.

**Expected output with corrected formula (2026-04-22 data):**
- ~78 accounts, ~163 lots
- MV = proportional share of each account's non-cash MV for uncovered positions
- Down from 458 accounts in 2026-04-21 shadow (HLOT2b now covers most positions via reopen)

---

## FIFO / Reopen Coverage Analysis

The HLOT2b reopen lots (74dbad2ba) now correctly add ULN-derived positions to the FIFO stack.
This REDUCES the shadow's scope (fewer uncovered positions), which is CORRECT — the reopen path
is the authoritative mechanism for those positions.

| Price quality in sleeve (2026-04-22) | Count |
|--------------------------------------|-------|
| linear_interpolation | 31,304 |
| silver_unrealized_topup | 1,097 |
| silver_unrealized_reopen | 609 |
| rps_injection | 532 |
| synthetic_injection | 147 |
| canonical_holdings_reopen | 99 |
| non_unitized | 42 |

The shadow's remaining useful scope is the 166 ULN non-cash positions (78 accounts) NOT covered
by any FIFO open lot. These are the true "uncovered" positions the shadow was designed for.

---

## Acceptance Criteria Status

| AC | Status | Notes |
|----|--------|-------|
| AC#1: Pre-commit gate clean | DONE (Fix B+C shipped 2026-05-01) | |
| AC#2: Jones z0817905851 shadow MV = cash-only | BLOCKED — shadow empty (Fix B) | Need Fix B correction |
| AC#3: 3 pure-sleeve accounts within 2% of allocations | BLOCKED — shadow empty | Need Fix B correction |
| AC#4: Cohort stability (+-5 accounts across 3 dates) | BLOCKED — shadow empty | Need Fix B correction |
| AC#5: Open MV per nightly assertion | BLOCKED — shadow empty | Need Fix B correction |
| AC#6: 3 consecutive clean nightly emissions | BLOCKED — shadow empty | Need Fix B correction |
| AC#7: No regression to canonical holdings_lots | N/A (shadow separate artifact) | |
| AC#8: RAVC4 to COO | PENDING | This investigation is the prerequisite |
| AC#9: Session log | IN PROGRESS | This document |

---

## Proposed Fix (Fix B Correction)

**File:** `data/black_diamond/scripts/gold/B_01.holdings_lots.py`

**Change:** In `_build_uln_sleeve_lots`, at the `non_cash_target_mv` line (~line 977):

```python
# BEFORE (Fix B — over-corrects to zero):
fifo_covered_mv = fifo_mv_by_acct.get(acct_id, 0.0)
non_cash_target_mv = max(account_mv - cash_mv - fifo_covered_mv, 0.0)

# AFTER (Fix B correction — revert target formula, keep denominator fix):
non_cash_target_mv = max(account_mv - cash_mv, 0.0)
```

The `fifo_mv_by_acct` block (lines 952-961) can remain — it was introduced for Fix B but
is not harmful to retain. The computation can be removed in a follow-up cleanup.

**Risk:** LOW. Additive change (reverts one formula). Denominator fix (Fix B part 2) stays.
Shadow artifact is separate from canonical holdings_lots — no PROD impact until SL-P2.

**Gate:** `.tools/ds-commit-gate.sh` + CTO ratify (Fix B was COO/CTO-approved, correction
should route through same channel).

---

## Pending

- COO RAVC5 to review these findings
- CTO ratify needed for Fix B correction before ship
- After correction shipped to S3: 3 nightly shadow emissions required for AC#6
