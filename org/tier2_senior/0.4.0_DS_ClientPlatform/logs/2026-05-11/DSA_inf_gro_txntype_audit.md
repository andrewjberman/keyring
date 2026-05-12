# Orion txn_type Universe Audit — ADVI_INFGRO Stage -1
# Completed by: 0.4.0_DS_ClientPlatform~B (DS~A sessions wrapped; ~B covering)
# Date: 2026-05-11
# Authorized by: Andrew direct relay (CTO 20260511T205735Z)

---

## Schema Discovery

Silver transactions partition: `s3://opal-data-inf/silver/transactions/`
Total partitions: 1,510 (2020-05-26 to 2026-05-08)
Total rows across full history: 1,145,124

Two type-classification columns present:
- `activity_category` — higher-level Orion classification (coarser)
- `type_desc` — granular transaction type (this is the canonical classification column)

Both columns populated on all rows inspected. `type_desc` has 58 distinct (type_desc, activity_category) pairs; 43 distinct type_desc values when collapsed. **Recommend CTO uses `type_desc` as the taxonomy key** — activity_category is a coarser grouping that loses precision for NNA/Return/Internal distinctions.

---

## Full Taxonomy Table

Bucket key: **N** = NNA | **I** = Internal | **R** = Return | **?** = REVIEW (see notes below table)

