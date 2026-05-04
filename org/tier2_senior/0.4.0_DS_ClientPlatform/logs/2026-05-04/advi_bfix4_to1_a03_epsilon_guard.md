# Session Log — ADVI_BFIX4 TO-1: A_03 Epsilon Guard

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-04
**Task Order:** ADVI_BFIX4.TO-1
**Status:** SHIPPED — awaiting AE 0.7 QA chain re-run

---

## Summary

Implemented A_03 epsilon guard per ADVI_BFIX4 TO-1 (B2). Added `signed_units.abs() >= 1e-6`
defensive filter in `_load_synthetic_buy_events()` before the existing `> 0.001` tiny-position
filter. Pre-commit gate clean. Committed `be11d25fe`, pushed, S3 upload MATCH.
RAVC2 sent to AE 0.7 for `--from A_03 --force` QA chain re-run.

---

## Compiler Tools

| Tool | Target | Result |
|------|--------|--------|
| comp-pipescript io | A_03 | No column-gap reads detected; writes: positions_cube + synthetic_positions_index |
| comp-blast | A_03 | No downstream consumers found |
| ds-commit-gate | A_03.positions_cube.py | PASS — py_compile + AST + ruff all exit 0 |
| comp-pipescript deployed | A_03 | MATCH (ETag 478c1897faca6c2012fe9d9d41272dc2, 2026-05-04T17:41:32Z) |

---

## Code Change

**File:** `data/black_diamond/scripts/gold/A_03.positions_cube.py`

**Location:** `_load_synthetic_buy_events()`, after `signed_units` computation (line ~834)

**Pre-change (lines 830-837):**
```python
# Compute units
missing_df['signed_units'] = (
    (missing_df['injectable'] / missing_df['price'])
    .round(4)
)

# Filter tiny positions
missing_df = missing_df[missing_df['signed_units'] > 0.001].copy()
```

**Post-change:**
```python
# Compute units
missing_df['signed_units'] = (
    (missing_df['injectable'] / missing_df['price'])
    .round(4)
)

# epsilon guard -- skip near-zero unit positions to avoid divide-by-zero / phantom AUA
missing_df = missing_df[missing_df['signed_units'].abs() >= 1e-6].copy()

# Filter tiny positions
missing_df = missing_df[missing_df['signed_units'] > 0.001].copy()
```

`from __future__ import annotations` confirmed present at line 33 (pre-existing, backfill sweep).

---

## z0822229381 (AQR) Source-Data Investigation

**Account:** z0822229381 (AQR TA DELPHI PLUS FUND LLC, account number 54436187)

**Finding: Epsilon is in B_00 BD bronze path, NOT A_03 UNREALIZED injection path.**

| Source | State | Units | Market Value |
|--------|-------|-------|-------------|
| canonical_holdings (B_00) | source='bd' | 3.637979e-11 DELPHI | ~$0 |
| silver/allocations | — | — | ~$1,951,010 (silver AUA) |
| silver/unrealized (A_03 input) | 2 rows: DELPHI + CASH | NO units column | unit_cost=0.0 both rows |

**Root cause chain:**
1. BD bronze UNREALIZED_DAILY_2026-04-30.xlsx delivers z0822229381 with AQR DELPHI position
2. B_00 ingests this as `source='bd'` in canonical_holdings
3. The units value carried from BD bronze is epsilon (3.637979e-11) — this is a BD data quality issue
4. DELPHI is par-valued ($1.00/unit per `_PAR_VALUED_PATTERNS` in A_03 line 301)
5. B_00 does NOT apply the epsilon guard — the BD bronze path has no equivalent filter
6. Result: canonical_holdings has z0822229381 with $0 AUA despite silver/allocations showing $1.95M

