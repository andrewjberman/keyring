# ADDENDUM -- can the in-house Analysis report run on yfinance for now? (probe result)

- **Author:** `4.0.0_SA_CRO` (base), 2026-10-05 ~20:1xZ (4:1x PM Eastern).
- **Order:** Andrew-direct 2026-10-05 ~19:5xZ, verbatim in
  `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261005_195xZ_YCDGEN_FIVE_RECS_APPROVED_EXPLORE_YFINANCE.md`
  ("all recs approved, but were out of quota for today on bloomberg + we cant get BQL, so id like to explore if this
  can be done via yfinance for now").
- **Parent:** `docs/briefs/irpt-ycharts-inhouse-generation-feasibility-20261005.md` (gap numbers G1-G11 are its).
- **Consumer:** Andrew; `1.0.0_SA_CTO` for the IRPT_YCDGEN endpoint revision.
- Every figure below is MEASURED by this seat today unless marked. No ticker, amount or client name appears here.

---

## 1. Answer

**Yes. yfinance alone carries the first in-house version of all three variants, with no Bloomberg call.** On the
reference portfolio it supplies the price history, the single-stock reference fields and the fund look-through for
every sleeve that has one. What it does not supply is a short, nameable list (section 4), and none of it blocks a
working report.

## 2. The probe

- **What ran:** yfinance 1.2.0 (already installed; Yahoo is already the vendor of Opal's scheduled price pull), one
  pass over the 99 holdings of frozen request `REQ-a618aa83407689bc95193a01` plus four controls (an equity ETF, a bond
  ETF, a mutual fund, a stock). Three reads per ticker: `info`, monthly `history(period="max")`, and `funds_data` for
  funds. Read-only; nothing written to a production path. Zero request errors.
- **Controls:** all four returned full data, including the mutual fund (history from 2000, sector weights, asset
  classes, top holdings, expense ratio). The reference portfolio itself holds no mutual fund, so mutual-fund coverage
  rests on that one control.
- **Denominator:** 99 holdings; weights are dollar weights of that one portfolio.

## 3. What yfinance returned

**The portfolio's make-up, now exact:** 81 single stocks (20.7 percent of weight) and 18 exchange-traded funds (79.3
percent). This replaces the parent's "39 to 83 percent" range for funds.

| Need (parent gap) | yfinance source | Coverage on the 99 holdings |
|---|---|---|
| Total-return price history (G1) | `history`, which returns both the close and the dividend-adjusted close, plus the dividends themselves | 98 of 99 (99.7 percent of weight); all 98 carry an adjusted close. The one miss is a share-class symbol Yahoo spells with a hyphen: a mapping fix, not a data gap |
| Long windows (G2) | `history(period="max")` | 5 years: 94 holdings, 99.3 percent of weight. 10 years: 90, 98.5 percent. 15 years: 82, 69.9 percent. The shortfall at 15 years is holdings that did not exist then |
| Single-stock reference (G5) | `info`: sector, industry, country, market cap, beta, dividend yield, P/E, P/B, P/S, return on assets, return on equity, debt to equity | sector, country and market cap for 80 of 81 stocks; the ratios for 68 to 80 of 81 |
| Fund asset mix (stock, bond, cash, preferred, convertible, other) | `funds_data.asset_classes` | 18 of 18 funds |
| Fund sector look-through (G6) | `funds_data.sector_weightings` (11 sectors) | 14 of 18 funds; the other 4 are bond funds, which have no equity sectors. Stocks plus funds together: sector data for 88.0 percent of the portfolio's weight, against an equity share of 88.2 percent |
| Fund fundamentals (G7) | `info` and `funds_data`: net expense ratio, yield, total assets, inception date, category, fund family, holdings turnover; weighted P/E, P/B, P/S, P/cash-flow, median market cap | 18 of 18 for expense ratio, yield, assets and inception date |
| Bond sleeve (G8) | `funds_data.bond_ratings` (credit quality: government, AAA, AA, A, BBB, BB, B, below B, other) and `bond_holdings` (duration, maturity, credit quality) | credit-quality breakdown for 6 of 18 funds, which includes all 4 bond funds |
| Fund constituents (G10) | `funds_data.top_holdings` | top 10 for 14 of 18 funds (13 with ten rows, 1 with nine); none for the 4 bond funds |

**A side effect worth knowing:** Yahoo's fund sector names are the Morningstar scheme (basic materials, consumer
cyclical, financial services and so on), the same scheme YCharts prints, while Yahoo's single-stock sectors use the
same names. On yfinance the sector pages would therefore come out in one consistent scheme that matches the YCharts
layout, without a mapping. This touches the approved choice of GICS sectors (card 3): GICS was recommended because
Bloomberg was the assumed source. Recommendation: while the source is yfinance, print its scheme and state it on the
page; revisit when Bloomberg is the source.

