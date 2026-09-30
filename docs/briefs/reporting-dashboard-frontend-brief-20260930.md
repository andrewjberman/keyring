# BRIEF: the client reporting dashboard -- FRONTEND (the views, and how they read the backend)

- Author: `4.0.0_SA_CRO` (base), 2026-09-30. Mode: NEW (L1). Consumer: `1.0.0_SA_CTO`; execution by `2.0.0_SA_COO~D` (Andrew's seating: frontend on ~D, backend on ~P, in concert).
- Companion: `docs/briefs/reporting-dashboard-backend-brief-20260930.md` (the gold tables, the total-return method, the served files). This brief names the served files and fields it needs; it does not redefine them.
- Andrew's words, verbatim, in `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260930_06xxZ_REPORTING_DASHBOARD_TWO_BRIEFS_SCOPE_ANSWERS.md`. His request came with four screenshots of Black Diamond's client dashboard (net worth, activity summary, transactions); those show a real client household and are NOT copied into any file. His judgment of that product: "it sucks, its not good"; take the few good ideas, not the product.
- Claim classes: READ (seen in a file, by this seat or a subagent), PROPOSED (this seat's design), OPEN (needs a ruling), ABSENT (searched, scope stated).

## PART I -- THE OUTCOME TERRITORY

### The candidate thread (for FWD-1)

**F1. An advisor picks one 49 Financial account, and a chart of its daily total return appears at once; they change the start and end date and the chart and the headline number change with no wait.** One page, one account, the real data. It is the thread round 1 builds, with the backend's first served file. It is chosen because everything else on the dashboard is a view of the same daily file.

### The rest of the territory

**F2. A person reads how each asset class performed over the window,** and sees at a glance which class drove the account.
**F3. A person compares the asset-class mix at two dates and sees how it moved** (a period-over-period view, in the canonical Opal classes).
**F4. A person sees realized and unrealized gain for the window** next to income, so gain is never confused with market movement alone.
**F5. A person reads an activity summary for the window** (beginning value, contributions, withdrawals, gain or loss by kind, income, ending value) and sees the chart of value against contributions beside it.
**F6. A person browses the transactions for the window,** filters by type, sorts, and exports them.
**F7. At the deepest drawdown in the window, a person sees the topics that were trending then,** as a cloud they can read at a glance (Andrew's signature view; Cottonwood asked for it).
**F8. A person can always tell what they are looking at:** that returns are total return, before advisory fees, where the data starts, and which days could not be measured. A number the data cannot support is shown as such, never as a plausible-looking figure.
**F9. A household or client view is the same page over more accounts,** with no new concepts.

### Out of scope (Andrew, scratched)

A net-worth view, held-away accounts, liabilities. The activity summary is not paired with a net-worth toggle. Fees are not shown as a return adjustment; the returns are labelled gross.

## PART II -- WHERE THE BOUNDARY SITS

**This project owns:** the dashboard's pages and components, the reading of the served files, the presentation of coverage and method labels, and the acceptance of what a person sees.

**It relies on, and does not own:**

| Sibling | Relationship |
|---|---|
| The backend brief's project (COO~P) | The served files (`series`, `activity`, `transactions`, `manifest`, `topics`) and their fields. This brief asks for fields; that project decides the tables. |
| `IRPT_FNTEND` (D9) and the existing portal | The Investor Reporting route and its tabs (Performance, Holdings, Analysis); this dashboard extends the Performance and Holdings surfaces. |
| `DSGN_IRPTV1` (D13; `2.0.0_SA_COO~D`) | The design closer for the portal; the frontend work sits under its rules. |
| The news pipeline | The topic data behind F7; read through the backend's `topics` file. |

## PART III -- THE QUALITATIVE BAR

- **F1 passes when** Andrew picks an account and dates and sees the curve within about two seconds of the page opening (his target for the whole load), and dragging the dates afterwards makes no network request. It fails if a date change waits on the server.
- **F2, F3 pass when** a person can say in one sentence which class drove the window and how the mix moved, without reading a table.
- **F5 passes when** the summary's numbers, summed by hand from the transactions list for the same window, agree.
- **F7 passes when** the topics shown around the deepest drawdown are ones a person who lived that week recognises, and the view says plainly that they are market-wide topics, not filtered to the portfolio.
- **F8 passes when** a reader who sees a partial-history account, a day that could not be measured, or a window before the news data starts can say why, from the screen alone.

## PART IV -- THE SUBSTRATE: FINDINGS (READ, research subagents, 2026-09-30)

1. **Where the dashboard lives today:** one route, `/investor-reporting`, with three tabs (Performance, Holdings, Analysis) (`TabShell.tsx:18-26`) and a print route. The Performance tab is `portal/src/pages/InvestorReporting/tabs/reporting/` (`ReportingTab.tsx`, `PerformanceChart.tsx`, `PerformanceHeadline.tsx`, `PeriodControls.tsx`, `ReturnsHeatmap.tsx`, `AccountsTable.tsx`); the Holdings tab is `tabs/holdings/` (`HoldingsTab.tsx`, `AllocationBars.tsx`, `HoldingsTreemap.tsx`, `DrillTree.tsx`, `SecurityList.tsx`, `SliceTable.tsx`, `assetClass.ts`). The master guidance brief AD-03 removes the Allocation panel from Holdings.
2. **Performance today calls the server per window:** a one-account `GET /performance` for the selected window, plus one call per account for the picker's figure, keyed by window and account, so a period change refetches every account (`ReportingTab.tsx:450-484`). This is the pattern the served-series design removes.
3. **No transactions page, no per-class performance page, no activity summary, no separate allocation-change page** exist for this product (ABSENT: searched the InvestorReporting subtree and the route list).
4. **Charting:** `recharts ^3.7.0` (`portal/package.json:42`); `@visx/text` and `@visx/wordcloud` are also present. A topic-cloud component exists, `portal/src/components/market-performance/TopicCloud.tsx`, on `@visx/wordcloud`: input `{keyword, sentiment in [-1,1], count}`, top 20; it is a live-latest widget fed by `keyword-sentiments.json` and a 7-day window, not a historical one. It renders empty under test, so the narrative page draws terms as DOM (`PeriodInContextPage.tsx`).
5. **Colour and design law** (`portal/CLAUDE.md`, `portal/DESIGN.md`): light canvas `#F4F6FA`; white containers with a `#C4CBDB` hairline and navy ink `#163372`; one dark band per page; light text or ghost fills on the canvas or a white panel are illegal; charts keep their colour (C6); status colours and data colours are disjoint families (C6); ordered scales are single-hue ramps except the canonical duration ladder (C4, C7); every figure uses tabular numerals (C2). The colour registry is `portal/src/lib/chartColors.ts` (`ASSET_CLASS`, `PALETTE`). Verification is `/frontend-dev`: render, screenshot, read it with the clause cited. Dev builds run on port 5174 only.
6. **Asset classes and their display order** (`portal/.../holdings/assetClass.ts:21-25`, Andrew-direct 2026-09-30): Cash, Fixed Income, Equity, Structured, Alternatives, Commodities, then Other and Unclassified.
7. **The method label is wrong today:** the portal says "Time-weighted, net of fees" for a return that is price-only and carries no fees (`MethodAndSources.tsx:32-63`). The new label is a required part of this work (F8).
8. **Existing narrative page prior art:** `PeriodInContextPage.tsx` renders a packet of drawdown events with dated news evidence (a print page). It is the closest existing drawdown-and-news view; the topic view is a live, interactive cousin, not a new idea.
9. **An older frontend brief and PRD exist** (`docs/briefs/investor-reporting-ir-fe-brief-20260910.md`, `org/missions/D9/IRPT/IRPT_FNTEND/prd/IRPT_FNTEND_PRD.md` v0.10, `docs/briefs/irpt-master-guidance-brief-20260928.md` AD-01 to AD-15). This brief supplements them for the new views; where a ratified AD conflicts, the AD stands until the CTO says otherwise.

## PART V -- THE DESIGN (PROPOSED)

### 1. One page, one data load, everything computed in the browser

The page fetches, for the selected account (or household), one `series` file and one `manifest` (backend brief, section 6). The chart, the headline number, the asset-class view, the allocation comparison, the gain and activity summary, and the drawdown list are all computed in the browser from that one file, so a date change is instant and the network is silent. Transactions are the exception: paged files, loaded as the person scrolls or filters. The topics file is shared and small, fetched only when a drawdown is opened.

**Fields the frontend needs from `series` (asked of the backend; names are the backend's to fix):** date; whole-account value; daily total return; a per-day basis flag (measured, fallback, not measurable, large flow); external flow; income; per-class value and weight by day; the drawdown episode list (peak, trough, recovery dates) if the publisher computes it; method version; data as-of; the account's first data date.

### 2. The views (PROPOSED shapes; the design closer refines them)

- **Performance (F1).** A line or area chart of cumulative total return over the window, with the headline number beside it (window return, and for windows over a year an annualized figure). Controls: presets (1M, 3M, YTD, 1Y, since inception) and a custom start and end (two date fields, and a brush on the chart that drives the same fields). Every window is computed from the daily file. A benchmark overlay is a later enrichment, not in the first round. The method label "Total return, before advisory fees" sits on the chart, with the info popover naming the method version.
- **Activity summary (F5) and the value chart.** The default component: the summary block on the left (beginning value; net additions, split contributions and withdrawals; gain or loss, split market realized, market unrealized and income; ending value; fees shown as not included), and a chart on the right of account value against a step line of cumulative contributions, so a jump from a deposit reads as a deposit, not as performance. (Andrew's screenshots pair exactly this summary and chart; his earlier idea of a toggle to a net-worth view is scrapped.)
- **Asset-class performance (F2).** One row per canonical class in the fixed display order: window return of the class, its contribution to the account return, and its weight at the end. A small multiple or a sorted bar; classes sum to the account. Unclassified is shown as its own row, never folded away.
- **Allocation change (F3).** Two dates (default: window start and end, editable) shown as two stacked bars or a paired-row table with the delta in points, by class and, on expansion, by sub-class. Colours come from `chartColors.ts` `ASSET_CLASS`.
- **Gain (F4).** Realized gain, unrealized change and income for the window, as three figures and a small stacked bar; a `NO_LOTS` coverage state shows "Gain detail is not available for this account's custodian yet" with the reason, not a zero.
- **Transactions (F6).** A table with sort, a type filter, search by symbol, and export; columns date, asset, action, type, symbol, units, price, amount, custodian, fee (Andrew's list). Paged and virtualised for long windows. Opal's normalised action and type vocabulary, not the custodian's codes.
- **Topic snapshot (F7).** A marker on the chart at each material drawdown (deepest first). Clicking it opens a panel with the drawdown's dates and depth and a word cloud of the phrases trending in the window around the trough, sized by score and coloured by sentiment, with the top headlines listed under it. The panel states that topics are market-wide. A drawdown before the news data starts shows "No topic history for these dates", not an empty cloud. The existing `TopicCloud.tsx` is reused or its component pattern is; it renders as DOM under test (per the narrative page).
- **Household and client (F9).** The same page with an account picker that offers "All accounts" and each account; the aggregate is served by the backend, and the page draws it with no special case.

### 3. Coverage and honesty states (F8)

The frontend maps the backend's closed coverage vocabulary to plain sentences and shows them where the number is: partial history ("This account's data starts on <date>"); days that could not be measured (a gap marked on the chart, the window return says how many days were excluded); a day whose flow did not reconcile (drawn from the fallback, footnoted); no lot detail; source lag ("Data through <date>"). A window that starts before the first data date is clipped and says so. No state is ever hidden by an average.

### 4. Loading, errors, and the two-second target

A skeleton frame, the page's figures appear together when the file lands (no piecemeal reflow), and a file that failed to load says which account and which file. The two-second target is the whole page load to a drawn chart; measuring it is part of the round-1 acceptance (the backend brief owns the file; this brief owns the time to paint).

### 5. Print and export

The existing print route is the model: a window's chart, summary and classes print as a page; the transactions export is a file. The report PDF path already exists in IRPT and is not changed here.

## PART VI -- ROUND STRUCTURE (for the CTO's decomposition)

Round 1 builds the thread (F1): the Performance chart with custom bookends and the honest label, reading the backend's first `series` file for one 49 Financial account, with the coverage states that file can produce. Each later round enriches, in step with the backend's rounds: asset-class performance, allocation change, activity summary with the value-and-contributions chart, gains, transactions, the topic snapshot, then Inflection and Cottonwood accounts (no frontend change expected, since gold is one shape), then household and client. Verification is `/frontend-dev` screenshots of the real page on the real data at each round, read against the colour law with the clause cited; a build task order carries at most three mechanical criteria (spine v3.18).

## PART VII -- CALLS

None waits on Andrew for round 1. To settle in the PRD by the CTO and the design closer: the exact presets; whether a benchmark overlay is a first-wave or a later enrichment; whether the Holdings tab's Allocation panel (AD-03 removes it) is replaced by the allocation-change view; how the page indicates a household aggregate whose accounts have different histories.

## PART VIII -- WHAT THIS BRIEF DOES NOT CLAIM

- It opened no page and ran no screenshot; the portal structure is from a subagent's read of the tree.
- It did not read `AnalysisTab.tsx`, `TopicCloud.tsx`'s source, or the master guidance briefs in full.
- It proposes shapes and states, not pixel designs; the design closer owns those.
- It does not claim the served file has the fields listed; the backend project decides its tables, and a missing field is a change request across the two briefs.
- The two-second figure is Andrew's target, not a measurement of any page.
- The screenshots Andrew supplied were viewed for structure only; no client data from them appears here.

## REFS TO CARRY

```
BRIEF PATH        docs/briefs/reporting-dashboard-frontend-brief-20260930.md
COMPANION         docs/briefs/reporting-dashboard-backend-brief-20260930.md
PROJECT           NONE-YET (unregistered); siblings IRPT_FNTEND, DSGN_IRPTV1, the backend brief's project
PORTAL            portal/src/pages/InvestorReporting/ ; portal/src/components/market-performance/TopicCloud.tsx ; portal/src/lib/chartColors.ts ; portal/DESIGN.md
PRIOR ART         docs/briefs/investor-reporting-ir-fe-brief-20260910.md ; docs/briefs/irpt-master-guidance-brief-20260928.md
                  org/missions/D9/IRPT/IRPT_FNTEND/prd/IRPT_FNTEND_PRD.md ; portal/src/pages/InvestorReporting/render/narrative/PeriodInContextPage.tsx
MEASURED AT       2026-09-30 by research subagents (READ from files)
```
