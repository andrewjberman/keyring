# REQ: Schwab SoT May 2025 Cross-Reference -- 0.4.0_DS_ClientPlatform

**Date:** 2026-03-04
**Requested by:** CEO (off-books, logged as REQ)

## Objective

Compare Schwab's official 49 Financial Business Review Dashboard (through 5/30/2025) against
our internal data stack (bronze xlsx, silver parquets, gold layer outputs) to identify
why reported figures vary across the three data sources: Schwab (custodian), Black Diamond
(portfolio management), and our computed gold layer.

Source PDF: `C:\Users\AndrewBerman\Downloads\49 Financial Business Review Dashboard May 2025 1.pdf`

---

## 1. Schwab SoT Inventory (Structured from PDF)

### Firm Summary
| Metric | Value |
|--------|-------|
| Assets at Schwab | $1,042M |
| Assets Away | $0M |
| Total Clients | 2,460 |
| Average Client Size | $423.4K |
| 12-Month NNA | $344.1M |
| YoY Asset Change | +65% |

### Asset Mix (Current, May 2025)
| Asset Class | Value | Share |
|-------------|-------|-------|
| ETFs | $846M | 81% |
| Equities | $93M | 9% |
| Mutual Funds | $47M | 5% |
| Cash | $35M | 3% |
| Fixed Income | $19M | 2% |
| Other | $8M | <1% |
| Alternatives | $2M | <1% |

### Annual Assets (Corrected from chart position analysis)
| Year | Assets |
|------|--------|
| 2020 | $34.6M |
| 2021 | $44.6M |
| 2022 | $93.5M |
| 2023 | $544.7M |
| 2024 | $871.7M |
| 2025 (May) | $1,042M |

Note: Raw PDF text extraction scrambled year-value pairings. Corrected via x-position
analysis of text blocks against year axis labels.

### Annual NNA (Corrected)
| Year | NNA |
|------|-----|
| 2020 | $3.3M |
| 2021 | $4.6M |
| 2022 | $47.3M |
| 2023 | $281.3M |
| 2024 | $390.1M |
| 2025 (YTD May) | $124.3M |

### Monthly Assets (May 2024 - May 2025)
| Month | Assets |
|-------|--------|
| May 2024 | $629.5M |
| Jun 2024 | $678.7M |
| Jul 2024 | $721.8M |
| Aug 2024 | $742.2M |
| Sep 2024 | $757.5M |
| Oct 2024 | $790.9M |
| Nov 2024 | $833.1M |
| Dec 2024 | $871.7M |
| Jan 2025 | $940.5M |
| Feb 2025 | $961.9M |
| Mar 2025 | $975.8M |
| Apr 2025 | $989.6M |
| May 2025 | $1,042M |

### Monthly NNA (May 2024 - May 2025)
| Month | NNA |
|-------|-----|
| May 2024 | $21M |
| Jun 2024 | $9M |
| Jul 2024 | $29M |
| Aug 2024 | $22M |
| Sep 2024 | $44M |
| Oct 2024 | $64M |
| Nov 2024 | $18M |
| Dec 2024 | $46M |
| Jan 2025 | $7M |
| Feb 2025 | $9M |
| Mar 2025 | $28M |
| Apr 2025 | $46M |
| May 2025 | $10M |

### Monthly TOA Flows (May 2024 - May 2025)
| Month | TOA In | TOA Out | Net TOA |
|-------|--------|---------|---------|
| May 2024 | $44.8M | ($24.3M) | $20.6M |
| Jun 2024 | $49.6M | ($40.7M) | $8.9M |
| Jul 2024 | $49.8M | ($20.7M) | $29.0M |
| Aug 2024 | $52.3M | ($30.5M) | $21.8M |
| Sep 2024 | $70.2M | ($26.2M) | $44.0M |
| Oct 2024 | $81.8M | ($17.5M) | $64.3M |
| Nov 2024 | $28.9M | ($11.0M) | $17.9M |
| Dec 2024 | $69.5M | ($23.2M) | $46.3M |
| Jan 2025 | $23.8M | ($16.4M) | $7.4M |
| Feb 2025 | $40.9M | ($31.4M) | $9.5M |
| Mar 2025 | $43.4M | ($15.1M) | $28.2M |
| Apr 2025 | $58.8M | ($12.5M) | $46.3M |
| May 2025 | $23.9M | ($13.5M) | $10.4M |

