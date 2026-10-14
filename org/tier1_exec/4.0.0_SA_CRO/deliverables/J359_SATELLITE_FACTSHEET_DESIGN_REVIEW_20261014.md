# J359 -- design review: a factsheet per Opal Satellite in the Positioning modal

**archetype:** EXPLORE

From `4.0.0_SA_CRO~DELL1` to `2.0.0_SA_COO~J1`. Requested by Andrew in session on 2026-10-14. Brief:
`C:/Users/Test/AppData/Local/Temp/remote-job-J359-brief.md` (requester Yang Liu, for CW). Everything below was read on
2026-10-14 between 15:40Z and 15:50Z.

## What was asked (read from the Teams thread, Andrew and Yang 1:1)

- 15:00:42Z, Yang: "CW is looking for a factsheet like template like this to host each satellite model". Two PDFs are
  attached: `Opal_Dividend_Income_One_Pager 1.pdf` and `Opal_Moderate_Income_Tax_Efficient_One_Pager 1.pdf`.
- 15:31Z, Andrew: "formulate this with the currently served data and just drop them in those popups".
- 15:35:42Z, Yang: "no need to generate additional data, just reorganizing some of the existing data."
- 15:36:02Z, Yang: "We told them 1-2 weeks, so no rush."

## Verdict

The approach is sound as long as it **reorganizes served data inside the existing `SatelliteModal`**, with no new
producer, route or store. Five design points need settling before any building starts; points 1 to 3 are where a
client-facing factsheet goes wrong.

## Findings

### 1. The example PDFs are not reachable through the gateway (BLOCKS the template's field list)

- The brief says "use opalgateway to grab the relevant files". Both PDFs sit in **Yang's** OneDrive.
- `read_document(item_id=0176OZOPFGFYSB6XHF4BBLCZHACUL7DZUC)` returns
  `Graph 400 invalidRequest: The provided item ID is not valid for the requested drive`, because the gateway reads
  Andrew's drive.
- Searching Andrew's OneDrive for `Opal_Dividend_Income_One_Pager` returns 0 items.
- Without the PDFs, nobody can say which sections CW expects.
- **Act:** ask Yang to send the two PDFs into Andrew's OneDrive or a SharePoint site the gateway reads, or ask Andrew to
  save them. Then list the PDF's sections against the served fields in the table below. That table is the cell's real
  spec.

### 2. Satellite "returns" are a backcast of today's holdings, not a track record (compliance-shaped)

- `characteristics.json` `method.tickers_block.returns_rule` is
  `etf_positioning_gold.py compute_returns(ticker, bbg_as_of, ...)`.
- Each satellite's 1D to 1Y figure is the **current weights** times each holding's own trailing return. It is not the
  satellite's realized performance, because rebalances, trades and fees are not in it.
- A one-pager's performance table is read as realized performance. Shown to a client firm without a label, this is
  hypothetical performance under the SEC Marketing Rule.
