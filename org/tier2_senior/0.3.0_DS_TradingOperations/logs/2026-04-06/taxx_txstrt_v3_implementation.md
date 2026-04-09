# Session Log: TAXX_TXSTRT — v3 Trade Allocator Implementation

**Agent:** 0.3.0_DS_TradingOperations
**Date:** 2026-04-06
**Project:** TAXX_TXSTRT (Tax SMA Trade Allocation Strategy)

## Activation

Andrew directed v3 implementation based on updated requirements from Yang.

## Work Performed

### 1. Yang's Updated Trade Files (2026-04-06)

Received new optimizer output at `C:\Users\AndrewBerman\Downloads\Trade 20260406\` with 3 Axioma workbooks (Acct-1, Acct-2, Acct-3). Key findings:

- Yang's optimizer now handles HTB constraints upstream — SSAVAIL2 no longer needed as input
- NFLX already excluded from optimizer for Acct-1 (not in Trade List)
- AAPL already excluded from optimizer for Acct-2 (not in Trade List)
- VIGAX/VMGM/VSGAX not in Russell 1000 universe (Acct-3 mutual funds)
- HD still present as a short in Acct-1 (-0.225%) and Acct-2 (-0.257%)
- HD only banned for Acct-1 (Chiles); banned lists are per-account, not firm-wide

### 2. v3 Allocator — New Constraint Architecture

Created `models/tax_strategy/trade_allocator_v3.py`. Major changes from v2:

**Removed:**
- HTB validation step (Yang's optimizer handles borrow constraints)
- SSAVAIL2 as a required input (CLI now takes only trade_folder + manifest)

**Changed — Exclusion Logic (Step 1):**
- v2: banned longs reallocated same-sector, banned shorts reallocated same-sector
- v3: banned positions on BOTH sides removed WITHOUT replacement (deleverage preference)
- Yang's philosophy: deleverage rather than substitute

**New — Deleverage Check (Step 1b):**
- After removing banned positions, calculate long-short gap
- If gap > 2% in either direction, trim the heavier side by (gap - 2%)
- Trim distributed pro-rata across sectors of the removed banned positions
- Within each sector, trim lowest-conviction positions first:
  - Longs: lowest alpha first
  - Shorts: highest alpha (least negative) first
- Full shares only, no partials
- Symmetric: works for both banned shorts (trim longs) and banned longs (trim shorts)

**Changed — Weight Cap Tolerance (Step 2):**
- v2: triggered at >1.00%, caused ~50 mutations per account from optimizer rounding
- v3: tolerance band at 1.1% — only triggers if position exceeds 1.1%, caps back to 1.0%
- Yang's optimizer lands positions at 1.001-1.05%, so these pass through untouched now

**New — Merged Schwab CSV:**
- `schwab_upload_ALL.csv` in schwab/ dir — all accounts stacked (Acct-1, then 2, then 3)

### 3. v3 Results (2026-04-06 run)

| Account | Divest | Mutations | Longs | Shorts | L-S Gap | Deleverage? |
|---------|--------|-----------|-------|--------|---------|-------------|
| Acct-1 (Chiles) | HD, NFLX | 1 (HD removed) | 203 | 187 | +0.21% | No |
| Acct-2 (Nixon) | AAPL | 0 | 203 | 188 | -0.00% | No |
| Acct-3 (Bump) | VIGAX, VMGM, VSGAX | 0 | 121 | 100 | -0.00% | No |

All L-S gaps well within 2% threshold. Merged CSV: 1,002 trades.

## Files Modified

| File | Change |
|------|--------|
| models/tax_strategy/trade_allocator_v3.py | NEW — v3 allocator (exclusions + deleverage + weight cap with tolerance) |
| models/tax_strategy/output/v3_20260406_190118/ | NEW — v3 production run output |

## Current State

- v3: `trade_allocator_v3.py` — validated, production-ready
- Deleverage logic wired but did not trigger (HD weight too small to breach 2% gap)
- Weight cap tolerance eliminated ~50 mutations per account

## Next Steps

- [Andrew] Review v3 Schwab CSVs at `output/v3_20260406_190118/schwab/`
- [Andrew] Confirm v3 output is ready for Schwab upload
- [0.3.0_DS_TradingOperations] Awaiting direction on additional constraints or next trade date run
