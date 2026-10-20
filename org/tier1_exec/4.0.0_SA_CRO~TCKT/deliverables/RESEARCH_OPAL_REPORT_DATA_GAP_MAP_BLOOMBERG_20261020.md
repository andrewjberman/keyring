# Opal report data gap map: yfinance first, Bloomberg fallback (4.0.0_SA_CRO~TCKT, 2026-10-20 ~22:xxZ)

Read-only research. Claim tags: M = measured (read here), I = inferred.

**Andrew's rulings:** `ANDREW_DIRECT_20261020_22xxZ_REPORT_FROM_DATA_WE_HAVE_BLOOMBERG_DRAW.md`, plus his later words:
- "the premise is simply to recreate the y chart format, hwoever we have to do it";
- "there are no limits on bloomberg when it comes to this, it has to get done".

**Target:** every chart and concentration breakdown in the YCharts Comprehensive Overview sample, reproduced from real
data. The source order is yfinance first, Bloomberg second, and Bloomberg has no budget limit.

**Inputs (M):**
- run 7d run.json: `s3://opal-data-49financial/irpt/49financial/state/ycharts_runs/request=REQ-bb8793fa8c8e2c9da8bc033d/run.json`;
- the sample page inventory (local only; field names are used here, never values);
- `opal-data-etfs/bbg/2026-10-19/characteristics.parquet`;
- yfinance 1.7.0 read-only calls on AAPL, SPY and AGG;
- `integrations/bloomberg/{READ_HERE,README}.md` and `research/pull_consumer.py`.

## 1. What run 7d actually lacked (M)

- **Element counts:** run.json has 257 elements, 13 VALUE and 244 NOT_AVAILABLE. The portal's "100 sections, 87 not
  available" is a coarser grouping of the same record.
- **The root cause is coverage, not design.** The producer already reads Bloomberg mnemonics for these groups:
  `CNTRY_OF_DOMICILE`, `GICS_SECTOR_NAME`, `CUR_MKT_CAP`, `FUND_EXPENSE_RATIO`, `EQY_DVD_YLD_IND_NET`.
- **But the parquet covers only Opal's ETFs and their constituents:** 173 rows. Its universe is derived by
  `etf_daily_pull.py` from `opal-data-etfs/silver/holdings`.
- **Result:** a filed holding outside that universe reads `INPUT_MISSING:security_not_covered`.
- **The other groups have no field wired at all:** `field: null`, `NOT_IN_THIS_VERSION`. These are bond sector, credit,
  maturity, style, market cap buckets and most fundamentals.

**Parquet columns (M):** `security, NAME, EQY_DVD_YLD_IND_NET, BETA_ADJ_OVERRIDABLE, GICS_SECTOR_NAME,
GICS_INDUSTRY_GROUP_NAME, GICS_INDUSTRY_GROUP, CNTRY_OF_DOMICILE, CUR_MKT_CAP, FUND_EXPENSE_RATIO, FUND_TOTAL_ASSETS,
TOTAL_NUMBER_OF_HOLDINGS_IN_PORT, HB_OAS_EFF_DURTN, YAS_ISPREAD_TO_GOVT, TRACKING_ERROR`.

**How a portfolio breakdown is built (I):** YCharts rolls each holding up by weight.
- A stock contributes its own attributes.
- A fund contributes its fund-level allocations.
- So every group below needs a stock path and a fund path.

## 2. The map, ranked by the charts and breakdowns each group unlocks

The NA column counts run 7d's NOT_AVAILABLE elements. "yf" = yfinance (`Ticker.info` keys and `Ticker.funds_data`
methods). "BBG" = a Bloomberg ReferenceDataRequest mnemonic through the existing pull seam.

