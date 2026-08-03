# ETFS July 2026 — FINAL deliverables

**Prepared 2026-08-03 by `1.0.0_SA_CTO`** (Andrew-direct ask: brief on the inflection/Orion
conclusion; confirm full July for 49F/Cottonwood/Inflection; spreadsheets + presentation).

| file | what |
|---|---|
| `OPAL_ETFS_July2026_Final.xlsx` | THE WORKBOOK. Summary (all bases + Orion delta), per-partner daily sheets (22 trading days each, from the corrected store), inflection true-settled sheet, delivered-vs-current delta sheet. Formulas live; recalculated in Excel, 0 errors; totals cross-checked against the memorialized figures @5f27b84c0f. |
| `OPAL_ETFS_July2026_Briefing.pptx` | THE PRESENTATION. 6 slides: headline numbers · coverage verdict · Orion label finding (+$424,062.91 / 0.891%) · the two-date-bases defect · the three open decisions. Validated + visually QA'd. |
| `opaletfs_{partner}_202607_CORRECTED_trading_days.csv` | Corrected per-partner July series (22 NYSE trading days, current daily store as of 2026-08-03). **These are the authoritative July dailies.** |
| `opaletfs_{partner}_202607_AS_DELIVERED_20260801.csv` | The exact CSVs the Aug-1 month-end email carried (calendar-31-day, carry-forward). KEPT FOR THE RECORD — inflection is stale on 7 weekdays (backfill landed 4h after the fire) and cottonwood on 2 days (pre-repoint 07-20; carried 07-31). 49financial was exact. |

**Basis caveat (binding until resolved):** all monthly averages assume a simple mean over
trading-day observations. The production ETFS_AVGCAP aggregation formula is UNCONFIRMED —
confirm it before any dollar figure reaches a partner. No partner restatement has occurred.

Source data: `s3://opal-data-etfs/daily/{partner}/2026-07-*.json` (+ inflection true-settled
series from `../ETFS_ORION_LABEL_CORRECTION/` @5f27b84c0f). Analysis + generators archived in
the session scratchpad; figures independently cross-checked in this session.
