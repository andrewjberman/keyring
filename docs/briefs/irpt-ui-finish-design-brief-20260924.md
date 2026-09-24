# Investor Reporting: finish the advisor-facing UI -- canonical colour, the three analysis variants as cards, progressive disclosure, the Opal light look

**Brief (L1), MIDSTREAM, for DSGN_IRPTV1.** Author: 4.0.0_SA_CRO. Written 2026-09-24, 4:00-5:30 PM ET.
All times US Eastern (UTC-4). Next reader: 1.0.0_SA_CTO, running `/endpoint --forward` on this brief.

**Andrew-direct at the 4.0.0_SA_CRO terminal, 2026-09-24, verbatim.**

The commission (~4:xx PM ET):
> I need you to scan all the work that the COO~D has been doing and also review my transcripts here: "C:\Users\
> AndrewBerman\Downloads\design notes". A few parts of it have been rectified by the agent, but that agent is just
> driving solo, which is good, but I sense that doing this properly, really ironing out every single opportunity here
> to finish UI, and properly issuing that through canonical-flow may be the proper mechanism to get this done. Please
> do a deep dive on it, and build out a brief to finish the UI design for Investor Reporting. Items I especially want
> to bring to attention here include the concept behind using the /philosophy cards for the variants for the
> analysis, the canonical color system for models and asset classes, progressive disclosure as a whole for UI design,
> and also being a little more creative with drawing cues from the www.opalinvest.com website and existing art as it
> pertains to opalinvest.dev and website design patterns.

The routing (minutes later):
> When you are done with this, I want you to /brief-create and issue it to CTO. CTO should then work with COO~D to
> figure out how to bring this in on DSGN_IRPTV1, thereby bringing COO~D back on a more developed track with
> /canonical-flow / /canonical-drive and run the project accordingly. Make sure this gets done.

