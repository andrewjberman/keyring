# Investor Reporting page -- Product Manager walk and design concepts

Author: `4.0.0_SA_CRO~F`, 2026-09-24 ~04:5xZ. Andrew-direct carrier:
`ANDREW_DIRECT_20260924_042xZ_IRPT_PAGE_PM_WALK_AND_DESIGN_CONCEPTS.md` (same folder).
Read from source at portal DEV HEAD (`portal/src/pages/InvestorReporting/**`, `portal/src/api/endpoints/investor-reporting.ts`),
the ten consumed contracts (`contracts/index.ts`), the P/M/Y lane `INTERFACES.md`/`STATUS.md` under
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_{P,M,Y}/`, and the four reference pages Andrew named.
Dev server on 5175 was DOWN at read time, so this is a code walk, not a screenshot walk; every defect below
names the file that renders it.

Status: DRAFT for Andrew's layout iteration. The brief follows once the component layout is agreed.

---

## 1. The PM walk -- what a first-time user hits, top to bottom

Legend: **[ID]** identity leakage (a hash/id/code where a name belongs) · **[VOC]** internal vocabulary on a client-facing surface ·
**[STR]** structural / layout · **[MISS]** something the page should have and does not · **[SYS]** off the portal design system.

### 1.1 Header and client selector (`index.tsx`, `header/ClientSearch.tsx`, `header/FirmDropdown.tsx`, `header/ScopeSummary.tsx`)

| # | Defect | Where |
|---|---|---|
| H1 | **[STR] The client picker is a 288px combobox (`w-72`) that pages 25 rows at a time with a text link "Load more clients" under it.** It is the ONLY way to reach a client. There is no browsable client list, no table, no recent/favourites. | `ClientSearch.tsx:135-176`, `limit: 25`, `loadMore()` |
| H2 | **[STR] Two different firm controls for the same job.** Internal users get a raw HTML `<select aria-label="Select Firm">` listing tenant tokens; firm users get `FirmDropdown` (the shared `PageSurfaceControl`). Model Portfolios uses ONE `PageSurfaceControl` labelled "Select Partner:". | `index.tsx:133-141` |
| H3 | **[ID] Account chips are raw account ids** (`A-0001`, `acc_d486fc9455d6b2aa18e13af1`) rendered as buttons after a selection. The contract carries `displayName` + `maskedDiscriminator` for accounts; the chips do not use them. | `ClientSearch.tsx:184-205` |
| H4 | **[VOC] Search row description is the raw `kind` token** ("relationship", "account") or a capability-gap code (`view-holdings -- REASON_CODE`). | `ClientSearch.tsx:161-167` |
| H5 | **[VOC] The context strip is an entitlement debug panel**: "Permitted accounts 3 of 3 in scope (3 permitted)", "Scope match: exact", "Directory as of", "Cohort: supervision: opal-supervised", "Not fully projected 0 of 1". None of this is what an advisor wants above a client report. | `ScopeSummary.tsx:94-150` |
| H6 | **[VOC] Global-mode prompt**: "Choose a client to confirm its firm and accounts in Resolution." | `index.tsx:154` |
| H7 | **[MISS] No client identity card.** Every reference page opens with who/what/how-much: Advisor Intelligence L3 opens with `ConsolidatedOverviewPanel` (Total AUA tile + metric tiles + as-of). Here the header has a search box and a debug strip and nothing that says "The Smith Household, 3 accounts, $2.4M, as of 09-09". | -- |
| H8 | **[STR] The page description is a sentence fragment** ("Client-scoped performance, holdings, analysis and export.") and the tab strip has three tabs labelled Reporting / Analysis / Holdings -- "Reporting" inside "Investor Reporting" is tautological; Andrew's word for it is **Performance**. | `TabShell.tsx:18-22` |

### 1.2 Performance tab (`tabs/reporting/*`, `render/performance/*`)

| # | Defect | Where |
|---|---|---|
| P1 | **[VOC] A status band sits on top of every report** printing the state token, "Business date 2026-09-09" and the public reason code VERBATIM (`REQUESTED_WINDOW_ANSWERED`, `TARGET_BLEND_MODEL_REVISION_UNNAMED`). | `AnswerStatus.tsx` |
| P2 | **[STR] Period controls card** holds presets + a custom range + Refresh + a permanently disabled Export, then prints three date sentences ("Requested ... Answered ... The source answered a different window"). | `PeriodControls.tsx` |
| P3 | **[MISS] The summary has no benchmark, no spread, no value change.** Three cards: Beginning value, Ending value, Period return. Beginning/Ending are "UNAVAILABLE no-household-value-fact" on today's payloads; period return is unavailable unless a summary return's window equals the answered window, else the code `no-summary-return-for-answered-window` prints as the value. | `Summary.tsx` |
| P4 | **[MISS] The cumulative chart is one line.** No benchmark overlay, no period shading, no hover value. | `CumulativeReturnChart.tsx` |
| P5 | **[STR] Period results is a 3-column table** (Period / Window / Return) and benchmarks are a SECOND table below it with a "Reference" column that is the opaque `benchmarkId`. The Model Portfolios Benchmark tab shows the same facts as ONE heatmap: periods across, portfolio vs benchmark rows, net spread cells. | `PeriodResults.tsx` |
| P6 | **[ID] Accounts table prints `accountId` as a "Reference" column**, `String(account.covered)` ("true"/"false") as a cell, and every period return as an inline text run. | `AccountDetail.tsx` |
| P7 | **[ID] "Methods and sources" is 16 label/value rows** including Producer, Tenant, Source coordinate, Source revision, Report revision, Entitlement revision, Report schema, Ingested, Generated. This is provenance, which belongs in a collapsed footer / "About this data" popover, not the body. | `tabs/reporting/MethodAndSources.tsx` |
| P8 | **[SYS] The tab body is styled by `render/print.css`** (`.ir-page`), the PDF stylesheet, so the screen layout is a print layout. Nothing on the tab uses `Panel`/`PanelHeader`/`SmartPanelFooter`. | `ReportingTab.tsx:66` |
| P9 | **[STR] `FirmAttribution` chip floats alone in a right-aligned row** above the summary, three times across the tabs. | `ReportingTab.tsx`, `HoldingsTab.tsx`, `AnalysisTab.tsx` |

### 1.3 Holdings tab (`tabs/holdings/*`)

| # | Defect | Where |
|---|---|---|
| L1 | **[MISS] There is no holdings list.** The contract has leaf `security` nodes (`securityId` = `TICKER:SPY`, amount, pctOfTotal, classification) and the wire carries `unique_position_count`, but nothing renders a flat security table. The only table is the per-drill `SliceTable` of the CURRENT node's children. | `DrillTree.tsx`, `SliceTable.tsx` |
| L2 | **[VOC] `SliceTable` has nine columns: Node, Basis, Amount, Denominator, % of parent, % of total, Supervision, Advisory, Provenance.** "Basis" prints `observed-custody`; "Denominator" prints `500,000`; "Provenance" prints a source coordinate string. Three of nine columns are producer bookkeeping. | `SliceTable.tsx:116-128` |
| L3 | **[STR] The L0 strip is the shared `CategoryViewTree` fed with EMPTY children**, so its hover detail and "View breakdown" dialog are vacuous here, while on Model Portfolios the same component is the hero card. | `DrillTree.tsx:127-148` (`mdpfResultFromSnapshot`) |
| L4 | **[SYS] The donut is a default recharts pie** with the library `<Legend />` and `<Tooltip />`, sitting in a 2-column grid beside the nine-column table. Colours key off canonical MODEL names, so any non-model slice (a security, a sleeve) falls back to slate grey. | `DrillTree.tsx:283-310`, `colorForSlice` |
| L5 | **[VOC] Qualification prose above the body**: "Classification unknown for 3 of 12 holdings nodes -- their supervision and advisory partitions are shown as withheld, not as a classification." | `HoldingsTab.tsx:70-93` |
| L6 | **[MISS] Summary strip has no Models / SMAs / Client split**, which is the L0 Andrew ratified for this product (CONTRACT.md Holdings taxonomy amendment) and the exact hero `CategoryViewTree` already draws for Model Portfolios. | `HoldingsSummary.tsx` |
| L7 | **[MISS] No asset class, sector, quantity, price on any node** -- the contract does not carry them yet. M's `INTERFACES.md` says security-reference / dated-price enrichment is PARKED in that lane. This is a data ask, recorded in section 4. | `contracts/index.ts` HoldingsNode |

### 1.4 Analysis tab (`tabs/analysis/*`)

This is the hash wall. The tab stacks, in this order, ELEVEN white cards for what is one flow:

| # | Card (in DOM order) | What it prints |
|---|---|---|
| A1 | `ProspectComposer` -- "Prospect portfolio" | file input, a USD checkbox, price date, reference notional, Review portfolio button, then a 100-row preview table, title, Prepared for, Generate Overview |
| A2 | `OwnedRequestHistory` -- "Your analysis requests" | a button list "Open req_<uuid> · revision 3", Next page, then `ProspectJobStatus` printing "Request <uuid>" and a Check status button |
| A3 | `GenerateComposer` -- "Generate" | eight numbered fields: Client `<clientId>`, Accounts as raw ids with checkboxes, Holdings snapshot `sx-2026-09-09 as of ...`, Comparisons as a FREE-TEXT "catalog key" input, Title, Prepared for, Variant select, and **"Idempotency key: <uuid> -- a transport retry keeps it; any changed input mints a new one"** |
| A4 | `VariantSelector` | variant, primary portfolio (= account ids joined), comparisons, input date, settings as a bullet list |
| A5 | `RevisionIdentity` -- "Revision identity" | SEVEN id rows: request, revision, ingestion-gate, destination-policy, stage, release-policy, release-state, plus "N correction(s) carried" |
| A6 | `RequestList` -- "Analysis requests" | `requestRevision` as a link, "stage: gated", "release: held", and the sections inline when released |
| A7 | `InputReview` -- "Inferred inputs" | 7-column holdings table where EVERY row carries a "Correct account grouping" input+button, and every finding adds another |
| A8 | `StageDisplay` | "Stage: Gated · Release: Held · Release policy revision: <rev> · READY -- 2 days old (REASON_CODE)" |
| A9 | `VendorPdfPreview` -- "Vendor preview -- not the Opal report" | "Artifact: <artifactRef> · Route: /api/scoped/... · Pages: 12" |
| A10 | disabled Export button | -- |
| A11 | `NativeSections` (inside A6) | per section: SUPPORTED/UNSUPPORTED badge, MODELED badge, a 5-column values table, "Vendor attribution: <coordinate>", then `ExtractionCoverage` prose ("12 values included: 10 dated and 2 without a stated date. 0 field or column records were not located...") |

Structural reading: **two composers for one job** (custody-scoped vs uploaded CSV) stacked as separate cards; **identity shown four times** (A2, A3 footer, A5, A8); **the report itself (A11) is buried inside a list row (A6)**. The real flow is five steps and one artifact: choose input → review holdings → set comparisons/title/recipient → generate and wait → read/export the report. That is a stepper with a history rail, not eleven cards.

### 1.5 Cross-cutting

| # | Defect |
|---|---|
| X1 | **[SYS] Nothing on the page uses the portal panel system** (`Panel`, `PanelHeader` with title/helpText/actions, `PanelContent`, `SmartPanelFooter` for the source line). Every card is a hand-rolled `rounded-lg border border-slate-200 bg-white p-6`. The other four pages are built entirely from the panel system. |
| X2 | **[SYS] Ink is `text-slate-*` throughout**; DESIGN.md's ink is navy `#163372` on white panels with `#C4CBDB` hairlines, one purple action per page, radii 2/3/4px. |
| X3 | **[STR] Export is disabled in two places** (PeriodControls, AnalysisTab) with no page-level action bar. |
| X4 | **[STR] Every tab is a single column of stacked cards.** Mobile (390px) was fixed cell by cell (FE-s-18) but desktop (1440px) was never laid out: no two-column splits, no side rail, no frozen header. |
| X5 | **[VOC] Every reason code, state token and envelope word reaches the screen verbatim** because the FE rules were "print the producer's own vocabulary". Correct for evidence; wrong for a client-facing page. The concepts below keep the facts and move the tokens to a disclosure layer (footer, popover, "About this data"). |

---

## 2. Design concepts (`/draw` house style)

### 2.0 The reference map -- which existing page teaches which tab

The **"reference page ↔ Investor Reporting surface"** mapping is exact and deliberate:

```
  ┌───────────────────────────┬────────────────────────────────────────────────────────────────┐
  │  Investor Reporting       │  Existing portal surface it should borrow from                 │
  ├───────────────────────────┼────────────────────────────────────────────────────────────────┤
  │ Header: firm control      │ ModelPortfolios.tsx:1265 PageHeaderCleanBadge + PageSurfaceCtrl │
  │                           │   "Select Partner:" dropdown (ONE control, both principal kinds)│
  │ Header: client identity   │ AdvisorIntelligence ConsolidatedOverviewPanel Row 1             │
  │                           │   (Total AUA tile + metric tiles + data_as_of)                  │
  │ Header: client picker     │ AdvisorIntelligence L2 ClientListPanel (a LIST you browse) +    │
  │                           │   the existing Combobox kept as type-ahead only                 │
  │ Holdings L0               │ components/CategoryViewTree.tsx hero card: Models / SMAs /      │
  │                           │   Client, filled pie, nested tiles, View breakdown dialog       │
  │ Holdings allocation       │ Positioning/panels/PositioningSummary.tsx frozen-pane bars +    │
  │                           │   expandable classification matrix                              │
  │ Holdings security list    │ Positioning/tabs/HoldingsTab.tsx treemap + dense table          │
  │                           │   (ticker, name, sub-asset class, sector, weight, returns)      │
  │ Performance summary       │ AdvisorIntelligence CanonicalBookView L3 overview tiles +       │
  │                           │   window toggle (QTD/YTD/1Y/3Y/SI/custom)                       │
  │ Performance vs benchmark  │ ModelPortfolios Benchmark tab: BenchmarkHeatmap (periods across,│
  │                           │   spread cells, Gross/Net toggle) + ReturnVolatilityScatter     │
  │ Performance by account    │ AdvisorIntelligence FeeSummaryPanel accounts table (one row per │
  │                           │   account, click = L4 modal)                                    │
  │ Analysis                  │ no sibling -- a 5-step stepper with a history rail (below)      │
  └───────────────────────────┴────────────────────────────────────────────────────────────────┘
```

### 2.1 HEADER -- one identity card, one picker, one firm control

```
INVESTOR REPORTING HEADER -- who am I looking at, over what, as of when

1. The header plane -- how a selection becomes a scoped page

   FIRM CONTROL          CLIENT PICKER                 IDENTITY CARD                 TABS
   ────────────          ─────────────                 ─────────────                 ────
  ┌────────────────┐    ┌──────────────────────────┐   ┌──────────────────────────┐
  │ Select Firm:   │    │ [Search clients...     ▾]│   │ Smith Household           │  Performance
  │ [49 Financial▾]│───►│  type-ahead (existing    │──►│ 49 Financial · Relationship│  Holdings
  │ (Global for    │    │  Combobox, 25/page)      │   │ 3 of 3 accounts  $2.41M   │  Analysis
  │  Opal users)   │    │  -- OR --                │   │ as of 2026-09-09          │
  └────────────────┘    │ [Browse ▸] opens a       │   │ ┌─────────┬─────────┬───┐ │  ┌────────┐
     ONE control, both  │  right-hand DRAWER:      │   │ │Taxable  │IRA      │...│ │  │ Export │
     principal kinds    │  scrollable client LIST, │   │ │••4417   │••0093   │   │ │  └────────┘
     (PageSurfaceCtrl,  │  grouped by firm, with   │   │ │$1.2M    │$0.9M    │   │ │   page-level
     as on Model        │  name · masked tail ·    │   │ └─────────┴─────────┴───┘ │   action, one
     Portfolios)        │  kind · status · accts   │   │  account chips = NAME +    │   purple button
                        │  (replaces "Load more")  │   │  masked tail, toggle to    │
                        └──────────────────────────┘   │  narrow scope              │
                                                       └──────────────────────────┘
                                                        data: DirectoryEntry.displayName,
                                                        maskedDiscriminator, kind, termination;
                                                        ResolvedScope.permittedAccountIds,
                                                        verifiedRequestFirm.displayName;
                                                        HoldingsSnapshot.custodyTotalAmount
                                                        (the $ tile; absent -> "value pending")

   DISCLOSURE LAYER (collapsed by default, one link "About this scope"):
     scope match · directory as-of · entitlement revision · cohort facts · unprojected grant
     = everything ScopeSummary.tsx prints today, moved OFF the header into a popover.

2. The query plane -- how an advisor reaches a client
    YOU (advisor)
        │  "show me the Smith household"
        ▼
   ┌────────────────┐  type 3 letters, or open Browse and scroll the firm's list
   │ CLIENT PICKER  │
   └───────┬────────┘
           ▼  POST selections {scope_kind, scope_ids}  -> sel_<64hex> (server-accepted)
   ┌────────────────┐
   │ IDENTITY CARD  │  fills from ResolvedScope + DirectoryEntry; $ tile from the holdings total
   └───────┬────────┘
           ▼
   ANSWER on screen: "Smith Household · 49 Financial · 3 accounts · $2.41M · as of 2026-09-09"
   and the three tabs unlock.
```

Story: the header answers WHO, HOW MUCH, AS OF WHEN before a single tab is opened; the entitlement bookkeeping is still one click away for support, but it is no longer the first thing a client sees over their shoulder.

### 2.2 HOLDINGS -- L0 hero, allocation bars, then the security list

```
HOLDINGS TAB -- what the client owns, three ways down

1. The holdings plane -- how one HoldingsSnapshot becomes three views

   L0 HERO (CategoryViewTree)          L1 ALLOCATION (PositioningSummary pattern)      L2 SECURITY LIST (Positioning HoldingsTab pattern)
   ─────────────────────────           ────────────────────────────────────────         ─────────────────────────────────────────────
  ┌───────────────────────────┐        ┌──────────────────────────────────────┐        ┌──────────────────────────────────────────────┐
  │ TOTAL $2,410,000  ◕ pie   │        │ Models      ████████████░░░░  62%    │        │ [Treemap: size = weight, colour = model/    │
  │ ┌────────┬───────┬──────┐ │  click │ SMAs        ████░░░░░░░░░░░░  18%    │  click │  sleeve; hover = ticker · name · $ · %]     │
  │ │Models  │SMAs   │Client│ │ ─────► │ Client      ████░░░░░░░░░░░░  20%    │ ─────► ├──────────────────────────────────────────────┤
  │ │$1.49M  │$0.43M │$0.48M│ │  tile  │  ▸ expand: per-account matrix        │  bar   │ Ticker  Name          Sleeve   Wt%   Value   │
  │ │62%     │18%    │20%   │ │        │    (frozen header row, scroll body)  │        │ SPY     SPDR S&P 500  Primary  25.0  $602k   │
  │ └────────┴───────┴──────┘ │        │    Account · Models · SMAs · Client  │        │ AGG     iShares Core  Primary  14.2  $342k   │
  │ hover = L1 detail;        │        │    Taxable   $0.9M  $0.2M  $0.1M     │        │ ...     (sortable; filter by sleeve/account) │
  │ click = View breakdown    │        │    IRA       $0.6M  $0.2M  $0.1M     │        │ CASH    Cash          --       3.1   $75k    │
  │ (L2 dialog: Primary/      │        └──────────────────────────────────────┘        │──────────────────────────────────────────────│
  │  Custom, strategy SMAs,   │                                                        │ 12 positions · dedup'd · as of 2026-09-09    │
  │  Supervised/Unsupervised) │                                                        │ Source: SmartX (custody) · SmartX (models)   │
  └───────────────────────────┘                                                        └──────────────────────────────────────────────┘
   data: root children by      data: account nodes x model/sleeve children               data: kind='security' leaf nodes: displayName,
   displayName, amount,         (amount, pctOfParent); coverage.uncovered                 securityId (TICKER:SPY), amount, pctOfTotal,
   pctOfTotal; the exact        accounts listed by NAME with reason                       parent sleeve/model; custody_totals.
   Models/SMAs/Client L0 the                                                              unique_position_count; sourceSetRevision
   CONTRACT ratifies                                                                      NOT YET IN CONTRACT: name, asset class,
                                                                                          sector, quantity, price  (section 4 ask)

   DISCLOSURE LAYER (footer, one line + popover): business date vs observed time · source revisions ·
     classification gaps ("3 of 12 nodes unclassified") · basis (observed vs target) · provenance.
     = HoldingsQualification + SliceTable's Basis/Denominator/Provenance columns, moved off the body.

2. The query plane -- how an advisor answers "what's in the IRA?"
    YOU (advisor)
        │  "what does the IRA hold, and how much of it is in the Primary model?"
        ▼
   L0 hero: hover Models -> "Primary $1.1M · Custom $0.39M"; click -> breakdown dialog
        ▼
   L1 bars: expand -> IRA row: Models $0.6M · SMAs $0.2M · Client $0.1M
        ▼
   L2 list: filter Account = IRA -> 7 positions, sorted by weight
   ANSWER on screen: "IRA · $0.9M · 7 positions · 67% Primary model · SPY 28%, AGG 15%, ..."
```

Story: the same three levels Andrew specified for Model Portfolios (Models / SMAs / Client, then Primary/Custom, then the securities) now read top-down on a client, and the security list -- the thing that does not exist today -- is the Positioning Holdings table over the snapshot's leaf nodes.

### 2.3 PERFORMANCE -- window, headline, chart vs benchmark, heatmap, accounts

```
PERFORMANCE TAB -- how did the client do, against what, by account

1. The performance plane -- how one PerformanceReport becomes the page

   WINDOW + HEADLINE                         CHART                                  BENCHMARK HEATMAP                      ACCOUNTS
   ─────────────────                         ─────                                  ─────────────────                      ────────
  ┌────────────────────────────────────────────────────────────────────────────┐
  │ [QTD] [YTD] [1Y] [3Y] [SI] [Custom ▾]        Net ○ Gross ●   as of 2026-09-09│  ONE control row (AdvisorIntelligence rfsWindow
  │  answered 2026-01-02 -> 2026-09-09 (i)                        [ Export PDF ] │  toggle + Model Portfolios Gross/Net toggle);
  ├──────────────┬──────────────┬──────────────┬──────────────────────────────┤  the "(i)" holds requested-vs-answered detail
  │ Period return│ vs benchmark │ Ending value │ Beginning value              │
  │  +7.32%      │  +1.10%      │  $2.41M      │  $2.18M                      │  data: summaryReturns[window == actualDates],
  │  YTD, net    │ 60/40 blend  │  09-09       │  01-02                       │  benchmarks[0].periodReturns (spread = FE
  │              │              │  (or "not    │  (or "not supplied")         │  difference of two supplied facts -- flag for
  │              │              │   supplied") │                              │  CTO: today the FE computes nothing)
  ├──────────────┴──────────────┴──────────────┴──────────────────────────────┤
  │ Cumulative return, portfolio ── vs benchmark ┄┄  (area, hover = date/value) │  data: dailyCumulative; benchmark series is
  │      ╭──╮   ╭────╮                                                          │  NOT in contract (section 4 ask); until then
  │ ╭────╯  ╰───╯    ╰──╮  ╭──                                                  │  the chart is single-series with period shading
  ├─────────────────────────────────────────────────────────────────────────────┤
  │ Returns by period          QTD     YTD      1Y      3Y      SI               │  BenchmarkHeatmap pattern: rows = portfolio,
  │ Portfolio (net)           +2.11%  +7.32%  +10.41%   --      +21.0%           │  benchmark, spread; columns = periods; a cell
  │ Benchmark                 +1.80%  +6.22%   +9.10%  +4.1%   +18.9%            │  the source did not supply reads "--" with a
  │ Spread                    +0.31%  +1.10%   +1.31%   n/a    +2.1%             │  hover reason (NOT_ENOUGH_HISTORY), never 0
  ├─────────────────────────────────────────────────────────────────────────────┤
  │ Accounts                     Ending value   QTD     YTD     1Y    Covered    │  FeeSummaryPanel accounts-table pattern:
  │ Taxable ••4417               $1.20M        +2.0%   +6.9%  +9.8%   yes       │  displayName + maskedDiscriminator, NEVER the
  │ IRA ••0093                   $0.90M        +2.3%   +7.9%  +11.2%  yes       │  accountId; an uncovered account is a ROW
  │ Roth ••7710                  --             --      --      --    no: source│  with its reason, not a footnote list
  │                                                            not mapped       │
  └─────────────────────────────────────────────────────────────────────────────┘
   FOOTER (SmartPanelFooter, one line): "Time-weighted, net of fees, accrual basis, USD · Source: Black Diamond
   (rev bd-2026-09-09) · report rev-49f-000091"  -> popover holds the other 12 MethodAndSources rows.

2. The query plane -- how an advisor answers "how are we doing this year?"
    YOU (advisor)
        │  "YTD, net, versus the benchmark, and which account lagged?"
        ▼
   click [YTD] -> headline tiles re-fill; heatmap column YTD highlights
        ▼
   read Spread row (+1.10%), scan Accounts YTD column -> Taxable +6.9% is the laggard
        ▼
   click Taxable row -> L4 account modal (AdvisorIntelligence pattern) with its own cumulative line
   ANSWER on screen: "YTD +7.32% net vs +6.22% benchmark (+1.10%); Taxable lagged at +6.9%"
```

Story: the tab stops being a printed page on a screen and becomes the Model Portfolios Benchmark tab over ONE client: a window, a headline, a heatmap with spreads, and accounts as rows. Method and lineage survive, in the footer where every other page keeps them.

### 2.4 ANALYSIS -- a five-step flow with a history rail, not eleven cards

```
ANALYSIS TAB -- turn a set of holdings into a YCharts-backed report

1. The analysis plane -- the flow is an upload, so the screen is a stepper

   HISTORY RAIL (left, 30%)          STEPPER (right, 70%)  -- one step visible at a time, others collapsed to a row
   ────────────────────────          ──────────────────────────────────────────────────────────────────────────────
  ┌──────────────────────────┐      ┌───────────────────────────────────────────────────────────────────────────────┐
  │ Your reports        [+New]│      │ ① INPUT   ─── ② REVIEW ─── ③ SETTINGS ─── ④ GENERATE ─── ⑤ REPORT            │
  │──────────────────────────│      ├───────────────────────────────────────────────────────────────────────────────┤
  │ ● Smith Overview          │      │ ① INPUT  (choose ONE source; the two composers become two radio cards)        │
  │   Released · 09-22 · v3   │      │  ┌────────────────────────────┐  ┌────────────────────────────────────────┐  │
  │ ◐ Smith vs 60/40          │      │  │ ◉ Selected client holdings │  │ ○ Upload a portfolio                    │  │
  │   Generating · 09-24      │      │  │   Smith Household, 3 accts │  │   CSV/XLSX template  [Choose file]      │  │
  │ ○ Prospect: Jones         │      │  │   snapshot as of 09-09     │  │   amounts are USD ☑ · price date [ ]    │  │
  │   Needs review · 09-23    │      │  │   [x] Taxable  [x] IRA     │  │   reference notional [ ]                │  │
  │                           │      │  └────────────────────────────┘  └────────────────────────────────────────┘  │
  │ filter: all · released ·  │      │                                                                [Continue ►]   │
  │ in progress · needs review│      ├───────────────────────────────────────────────────────────────────────────────┤
  │                           │      │ ② REVIEW  "12 holdings normalized · 2 need attention"                         │
  │ data: OwnedRequestHistory │      │   Holding        Source value   Qty    Amount    Unit    Status              │
  │ page (title, stage,       │      │   SPDR S&P 500   25,000.00 USD   --   $25,000   currency ok                  │
  │ releaseState, businessAsOf│      │   "ACME FUND X"  1,200 sh        1,200  --      shares  ▲ unresolved [fix ▾]│  │
  │ -> a STATUS DOT, a title, │      │   ... (only flagged rows carry a control; the per-row "Correct account       │
  │ a date; the request id    │      │        grouping" input is gone -- grouping is a column with an edit icon)    │
  │ lives in the row's        │      ├───────────────────────────────────────────────────────────────────────────────┤
  │ tooltip/copy button)      │      │ ③ SETTINGS  Title [Smith Household Overview ] · Prepared for [J. Smith      ] │
  │                           │      │   Compare against (0-5): [ + add ▾ ] -> picker over the CATALOGUE when Y     │
  │                           │      │   ships it; until then the same free-text key, labelled honestly.           │
  │                           │      │   Variant: Overview (auto from 0 comparisons)                                 │
  │                           │      ├───────────────────────────────────────────────────────────────────────────────┤
  │                           │      │ ④ GENERATE  [ Generate report ]  ->  progress row: Received ▸ Gated ▸        │
  │                           │      │   Normalized ▸ Generating ▸ Validated ▸ Released   (StageDisplay as a rail;  │
  │                           │      │   polls StatusEnvelope; the request id sits behind a "copy id" icon)         │
  │                           │      ├───────────────────────────────────────────────────────────────────────────────┤
  │                           │      │ ⑤ REPORT  Smith Household Overview · Released 09-22 · v3        [Export PDF] │
  │                           │      │   ┌ Certified ─────────────────────────────────────────────────────────────┐ │
  │                           │      │   │ 1. Asset allocation     2. Risk        3. Fees (MODELED)   4. Income   │ │
  │                           │      │   │   [values table]          [values]       [values + disclosure]         │ │
  │                           │      │   └───────────────────────────────────────────────────────────────────────┘ │
  │                           │      │   [ View vendor PDF ]  (protectedArtifact.downloadRoute, labelled preview) │
  │                           │      │   footer: "Extraction certified · 12 of 12 values confirmed · coverage:    │
  │                           │      │   complete for the field inventory (i)"  -> popover = ExtractionCoverage  │
  └──────────────────────────┘      └───────────────────────────────────────────────────────────────────────────────┘
   DISCLOSURE LAYER: request id, revision, ingestion-gate, destination-policy, release-policy revisions,
   idempotency key, artifactRef, contentHash = ONE "Details" popover on step ⑤ and on each rail row.
   (RevisionIdentity + StageDisplay + VendorPdfPreview + the composer's idempotency paragraph, off the body.)

2. The query plane -- how an advisor makes a prospect report
    YOU (advisor)
        │  "run an overview on this prospect's spreadsheet"
        ▼
   ① Upload -> ② two rows flagged, fix one, accept one -> ③ title + recipient -> ④ Generate
        ▼  (rail row appears at once as "Generating"; the advisor can leave the tab)
   ⑤ rail row flips to Released -> click -> report sections + Export PDF
   ANSWER on screen: "Jones Prospect Overview · Released · 4 sections certified · [Export PDF]"
```

Story: the advisor sees ONE thing at a time and always knows which step they are on; every identifier the fabric needs for evidence is still on the page, one click down, and the report -- the reason the tab exists -- is the last step, not a row inside a list inside a card.

---

## 3. Layout decisions for Andrew (the iteration list)

These are the calls that change the component set. Recommendation first.

1. **Client picker: type-ahead PLUS a browse drawer** (recommended), vs a full-width client table on the page above the tabs (Advisor Intelligence L2 style). The drawer keeps the identity card as the header's centre of mass.
2. **Identity card $ tile source**: the holdings custody total (recommended; it is the one number the CONTRACT calls "unique custody total"), vs the performance ending value. They can differ by basis; pick one and label it.
3. **Performance heatmap orientation**: periods across, portfolio/benchmark/spread down (recommended, matches Model Portfolios), vs periods down.
4. **Spread cell**: computed on the FE from two supplied facts (recommended; it is subtraction, and Model Portfolios already does it), vs waiting for the producer to supply it. The FE rules today forbid ANY derivation; this needs a CTO word either way.
5. **Holdings L2**: treemap + table (recommended, Positioning's exact pattern), vs table only until asset class / sector arrive.
6. **Analysis history rail**: left 30% rail (recommended), vs a "History" sub-tab.
7. **Tab names**: Performance / Holdings / Analysis in that order (recommended), vs today's Reporting / Analysis / Holdings.
8. **Export**: one page-level Export button in the header that exports the ACTIVE tab (recommended), vs per-tab buttons.

## 4. Data the concepts need that the wire does not carry today (asks, not blockers)

| Need | Tab | Who | Today |
|---|---|---|---|
| Security name, asset class, sector, quantity, price on `security` nodes | Holdings L2 | `2.0.0_SA_COO~M` (INTERFACES: "canonical security-reference/dated-price enrichment ... PARKED") | absent; L2 renders ticker + $ + % only |
| Benchmark daily series for the chart overlay | Performance | `2.0.0_SA_COO~P` | absent; `benchmarks[]` carries period returns only |
| Household beginning/ending value facts | Performance headline | `2.0.0_SA_COO~P` | optional, unsupported on current fixtures |
| Comparison catalogue (names for the "compare against" picker) | Analysis ③ | `2.0.0_SA_COO~Y` (INTERFACES: catalogue `9daa67433e`, "every currently selected comparison remains unavailable") | free-text opaque keys |
| Account display names in `DirectoryEntry` for account-kind rows | Header chips | `2.0.0_SA_COO~P` (directory/header writer) | present in contract; chips ignore it |

Everything else in sections 2.1-2.4 is a pure re-render of data already on the wire.

## 5. What this is not

Not a brief, not a task order, not a design-system ruling. The brief (`/brief-create`) is cut after Andrew's layout pass in section 3. Nothing here touches the IRPT post-slug HOLD or the P/M/Y closer contract; it is the CRO's design read, surfaced to the CTO for the "alterations" Andrew said he might bring.
