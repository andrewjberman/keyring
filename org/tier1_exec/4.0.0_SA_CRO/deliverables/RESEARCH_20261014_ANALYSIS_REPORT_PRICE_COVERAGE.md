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

## Addendum ~17:3xZ -- yfinance probe, on Andrew's ~17:3xZ word (record ANDREW_DIRECT_20261014_173xZ_YFINANCE_FOR_GAPS_ELSE_YCHARTS_TRUST_TOKEN.md)

Probe run from dell2 at 17:38:44Z: yfinance 1.7.0, `yf.download(..., period="max", auto_adjust=False, actions=True)`, read-only. Script
and JSON are in the session scratchpad (`coverage/yf_probe.py`, `yf_probe.json`).

**yfinance covers every gap**, with full history, an adjusted close and dividend events:

| Symbol | First | Rows | Dividend events |
|---|---|---|---|
| ^SP500TR (S&P 500 Total Return; `^SPXTR` is not a Yahoo symbol and returns nothing) | 1988-01-04 | 9,769 | -- (total-return index) |
| DGRO | 2014-06-12 | 3,104 | 49 |
| SPHY | 2012-06-19 | 3,601 | 172 |
| SPYM | 2005-11-15 | 5,260 | 84 |
| VGSH | 2009-11-23 | 4,248 | 201 |
| IEFA | 2012-10-24 | 3,512 | 29 |
| IEMG | 2012-10-24 | 3,512 | 29 |
| IJH | 2000-05-26 | 6,635 | 108 |
| QUAL | 2013-07-18 | 3,331 | 52 |

The Opal ETFs, VEA and VTV also returned full history (DIVZ from 2021-01-28, PFDE and PFOE from 2025-12-31).

**Round trip:**
- **One batched call:** 16 symbols at maximum history took 2.21 s.
- **One symbol:** one year of daily history took 0.13 s.

**Two caveats:**
- **Today's row:** the last row is today's (2026-10-14), an intraday value while the market is open. A producer must cut at the
  trading-day frontier, T-1 by `lib/trading_calendar.py`.
- **Label:** ruling 7546 keeps yfinance labelled UNVERIFIED.

Not attempted: the YCharts trust-token path. Andrew's word makes it the fallback "if it does not work", and yfinance works.

## Addendum ~17:4xZ -- the YCharts trust-token fallback, probed on Andrew's ~17:4xZ ask ("try the ycharts trust token as a fallback, i want to see if it works and the turnaround")

The probe ran from dell2 at 17:47:08Z, through the deployed `ycharts-market-data-pull` Lambda's own client (`ycharts_client.py`,
downloaded from the live function, LastModified 2026-05-22), called locally. That client reads stored session cookies and makes plain
HTTPS GETs to YCharts' internal chart endpoints. No browser was used and nothing was written. Script and JSON are in the session
scratchpad (`coverage/yc_probe.py`, `yc_probe.json`).

**Result:**

| Secret | Result |
|---|---|
| `ycharts/session/current` (written by `ycharts-session-capture`, last changed 2026-10-05) | not usable by this client: its `cookies` field is a list, the client expects a string (`AttributeError`). Its capture and probe schedules are both DISABLED |
| `ycharts/credentials` (session cookies, last changed 2026-07-01) | **WORKS**: freshness GET `/indices/table_data` 200 in 0.47 s |

| Call (`GET /charts/fund_data.json`, zoom=max) | HTTP | Round trip | Bytes | Daily points |
|---|---|---|---|---|
| DGRO price | 200 | 0.23 s | 35,349 | 1,256 (2021-10-13 to 2026-10-14) |
| ^SPXTR level | 200 | 0.10 s | 38,585 | 1,256 (2021-10-13 to 2026-10-14) |

**Throughput and timeline:**
- **One symbol per call.** Each call takes 0.1 to 0.5 s.
- **Spacing:** the client's measured safe spacing is 2 s between calls (`REQUEST_SPACING_S`).
- **A request needing N missing symbols takes about 2.3 x N seconds:** about 35 s for the 15 report tickers, about 21 s for the 9 gaps.
- **Not a single batched call:** `fund_data` takes one security, so it is N calls.
- **Depth:** zoom=max returned 5 years, not full history (1,256 points). The last point is today (intraday), so cut at T-1.

**Risks:**
- These are YCharts' internal web endpoints on a shared signed-in session. The client's own header records the ToS framing and a 403
  "concurrent sign in" eviction mode.
- The session in `ycharts/credentials` is three months old and nothing refreshes it automatically (the capture schedule is disabled).
- Whether this call disturbs the resident's YCharts browser session was not measured.

**Comparison with yfinance:** yfinance gave full history (^SP500TR from 1988) for 16 symbols in ONE 2.21 s batched call. YCharts gives
5 years per symbol, one symbol per call, about 2.3 s each.
