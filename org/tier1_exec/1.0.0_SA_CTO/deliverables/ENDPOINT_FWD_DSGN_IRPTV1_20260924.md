# ENDPOINT (step 2, /endpoint --forward) -- DSGN_IRPTV1 (D13): the Investor Reporting page remediation

Seat: 1.0.0_SA_CTO (Claude). Phase 0, greenfield path. Cut 2026-09-24 ~04:5xZ.
Brief: docs/briefs/irpt-page-remediation-brief-20260924.md -- author 4.0.0_SA_CRO~F, dated 2026-09-24 ~05:2xZ,
mode --midstream, 22,530 bytes, committed in the shared tree at fb90ad8fe0 (O4 amended in place with the area-chart word).
Project: DSGN_IRPTV1 under D13 (DSGN), Andrew-direct ~05:2xZ: "This should be its own project. Tell CTO this will be D13
project, DSGN_IRPTV1. I want a proper canonical-flow issued on this from COO~D." L5/L6 issuer 2.0.0_SA_COO~D.
L2 CALL on the brief's Part 0 question (amend IRPT_FNTEND's FWD set, or new ids): NEW IDS. Andrew made this its own
project; its endpoint is its own FWD list, with FWD-1 the thread. IRPT_FNTEND's FWD-12 is the lineage this list serves,
not a member of it; IRPT_FNTEND / IRPT_BCKEND stay siblings this project relies on and does not own.

STATUS: NOT YET LANDED IN A PRD. The PRD does not exist yet. This block belongs under the section titled
`ENDPOINT (step 2, /endpoint --forward)` in org/missions/D13/DSGN/DSGN_IRPTV1/prd/DSGN_IRPTV1_PRD.md (L4).

