# Session Log: TAXX_TXSTRT - v4 Guardrail Allocator

**Agent:** 0.3.0_DS_TradingOperations
**Date:** 2026-04-07
**Project:** TAXX_TXSTRT (Tax SMA Trade Allocation Strategy)

## Activation

Took over the TAXX continuation thread for the new trade set at `C:\Users\AndrewBerman\Desktop\Trade 20260407`.

## Work Performed

### 1. Reconstructed the interrupted TAXX handoff

Read the prior thread state and verified the new optimizer workbook schema directly. Confirmed:

- Source workbook for v4 should be `Asset-Level Analysis - Delta`
- `AB` = `Short Total`
- `AD` = `Short Rate`
- Bloomberg ticker formatting requirement applies on output (`.` -> `/`)

Also verified that the 2026-04-07 optimizer books do not currently contain any raw HTB failures under the new rules:

- `Short Total >= abs(Final Shares)` for all sampled and all scanned short rows
- `Short Rate == 0.00%` for all scanned short rows

### 2. Implemented the TAXX guardrail post-processor

Created a new guardrail allocator, finalized at `models/tax_strategy/post_processor.py`, with the requested rule order:

1. Banned securities are zeroed if they appear long or short
2. HTB-invalid shorts are zeroed if `Short Total < abs(short shares)` or `Short Rate > 0`
3. If step 1 or 2 removals create gross imbalance, the heavier side is delevered within the sectors where the errors occurred
4. Any position above `abs(1.0%)` with trigger tolerance `> 1.1%` is trimmed in place
5. Any sector net outside `abs(0.75%)` is repaired via sector-specific deleveraging

Additional implementation details:

- Parses directly from `Asset-Level Analysis - Delta`
- Uses share-based whole-share trims only
- Writes Schwab output with Bloomberg ticker formatting
- Preserves run isolation under `models/tax_strategy/output/v4_<timestamp>/`
- Updates `models/tax_strategy/output/runs.json`
- Includes explicit final upload parity validation against `Asset-Level Analysis - Delta` column `E` (`Delta Shares`)
- Emits merged Schwab output ordered acct-1, acct-2, acct-3

### 3. Fixed a cash-bucket parsing bug

Initial v4 run incorrectly treated `CASH_USD` as a tradeable equity position. The workbook encodes that row in cash units, which breaks share-based guardrail math and falsely triggered `[Unassigned]` sector repair.

Patched v4 to exclude `CASH_USD` from the parsed security universe, then reran.

### 4. Executed v4 against the new 2026-04-07 books

Command used:

`python models/tax_strategy/post_processor.py "C:\Users\AndrewBerman\Desktop\Trade 20260407" "models\tax_strategy\Tax SMA Accounts (1).xlsx"`

Final validated run:

- `models/tax_strategy/output/v4_20260407_115121/`

Observed results:

- Chiles: 203 longs / 185 shorts, gap `-0.0392%`
- Nixon: 203 longs / 186 shorts, gap `-0.0152%`
- Bump: 144 longs / 139 shorts, gap `-0.0013%`
- No banned-security hits
- No HTB hits
- No balance repair required
- No single-name max-weight trims
- No sector-net repairs
- Upload parity passed for all three accounts versus Yang's `Delta Shares`

## Files Modified

| File | Change |
|------|--------|
| models/tax_strategy/post_processor.py | NEW - TAXX guardrail post-processor using Asset-Level Analysis - Delta |
| models/tax_strategy/output/runs.json | UPDATED - appended v4 run entry |
| models/tax_strategy/output/v4_20260407_115121/ | NEW - latest validated v4 output set |
| org/tier2_senior/0.3.0_DS_TradingOperations/logs/2026-04-07/taxx_txstrt_v4_guardrail_run.md | UPDATED - final state and validation notes |

## Current State

- v4 post-processor is implemented and runnable via `models/tax_strategy/post_processor.py`
- Latest validated run is `models/tax_strategy/output/v4_20260407_115121/`
- Current 2026-04-07 optimizer output already satisfies all v4 guardrail checks after excluding the non-tradeable `CASH_USD` bookkeeping row

## Next Steps

- [Andrew] Review `models/tax_strategy/output/v4_20260407_115121/schwab/schwab_upload_ALL.csv`
- [Andrew] Confirm that excluding `CASH_USD` from guardrail scope is the intended production behavior
- [0.3.0_DS_TradingOperations] If needed, add a stricter natural-language risk section for "pass-with-no-findings" runs or fold v4 back into the main TAXX allocator line
