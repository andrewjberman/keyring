# Price coverage for the Analysis Request report -- the estate's stores and the one YCharts data call (2026-10-14 ~16:3xZ)

**Author:** `4.0.0_SA_CRO~DELL2`, on Andrew's "Yes do it" (record @98eacceda3). This was a read-only read: **no YCharts call was made**
(reason below), with no writes, no Bloomberg and no yfinance. Working files are in the session scratchpad (`coverage/symbols.json`,
`coverage.json`) and are not persisted. Trading-day frontier: 2026-10-13 (T-1).

## The symbol set the report needs (15 tickers, 5 model series, 1 risk-free series)

- **Opal ETFs:** DIVZ, IDVZ, PFDE, PFOE.
- **Comparison catalogue:** five Opal model series, UST, ST, INT, LT and ULT. These are model portfolios, not tickers
  (`ycharts/generate/templates.json` `comparison_catalog.entries`).
- **Benchmark:** ^SPXTR, the only benchmark the Overview map uses (r29 `ycharts/research/overview_map.json`, `benchmark_level_series`).
- **Risk-free:** FRED 3-month Treasury, `s3://opal-data-portal-v2/json/macro/yield_curve_fred.json` (`layout_overview.py:66`).
- **One real 49financial holdings file:** DGRO, IEFA, IEMG, IJH, QUAL, SPHY, SPYM, VEA, VGSH, VTV. This is the 2026-10-09 partner upload,
  normalized portfolio `ART-ea14188f...`. The 10-11 and 10-14 files are test files.

## Where prices exist

| Store | Location | What it holds |
|---|---|---|
| MDPF_SECHIST series (the PRD's "first" store) | `s3://opal-data-assets/mdpf/global/silver/security_series/` | **0 objects.** Its writer ships switched off; its header says the price store "stays the only live writer" |
| MDPF_DEMQUE price store | `s3://opal-data-assets/yahoo/global/silver/price_history/` | 483 securities keyed by Commonwealth CUSIP, Yahoo-sourced, with price, dividend and split files |
| Opal ETFs, Bloomberg | `opal-data-etfs/bbg-testpull/tickers/<T>/history.csv` + `bbg/<date>/history_topup` | history plus daily top-ups carrying total return; 37 top-ups after 08-20 = 37 trading days |
| Opal model series | `opal-data-portal-v2/json/benchmarks/model_portfolio_timeseries.json` | UST/ST/INT/LT/ULT, daily, 2024-04-30 to 10-13 |
| Risk-free | the FRED file above | 497 points, 2024-10-15 to 10-09 |

## Coverage

| Symbols | Held | Depth / freshness |
|---|---|---|
| DIVZ, IDVZ, PFDE, PFOE | yes (Bloomberg) | from inception to 10-13, total return |
| UST, ST, INT, LT, ULT | yes | 2024-04-30 to 10-13 |
| 3M Treasury | yes | 2 years, to 10-09 |
| VEA, VTV | yes (price store) | 2013 to 10-13, dividends file |
| IEFA, IEMG, IJH, QUAL | thin (price store) | 2026-04-14 to 10-09: about 6 months, two trading days short |
| **^SPXTR** (benchmark; beta and alpha need it, `layout_overview.py:228`) | **absent** | -- |
| **DGRO, SPHY, SPYM, VGSH** | **absent** | -- |

**Totals:**
- 10 of 15 tickers are held.
- 6 of those are current and deep (the 4 Opal ETFs, VEA and VTV).
- 4 are thin (IEFA, IEMG, IJH, QUAL).
- 5 are absent (^SPXTR and 4 holdings).
- The 5 model series and the risk-free series are held.

## The "single YCharts data call" does not exist today

- The gateway's YCharts tools (`infra/aws/ec2/opal-gateway/app/integrations/ycharts/client.py`) are **not a keyed data API**. They replay
  a shared signed-in session cookie (secret `ycharts/credentials`, last changed 2026-07-01) against ycharts.com's internal web endpoints.
- The time-series tool takes **one symbol per call** (`general_data`, ~`:133`), so it cannot batch.
- **No official YCharts API key exists:** there is no `ycharts/api/key` secret. The official API is still an open recommendation, with its
  terms-of-service exposure flagged (`docs/architecture/YALP_MDSRC.md` sections 6.3 and 7).
- Using the shared session from another seat could also sign the report machine's own YCharts session out.

## What this changes for IRPT_ANLREQ C-PRICES (v0.9+)

1. **"MDPF_SECHIST first" has nothing to read yet.** The live per-security writer is MDPF_DEMQUE's Yahoo price store, and the Opal ETFs'
   prices are in the Bloomberg pull. Both are dell1 (MDPF) stores.
2. **The one YCharts data call needs a precondition** before it exists:
   - (a) the official YCharts API procured and keyed; or
   - (b) the session-cookie path accepted as "the data call", with its terms-of-service and session-collision risk.

   Until then, the next step in the PRD order is yfinance, labelled UNVERIFIED.
3. **The benchmark ^SPXTR is held nowhere.** Without it, the Overview's beta and alpha cannot be computed whatever the holdings coverage.

## Not read

- The contents of the price store's price and dividend files (index rows only).
- Whether every Bloomberg top-up carries all four Opal ETFs.
- yfinance coverage.
- Any other firm's Black Diamond price store (avoided for the cross-firm rule).
- Whether `ycharts/credentials` still signs in.

-- 4.0.0_SA_CRO~DELL2
