# DSGN_AMGTV1 -- ROUND 33 ANALYSIS and the round-32 grades (L10), `1.0.0_SA_CTO~Z`, 2026-10-03 ~22:4xZ

**Inputs:** COMPLETION_REPORT.round32.json @0f883b11a3 (27/27 COVERED, 114/114 proved); round 33's close @110ffcab86. The served build
is portal PROD dbd29c6320 (Deploy 37156394008 SUCCESS), carrying rounds 29-33 on Andrew's card-1 word and the laptop's promote.
**Grades:** `ledger/COMPLETION_GRADES.round32.json`: **10 REALIZED, 3 NOT_REALIZED, 13 NOT_EVALUATED, 1 RETIRED.**

## 1. WHAT THE GRADES SAY

- **Why round 26's 21 REALIZED do not carry:** the redesign (rounds 29-32) rewrote most faces, so a round-26 grade on the old faces
  proves nothing about the new ones. Each outcome was re-read on the redesign's five close walks of f9c6fa73, whose
  SecurityAnalysis bytes equal PROD's apart from one type alias.
- **REALIZED (10):** FWD-6, 12, 15, 16, 17, 18, 22 (under v0.15), 23, 25, 26.
- **NOT_REALIZED (3):**
  - FWD-5: no word cloud on any face.
  - FWD-21: at 90D, labels collide with bubbles and leader lines run through labels (TOKYO ELECTRON LTD, UnitedHealth Group Inc;
    verified on shot 004 of walk 20261003T175905Z).
  - FWD-27:
    - one security under two names on one page ("The Boeing Co" vs "BOEING CO/THE (subject)" in Peers, verified on shot 016);
    - a header move with no window named;
    - What-changed changes at raw precision against rounded before/after values;
    - provenance lines at rest on the Model tab.
- **NOT_EVALUATED (13):** the walks did not reach every limb:
  - AMD's tab shots are all behind the still-open day dialog;
  - no non-USD name, and no filing without officers, was walked;
  - the six-state capture was not re-run on the redesign;
  - no hover reads.
  FWD-1 stays Andrew's own signed-in PROD read.
- **The walks predate RESAPP's title-case deploy** (lPTMo20T, ~19:5xZ), so FWD-27's name limb must be re-read on today's data.

## 2. RULINGS

| # | item | ruling |
|---|---|---|
| 1 | FWD-1/4/13 still said "four cards" after SAUX-03 (Andrew's 10-02 walk) replaced the header | **PRD v0.15:** the three outcomes read the key-figures row. CVO re-sign owed. FWD-4 is graded on its currency walk. |
| 2 | FWD-22's 90/365 limb | **v0.15** accepts FWD-26's interim "not produced yet" branch until the PX_LAST history serves (card 4). |
| 3 | The 13 NOT_EVALUATED | **One served-build walk is cut in round 34,** designed to the gaps, not a repeat of round 32's (list below). |
| 4 | FWD-27's provenance lines at rest (SAUX-25) | The producer half is RESAPP FWD-38 (d), so it goes to `2.0.0_SA_COO~Z`. DSGN prints only what the route serves. |
| 5 | FWD-5's word cloud | DSGN's render cell is cut when RESAPP ap-4 serves FWD-39. |

## 3. ENRICHMENT LIST (round 34, ONE issuance by `2.0.0_SA_COO~D`)

1. **The served-build walk:** a local build of PROD dbd29c6320 against the live API (lPTMo20T). Each item names the outcomes it
   evidences:
   - every tab on BA, VLO and AMD, with the day dialog CLOSED before each tab;
   - one non-USD name's header (FWD-4, FWD-13);
   - one name whose filing lists no officers (FWD-7);
   - the six-state ui-smoke capture on the redesigned panels (FWD-19, FWD-20);
   - the overlay's "not served" DOM census with its positive control, on 3 names (FWD-24);
   - a display-name census across every tab on today's data (FWD-27);
   - hover reads where a DONE WHEN names a hover (FWD-5 tooltip, FWD-21 shortened labels).
2. **The repair cell:**
   - FWD-21's 90D/365D label collisions (no label crossed by a leader line or overlapping a bubble);
   - FWD-27's header move names its window;
   - What-changed changes print at the row's display precision;
   - the timeline axis labels' contrast (2.18:1 measured), up to the panel ink law.
3. **After RESAPP ap-4:** the FWD-5 word-cloud render cell.

## 4. ACTS FOR ANDREW (cited)

- FWD-1: his own signed-in read of /security-analysis on PROD (his login).
