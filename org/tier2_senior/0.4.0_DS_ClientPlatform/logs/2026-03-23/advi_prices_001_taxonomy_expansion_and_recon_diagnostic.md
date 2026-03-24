# ADVI_PRICES-001: Transaction Taxonomy Expansion + Recon Diagnostic -- 0.4.0_DS_ClientPlatform

**Date:** 2026-03-23
**Branch:** CLOUD

## Objective

Close the ADVI_PRICES investigation with two deliverables:
1. WS1: Expand SELL_TYPES/CA_SELL_SUBTYPES in `03_build_holdings_lots.py` to close phantom lots caused by unrecognized exit transaction types (+$91M across 269 accounts).
2. WS2: Build a same-date reconciliation diagnostic (`recon_lots_vs_allocations.py`) with RC classification and phantom account drill-down.

---

## Work Completed

### 1. WS1 -- Transaction Taxonomy Enumeration and Allowlist Expansion

**Context from ADVI_PRICES-001 thread:** Same-date recon shows +$25.6M net gap (+1.6%), with 269 phantom accounts (+$91M) and 156 missing-lots accounts (-$28M). COO confirmed ZERO accounts are `account_is_open==False` with open lots, so the allocation liveness hard stop (Fix Track B) will NOT help. The phantom problem is purely about unrecognized exit transaction types.

**Analysis of existing allowlists:**

| Set | Before | After | Added |
|-----|--------|-------|-------|
| SELL_TYPES | 5 types | 6 types | `Redemption` |
| CA_SELL_SUBTYPES | 4 subtypes | 9 subtypes | `Exchange`, `Tender`, `Maturity`, `Called`, `Liquidation` |

**Rationale per addition:**

| Type/Subtype | Category | Rationale |
|---|---|---|
| `Redemption` | SELL_TYPES | BD encodes mutual fund/ETF share class exits as Redemption, not Sale. Without this, redeemed positions stay open indefinitely in FIFO. Most likely driver of phantom lots in advisory accounts heavy in fund share classes. |
| `Exchange` | CA_SELL_SUBTYPES | Corporate exchange/restructuring -- old shares exit. M&A events where one ticker is replaced by another. |
| `Tender` | CA_SELL_SUBTYPES | Tender offer accepted -- shares tendered out. Less common but can leave large lots open when missed. |
| `Maturity` | CA_SELL_SUBTYPES | Bond/CD matured -- units go to zero. Required for fixed income accounts. |
| `Called` | CA_SELL_SUBTYPES | Bond called by issuer -- units go to zero. Required for callable bond positions. |
| `Liquidation` | CA_SELL_SUBTYPES | Fund/trust liquidation -- units go to zero. Covers closed-end fund / trust terminations. |

**Types explicitly NOT added:**

| Type | Reason |
|---|---|
| `Journal` | Bidirectional (can add or remove units). Adding to SELL_TYPES would incorrectly classify all Journal rows as sells. Needs special handling (unit-sign-based classification) if data shows it drives phantom lots. |
| `Return of Capital` | Primarily reduces cost basis, not units. Can reduce units to zero in rare liquidating distributions, but adding it risks mis-classifying standard ROC events as sells. |
| `Fee` / `Withdrawal` | These are cash-flow events, not position-level unit changes. |

**Supporting script:** `data/black_diamond/scripts/diagnostics/diag_txn_taxonomy_enumeration.py` -- AE should run this against silver/transactions to validate which of these types actually exist in the data and identify any additional exit-like types.

Also fixed emoji in `save_lots()` print statement (CLAUDE.md rule 13: no emojis in code).

### 2. WS2 -- Reconciliation Diagnostic Script

Built `data/black_diamond/scripts/diagnostics/recon_lots_vs_allocations.py`:

- **Inputs:** `--date YYYY-MM-DD` (required), optional `--phantom-list` and `--output-dir`
- **Reads:** `silver/allocations/{date}.parquet` + `gold/holdings_lots/{date}.parquet`
- **Produces:**
  1. Summary: BD AUA total, lot MV total, net gap, % gap
  2. Per-account join with classification
  3. Waterfall: $ impact per RC1-RC5 category
  4. Top 20 phantom account drill-down with per-security detail
- **Drill-down:** For each phantom account, identifies top securities by lot MV, checks 90-day transaction window, flags securities with ZERO recent transactions as `** STALE`

