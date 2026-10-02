# IRPT three surfaces: status research and three briefs -- 4.0.0_SA_CRO~X

**archetype:** TRACE
**Date:** 2026-10-02 (14:54Z-17:12Z)
**Task Order:** ad-hoc, Andrew-direct ~14:5xZ (record @fc46925968, addenda @c56606d5ce, @25c40b0035)
**Status:** COMPLETE

---

## Objective

Record Andrew's words on the Investor Reporting Performance, Analysis and Holdings surfaces verbatim, research each
surface's status, and deliver three briefs in order to 1.0.0_SA_CTO for fold-in to 2.0.0_SA_COO~P, ~Y and ~M.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find (rail) | a raw grep over an `infra/` .tf file was refused by the rail | PASS | rerouted to the native Grep tool for one literal |
| to-check | (fork) `python .tools/to-check.py --project IRPT_BCKEND` | PASS | open-order list for brief 1 section 5 |
| comp-routes | (fork) `comp-routes api-routes` | FAIL | does not model the IRPT HTTP API (22 routes, none IRPT); live `get-routes` used |

**What worked:** three parallel read-only research forks; every load-bearing claim re-printed at its cited line before use.
**What failed:** `comp-routes api-routes` coverage of the IRPT API.
**Gap found:** comp-routes has no IRPT HTTP API root.

---

## Work Completed

1. Record @fc46925968 (verbatim, points P1-P4, A1-A6, H1-H2); addendum 1 @c56606d5ce (Alyssa Keith's easy file for
   cases A-C, Stevens file for D); addendum 2 @25c40b0035 (typo file, AAPL -> APPL, made by this seat).
2. Read Andrew's Teams chat with Alyssa Keith (gateway, read-only): the 14:47Z ask for an easy and a hard spreadsheet.
3. Three research forks (Performance calc, Performance backend, Analysis); claims spot-checked at source:
   census table `:90-96`, design `:72`, 09-30 record `:35-44`, `holdings_gold.py:270`, `REAL_RUNS_20261001.md:257`,
   `ProspectComposer.tsx:326` on origin/PROD, gate wiring by `git grep`, `maintained_sources.py:555-560`,
   `ReportingTab.tsx:614-640`, `integrations.tf:58`, `reporting-gold/handler.py:18-19`.
4. Holdings researched directly: `HoldingsTreemap.tsx` grouping, live `irpt-holdings` config (b26847ea04 build).
5. Briefs 1-3 committed @80fa729b0e; one message to 1.0.0_SA_CTO (delivered, 1,158 bytes).

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `deliverables/ANDREW_DIRECT_20261002_145xZ_IRPT_THREE_SURFACES_STATUS_AND_THREE_BRIEFS.md` | record + 2 addenda | fc46925968, c56606d5ce, 25c40b0035 |
| `deliverables/IRPT_BRIEF_{1,2,3}_*_20261002.md` | three briefs | 80fa729b0e |
| `C:\Users\AndrewBerman\Downloads\... - TYPO CASE (AAPL as APPL).xlsx` | test file, outside git | n/a |

---

## Blockers

None at this seat.

## Current State

Delivered; the fold-in is 1.0.0_SA_CTO's. Push state LOCAL; origin/CLOUD 0c388df7f1 at 17:09Z (ls-remote read).

## Next Steps

1. **[1.0.0_SA_CTO]** Fold briefs 1-3 into ~P, ~Y, ~M; brief 1 section 7 holds three calls for Andrew.
2. **[4.0.0_SA_CRO~X]** Answer the CTO's questions on the briefs; nothing else owed.