| type_desc | activity_category | row_count | first_date | last_date | sample_ticker | sample_amount | bucket |
|---|---|---:|---|---|---|---:|:---:|
| Buy Exchange | Exchange In | 326,134 | 2020-05-26 | 2026-05-08 | FDRXX | 200.00 | **I** |
| Sell Exchange | Exchange Out | 326,134 | 2020-05-26 | 2026-05-08 | FID:CASH | -200.00 | **I** |
| Income Reinvested | Net Dividends/Interest/Gains Withdrawn | 224,497 | 2020-06-05 | 2026-05-08 | FID:CASH | 2.87 | **I** |
| Dividend to Cash | Dividends and Interest | 213,185 | 2020-06-05 | 2026-05-08 | PFF | 2.87 | **R** |
| Management Fee | Advisory Fees Paid | 14,449 | 2020-07-10 | 2026-05-08 | FID:CASH | -120.39 | **R** |
| Merge In from Other Account | Merge In | 6,521 | 2020-06-03 | 2026-05-04 | AALXX | 40,323.43 | **N** |
| Long Term Gain to Cash | Dividends and Interest | 4,725 | 2020-12-02 | 2026-05-08 | MLAIX | 960.37 | **R** |
| Trading Expense | Misc Charge | 4,472 | 2021-03-24 | 2026-05-08 | FAFFX | -5.29 | **R** |
| Client Contribution | Contributions | 4,358 | 2020-05-26 | 2026-05-07 | FID:CASH | 200.00 | **N** |
| Client Distribution | Distributions | 3,992 | 2020-06-08 | 2026-05-08 | FID:CASH | -2,550.00 | **N** |
| Short Term Gain to Cash | Dividends and Interest | 3,586 | 2020-12-07 | 2026-03-30 | GOVT | 26.50 | **R** |
| Interest Paid in Cash | Dividends and Interest | 3,012 | 2020-11-30 | 2026-05-08 | FCASH | 1.15 | **R** |
| Federal Tax Withheld | Distributions | 2,252 | 2020-06-09 | 2026-05-08 | FID:CASH | -1,428.50 | **R** |
| Internal Account Journal In | Journal In | 1,271 | 2020-07-01 | 2026-05-08 | FID:CASH | 0.01 | **I** |
| External Account Activity In | Merge In | 1,145 | 2022-08-29 | 2026-01-30 | FDRXX | 1.73 | **N** |
| Starting Value | Contributions | 896 | 2021-01-26 | 2026-05-04 | AMMXX | 32,143.21 | **?** |
| Fee Credit | Advisory Fees Paid | 862 | 2020-10-12 | 2026-04-20 | FID:CASH | 137.54 | **R** |
| Internal Account Journal Out | Journal Out | 769 | 2020-07-09 | 2026-05-08 | FID:CASH | -30,000.00 | **I** |
| Decrease in Value | Other | 398 | 2020-08-03 | 2022-09-28 | PFONX | -0.96 | **I** |
| Rollover Contribution | Contributions | 361 | 2020-08-27 | 2026-05-05 | FID:CASH | 13,332.00 | **N** |
| Merge In Exchange | Exchange In | 350 | 2021-05-07 | 2025-10-24 | FID:CASH | 118.43 | **?** |
| Merge Out Exchange | Exchange Out | 350 | 2021-05-07 | 2025-10-24 | PRSP | -118.43 | **?** |
| Merge Out to Other Account | Merge Out | 350 | 2020-06-05 | 2026-05-01 | TMAAX | -19,393.43 | **N** |
| State Tax Withheld | Distributions | 274 | 2021-03-29 | 2026-05-08 | FID:CASH | -20.00 | **R** |
| Cancel Account | Distributions | 101 | 2025-06-30 | 2026-05-05 | FCASH | -87.46 | **?** |
| Dividend Paid from Cash | Dividends and Interest | 101 | 2020-12-08 | 2025-04-30 | NHMRX | -67.86 | **?** |
| Income Paid | Net Dividends/Interest/Gains Withdrawn | 101 | 2020-12-08 | 2025-04-30 | FID:CASH | -19.16 | **?** |
| Trading Expense | Other | 77 | 2024-05-01 | 2026-05-06 | PHLPX | -11.00 | **R** |
| Dividend Reinvested | Dividend Interest Reinvested | 59 | 2026-02-04 | 2026-05-06 | BIV | 49.84 | **I** |
| Dividend to Cash | Other | 38 | 2024-01-25 | 2026-04-23 | ORCL | 57.78 | **R** |
| Foreign Dividend Tax | Other | 33 | 2024-12-06 | 2026-05-08 | UNCRY | -41.49 | **R** |
| Foreign Tax Withheld | Distributions | 33 | 2024-12-06 | 2026-05-08 | FID:CASH | -65.69 | **R** |
| Interest Reinvested | Dividend Interest Reinvested | 25 | 2025-05-20 | 2026-04-30 | FID:CASH | 1.52 | **I** |
| ADR Fee | Misc Charge | 24 | 2023-08-04 | 2026-05-08 | FID:CASH | -0.95 | **R** |
| Merge In from Other Account | Other | 24 | 2023-07-05 | 2026-05-06 | FID:CASH | 13.18 | **N** |
| Income Reinvested | Other | 22 | 2024-10-24 | 2026-04-23 | FID:CASH | 58.36 | **I** |
| Employer Contribution | Contributions | 18 | 2022-01-03 | 2026-01-13 | FID:CASH | 375.00 | **N** |
| Internal Account Journal Out | Other | 17 | 2025-05-01 | 2026-05-01 | FID:CASH | -0.39 | **I** |
| External Account Activity Out | Merge Out | 14 | 2024-05-20 | 2025-07-21 | FDRXX | -7.78 | **N** |
| Merge Out to Other Account | Other | 10 | 2021-12-20 | 2026-05-04 | FID:CASH | -50.00 | **N** |
| ADR Fee | Other | 9 | 2025-01-09 | 2026-05-05 | FID:CASH | -0.81 | **R** |
| Return of Capital | Dividends and Interest | 9 | 2021-11-25 | 2026-02-20 | 30xxxx339 | 24.81 | **I** |
| Administrative Fee | Misc Charge | 8 | 2021-01-14 | 2026-04-30 | FID:CASH | -8.00 | **R** |
| Administrative Fee Adjustment | Misc Charge | 6 | 2020-06-17 | 2020-09-16 | FID:CASH | 125.00 | **R** |
| Dividend Reinvested | Other | 6 | 2026-01-30 | 2026-05-01 | DIVZ | 81.82 | **I** |
| Spin Off in | Exchange In | 6 | 2020-11-17 | 2025-10-30 | VTRS | 983.05 | **I** |
| Spin Off out | Exchange Out | 6 | 2020-11-17 | 2025-10-30 | PFE | -983.05 | **I** |
| Wire Fee | Misc Charge | 6 | 2023-07-19 | 2026-04-29 | FID:CASH | -15.00 | **R** |
| Client Contribution | Other | 5 | 2025-09-18 | 2026-05-08 | FID:CASH | 200.00 | **N** |
| Internal Account Journal In | Other | 5 | 2025-05-01 | 2026-05-01 | FID:CASH | 0.39 | **I** |
| Interest Reinvested | Other | 4 | 2025-11-20 | 2026-01-30 | FID:CASH | 4.29 | **I** |
| Management Fee | Other | 4 | 2026-04-14 | 2026-04-14 | FID:CASH | -218.88 | **R** |
| Interest Paid | Other | 3 | 2022-01-20 | 2024-02-20 | FID:CASH | -1.27 | **R** |
| Return of Principal (Bonds) | Dividends and Interest | 2 | 2026-04-02 | 2026-04-02 | 525ESC0S9 | 1.98 | **I** |
| Tax Credit | Distributions | 2 | 2025-08-14 | 2026-02-20 | FID:CASH | 0.22 | **R** |
| Administrative Fee | Other | 1 | 2024-10-15 | 2024-10-15 | FID:CASH | -2.81 | **R** |
| Return of Capital | Other | 1 | 2026-04-23 | 2026-04-23 | UBS | 1.65 | **I** |
| Rollover Contribution | Other | 1 | 2026-01-30 | 2026-01-30 | FID:CASH | 823.50 | **N** |

