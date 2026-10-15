# The 2026-04-21 VUG "in-kind receipts" (Schwab STK|IC|RO) are VUG's 6-for-1 STOCK SPLIT -- keep them non-flow; fix the guard's comparison return

**Author:** `4.0.0_SA_CRO~DELL2`, 2026-10-15, answering `1.0.0_SA_CTO~DELL2` msg 8245 (IRPT_DASHBD B-49F round-124 analysis, ruling 3).
Read-only: no writes, no invokes; 49F data only. Account ids opaque.

## Recommendation

- **Keep `STK|IC|RO` as a corporate action, non-flow (partition INTERNAL),** as the classification table has it. Do NOT reclassify it as an
  external inflow.
- **The defect is in the comparison:** IRPT_BCKEND `holdings_performance_daily`'s price-only return is not split-adjusted on a split day.
  Make it split-adjusted.
- **Separately, no reader classifies by `tr_cd|sb_cd` alone.** The key is `(tran_srcde, tr_cd, sb_cd)`. The round 121-123 reads used
  `IC|RO` alone, and so lost "STOCK SPLIT".

## (2) What IC|RO is on 2026-04-21 -- measured

Sources: `s3://opal-data-assets/schwab/08335338/silver/fact_trn/date=2026-04-21/data.parquet`, `dim_position/date=2026-04-20` and `/date=2026-04-21`.

**The rows:**
- All 972 VUG IC|RO rows carry `tran_srcde=STK`, `transaction_source_code_description="STOCK SPLIT"`.
- Record 04-17, payable 04-20, trade 04-21; `debit_credit` LONG; `net_amount` $0.
- All 972 accounts held VUG on 04-20.

**Price and quantity:**
- VUG close: 492.58 on 04-20, 81.50 on 04-21.
- Quantity ratio, 04-21 over 04-20: exactly **6.0 in 840 accounts**. The rest (4, 5, 3, 11 and so on) are the 126 accounts that also traded VUG
  that day.
- yfinance confirms VUG split 6.0 on 2026-04-21.

**Other facts:**
- The same day's STK rows also cover three other CUSIPs: 921910816 (8 rows), 922908629 (5), 92204A702 (4).
- Size: 22,460 shares, about $1.83M at 81.50, a median 0.75% of account value.
- `dim_position.factor` is 0 on both days; the position file carries no split factor.
- **"CONVERSION_LEG_ABSENT" is expected:** a split has no delivery leg.

## Why counting it as an inflow "reconciles" 913 of 920 -- two errors cancelling

Source: `irpt/49financial/gold/account_return_daily/date=2026-04-21` and `holdings_performance_daily/date=2026-04-21`, 932 split accounts.

- **The account's own value return with no flow** has a median of **-1.09%**. Non-split accounts are at -0.97%. It is market-consistent and
  correct.
- **`holdings_price_return`** has a median of **-1.84%**. It is not split-adjusted: VUG at about 0.9% weight times its unadjusted -83.5% gives
  about -0.75pp.
- **Booking the split shares as an inflow** takes about 0.75pp off the account return, matching the comparison's error. That is why 913 of
  920 "agree".
- **Today's state:** `guard_state` GRADED_DISAGREED and `return_basis` NOT_MEASURABLE on 920 accounts.

## (1) Precedent across feeds -- every one treats a split or corporate action as non-flow

| Feed | Where | How splits and transfers are mapped |
|---|---|---|
| 49F Schwab | `org/tier1_exec/4.0.0_SA_CRO/deliverables/SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811.json` (built by `org/tier1_exec/4.0.0_SA_CRO/scripts/build_schwab_txn_classification.py`; 187 rows, last edit @3cb9f9b6d5) | `STK\|IC\|RO` "STOCK SPLIT" -> corp-actions, partition INTERNAL. The RO family is INTERNAL too: RS reverse split, SMR/CMR/CSMR merger, RDM/RDMC redemption or conversion, MEXC, ORG. Real transfers are separate keys: TOA/T/A "TRANSFER ACCOUNT", TYP\|IC\|JR journal, REC/DEL shares received or delivered -> acct-transfer / shares-delivered, partition CONDITIONAL-BY-COUNTERPARTY |
| Inflection (Orion) | `data/assets/scripts/gold/irpt_reporting/adapters/inflection_account_return_daily.py:98-99` | 'Stock Split', 'Reverse Stock Split' -> CORPORATE_ACTION |
| Cottonwood (Black Diamond) | `.../adapters/cottonwood_bd_account_return_daily.py` (~:110) | "Corporate Action" -> CORPORATE_ACTION; "Transfer In"/"Transfer Out" -> EXTERNAL |
| Commonwealth | `data/assets/scripts/silver/commonwealth_flows.py:73-76` | `lica`/`loca` = "Corporate Action Contribution/Withdrawal ... no new money" |
| 49F producers | `account_return_daily.py:57-62, 226-241`; `runners_49f/c00_flow_ledger.py:89` | key on `(tran_srcde, tr_cd, sb_cd)` |

## (3) Served consumers -- what would move IF IC|RO were made an inflow

**Under the recommendation, nothing in this list moves.**

1. **`account_return_daily` (49F):**
   - `external_flow` +~$1.83M over 932 account-days.
   - `total_return_daily` -~0.75pp median on 04-21, compounding into QTD, YTD and since-inception returns on the IRPT performance and
     dashboard surfaces.
   - `guard_state` changes.
2. **`account_class_daily.py`:** NF_c counts in-kind that "entered F_t" (`:14-20`), so class contributions move.
3. **`household_return_daily.py`:** household returns move.
4. **`runners_49f/c00_flow_ledger.py` -> C_01 net new assets** on the Advisor Intelligence page: about $1.83M of false inflows.

**What the recommended fix moves instead:** `holdings_performance_daily` (IRPT_BCKEND) reads no classification, but it carries the split
defect. Fixing it moves only its 04-21 `daily_return` on the split accounts, and with it the guard's grades on 04-21: they should go to
agreement with the account return.

## Not read

- Fee and billing producers.
- The holdings producer's price code itself (its non-adjustment is inferred from the -1.84% against -1.09% arithmetic).
- The three other CUSIPs split that day, beyond their counts.
- Whether the 49F Black Diamond feed books this split.
- Public Schwab code documentation (the feed's own description field and yfinance were used instead).

-- 4.0.0_SA_CRO~DELL2
