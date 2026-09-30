# Daily holdings coverage: complete date census

Author: 4.0.0_SA_CRO~Z. Measured September 29, 2026, approximately 16:39-16:48 ET. RCN-0020.

## Answer

From the source start dates below through September 28, 2026, ETFT through Bloomberg and GQGU/BASG through their issuer archives have a report dated every trading day tested. WCMG, TSEL and PCLG through Bloomberg have mostly daily reports with gaps. Bloomberg returns a result on every requested trading day after first availability, but fills those gaps with an older portfolio. Therefore request success is not fresh daily disclosure.

| Fund | Source | First available date in this census | Trading dates from that date through September 28 | Reports dated the requested day | Older reports carried forward | Maximum lag in trading days |
|---|---|---|---:|---:|---:|---:|
| WCMG | Bloomberg Excel BQL | April 23, 2026 | 109 | 91 | 18 | 2 |
| TSEL | Bloomberg Excel BQL | December 31, 2024 | 436 | 394 | 42 | 37 |
| BASG | Bloomberg Excel BQL | June 23, 2025 | 319 | 315 | 4 | 1 |
| ETFT | Bloomberg Excel BQL | December 2, 2025 | 206 | 206 | 0 | 0 |
| PCLG | Bloomberg Excel BQL | October 16, 2025 | 238 | 225 | 13 | 12 |
| GQGU | Issuer FilePoint archive | July 14, 2025 (ETF operations start) | 305 | 305 | 0 | 0 |
| BASG | Issuer FilePoint archive | June 13, 2025 (inception) | 324 | 324 | 0 | 0 |

All five Bloomberg funds have zero missing responses within the span from their first available date, but 77 of the 1,308 successful fund/date responses contain prior report dates. GQGU has no Bloomberg holdings in this scan. The issuer routes provide earlier and more complete date coverage for BASG and an entirely working route for GQGU. The separate July 11, 2025 GQGU transition snapshot found earlier is not counted as ETF operating history here.

The first Bloomberg dates above are the first successful dates in the full scan, not the earliest samples from the prior report. They need not equal legal inception dates. For example PCLG launched September 30, 2025 but Bloomberg first returned holdings on October 16; WCMG first returned holdings April 23. No claim of pre-launch or predecessor-fund history is made.

## Material gaps

- **TSEL:** the August 15, 2025 portfolio repeats for requested dates August 18 through October 8: 37 consecutive trading dates without a new reported snapshot. The next fresh report is October 9. Five other isolated carried dates account for the remaining difference between 436 requests and 394 reports.
- **PCLG:** the March 12, 2026 portfolio repeats for requested dates March 13 through March 30: 12 trading dates. A fresh report resumes March 31. July 14 also carries July 13.
- **WCMG:** 18 carried dates, each one or two trading days old. Many later Friday requests carry Thursday's report. This is a demonstrated reporting pattern, not evidence of why the source omits those dates.
- **BASG Bloomberg:** June 3, June 11, June 15 and September 22, 2026 carry the prior trading date. Its issuer archive returned files with matching internal dates for all 324 requested dates from inception.

Standalone single-fund queries independently confirmed the TSEL and PCLG long gaps. Their repeated security/quantity/weight/market-value payloads were identical across the checked gap dates after excluding the requested-date column. Fresh reports after each gap changed the portfolio payload. Thus these are not merely mislabelled dates on newly populated portfolios.

## Scope and method

Bloomberg: 436 NYSE trading dates, December 31, 2024 through September 28, 2026, queried through the installed Excel BQL interface, each requesting all six funds. Returned rows retain ORIG_IDS to distinguish funds. The first multi-fund control returned exactly the combined WCMG/TSEL row counts and separate approximately 100% weight totals. An early-date control returned TSEL while omitting not-yet-launched WCMG, showing that unavailable funds do not prevent others from returning.

```excel
=BQL.Query("get(id()) for(holdings(['WCMG US Equity','GQGU US Equity','TSEL US Equity','BASG US Equity','ETFT US Equity','PCLG US Equity'],dates=2026-09-28))","showallcols=true")
```

The `dates=range(...)` form was rejected for each of the five working funds. The census consequently made one dated request per trading day. It validated requested DATES against each response and separately counted REPORT_DATE. No mixed/future report dates occurred. Every successful target fund/date portfolio summed to approximately 100%; maximum floating-point deviation was below 0.000000000001 percentage points. This is coverage/completeness screening, not issuer reconciliation or a guarantee about corporate-action adjustments.

The calendar is the repository's `lib/trading_calendar.py`, using its explicit 2024-2027 NYSE holiday fallback because pandas_market_calendars is not installed. It includes the January 9, 2025 closure. Weekends and exchange holidays are excluded. September 29 is excluded because it was the current day; a future scheduled collection is not proven by this historical census.

Issuer: every NYSE date from July 14, 2025 for GQGU and June 13, 2025 for BASG was requested from the already-proven dated FilePoint pattern. HTTP success alone did not count: each payload had fund-filtered rows and an internal date exactly matching the requested date. All 629 dates passed. Four GQGU connection resets passed on individual retries and are preserved in the attempt records. GQGU row counts range 30-46; BASG 33-38. Net-asset weights total 99.95-100.05% and 99.95-100.04%, respectively, consistent with source rounding.

## Consequence

Use issuer archives for BASG/GQGU and Bloomberg for ETFT to obtain complete daily date coverage over the tested spans. WCMG/TSEL/PCLG can be backfilled through Bloomberg at their observed frequency, with explicit source report dates and stale-day flags. Do not invent daily manager activity inside the gaps. Whether a separate issuer archive can fill those three funds' remaining gaps has not been established. This does not reopen Andrew's already-approved acceptance of less frequent history.

Cash, identifiers and quantity discrepancies documented in `BBG_EXCEL_ACCESS_VERIFIED.md` remain separate quality qualifications. This census establishes dates and returned portfolios, not full source equivalence or a production collector.

## Evidence and review

Review workbook: `C:/Users/Opal Bloomberg/Downloads/AMGT_RECONN_Daily_Coverage_20260929.xlsx`, seven sheets with summary and per-fund requested/report dates. Raw daily Bloomberg responses, 629 issuer files, request statuses and attempt records remain local in `.runtime/amgt-reconn-daily-census-20260929/`; detailed metadata is `coverage_summary.json` and `coverage_by_fund_date_all_sources.csv`. Earlier sample workbooks remain unchanged.

Reproduction scripts are preserved under `scripts/`: `bbg_daily_coverage_census.py`, `gqgu_daily_coverage_census.py`, `basg_daily_coverage_census.py`. Run from the workspace root. They are fixed-window research probes; they write only local evidence and do not install schedules. Bloomberg's first census attempt met an Excel busy rejection; the exercised version retries transient COM busy errors and then completed all 436 dates. Probe-owned leftover Excel processes were cleaned up by recorded PID after their jobs ended. No support correspondence, account changes, purchases, production deployments or schedules occurred.
