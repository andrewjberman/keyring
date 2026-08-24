# ANDREW-DIRECT 2026-08-24 ~17:1xZ (base CTO terminal) -- 49 FINANCIAL, finding 3 of 3: ALL OF THIS SERVES PERFORMANCE ATTRIBUTION AND REPORTING -- built on our account -> client/relationship -> advisor -> firm SPINE, not reinvented; the existing BD Performance Reporting dashboard (his screenshots + recording) is the inspiration for a comparable interface folded into Advisor Intelligence, living ENTIRELY in the "Books" tab and the advisorpublicprofile "Book" toggle view

**Recorded by:** `1.0.0_SA_CTO` (addressed seat) - **archetype:** SCRIBE / COORDINATE
**Context:** the third of three findings from the 49 Financial meeting (Mike), after finding 1
(@dbf4e493eb, structure / Insurance split) and finding 2 (@a5f1acd3ad, BD history stitching). Quoted
exactly as typed. **DISTRIBUTION RESTRICTION (his ~16:1xZ word) binds: nothing on this subject to
`4.0.0_SA_CRO`.**

## VERBATIM

> "Finding 3: We are doing all of this to facilitate our work on Performance Attribution and Reporting.
> What that means is the following. We should not reinvent the wheel from scratch; rather we should use
> our account -> client/relationship -> advisor -> firm spine as the basis for how we design performance
> reporting on a per client basis. I Think a logical way of how to set this project up is that I will
> take some screenshots and do a little recording of operations on the existing BD Performance Reporting
> dashboard which we can use for inspiration on developing a comparable interface function that folds
> into the Advisor Intelligence platform. I foresee this function as living entirely in the "Books" tab
> and commensurately the advisorpublicprofile "Book" toggle view."

## WHAT IT BINDS (surfaced, unwidened; the phrasing is the ruling)

1. **THE PURPOSE OF THE WHOLE 49F PROGRAM IS PERFORMANCE ATTRIBUTION AND REPORTING.** Findings 1 and 2 --
   the 08335338 ADVI route, Fidelity next, the Insurance split, the BD-history stitching -- all
   "facilitate" this. It is the intent every 49F project under D2 now traces to (the intent-denominator
   discipline: a cell that does not serve per-client performance reporting is out of the program's frame).
2. **DO NOT REINVENT.** Design per-client performance reporting on **OUR EXISTING SPINE: account ->
   client/relationship -> advisor -> firm** -- the same aggregation spine finding 1 named for Insurance.
   (In-estate: the canonical 49F runner chain's a-series dims + c-series flows/NNA/TWR at
   `opal-data-49financial/gold/advi/`; CRO's `ADVI_PERFORMANCE` GIPS field contract; the D2 parity
   program's per-account classification harness -- Build Ladder rung 2 applies before any new code.)
3. **THE INSPIRATION SOURCE = the existing BD Performance Reporting dashboard**: Andrew will supply
   **screenshots + a recording of its operations**; the deliverable is *"a comparable interface function
   that folds into the Advisor Intelligence platform"* -- comparable, not cloned; BD is the reference
   for the interface, not a data dependency (finding 2's trust ruling stands).
4. **PLACEMENT ON THE PRODUCT: ENTIRELY in the "Books" tab and, commensurately, the `advisorpublicprofile`
   "Book" toggle view.** Same surface finding 1 chose for Insurance; the Advisor and Distribution tabs
   are not touched by either.
5. **Process:** a new directive-class project through the Rule 27 pipeline; its stage-2 PRD WAITS on his
   screenshots + recording as a declared input (the shape rectangle is read from them, atom-decomp
   style, exactly as the Positioning page's shape was pinned from the served artifact). Registration
   can proceed now; the PRD's shape section is a declared gap until the input lands.

## THE PROGRAM SHAPE THESE THREE FINDINGS DRAW (CTO reading, for the registrations; not a ruling)

```
 PURPOSE: per-client PERFORMANCE ATTRIBUTION + REPORTING for 49 Financial (finding 3)
   on the spine  account -> client/relationship -> advisor -> firm
   surface       "Books" tab + advisorpublicprofile "Book" toggle ONLY
   inspiration   BD Performance Reporting dashboard (his screenshots + recording)

 FEEDS:
   value/history plane   Schwab 08335338 (limited history, fine for now)  +  Fidelity next   (finding 1)
   insurance plane       BD insurance endpoint snapshot -> its own project; never blended   (finding 1)
   legacy history        BD history in opal-data-bd -> opal-data-assets by design; the
                         STITCHING project (migrated / stayed / dropped / unknown)          (finding 2)
```

## BROADCAST
MCP to MSTR + the queued seats that will hold cells (COO, CVO, DS, DE, AE, DT, 0.6.0_AE_PartnerETL).
**NOT to 4.0.0_SA_CRO.** Same turn; push state stated on the commit.
