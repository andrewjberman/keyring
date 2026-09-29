# Bloomberg Excel holdings access: exercised result

Author: 4.0.0_SA_CRO~Z. Measured September 29, 2026, approximately 15:53-16:03 ET. RCN-0020, option 1.

## Decision-changing result

**Subsequent same-day complete date census:** see `DAILY_COVERAGE_CENSUS.md` for first available dates and fresh-versus-carried counts. This document's early dates and frequency statements are samples, superseded on coverage by that census. TSEL/PCLG have material reporting gaps; BASG's issuer archive has more complete coverage than Bloomberg.

The installed Bloomberg Excel add-in successfully serves full-sized current and historical holdings datasets for WCMG, TSEL, BASG, ETFT and PCLG under existing access. GQGU resolves to the correct name and ISIN, but its holdings queries fail. This supersedes the earlier assumption that the local raw BQL service refusal prevented using BQL at all. No purchase, permission change or credential submission was needed for Excel.

The same machine's raw `//blp/bqlsvc` request was retested after Excel succeeded and STILL returned `User not authorized to use BQL`. These are different access surfaces in the observed behavior. The experiment does not establish the internal cause or a way to enable direct BLPAPI BQL. Excel's BDS remains ordinary reference data; the working alternative is Excel's BQL implementation.

Proposed source architecture: one Bloomberg Excel automation adapter for five funds, plus GQGU's demonstrated issuer archive. Keep issuer data available to reconcile differences and cover gaps. The previous issuer-first architecture is no longer the only demonstrated route. A production collector is not installed, and a full historical coverage census remains separate work.

## Exercised recipe

An isolated, invisible Excel COM instance was created with `DispatchEx('Excel.Application')`. The first probe recognized the formulas but never completed even its IBM price control over 36 seconds. That was an invalid access test because its positive control failed.

The successful probe explicitly opened the installed `C:/blp/API/Office Tools/BloombergUI.xla`, registered `blpxladdin.xll` and `brtdwrap.xll` in that Excel instance, inserted formulas into a new workbook, pumped COM messages and recalculated. BDP and BDS controls, Excel BQL and BQL.Query all completed. Separate subsequent Excel instances reproduced the result. Each created Excel instance was closed after saving its own research workbook. No pre-existing user workbook was open or modified, and no registry/add-in installation settings were edited.

Process-lifecycle qualification: `Quit()` returned but five probe-owned, hidden Excel processes remained. They were subsequently identified from the recorded per-probe PIDs and explicitly stopped after confirming their Excel process names and empty window titles. Production automation needs reliable cleanup of its own Excel instance as well as data freshness/error checks; a successful COM query is not operational readiness.

Current full payload:

```excel
=BQL.Query("get(id()) for(holdings('WCMG US Equity'))","showallcols=true")
```

Historical full payload:

```excel
=BQL.Query("get(id()) for(holdings('WCMG US Equity',dates=2026-06-30))","showallcols=true")
```

Historical output contains ID, SOURCE, POSITION, POSITION_CHANGE, WEIGHTS, CURRENCY, REPORTED_MKT_VAL, DATES, REPORT_DATE, ORIG_IDS and POSITION_TYPE. The quantity is available as POSITION in the full payload. The attempted `id().positions` projection failed, so its failure must not be interpreted as quantity unavailability. The attempted historical `members(...,type=holdings,dates=...)` form rejected its parameters; the explicit `holdings(...,dates=...)` form above worked.

## Per-fund coverage samples

All five working funds returned portfolios for requested dates June 30 and September 23, 24, 25 and 28, 2026. This is daily sampling, not a census proving uninterrupted daily publication.

| ETF | September 28 requested-date rows | Earliest successful requested date tested | Returned report date for that early sample | Additional qualification |
|---|---:|---|---|---|
| WCMG | 49 | April 30, 2026 | April 30, 2026 | April 22 failed; May 29 also succeeded. Exact first available date unmeasured. |
| GQGU | None | None | None | Current ticker, current ISIN, members form, and July 14, 2025 / June 30, 2026 / September 25, 2026 requests failed. Name and ISIN query succeeded. |
| TSEL | 29 | January 3, 2025 | January 2, 2025 | Historical request can return a prior report. |
| BASG | 36 | June 30, 2025 | June 30, 2025 | June 16 failed; July 31 also succeeded. Issuer archive already reaches earlier. |
| ETFT | 30 | December 2, 2025 | December 2, 2025 | Launch-period sample works. |
| PCLG | 30 | October 31, 2025 | October 31, 2025 | September 30 failed; December 31 also succeeded. Exact first available date unmeasured. |