---

  FWD-1  An Opal user opens Investor Reporting, picks Anna Thiessen's Cottonwood brokerage account, and reads
         her identity card, her year-to-date return with its spread to the benchmark, her Models / SMAs / Client
         split and her security list -- on the live product, end to end
         DONE WHEN  EXERCISED -- one live trace, real login, real backend, real Cottonwood data, ending in the
                    rendered page; the frontend may be local or on DEV
         ACCEPT     an Opal user who has never seen the code can name, from the screen alone, who the client is,
                    how much she holds, her year-to-date return and spread, what she holds by category, and the
                    securities inside -- without reading a single id, hash or state word; every hop is a real
                    call and a hop fed by a fixture fails the outcome
         SOURCE     brief O0 (the candidate thread), Part III bullets 1-3

  FWD-2  An advisor knows who they are looking at from the header alone
         DONE WHEN  EXERCISED -- an advisor reads the header for a real client and answers who / how much / over
                    which accounts / as of when
         ACCEPT     the header shows the client's name, firm, the accounts by name and masked tail, the holdings
                    total and the business date; nothing about entitlements, revisions or cohorts is on it,
                    and all of that is one click away
         SOURCE     brief O1; Part III bullet 3

  FWD-3  An advisor reaches any permitted client by browsing, not only by typing
         DONE WHEN  EXERCISED -- an advisor who does not know a client's spelling finds them in the drawer
         ACCEPT     a browse drawer lists the firm's clients (grouped by firm in the Global view) with name,
                    masked tail, kind, active or terminated, and account count; the paged 25-row dropdown with
                    "Load more clients" is gone; typing still works for those who know the name
         SOURCE     brief O2 (card 1 ruled (a))

  FWD-4  One firm control, whoever the viewer is
         DONE WHEN  APPLIED -- the same dropdown the Model Portfolios header uses, on this page
         ACCEPT     an Opal user and a firm user see the same firm control with firm display names; only the
                    Opal user sees "Global (All)"
         SOURCE     brief O3

  FWD-5  An advisor reads a client's performance the way they read a model's on Model Portfolios
         DONE WHEN  EXERCISED -- an advisor reads a real client's return, spread and the lagging account in one
                    screen instead of opening Black Diamond or SmartX
         ACCEPT     one control row picks the window and net or gross; a headline row shows period return, spread
                    to the benchmark, beginning and ending value, each saying "not supplied" rather than zero when
                    the source did not supply it; a full-width cumulative-return chart in the "AUA Trend Analysis"
                    area style; a returns heatmap with periods across and portfolio, benchmark and spread as rows;
                    an accounts table with one row per account by name and masked tail, an uncovered account shown
                    as a row with its reason; the spread is a figure the server stated, never one the page worked
                    out; method and lineage sit in a footer line with a popover
         SOURCE     brief O4 (card 4 ruled (a); the area-chart word ~05:3xZ); Part IV.3 data gaps; Part V bullet 1

  FWD-6  An advisor sees a client's holdings three ways down, including a security list
         DONE WHEN  EXERCISED -- an advisor answers "what does the IRA hold" from the security list
         ACCEPT     the Holdings tab shows the Models / SMAs / Client hero card the Model Portfolios page shows,
                    then allocation bars per category with a per-account matrix, then a treemap and a sortable,
                    filterable table of the securities with ticker, name, sleeve, weight and value; asset class
                    and sector columns appear when their source is ruled and are absent, not blank, until then;
                    basis, denominator and provenance move to the footer
         SOURCE     brief O5 (card 3 ruled (a)); Part III bullet 2; Part V bullet 7

  FWD-7  An advisor produces an analysis report through a five-step flow and always knows which step they are on
         DONE WHEN  EXERCISED -- an advisor completes one report, leaving and returning to the tab while it
                    generates
         ACCEPT     the Analysis tab is a stepper -- Input, Review, Settings, Generate, Report -- with a left rail
                    of the advisor's reports (status dot, title, date, filter); every identifier the system needs
                    sits behind one "Details" popover per report and never in the body
         SOURCE     brief O6 (card 5 ruled (a)); Part III bullet 6

  FWD-8  A prospect is a first-class subject of an analysis, not a missing client
         DONE WHEN  EXERCISED -- an advisor produces a report for a portfolio that belongs to no existing client
         ACCEPT     with no client selected the Analysis tab is reachable and complete; the header shows a prospect
                    card (the uploaded portfolio's name, prepared-for, as-of and total) rather than "No client
                    selected"; step 1 leads with the upload path; the prospect's report appears in the advisor's own
                    history and can be re-opened and re-run without re-uploading, so a prospect who becomes a client
                    keeps their history
         SOURCE     brief O6, the prospect paragraph (Andrew-direct ~05:4xZ)

  FWD-9  An advisor exports the tab they are looking at from one place
         DONE WHEN  APPLIED -- one page-level Export action on the header
         ACCEPT     one Export control exports the active tab at the revision on screen; the two disabled per-tab
                    buttons are gone; what an export produces is the sibling projects' existing territory
         SOURCE     brief O7 (card 6 ruled (a))

  FWD-10 An advisor who uses the rest of the portal recognises this page
         DONE WHEN  APPLIED -- every panel on the page is the portal panel system laid out for a desktop screen
         ACCEPT     a designer picking the page up for the design team's pass finds the panel system and the
                    design law already applied and spends the pass on taste, not on removing hand-rolled cards;
                    the tabs read Performance, Holdings, Analysis in that order; an advisor who has used Model
                    Portfolios, Positioning and Advisor Intelligence recognises the hero card, the matrix, the
                    heatmap and the accounts table without explanation
         SOURCE     brief O8 (card 7 ruled (a)); Part III bullets 4-5; Part IV.1, IV.5, IV.6

  FWD-11 A client looking over the advisor's shoulder never reads a state token, reason code, hash or revision
         DONE WHEN  APPLIED -- on every tab the system's vocabulary lives only in disclosure surfaces
         ACCEPT     on any tab, a client watching the screen sees their name, accounts and numbers and not one
                    entitlement token, reason code or revision hash; the facts are retained one click down, so a
                    reviewer who needs a state or revision can still find it
         SOURCE     brief O9; Part III bullet 3; Part V bullet 6

---

WHAT THE ENDPOINT DOES NOT PROMISE (the brief's Part II and VII, carried so a later reader does not infer them):
the PDF / print package; the narrative page; the Global-view entitlement model's data half; any vendor call; any
contract change beyond the additive members already ruled (`display`, `valuation_facts` extension, `spread`); the
design team's own pass (DSGN_REBRND); asset class / sector columns until their source is ruled; the comparison
catalogue picker until the catalogue serves names.

SEQUENCING INPUT (not a ruling): the CTO holds this project against the IRPT post-slug HOLD and the P/M/Y closer
contract; the DEV consolidation is pushed (portal DEV 7975c3bb); the D1 run and the COT `display` republish precede
L5. FWD-1's thread reuses the account P and M already share (acc_d486fc9455d6b2aa18e13af1).

PROVENANCE
  GROUNDED ON  the brief at fb90ad8fe0, read in full (303 lines); every outcome cites its brief heading
  NOT READ     the D9/D13 task-order register, any decomposition, any project.json, the CONCEPTS deliverable
               beyond the brief's own citations of it, the sibling PRDs (the brief summarises their FWD ids)
  DONE WHEN    APPLIED on FWD-4, FWD-9, FWD-10, FWD-11; EXERCISED on FWD-1, FWD-2, FWD-3, FWD-5, FWD-6, FWD-7, FWD-8
  AT ANDREW    confirm the DONE WHEN lines (his word at L2); after that the loop cycles without him
