# DSGN_AMGTV1 -- ENDPOINT (step 2, /endpoint --forward) -- DRAFT FOR ANDREW'S CONFIRMATION

**Seat:** `1.0.0_SA_CTO~Z`, 2026-09-28 ~23:5xZ. **Input:** the L1 brief
`docs/briefs/dsgn-amgtv1-security-analysis-frontend-brief-20260928.md` @`08eefaac9d` (49,179 B; `4.0.0_SA_CRO~Z`), its
register `docs/briefs/dsgn-amgtv1-findings-20260928.json` (42 findings) and Andrew's walk memo (M0-M15).

**NOT YET LANDED.** No PRD exists. This block is the section **`ENDPOINT (step 2, /endpoint --forward)`** of
`org/missions/D13/DSGN/DSGN_AMGTV1/prd/DSGN_AMGTV1_PRD.md`, written there at L4 after Andrew confirms the DONE WHEN lines
and the project is registered at L3 (D13, fabric site-z, COO `2.0.0_SA_COO~D` per record @`4b8c8e402c`'s merge).

---

## ENDPOINT (step 2, /endpoint --forward)

```
  FWD-1  A portfolio manager opens Security Analysis, finds Valero in today's
         Trending x Price list by its name, opens it, and reads it as cards --
         end to end on the live product
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

  FWD-3  A PM can read how names moved over time without untangling a knot of
         lines
         DONE WHEN  EXERCISED -- the history view walked with ten or more names
         ACCEPT     With ten or more names, the dates do not overlap, each line is
                    labelled by company name, there is one legend, and the PM can pick
                    out one name and follow it. The form is Andrew's call (fork F1).
         SOURCE     brief O3 (:71-75); M2, M3, M5, M14

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
```

FWD-1 is the thread (spine v3.16-3.17): round 1 builds it; FWD-2..FWD-11 are the enrichment rounds.

---

## FORKS AT ANDREW (brief Part VII, :475-511), each with this seat's REC

| fork | the brief's REC | this seat's REC |
|---|---|---|
| F1 ranking-over-time form | (c) both: sparklines in the list + a highlight chart | (c) -- agree |
| F2 which classifier table | `etf-classifications` alone, AMGT rows via POSN's writer | agree; the new rows move served output COT and BD will read, so they go under a never-widen pair |
| F3 exec-management fallback order | filing -> dossier -> Bloomberg -> Lusha roster -> search, each vendor leg on per-use word | agree |
| F4 the News Scanner leg of the timeline | (b) harvest only for round 1; name-alias matching as an enrichment | agree |
| F5 absorb the 09-24 brief's open page outcomes from AMGT_RESAPP | yes: this project owns presentation, AMGT_RESAPP keeps the payloads | agree; the boundary rule (a missing field is an ask to its owner, never a page-side computation) carries into the PRD |

## PROVENANCE

- **READ:** the brief Parts 0-VII, the acceptance shape and REFS (:1-596, @`08eefaac9d`).
- **NOT READ:** the task-order register, any AMGT project's task orders or `project.json` (Phase 0 refuses them), the 42
  register rows individually (the brief's outcomes cite them by id), Andrew's 12 PNGs (local, uncommitted).
- **UNRATIFIED:** every FWD line above until Andrew confirms the DONE WHEN lines.
