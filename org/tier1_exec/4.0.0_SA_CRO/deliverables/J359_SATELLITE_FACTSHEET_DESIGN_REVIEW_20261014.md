# J359 -- design review: a factsheet per Opal Satellite in the Positioning modal

**archetype:** EXPLORE

From `4.0.0_SA_CRO~DELL1` to `2.0.0_SA_COO~J1`. Requested by Andrew in session on 2026-10-14. Brief:
`C:/Users/Test/AppData/Local/Temp/remote-job-J359-brief.md` (requester Yang Liu, for CW).

**v2, 15:5xZ:** the two example PDFs are now read, from local copies Andrew downloaded:
- `C:/Users/Test/Downloads/Opal_Dividend_Income_One_Pager 1.pdf`
- `C:/Users/Test/Downloads/Opal_Moderate_Income_Tax_Efficient_One_Pager 1.pdf`

v1 called them unreachable. That was wrong in substance: Andrew says the gateway can download Teams files. The two
routes this seat tried (`read_document` by item id, with and without the drive id) returned Graph 400, so the right
call is still to be named.

Served data was read live on 2026-10-14 between 15:40Z and 15:55Z:
- `s3://opal-data-cot/platinum/satellites/{registry,characteristics,holdings}.json`, as_of 2026-10-14;
- `s3://opal-data-portal-v2/json/positioning/positioning_data.json`.

## What was asked (Teams, Andrew and Yang 1:1)

- 15:00:42Z, Yang: "CW is looking for a factsheet like template like this to host each satellite model", with the two
  PDFs attached.
- 15:31Z, Andrew: "formulate this with the currently served data and just drop them in those popups".
- 15:35:42Z, Yang: "no need to generate additional data, just reorganizing some of the existing data."
- 15:36:02Z, Yang: "We told them 1-2 weeks, so no rush."

## Verdict

**The approach is right: reorganize served data in the existing `SatelliteModal`, using the template's layout.**

But **about half the template's sections have no served satellite counterpart.** The two one-pagers are restyled
**YCharts** reports; each disclosure names its source ("Source: YCharts, ... Comprehensive Overview"). Their
calendar-year performance, risk statistics, sector, market-cap, style and fundamentals blocks come from YCharts, not
from anything Opal serves for the satellites.

"No new data" therefore means a **partial** factsheet. Yang and CW should see the section list below before the build,
not after it.

## The template, section by section, against what is served for the satellites

| # | Template section (both PDFs) | Served for satellites? | Source / rule |
|---|---|---|---|
| 1 | Header: name, "Prepared for Cottonwood Capital Advisors", data as of | YES | `registry.json` code / displayName; as_of from the artifacts (holdings 2026-10-14; positioning and BBG 2026-10-13). Print the date each number carries. |
| 2 | Tile: YTD total return, plus trailing 1 year | YES, as hypothetical | `characteristics.json` satellites[n].returns YTD and 1Y. See finding B. |
| 3 | Tile: stocks / bonds split, plus a one-line note | YES | Sum of `holdings.json` row weights by `asset_class` (equity / fixed_income / cash / commodities / structured). Display aggregation, as `satelliteAdapter.ts` already does. |
| 4 | Tile: distribution yield, plus holdings count | YES, with coverage | `characteristics.json` yield (coverage 91.6% or more) and the row count of `holdings.json` (16 to 24). The PDF's "30 day SEC yield" is NOT served. |
| 5 | Performance: calendar-year bars 2021 to 2026 YTD, annualized 3 / 5 / 10 year | **NO** | Only windows up to 1Y exist (1D, WTD, MTD, 1M, QTD, 1Q, YTD, 1Y). No calendar years, no inception. |
| 6 | Risk statistics (1Y): standard deviation, Sharpe, Sortino, beta, 1Y and 5Y max drawdown | **Beta only**, with low coverage | Beta is served, but not renormalized (finding C). Nothing else in this block is served. |
| 7 | Region exposure (equity) | **Coarse only** | Equity `sub_asset_class` gives US Large Cap / US Mid Cap / Developed / EM. There is no country split. |
| 8 | Fixed income characteristics: current yield, YTM, effective duration | **Partial** | Duration is served, with coverage as low as 6.84% (Satellite 90). YTM is not served. |
| 9 | Holdings table: fund, name, weight, yield (the Moderate Income layout) | **YES, fully** | `holdings.json` rows (ticker, weight) joined to `characteristics.json` `tickers` (name, yield, fee, management_style). 26 distinct tickers across the 9 satellites, 26 of 26 named. **The satellites are fund-of-ETFs, so the Moderate Income layout (all funds, 100% total) is the right model, not Dividend Income's "Top 10 of 28 stocks".** |
| 10 | Stock sector exposure (Morningstar super-sectors) | **NO** | The closest served view is asset-class / sub-asset-class (12 classes over 178 rows: equity Developed / EM / US Large Cap / US Mid Cap; fixed_income High Yield / Intermediate / Short Duration / Structured Credit / Ultra Short Duration; cash; commodities Metals; structured Hedge). Show that as "Allocation", not as "Sector". |
| 11 | Market capitalization, equity style box, equity fundamentals (P/E, P/B, ROE, debt/capital, market cap) | **NO** | Not served for any satellite or model book. |
| 12 | Important disclosures | **No source** | A compliance text that must match the method of each number shown. See finding D. |