### Growth Sources (YoY, May 2024 to May 2025)
| Component | Value |
|-----------|-------|
| PY Assets (May 2024) | $629M |
| New Client NNA | $321M |
| Existing Client NNA | $34M |
| Market Impact | $58M |
| CY Assets (May 2025) | $1,042M |

Accounting identity: $629M + $321M + $34M + $58M = $1,042M. Checks out.

### 12-Month TOA Top 10 Contra Firms
| Contra Firm | TOA In | TOA Out | Net |
|-------------|--------|---------|-----|
| Fidelity | $69M | ($4M) | $73M |
| Citigroup | $42M | $0M | $42M |
| Wells Fargo | $16M | $0M | $16M |
| Pershing | $15M | ($1M) | $16M |
| Vanguard | $15M | $0M | $15M |
| Morgan Stanley | $8M | $0M | $8M |
| American Funds | $5M | $0M | $5M |
| RBC | $5M | $0M | $5M |
| Bank of America | $4M | $0M | $5M |
| JP Morgan Chase | $4M | $0M | $4M |

### Schwab Key Definitions (from Glossary page)
- **NNA** = total inflows + outflows. Includes Cash, TOA, AND FDIC.
- **New Client NNA** = from clients on platform < 365 days.
- **Existing Client NNA** = from clients on platform > 365 days.
- **Market Impact** = YoY balance change not attributable to NNA.
- **Clients** = funded clients grouped by individual address (not accounts).
- **TOA** = ACAT transfers between custodians (subset of NNA).

---

## 2. Cross-Reference: Monthly AUA

| Month | Our Gold Layer | Schwab | Difference | Diff% |
|-------|---------------|--------|------------|-------|
| May 2024 | $719,740,597 | $629,500,000 | +$90,240,597 | +14.3% |
| Jun 2024 | $705,351,848 | $678,700,000 | +$26,651,848 | +3.9% |
| Jul 2024 | $733,175,746 | $721,800,000 | +$11,375,746 | +1.6% |
| Aug 2024 | $752,788,403 | $742,200,000 | +$10,588,403 | +1.4% |
| Sep 2024 | $803,853,317 | $757,500,000 | +$46,353,317 | +6.1% |
| Oct 2024 | $838,345,097 | $790,900,000 | +$47,445,097 | +6.0% |
| Nov 2024 | $899,422,578 | $833,100,000 | +$66,322,578 | +8.0% |
| Dec 2024 | $911,907,383 | $871,700,000 | +$40,207,383 | +4.6% |
| Jan 2025 | $1,042,953,161 | $940,500,000 | +$102,453,161 | +10.9% |
| Feb 2025 | $1,094,609,500 | $961,900,000 | +$132,709,500 | +13.8% |
| Mar 2025 | $1,093,615,992 | $975,800,000 | +$117,815,992 | +12.1% |
| Apr 2025 | $1,121,066,056 | $989,600,000 | +$131,466,056 | +13.3% |
| May 2025 | $1,177,644,038 | $1,042,000,000 | +$135,644,038 | +13.0% |

**Key observation:** Our gold layer consistently runs ABOVE Schwab by $10M-$135M. The gap
has been widening: ~+1.5% in Jul/Aug 2024 to ~+13% by May 2025. The divergence
accelerated sharply in Jan 2025 and has not closed since.

---

## 3. Cross-Reference: Annual AUA (Year-End)