| Rank | Group (sample page) | Charts / breakdowns | NA | Stock path: yf, then BBG | Fund path: yf, then BBG | Fill |
|---|---|---|---|---|---|---|
| 1 | Region and country exposure (p3-4) | Market class, 3 regions, about 60 countries | 67 | yf `info.country` (M on AAPL); BBG `CNTRY_OF_DOMICILE` (M, in parquet) | yf has NO country or region method (M: `funds_data` has none); BBG `HB_GEO_CNTRY_ALLOC` (M served, READ_HERE s.4) | **BBG** for funds; yf for stocks |
| 2 | Stock sector (p5) | 11 sectors + cyclical/sensitive/defensive | 14 | yf `info.sector` (M); BBG `GICS_SECTOR_NAME` (M) | yf `funds_data.sector_weightings` (M: SPY 11 keys); BBG `HB_INDUSTRY_SECTOR_ALLOCATION` (M served) | **yf** |
| 3 | Asset allocation pie (p3) | Cash, stock, bond, preferred, convertible, other | 7 | yf `info.quoteType` (M) places the stock whole | yf `funds_data.asset_classes` (M: SPY, AGG, 6 keys); BBG `HB_ASSET_CLASS_ALLOCATION` (I, name to confirm) | **yf** |
| 4 | Credit quality (p5) | AAA to Not Rated | 8 | direct bonds: BBG `RTG_SP` / `RTG_MOODY` / `BB_COMPOSITE` (I) | yf `funds_data.bond_ratings` (M: AGG 9 keys); BBG `HB_*` rating allocation (I) | **yf** for funds |
| 5 | Bond maturity buckets (p6) | 16 buckets + short/intermediate/long | 17 | direct bonds: BBG `MATURITY` (I) | yf gives only the average maturity (`bond_holdings` "Maturity", M), not buckets; BBG `HB_*` maturity allocation (I, name to confirm) | **BBG** |
| 6 | Bond sector (p5) | Government, corporate, municipal, securitized, cash, derivative | 7 | BBG `INDUSTRY_SECTOR` / `BICS_LEVEL_1_SECTOR_NAME` (I) | yf has no bond-sector method (M); BBG `HB_*` fixed-income sector allocation (I) | **BBG** |
| 7 | Market cap buckets (p3) | Giant, large, mid, small, micro | 6 | yf `info.marketCap` (M); BBG `CUR_MKT_CAP` (M); bucketed by a stated cut rule | yf gives only the median market cap (`equity_holdings`, M), not buckets; BBG `HB_*` market-cap allocation (I) | yf for stocks, **BBG** for funds |
| 8 | Stock style box (p3) | 3x3 large/mid/small x value/blend/growth | 9 | yf `marketCap` + `priceToBook` + growth keys (M exist), under a stated style rule | yf: none (M); BBG fund style fields (I: e.g. `FUND_MKT_CAP_FOCUS` with a style or objective field), or a constituent look-through | **at risk**, see section 3 |
| 9 | Fundamentals (p8) | Stock block, bond block, general block | 19 | yf `trailingPE`, `priceToBook`, `priceToSalesTrailing12Months`, `dividendYield`, `debtToEquity`, `marketCap` (M); ROE/ROA `returnOnEquity`/`returnOnAssets` (I) | yf `equity_holdings` P/E, P/B, P/S, median mkt cap (M); `bond_holdings` duration, maturity, credit (M); `info.yield`, `netExpenseRatio`, `dividendYield` (M); BBG for the rest: `TOTAL_NUMBER_OF_HOLDINGS_IN_PORT` (M), `HB_OAS_EFF_DURTN` (M), YTM, coupon, average price, current yield (I fields) | about 12 **yf**, about 7 **BBG** (I split) |
| 10 | Top / underlying holdings (p9-11) | Top 10 table, top-25 look-through | 0 NA, partly shown | the portfolio's own holdings (VALUE today) | yf `funds_data.top_holdings` (M: top 10 per fund); full constituents: issuer CSV for the Opal ETFs (M, READ_HERE s.5), else BQL (not entitled, READ_HERE s.4) | yf top 10; full list **at risk** without BQL |
| 11 | Return and risk series (p2, 6-8) | Cumulative line, periodic and annual bars, drawdown, risk table, scatter, benchmark | 25 | prices (yfinance-first chain, C-PRICES); beta yf `beta3Year` for funds (M) or BBG `BETA_ADJ_OVERRIDABLE` (M) | same | **code, no new data** (computed from prices held) |
| 12 | Cover, disclosures, definitions (p1, 12-21) | Text | 65 | Opal-authored text | | **not data** |

## 3. Counts of the 244 NOT_AVAILABLE elements (I: the fundamentals split is estimated)

