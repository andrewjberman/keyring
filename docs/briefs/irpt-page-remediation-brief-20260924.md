# INVESTOR REPORTING PAGE REMEDIATION -- the advisor-facing re-render of the header and the three tabs

**Author:** `4.0.0_SA_CRO~F`. **Date:** 2026-09-24 ~05:2xZ. **Mode:** `--midstream` (IRPT_FNTEND / IRPT_BCKEND are in flight).
**Commissioned:** Andrew-direct 2026-09-24 ~04:2xZ at this terminal, verbatim in
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260924_042xZ_IRPT_PAGE_PM_WALK_AND_DESIGN_CONCEPTS.md`
(*"walk the 'Investor Reporting' page and identify all the points that need to be fixed ... /draw some design concepts ...
then you write a brief on exactly what needs to happen to realize that"*), and his layout ruling ~05:0xZ, verbatim
*"recs approved go ahaerdf"*, in `.../ANDREW_DIRECT_20260924_050xZ_IRPT_LAYOUT_RECS_APPROVED.md`.
**Grounding:** the PM walk + four concept drawings, `org/tier1_exec/4.0.0_SA_CRO/deliverables/IRPT_PAGE_PM_WALK_AND_DESIGN_CONCEPTS_20260924.md`
@`aaaf13178c` (cited below as CONCEPTS s.N), and `1.0.0_SA_CTO` ruling IRPT-DESIGN-RECON-CALLS-20260924 (msg 100194).
**Consumer:** `1.0.0_SA_CTO`, `/endpoint --forward` at L2. Every claim an outcome can be cut from sits under a numbered heading.

---

## PART 0 -- How the blind constraint was honoured, and where it bent

**Honoured.** This brief was written without reading `org/missions/D9/IRPT/IRPT_FNTEND/task-orders/`,
`IRPT_BCKEND/task-orders/`, either `decompositions/` folder, or either `project.json`'s `phase` / `blocking` fields.
The served reality was read directly: every file under `portal/src/pages/InvestorReporting/` at portal DEV HEAD, the
API client and the ten consumed contracts, and the four reference pages Andrew named. The existing PRD's purpose,
endpoint and F-row table (`IRPT_FNTEND_PRD.md` v0.10, lines 1-104) were read as the skill permits.

**Where it bent -- three leaks, named.**
1. The P/M/Y closer-contract pack (`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`,
   `COO_P/M/Y.md`) and each lane's `INTERFACES.md` / `STATUS.md` were read to answer Andrew's *"look at the data that is
   being queued up for it"*. Those documents describe in-flight work. What entered this brief from them is ONLY the data
   shape (which wire members exist, which are optional and unfilled, which are PARKED) -- Part IV. No outcome below
   ratifies a P/M/Y milestone; the milestones are in Part VI, marked not outcome-bearing.
2. The CTO's ruling 100194 arrived mid-write and names in-flight artifacts (the `display` member, `valuation_facts`, the
   DEV consolidation). Its rulings are carried as constraints (Part V), its sequencing as status (Part VI).
3. The component files carry their own cell ids in comments (FE-s-N, W1-S7 ...). They were read for what renders, not
   for what was ordered; no FE-s cell text was opened.

**"Unchanged" is the finding.** The eight outcomes the PRD carries (FWD-1, 3, 4, 5, 6, 8, 11, 12) still describe the right
product. FWD-12 -- *"the Investor Reporting screens look and behave like the rest of the Opal portal, so an advisor who
already uses the portal needs no re-learning"* -- is EXACTLY the outcome the served page fails. The failure is in
DECOMPOSITION, not DIRECTION: the cells built each contract's EVIDENCE surface (print the producer's state token, reason
code, revision and provenance verbatim, derive nothing) and no cell ever built the ADVISOR surface on top of it. So the
territory below is not a new endpoint; it is the advisor surface FWD-1/3/4/5/12 always promised, stated at the grain a
decomposition cannot skip. Whether that is an amendment to the existing FWD set or new ids is the CTO's L2 call.

---

## PART I -- THE OUTCOME TERRITORY

### O0 -- The candidate thread (spine v3.16: name it first; round 1 builds it end to end)

**One person, one journey, coarse grain:** an Opal internal user (Global view) opens Investor Reporting, selects the
Cottonwood account `acc_d486fc9455d6b2aa18e13af1` (the account P and M already share as their first live milestone --
Part VI), and READS, without touching anything else: the identity card (client name, firm, account count, custody total,
as-of), the Performance headline for the default window (YTD, net) with its benchmark spread, the Holdings L0
Models / SMAs / Client split, and the security list. One firm, one account, default window, no export, no analysis.
That thread is the page's spine; every outcome below enriches it.

### O1 -- An advisor identifies the client they are looking at before opening any tab

An advisor who lands on the page with a client selected can say, from the header alone, WHO (client display name, firm,
relationship or account kind), HOW MUCH (the holdings unique custody total), OVER WHAT (the permitted accounts by display
name and masked tail, toggleable to narrow the scope), and AS OF WHEN (the business date). None of the entitlement
bookkeeping that the header prints today (scope match, directory revision, cohort tokens, unprojected grant) is on the
header; all of it is one click away in an "About this scope" disclosure. CONCEPTS s.2.1; defects H3, H5, H6, H7.

### O2 -- An advisor reaches any permitted client by browsing, not only by typing

An advisor who does not know how a client is spelled opens a browse drawer, sees the firm's clients as a scrollable list
(name, masked tail, kind, active/terminated, account count), grouped by firm in Global view, and selects one. The existing
type-ahead remains for those who know the name. The paged 25-row combobox with a "Load more clients" link is gone.
Ruled (a) on `/open-calls` card 1. CONCEPTS s.2.1; defect H1.

### O3 -- One firm control, whoever the viewer is

An Opal user and a firm user see the SAME firm control, the shared `PageSurfaceControl` dropdown the Model Portfolios
header uses, labelled with firm display names; Global (All) appears only for the Opal user. CONCEPTS s.2.1; defect H2.

### O4 -- An advisor reads the client's performance the way they read a model's on Model Portfolios

On the Performance tab (the tab is named Performance -- Andrew's word, CTO 100194), an advisor picks a window from one
control row (QTD / YTD / 1Y / 3Y / SI / custom, Net / Gross), reads a headline row (period return, spread vs benchmark,
ending value, beginning value -- each "not supplied" when the source did not supply it, never zero), a cumulative-return
chart, a returns-by-period heatmap with periods ACROSS and portfolio / benchmark / spread as rows (ruled (a), card 4),
and an accounts table with one row per account by display name and masked tail, an uncovered account being a ROW with its
reason. The spread is a server-stated fact (`spread` member, P's adapter, CTO 100194); the browser still derives nothing.
Method, lineage and revision live in a one-line footer with a popover. CONCEPTS s.2.3; defects P1-P9.

### O5 -- An advisor sees the client's holdings three ways down, including the security list that does not exist today

On the Holdings tab an advisor reads (L0) the Models / SMAs / Client hero card -- the same `CategoryViewTree` hero Model
Portfolios shows, with its total pie, nested tiles, hover detail and breakdown dialog -- then (L1) allocation bars per
category with an expandable per-account matrix (the Positioning summary pattern), then (L2) a treemap and a sortable,
filterable security table (ticker, name, sleeve, weight, value; asset class and sector when their source lands) over the
snapshot's leaf security nodes. Ruled (a) on card 3: treemap + table NOW, classification columns fill later. Basis,
denominator, provenance and classification-gap prose move to the footer disclosure. CONCEPTS s.2.2; defects L1-L7.

### O6 -- An advisor produces an analysis report through a five-step flow and always knows which step they are on

The Analysis tab is a stepper -- Input (selected client holdings OR an uploaded portfolio, as two radio cards) → Review
(normalized holdings, only flagged rows carry a control) → Settings (title, prepared-for, comparisons, variant) → Generate
(a stage rail Received → Released, polled) → Report (certified sections, vendor PDF link, Export) -- with a left rail
(ruled (a), card 5) listing the advisor's reports as status dot, title, date, and a filter. Every identifier the fabric
needs (request id, revision, ingestion-gate / destination-policy / release-policy revisions, idempotency key, artifact ref,
hash) is on the page behind ONE "Details" popover per report, never in the body. CONCEPTS s.2.4; defects A1-A11.

### O7 -- An advisor exports the tab they are looking at from one place

One page-level Export action in the header (the page's single purple action under DESIGN.md) exports the ACTIVE tab at the
revision on screen; the two disabled per-tab buttons are gone. Ruled (a) on card 6. What "export" produces is FWD-3/4/8's
existing territory and is not re-specified here. CONCEPTS s.2.1; defect X3.

### O8 -- An advisor who uses the rest of the portal recognises this page

Every panel on the page is the portal panel system (`Panel`, `PanelHeader` with title / help / actions, `PanelContent`,
`SmartPanelFooter` carrying the source line); ink is navy on white with the hairline boundary; the tab order is
Performance / Holdings / Analysis (ruled (a), card 7); desktop (1440) is laid out with the two-column and rail splits the
concepts draw, not a single column of cards. This is FWD-12 restated at the grain a cell can serve. CONCEPTS s.1.5
(X1, X2, X4), s.2.0 reference map.

### O9 -- A client looking over the advisor's shoulder never reads a state token, reason code, hash or revision

On every tab, the producer's vocabulary (envelope states, public reason codes, revisions, source coordinates, fingerprints)
is rendered ONLY inside disclosure surfaces (footer line, popover, "Details"), never in a headline, tile, table cell or
band. The facts are retained, one click down; the words are not on the body. This is the cross-cutting rule the other
outcomes each apply once. CONCEPTS s.1.5 (X5).

---

## PART II -- WHERE THE BOUNDARY SITS

**This owns:** the advisor-facing render of `portal/src/pages/InvestorReporting/**` -- header, the three tabs, the
disclosure surfaces, the page-level Export control, and conformity to `portal/DESIGN.md`. It consumes the ten contracts
in `contracts/index.ts` as they are, plus the additive members named in Part V.

**It relies on, and does not own:**
- **IRPT_BCKEND / `2.0.0_SA_COO~P`** (closer contract v1.4: shared auth / scope / directory / header selection; the
  performance adapter; common client / schema / package writer) -- the `spread` member, `display` schema edit,
  `valuation_facts` extension, benchmark daily series, household begin/end values, and the Reporting → Performance rename
  on the portal candidate after the DEV consolidation (CTO 100194).
- **`2.0.0_SA_COO~M`** -- custody publication, the Models / SMAs / Client projection, `display` fill, quantity / price /
  as-of fill.
- **`2.0.0_SA_COO~Y`** -- upload / resolution, job semantics, the comparison catalogue.
- **The asset-taxonomy SOURCE card at Andrew** (via `1.0.0_SA_CTO`) -- asset class / sector on security nodes. O5's
  classification columns are DEFERRED to it, not blocked on it.
- **DSGN_REBRND (D13)** -- the design law itself. This brief applies DESIGN.md; it does not amend it. Andrew's word: this
  is *"a pass or several now to even get it ready to be taken seriously by design team"*; the design team's pass is
  DSGN's, later.
- **The IRPT post-slug HOLD** (Andrew-direct 2026-09-22 ~15:17 ET) and the P/M/Y closer contract -- untouched;
  `1.0.0_SA_CTO` sequences this brief against them.

**Not in scope:** the PDF / print package (`render/**`, FWD-8), the narrative page, the Global-view entitlement model
(FWD-11's data half), any vendor call, any contract change beyond the additive members Part V names.

---

## PART III -- THE QUALITATIVE BAR

- An advisor reads a client's YTD return, its spread to the benchmark, and which account lagged, in one screen, where
  today they would open Black Diamond or SmartX.
- An advisor answers "what does the IRA hold" from the security list, where today the only path is a per-node drill with
  a nine-column bookkeeping table.
- A client watching the advisor's screen sees their name, their accounts and their numbers, and not one entitlement
  token, reason code or revision hash.
- A designer picking the page up for DSGN's pass finds the portal panel system and DESIGN.md roles already applied, and
  spends their pass on taste, not on removing `text-slate-*` and hand-rolled cards.
- An advisor who has used Model Portfolios, Positioning and Advisor Intelligence recognises the hero card, the frozen-pane
  matrix, the heatmap and the accounts table without explanation.
- An advisor making a prospect report knows which of five steps they are on and can leave the tab while it generates.

No number is stated here; none is known at this step.

---

## PART IV -- THE SUBSTRATE: is this in a canonical pattern?

Findings, each with what was measured (all at portal DEV HEAD, 2026-09-24 ~04:3xZ; file paths under `portal/src/`).

1. **The page is NOT on the portal panel system.** Every card in `pages/InvestorReporting/**` is a hand-rolled
   `rounded-lg border border-slate-200 bg-white`; the one `Panel` use is `ScopeSummary.tsx`. The four reference pages are
   built entirely from `ui/components/panels`. (CONCEPTS X1.)
2. **The reference components already exist and are shared:** `components/CategoryViewTree.tsx` (the Models / SMAs /
   Client hero, 1158 lines, with pie, nested tiles, breakdown dialog -- already IMPORTED by `DrillTree.tsx` but fed empty
   children); `pages/Positioning/panels/PositioningSummary.tsx` (frozen-pane bars + matrix); `pages/Positioning/tabs/HoldingsTab.tsx`
   (treemap + dense classified table); `components/BenchmarkHeatmap.tsx` + the Benchmark tab of `pages/ModelPortfolios.tsx:2268-2375`
   (Gross/Net toggle, spread cells); `pages/AdvisorIntelligence/_shared/panels/ConsolidatedOverviewPanel.tsx` (overview
   tiles) and `_shared/tabs/FeeSummaryPanel.tsx` (accounts table with window toggle); `components/ui/PageSurfaceControl.tsx`
   (the firm dropdown Model Portfolios uses and `FirmDropdown.tsx` already imports). Prior art covers every concept in
   CONCEPTS s.2 except the Analysis stepper, which has no sibling.
3. **The data for O1-O5 is on the wire today**, with these gaps: security NAME (the `display` member, ruled 100156/100172,
   M's fill built @`699bf9ed1b`, gated on P's schema edit); ASSET CLASS / SECTOR (absent; taxonomy source card at Andrew);
   QUANTITY / PRICE / AS-OF (`valuation_facts` optional member exists on `HoldingsNode`, unfilled); SPREAD (ruled: additive
   `spread` per comparison row, P's adapter); BENCHMARK DAILY SERIES and HOUSEHOLD BEGIN/END VALUES (absent / optional
   unsupported; CTO: brief items); COMPARISON CATALOGUE (Y catalogue `9daa67433e`; every selection "unavailable" today).
   Account display names and masked tails for the header chips are in `DirectoryEntry` already. (CONCEPTS s.4.)
4. **The Performance tab is styled by the PDF stylesheet.** `ReportingTab.tsx` imports `render/print.css` and wraps the
   body in `.ir-page`; the `.ir-*` classes carry no colour outside that ancestor. A screen layout driven by a print
   stylesheet is off-pattern for every other page.
5. **The design law is written and current.** `portal/DESIGN.md` (456 lines): five locked colours, navy ink, white panels
   with a `#C4CBDB` hairline, ONE purple action per page, radii 2/3/4, 40/60 splits never 50/50, four empty states. The
   page's own comments already cite its clauses (C1, C3, C6, C8, C9, C11, C12) cell by cell -- the law reached the page
   as a series of local patches, not as a layout.
6. **Mobile was fixed; desktop was never designed.** The FE-s-18 comments across `HoldingsSummary`, `SliceTable`,
   `PeriodControls`, `TabShell` each repair a 390px break; nothing lays out 1440.
7. **The FE derivation rule is real and stays.** `Summary.tsx` "IT COMPUTES NOTHING"; `SliceTable.tsx` formats a
   fraction the snapshot supplied; CTO 100194 restates it for the spread. The concepts obey it: every number drawn is a
   wire fact or a ruled additive member.

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

Named, not sequenced.

- The FE derives nothing (CTO 100194): every figure on the page is a wire fact; the spread arrives as `spread`.
- The Reporting → Performance rename lands on the portal candidate AFTER the DEV consolidation now in review, so the
  consolidation's counts stay comparable (CTO 100194).
- Portal-first order for additive members (`display`, `valuation_facts`, `spread`): contract copy in both places, schema
  edit by P, fill by the producing lane.
- The header's selection stays server-accepted (`POST selections` → `sel_<64hex>`); the drawer and chips change the
  PRESENTATION of the selection, never who may see what.
- DESIGN.md governs every colour, weight, radius and state; a departure is a DSGN matter, not this brief's.
- The disclosure surfaces (footer line, popover, Details) keep every envelope fact the evidence rules require, so no L9
  grade that reads a state, reason code or revision off the DOM loses its object -- it moves, it does not vanish.
- Asset class / sector wait on the taxonomy source card; O5 ships without those columns and adds them when the source is
  ruled.
- The comparison picker in O6 step 3 becomes a catalogue picker when Y's catalogue serves names; until then it is the
  same key entry, labelled honestly.
- Nothing here pre-empts the DEV consolidation, the D1 run or the COT `display` republish (CTO 100194); the CTO holds
  sequencing against the IRPT post-slug HOLD.

---

## PART VI -- STATUS, MARKED NOT OUTCOME-BEARING

⛔ NOT OUTCOME-BEARING. Measured 2026-09-24 ~04:3xZ unless stated.

- Dev server on 5175 was DOWN; the PM walk is a code walk. No screenshot of the served page was taken.
- Portal route `/investor-reporting` is gated `requireAdmin requireInternal requireDev` (`App.tsx:436`); it is not on the
  firm-user nav today.
- P/M/Y first live milestones (CONTRACT.md v1.4, read 04:4xZ): P -- Cottonwood BD account → provider result → immutable
  report → Reporting screen; M -- Cottonwood `acc_d486fc9455d6b2aa18e13af1` → reconciled custody → publication →
  Holdings screen (CTO review `d8173c1b9c`: 57 positions, USD 19,705,844.84); Y -- dollar template upload → YCharts
  Overview → certified report → Analysis screen. P's STATUS (02:13Z): "Product remains incomplete and LOCAL." M's STATUS:
  "No product acceptance ID is complete yet."
- CTO 100194 order: DEV consolidation candidate (P) in review → `display` acceptance → CTO review → MSTR DEV push; D1
  third run pending; COT display republish pending.
- This brief's own records: concepts @`aaaf13178c`; Andrew-direct records @`597e6848af` and @`fb0137a89f`; broadcasts
  100187-100191 and 100220-100224; push state LOCAL (this lane never pushes).

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- It did not see the page rendered. A served-page walk may add defects (or remove ones the code implies but a stylesheet
  hides); it is the first act of any cell that touches layout.
- It did not open the FE-s task orders or decompositions, so it cannot say which existing cell built which defect, nor
  whether any open order already targets one. The CTO's L2 read reconciles that.
- It does not specify component props, breakpoints, or which shared component is extended versus wrapped -- that is the
  PRD's and the decomposition's.
- It does not claim the data asks in Part IV.3 are small. `spread`, `valuation_facts` fill and `display` each cross a
  contract copy in two places; their cost is P's/M's to state.
- It does not rule on DSGN's later pass, on the print package, or on the Global-view entitlement half of FWD-11.
- It does not claim the eight existing FWDs are wrong. It claims their decomposition never reached the advisor surface,
  and offers O0-O9 as that surface's territory for the CTO to cut against them.

---

## REFS TO CARRY

```
  BRIEF PATH        docs/briefs/irpt-page-remediation-brief-20260924.md
  PROJECT           DSGN_IRPTV1 (D13) -- NONE-YET registered. Andrew-direct 2026-09-24 ~05:2xZ, verbatim: "This should be
                    its own project. Tell CTO this will be D13 project, DSGN_IRPTV1. I want a proper canonical-flow
                    issued on this from COO~D. Tell CTO that." (record .../ANDREW_DIRECT_20260924_052xZ_DSGN_IRPTV1_OWN_PROJECT_D13_COO_D.md).
                    L5/L6 issuer: 2.0.0_SA_COO~D. IRPT_FNTEND (D9) is a SIBLING this project relies on, not its home.
  EXISTING PRD      org/missions/D9/IRPT/IRPT_FNTEND/prd/IRPT_FNTEND_PRD.md (v0.10, endpoint FWD-1,3,4,5,6,8,11,12)
                    org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md (counterpart)
  ENDPOINT OF RECORD org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FWD_IRPT_FNTEND_20260910.md
  SIBLING PROJECTS  IRPT_BCKEND (P/M/Y closer contract v1.4); DSGN_REBRND (D13, the design law's owner)
  PRIOR ART         CategoryViewTree.tsx; Positioning/panels/PositioningSummary.tsx; Positioning/tabs/HoldingsTab.tsx;
                    components/BenchmarkHeatmap.tsx + ModelPortfolios.tsx Benchmark tab; AdvisorIntelligence/_shared/
                    panels/ConsolidatedOverviewPanel.tsx + tabs/FeeSummaryPanel.tsx; components/ui/PageSurfaceControl.tsx;
                    portal/DESIGN.md
  CONCEPTS + WALK   org/tier1_exec/4.0.0_SA_CRO/deliverables/IRPT_PAGE_PM_WALK_AND_DESIGN_CONCEPTS_20260924.md @aaaf13178c
  ANDREW-DIRECT     .../ANDREW_DIRECT_20260924_042xZ_IRPT_PAGE_PM_WALK_AND_DESIGN_CONCEPTS.md @597e6848af
                    .../ANDREW_DIRECT_20260924_050xZ_IRPT_LAYOUT_RECS_APPROVED.md @fb0137a89f
  CTO RULING        1.0.0_SA_CTO msg 100194, IRPT-DESIGN-RECON-CALLS-20260924, RULINGS.md batch 24
  MEASURED AT       2026-09-24 04:3xZ (code walk), 04:4xZ (P/M/Y STATUS/INTERFACES), 05:2xZ (this brief)
```
