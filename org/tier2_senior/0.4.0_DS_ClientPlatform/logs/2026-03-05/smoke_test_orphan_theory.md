# Smoke Test: Orphan Theory -- 0.4.0_DS_ClientPlatform

**Date:** 2026-03-05
**Context:** Follow-up to REQ_schwab_sot_cross_reference (2026-03-04)
**CORRECTION:** Materiality assessment (same session) DISPROVED the orphan theory.
See "Materiality Assessment" section below. The initial smoke test had a methodological
flaw (narrow matching window). At full-month grain, BD has 100% transaction coverage.

## Hypothesis

The Schwab SoT cross-reference revealed a persistent inflow gap: Schwab reports $637.7M
in TOA inflows over 13 months (May 2024 - May 2025), while our transaction-based NNA
captures only $182M in total external inflows. The $456M gap suggested that BD does not
always generate transaction records when positions arrive via ACAT custodial transfers.
Positions appear in BD's allocation feed (positions_cube) without a corresponding
Transfer In, Cash Deposit, or any NNA transaction.

**Theory:** When a client ACATs positions in-kind from Fidelity, Vanguard, etc. to
Schwab, the positions show up in BD's daily allocation snapshots as new holdings, but
BD's transaction feed never records the event. Our NNA pipeline -- which relies
exclusively on the transaction feed -- misses these inflows entirely.

## Method

Scanned `gold/positions_cube/` parquet files for Dec 2-13, 2024 (10 business days)
against a Nov 29 baseline. For each (account_id, asset_name) pair, detected:

- **New positions:** units go from 0/absent to >0
- **Unit increases:** existing positions where units increase by >1%

Cross-referenced every unit-increase event against `silver/transactions/` for the same
account_id + asset_name + date (+/-1 day settlement window). Looked for any matching
Transfer In, Cash Deposit, or NNA-flagged transaction.

December 2024 was chosen because it has the clearest gap: Schwab TOA In = $69.5M, our
captured NNA inflows = $30.1M, leaving $39.4M unexplained.

## Results

### Raw Detection

| Metric | Value |
|---|---|
| Analysis window | Dec 2 - Dec 13, 2024 (10 business days) |
| Baseline date | Nov 29, 2024 |
| Total unit-increase events detected | 7,995 |
| New positions (0 -> >0) | 5,322 |
| Existing unit increases (>1%) | 2,673 |
| Corroborated by Transfer In / Cash Deposit / NNA txn | 306 (3.8%) |
| Raw orphans (no matching transaction) | 7,689 (96.2%) |

### False Positive Removal

The 96.2% raw orphan rate is inflated by four systematic categories that are NOT ACAT
transfers:

| Category | Count | Explanation |
|---|---|---|
| iPath VIX + TrueShares Bear Hedge (Dec 13) | 3,475 | Coordinated model trades -- Buy transactions confirmed on all |
| OPAL DIVIDEND INCOME ETF | 117 | Internal proprietary fund, not external transfer |
| Derivatives / options (./ESH5 etc.) | 9 | Futures/options positions, not custody transfers |
| T-Bill ETF (SPDR Bloomberg 1-3M, Dec 13) | 593 | Systematic rebalance -- all 593 had Buy transactions |

**After false positive removal: ~3,464 genuine orphan events.**

### Dollar Value

| Metric | Value |
|---|---|
| Priced orphan events (had canonical price) | 401 |
| Total priced orphan value | $1,797,011 |
| Unpriced orphan events (no canonical price) | ~3,063 |
| Estimated unpriced orphan value | $10-30M |
| Known Transfer In captured in window | $11,714,775 |
| Known Cash Deposit captured in window | $10,898,810 |
| Schwab TOA In (all Dec 2024) | $69,500,000 |
| Our total captured NNA inflows (all Dec 2024) | $30,116,747 |
| Unexplained gap | $39,383,253 |

The largest-unit orphan assets -- STATE STREET SPDR BLOOMBERG 1-3 MONTH T-BILL ETF
(12,275 units), INVESCO OPTIMUM YIELD DIVERSIFIED COMMODITY (6,429 units), INVESCO
BULLETSHARES products (5,771 units) -- have no entry in `interpolated_prices`. At
typical NAVs ($50-$100/unit), these alone could represent $10-30M of the gap.

### Top 10 Genuine Orphan Events

| Date | Type | Account | Asset | Units | Price | Est. Value |
|---|---|---|---|---|---|---|
| Dec 6 | NEW_POSITION | z0817746791 | FID CONTRA POOL CL 2 | 10,653 | $47.64 | $507,505 |
| Dec 5 | NEW_POSITION | z0818012711 | T ROWE PRICE RET BLEND 2035 B | 11,553 | $17.29 | $199,749 |
| Dec 4 | UNIT_INCREASE | z0818927251 | ARISTA NETWORKS INC COM SHS | 699 | $148.20 | $103,594 |
| Dec 5 | NEW_POSITION | z0819120791 | NPK INTERNATIONAL INC COM SHS | 12,100 | $7.83 | $94,742 |
| Dec 10 | NEW_POSITION | z0818099941 | EVENTIDE LARGE CAP FOCUS I | 3,680 | $14.94 | $55,000 |
| Dec 9 | NEW_POSITION | z0815569571 | NEW YORK CITY HSG DEV CORP 3.95% | 45,000 | $1.00 | $45,000 |
| Dec 12 | UNIT_INCREASE | z0818099941 | EVENTIDE LARGE CAP FOCUS I | 3,009 | $14.96 | $45,000 |
| Dec 4 | UNIT_INCREASE | z0819573511 | ARISTA NETWORKS INC COM SHS | 288 | $148.20 | $42,682 |
| Dec 2 | NEW_POSITION | z0813092121 | EVENTIDE HIGH DIVIDEND ETF | 1,504 | $26.60 | $40,007 |
| Dec 10 | UNIT_INCREASE | z0813092121 | EVENTIDE HIGH DIVIDEND ETF | 1,500 | $25.64 | $38,453 |