| Year | Our Gold | Schwab | Difference | Diff% |
|------|----------|--------|------------|-------|
| 2020 | $126,241,748 | $34,600,000 | +$91,641,748 | +265% |
| 2021 | $248,453,865 | $44,600,000 | +$203,853,865 | +457% |
| 2022 | $321,038,869 | $93,500,000 | +$227,538,869 | +243% |
| 2023 | $630,912,624 | $544,700,000 | +$86,212,624 | +16% |
| 2024 | $911,907,383 | $871,700,000 | +$40,207,383 | +5% |

**Key observation:** Massive divergence in 2020-2022 (+265% to +457%). Converges toward 2024 (+5%).
This strongly suggests BD was tracking assets that Schwab was not yet custodying in those years
(the 49F migration from TD Ameritrade was underway during this period).

---

## 4. Cross-Reference: Monthly NNA

| Month | Our NNA | Schwab NNA | Difference | Diff% |
|-------|---------|------------|------------|-------|
| May 2024 | -$1,798,457 | $21,000,000 | -$22,798,457 | -109% |
| Jun 2024 | -$7,441,253 | $9,000,000 | -$16,441,253 | -183% |
| Jul 2024 | $25,522,594 | $29,000,000 | -$3,477,406 | -12% |
| Aug 2024 | -$1,692,727 | $22,000,000 | -$23,692,727 | -108% |
| Sep 2024 | $23,030,034 | $44,000,000 | -$20,969,966 | -48% |
| Oct 2024 | $41,347,395 | $64,000,000 | -$22,652,605 | -35% |
| Nov 2024 | $11,981,257 | $18,000,000 | -$6,018,743 | -33% |
| Dec 2024 | $11,935,242 | $46,000,000 | -$34,064,758 | -74% |
| Jan 2025 | $45,219,741 | $7,000,000 | +$38,219,741 | +546% |
| Feb 2025 | $21,864,927 | $9,000,000 | +$12,864,927 | +143% |
| Mar 2025 | $14,959,887 | $28,000,000 | -$13,040,113 | -47% |
| Apr 2025 | $5,355,147 | $46,000,000 | -$40,644,853 | -88% |
| May 2025 | $21,273,219 | $10,000,000 | +$11,273,219 | +113% |

**13-month NNA totals:**
- Our NNA: $211,557,007
- Schwab NNA: $354,700,000
- Gap: -$143,142,993 (-40%)

**Key observation:** NNA is wildly divergent month-to-month. Some months we show NEGATIVE NNA
where Schwab shows positive (May, Jun, Aug 2024). Some months we show much MORE positive
(Jan, Feb 2025). The sign reversals indicate fundamentally different measurement approaches
or timing windows.

---

## 5. Cross-Reference: Monthly Inflows/Outflows vs Schwab TOA

| Month | Our Inflows | Our Outflows | Our Net | Schwab TOA In | Schwab Out | Schwab Net |
|-------|-------------|-------------|---------|---------------|------------|------------|
| May 2024 | $14,614,495 | $16,412,952 | -$1,798,457 | $44,800,000 | $24,300,000 | $20,500,000 |
| Jun 2024 | $46,240,402 | $53,681,654 | -$7,441,253 | $49,600,000 | $40,700,000 | $8,900,000 |
| Jul 2024 | $33,354,007 | $7,831,413 | $25,522,594 | $49,800,000 | $20,700,000 | $29,100,000 |
| Aug 2024 | $32,203,168 | $33,895,895 | -$1,692,727 | $52,300,000 | $30,500,000 | $21,800,000 |
| Sep 2024 | $37,472,187 | $14,442,153 | $23,030,034 | $70,200,000 | $26,200,000 | $44,000,000 |
| Oct 2024 | $58,158,645 | $16,811,250 | $41,347,395 | $81,800,000 | $17,500,000 | $64,300,000 |
| Nov 2024 | $20,009,051 | $8,027,794 | $11,981,257 | $28,900,000 | $11,000,000 | $17,900,000 |
| Dec 2024 | $23,304,471 | $11,369,229 | $11,935,242 | $69,500,000 | $23,200,000 | $46,300,000 |
| Jan 2025 | $62,510,526 | $17,290,785 | $45,219,741 | $23,800,000 | $16,400,000 | $7,400,000 |
| Feb 2025 | $74,597,775 | $52,732,848 | $21,864,927 | $40,900,000 | $31,400,000 | $9,500,000 |
| Mar 2025 | $42,341,730 | $27,381,843 | $14,959,887 | $43,400,000 | $15,100,000 | $28,300,000 |
| Apr 2025 | $39,473,723 | $34,118,576 | $5,355,147 | $58,800,000 | $12,500,000 | $46,300,000 |
| May 2025 | $47,833,561 | $26,560,341 | $21,273,219 | $23,900,000 | $13,500,000 | $10,400,000 |

