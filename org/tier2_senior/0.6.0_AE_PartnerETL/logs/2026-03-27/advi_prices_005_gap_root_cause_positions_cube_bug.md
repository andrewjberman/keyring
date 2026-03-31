# ADVI_PRICES.005 -- AUA Gap Root Cause: Positions Cube Undercounting -- 0.6.0_AE_PartnerETL

**Date:** 2026-03-27
**Start Time:** 1:15 AM ET
**End Time:** 2:15 AM ET

## Objective

Trace the $150M gross overvaluation / $138M gross undervaluation identified by 05e to its root cause. Determine whether Yahoo-first pricing, transaction prices, or something else drives the gold-vs-silver AUA gap.

---

## Finding: The AUA gap is NOT a pricing problem. It is a positions cube construction bug.

### Evidence Chain

**Step 1 -- Pricing is correct.** Compared canonical prices vs BD transaction prices for PATHFINDER DISCIPLINED US EQUITY ETF (PFDE). BD transactions price it at $23.83-$23.88. Yahoo Finance confirms $23.835 close on 3/25. Our canonical price is $23.94. All three sources agree within pennies. This holds across all 12 securities in the test account.

**Step 2 -- Account-level deep dive (z0821398141, "Ren Inc Charitable Fund").** Silver (BD allocation) says account is worth $5,460,004. Our gold positions sum to $1,530,790. Gap: $3,929,214. Cash is only $171,510 -- the gap is in non-cash securities.

**Step 3 -- Position-by-position comparison shows prices match, but unit counts are wrong.**

| Asset | Cube Units | Canon Px | Txn Px | Gold MV |
|-------|-----------|----------|--------|---------|
| PATHFINDER DISCIPLINED US EQUITY ETF | 22,212 | $23.94 | $23.83 | $531,755 |
| PATHFINDER FOCUSED OPPORTUNITIES ETF | 21,734 | $22.36 | $22.34 | $485,972 |
| SPDR HIGH YIELD BOND ETF | 8,974 | $23.29 | $23.26 | $209,004 |
| OPAL DIVIDEND INCOME ETF | 2,938 | $37.19 | -- | $109,264 |
| ... (8 more) | | | | |
| **TOTAL** | | | | **$1,530,790** |

Prices are correct. **The cube just doesn't have enough units.**

**Step 4 -- Full transaction scan.** Scanned all 239 transaction files from 2025-07 onward. Account has 426 transactions across 30 securities since 2025-12-31. The positions cube is massively undercounting:

| Asset | Cube Units | Buy Txns | Sell Txns | Expected Net | Missing |
|-------|-----------|----------|-----------|-------------|---------|
| PATHFINDER DISCIPLINED US EQUITY ETF | 22,212 | +223,420 | -36,208 | ~187,212 | ~165,000 |
| STATE STREET SPDR PORTFOLIO S&P 500 ETF | **0** | +3,693 | -90,688 | complex | **entirely absent** |
| OPAL INTERNATIONAL DIVIDEND INCOME ETF | 671 | +6,117 | -43,568 | complex | massive |
| OPAL DIVIDEND INCOME ETF | 2,938 | +6,492 | -28,432 | complex | massive |
| INVESCO QQQ TRUST SERIES I | 25 | +25 | 0 | 25 | **0 (only match)** |

Only 1 of 30 traded securities (INVESCO QQQ) has matching units between cube and transactions.

**Step 5 -- Pattern across all accounts.**

| Gap Severity | Accounts | Silver AUA | Median Positions | Zero Positions |
|---|---|---|---|---|
| <5% gap (healthy) | 1,940 | $517M | 14 | 0 |
| 5-50% gap | 3,336 | $967M | -- | -- |
| >50% gap (worst) | 995 | $127M | 2 | 432 (43%) |

Worst-offender accounts have median 2 positions (vs 14 for healthy accounts) and 43% have zero positions at all despite BD showing non-zero market value. Median create date for worst offenders is June 2024 vs July 2025 for healthy -- older accounts are more affected.

---

## Root Cause

`02_build_positions_cube.py` is not accumulating transaction units correctly. The transactions exist in the silver layer -- 426 transactions across 30 securities for this one account alone. But the positions cube captures only a small fraction of the units. The result is systematic undervaluation of accounts because we hold the right prices but the wrong (too small) number of units.

This is NOT addressable by Yahoo-first pricing, scoped overrides, or any price-level fix. The $150M/$138M gross over/under in 05e is driven by missing positions, not wrong prices.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Stopped investigating pricing fixes | Confirmed prices match BD transactions within pennies across all tested securities. The gap is not price-driven. |
| Identified 02_build_positions_cube.py as the target | Transaction data exists in silver, prices are correct, but cube unit counts are wrong. The bug is in how transactions are accumulated into positions. |

---

## Files Modified

None. This session was diagnostic only.

---

## Current State

**Status:** BLOCKED -- requires DS investigation of 02_build_positions_cube.py
**Active branch:** `CLOUD`

The AUA gap ($150M gross over / $138M gross under / $289M absolute error) is caused by `02_build_positions_cube.py` undercounting units. Account z0821398141 demonstrates the pattern: 426 transactions in silver, 30 securities traded, but the cube captures only a fraction of units (e.g., PDFE: 22K units in cube vs ~187K expected from net transactions). 995 accounts have >50% gap, 432 of those have zero positions despite non-zero silver AUA. The EC2 (i-01003b035d2988dfb) is still running with diagnostic scripts.

## Next Steps

1. **[0.4.0_DS_ClientPlatform] Investigate 02_build_positions_cube.py unit accumulation logic** -- Why does the cube show 22,212 units of PDFE when net transactions show ~187,212? Check how buys, sells, dividends, and transfers are summed. Check the start-date windowing (incremental mode uses `--start-date 8 days ago` -- is the full history being loaded for position accumulation?).
2. **[0.4.0_DS_ClientPlatform] Check forward-fill logic** -- Positions cube forward-fills from last transaction. For accounts with sparse recent activity, are older positions being dropped at the partition boundary?
3. **[0.6.0_AE_PartnerETL] After DS fix, re-run gold incremental and 05e** -- Verify gross error drops. With correct unit counts and correct prices, the gap should collapse.
4. **[0.6.0_AE_PartnerETL] Stop EC2 after DS confirms they have what they need** -- c6i.16xlarge still running for ad-hoc queries.

**Do NOT:**
- Pursue further pricing fixes (Yahoo-first, overrides, etc.) -- prices are confirmed correct
- Assume the gap is related to the historical-prices fetcher bug -- that's a separate issue (now fixed)
- Re-run 05e expecting improvement without fixing the cube