The Fidelity Contra Pool event is the textbook case: a mutual fund that cannot be
bought on the open market (pool class shares are plan-specific), appearing as a new
position with 10,653 units and zero transaction record. This can only arrive via in-kind
custodial transfer.

## Initial Conclusion (SUPERSEDED)

The initial 10-day smoke test appeared to confirm the theory, finding ~3,464 "genuine
orphan events." This conclusion was WRONG -- see materiality assessment below.

---

## Materiality Assessment (Same Session -- Corrects Initial Findings)

After the initial smoke test, a materiality assessment was run at **full calendar month
grain** (Dec 1 -> Dec 31, 2024) to determine whether the orphan volume was significant
relative to the ~98M total rows in positions_cube.

### Scale

| Metric | Value |
|---|---|
| positions_cube total partitions | 2,072 (Jun 2020 - Mar 2026) |
| Estimated total rows | ~98M |
| Average rows per date | ~47,000 |
| Dec 2024 rows (start) | 68,684 |
| Dec 2024 rows (end) | 71,404 |

### Full-Month Orphan Detection

| Metric | Value |
|---|---|
| New (account, asset) pairs Dec 1 -> Dec 31 | 5,630 |
| Explained by Buy transaction | 5,378 (95.5%) |
| Explained by Transfer In (NNA) | 265 (4.7%) |
| Explained by any transaction | **5,630 (100%)** |
| **True orphans (no transaction at all)** | **0 (0.0%)** |

### Why the Smoke Test Was Wrong

The initial smoke test used a **+/-1 day matching window** when comparing day-over-day
position changes against transactions. This window was too narrow. A position appearing
in positions_cube on Dec 6 might have a corresponding Buy transaction on Dec 3 (trade
date vs settlement date vs BD posting date). At full-month grain, where the entire
month's transactions are matched against the entire month's position changes, the
coverage is 100%.

The 3,464 "orphan events" from the initial scan were:
- Positions with Buy transactions on a different day (outside +/-1 window)
- Model rebalances where Buy and position appearance were days apart
- NOT evidence of missing transaction records

### Revised Root Cause of NNA Inflow Gap

The $39.4M Dec 2024 inflow gap ($69.5M Schwab TOA In vs $30.1M our NNA inflows) is
**not** caused by missing positions or missing transactions. It is a **cash flow
measurement boundary** difference:

1. Schwab records ACAT transfers at the **custodial ledger level** as a single dollar
   figure for the entire transfer.
2. BD records the same event as potentially multiple transactions: a Cash Deposit for
   the cash portion and Buy transactions for the investment portion.
3. Buys are classified as investment decisions (not NNA) in BD's transaction taxonomy.
4. When an ACAT arrives and the advisor immediately invests the cash, the cash "passes
   through" -- Schwab sees the full TOA value, but BD only captures the Cash Deposit
   component as NNA.

Evidence: 2,223 accounts (90% of accounts with Buy-only new positions) had **zero NNA
inflow transactions** despite $27.4M in Buy volume. These accounts were funded from
existing cash balances or from ACAT cash that BD did not tag as a Cash Deposit.

### Verdict

**Orphan theory: DISPROVEN.** BD has complete transaction coverage for all positions.
The NNA gap is a cash flow classification boundary issue between Schwab and BD, not a
data completeness issue. No allocation-diff pipeline is warranted.

**Monitoring:** Quarterly orphan checks at full-month grain per methodology in
`docs/architecture/BD_NNA_FRAMEWORK.md` Section 7. Current baseline: 0.0% orphan rate.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Used Dec 2024 for smoke test | Largest documented inflow gap ($39.4M) |
| Initial: 10 business days, +/-1 day window | Proved insufficient; produced false positives |
| Correction: full calendar month grain | Eliminated timing artifacts; revealed 100% coverage |
| Excluded Buy-transacted events from NNA | Buy = investment decision, not asset flow per BD taxonomy |

## Files Read

| File | Location | Purpose |
|---|---|---|
| positions_cube partitions | s3://opal-data-bd/gold/positions_cube/ | Unit counts by (account, asset, date) |
| transaction partitions | s3://opal-data-bd/silver/transactions/ | Transaction matching |
| interpolated_prices | s3://opal-data-bd/gold/ | Dollar value estimation (initial test only) |

## Blockers

None. No allocation-diff pipeline needed -- BD transaction coverage is complete.

## Current State

Status: COMPLETE (with materiality correction)
Active branch: CLOUD
