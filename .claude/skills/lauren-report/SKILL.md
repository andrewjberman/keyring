---
name: lauren-report
description: Generate an Opal Capital quarterly EARNINGS UPDATE in Lauren Harmon's format (her ASML / UNH 2Q26 and 3Q26 updates) as a Word .docx with native Word charts -- `/lauren-report {ticker} [{quarter}]`. Rolls the company's Financial Summary and appendix charts forward one quarter from its chartbook, fills the new quarter from the company's release and filings, pulls Opal's prior view and consensus from the Opal data harvest through the opalgateway MCP (web search, SEC EDGAR / company IR first, when the gateway or the data is unavailable), writes the sections in her voice, and leaves AlphaSense-only charts as labelled placeholders. Use on "/lauren-report", "earnings update for X", "Lauren's format".
---

# /lauren-report -- quarterly earnings update (Lauren Harmon's format)

**Input:** a ticker or company, optionally the quarter (default: the latest reported quarter). **Output:**
`<TICKER> earnings update <nQyy>.docx` (plus the updated chartbook and the report JSON) in her linked folder.

Format and voice: `references/example_asml_2q26.json` + `references/report_spec.md`. Sources and the fallback rule:
`references/data_sources.md`. Read them before the first report of a session.

## How her reports work (keep this model)
- The format is fixed; what varies per company is the KPI wording and the **chart set**. Charts stay the same
  quarter to quarter: each report adds one quarter to each chart. She drops a chart when its data stops (ASML's
  bookings charts went in 3Q26 when ASML stopped quarterly bookings disclosure).
- So every company has a **chartbook**: `<TICKER>_chartbook.json`, kept beside her reports. It is the memory of the
  chart set and all series history:
  ```json
  {"ticker": "ASML", "quarter_labels": "Mon-yy",
   "figures": [{"id": "sales_growth", "title": "local currency sales growth (% year-over-year)", "type": "bar",
                "format": "0", "window": 17, "source": "release: total net sales; derived y/y",
                "series": [{"name": "sales growth", "data": {"2022Q2": 35, "2022Q3": 10}}]},
               {"id": "net_bookings", "retired": "3Q26: company stopped quarterly bookings disclosure", ...}],
   "summary_rows": {"Revenue": {"2024Q1": "5,290"}}}
  ```
  `source` says where each series comes from (`release`, `10-Q`, `IR presentation`, `alphasense`, `derived`).
- **First report for a ticker with no chartbook:** ask her once for the chart workbook behind her last report (her
  "2Q build") and seed the chartbook from it; if she has none, seed from the company's historical quarterly data
  (IR historical workbook, XBRL) and leave AlphaSense-only series as `pending`. Say which figures were seeded from what.

## Steps
1. **Resolve** -- `harvest_resolve_security(query)`; `exact` -> harvest available. Otherwise (or gateway down) use
   the web for every harvest item and say so in one line.
2. **Prior view (parallel)** -- `harvest_get_research` (prior reports, fund of record, last stated position,
   positives/negatives), `harvest_get_fundamentals` `consensus` and `model` (with `mnemonics`) and `price`,
   `harvest_search_articles`. Load the chartbook and her previous report's JSON if present (carry "Why we own").
3. **The new quarter** -- from the release / 10-Q / 6-K / IR presentation (data_sources.md section 2): every
   Financial Summary line for the quarter, every chartbook series for the quarter, guidance (updated vs prior,
   next-quarter guide), the geographic and segment splits, the stock reaction, broker rating and target changes.
4. **Roll forward** -- append the quarter to the chartbook (never overwrite history silently; a restated past value
   is changed with a `restated` note), recompute derived series (y/y growth, margins, mix), drop the oldest Summary
   column, set the header block (date of pricing = T-1 close, market cap, EV, balance sheet from the latest filing).
   Retire a figure only when its data has stopped, and say so.
5. **Write** -- in her voice (see the example): Recommendation verdict first; Positives / Negatives each one dense
   paragraph of specifics (beat/miss vs guidance and consensus, the numbers, management quotes in quotation marks);
   Geographic and Segment highlights as one paragraph each; 3-5 "Topic - text" risks; Guidance with UPDATED /
   INCREASE in caps where she uses them; brokers by name with rating and target (from -> to).
6. **Render** -- write the report JSON, then `python scripts/build_report.py <report.json> "<output folder>"` (Python
   3.8+, standard library only). It prints `OK: <path> (<n> native charts)`; fix and re-run on `ERROR`.
7. **Deliver** -- save the .docx, the updated chartbook and the JSON to her linked folder (ask once if unknown; use
   the Microsoft / OneDrive connector if that is how the folder is linked). Reply with the path and three lines:
   data sources used (harvest / web), figures still pending (and what each needs), anything restated.

## Rules
- Never invent a number, a quote, a broker action or a chart point. Missing data is a gap (`null`) or a pending
  figure that names what is needed.
- Every figure in the text ties to the Summary or a chart; growth and margins are computed from the same inputs.
- Her structure and section names are fixed; do not add sections. Content changes go in the JSON, never the builder.
- An AlphaSense enrichment step (`/alphasense-enrich`) can later fill pending figures once the AlphaSense MCP is
  connected; keep pending notes specific enough for it (series, unit, quarters).