**Andrew's design notes** are the three transcripts and 13 screenshots in `C:\Users\AndrewBerman\Downloads\design
notes\`, taken 3:09-3:41 PM ET. The transcripts are already recorded byte-identical in the repo by 2.0.0_SA_COO~D:
`org/tier1_exec/2.0.0_SA_COO~D/deliverables/ANDREW_DIRECT_20260924_194xZ_IRPT_DESIGN_NOTES/`
(`holdings_ui`, `analysis_ui`, `performance_and_general_ui` `.verbatim.txt`).

This brief quotes them by file (H = Holdings, A = Analysis, P = Performance and general) and line.

---

## PART 0 -- How the blind constraint was honoured, and where it bent

**The constraint:** a midstream brief is written blind to the project's open task-order set, so that its endpoint
does not simply ratify what is already open.

**How it was honoured.**
- The outcomes in Part I are cut from three sources:
  - Andrew's verbatim notes;
  - his screenshots;
  - the code the page runs at portal DEV `c75a0fc9`, which is what a user sees (reality, admissible).
- They are not cut from any task order or next-list.
- This seat read no DSGN_IRPTV1 task-order file.

**Where it bent. Three leaks, named so a ratifying outcome can be spotted:**
1. **The census agent read the branch.** The census of COO~D's work was done by a subagent of this seat. It read
   every round-1/2 task order, the round-1 analysis's enrichment list, and COO~D's STATUS next-list (items 2-12),
   and this seat read its report.
   - Several of Andrew's items coincide with next-list items: model colours, the drill table, the full-width models
     dialog, the client picker, the sample view, the variant cards, progressive disclosure.
   - Where they coincide, the outcome below cites Andrew's words as its source, never the next-list. The coincidence
     is convergence, not origin.
2. **This seat read `project.json`'s `phase`/`blocking` fields** earlier today for the crash-recovery brief.
3. **This seat knows the round-2 cells' names** from the CTO's control sheet.

---

## PART I -- THE OUTCOME TERRITORY

**Candidate thread (becomes the next round's FWD-1 journey).**
- **Who and what:** an Opal advisor picks Anna Thiessen (Cottonwood, account `acc_d486fc9455d6b2aa18e13af1`) from one
  search box.
- **What they see:** a short Holdings view in canonical model and asset-class colour.
- **How they drill:** Models, then one model, then that model's securities, drilled on the Securities map with the
  Positioning tooltip.
- **What they never see:** a system string, and the page never makes them scroll past a wall.
- **The standard:** real login, real data. It is the existing FWD-1 journey (Anna's account end to end) held to the
  design bar below; it is not a new journey.

### O1. An advisor finds any client with one search box, and never scrolls a list or an account wall to do it
- Source: H:11-26 ("the drop down is actually just a search bar", "a paginated list for all of the names"); A:7-13;
  screenshots 150934, 150943, 154108.
- Header: a search that types ahead; the portal's own dropdown look (H:16-17 "the same drop down design that we use
  elsewhere in the platform"); legible ink on the canvas (H:18-21).
- A browsable list of clients is paged (H:23-25), not a truncated menu. Names, masked account tails and firm tags are
  never clipped.

### O2. An advisor chooses accounts where the choice matters -- inside the view -- and the header only picks the client
- Source: A:16-30 ("Those bubbles should not be there ... account level drill downs ... should be done much deeper into
  the page where it is relevant").
- There are no account chips in the header. Narrowing to accounts happens next to the view it narrows: the Holdings
  drill, Performance's account table, the Analysis input.

### O3. An advisor sees every Opal model in its one canonical colour, the same colour it wears on Model Portfolios
- Source: H:44-50 ("We have canonical colors for the opal primary models. Ultra long term is red ... that should be
  referring to that for opal primary models"); screenshot 151107 (Ultra Long Term shown blue).
- The same model is the same colour on every Investor Reporting surface: pie, bars, legend, modal, treemap group.
  Those surfaces are Model Portfolios, Positioning and Attribution.

### O4. An advisor sees every security coloured by its canonical Opal asset class, Opal and non-Opal alike
- Source: H:35-42, H:69-73 ("gold for commodities, orange for alternatives, pink for the structured hedge, green for
  fixed income and cash and blue for equities ... there should be a canonical library"), H:87-96 (extend the ETF
  classifier "to include all the securities that are coming in through the investor reporting").
- The classes: equity, fixed income, cash, structured / hedge, commodities, alternatives.
- The surfaces: the Securities map, the securities table, the models dialog.
- A security the classifier does not yet know shows an explicit "unclassified" state, never a borrowed colour
  (H:41-42, "we will cross that bridge").

### O5. An advisor drills from total assets to models to securities, and no chart breaks at any depth
- Source: H:27-34 (the models dialog "should be full wide for the securities list"), H:63-83 (20-plus slices blow out
  the pie; "the drill down to securities is simply too much ... in the model holdings pie chart ... it makes far more
  sense to display the drill down ... in the securities map"); screenshots 151014, 151114.
- The pie and bars stop at model level.
- Security-level drill lives on the Securities map, with the Positioning page's tooltip (H:82-83 "that should be all
  copied over").
- Legends scale to many members.
- The models dialog uses its full width.

### O6. An advisor reads only client-language labels; every system fact is one deliberate click away
- Source: H:51-62 ("nobody is going to know what a node is ... strings of code ... has to be cleaned up"), A:47-56,
  A:65-69; screenshots 151107, 151114, 151124, 151134, 152625, 152633.
- No Node, Basis, Denominator or Provenance column. At most one share column (H:59-61 "percent of accounts").
- No hashes, catalog keys, idempotency keys, reason codes or "UNAVAILABLE (no-declared-route)" on any body.
- Supervision and Advisory are shown where the data exists (H:57-58: a data issue, not a design one).

### O7. An advisor sees a short page and opens detail only when they want it (progressive disclosure, page-wide)
- Source: H:96-101 ("drastically minimize the vertical size ... use toggles, use pop up modals ... only display it if
  the user is actually interested"), A:54, P:34-35.
- At rest, each tab shows its headline and one primary visual. Everything else sits behind a toggle, a tile, a dialog
  or a help tip.
- Prior art for this exists (Part IV F7).

### O8. An advisor starts an analysis by choosing one of three variant cards, and always knows where to upload and what comes next
- Source: A:57-64 ("use three cards, which will be emblematic of the three variants of Y-Charts comparison ... solo
  portfolio analysis, a portfolio versus one model ... portfolio versus multiple Opal models ... in the philosophy
  fixture card form"), A:65-69 ("where do you even upload ... users can follow along where they are inputting").
- The three cards are the variant choice.
- The upload is a designed step with a visible place and state, not a bare file input.
- The advisor follows the input step by step.

### O9. An advisor never meets request-history machinery on the Analysis tab
- Source: A:31-41 ("the analysis requests and the request history ... I would just pull those out outright ... We
  don't need to design that for them").
- The requests list and the history panels are gone from the advisor surface. Requests are still stored server-side
  (A:37-38).
- **This retires part of the ratified endpoint** (Part VI S3).

### O10. An advisor landing on a tab before choosing a client sees a sample of what it will show
- Source: P:32-37 ("some kind of sample view of the performance reporting components ... colorful, fun things that
  catch their eye ... select a client to see").
- Before a client is chosen, Performance, and by the same logic Holdings, shows illustrative components clearly
  marked as a sample, with one prompt to select a client.
- The sample never looks like client data.

### O11. The whole page reads as Opal's light, client-facing look, and every portal pattern holds on it
- Source: P:14-31 ("I like the white tabs and white panels ... our B-side look for client-facing applications ...
  philosophy page ... model portfolios page ... cards and modal pop-ups. That theme, which came from the Opal website
  ... what we should be using all over the investor reporting page"; "We only ever put source and timestamp in the
  footer bars"; tooltips; "a once-over"), and the commission's "drawing cues from the www.opalinvest.com website and
  existing art".
- Panels, cards and dialogs are the Philosophy / Model Portfolios family.
- Footers carry source and timestamp only.
- There is one tooltip look for chart data and one for help.
- There is no stray scrollbar.
- Website motifs are used where they help the advisor (Part IV F9).

---

## PART II -- WHERE THE BOUNDARY SITS

- **Owned by DSGN_IRPTV1 (2.0.0_SA_COO~D):** the advisor-facing render of `portal/src/pages/InvestorReporting/**`.
  - That includes every outcome's frontend half.
  - By Andrew's 11:31 AM ET word (record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260924_153xZ_IRPT_FRONTEND_CANDIDATES_HAND_TO_COO_D.md`),
    it also covers integration of every IRPT portal candidate onto DEV.
- **Relied on, owned elsewhere:**
  - **IRPT_BCKEND (2.0.0_SA_COO~M, Holdings):** an `asset_class` / `sub_asset_class` on every served holding (O4);
    Supervision and Advisory values (O6).
  - **IRPT_BCKEND (2.0.0_SA_COO~P, shared routes and schemas; Performance):** the served `spread` and the envelope
    fields each view reads.
  - **IRPT_BCKEND (2.0.0_SA_COO~Y, Analysis):** the upload and job semantics behind O8's steps.
  - These run on the closer path to goal-record SOUND (`org/missions/D9/IRPT/IRPT_BCKEND/ledger/ROUND_ANALYSIS.round18.md`).
  - **The one contact:** each backend seat hands portal candidates to 2.0.0_SA_COO~D.
- **Relied on: the security classifier.** Its owner is to be named by the CTO. The asset-class source is the
  `ETFClassifier` over DynamoDB (`data/black_diamond/scripts/gold/lib/etf_classifier.py:36-60`). Andrew's "expand the
  ETF classifier ... to include all the securities" (H:91-96) is a data-plane act, not a DSGN_IRPTV1 cell.
- **Relied on: portal-shared components and the design law** (`portal/src/lib/**`, `src/components/**`,
  `src/ui/**`, `portal/DESIGN.md`). DSGN_REBRND owns the law, and `DESIGN.md` C13 was ratified today.
  - A shared change, such as a searchable dropdown, a pagination control, a DESIGN.md clause for progressive
    disclosure, or fixing the model-colour lookup inside the shared library, is outside `InvestorReporting/**`.
  - DSGN_IRPTV1 may consume these. The CTO routes their writes.
- **Relied on, read-only: the reference pages.** Philosophy (`/philosophy`), Model Portfolios (`/portfolios`) and
  Positioning (`/positioning`) are copied from, never edited by this work.
- **Out of scope:**
  - the PDF / branded export package;
  - vendor calls;
  - PROD promotion, which stays on Andrew's word;
  - non-IRPT pages.

---

## PART III -- THE QUALITATIVE BAR

- Andrew reads a client's holdings without meeting a word he would have to ask an engineer about.
- The same model and the same asset class are the same colour on Investor Reporting as on Model Portfolios and
  Positioning, so an advisor moving between pages never re-learns a legend.
- At rest, a tab fits the story on one screen: detail appears only when the advisor asks for it, and the vertical
  scroll that H:97-98 complains about is gone.
- Starting an analysis feels like choosing a product card, not filling in a form.
- The graded judgment is one real signed-in run of each outcome, looked at, as the joint model with reports 2 and 3
  requires. It is never static markup or a fixture: round 2 passed every static check while the page drew black tiles.

---

## PART IV -- THE SUBSTRATE (findings, measured at portal DEV `c75a0fc9` unless marked)

- **F1. The canonical model colours exist.** `portal/src/lib/modelPortfolioColors.ts:16-133`: Ultra Long-Term
  `#ef4444` red, Long-Term blue, Intermediate green, Short amber, Ultra Short orange, 50/50 teal and lime, Fixed Income
  violet, Non-Model silver. DESIGN.md C4 (`:262-290`) locks them.
  - Investor Reporting's pie does call the library (`tabs/holdings/DrillTree.tsx:131-133`). But `getModelColor`
    (`:165-183`) falls back to a substring walk, and "Long Term" is its second key.
  - Replaying the resolver, "Opal Ultra Long Term" resolves to blue (INFERRED: the label actually served was not
    measured).
  - Direction: resolve by canonical model code (`canonicalModelCode`, `:361`), never by display label. The same class
    of defect is documented at `components/ModelPortfolioModal.tsx:148-153`.
- **F2. The canonical asset-class colours exist.** `portal/src/lib/chartColors.ts` `ASSET_CLASS` `:115-126`, plus
  `SUB_ASSET_COLORS` `:290-325` and the text-contrast helpers at `:328` and `:356`. They were ruled in POSN_ASTTAX's PRD
  section 3 (`org/missions/D4/POSN/POSN_ASTTAX/prd/POSN_ASTTAX_PRD.md:407-411`).
  - They match Andrew's scheme except **cash, which is amber there** ("amber stays Cash", `:185-188`). Andrew's H:72
  says "green for fixed income and cash" (Part VII call C1).
  - Investor Reporting has zero consumers of it.
  - **A trap:** the brand token set `design/brands/opal-capital.json:385-401` (CSS `--asset-*`, `src/index.css:197-200`)
    swaps equity and fixed income. It has no `src/` consumer and must not be adopted.
- **F3. The holdings data carries no asset class.** `tabs/holdings/HoldingsTreemap.tsx:21` says so. Today the map
  colours by a hash of the group name (`:76-87`), which is why it rendered one magenta. O4 therefore needs a served
  field (Part V).
- **F4. The Positioning treemap and tooltip are the reference.**
  - `pages/Positioning/tabs/HoldingsTab.tsx`: tile content `HoldingsCustomTreemapContent` (`:352` onward), tooltip
    `HoldingsTreemapTooltip` (`:311-336`) on the portal-wide `DataTooltip`, and a present-classes-only legend
    (`:1267-1276`).
  - The Holdings Breakdown panel with asset and sub-asset classes (`:1283-1308`, `:1337-1338`) is what Andrew calls
    "the ETF classifier" table (INFERRED).
- **F5. The Philosophy cards are reusable as the three variant cards.**
  - `pages/CapitalMarketAssumptions/components/PhilosophyPillars.tsx:183-214`: a white card, navy `GraphicPanel`, a
    large numeral, an icon, a title and tagline, and "Read more" into a `HeroDialog`. Built from
    `ui/components/graphic/HeroGraphic.tsx` (`GraphicPanel :47`, `HeroDialog :121`).
  - The variant mapping already exists: `tabs/analysis/composer.ts:56-75`. Overview has 0 comparisons (solo
    portfolio), Comparison has 1 (versus one model), Multi-Comp has 2-5 (versus multiple Opal models).
  - `HeroGraphic.tsx:16-18` limits its indigo to surfaces Andrew has confirmed. A:57-64 reads as that confirmation for
    Investor Reporting (INFERRED), so the PRD should state it.
- **F6. The Model Portfolios cards and dialogs are the light family.**
  - `components/CategoryViewTree.tsx` (`CategoryOverview :871-984`, `CategoryTile :565`,
    `CategoryBreakdownDialog :760-859`) and `components/ModelPortfolioModal.tsx:125-236` (a `HeroDialog` with a
    date-stamp footer).
  - Investor Reporting's models dialog is `CategoryBreakdownDialog` in two `md:grid-cols-2` grids (`:799`, `:811`),
    which is the two-sided layout H:32-34 rejects.
- **F7. Progressive disclosure has prior art but no law.**
  - `CategoryTile` shows a brief at rest, detail on hover, and a dialog on click (`CategoryViewTree.tsx:33-37`,
    `:554-564`).
  - `PanelHeader`'s `helpText` holds the facts one click down, and Investor Reporting's Holdings footers already use it
    as of `c75a0fc9`.
  - "Progressive disclosure" has zero hits in `DESIGN.md`, `DESIGN_SYSTEM.md` or `COLOR_ARCHETYPES.md`.
- **F8. Panels, footers and tooltips have one pattern each.**
  - `ui/components/panels/Panel.tsx`, `PanelHeader.tsx:46-119`, `PanelFooter.tsx:73-122` (timestamp and source only;
    correct use at `Positioning/tabs/HoldingsTab.tsx:767`).
  - Tooltips: `DataTooltip` for chart data (the "ONE tooltip look", 32 files) and `HelperTip` for help. Investor
    Reporting uses four patterns today (a default recharts tooltip at `DrillTree.tsx:376`).
- **F9. The website's patterns.**
  - Measured capture `design/brand/opalinvest.com.md` (2026-09-11): canvas `#F4F6FA`, one dark band `#0A1733`, accent
    `#5F3BE3` at about 1%, Lato 400/700, radii of 2-4px, no shadows, 40/60 splits.
  - This seat's read of the live site today (text, not pixels) found:
    - numbered 01 / 02 / 03 cards, three to a row;
    - expandable "Our Process" sections, i.e. progressive disclosure on the site itself;
    - a four-card process band: Discovery, Design, Implementation, Partnership;
    - the five outcome models on a drag slider from "SHORT TERM" to "LONG TERM", Ultra Short-Term (0/100) to Ultra
      Long-Term (90/10).
  - The numbered cards fit O8. The process band fits O8's steps. The model spectrum fits O3 and O10's sample.
  - Art on the site and the portal is CSS gradient, grid and glow with lucide icons; there are no raster assets
    (`HeroGraphic.tsx`).
- **F10. There is no shared searchable dropdown or paginator.**
  - The portal's dropdown is `components/ui/PageSurfaceControl.tsx` (a native select that cannot search, used on Model
    Portfolios, Positioning and Advisor Intelligence).
  - Catalyst `Combobox` has one user, Investor Reporting's `ClientSearch`, and its options still carry OS-dark-mode
    classes (`combobox.tsx:111`, `:150`).
  - `catalyst/pagination.tsx` has zero importers. O1 needs one shared control or an Investor Reporting-local one
    (Part VII call C3).

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

- **Classification, served.** Every holding the Holdings API serves carries a canonical asset class, and sub-asset
  class where known. The classifier covers the securities Investor Reporting shows, or marks them unclassified.
  - Coverage of the served classifier is UNMEASURED; the frontend fallback lists 36 tickers.
- **Model identity, served or derivable.** A model node carries its canonical model code, so colour never depends on a
  display string.
- **A cash colour ruling** (call C1).
- **A place for shared components** (call C3), and a portal-law home for the progressive-disclosure rule if Andrew
  wants it portal-wide (call C2).
- **Endpoint amendments the CTO makes at L2.** The retirement in O9 and the move in O2 change ratified text (Part VI
  S3). They need the ENDPOINT half re-signed under proportionate sign-off.
- **The real run.** The graded run needs a real signed-in session: Andrew's, or IRPT_BCKEND's approved bounded test
  principal (`IB-rtf-3`).

---

## PART VI -- STATUS (NOT OUTCOME-BEARING)

Measured 2026-09-24 ~20:59Z (4:59 PM ET) at portal DEV `c75a0fc9` (origin/DEV `c75a0fc95d`, ls-remote 21:21Z) by this
seat's census subagent, grading the code and not the claims.

- **S1. Andrew's 33 note items at `c75a0fc9`: 7 fixed, 4 partly, 22 not yet.** Two of the 7 fixed rows are the same
  header fix, which is why six fixes are listed below.
  - Fixed by 2.0.0_SA_COO~D today:
    - the "not supplied" chip flood (93b28880);
    - the account bubbles (93b28880);
    - legible search ink (93b28880);
    - the tab-bar scrollbar (93b28880);
    - the 1,000-plus account checkboxes (68f46e18);
    - Holdings footers carrying source and timestamp only (c75a0fc9).
  - Partly:
    - request panels still mount when requests exist;
    - a free-text "catalog key" input;
    - upload works on the served lane but is undesigned (088386fe);
    - Performance footers.
  - Not yet: everything in O3-O5, O7, O8's cards, O10 and O11's look.
- **S2. The FAST lease.** DSGN_IRPTV1 runs FAST under 2.0.0_SA_COO~D, re-armed at 2:16 PM ET on Andrew's word via the
  CTO. It extends while Andrew is typing (`.tools/drive-mode.py status`).
  - None of today's FAST pins is CVO-graded.
  - Every real run so far used the stubbed-auth smoke fixture, not a signed-in session.
- **S3. The ratified endpoint these outcomes touch** (PRD v0.5, FWD-1..11).
  - O2 moves FWD-2's "which accounts" out of the header.
  - O9 retires FWD-7's "history as a 30% left rail" and FWD-8's owner-scoped history. Andrew approved both at
    ~05:0xZ (`ANDREW_DIRECT_20260924_050xZ_IRPT_LAYOUT_RECS_APPROVED.md`, `..._054xZ_...`). A:31-41 is his later word.
  - O8's cards are consistent with FWD-7's stepper; the cards are its variant step.
  - FWD-10's tab order (Performance, Holdings, Analysis) is still off in the code (`TabShell.tsx:18-25` reads
    Performance, Analysis, Holdings).

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM, and the calls it leaves open

**Not claimed.**
- This seat did not look at the running page after `c75a0fc9`. The screenshots are 3:09-3:41 PM ET vintage.
- The served label that painted Ultra Long Term blue was not measured.
- The served classifier's coverage was not measured.
- The website was read as text today plus the 2026-09-11 measured capture. No fresh pixel capture was taken.
- "B-side" is Andrew's term. Mapping it to the HeroGraphic card-and-dialog family is INFERRED from the pages he named.

**Calls for Andrew.** These are open design decisions; the CTO carries them at L2 and none blocks the brief.
- **C1. Cash colour.** Green, as H:72 says, or amber, as POSN_ASTTAX ruled ("amber stays Cash")? Whichever he picks,
  it applies to Positioning too, so an advisor never sees two cash colours.
- **C2. Progressive disclosure: this page only, or portal law?** If portal law, it becomes a DESIGN.md clause through
  DSGN_REBRND.
- **C3. Shared or local?** Are the searchable dropdown and the paginator O1 needs built once as shared portal
  components, or inside `InvestorReporting/**` only?

---

## REFS TO CARRY

```
  BRIEF PATH        docs/briefs/irpt-ui-finish-design-brief-20260924.md
  PROJECT           DSGN_IRPTV1 (D13; COO lane 2.0.0_SA_COO~D; FAST lease live at writing)
  EXISTING PRD      org/missions/D13/DSGN/DSGN_IRPTV1/prd/DSGN_IRPTV1_PRD.md (v0.5; ENDPOINT FWD-1..11)
  PRIOR BRIEF       docs/briefs/irpt-page-remediation-brief-20260924.md (4.0.0_SA_CRO~F; O0-O9 = FWD-1..11)
  SIBLING PROJECTS  IRPT_BCKEND (P/M/Y, closer path); DSGN_REBRND (design law); POSN_ASTTAX (asset-class colours)
  ANDREW'S NOTES    org/tier1_exec/2.0.0_SA_COO~D/deliverables/ANDREW_DIRECT_20260924_194xZ_IRPT_DESIGN_NOTES/
                    + 13 screenshots in C:\Users\AndrewBerman\Downloads\design notes\ (outside the repo)
  PRIOR ART         modelPortfolioColors.ts; chartColors.ts ASSET_CLASS; PhilosophyPillars.tsx + HeroGraphic.tsx;
                    CategoryViewTree.tsx (CategoryTile, CategoryBreakdownDialog); ModelPortfolioModal.tsx;
                    Positioning HoldingsTab.tsx (treemap content + tooltip + breakdown); DataTooltip; HelperTip;
                    Panel / PanelHeader / PanelFooter; PageSurfaceControl; design/brand/opalinvest.com.md
  MEASURED AT       portal DEV c75a0fc9 ~20:59Z 2026-09-24; origin/DEV ls-remote 21:21Z; site read ~20:3xZ
```
