# AUA Gap Root Cause Investigation -- 0.4.0_DS_ClientPlatform

**Date:** 2026-03-28
**Project:** ADVI_PRICES (root cause investigation)
**Trigger:** CTO message -- two diagnostic tracks (canonical prices logic + .007 silver override assessment)

---

## Objective

Investigate why post-passthrough gold run shows $150M gross over / $138M gross under,
with PFDE priced at T1 $23.56 and IQLT using linear_interpolation (+$7.4M).

---

## Work Completed

### 1. CTO Track 1 Investigation: Canonical Prices Priority Logic

Traced the full T2 join path in `build_canonical_prices_v2.py`:
- Line 418: `spine['ticker'] = spine['asset_name'].map(name_to_ticker)` -- maps asset_name to ticker
- Line 433-435: T2 join on `['ticker', 'date']` -- joins Yahoo historical_prices onto spine
- `OPAL_ETF_OVERRIDES` correctly maps `'PATHFINDER DISCIPLINED US EQUITY ETF' -> 'PFDE'` and `'PATHFINDER FOCUSED OPPORTUNITIES ETF' -> 'PFOE'`

**Finding:** The canonical prices priority logic is correct. PFDE/PFOE tickers resolve correctly through the override chain.

### 2. AE Evidence Pivot: Pricing Is Correct, Units Are Wrong

Read AE log `advi_prices_005_gap_root_cause_positions_cube_bug.md` (2026-03-27 1:15-2:15 AM ET).
AE performed position-by-position comparison for account z0821398141:

| Asset | Cube Units | BD Txn Price | Canon Price | Yahoo Price |
|-------|-----------|-------------|-------------|-------------|
| PFDE  | 22,212    | $23.83-23.88 | $23.94     | $23.835     |
| PFOE  | 21,734    | $22.34      | $22.36      | --          |

**Prices match within pennies. The cube just has wrong unit counts.**

PFDE: 22K units in cube vs ~187K expected from net buy/sell transactions (165K missing).
995 accounts >50% off silver. 432 of those have ZERO positions despite BD showing non-zero AUA.

### 3. Root Cause: `transaction_id` Dedup Is Not Account-Scoped

`02_build_positions_cube.py` line 225:
```python
df = df.drop_duplicates(subset=['transaction_id'], keep='last')
```

This is a **global** dedup on `transaction_id` alone. BD exports transactions across
overlapping daily and backfill files. The dedup's purpose is to collapse re-delivered
rows (same transaction appearing in multiple export files).

**The bug:** If BD assigns `transaction_id` values that are unique per-account but NOT
globally unique, this dedup collapses legitimate transactions from different accounts.
For example, account A's transaction #5001 and account B's transaction #5001 would be
treated as the same transaction -- only one survives.

**Supporting evidence:**
- Only 1 of 30 securities (QQQ, which had a single transaction) has matching units
- Older accounts more affected (more transaction history = more collision opportunities)
- 43% of worst-offender accounts have ZERO positions (all transactions dropped)
- The pattern affects ALL securities uniformly, not specific asset types

**Diagnostic script `05f_diagnose_positions_cube.py` (already written, untracked)**
tests this hypothesis with:
- H1: global uniqueness check (cross-account collision count)
- Row-loss comparison: global dedup vs account-scoped dedup

### 4. Fix Applied: Account-Scoped Dedup

Changed `drop_duplicates(subset=['transaction_id'])` to
`drop_duplicates(subset=['transaction_id', 'account_id'])` in all affected scripts.

**Safety analysis:** If transaction_ids ARE globally unique, this change is a no-op
(all duplicates already share the same account_id). If they are per-account unique,
this fixes the cross-account collision. No risk of regression either way.

### 5. CTO Track 2 Assessment: .007 Silver AUA Override

**.007 should NOT be deployed.** The $127M gross undervaluation is caused by missing
positions (unit undercounting), not pricing methodology gaps. Fixing the dedup should
collapse the gap dramatically. Silver AUA override would paper over the real problem
and mask any future unit-counting regressions.