| Source | Elements |
|---|---|
| yfinance first | 41 (sector 14, asset allocation 7, credit 8, fundamentals ~12) |
| Bloomberg fallback | 104 (region and country 67, maturity 17, bond sector 7, market cap buckets 6, fundamentals ~7) |
| Already held: price math to code | 25 |
| Text, not data | 65 |
| At risk | 9 (style box) |

Neither source can fill **only the style box for funds**, and only if no Bloomberg fund-style field serves it:
- yfinance has no style.
- Bloomberg will not enumerate fund constituents without BQL, which this seat is not entitled to (M, READ_HERE s.4).

Andrew's "no limits on Bloomberg" makes the BQL entitlement the clean answer. One purchase turns on constituent
look-through for every fund, which also completes the top-25 table (row 10). That is his spend decision, named as such.

## 4. Build order (most charts first; this is order, not scope)

1. **yfinance `info` plus `funds_data`, per security** in the filed holdings and comparables. This unlocks sector,
   asset-allocation pie, credit quality, about 12 fundamentals and top-10 holdings.
2. **Price math already held.** Cumulative, periodic, annual, drawdown, risk table, scatter and benchmark: code only.
3. **Bloomberg `HB_GEO_CNTRY_ALLOC` + `CNTRY_OF_DOMICILE`.** This is the region and country block, the largest single
   group (67).
4. **Bloomberg holdings-based allocations** for maturity, bond sector and market cap (exact `HB_*` names to confirm with a
   `FLDS` read on the Terminal), plus the remaining bond fundamentals.
5. **Style box:** a Bloomberg fund-style field if one serves, else the BQL entitlement.

## 5. The draw (I unless marked)

- **Universe:** every security in a filed holdings file, plus every comparable ETF and model holding.
- **Unit:** one security, cached per security per trading day.
- **Cadence:** on demand at filing.
  - The `HB_*` allocations are CURRENT-DAY ONLY: a HistoricalDataRequest returns zero rows (M, READ_HERE s.4). There is
    no backfill, and a report reads today's allocations, so this is enough.
  - Optionally add the filed universe to the daily vehicle's derived universe, so repeat holdings are already warm.
- **Vehicle:** the existing on-demand seam, `integrations/bloomberg/research/pull_consumer.py` (M).
  - It takes one SQS message per ticker and runs `bloomberg_health()` first.
  - It writes `status.json` FETCHING to LANDED or FAILED, and never auto-signs-in.
  - It runs under the PY_AWS interpreter on the Terminal box.
  - The resident would enqueue the misses and read the landed rows; yfinance answers first and in-process.
- **Landing:**
  - Today's characteristics sit at `opal-data-etfs/bbg/<date>/characteristics.parquet`. That is a pre-canon catalog
    address (`infra/logic/registry/legacy_addresses.json:1179`, `catalog-opal-data-etfs-silver-bbg-characteristics`).
  - A per-security reference family for the report needs a **registry row (missing)**, so `address()` can build it
    (rule 30).
- **Constraints:**
  - One Terminal seat. Sign-in is two-phase with a 2-attempt budget (READ_HERE s.2).
  - A signed-out terminal stops every Bloomberg leg, so yfinance-first keeps reports flowing.
  - BQL is not entitled.

## 6. Conflict check

- **C-PRICES** (IRPT_ANLREQ PRD: "Bloomberg is OUT of this chain") governs PRICES only. It stays: prices remain
  yfinance-first.
- **Andrew's new word is about security characteristics.** The OPAL_HELD design already reads a Bloomberg
  characteristics parquet. His ruling widens that read's universe and field set; it overturns no recorded ruling (M,
  rows read).
- **C-SWAP / C-KIMI:** untouched.

## 7. What this does not claim

- `HB_*` names other than `HB_GEO_CNTRY_ALLOC`, `HB_INDUSTRY_SECTOR_ALLOCATION` and `HB_OAS_EFF_DURTN` are unconfirmed
  (no `FLDS` read; no Bloomberg pull was made).
- yfinance coverage is measured on three liquid US tickers only, not on mutual funds, ADRs, bonds or small caps.
- The fundamentals split (~12 / ~7) is estimated.
- Whether run 7d's 3 synthetic holdings would resolve in yfinance was not checked.