Four batches contained 58 queries including controls, syntax probes, failed dates, identity checks and repeated shapes. Thirty-three successful dated snapshots across the five target ETFs each summed to approximately 100% weight. A SPY historical positive control returned 506 rows and approximately 100% weight in the final dynamic-range read. The earlier SPY capture was truncated by the prototype's 180-row read bound; it is explicitly superseded by that full capture. No target ETF exceeded the initial bound.

## Quality boundaries that remain material

1. **Requested date differs from report date.** WCMG requested September 25 returned report date September 24; TSEL requested September 23 returned September 22. Current and historical queries also use different date-column layouts. Preserve raw columns and normalize deliberately. A successful request for each day does not prove a fresh disclosure each day.
2. **A 100% sum is not proof of issuer parity.** September 28 comparisons show complete-sized portfolios, but cash and some quantities differ. The comparison used ticker stems with a few exchange suffix conversions, not a finished identifier crosswalk.
3. **Equity checks:** PCLG's 28 matched equities had identical quantities and market values; ETFT's 28 matched equities had identical quantities and market values within issuer whole-dollar rounding. TSEL's 27 matched equities had equal quantities; its differences were cash/money-market rows. WCMG had 44 of 45 automatically matched quantities equal, with matched market values within $0.04; Kioxia quantity differed threefold despite equal market value, and two other equities needed explicit exchange/ticker mapping. A corporate-action explanation is a hypothesis, not a finding.
4. **BASG quantity discrepancy:** all 34 matched equities had quantity differences despite the same displayed report date. We have not established the reason. Latest and historical Bloomberg queries agree with one another, so choosing one of those forms does not resolve the issuer discrepancy.
5. **Cash semantics:** Bloomberg may separately show a money-market holding and USD cash, while the issuer aggregates cash. Some Bloomberg cash rows carry nonzero weight/position and zero reported market value. Do not blindly recompute weights from that value column or treat those differences as trades.

These qualifications do not erase the access result. They determine what must be reconciled before using the datasets to infer manager trades or claiming exact source equivalence.

## What happened to the Terminal/portfolio-ID investigation

No Terminal UI was running initially; ordinary DAPI was nevertheless serving prices. A Terminal launch reached its login form. No credentials were entered, no login was submitted, and the login window opened by this investigation was closed afterward. Once Excel produced actual holdings, the custom-portfolio-ID detour was no longer necessary to demonstrate a route. PRTU identifiers and Terminal exports remain untested; there is no claim they fail.

## Review artifacts and remaining support question

Review workbook: `C:/Users/Opal Bloomberg/Downloads/AMGT_RECONN_Bloomberg_Access_20260929.xlsx`. Eleven sheets contain a readme, five September 28 snapshots and five early samples, saved as static evidence rather than live formulas. The readme flags GQGU and date/source differences.

Reusable probe: `scripts/bbg_excel_holdings_probe.py`, accompanied by `scripts/bbg_excel_probe_queries.json`. Requires local Excel, Bloomberg Office Tools, pywin32 and existing Bloomberg access. This preserves the exercised research mechanism, not an unattended operational service. Its evidence defaults to `.runtime/amgt-reconn-bbg-excel-probes/` (overridable with `--output`); never configure production schedules to run it without a separate implementation review. The durable copy adds output-path arguments to the exercised scratch script; that small wrapper change was syntax-checked, not separately rerun against Bloomberg.

Local raw evidence is under `.runtime/amgt-reconn-bbg-access-20260929/`, including the two initialization probes, four query manifests/results/workbooks, `probe_summary.json`, `issuer_comparison.json` and `raw_bql_recheck.txt`. Raw Bloomberg responses and workbooks are not committed.

Prepared, NOT SENT, support question:

> Excel BQL.Query returns holdings for WCMG, TSEL, BASG, ETFT and PCLG on this installation, while the same query through the local //blp/bqlsvc service returns "User not authorized to use BQL." GQGU US Equity resolves correctly to GQG US Equity ETF / US00775Y2569, but current and dated holdings queries return no results. Please confirm (1) GQGU holdings coverage or the correct identifier; (2) the source, reporting cadence, earliest available report dates and fill behavior for these six ETFs; (3) cash/quantity conventions, including differing BASG quantities versus the issuer for September 28; and (4) whether direct BLPAPI BQL can be enabled for this login and whether any additional licensing is required. We are not requesting a purchase or account change.
