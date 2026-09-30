# RCN-0019: Portal total-return correctness and provenance

**The Portal uses income-inclusive return data. Joe's 1.68% YTD number reproduces correctly. However, Positioning has a confirmed date-boundary defect in WTD, MTD and QTD, so the two surfaces cannot receive an unqualified all-correct verdict.**

Produced by `4.0.0_SA_CRO~I` for Andrew on 2026-09-28. Scope follows [Andrew's original instruction and clarification](ANDREW_DIRECT_20260928_INFLECTION_PERFORMANCE_INVESTIGATION.md): verify the Portal's performance numbers and preserve proof of total-return provenance. Yield quotations and investment rationale are outside this final assessment.

**What passed.** Both production generators compound daily `return`, not the ETF `price_return` field. The Bloomberg source mapping explicitly selects `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS`. Independent calculations reproduced:

- **300/300 Benchmark return cells:** five models x three series (model, index benchmark, ETF benchmark) x ten periods x two dates.
- **160/160 Positioning YTD cells:** 80 holding rows across five models on each date. Repeated tickers across models count as separate displayed rows.
- Positioning's 1D, trailing 1M, trailing 1Q and 1Y calculations also matched their specified windows, including correctly blank 1Y values for recently launched funds.

| Ultra Short-Term Benchmark YTD | Source calculation | Published Gross |
|---|---:|---:|
| Through September 21; published September 22, the date of Joe's original question | 1.684119973% | **1.68%** |
| Through September 25; latest snapshot inspected September 28 | 1.510850123% | **1.51%** |

Gross is the frontend default. Its Net toggle subtracts the prorated annual 36-basis-point charge from model returns; it does not exclude income. The corresponding YTD Net calculations are 1.41% and 1.24%. These are model performance figures, not a claim about an individual client's realized return.

**Confirmed Portal defect: Positioning drops the first day of to-date periods.** The deployed `calculate_etf_period_returns` establishes Monday, the first of the month, the first of the quarter, and January 1 as period starts, then filters with `date > start_date`. Daily returns describe the change from the preceding close. To include the first day's return, those to-date windows require `date >= start_date`. Benchmark already uses the inclusive boundary.

| Positioning metric, through September 25 | Published | Correct inclusive total return |
|---|---:|---:|
| VGSH WTD | -0.07% | **-0.02%** |
| VGSH MTD | -0.43% | **-0.52%** |
| VCSH MTD | -0.87% | **-1.06%** |
| VCSH QTD | -0.88% | **-0.95%** |

The latest snapshot has **224 affected cells**: 72 WTD, 78 MTD and 74 QTD out of 80 holding rows per period. The September 21 snapshot has 231 affected cells: 80 WTD, 78 MTD and 73 QTD. September 21 was a Monday; all WTD cells were blank even though that day's returns existed. Counts are differences at the displayed two-decimal precision, including incorrect blanks.

The same faulty boundary applies to YTD, but **it does not change the 2026 YTD values** because January 1 has no trading return in these ETF inputs. This is not evidence that income was omitted from the YTD number. It is evidence that income-inclusive inputs can still produce incorrectly labeled period results when the dates are wrong.

The proposed fix is narrow: use an inclusive start for WTD/MTD/QTD/YTD; preserve exclusive starts for trailing windows. Verification should exercise a Monday, a month/quarter whose first day is a trading day, and a year with a trading January 1 in synthetic boundary data. Then regenerate the artifact and verify the authenticated screen. This investigation made no production change and dispatched no implementation order.

**Direct provenance of income inclusion.** The lineage is:

`Bloomberg gross-dividend daily total-return field -> dated source PKL -> identical S3 PKL -> deployed Lambda compounding -> versioned JSON -> Portal frontend field binding`.

1. Inspected the actual OneDrive source notebooks and the repository notebooks named by the scheduled runner. `market_indices_data_pull.ipynb`, cell 10, maps `return` to `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS`; cells 13 and 16 download and save it as `return_daily`. `model_portfolio_regression_analysis.ipynb`, cell 3, makes the same mapping for ETFs; cells 10, 12 and 35 download and save `etf_returns`. Cells use zero-based indices. Relevant field mappings and download functions agree between the two homes. The repo model notebook also has a separate split-lot handling change; no equivalence of entire notebook files is asserted.
2. Read the OneDrive output files for September 21 and September 25. **All four files are byte-identical, by SHA-256, to the dated S3 inputs** retrieved for this audit. Thus the provenance does not stop at a similarly named source file.
3. Downloaded the live Benchmark and Positioning Lambda packages. Both handler files are byte-identical to the inspected repository handlers. Benchmark compounds `data.pkl -> return_daily -> return`; Positioning compounds `model.pkl -> etf_returns -> return`.
4. Read the live CloudFront configuration and its pinned `public-data-router:7` code. `/api/general/benchmarks/model_portfolio_benchmarks.json` and `/api/general/positioning/positioning_data.json` route to the two audited keys under `opal-data-portal-v2/json/`.
5. Inspected the publicly served frontend bundles. They fetch those endpoints and select the audited `returns` fields. Positioning does not calculate a replacement return in the browser.

**Numerical evidence distinguishes total return from price-only return.** Through September 25, the same ETF source files give:

| Holding | Income-inclusive YTD, displayed in Positioning | Price-only YTD, independently compounded |
|---|---:|---:|
| VGSH | +0.50% | -1.94% |
| VCSH | approximately 0.00% | -2.92% |
| TBIL | +2.63% | +0.20% |

There is separate corroboration for the Ultra Short-Term custom Bloomberg index used by Benchmark. On September 1 its daily return is **-0.0758%**. Reconstructing the model's same-day weighted ETF total returns gives **-0.075630%**; using those weights with ETF price-only returns gives **-0.299209%**. The approximately 0.224-percentage-point income-related difference is preserved in the index. April 1 and July 1 show the same distinction. Across 2026 through September 25, index daily returns correlate **0.9999954** with the independent holdings total-return reconstruction. This corroborates inclusion of income, rather than relying only on a field label.

**Limits that remain material to a full certification.** The separate model-holdings reconstruction gives +1.534495869% YTD through September 25, while Benchmark's custom-index source gives +1.510850123%: **2.36 basis points difference**. The September 21 difference is 2.31 basis points. This is between two upstream representations, not between Portal arithmetic and its selected input. Its cause has not been established. The custom Bloomberg index's complete construction configuration was not retrieved.

The market-index downloader also substitutes `price_return` if the Bloomberg total-return observation is missing, without retaining a fallback flag. A price change of a total-return index can legitimately contain income, but the generic fallback prevents a universal guarantee from the output schema alone. None of the tested Benchmark windows contains a missing final `return`; that does not identify whether a fallback was used upstream. For ETF Positioning, the inspected download function preserves the requested total-return field without this substitution. Missing ETF observations in the audit were confined to inception-limited 1Y windows already displayed as blank.

An authenticated browser was unavailable. Anonymous API requests return 401, as expected. The evidence covers live deployment bytes, origin payloads and frontend bindings; it does not certify Joe's particular session, selected toggle, cache state, or a screenshot of his screen. No independent issuer-by-issuer distribution audit was performed.

**Verification disposition.** Mechanical: PASS for origin routing, deployed code equality and source-to-output arithmetic; authenticated rendering unverified. Declarative: FAIL for Positioning's WTD/MTD/QTD labels against their actual date windows. Semantic: income inclusion is supported by source-field provenance and numerical discrimination from price-only returns, while a blanket all-period correctness certification is withheld because of the confirmed boundary defect and the named upstream reconciliation limit. Applied the [verify skill](C:/Users/AndrewBerman/.codex/skills/verify/SKILL.md); exact-seat startup and inbox acknowledgment followed [load](C:/Users/AndrewBerman/.codex/skills/load/SKILL.md).

**Reproducible evidence.** [reconciliation.json](inflection-performance-audit-20260928/reconciliation.json) contains every YTD comparison, model cross-check and input/deployed-source SHA-256. [period_audit.json](inflection-performance-audit-20260928/period_audit.json) contains all 300 Benchmark and 1,280 Positioning checks, with published and independently calculated values, dates, windows and missing-observation counts. [source_provenance.json](inflection-performance-audit-20260928/source_provenance.json) records notebook and code-cell hashes, the four source-to-S3 identity checks, and the income examples. The two scripts run offline against trusted local snapshots:

```powershell
python org/tier1_exec/4.0.0_SA_CRO/deliverables/inflection-performance-audit-20260928/reconcile.py tmp/cro-i-performance-audit-20260928 tmp/cro-i-performance-audit-20260928/recheck.json
python org/tier1_exec/4.0.0_SA_CRO/deliverables/inflection-performance-audit-20260928/audit_periods.py tmp/cro-i-performance-audit-20260928 tmp/cro-i-performance-audit-20260928/period_recheck.json
```

Raw inputs remain in `tmp/cro-i-performance-audit-20260928`. The private lossless email relay remains in `tmp/cro-i-relay/20260928_dashboard_performance_numbers/EMAILS_VERBATIM.md`; neither raw correspondence nor temporary signed download URLs are committed.

| S3 key in `opal-data-portal-v2` | Historical object version | Latest inspected object version |
|---|---|---|
| `json/benchmarks/model_portfolio_benchmarks.json` | `OpmZma3_I9jmxnfZDx9RTpilTrs4rzbq` | `Pxy6ATX1Eah8up3d9.iauhexhaxPMkxX` |
| `json/positioning/positioning_data.json` | `ZhAnRphqvDgpgIqamnzUp1eHHUKjRhY9` | `Do5scz0LyN5yNJdT.HkV335HP263mfJn` |
| `benchmarks/data_20260921_v1.pkl` / `benchmarks/data_20260925_v1.pkl` | `fOC7um3j.YzUVnI7kZ72Mfvp0zl3WnRW` | `H7ZfeDOVxcNmnSzIWI_QqN55gQIDzfa7` |
| `benchmarks/model_20260921_v1.pkl` / `benchmarks/model_20260925_v1.pkl` | `wR9H8h5_qZ42PonKae.211omAzjM.NI1` | `7g8i_WYpykY7zpDWFpa8sH6ndmWwqkUe` |

Historical JSON publication: September 22, data through September 21. Latest JSON publication: September 26, data through September 25. Live distribution: `EVTSA9VEHNZVH`, aliases `opalinvest.dev` and `www.opalinvest.dev`, ETag `E1Q54J6FUFHNRP`. Served chunks: `index-BSJ0dYHG.js`, `ModelPortfolios-DKBKUb7w.js`, `index-C5iNecJJ.js`.

Source anchors: `portal/src/api/portal-proxy.ts:829,1177`; `portal/src/pages/ModelPortfolios.tsx:543,993,2360`; `portal/src/components/BenchmarkHeatmap.tsx:87,104`; `portal/src/pages/Positioning/tabs/HoldingsTab.tsx:1165`; `infra/aws/lambda/v2_portal/yang_pipeline/portfolios/yang-model-portfolio-benchmarks/lambda_function.py:411,484,518,558`; `infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py:1987,2042,2052,2737`. Notebook root: `integrations/bloomberg/pipeline/tplus1/src/`; source-copy locations are recorded in the provenance JSON.

Workspace HEAD measured during review: `b8d2fc63ff198cf6417d867d70fab5dbc656af78`; Portal HEAD: `2febba0bd343905877ac3c01247bc6279ac36c6e`. Other seats' changes were left intact. **Push state: LOCAL.** Origin CLOUD measured by `git ls-remote` at 22:38Z: `fd045338c40d3d3785d6e5c9c90e64da2024a276`. This is an investigation report, not a production fix or deployment.
