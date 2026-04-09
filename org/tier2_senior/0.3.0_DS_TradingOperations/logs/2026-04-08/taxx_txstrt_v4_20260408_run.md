# Session Log: TAXX_TXSTRT - v4 Daily Run (2026-04-08)

**Agent:** 0.3.0_DS_TradingOperations
**Date:** 2026-04-08
**Project:** TAXX_TXSTRT (Tax SMA Trade Allocation Strategy)

## Activation

New day of trade files received for post-processor run:
- `C:\Users\AndrewBerman\Downloads\OneDrive_1_4-8-2026\Acct-{1,2,3}.xlsx`
- Updated manifest: `C:\Users\AndrewBerman\Downloads\Tax SMA Accounts (1).xlsx`

## Work Performed

### 1. Initial v4 run with old manifest

Ran post-processor against the three new trade files using the prior manifest.
Run ID: `v4_20260408_093607`

Result: clean pass, zero guardrail interventions across all three accounts. Upload parity passed.

### 2. Schwab upload filename fix

Updated `post_processor.py` to include the run timestamp in the merged upload filename:
`schwab_upload_ALL.csv` -> `schwab_upload_ALL_{timestamp}.csv`

### 3. Manifest update

Replaced `models/tax_strategy/Tax SMA Accounts (1).xlsx` with updated version from Andrew.

Changes in the new manifest:

| Account | Field | Old | New |
|---------|-------|-----|-----|
| Chiles (1) | AUM (Mn) | 1.00 | 1.06 |
| Chiles (1) | Divest | HD, NFLX | HD, NFLX, BRK/B, GOOG, CAN, META, MMM, GOOGL |
| Nixon (2) | AUM (Mn) | 0.75 | 0.77 |
| Nixon (2) | Divest | *(none)* | AAPL |
| Bump (3) | Account Number | 3495-0058 | 3594-0058 |
| Bump (3) | AUM (Mn) | 1.95 | 1.98 |
| Bump (3) | Divest | *(none)* | VIGAX, VMGM, VSGAX |

### 4. Re-run with updated manifest

Run ID: `v4_20260408_095059`

Results -- zero guardrail interventions:

| Account | Longs | Shorts | Long % | Short % | L/S Gap | Banned | HTB | Mutations |
|---------|-------|--------|--------|---------|---------|--------|-----|-----------|
| Chiles ($1.06M) | 203 | 188 | 99.87% | 100.04% | -0.17% | 0 | 0 | 0 |
| Nixon ($0.77M) | 203 | 188 | 99.92% | 99.94% | -0.02% | 0 | 0 | 0 |
| Bump ($1.98M) | 156 | 148 | 45.03% | 45.03% | -0.00% | 0 | 0 | 0 |

New divest tickers (BRK/B, GOOG, CAN, META, MMM, GOOGL, AAPL, VIGAX, VMGM, VSGAX) did not trigger because none appear in Yang's optimizer output for today.

Upload parity passed on all three accounts. Only B (buy) and SS (sell short) transaction types present -- no short covers or sells.

### 5. Comparison vs. prior day (2026-04-07)

| Account | 04-07 Longs/Shorts | 04-08 Longs/Shorts | Delta |
|---------|--------------------|--------------------|-------|
| Chiles | 203 / 185 | 203 / 188 | +3 shorts |
| Nixon | 203 / 186 | 203 / 188 | +2 shorts |
| Bump | 144 / 139 | 156 / 148 | +12 longs, +9 shorts |

Yang added more positions across the board, particularly for Bump.

## Files Modified

| File | Change |
|------|--------|
| models/tax_strategy/post_processor.py | Timestamped schwab_upload_ALL filename |
| models/tax_strategy/Tax SMA Accounts (1).xlsx | Replaced with updated manifest (new acct numbers, AUM, divest lists) |
| models/tax_strategy/output/v4_20260408_093607/ | Initial run output (old manifest) |
| models/tax_strategy/output/v4_20260408_095059/ | Final run output (updated manifest) |
| models/tax_strategy/output/runs.json | Appended both run entries |

## Current State

- Final validated run: `models/tax_strategy/output/v4_20260408_095059/`
- Schwab upload: `models/tax_strategy/output/v4_20260408_095059/schwab/schwab_upload_ALL_20260408_095059.csv`
- All guardrails passed with no interventions
- Manifest updated with new account numbers, AUM, and divest lists

## Next Steps

- [Andrew] Review `schwab_upload_ALL_20260408_095059.csv` for upload
- [Andrew] Confirm new divest lists are complete (particularly the 6 new Chiles tickers)