- **Design:** either leave returns off the factsheet, or title them "Trailing returns of current holdings
  (hypothetical; not the satellite's realized performance)", with the as-of date. Which one is Andrew's call, and it
  should be asked before building.

### 3. The characteristics are weight-sums over partial coverage, not renormalized (they understate)

- `method.formula` is `sum(weight_pct * value over holdings WITH a value) / 100`, with `renormalised: false` and
  `divisor: 100`. A holding with no value counts as zero.
- Lowest coverage across the 9 satellites:

  | Field | Lowest weight coverage | Satellite |
  |---|---|---|
  | fee | 98.94% | 90 |
  | yield | 91.6% | 15 |
  | duration | 6.84% | 90 |
  | beta | 17.09% | 15 |
  | 1Y return | 80.05% | 80 |

- So Satellite 15's beta covers only about a sixth of its weight. Every return window below 100% coverage is a partial
  sum.
- The current modal already shows Beta this way. A factsheet makes it more prominent.
- **Design:** print each figure with its coverage, which is served as `coverage.weight_with_value`, or show
  "Not available" below a coverage floor. Andrew or Yang sets the floor. Never present a partial sum as the satellite's
  figure.
- Duration is a special case: equities legitimately have no duration. It needs a stated basis, such as "duration of the
  fixed-income sleeve" (not served) or the served number with its coverage.

### 4. What is served, and therefore what the template can hold without new data

All three artifacts are scoped routes that the portal already reads (`src/api/endpoints/satelliteRegistry.ts:92,100,108`;
firm resolved from the JWT to the bucket).

| Factsheet section | Served source | Notes |
|---|---|---|
| Name, code | `registry.json` books[].code / displayName | Satellite 60's displayName is `Opal - Satellite 60`; the others read `Opal Satellite NN`. Use `shortSatelliteName()` as the modal does. |
| Model blend | `registry.json` constituents[] (book, declared weight) | Already shown in the modal's right pane. |
| Asset allocation | `holdings.json` rows: weight, asset_class, sub_asset_class | Display sum only, as `satelliteAdapter.ts` already does. Coverage labelled 20 of 20 for Satellite 60. |
| Top holdings | `holdings.json` rows plus `characteristics.json` `tickers` (name, management_style, fee, yield) | 16 to 24 rows per satellite. |
| Characteristics | `characteristics.json` satellites[name] fee / yield / duration / beta, plus coverage | See finding 3. |
| Trailing returns | the same artifact, `returns` (8 windows) | See finding 2. |
| As-of | holdings `as_of` 2026-10-14; positioning and BBG `as_of` 2026-10-13 | Print the dates the numbers carry. Two clocks are in play. |
| Objective / strategy text, inception, benchmark, risk statistics, disclosures | **not served** | The modal's own header says "no satellite prose exists". The adapter emits no benchmark (`capabilitiesFor('satellites')` is false). |

- If the PDFs carry an objective paragraph or disclosures, they need a source. Hard-coded text in the TSX file would
  be a second carrier, and the content store has no satellite namespace (SatelliteModal header).
- **Ask Yang:** omit them, or supply the text plus where it should live.

### 5. Shape of the build (keep it small)

- Change `src/components/SatelliteModal.tsx` only, plus at most one small presentational component. Read through the
  adapter's existing payload: `PositioningPortfolio` already carries characteristics, allocation and holdings.
- No new fetch and no new route; a lambda change is out of scope ("no need to generate additional data").
- Keep the sibling shape: HeroDialog, details left, content right. Same family as ModelPortfolioModal and EtfModal.
- SatelliteModal's header comment still says "the adapter's MEASURE blend over the constituents' live positioning
  (blend A)". Since POSN_ASTTAX TO-V7-1 the adapter reads served `characteristics.json`. Correct the comment while
  editing the file.
- No PDF or print export unless Yang asks for it. The CHECK in the brief is "open each popup and see the factsheet".

### 6. Landing law (client-facing)

CW is a partner firm, and Positioning's Satellites mode is visible to CW. Under the Portal rule (CLAUDE.md @fcdfc34843):
- DEV is written only by `.tools/portal-merge-forward.sh cand/dell1/<slug>` on an approved row, and a client-facing
  change **waits for Andrew's approval**;
- PROD waits on his word as well.

Plan for that approval in the 1-2 week window. Validate on the dev build (port 5174) as a CW login, using the read-only
walker (`/ui-walk`), across all 9 satellites. Grade on the 9 popups, not one.

### 7. Related open item

Satellite returns use the same `compute_returns` as MDPF_SECHIST FWD-9. On a day a holding's own market was closed,
that function currently blanks every window for that holding (`etf_positioning_gold.py:994`), which lowers return
coverage that day. The rule change is with `1.0.0_SA_CTO~DELL1`
(`org/tier1_exec/4.0.0_SA_CRO/deliverables/CLOSED_MARKET_ASOF_RESEARCH_MDPF_SECHIST_FWD9_20261014.md`). J359 should not
work around it.

## Not read

- The two PDFs (finding 1).
- The live CW render of the current modal.
- `capabilitiesFor('satellites')` source lines (cited from the adapter's comment at `satelliteAdapter.ts:449-450`).
