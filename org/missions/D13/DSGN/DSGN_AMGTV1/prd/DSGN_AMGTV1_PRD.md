# DSGN_AMGTV1 -- Security Analysis page redesign: the AMGT Security Analysis page rebuilt from the estate's own cards, modals and charts

```json
{
 "project": "DSGN_AMGTV1",
 "directive": "D13",
 "fabric": "site-z",
 "prd_version": "v0.6",
 "step": 4,
 "brief_ref": "docs/briefs/dsgn-amgtv1-security-analysis-frontend-brief-20260928.md@08eefaac9d",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7", "FWD-8", "FWD-9", "FWD-10", "FWD-11", "FWD-12", "FWD-13", "FWD-14", "FWD-15", "FWD-16", "FWD-17", "FWD-18", "FWD-19", "FWD-20", "FWD-21", "FWD-22", "FWD-23", "FWD-24"],
 "status": "DRAFT"
}
```

**Author:** `1.0.0_SA_CTO~Z` (L4), 2026-09-29. **Brief:** `4.0.0_SA_CRO~Z`, from Andrew's walk memo, his 12 snapshots and a
signed-in `/ui-walk` (record `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260928_223xZ_DSGN_AMGTV1_WALK_MEMO_UIWALK_FIXTURE_PORT_BRIEF.md`).
**Registered** @`2f8568fd32` (D13, fabric site-z, the named per-member exception). **COO:** `2.0.0_SA_COO~D` on site Z.
**CVO:** `3.0.0_SA_CVO~Z`. **ENDPOINT note (v0.2, outside the signed section):** the ENDPOINT below is the endpoint
record @`3d7fc6695e` verbatim except FWD-3's ACCEPT, which dropped "The form is Andrew's call (fork F1)." because F1 was
ruled @`ac5433b35b` before landing (`3.0.0_SA_CVO~Z` condition 1). **Endpoint** confirmed by Andrew's word of 2026-09-29 ~02:2xZ (record
`ANDREW_DIRECT_20260929_022xZ_NOTHING_WAITS_ON_ANDREW_SELF_DRIVE_RESOLVES_CALLS.md`, call 2); forks F1-F5 ruled @`ac5433b35b`.

## ENDPOINT (step 2, /endpoint --forward)

Landed verbatim from `org/tier1_exec/1.0.0_SA_CTO/deliverables/DSGN_AMGTV1_ENDPOINT_FORWARD_20260928.md` @`3d7fc6695e`.