**13-month totals:**
- Our Inflows: $532,113,740 vs Schwab TOA In: $637,700,000 (we under-count by $106M)
- Our Outflows: $320,556,733 vs Schwab TOA Out: $283,000,000 (we over-count by $38M)
- Our Net: $211,557,007 vs Schwab Net: $354,700,000 (we under-count by $143M)

**Critical note:** Schwab TOA is a SUBSET of Schwab NNA. Schwab NNA includes Cash + TOA + FDIC.
TOA is only the ACAT transfer component. Our flows use Cash Deposit/Withdrawal + Transfer In/Out
from BD transaction data, which maps closest to Schwab's full NNA definition (not just TOA).
Yet we still under-count inflows by ~17% and over-count outflows by ~13%.

---

## 6. Cross-Reference: Growth Decomposition (YoY May 2024 to May 2025)

| Component | Our Gold | Schwab | Difference |
|-----------|----------|--------|------------|
| PY Assets | $719,740,597 | $629,000,000 | +$90,740,597 |
| CY Assets | $1,177,644,038 | $1,042,000,000 | +$135,644,038 |
| NNA (12M) | $213,355,464 | $355,000,000 | -$141,644,536 |
| Market Impact | $244,547,978 | $58,000,000 | +$186,547,978 |
| Total Change | $457,903,441 | $413,000,000 | +$44,903,441 |

**Key observation:** We attribute ~$245M to Market Impact vs Schwab's $58M. This is because
our lower NNA pushes more of the AUA growth into the "market" residual. The accounting
identity holds for both: CY = PY + NNA + Market. But the NNA/Market split is very different.

---

## 7. Cross-Reference: Client / Account Counts

| Source | Metric | Count |
|--------|--------|-------|
| Schwab | Funded clients (by address) | 2,460 |
| BD BI (Jan 2026) | Relationships (deduped) | 2,818 |
| BD BI (Jan 2026) | Accounts (deduped) | 6,084 |
| Our client_dimension | Relationships (all-time) | 3,515 |
| Our accounts_dimension | Accounts (total) | 9,706 |
| Our accounts_dimension | Accounts (open) | 9,332 |
| Our accounts_dimension | Relationships with open accts | 3,372 |

**Gap analysis:**
- Our all-time relationships (3,515) vs Schwab clients (2,460) = +1,055 (+43%)
- Our open-acct relationships (3,372) vs BD BI relationships (2,818) = +554
- BD BI relationships (2,818) vs Schwab clients (2,460) = +358
- Our account count (9,706) vs BD BI accounts (6,084) = +3,622

The 3,622-account gap between our accounts_dimension and BD BI suggests our dimension
includes historical/closed accounts that BD's BI monthly snapshot excludes. The BI file
showed 0 closed accounts in January 2026 (Account Is Open = True for all 6,084 rows).

---

## 8. BD BI Validation Point (January 2026)

BD BI EMV (deduped by AccountID): $1,520,959,643
Our silver/daily_aua_firm (2026-01-27): $1,545,072,909
Our accounts_dimension (2026-01-27): 8,405 accounts