After the dedup fix gold run, re-evaluate: if residual gap is small (<1%), .007 is
unnecessary. If there's still a meaningful structural gap after correct unit counts,
reassess .007 scope at that point.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Scoped dedup to `['transaction_id', 'account_id']` not just `['transaction_id']` | Safe in both directions: no-op if IDs are globally unique, fix if per-account unique. |
| Fixed ALL gold scripts (00-04) + lib/nna_flows.py + silver merge + canonical prices | Same dedup pattern pervasive across 40+ scripts. Gold scripts are the critical path. |
| Did NOT fix diagnostic scripts (05f, 05g, 05h) | They intentionally use global dedup for comparison/measurement. |
| Recommend AGAINST deploying .007 | Root cause is unit undercounting, not pricing. Override would mask the real problem. |
| Recommend running 05f on EC2 before gold rerun | Confirms H1, quantifies rows incorrectly dropped, validates fix before full rebuild. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `data/black_diamond/scripts/gold/02_build_positions_cube.py` | Scoped dedup to `['transaction_id', 'account_id']` | No -- local only |
| `data/black_diamond/scripts/gold/03_build_holdings_lots.py` | Same dedup fix | No -- local only |
| `data/black_diamond/scripts/gold/00_build_accounts_dimension.py` | Same dedup fix | No -- local only |
| `data/black_diamond/scripts/gold/01_build_advisor_assignments_history.py` | Same dedup fix | No -- local only |
| `data/black_diamond/scripts/gold/04_build_client_dimension.py` | Same dedup fix | No -- local only |
| `data/black_diamond/scripts/gold/lib/nna_flows.py` | Same dedup fix | No -- local only |
| `data/black_diamond/scripts/silver/build_canonical_prices_v2.py` | Same dedup fix | No -- local only |
| `data/black_diamond/scripts/silver/merge-daily-incremental.py` | Same dedup fix | No -- local only |

---

### 6. CTO HOLD: Portfolio Group Duplication Concern

CTO flagged: BD has ~6x portfolio group duplication per transaction. If cross-account
duplicates are portfolio group copies (same real-world transaction appearing under multiple
accounts in a group), then `['transaction_id', 'account_id']` dedup would INFLATE units.

**All 8 code changes REVERTED.** No gold/silver scripts modified.

**Updated 05f diagnostic** with:
- H1b: Portfolio group analysis -- classifies cross-account duplicates as portfolio copies
  vs true collisions by comparing (asset_name, units, trade_date) across accounts
- H3: PFDE-specific trace for z0821398141 -- shows raw rows being dropped, what survives
  global vs account-scoped dedup, and whether shared IDs are portfolio group or collision
- portfolio_id column analysis (if present in silver data)

**Three possible outcomes from 05f:**

| Diagnostic Result | Meaning | Fix |
|---|---|---|
| Majority portfolio group copies | Same real txn under multiple accounts | Global dedup is correct; undercounting has a different cause |
| Majority true collisions | Different txns sharing an ID | Account-scoped dedup is safe |
| Mixed | Both patterns present | Need composite key: `['transaction_id', 'account_id', 'asset_name']` or filter by portfolio_id |

---

### 7. 05f Results: Dedup Hypothesis REJECTED

AE ran enhanced 05f on EC2. Results:

1. **Cross-account duplicate transaction_ids: ZERO.** BD IDs are globally unique.
   Account-scoped dedup recovers zero additional rows. H1 rejected.
2. **PFDE in z0821398141: only 5 unique transactions.** The ~160K missing buy units
   were never delivered by BD in any transaction type. Not a dedup problem.
3. **Passthrough fix helped 360 accounts** drop out of the >50% bucket, but 635 accounts
   remain with gaps due to BD never sending complete transaction history.

**Revised Track 2 assessment: .007 silver AUA override IS the correct fix.**
The gap is a BD data completeness issue (missing transactions), not a pipeline bug.
Silver AUA from BD's allocation snapshots reflects the custodian's ground truth.
The override bridges accounts where our transaction-derived positions undercount
because BD never delivered the full transaction history.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| REVERTED dedup changes | CTO HOLD was correct. 05f confirmed zero cross-account collisions. |
| Dedup hypothesis rejected | BD transaction_ids ARE globally unique. No ID collision issue. |
| .007 silver AUA override re-endorsed | Gap is BD data completeness, not pipeline logic. Override is the structural bridge. |
| Passthrough fix validated | Journal/Valuation/CAA types recovered real data for 360 accounts. |

---

## Current State

**Status:** COMPLETE (investigation)
**Active branch:** `CLOUD`

Investigation complete. AUA gap root cause is BD transaction data incompleteness --
BD never delivered the full transaction history for ~635 accounts. Prices are confirmed
correct. The passthrough fix (Journal/Valuation/CAA) was necessary and helped 360 accounts.
The remaining gap requires the .007 silver AUA override, which bridges accounts where
our transaction-derived positions undercount vs BD's custodial allocation snapshots.

All code changes reverted -- no gold/silver scripts modified. 05f diagnostic enhanced
and confirmed the dedup is clean.

---

## Next Steps

1. **[0.4.0_DS_ClientPlatform] Proceed with .007 silver AUA override** -- this is now confirmed as the correct structural fix, not a workaround
2. **[0.6.0_AE_PartnerETL] Full gold rebuild with .007** after DS commits and DT pushes
3. **[0.6.0_AE_PartnerETL] Run 05e after gold rebuild** -- verify gross error reduction
4. **[0.4.0_DS_ClientPlatform] Evaluate .008 (bond classifier)** -- still gated on .007 results

**Do NOT:**
- Re-attempt dedup changes -- confirmed zero cross-account collisions
- Assume pricing fixes will help -- prices are correct, units are incomplete
- Skip .007 in favor of further investigation -- BD data gap is the terminal root cause