```
  FWD-1  A portfolio manager opens Security Analysis, finds Valero in today's
         Trending x Price ranking by its name, opens it, and reads it as cards --
         end to end on the live product
         (v0.6: the ranking is FWD-22's bars; the list form is retired by
         FWD-2's v0.6 restatement)
         DONE WHEN  EXERCISED -- one live walk, signed in with a real account,
                    on real data, ending in Valero's Recommendation card open
         ACCEPT     The PM picks Valero out of the list by its company name, reads
                    its header as four cards and opens the Financials one, opens the
                    Thesis and reads it as three cards under the main chart, then
                    opens the Recommendation and can say whose view it is and which
                    document each citation comes from. Any step fed by sample data
                    instead of the real thing fails the outcome.
         SOURCE     brief O1 (:54-62); memo M6, M7, M9, M14

  FWD-2  A PM can tell who every ranked name is, how it is classified and how
         far it moved
         DONE WHEN  EXERCISED -- all four lead-panel lists walked and read
         ACCEPT     In all four lists every row shows the company's name, its ticker,
                    Opal's own asset class, sub-asset class and sector, the period
                    figure and how many places it moved since the last run -- laid
                    out like the Positioning page's holdings breakdown. No row names
                    a company by a code the PM would have to look up.
         SOURCE     brief O2 (:64-69); M2, M4, M6, M14
         v0.6 RESTATED (CTO~Z placement ruling R5; Andrew 2026-10-01 03:4xZ
                    "No other views for chatter, no other views for price"): the
                    list form is RETIRED. The same identity -- name, ticker, asset
                    class, sub-asset class, sector, the period figure and places
                    moved -- is read on each FWD-21 bubble and each FWD-22 bar (its
                    label, or one hover away). DONE WHEN: the walk reads every
                    identity field on 3 bubbles and 3 bars; no mark names a company
                    by a code alone.

  FWD-3  A PM can read how names moved over time without untangling a knot of
         lines
         DONE WHEN  EXERCISED -- the history view walked with ten or more names
         ACCEPT     With ten or more names, the dates do not overlap, each line is
                    labelled by company name, there is one legend, and the PM can pick
                    out one name and follow it.
         SOURCE     brief O3 (:71-75); M2, M3, M5, M14
         RETIRED    v0.6 (CTO~Z placement rulings R5 + R10). Andrew 2026-10-01
                    03:4xZ rejected the "lines with normalized y-axis percentile
                    ranks" view: chatter is always the bubble chart (FWD-21), price
                    always horizontal bars (FWD-22), no other views. The line-history
                    view, the per-row sparkline and the highlight chart (fork F1) are
                    removed, not built. Not graded.

  FWD-4  A PM reads a security's headline figures as four cards, each opening
         to the detail
         DONE WHEN  EXERCISED -- walked on names in more than one currency
         ACCEPT     The header holds no more than four cards -- Price, Financials,
                    Market features, Trading technicals -- each leading with one
                    figure and opening a window with the rest, and every money figure
                    is shown in the company's own currency.
         SOURCE     brief O4 (:77-82); M7

  FWD-5  A PM reads a covered company's story along a timeline
         DONE WHEN  EXERCISED -- walked on a covered name with harvested coverage
         ACCEPT     For a company we cover, a dated line shows its articles, events
                    and headlines, with a word cloud from its own coverage; the
                    firm's own harvested publications come first. A company that has
                    coverage never reads "none".
         SOURCE     brief O5 (:84-88); M8, M15

  FWD-6  A PM reads the Thesis as three cards and can trust where each line
         came from
         DONE WHEN  EXERCISED -- walked on a name whose thesis is drafted
         ACCEPT     Investment thesis, Risks and Recommendation sit as three cards
                    under the main chart; each opens a window with its sentences and
                    their evidence; every citation names its document in words; and
                    the Recommendation says whose view it is -- the team's stated
                    position, never a line lifted from a filing and passed off as one.
         SOURCE     brief O6 (:90-95); M9

  FWD-7  A PM sees who runs the company, for every covered name
         DONE WHEN  EXERCISED -- walked on a name whose filing lists no officers
         ACCEPT     The management tab shows the company's officers and says where
                    the list came from, even when the company's filing has no
                    officer section.
         SOURCE     brief O7 (:97-100); M10

  FWD-8  A PM reads the comparable companies as a clean table
         DONE WHEN  EXERCISED -- walked on three names
         ACCEPT     The peers table keeps what Andrew liked, shows readable tickers,
                    explains missing columns once and neatly, and shows no internal
                    system text.
         SOURCE     brief O8 (:102-106); M11

  FWD-9  A PM reads the Model sheet in plain line names and knows why a line is
         missing
         DONE WHEN  EXERCISED -- walked on a name with missing lines
         ACCEPT     Every line is named in words, not a data vendor's code, and every
                    missing line says in one sentence whether the data is missing or
                    the page cannot yet show it.
         SOURCE     brief O9 (:108-112); M12

  FWD-10 A PM reads Posture as a verdict with its reasons, or as an honest empty
         state
         DONE WHEN  EXERCISED -- walked on one name with a call and one without
         ACCEPT     A call reads as a verdict card with numbered reasons that each
                    open to more; no call reads as a designed empty state with its
                    date -- never a paragraph of machine reasoning.
         SOURCE     brief O10 (:114-117); M13

  FWD-11 A reviewer cannot tell this page from the firm's other finished pages
         DONE WHEN  EXERCISED -- a side-by-side read against Market, Positioning
                    and Philosophy
         ACCEPT     Put beside the Market, Positioning and Philosophy pages, the cards,
                    windows, charts, empty states and footers are the same pieces;
                    every footer reads as a time and a source; and no raw code, id or
                    storage path shows anywhere on the page.
         SOURCE     brief O11 (:119-124); M4, M13, M14

  ===== v0.4, 2026-09-30 -- FWD-12..FWD-20 RE-HOMED FROM AMGT_RESAPP ========
  Each outcome is AMGT_RESAPP's FWD-21..FWD-29 carried whole, minus only the
  forms this endpoint replaces. Where the two differ, this endpoint's form
  (FWD-4's four cards, FWD-6's three cards, FWD-10's verdict card) wins.

  FWD-12 The page has ONE dark band and every other container is a white
         hairline panel
         DONE WHEN  EXERCISED -- the rendered Security state reads
                    bandContainersTopLevel == 1, the identity header is that
                    band, and the tab panels are white hairline panels
         ACCEPT     A PM reads the thesis without scrolling past more dark bands.
         SOURCE     AMGT_RESAPP FWD-21; Andrew's F1 word (Security mode: the
                    identity header is the ONE band)
  FWD-13 A PM never parses a raw float and can still dispute any headline
         figure
         DONE WHEN  EXERCISED -- every figure on the four header cards carries
                    its units and tabular numerals, its tooltip carries the
                    mnemonic and the full-precision value verbatim, and price,
                    market cap, net debt, enterprise value, beta and short
                    interest each sit on one named card
         ACCEPT     No 161867780096.00003 anywhere; every figure traceable to
                    its field.
         SOURCE     AMGT_RESAPP FWD-22
  FWD-14 Every drafted sentence keeps its evidence, folded until asked for
         DONE WHEN  EXERCISED -- in the Thesis windows each sentence shows its
                    PASS face and its passage count; opening it reveals the
                    passage and accession line FROM THE DOM; and a census of
                    passages carried in a native title= tooltip reads ZERO in
                    the same capture as its positive control (the application
                    route, the tab's label present, a NON-ZERO count of nodes
                    scanned)
         ACCEPT     The verbatim gate (AMGT-rj-2) is preserved BY CONSTRUCTION.
         SOURCE     AMGT_RESAPP FWD-23 and its addendum
  FWD-15 The Model sheet reads as a table and a refusal as ONE line per row
         DONE WHEN  EXERCISED -- the fiscal table renders as a white heatmap
                    panel with tabular numerals; a REFUSED row renders one status
                    icon and one navy sentence spanning the row; ABSENT rows
                    fold into a single footnote naming them
         ACCEPT     A refusal is readable once, not ten times.
         SOURCE     AMGT_RESAPP FWD-24
  FWD-16 The comparable set shows the columns that EXIST, and the absent ones
         are openable
         DONE WHEN  EXERCISED -- the table renders the PRESENT columns only; an
                    "Absent columns (N)" disclosure lists each with its registry
                    reason; the basis is a status chip with the test statement
                    one hover away
         ACCEPT     A PM reads the real columns instead of scanning ABSENT ones.
         SOURCE     AMGT_RESAPP FWD-25
  FWD-17 The Posture verdict card carries its comparable, and status colour
         never carries meaning as text
         DONE WHEN  EXERCISED -- the verdict card shows the comparable beside
                    the verdict; each numbered reason has its cites folded; an
                    UNRESOLVED cite renders a status.warning ICON beside navy
                    text and NOT amber text
         ACCEPT     C6 holds on a light ground.
         SOURCE     AMGT_RESAPP FWD-26
  FWD-18 The Lead Panel's controls read as the Dashboard's controls do
         DONE WHEN  EXERCISED -- Movement and Subject render as segmented
                    controls whose active state is WEIGHT AND RULE, the
                    generation and resolution lines sit in a "Source:" footer,
                    and the rendered state reads purpleFills == 0 in Universe
                    mode and == 1 (Refresh) in Security mode
         ACCEPT     One purple action per view (C8).
         SOURCE     AMGT_RESAPP FWD-27
         v0.6       Movement (Trending / Breakout) renders Trending only through
                    the Friday demo (CTO~Z ruling R6: Breakout x Chatter served empty
                    16 days); the Movement control is absent, not disabled, and
                    returns when Breakout x Chatter serves. Subject stays.
  FWD-19 Every panel renders one of the four DESIGNED states when empty
         DONE WHEN  EXERCISED -- PanelEmpty, PanelLoading, PanelError and
                    PanelNoPermission from src/ui/components/states each captured
                    at least once across the six states, on every panel
         ACCEPT     An empty panel looks designed, as /market's already does.
         SOURCE     AMGT_RESAPP FWD-28; C12
  FWD-20 The contract's render check PASSES, and CAN FAIL
         DONE WHEN  EXERCISED -- portal/scripts/ui-smoke.mjs writes, for each of
                    the six states, a PNG at 1440 and a DOM JSON reading
                    bandContainersTopLevel == 1, fonts == {Lato}, weights within
                    {400,700}, no size below 11, radii within {2,3,4,pill},
                    shadows == 0 outside the focus ring, lowContrastChars == 0,
                    purpleFills per FWD-18 and the four states present; the
                    drafting, tabs and posture harnesses green; AND the
                    same instrument FAILS a planted page on each clause (one
                    violation per clause, each beside a clean control), and
                    FAILS the real pre-redesign page (portal 8fa7abde) on the
                    band clause; AND the six PNGs are read by a person, a
                    rejection citing its clause
         ACCEPT     A JSON PASS WITHOUT THE PNG READ BY A PERSON IS CARE, NOT A
                    CONTROL; FWD-11's side-by-side read is the person's arm.
         SOURCE     AMGT_RESAPP FWD-29 (no DSGN owner before v0.4)

  ===== v0.6, 2026-10-01 -- THE FRIDAY DEMO (FWD-21..FWD-24) ==============
  Andrew 2026-10-01 03:4xZ (verbatim in 4.0.0_SA_CRO~Z/deliverables/
  ANDREW_DIRECT_20261001_034xZ_AMGT_SECURITY_ANALYSIS_DEMO_FRIDAY.md); on
  PROD by 09:00 ET 2026-10-02 (@4cff5b352d). Brief O1-O4 (@1391c2f70a).
  Every served field these read is AMGT_RESAPP's, per the shared CONTRACT
  org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_FRIDAY_DEMO_20261001/
  CONTRACT.md.

  FWD-21 A PM sees what is being talked about, by period, as bubbles
         DONE WHEN  EXERCISED -- one live walk on the portal build: the chatter
                    view renders ONE bubble per security, its area sized by the
                    collected count for that security in the selected calendar
                    month, read from the served monthly route (CONTRACT section
                    1); a cursor steps this month, M-1, M-2 and back, and at least
                    one bubble's size changes between two steps on served data;
                    the size is labelled "collected", never "market chatter"
         ACCEPT     The PM says which names were collected most this month, steps
                    back two months and says what changed. Chatter has this ONE
                    form: no list, line or toggle to another chatter view exists
                    on the page.
         SOURCE     brief O1; CTO~Z rulings R4, R5

  FWD-22 A PM sees what moved in price, ranked, as horizontal bars
         DONE WHEN  EXERCISED -- the price view renders horizontal bars, longest
                    first and descending vertically, one per security, the
                    measure the 30-day return, signed, in percent, printed as
                    served (the page never rescales a served unit); a DOM census
                    of the price view reads 0 line charts and 0 view toggles
         ACCEPT     The PM reads the biggest mover first and the sign of each
                    move. Price has this ONE form.
         SOURCE     brief O2; CTO~Z rulings R3, R5

  FWD-23 The Lead Panel and the selected-name header look like the rest of
         the portal
         DONE WHEN  EXERCISED -- the panel's header and the selected-name header
                    are built from the /philosophy fixture-card face
                    (PhilosophyPillars, extracted per C-ESTATE-FIXTURES with its
                    before/after render), its colours come from lib/chartColors.ts
                    (0 hard-coded hex in the panel's chart files), its controls are
                    the shared Segmented control (0 hand-built controls), and no
                    visible text reads an internal name ("Lead Panel")
         ACCEPT     Put beside /philosophy, a reviewer reads the same card family;
                    a person reads the PNGs and cites a clause for any rejection.
         SOURCE     brief O3; Andrew "It was a big improvement to start bringing in
                    those /philosophy fixture cards, need to keep going with that"

  FWD-24 A PM opens a name and reads its numbers, never an empty or
         mislabelled cell
         DONE WHEN  EXERCISED -- on 3 names walked, the selected-name header
                    shows the chatter and price readings of the latest served
                    trading day the payload carries (the page computes no date);
                    the cell labelled "Breakout (price)" reads the breakout row;
                    every unit prints as served; "places moved" prints wherever
                    served; a DOM census reads 0 "not served" for a field the
                    payload carries, beside a positive control (a field the
                    payload truly lacks renders its designed empty state)
         ACCEPT     No cell on the demo thread reads empty because of a date,
                    label or unit convention.
         SOURCE     brief O4, IV.3; CONTRACT sections 2-3
```

