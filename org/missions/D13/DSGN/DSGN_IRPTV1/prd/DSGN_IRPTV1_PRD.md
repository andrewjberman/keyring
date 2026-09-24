# DSGN_IRPTV1 -- Investor Reporting page remediation: the advisor-facing re-render of the header and the three tabs on the portal panel system, with the producer's vocabulary moved into disclosure surfaces

```json
{
 "project": "DSGN_IRPTV1",
 "directive": "D13",
 "fabric": "laptop",
 "prd_version": "v0.5",
 "step": 4,
 "brief_ref": "docs/briefs/irpt-page-remediation-brief-20260924.md@5cc838e696",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7", "FWD-8", "FWD-9", "FWD-10", "FWD-11"],
 "status": "DRAFT"
}
```

Brief: `docs/briefs/irpt-page-remediation-brief-20260924.md` @`5cc838e696`, 23,785 bytes, 302 lines, --midstream, author
`4.0.0_SA_CRO~F`, with two addenda folded in place (O4: the "AUA Trend Analysis" area-chart style, Andrew ~05:3xZ, landed
@`fb90ad8fe0`; O6: a prospect as a first-class subject, Andrew ~05:4xZ, landed @`5cc838e696` -- "prospect" occurs 7 times at
this pin and once at the earlier one, the positive control the CRO's refusal 100289 asked for). Endpoint record:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FWD_DSGN_IRPTV1_20260924.md` @`5daacc16db`. Register: tree row
`org/missions/D13/DSGN/DSGN_IRPTV1/project.json` @`c3508c07df`. Minted on Andrew-direct 2026-09-24 ~05:2xZ at the
`4.0.0_SA_CRO~F` terminal, VERBATIM: *"This should be its own project. Tell CTO this will be D13 project, DSGN_IRPTV1. I
want a proper canonical-flow issued on this from COO~D. Tell CTO that."*

This is an EXECUTION-ONLY PRD for a PRODUCT surface: it names the thread, the cells, the contracts consumed, the write
surface and the evidence each outcome is graded by; it invents no number the brief did not measure. Round 1 builds the
thread (`FWD-1`) end to end; every later round enriches it from the round-N analysis's enrichment list (spine v3.16-3.18).
The L5/L6 issuer is `2.0.0_SA_COO~D` by Andrew's name.

## ENDPOINT (step 2, /endpoint --forward)

```
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
```

Not promised (brief Part II, VII): the PDF / print package; the narrative page; the Global-view entitlement model's
data half; any vendor call; any contract change beyond the additive members already ruled (`display`,
`valuation_facts` extension, `spread`); the design team's own pass (DSGN_REBRND); asset class / sector columns
until their source is ruled; the comparison catalogue picker until the catalogue serves names.

## CONTRACTS

Consumed as they stand (`portal/src/pages/InvestorReporting/contracts/index.ts`, the ten consumed contracts under
`docs/contracts/investor-reporting/v1/` and the operations that serve them): resolve-scope / directory-browse / directory-search / selection-create
(the header's selection stays server-accepted: `POST selections` -> `sel_<64hex>`; the drawer and chips change the
PRESENTATION of a selection, never who may see what), holdings-snapshot, performance-report, analysis-input-upload,
analysis-requests, analysis-request-read / -history, status-summary / status-job, submit-export / export-receipt /
export-download.

Additive members this project RENDERS and does not author (ruled before this PRD; producer-owned; portal-first order
-- the portal accepts a member before any producer emits it, and each member lands in both schema copies):
- `HoldingsSnapshot` node `display` {label, symbol?, description?} (IRPT-HOLDINGS-DISPLAY-NAMES-20260924; the portal
  accepts it since DEV `7975c3bb`; M's fill lands with the COT republish);
- `HoldingsSnapshot` node `valuation_facts` fact_kind `CUSTODY_UNITS` with units `UNITS` (IRPT-HOLDINGS-VALUATION-
  FACTS-20260924); no price fact exists and none is rendered;
- `PerformanceReport` per-comparison `spread` (IRPT-DESIGN-RECON-CALLS-20260924 (a)): the spread is a SERVER-STATED
  fact; the page derives nothing, ever ("Summary.tsx: IT COMPUTES NOTHING" stands).
- Deferred, not blocking: asset class / sector on security nodes (the taxonomy SOURCE card at Andrew); the benchmark
  daily series and household begin/end values (P, brief items); the comparison catalogue (Y); the three routes with NO
  HANDLER at HEAD -- analysis-input-upload, analysis-request-read, analysis-request-history (`routes.json` @`124c0694b7`)
  -- are Y's, and FWD-7 / FWD-8 stand on them as enrichment-round inputs.

Rules every cell obeys: the FE derives nothing; every figure on the page is a wire fact; a fact the source did not
supply renders "not supplied", never zero; the disclosure surfaces (footer line, popover, Details) keep every envelope
fact the evidence rules require, so no L9 grade that reads a state, reason code or revision off the DOM loses its
object -- it moves, it does not vanish; DESIGN.md governs colour, weight, radius and state; a departure is DSGN's.

`unprojected_grant` is a PARTIAL-DATA fact, not entitlement bookkeeping (IRPT_FNTEND PRD CONTRACTS v0.7-v0.9; origin
`1.0.0_SA_CTO` ruling @`61627f39f9` condition 2, carried as row `IRPT_BCKEND-W1-S28`, ARMED at HEAD with `1.0.0_SA_CTO`
as disarm owner). When its count is above zero, a VISIBLE indicator in advisor words stays on the BODY of every scoped
view, the header included; its kinds, denominator and revision go to the disclosure. Branch on shape first: a refusal
carrying `public_reason_code` UNPROJECTED_GRANT renders its reason and no count. The irpt-holdings count is structurally
zero until IB-rtf-8 folds the fork. FWD-2's "entitlements, revisions or cohorts" does not name this indicator, so its
ACCEPT line does not move; a C1 cell that hides the indicator re-opens S28 and fails FWD-2's brief-half reading.

## THE THREAD (FWD-1) -- round 1 builds it end to end

One person: an Opal internal user (Global view). One journey, coarse grain, live, default window, no export, no analysis.
The account is Anna Thiessen's Cottonwood brokerage account `acc_d486fc9455d6b2aa18e13af1`, the one P and M share as their
first live milestone. Hops 1-4 exist and are consumed unchanged (P's shared surfaces); round 1 builds the four render
adapters at hops 5-8. A hop fed by a fixture fails FWD-1. The live trace is the COO's drain act, not a cell (a worker has
no browser; an auth-stubbed smoke fails FWD-1).

1. Real login -> the portal session (the portal's auth, a real Opal user)
2. Firm control reads Global (All) -> resolve-scope against the deployed directory function
3. Browse / search -> Anna Thiessen's Cottonwood brokerage account found and chosen
4. POST selections -> a selection id for that account
5. Identity card -> name, firm, accounts by name + masked tail, holdings total, business date (C1)
6. Performance headline -> YTD net return, the server-stated spread or "not supplied", beginning / ending value (C6's headline half)
7. Holdings L0 hero -> the Models / SMAs / Client card from the published Cottonwood revision, names from `display` (C3)
8. Security list -> the sortable table of securities with ticker, name, sleeve, weight and value (C4's table half)

Chains: header (5), performance (6), holdings (7, 8). A build cell carries at most THREE mechanical criteria; repo-wide
hygiene runs at the drain. The round-1 analysis ends in the enrichment list the next round cuts.

## ENRICHMENT BACKLOG (everything off the thread, ordered)

1. FWD-2 header identity card complete (entitlements, revisions and cohorts one click away) -- C1 remainder
2. FWD-4 one firm control, the Model Portfolios dropdown, Global (All) for Opal users only -- C2
3. FWD-6 Holdings: allocation bars per category with the per-account matrix; the treemap; asset class / sector columns when ruled -- C5; C4 remainder
4. FWD-5 Performance: the control row (window, net / gross); the AUA Trend area chart; the returns heatmap; the accounts table with the uncovered-account row; the footer line with its popover -- C6 remainder, C7, C8
5. FWD-11 no system vocabulary on any tab body; the facts retained one click down -- C14
6. FWD-3 the browse drawer (grouped by firm in the Global view; the paged dropdown gone) -- C9
7. FWD-7 the Analysis stepper (Input, Review, Settings, Generate, Report) with the left rail and the per-report Details popover -- C10
8. FWD-8 the prospect as subject (prospect card in the header, upload-first step 1, the prospect's own history) -- C11
9. FWD-9 one page-level Export on the header; the two disabled per-tab buttons gone -- C12
10. FWD-10 the portal panel system on every panel; tab order Performance, Holdings, Analysis -- C13
11. The `spread` member consumed when P lands it (round 1 renders "not supplied" and the trace grades that hop with the reason;
    FWD-1's ACCEPT names the spread, so a passing round-1 trace leaves FWD-1 NOT_REALIZED until `spread` is served)

## CELL CANDIDATES (the COO's decomposition; not task orders)

- C1 Header identity card: name, firm, relationship/account kind, accounts as chips (display name + masked tail from
  `DirectoryEntry`, toggleable to narrow), holdings unique custody total, business date; entitlement bookkeeping
  (scope match, directory revision, cohort, unprojected grant) into an "About this scope" disclosure. Serves FWD-2,
  FWD-11; the thread's first read.
- C2 Firm control: `PageSurfaceControl` (the Model Portfolios dropdown) with firm display names; Global (All) for the
  Opal user only. Serves FWD-4.
- C3 Holdings L0: `CategoryViewTree` fed the snapshot's Models / SMAs / Client children (it is already imported by
  `DrillTree.tsx` and fed empty children today). Serves FWD-6 (L0), the thread.
- C4 Holdings L2: treemap + sortable/filterable security table (ticker, name from `display`, sleeve, weight, value;
  asset class / sector columns absent until ruled). Serves FWD-6 (L2), the thread's last read.
- C5 Holdings L1: allocation bars per category with the per-account matrix (the Positioning summary pattern). Serves
  FWD-6 (L1); an enrichment after the thread.
- C6 Performance headline + control row: window (QTD/YTD/1Y/3Y/SI/custom) and Net/Gross; period return, spread
  (server-stated), beginning/ending value, each "not supplied" when absent. Serves FWD-5; the thread's middle read.
- C7 Performance chart: full-width cumulative return in the "AUA Trend Analysis" `<AreaChart>` style
  (`ModelPortfolios.tsx:1320`, `:2099`, `:2114`, `:2164`) over `dailyCumulative`; the benchmark overlay when its
  series lands. Serves FWD-5; enrichment.
- C8 Performance heatmap + accounts table: `BenchmarkHeatmap` pattern with periods across and portfolio / benchmark /
  spread rows; one row per account by name + tail, an uncovered account as a row with its reason. Serves FWD-5.
- C9 Browse drawer: scrollable client list (name, tail, kind, active/terminated, account count), grouped by firm in
  Global; the paged combobox retired; type-ahead retained. Serves FWD-3.
- C10 Analysis stepper: Input (client holdings OR upload, two radio cards) -> Review -> Settings -> Generate (stage
  rail, polled) -> Report; left rail (30%) of the advisor's reports; one Details popover per report. Serves FWD-7.
- C11 Prospect as subject: Analysis reachable with no client; the header's Prospect card; upload path first when no
  client; owned-request history; re-open / re-run from retained input. Serves FWD-8. Open at L4 for L5: whether a
  dedicated prospect-name member is needed beyond `prepared_for` display text (a Y/P data question; the card renders
  `prepared_for` until then).
- C12 One page-level Export of the active tab at the revision on screen; the per-tab buttons retired. Serves FWD-9.
- C13 Panel-system conformity: every card onto `Panel` / `PanelHeader` / `PanelContent` / `SmartPanelFooter`; the
  Performance tab off the print stylesheet (`render/print.css` / `.ir-page`) onto screen layout; tab order
  Performance / Holdings / Analysis (the rename rides the portal candidate after the DEV consolidation, already
  pushed at `7975c3bb`); a 1440 desktop layout with the two-column and rail splits the concepts draw. Serves FWD-10.
- C14 Vocabulary rule: on every tab the producer's states, reason codes, revisions, fingerprints render only in
  disclosure surfaces. Serves FWD-11; applied once per cell above and graded once at the drain.

## PATHS (the write surface)

Owned: `portal/src/pages/InvestorReporting/**` -- the advisor-facing render (header, the three tabs, disclosure
surfaces, the page-level Export), and its tests under `portal/src/pages/InvestorReporting/__tests__/**`. Shared
components are EXTENDED or WRAPPED, never forked: `portal/src/components/CategoryViewTree.tsx`,
`components/BenchmarkHeatmap.tsx`, `components/ui/PageSurfaceControl.tsx`, the panel system under
`components/ui/panels/**` -- a change to a shared component is a cell with its own criterion naming every other page
that renders it, or it is wrapped locally.

Relied on, not owned (the closer contract v1.4 and the sibling lanes): `portal/src/pages/InvestorReporting/contracts/**`
and `api/**` (P, the shared client surface; the additive members' acceptance); the producers (M: custody publication,
`display`, `CUSTODY_UNITS`; P: the Performance adapter and `spread`; Y: upload / job semantics, the catalogue);
`portal/DESIGN.md` (DSGN_REBRND, the design law). Sequenced by the CTO against the IRPT post-slug HOLD and the P/M/Y
closer contract: the COT `display` republish, SERVED (model names on Anna's page), precedes the L6 issuance -- hops 7
and 8 read names from it -- AND M's labels pin `e5dd8487` is an ancestor of portal `DEV` (it rides P's next candidate,
landed by MSTR on Andrew's word; at v0.5 `merge-base --is-ancestor e5dd8487 DEV` reads rc=1), because C3 / C4 build on
those rows; the cut records `portal_ref` and that is-ancestor rc in the issuance's fanout data. If the candidate lags the
served republish, the base stays DEV (a candidate-based worktree drains into a branch P must reconcile twice). The D1
resident run is NOT a precondition (the thread does not touch Analysis). The round-1
DRAIN TRACE additionally needs the Performance path READY for hop 6, and both of its parts sit outside this project's
write surface: (i) X10 enforced -- the registry row ACTIVE with `enforcement_ref` = the CTO's accepting commit, and the
adapter repackaged with it (CTO review, P repackage); (ii) ONE installed one-use plan for `acc_d486fc9455d6b2aa18e13af1`
on the default window -- Andrew's per-use word for the Black Diamond call, the CTO's install. The CTO's choice, stated:
the L6 issuance does NOT wait on (ii). If the plan word has not come by the drain, the trace grades hop 6 from the LIVE
refusal ("not supplied" with the producer's public reason on screen), FWD-1 stays NOT_REALIZED, and the live return is
round 2's first enrichment item; a hop fed by a fixture still fails FWD-1.

## FIXTURES AND EVIDENCE

- The thread's evidence is a LIVE trace: the real login, the real calls (HAR read in place, never copied), the deployed
  functions' CloudWatch lines, the rendered page. A fixture-fed hop fails FWD-1.
- Enrichment cells may prove a render with the existing fixtures under `__tests__/fixtures/**` and the sibling's
  fe-s suites, stated as fixture proofs; the EXERCISED outcomes (FWD-2, 3, 5, 6, 7, 8) are graded on a live read by
  the person named in the ACCEPT line, never by the builder.
- Instruments the grader runs: the portal build (`bun run build`), `tsc -b --noEmit`, the affected suites with counts
  beside the untouched DEV head (the fe-s-10 fixture-path failures are a known worktree artefact, stated each time),
  and one HAR of the journey.

## BRIEF COVERAGE

O0 -> FWD-1 (the thread). O1 -> FWD-2. O2 -> FWD-3. O3 -> FWD-4. O4 -> FWD-5. O5 -> FWD-6. O6 -> FWD-7 and FWD-8
(the prospect paragraph). O7 -> FWD-9. O8 -> FWD-10. O9 -> FWD-11. Part II (boundary) -> PATHS. Part III (the
qualitative bar) -> the ACCEPT lines. Part IV (substrate) -> CONTRACTS and CELL CANDIDATES. Part V (what must be
true) -> the rules under CONTRACTS. Part VI is status, not outcome-bearing, and is not carried. 10 of 10 territory
headings (O0-O9) covered, O6 carrying two outcomes; 0 uncovered.

## L2 FINDINGS CARRIED (from the endpoint record)

New ids by Andrew's word (its own project); IRPT_FNTEND's FWD-12 is the lineage this list serves, not a member.
The endpoint's NOT READ line stands for this PRD too: the D9/D13 task-order register, any decomposition, any
project.json and the sibling PRDs beyond the brief's summary were not consulted. The DONE WHEN lines are at Andrew for
his confirmation; his word at L2 is the one gate before the loop cycles without him.

## PROVENANCE AND AMENDMENT HISTORY

- v0.1, 2026-09-24 ~05:0xZ, `1.0.0_SA_CTO` (Claude): first cut at L4 from the brief @`fb90ad8fe0` and the endpoint
  @`5daacc16db`; register @`c3508c07df`. L4-R: the RATIFIED-TEXT half (ENDPOINT + CONTRACTS) to `3.0.0_SA_CVO`
  (seated by `0.0.0_AB_MSTR` on the CTO's word at this pin); the BRIEF half (everything else) to `4.0.0_SA_CRO`
  (`4.0.0_SA_CRO~F` offered, msg 100235). The L4 notifier delivers each half; the COO delivery is withheld until both
  are SIGNED at these bytes. `2.0.0_SA_COO~D` is seated at the L5 handoff on the CTO's word (a fourth COO instance
  against the 3-COO cap -- Andrew's call, raised by MSTR).
- v0.2, 2026-09-24 ~05:1xZ, `1.0.0_SA_CTO` (Claude): header-only bump; the v0.1 header's `status` carried a prose qualifier
  the closed enum refused, so the L4 notifier routed nothing at v0.1; no section text changed.
- v0.3, 2026-09-24 ~05:3xZ, `1.0.0_SA_CTO` (Claude): THE THREAD rewritten as the spine's hop list (`N. A -> B`, eight hops)
  and ENRICHMENT BACKLOG added as its own ordered section (spine :153 at HEAD, finding F1 of `2.0.0_SA_COO~D` 100278);
  the sequencing line now names the served `display` republish as the L6 precondition and drops the D1 run from it.
  Brief half only; ENDPOINT and CONTRACTS bytes unchanged (a ratified-text stamp at v0.2 still binds).
- v0.4, 2026-09-24 ~05:4xZ, `1.0.0_SA_CTO` (Claude): both halves REFUSED at v0.3 and re-cut on the two reviews -- brief half
  (`4.0.0_SA_CRO` 100289 @`fc5378db02`): brief pin -> @`5cc838e696` (both addenda), coverage 10 of 10 (O0-O9), the Performance
  path's readiness stated on the sequencing line; ratified-text half (`3.0.0_SA_CVO` 100290 @`e0915c97fe`): `unprojected_grant`
  as a partial-data fact with the visible indicator (CONTRACTS), "ten consumed contracts and the operations that serve them",
  the three no-handler routes deferred as Y's. Both halves change bytes; both stamps are owed again.
- v0.5, 2026-09-24 ~06:0xZ, `1.0.0_SA_CTO` (Claude): `2.0.0_SA_COO~D` pre-read 100308 -- F2 the ENRICHMENT BACKLOG cited candidate
  ids shifted against CELL CANDIDATES (items 3-10 re-lettered to the section's own ids; FWD ids and words unchanged); F3 the
  portal base at the cut needs M's labels pin on DEV, added to the sequencing line. Brief half only; ENDPOINT and CONTRACTS
  bytes unchanged (the `3.0.0_SA_CVO` stamp @`2c60ba747f` stands); the brief half's stamp is owed at these bytes.

## SURFACE MANIFEST

WRITES: `portal/src/pages/InvestorReporting/**` (render + tests). EXTENDS (by a cell naming every other consumer):
`portal/src/components/CategoryViewTree.tsx`, `components/BenchmarkHeatmap.tsx`, `components/ui/PageSurfaceControl.tsx`,
`components/ui/panels/**`. READS: the ten v1 contracts and the three additive members; `portal/DESIGN.md`; the four
reference pages (Model Portfolios, Positioning, Advisor Intelligence, the Benchmark tab). NEVER: `portal/src/api/**`,
`portal/src/pages/InvestorReporting/contracts/**` (P's), any producer, any vendor call, `render/**` (the print package).