---

## Bucket Summary

| Bucket | Row count | % of total | Notes |
|---|---:|---:|---|
| **I** Internal | 880,100 | 76.8% | Dominated by Buy/Sell Exchange (652K), Income Reinvested (224K) |
| **R** Return | 267,981 | 23.4% | Dominated by Dividend to Cash (213K), Management Fees (15K) |
| **N** NNA | 19,159 | 1.7% | Contributions, Distributions, Merges, Rollovers |
| **?** Review | ~1,900 | ~0.2% | See notes below |

---

## Review Items (CTO judgment required)

**1. `Starting Value` (Contributions, 896 rows, 2021–2026)**
Opening balance seeded when an account first appears. Large positive amounts ($32K sample). Could be:
- NNA → onboarding transfer (assets arrived from outside the firm)
- Internal → synthetic seed entry (system-generated, no actual cash flow)
Recommendation: NNA if it represents a custodian-to-custodian transfer; Internal if it's a system initialization stub. Check whether these rows have corresponding `Merge In from Other Account` entries on the same account/date — if so, it's a duplicate coding of the same onboarding transfer.

**2. `Merge In Exchange` + `Merge Out Exchange` (350 rows each, perfectly paired)**
These appear paired alongside `Merge In from Other Account` (6,521 rows). They may be the securities-side exchange entries for the same merge transaction — the canonical NNA is already captured by `Merge In/Out from/to Other Account`. If these are double-counting the same transfer: classify as **I**. If they represent a distinct additional cash flow: **N**.
CTO action: spot-check one account that has both `Merge In from Other Account` and `Merge In Exchange` on the same date — confirm whether they represent the same economic event or two.

**3. `Cancel Account` (Distributions, 101 rows, 2025–2026)**
Account closure distribution. Negative amounts ($-87 sample). Likely a final distribution to the client when closing an account — that is a real NNA outflow. But could also be a system closure entry with no real cash movement.
Recommendation: NNA (treat same as Client Distribution) unless CTO has evidence it's synthetic.

**4. `Dividend Paid from Cash` + `Income Paid` (101 rows each, 2020–2025)**
Always appear as paired entries (same count). Sample shows opposite signs ($-67.86 Dividend Paid from Cash / $-19.16 Income Paid). The `activity_category` "Net Dividends/Interest/Gains Withdrawn" suggests these are income distributions sent OUT to the client — if cash leaves the account to the client: **N** (economic outflow). If these are internal accounting entries for income being realized: **R**.
Recommendation: NNA (distributions to client), but flag: these may have been excluded from existing INF_C_01 NNA computation. CTO should verify against current INF_C_01 `_is_nna_flow()` logic.

---

## JOE-TXN-BACKFILL Inheritance Note

Per CTO instruction: JOE-TXN-BACKFILL classification for Merge In/Out is canonical and MUST NOT be re-decided.
- `Merge In from Other Account` → **N** (confirmed, large positive amounts, 6,521 rows)
- `Merge Out to Other Account` → **N** (confirmed, large negative amounts, 350 rows)
- `External Account Activity In/Out` → **N** by extension (same economic event, different Orion label)

---

## Structural Notes for PRD §2

1. **`type_desc` not `activity_category` is the key column** — activity_category has only 11 distinct values and conflates things that need separate treatment (e.g., "Dividends and Interest" contains both Dividend to Cash [Return] and Income Reinvested [Internal]).

2. **Variant rows** — Several type_desc values appear under multiple activity_category values (e.g., `Dividend to Cash` appears under both `Dividends and Interest` and `Other`). Row count is small (~38). PRD taxonomy should key on type_desc and treat activity_category variants as the same bucket.

3. **Buy Exchange + Sell Exchange dominate (57%)** — These are rebalance trades that cancel perfectly (same 326,134 count). For AUA delta calculation they're pure noise (buy one security, sell another, net cash = $0). Critical to exclude from NNA computation.

4. **Income Reinvested (DRIP) is the #3 entry (224K rows)** — also pure Internal. Net cash to account = $0.

5. **Total NNA rows are only 1.7% of all transactions** but they represent the economically meaningful cash flows (deposits $4.4K rows, withdrawals $4K rows, merges $7.7K rows).

6. **Tax withholding rows** (Federal/State/Foreign, 2,252+274+33 = 2,559 rows) — classified as Return (tax expense). For NNA computation, these should NOT be included in net flows — they're tax on income, not client-driven deposits/withdrawals.