Count: sections 1, 2, 3, 4 and 9 are fully servable. Sections 6, 7 and 8 are partial. Sections 5, 10, 11 and 12 are not
served.

## Findings

### A. Decide the unserved sections BEFORE the build (the one question for Yang)

There are three options:
- (i) **Omit** sections 5, 10 and 11, and render 6 to 8 with only what is served. This is the honest partial, and fits
  "no new data".
- (ii) Show them as **"Not available"**. This shows what is missing, but a client sees a half-empty factsheet.
- (iii) A **data project** that sources them, for example from YCharts or a Bloomberg look-through of the 26 ETFs. That
  is new data, contrary to Yang's word, and it is not a 1-2 week remote job. YCharts is also fragile on this estate: a
  WAF block on 2026-10-14, and `1.0.0_SA_CTO~DELL1`'s stop on further YCharts calls from this seat (msg 5356).

**Recommendation: (i).** Have Yang confirm it with CW against the table above.

### B. Returns are hypothetical. Label them with THEIR method, not the PDF's.

- The Moderate Income PDF already sets the precedent of "hypothetical" returns for CW. Its method is YCharts' "target
  weights, rebalanced quarterly".
- The satellite figures use a different method: **current holdings' weights times each holding's own trailing return**
  (`method.tickers_block.returns_rule`: `etf_positioning_gold.py compute_returns`). There is no rebalance history, and
  return coverage is not 100% (1Y as low as 80.05%, Satellite 80).
- The label and the disclosure must state this method. Copying the PDF's disclosure would misdescribe the numbers.

### C. The characteristics understate where coverage is partial

- `method.formula` is `sum(weight_pct * value over holdings WITH a value) / 100`, with `renormalised: false`. A holding
  with no value counts as zero.
- Lowest coverage across the 9 satellites:

  | Field | Lowest weight coverage | Satellite |
  |---|---|---|
  | fee | 98.94% | 90 |
  | yield | 91.6% | 15 |
  | duration | 6.84% | 90 |
  | beta | 17.09% | 15 |
  | 1Y return | 80.05% | 80 |

- **Design:** print each figure with its coverage (served as `coverage.weight_with_value`), or "Not available" below a
  floor that Yang or Andrew sets. Never present a partial sum as the satellite's figure.
- The current modal already shows Beta this way.

### D. Disclosures need an owner

- The PDFs carry a full disclosure paragraph, which is content, not data.
- It must say:
  - source = Opal served data, not YCharts;
  - returns = hypothetical, current holdings' trailing returns;
  - characteristics = weighted over covered holdings;
  - holdings as of their date.
- Who writes and approves it is Yang's or Andrew's call.
- Where it lives: hard-coded TSX text is a second carrier, and the content store has no satellite namespace
  (SatelliteModal header). The smallest honest home is one constant in the modal file, written verbatim from Yang's
  approved text. Name that file as its single home.

### E. Shape of the build (keep it small)

- Change `src/components/SatelliteModal.tsx` and at most one presentational component. Read the payload the adapter
  already builds (`PositioningPortfolio`: characteristics, allocation, holdings), plus the `tickers` identity it
  already attaches.
- No new fetch, route or Lambda.
- Reuse the template's visual grammar: three KPI tiles, holdings table, allocation bars. Do this inside the HeroDialog
  family (ModelPortfolioModal, EtfModal), not as a separate page.
- No PDF or print export unless Yang asks. The brief's CHECK is "open each popup and see the factsheet".
- SatelliteModal's header comment still says "the adapter's MEASURE blend over the constituents' live positioning
  (blend A)". Since POSN_ASTTAX TO-V7-1 the adapter reads served `characteristics.json`. Correct the comment in the
  same edit.
- Satellite 60's served displayName is `Opal - Satellite 60`; the other eight read `Opal Satellite NN`. Keep using
  `shortSatelliteName()`.
- **Do NOT blend the constituent model books' `segment.sector` / `segment.geography`** (served in
  `positioning_data.json` for UST/ST/INT/LT/ULT) into a satellite figure. `satelliteAdapter.ts`'s header records why
  that was removed: a satellite holds tickers no model book carries (GLD in 9 of 9). The sections 7 and 10 shortcut is
  exactly that defect.

### F. Landing law (client-facing)

- CW sees Satellites mode (`src/pages/Positioning/shared/modeAccess.ts:118`, satellites = internal plus `cottonwood`).
- Under the Portal rule (CLAUDE.md @fcdfc34843), DEV is written only by `.tools/portal-merge-forward.sh cand/dell1/<slug>`
  on an approved row; client-facing changes **wait for Andrew**, and so does PROD.
- Validate on the dev build (port 5174) as a CW login (`/ui-walk`) across all **9** satellites.

### G. Related open item

Satellite returns use the same `compute_returns` as MDPF_SECHIST FWD-9. On a day a holding's own market was closed,
every window for that holding blanks (`etf_positioning_gold.py:994`). The rule change is with `1.0.0_SA_CTO~DELL1`
(`org/tier1_exec/4.0.0_SA_CRO/deliverables/CLOSED_MARKET_ASOF_RESEARCH_MDPF_SECHIST_FWD9_20261014.md`). Do not work
around it in J359.

## Not read

- The live CW render of the current modal.
- `capabilitiesFor('satellites')` source lines (cited from `satelliteAdapter.ts:449-450`).
- Which gateway call downloads a Teams attachment from the sender's OneDrive.