## CONTRACTS

**C-PRESENTATION-ONLY.** This project owns the PRESENTATION of `portal/src/pages/SecurityAnalysis/**`. Every figure,
name, classification, rank change, currency, citation and verdict on the page is a field of a served payload
(`lib/research/api/scoped_amgt.py`, the scoped AMGT API). **A field the page needs and the payload lacks is an ASK to its
owning project, never a page-side computation** (F5; brief Part II): the page does not rank, classify, convert a currency,
derive a rank change or choose whose recommendation a sentence is. A value the payload does not carry renders as a
designed empty state naming, in plain words, what is missing and which team fills it (for example "the research
team's pack does not include this yet") -- never a project code, serial or storage path (FWD-11; v0.2 wording,
`3.0.0_SA_CVO~Z` condition 2).

**C-ESTATE-FIXTURES.** Cards, modals, charts, empty states and footers are the estate's own pieces (brief IV.3, IV.5):
`HeroDialog` + `DialogStamp`, `Panel` / `PanelHeader` / `PanelFooter` / `SmartPanelFooter`, `ChartLegend`, `DataTooltip`,
`Segmented`, `TopicCloud`, `ModelTiltTimeSeriesView`, the palette in `lib/chartColors.ts`. **A needed piece that lives
inline in another page is EXTRACTED into a shared module, and that page renders byte-identically before and after**
(a before/after render is the extraction's criterion). Nothing is forked. `portal/DESIGN.md` C1-C14 and the colour law
govern.

**C-FORKS (ruled @`ac5433b35b`).** F1 ~~both a per-row rank/price sparkline and a highlight chart (the ported
`ModelTiltTimeSeriesView` with legend toggles)~~ RETIRED v0.6 with FWD-3 (chatter = bubbles, price = bars, no other
views); F2 classification from `etf-classifications` only; F3 the officer
fallback order filing -> dossier -> Bloomberg -> Lusha -> search, every vendor leg on Andrew's per-use word, the page
naming each roster's source; F4 Opal Data Harvest only on the timeline in round 1; F5 this project owns presentation,
AMGT_RESAPP keeps the payloads.

**C-CASE-UNIT (v0.3, AMGT_CORPUS round-9 analysis ruling 1).** A team case figure carries `unit_as_written` (the symbol the
team typed) and a `currency` that may be null. The page prints the team's figure with the team's symbol and "as written in
the team's pack", and never beside the Price tile as if in the listing's currency (on 5 of 8 names read, the symbol is not
the listing currency). FWD-4's "every money figure in the company's own currency" binds served figures, not a pack's typed
symbol.

**C-FRIDAY (v0.6).** The shared CONTRACT `org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_FRIDAY_DEMO_20261001/CONTRACT.md`
binds this project with one writer per shared surface: (1) the monthly collected-count route is AMGT_RESAPP's; the page
consumes its shape and, until it is served, builds FWD-21 against fixtures of that exact shape, never against a page-side
aggregate; (2) units: the page prints a served unit as served and never rescales (breakout arrives in percent); (3) dates:
the server falls back to the latest served ranking and the page never computes or guesses a date. A defect on a shared
surface is fixed by its writer only; a page-side fix of a served value is refused at the cut.

**C-ASKS (owned elsewhere; this project renders them when served):**

| ask | owner | state at writing |
|---|---|---|
| rows carry the company name and `classification {asset_class, sub_asset_class, sector}` from `etf-classifications`, joined server-side | AMGT_RESAPP (API join) + POSN's writer (the AMGT rows, a served move under a never-widen pair) | open |
| rows carry `rank_change` against the previous complete generation | AMGT_RESAPP | open |
| every money figure carries its currency | AMGT_RESAPP | open |
| the timeline routes answer with data | AMGT_HARVST | **met** 2026-09-29 (combined deploy, a-2 AC1 PASS for 992_HK_Equity) |
| the dossier's team recommendation, management passage and description are served | AMGT_CORPUS | open |
| exec roster re-run with its fallback chain; posture re-run; peers dedupe and identity | AMGT_RESAPP | open |
| white-ground `PanelHeader` / `PanelFooter` variants | DSGN_REBRND (laptop) | open, cross-fabric: WAITED ON, never driven here |
| monthly collected-count route per security (FWD-21) | AMGT_RESAPP | open (v0.6; CONTRACT section 1) |
| per-name latest-served date fallback; breakout in percent; 95-name price universe (FWD-22, FWD-24) | AMGT_RESAPP | open (v0.6) |

## THE THREAD (FWD-1) -- round 1 builds it end to end

One person: a portfolio manager on the asset management team. One journey, coarse grain, live, default window. A hop
fed by a fixture fails FWD-1; the live trace is the COO's drain act, signed in with a real account on the portal build
(local 5174 or DEV).

1. Real login -> the portal session.
2. `/security-analysis` -> the Trending x Price list from the served lead panel.
3. The row reads **Valero** by company name (hop 3 renders the name the payload carries; where it does not, the row reads
   the served identity and the trace records the name ask open -- FWD-1 does not pass on a ticker).
4. Open Valero -> the header as **four cards** (C-ESTATE-FIXTURES), the Financials card opening its modal.
5. The Thesis tab -> **three cards** under the principal chart.
6. The Recommendation card -> whose view it is and the document each citation names. **If the dossier route (AMGT_CORPUS)
   is not served by the drain, the card renders the live state with its reason, FWD-1 stays NOT_REALIZED, and that route
   is round 2's first enrichment input** -- never a fixture.

Chains: lead panel (2-3), header (4), thesis (5-6). A build cell carries at most THREE mechanical criteria; repo-wide
hygiene runs at the drain. The round-1 analysis ends in the enrichment list.

## ENRICHMENT BACKLOG (off the thread, in the brief's order)

**v0.6, FIRST:** the Friday demo (PROD by 09:00 ET 2026-10-02; freeze Thu 18:00 ET): FWD-23 and the removal half of
FWD-21/FWD-22 (toggle, line chart, list view) need no route and start at once; FWD-24's page fixes next; FWD-21 builds on
fixtures of the CONTRACT's route shape and wires to the live route when AMGT_RESAPP serves it. Then the backlog below.

FWD-2 (classified rows, rank change -- v0.6 on the bubbles and bars), ~~FWD-3 (sparklines + highlight chart)~~ RETIRED v0.6, FWD-4 (all
four cards and their modals, currency per figure), FWD-5 (the timeline spine and per-security word cloud), FWD-6 (Thesis
modals with evidence), FWD-7 (exec roster with source), FWD-8 (peers table), FWD-9 (plain line names, missing-line
reasons), FWD-10 (posture verdict card / empty state), FWD-11 (the side-by-side review). The register
`docs/briefs/dsgn-amgtv1-findings-20260928.json` (42 findings, AMV-01..42) is the decomposition's input; each finding is
graded against its own acceptance line. FWD-12..FWD-20 (v0.4) enter at round 12; FWD-20 is the instrument
the others are graded by, so it leads.

## PATHS (the write surface)

**Owned:** `portal/src/pages/SecurityAnalysis/**` and its tests. **Extended by a cell naming every other reader:** new
shared modules extracted from `pages/Positioning/tabs/HoldingsTab.tsx` (`ClassifiedSecurityTable`), the Philosophy card
row (`pages/CapitalMarketAssumptions/components/PhilosophyPillars.tsx`), and chart pieces under `components/` and
`ui/components/`. **Read and copied from, never edited except by an extraction cell:** `/positioning`, `/philosophy`,
`/market`. **Never:** the scoped API, any producer, any gold table, any vendor call, `portal/src/api/**` beyond adding a
client call for a route that is already served.

## FIXTURES AND EVIDENCE

Each candidate is walked with `/ui-walk --route /security-analysis --security <names>` and its screenshots are read by a
person; register findings are graded against their acceptance lines; `design:bands`, `raw-code` and `format:*` read zero
hits on the touched surfaces; every extraction ships before/after renders of its source page. The CVO grades JUDGMENT
criteria at L9 on the PNGs, citing the contract clause.

## PROVENANCE AND AMENDMENT HISTORY

- v0.6 (2026-10-01, `1.0.0_SA_CTO~Z`): the Friday demo. Andrew 2026-10-01 03:4xZ (CRO~Z order + brief @1391c2f70a) and the
  CTO~Z placement `CTO_PLACEMENT_20261001_043xZ_AMGT_FRIDAY_DEMO_RESTRUCTURE.md` @e18d3a4e6a, rulings R3-R6 and R10.
  FWD-21..FWD-24 added (bubbles + month cursor; ranked bars; /philosophy card family; populated, correctly labelled
  header). FWD-3 RETIRED and fork F1 retired with it. FWD-2 restated (identity on the marks; the list form retired);
  FWD-1 reads "ranking" for "list"; FWD-18 renders Trending only through the demo. C-FRIDAY added (the shared CONTRACT).
  ENDPOINT change: both halves re-open (v3.19); the ratified-text half to `3.0.0_SA_CVO~Z`, the brief half accepted as
  CRO-authored under proportionate sign-off.
- v0.5 (2026-09-30, `1.0.0_SA_CTO~Z`): FWD-20's control clause re-stated. COO~D measured at the round-12 cut (msg 27092) that the
  pre-redesign build already passes every style clause except the band (AMGT_RESAPP rounds 37-38 fixed that chrome first), so "the
  pre-redesign page FAILS each clause" could not be met. The clause's purpose is CAN-FAIL: a planted page fails each clause beside a
  clean control, and the real pre-redesign page fails the band clause. This is an ENDPOINT change, so the ratified half re-opens to
  `3.0.0_SA_CVO~Z`.
- v0.4 (2026-09-30, `1.0.0_SA_CTO~Z`): FWD-12..FWD-20 appended, re-homed from AMGT_RESAPP FWD-21..FWD-29 under that
  project's round-51 ruling 4, from the round-52 map `PAGE_FWD_MAP_ROUND52.json` @`8aa352afc4`. The outcomes are carried whole,
  minus only the forms this endpoint replaces (AMGT_RESAPP PRD v0.29, s.C.1). ENDPOINT change: the ratified half re-opens to
  `3.0.0_SA_CVO~Z`. They enter the enrichment backlog at round 12, because round 11 is already cut and mid-round the spec is
  frozen.
- v0.2 (2026-09-29, `1.0.0_SA_CTO~Z`): two wording conditions from `3.0.0_SA_CVO~Z`'s ratified-text SIGN @`5a222f83d6`
  (review `DSGN_AMGTV1_L4R_RATIFIED_TEXT_REVIEW_20260929_Z_SIGN.md` @`82fb40d877`): the ENDPOINT header states FWD-3's dropped
  fork sentence; C-PRESENTATION-ONLY names an empty state's owner in words. No ENDPOINT change; no half re-opens.
- v0.1 (2026-09-29, `1.0.0_SA_CTO~Z`): ENDPOINT landed from @`3d7fc6695e`, confirmed by Andrew's ~02:2xZ word; CONTRACTS from
  the brief's Parts II, IV and VII and the F1-F5 ruling @`ac5433b35b`.

## SURFACE MANIFEST

WRITES: `portal/src/pages/SecurityAnalysis/**` (render + tests); new shared modules extracted from `HoldingsTab.tsx`,
`PhilosophyPillars.tsx` and the market-performance chart modals, each with a before/after render of its source page.
EXTENDS (by a cell naming every other consumer): `portal/src/components/**`, `portal/src/ui/components/**`,
`portal/src/lib/chartColors.ts`. READS: the scoped AMGT API payloads (`/thesis`, `/overlay`, `/peers`, the lead panel, the
two timeline routes), `portal/DESIGN.md`, the reference pages `/market`, `/positioning`, `/philosophy`. NEVER: the scoped
API or any producer, gold, the classifier table, any vendor call.