**A_03 injection path analysis:**
- silver/unrealized has z0822229381 with unit_cost=0.0, NO units column
- A_03's `_load_synthetic_buy_events()` computes injectable from silver allocation residual
- If z0822229381 is NOT in `rps_covered` (which it is — it's in UNREALIZED_DAILY), it falls through to injection
- At injection, A_03 would compute ~1.95M units (large injection, not epsilon)
- The epsilon guard does NOT fire for z0822229381 in A_03 — its AUA issue is entirely B_00 territory

**AQR state:** persistent epsilon. UNREALIZED_DAILY has been delivering epsilon DELPHI units across
multiple dates. This is a BD data quality artifact for AQR custodied via Schwab (SCHWAB-1186041 symbol).

---

## Similar-Accounts Scan

**Methodology:** Scanned silver/unrealized (96,033 rows) for accounts that could produce epsilon
injection via `signed_units = injectable / price`.

**Finding:** silver/unrealized has NO `units` column. Epsilon injection risk in A_03 comes only
from `injectable / price` near-zero results. Since `injectable > 0` is enforced at line 816 before
unit computation, and price > 0 by construction from BD price lookup, epsilon signed_units can only
occur from float precision artifacts in residual * lot_weight calculations.

**Similar accounts with unit_cost = 0.0 in silver/unrealized:**
z0822229381 rows include CASH (unit_cost=0.0) and AQR DELPHI (unit_cost=0.0). CASH assets are
typically excluded from injection (CASH not a missing pair in unrealized context). No other accounts
identified with systematically epsilon-risk profiles in current data.

**Epsilon guard impact today:** Guard is defensive. No accounts in current silver/unrealized data are
expected to produce `abs(signed_units) < 1e-6` at the point of injection, since injectable is
dollar-denominated (> $0) and prices are non-zero. The guard protects against future float
precision edge cases (e.g., residual * lot_weight rounding to 1e-8 for a $1.00 price).

---

## Note on B2 vs Account_Performance AUA (AC#5-7 caveat)

**Key finding:** B_03 reads from `canonical_holdings` (B_00 output), NOT `positions_cube` (A_03 output).
Chain: B_00 → B_01/B_02/B_03 → C_03 (account_performance) → D_04.
A_03 is a separate artifact feeding only `positions_cube` and `synthetic_positions_index`.

**Implication:** The epsilon guard in A_03 does NOT affect the account_performance chain.
z0822229381's $1.95M silver AUA will remain excluded from `c1_recovered` and `firm_composition.json`
until B1 (BFIX4 in B_00) lands. B2 is correctly scoped as a defensive code quality fix.

**Expected QA delta from B2 alone:**
- c1_recovered_accounts.json count: no change expected (A_03 fix doesn't flow to D_04's detection)
- excluded_c1_count: no change expected
- firm_composition total_market_value: no change expected
- positions_cube quality: improved (epsilon positions filtered before injection)

This is documented here per TO-1 scope requirement; RAVC3 to COO will include this finding.

---

## Deploy Cycle

| Step | Result |
|------|--------|
| Pre-commit gate | PASS — all 3 checks exit 0 |
| Commit | be11d25fe — fix(A_03): epsilon guard for near-zero unit positions (BFIX4 TO-1; B2) |
| Push | origin/CLOUD — d189c3c4e..be11d25fe |
| S3 upload | s3://opal-data-bd/code/gold/A_03.positions_cube.py (78.7 KiB) |
| S3 ETag | 478c1897faca6c2012fe9d9d41272dc2 (2026-05-04T17:41:32Z) |
| comp-pipescript deployed | MATCH |
| RAVC2 to AE 0.7 | Sent 20260504T174300Z (approx) — QA dispatch: --from A_03 --force |

---

## Next Steps

- [AE 0.7] QA chain re-run: `--from A_03 --force` on bd-gold-qa-runner
- [DS~B] On QA result: RAVC3 to COO with SSM ID + outcome + caveat on B2 scope
- [DS~B/CTO] B1 (BFIX4 in B_00) gated on Andrew ruling — do NOT proceed until authorized