RC classification logic:
- RC1_PHANTOM: lot_mv > 2x bd_aua
- RC2_ALLOC_ONLY: bd_aua > $1K and lot_mv == 0
- RC3_INSURANCE: account_type == Insurance and diff < -$100
- RC4_NON_INVESTMENT: account_type in Bank/Savings/CreditCard/Loans/Mortgage/TermLife
- RC5_NORMAL: everything else

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Added `Redemption` to SELL_TYPES (not CA_SELL_SUBTYPES) | BD encodes fund-level exits as a top-level transaction_type, not as a Corporate Action subtype |
| Did NOT add `Journal` | Bidirectional type -- would cause false sell classifications. Needs unit-sign-based handling if data confirms it drives phantoms. |
| Did NOT modify 02_build_positions_cube.py | Task order constraint. AE should sync allowlists after gold rerun validates. |
| Wrote enumeration script as standalone diagnostic | Reusable by AE to validate the expansion and identify any remaining gaps. |
| Recon script uses full outer join | Captures both phantom lots (lots but no alloc) AND alloc-only accounts (alloc but no lots). |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `data/black_diamond/scripts/gold/03_build_holdings_lots.py` | Expanded SELL_TYPES (+1) and CA_SELL_SUBTYPES (+5), fixed emoji | Yes -- `f1b3f33d` |
| `docs/data/transaction_type_canonical_reference.md` | Added 6 new types to reference doc | Yes -- `f1b3f33d` |
| `data/black_diamond/scripts/diagnostics/recon_lots_vs_allocations.py` | Created recon diagnostic | Yes -- `9b039259` |
| `data/black_diamond/scripts/diagnostics/diag_txn_taxonomy_enumeration.py` | Created taxonomy enumeration | Yes -- `9b039259` |

---

## Briefs Written

None required for this task. The diagnostic scripts are self-documenting and the allowlist expansion is in-code. AE task order (ADVI_PRICES.001.ae) specifies the gold rerun procedure.

---

## Current State

> **Primary handoff point.**

**Status:** COMPLETE
**Active branch:** CLOUD

Two commits on CLOUD: `f1b3f33d` (WS1: taxonomy expansion in 03_build_holdings_lots.py + canonical reference) and `9b039259` (WS2: recon_lots_vs_allocations.py + taxonomy enumeration script). SELL_TYPES now includes `Redemption`; CA_SELL_SUBTYPES now includes `Exchange`, `Tender`, `Maturity`, `Called`, `Liquidation`. The recon script is ready to run against `--date 2026-03-19` once AE reruns the gold layer with the expanded allowlists. Task order `ADVI_PRICES.001.ds-txn-taxonomy-and-recon-diagnostic.md` marked complete.

**IMPORTANT:** 02_build_positions_cube.py still has the OLD allowlists. It was not modified per task order constraint. AE must sync these allowlists in 02 before the gold rerun, or the positions cube will diverge from holdings_lots.

---

## Next Steps

1. **[0.6.0_AE_PartnerETL] Run taxonomy enumeration** -- `python diag_txn_taxonomy_enumeration.py --days 30` to validate which added types actually exist in silver/transactions and identify any additional gaps.
2. **[0.6.0_AE_PartnerETL] Sync allowlists in 02_build_positions_cube.py** -- the same SELL_TYPES/CA_SELL_SUBTYPES expansion must be applied to script 02 before gold rerun (not in scope of this task order but required for consistency).
3. **[0.6.0_AE_PartnerETL] Upload updated gold scripts to S3 and run gold layer** -- per AE task order ADVI_PRICES.001.ae.
4. **[0.6.0_AE_PartnerETL] Run recon after gold rerun** -- `python recon_lots_vs_allocations.py --date 2026-03-19 --phantom-list diagnostics/prices_recon_accounts_2026-03-19.json --output-dir /tmp/recon/` to verify phantom lot reduction.
5. **[0.4.0_DT_ClientPlatform] Push + verify** -- per DT task order ADVI_PRICES.001.dt.

**Files to touch next:**
- `data/black_diamond/scripts/gold/02_build_positions_cube.py` -- AE must sync SELL_TYPES/CA_SELL_SUBTYPES (same 6 additions)

**Do NOT:**
- Run gold layer rerun (AE scope)
- Push to remote (DT scope)
- Modify 02_build_positions_cube.py (task order constraint, AE scope)