## 4. What yfinance does not give

| Report content | Why not | What the first version does |
|---|---|---|
| Region and country look-through of funds (about 78 elements per variant) | no such field in yfinance | print stock holdings by country; for funds, state "not available" or use the fund's category label; Bloomberg `HB_GEO_CNTRY_ALLOC` or SEC filings later |
| Top-25 constituents | only the top 10 are served | print the top 10 and say so |
| Maturity buckets (16) and bond-sector breakdown (6) | only average duration, average maturity and the credit-quality breakdown | print the averages and credit quality; SEC filings later |
| Market-cap buckets and the style box | only a median market cap per fund | Opal-defined buckets for the stock sleeve only; no style box (already approved) |
| Sales loads, SEC yields, fee waivers | not served | omit; SEC prospectus data later |
| Risk-free rate (G3) | Yahoo serves a 13-week Treasury bill yield index; not probed today | probe it, or use the Bloomberg series already received daily |
| History of the snapshot fields | Yahoo serves the current values only | capture nightly from the first day, as for Bloomberg |

## 5. Conditions of using yfinance as the source "for now"

- **It is an unofficial reader of Yahoo's site**, not a contracted feed. Yahoo can change or throttle it without
  notice. Opal's scheduled price pull has run on it daily, so the risk is known and already carried.
- **Fetch on a schedule, never at report time.** The probe was three reads per ticker with a pause between tickers.
  The report reads Opal's cache; a first-seen security is fetched once when the upload resolves it.
- **Fund figures carry Yahoo's own as-of date**, typically the fund's last monthly or quarterly disclosure. The
  report prints that date.
- **One portfolio was probed.** Coverage on other client files is expected to be similar for US-listed stocks and
  funds and is unmeasured.
- **The existing pull must change one thing first:** it stores one close column from two differently adjusted
  fetches (parent G1, INHERITED). The in-house report needs the adjusted close, or the close and dividends, stored
  as separate named columns.

## 6. What this changes in the parent's sequence

- Stages 1 to 4 (the Overview thread, fair exposures, long windows, Comparison and Multi) need **no Bloomberg call
  and no new vendor**: yfinance covers them, minus the rows in section 4.
- Bloomberg moves from a prerequisite to a later enrichment (fund region look-through, the daily fund-allocation
  capture approved in card 2, which waits on quota).
- Stage 5 (fund detail from SEC filings) and stage 6 (one side-by-side per variant, then YCharts retires) are
  unchanged.

## REFS

```
  THIS FILE     docs/briefs/irpt-ycharts-inhouse-generation-yfinance-probe-20261005.md
  PARENT        docs/briefs/irpt-ycharts-inhouse-generation-feasibility-20261005.md
  ORDER         org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261005_195xZ_YCDGEN_FIVE_RECS_APPROVED_EXPLORE_YFINANCE.md
  HOLDINGS READ opal-data-cottonwood/irpt/cottonwood/state/ycharts_runs/request=YCD-R3-20261005T0219Z/run.json (99 rows)
  EXISTING PULL data/black_diamond/scripts/silver/fetch_historical_prices_yfinance.py
  PROBE SCRIPT  session scratchpad (not committed: its output names client holdings)
  MEASURED AT   2026-10-05 ~20:0xZ
```