BD-reported EMV vs our calculated AUA: gap of $24M (+1.6%). This is a reasonable pricing
difference (our canonical prices may differ slightly from BD's end-of-day values).

The BD BI file also reveals multiple portfolio groups per account (same account appears in
"49F Schwab AUM", individual advisor groups, and "Local Ops" groups). Deduplication by
AccountID is essential.

---

## 9. Root Cause Hypotheses

### H1: AUA Overcount (Our Gold > Schwab by ~13%)

**Primary cause: BD tracks assets Schwab does not custody.**

Evidence:
- Schwab reports $0M "Assets Away" but this is based on ADV filings, not BD data.
- BD's BI data shows a "49 Private Wealth" portfolio group with $348.9M EMV (Jan 2026).
  These may be assets held at custodians other than Schwab (private placements,
  alternatives, direct holdings) that BD tracks for reporting but Schwab doesn't see.
- Our positions_cube is built from ALL BD allocation data, not filtered to Schwab-custodied
  positions only. We compute `total_aua = sum(units x price)` for every position BD reports.

**Secondary cause: Pricing differences.**

- Our canonical_prices are built from Yahoo Finance + transaction-observed + interpolation.
- Schwab uses its own pricing feed. For ETFs/equities this is minimal difference.
- For alternatives, illiquid, or private positions, our prices could diverge significantly.

**Supporting data:** In early years (2020-2022), our AUA was 2.5x-4.6x Schwab's. This is
the TD Ameritrade migration period -- BD was tracking all assets before they moved to Schwab.

### H2: NNA Undercount (Our Gold < Schwab by ~40%)

**Primary cause: Different NNA definitions.**

- Schwab NNA = Cash + TOA (ACAT) + FDIC. Includes all cash movements including FDIC sweep.
- Our NNA = Cash Deposit + Cash Withdrawal + Transfer In + Transfer Out from BD transactions.
- We exclude: Dividend, Dividend Reinvestment, Buy, Sale, Interest, Expense, Corporate Action,
  Journal, Return of Capital, Management Fee, Income Reinvestment.
- Schwab likely counts some of these as NNA (particularly FDIC sweeps and interest).

**Secondary cause: In-kind transfers may be missing.**

- When positions transfer between custodians (ACAT), they may appear in BD's positions_cube
  as new positions without a corresponding Transfer In transaction. If BD does not always
  generate a transaction record for in-kind transfers, our flow accounting misses them.
- This would explain why our inflows are $106M below Schwab's TOA In.

**Tertiary cause: Outflow capping artifacts.**

- Script 05 applies an AUA-based outflow cap (VELOCITY_CAP_ENABLED) and per-event $50M cap.
- These caps prevent BD data quality issues (phantom withdrawals from mispriced 401k accounts)
  from inflating outflows. But they may also suppress legitimate large outflows.
- Net effect: our outflows are $38M ABOVE Schwab's TOA Out despite the caps. This suggests
  BD records more outflow events than Schwab tracks as TOA.

**Timing differences:**

- Schwab uses calendar month-end. Our data uses the last available BD date per month.
- Settlement timing (T+1 vs T+2) could shift flows between months.

### H3: Client Count Overcount (+43%)

**Primary cause: Our client_dimension includes all-time relationships.**

- 3,515 total vs 2,460 Schwab = +1,055. Of these, only 3,372 have open accounts.
- Schwab counts "funded clients grouped by individual address" -- multi-account households
  count as one client.
- BD relationships are by relationship_id, which may split households differently.
- Historical/terminated relationships inflate our count.

---

## 10. Schwab Glossary Key Definitions

For reference, Schwab defines:
- "Clients moving from existing Schwab platforms (Retail or Advisor Services) to an Advisor
  are not considered NNA" -- this means internal Schwab-to-Schwab transfers do NOT count.
  This is a potential source of our Jan 2025 spike: if BD logged an internal Schwab transfer
  as a Transfer In, we'd count it as NNA while Schwab would not.
- "TOA Ratio: the ratio of TOA inflows to TOA outflows" -- NOT the same as NNA ratio.
  TOA is strictly ACAT transfers. NNA is broader.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Corrected annual Assets/NNA ordering from PDF | PDF text extraction scrambled chart label-value pairs; used x-position analysis |
| Used last available date per month for matching | Schwab uses calendar month-end; our data may not have exact month-end dates |
| Deduped BD BI by AccountID | Same account appears in multiple portfolio groups (architect, local ops, firm) |
| Did not attempt to filter our AUA to Schwab-only positions | No reliable Schwab-custodied flag exists in BD data |

---

## Files Read

| File | Location | Purpose |
|------|----------|---------|
| Schwab PDF | local download | Source of truth |
| timeseries_chart.json | s3://opal-data-bd/gold/ | Our AUA/NNA timeseries |
| header_metrics.json | s3://opal-data-bd/gold/partner_analytics/ | Our AUA totals by period |
| client_dimension.parquet | s3://opal-data-bd/gold/ | Relationship count |
| accounts_dimension_latest.parquet | s3://opal-data-bd/gold/ | Account count |
| daily_aua_firm.parquet | s3://opal-data-bd/silver/ | Legacy firm-wide AUA |
| daily_aua.parquet | s3://opal-data-bd/silver/ | Per-account AUA |
| BI_2025_latest.xlsx | s3://opal-data-bd/bronze/bi/ | BD BI account mapping (Jan 2026) |
| silver/transactions/*.parquet | s3://opal-data-bd/ | Transaction types inventory |
| silver/allocations/*.parquet | s3://opal-data-bd/ | BD allocation market values |
| 05_build_client_performance.py | data/black_diamond/scripts/gold/ | AUA computation logic |
| 09_generate_partner_analytics.py | data/black_diamond/scripts/gold/ | Partner analytics logic |
| bd-portal-publisher/lambda_function.py | infra/aws/lambda/bd-pipeline/ | Timeseries chart logic |

---

## Blockers

None. Investigation complete. Findings require CEO decision on next steps.

---

## Current State

**Status:** COMPLETE
**Active branch:** CLOUD

Full inventory of Schwab SoT figures structured from PDF. Cross-referenced against
gold layer (timeseries_chart.json, partner_analytics), silver layer (daily_aua_firm,
daily_aua, transactions), and bronze layer (BI xlsx, allocations). Three major variance
categories identified: AUA overcount (+13%), NNA undercount (-40%), and client count
overcount (+43%). Root cause hypotheses documented with supporting data.

---

## Next Steps

1. **[CEO] Decide whether to filter gold AUA to Schwab-custodied positions only.**
   This requires a custodian flag on positions or accounts. BD may have a "portfolio_group"
   or custodian field that distinguishes Schwab-held vs held-away positions.

2. **[DS] If CEO directs: investigate portfolio_group filtering.**
   "49F Schwab AUM" in BI data maps to $737M (Jan 2026) for 2,987 accounts.
   Compare with Schwab's $940.5M (Jan 2025). The gap would narrow significantly
   if we can identify which portfolio groups are Schwab-custodied.

3. **[DS] If CEO directs: reconcile NNA definitions.**
   Compare our transaction type classification against Schwab's NNA definition.
   Specifically: do FDIC sweeps and internal Schwab transfers appear in BD transactions?
   If so, under what transaction_type?

4. **[DS] If CEO directs: deep-dive on specific month variances.**
   Jan 2025 is the most extreme: our NNA = +$45M vs Schwab NNA = +$7M. This $38M
   discrepancy in a single month suggests a large in-kind transfer or data event.
   Pull BD transactions for January 2025 and identify the top 10 flows by magnitude.

**Do NOT:**
- Modify any gold layer scripts based on this analysis (investigation only)
- Push any changes (DS cannot push)
- Assume Schwab is correct and BD is wrong or vice versa -- these are different systems
  with different measurement scopes
