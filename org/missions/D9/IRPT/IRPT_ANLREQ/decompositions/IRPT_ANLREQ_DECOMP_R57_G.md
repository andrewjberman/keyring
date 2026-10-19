# IRPT_ANLREQ round 57, workstream ~G (ENGINE) -- decomposition: the Opal-built report's price pages (FWD-7; row 3c22, hold C-V1 lifted)

Issuer `2.0.0_SA_COO~G2`, 2026-10-19.

**Input.** Andrew-direct 2026-10-19 ~14:4xZ "all holds are lifted" (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261019_144xZ_ALL_HOLDS_LIFTED.md` @93efb20243), closing row 3c22 (C-V1, IRPT_YCDGEN PRD :251, "let's avoid pricing for the v1"). CTO msgs 10729, 10734, 10743: cut the price pages as the next ENGINE round; they build on AR-g-155's `fund_data` form (`price_adapter_ycharts.py:97`), AR-g-152 stays archived (tag `archive/wk-IRPT_ANLREQ-276`); prices come only from the source order Andrew set on 10-14 (estate, yfinance, ycharts), no new vendor leg; ADD one per-holding price table as its own cell, parallel, gating none of the 17; dividends/yields, the scatter plot and ROA/ROE are out. The round ships behind the 425-cards fix (TO-AR-y-404) in IB2's queue; nothing here is deployed by it.

**Measured base** (`deliverables/2.0.0_SA_COO~G2/PRICE_PAGES_INVENTORY_20261019.md`, @fd2ea7e9a7): the producer's price stage (AR-g-86/93) is already on in r34k and turns 9 of 254 overview elements to VALUE; 17 price-based elements still read NOT_IN_THIS_VERSION. The layout already holds the statistic engine (`_STATS`: total_return incl. ytd, std_dev, max_drawdown, alpha, beta, sharpe, sortino, var_monthly over 1y..15y; `cumulative_series`), the chart renderer (a list of numbers or [x, y] pairs) and the table renderer (a dict, or a list of dicts). So most of the 17 are re-points of a map element's `source` to `OWN_SERIES`, and only four forms are new code.

## Cells

| cell | elements (17 + the table) | what it adds | write set | chain |
|---|---|---|---|---|
| `AR-g-163` | p2.e11 Beta 5Y, p2.e15 Alpha 5Y, p2.e14 YTD, p7.e04 Std Dev, p7.e10 Return, p7.e13 Std Dev (tables), p7.e11, p7.e12 (the two Risk/Reward charts) | MAP ONLY: re-point to `OWN_SERIES` statistics that exist (`beta_5y`, `alpha_5y`, `total_return_ytd`; column lists) | `overview_map.json`, one new test file | A |
| `AR-g-164` | p2.e04 cumulative chart, p6.e21 drawdown chart, p2.e17 annual bars, p2.e18 annual table, p7.e15 benchmark chart | NEW statistics `drawdown_series`, `annual_returns`; the benchmark as a named series; `cumulative_series` wired | `layout_overview.py`, `overview_map.json`, one new test file | B (1 of 2) |
| `AR-g-165` | p2.e07, p2.e16 as-of lines; p2.e03, p6.e20 legends | NEW text statistics `as_of_text`, `legend_text` | `layout_overview.py`, `overview_map.json`, one new test file | B (2 of 2, after 164) |
| `AR-g-166` | the per-holding price table (new element `opal.prices.holdings`) | NEW computed method `PRICE_TABLE`; the element appended after the last page like the classified elements; ticker, last price date, source tier as the claim | `layout_overview.py`, `opal_producer.py`, one new test file | C |

17 = 8 + 5 + 4. Every cell is gated by the shared checker `deliverables/2.0.0_SA_COO~G2/checks/ar_price_checks.py` (`<cell> build|guard|regress`), dry-run at the base: all four builds FAIL, all four guards PASS, regress PASS; `calibrate` reads OK at the base (the checker's own YTD and max-drawdown arithmetic agrees with the shipped elements).

## Edges and chains

- **A, B, C are independent** (no data edge). **165 depends on 164** (same worker queue: both add statistics in `layout_overview.py`'s statistic engine; two orders on one chain belong to one worker).
- Shared files: `overview_map.json` is edited by A and B at DIFFERENT elements (a pretty-printed 3,204-line file: the merges are textual and disjoint); `layout_overview.py` is edited by B and C in different regions (B: the statistic engine; C: the computed-method dispatch and a new method). The issuer merges at the drain, one chain at a time (`safe-merge.sh`), and re-runs every cell's three arms on the merged tree.
- `fanout: 3 of 3 chains, cap 8` (A, B, C).

## What this round decides (inside this decomposition)

- **Columns.** The vendor Risk/Reward tables carry 1Y 3Y 5Y 10Y plus All Time (and 15Y for Risk Info). The price window is 10 years (`PRICE_HISTORY_YEARS`), so 15Y can never read; and `total_return_all` is not a statistic of the engine. The tables carry **1Y 3Y 5Y 10Y** only. All Time and 15Y are NOT built (named in the packet).
- **Annual returns.** One column per calendar year that has a prior-year-end level in the window (the layout's YTD convention: the last level at or before 31 December), then `YTD`; the bars are the same numbers in order.
- **Legend text** (no Opal-path equivalent of the vendor portfolio name): `Opal portfolio: buy-and-hold from the accepted amounts, priced to <YYYY-MM-DD>.` The as-of line is `As of <YYYY-MM-DD>`; both dates are the last level of the series. No holding count and no source list on the legend: the statistic engine sees only the series (a count of all holdings would overstate coverage when one is unpriced); the sources are the claim of the price table (cell 166) and of `run.json`.
- **Price table.** A list of dicts, one per priced holding in holdings order: `Ticker`, `Last price date`, `Source` (a NEUTRAL label of the tier that answered, one-to-one: estate -> `Opal data store`, yfinance -> `Public market data`, ycharts -> `Licensed market data`; R8 forbids a vendor name on an Opal page, and the exact tier stays the run.json claim; AMENDMENT 1 of AR-g-166). An unpriced holding reads `Last price date` `not priced` and `Source` `none`. It reads only the price stage's own record (`run.json` `prices.symbols`), no new vendor call, and with pricing off the element is present and reads NOT_AVAILABLE / NOT_IN_THIS_VERSION like every other price element.
- **Claim.** Each priced figure keeps its source as a claim field in `run.json` already (`prices.symbols[t].source`); cell 166 puts the same claim on the page.

## Not in this round (named)

All Time and 15Y columns; dividends and yields (Distribution Yield p2.e10 and p8.e05, Current Yield p8.e15, Yield to Maturity p8.e17: FWD-10, no price tier serves them); the Risk/Reward scatter plot (p8.e02) and ROA/ROE (p8.e08, p8.e13); the fund look-through charts; the comparison and multi maps (not measured); a live priced request (window 5's first answer is owed); the release itself (its own never-widen pair, after TO-AR-y-404; the new map bytes and `layout_overview.py` and `opal_producer.py` are movers the pair must name).

## Four-postulate record

(i) Domain: the 17 price-based elements of the overview map that read NOT_IN_THIS_VERSION with pricing on, by subtraction from the printed 254 (157 unavailable: 65 BUILDER_ONLY, 70 OPAL_HELD no-rule, 22 VENDOR_SOURCED); 17 are in, the rest named out above. (ii) One grain: a map element. (iii) One intent per cell: re-point / new series / new text / new table. (iv) What this round does NOT move: pricing off (every price element still reads NOT_IN_THIS_VERSION), the nine base VALUE elements (byte-equal), every non-price element, the tiers, the readers, the adapters.

fanout: 3 of 3 chains, cap 8, reason: A (163), B (164 then 165), C (166); the shared files are merged by the issuer at the drain.
