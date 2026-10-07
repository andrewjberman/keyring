# ADVI_COTBKF decomposition -- ROUND 12 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-07 ~14:3xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s round-11 ADDENDUM 1 `CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_11_ADDENDUM_1_20261007.md` @e74f8eeb8e (msg 677):
"issue cell A now", C-DAILY step 1, with criterion (2) printing snapshot differences by account and security. Cells B-D (valuation,
return, monthly grade) stay gated on MDPF_SECHIST's first announced price load. Pre-draft:
`deliverables/2.0.0_SA_COO~C2/DRAFT_FWD3_DAILY_RETURNS_CUT_20261007.md`.

**Rule 24.** Domain: cell A only (B-D gated). One cell.

## Measured constraints (dell2, 14:3xZ)

1. Silver transactions: 1,416,497 rows (C-SILVER, every delivered record kept), 1,533 accounts, trade dates 2013-04-03 to 2026-06-22.
2. Silver positions: one snapshot, 2026-06-23, 469 rows, 83 accounts (columns AccountNumber, Cusip, Quantity, ...).
3. `data/assets/scripts/silver/commonwealth_crosswalk.py` already holds the signed-quantity rules (`SIGN`, `_signed`, `rebuild_holdings`,
   `position_holdings`, `rebuild_check`); its REBUILD-CHECK compares the rebuilt end holdings with the snapshot within 0.001.
4. Calendar: `lib/trading_calendar.py`, 2010-2027 (CB-e-1's guard refuses an uncovering calendar).

## The cell

| cell | what | serves | risk | slot |
|---|---|---|---|---|
| `CB-l-1` | daily holdings per account, per trading day, quantity by security, rebuilt from the transactions; end-state checked against the 2026-06-23 snapshot with every difference printed by account and security | FWD-3 (C-DAILY step 1) | LOCAL | `0.9.0_WK_ADVI_COTBKF~28` |

**Write set:** `data/assets/scripts/silver/commonwealth_daily_holdings.py` + its test; the deliverables folder; the channel.
**Fan-out:** `1 of 1 chains, cap 8`. No apply this round.
