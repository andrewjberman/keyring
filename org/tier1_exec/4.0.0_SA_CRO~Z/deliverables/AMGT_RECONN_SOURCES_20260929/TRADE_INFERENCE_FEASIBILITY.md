# Trade inference from daily holdings: feasibility, measured

Author: 4.0.0_SA_CRO~Z. Measured September 30, 2026, ~04:2x UTC, on Andrew's direction to reverse engineer each rival fund's trades (verbatim in `ANDREW_DIRECT.md`, "Trade schedule as the foundation of the analysis"). Local files only; no network.

## The answer

**Yes, and more directly than a price-and-weight reconstruction.** Every issuer file for these funds carries share **quantities**, not only weights. A trade therefore shows up as a change in share count, once the day's fund flow is removed. For these ETFs, creations and redemptions scale every position almost exactly pro rata, so the flow is one number per day and removing it is clean. What stays approximate is the trade's **price** and its exact **day inside the window** between two reports. The share count itself does not.

## Method

For each pair of consecutive report dates, over the securities held on both days:

- **flow factor** `f` = median of `q_t / q_{t-1}` (in-kind flows scale every position by the same ratio);
- **residual** = `q_t - f * q_{t-1}`: the discretionary change;
- **trade event** = residual above `max(0.2% of prior shares, 5 shares)`, plus every entry and exit. The 0.2% floor is Andrew's (*"Trades can be 0.2% or more, not 0.5%"*); the probe's first pass used 0.5%, and both are reported below.

Script: `scripts/trade_inference_probe.py` (`python .../trade_inference_probe.py BASG GQGU`), over the full issuer archives already captured for the coverage census (`.runtime/amgt-reconn-daily-census-20260929/{basg,gqgu}/`, device-local).

## Results

| Fund | Report dates | Day pairs | Pairs with a flow (f != 1) | Median spread of position ratios around f | Position-days fully explained by flow | Trade events | Pairs with at least one trade |
|---|---:|---:|---:|---:|---:|---|---:|
| BASG | 324 (2025-06-13 to 2026-09-28) | 323 | 171 | 0.001% | 92.54% at 0.2% (94.87% at 0.5%) | at 0.2%: 411 adds, 400 trims, 10 entries, 13 exits (834); at 0.5%: 580 | 157 at 0.2% (133 at 0.5%) |
| GQGU | 305 (2025-07-14 to 2026-09-28) | 304 | 168 | 0.0003% | 89.52% at 0.2% (89.84% at 0.5%) | at 0.2%: 603 adds, 483 trims, 92 entries, 88 exits (1,266); at 0.5%: 1,233 | 240 at 0.2% (239 at 0.5%) |

The spread figure is the test of the premise: on flow days, position ratios agree with the flow factor to a few millionths, so the flow model holds and anything off it is a decision. The largest events read like portfolio decisions, not noise. For example, BASG on 2026-05-28 entered GOOG (~$9.9M) and exited VLTO (~$8.5M) with no fund flow (f = 1.0000); on 2025-11-03 it entered AVGO and exited KLAC. GQGU is visibly the more active manager: 1,266 events over 240 of 304 day pairs at 0.2%, against BASG's 834 over 157 of 323. The 0.2% floor sits some 200 times above the flow model's median error.

## What the probe also exposed (design requirements, not failures)

- **Identifier changes masquerade as trades.** GQGU on 2026-07-01 shows an XOM "entry" of 291,467 shares and an XOM "exit" of 265,938 shares on the same day. That is a changed security identifier or a corporate action, not two trades. The production table keys on the resolved security identity (`lib/research/identity/`) and applies corporate actions (splits, spin-offs, mergers) before computing residuals.
- **Trade timing convention.** Fund accounting often books a trade the business day after execution, so a holdings file dated T may reflect trades made on T-1. This must be measured per issuer against price action before a date is stated as the trade date. Until then, the table states a trade window, not a trade day.
- **Price.** The same issuer files give an implied close price for every held security (market value / quantity), so held-position prices come free. Bloomberg is needed for prices of securities after they are exited, for total returns (dividends), and for the day's range, which bounds the execution price.
- **Cash as a cross-check, not the signal.** The change in cash should roughly equal minus the net trade notional, plus dividends, minus expenses, plus any cash in creation baskets. A large unexplained cash residual on a day flags a missed trade or an unapplied corporate action. It does not drive the inference, which answers Andrew's cash concern.

## Coverage of the other four funds

The captured issuer files for TSEL (`Shares Par Value`) and PCLG (`Basket Quantity`, plus `ETF Shares Outstanding` and `Total Net Assets`) carry quantities; the Bloomberg backfill carries `POSITION` for WCMG, TSEL, ETFT and PCLG (`BBG_EXCEL_ACCESS_VERIFIED.md`). Days that Bloomberg carries forward from an older report create no trades; they widen the trade window instead. TSEL's 37-day stale run is one 37-day window. This probe measured BASG and GQGU only.

## Not claimed

Exact execution prices or times, intraday trading, trades that open and close between two reports (invisible by construction), or any intent. The 0.2% floor is Andrew's; the 5-share floor absorbs whole-share rounding of in-kind baskets and is a probe setting.

## Dividends (Andrew, same session: *"Also probably need to account for dividends on thes"*, *"bbg should have dividend calendar for the holdings"*)

Dividends touch the method in three places, and the production table accounts for each:

1. **Cash cross-check.** A window's cash change includes dividends received: shares held at record date times the dividend per share, landing on the pay date (receivable from the ex-date where the fund books accruals). Without this, every dividend window reads as an unexplained cash residual.
2. **Share counts.** Stock dividends, special distributions paid in shares, and splits change quantities. They are applied as corporate actions before the residual is computed, so they never read as trades.
3. **Returns.** Did-the-trade-work evaluation uses total return (price plus dividends), and ex-date price drops are not read as losses.

Source: Bloomberg's dividend history per held security (the `DVD_HIST_ALL` reference field: declared, ex, record and pay dates, amount, type; stock and special dividends are typed). It is ordinary reference data, the BDS class the Excel probes already exercised. It is not yet pulled for these holdings; it is an enrichment pull under the vendor rule the PRD states.
