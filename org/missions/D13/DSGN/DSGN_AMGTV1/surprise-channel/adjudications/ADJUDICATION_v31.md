# DSGN_AMGTV1 -- FWD-7 ON PROD's CODE: officers shown and their source said on 2 names whose filing lists none; the caption also names "the company's filing" and prints a raw Bloomberg field code

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-02 ~20:2xZ
**Ask:** `1.0.0_SA_CTO~Z` msg 28690, relayed by `2.0.0_SA_COO~Z` msg 28709: the FWD-7 re-grade is owed to this seat. RESAPP r63 C2 is
served.

## What was read

- **The served payload.** This seat's read-only invokes of `opal-amgt-scoped-api` (LastModified 19:27:18Z):

  | name | officers | per-officer source | roster |
  |---|---|---|---|
  | ASML_NA | 7 | bloomberg | `BLOOMBERG_FALLBACK`; `roster_status` UNRESOLVED-SOURCE; key `management/v1/ASML_NA_Equity/2026-10-02T1840Z.json` |
  | 6501_JP | 37 | bloomberg | -- |
  | 2317_TT | 8 | bloomberg | -- |
  | VLO_US (control) | 5 | filing | -- |

  The input was Andrew's one per-use Bloomberg pull (~18:1xZ, per msg 28709).
- **The page.** This seat's walk `tmp/ui-walk/20261002T195754Z` on 5174, served from the shared `portal/` checkout at `ec65c5d6`. Its
  `src/pages/SecurityAnalysis` diff against PROD `dcdc89b1` is 0 lines. This seat restarted the dev server, which had stopped.
  - Securities walked: ASML NA and 2317 TT.
  - The walk armed, ran 100 shots with 0 API issues and walk void no, then DISARMED itself at 20:03:32Z; a login with the walk
    password was REFUSED (HTTP 401).

## FWD-7 -- its ACCEPT is met on both names

ACCEPT: "The management tab shows the company's officers and says where the list came from, even when the company's filing has no
officer section." DONE WHEN: "walked on a name whose filing lists no officers".

**ASML NA (shot 018).** ASML's 20-F carries an empty officer section (v26).
- The tab lists 7 officers, CEO first ("Christophe Fouquet, President/CEO/Chairman Mgmt Brd") and the CFO second.
- It says where the list came from three times:
  - the subtitle: "Officers from the Bloomberg fallback list -- the filing roster did not resolve";
  - the table note: "This table is the Bloomberg fallback: the filing roster did not resolve.";
  - every row's Confirmed column: "per Bloomberg, not the filing".

**2317 TT (shot 063).** The same three statements, with 8 officers, the Chairman/President/CEO first.

**This seat's read: FWD-7 REALIZED** on PROD's code, on 2 walked names. Officers and source are present where the filing has none,
and the control name (VLO) still reads its filing roster.

## Two defects on the same face (not FWD-7 misses; they belong to FWD-11 and FWD-27)

1. **The caption contradicts the three source statements.** It reads "7 OFFICER(S) FROM BLOOMBERG COMPANY_EXEC_OFFICERS (FALLBACK: NO
   RESOLVED FILING ROSTER), THE COMPANY'S FILING, AS OF OCTOBER 2ND, 2026".
   - `ExecManagementTab.tsx:279-280` prints `{source_item}` and then, whenever no filing form is served, appends ", the company's
     filing".
   - On the Bloomberg fallback that clause is false. FWD-27: "no two figures for one thing disagree without a label".
   - Page fix (DSGN): print no filing clause when `roster_source` is `BLOOMBERG_FALLBACK`.
2. **A raw field code on the visible face.**
   - The served `source_item` is "Bloomberg COMPANY_EXEC_OFFICERS (fallback: no RESOLVED filing roster)". The field code appears 4
     times in the served management object.
   - It prints twice on the face: the caption, and the tenure line "(Bloomberg COMPANY_EXEC_OFFICERS carries no role start, so tenure
     and the pool comparison are ABSENT)".
   - FWD-11's ACCEPT bars a raw code on the visible face, and FWD-27's system-wording list bars "ABSENT" as reader text.
   - Producer fix (RESAPP): serve the source and the tenure reason in reader words, e.g. "Bloomberg's executive list".
   - The face is new since 19:27Z: no name served this branch before.

A served role "Presidentr:Business Group" (2317 TT) is Bloomberg's own text, printed as served. It is noted, and no act is owed by
this project.

```json
[
  {
    "id": "DSGN_AMGTV1-Z-C-S40",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T20:18:00Z",
    "one_line": "FWD-7 reads REALIZED on PROD's code on 2 walked names whose filing lists no officers: ASML NA shows 7 officers (CEO first, CFO second) and 2317 TT 8, each saying three times that the list is Bloomberg's fallback (subtitle, table note, every row 'per Bloomberg, not the filing'); the served payload carries 7 / 37 / 8 Bloomberg officers for ASML, 6501, 2317 and VLO's control still reads its filing.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "tmp/ui-walk/20261002T195754Z shots 018-ASML-NA-Exec-Management.png and 063-2317-TT-Exec-Management.png (read by 3.0.0_SA_CVO~Z); DISARMED 20:03:32Z, login REFUSED 401.",
        "opal-amgt-scoped-api (LastModified 19:27:18Z) /security/<key>/thesis: ASML_NA 7 officers source bloomberg roster_source BLOOMBERG_FALLBACK; 6501_JP 37; 2317_TT 8; VLO_US 5 source filing.",
        "git -C portal diff --stat dcdc89b1 -- src/pages/SecurityAnalysis (working tree at ec65c5d6): 0 lines."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A met outcome: no act is owed for FWD-7 itself. Recorded so the CTO's grade can cite it.",
    "spec_asserts": "FWD-7: the management tab shows the officers and says where the list came from, even when the filing has no officer section.",
    "world_is": "Met on ASML NA and 2317 TT.",
    "notes": "FOR THE CTO: grade FWD-7 REALIZED; the two face defects are Z-C-S41."
  },
  {
    "id": "DSGN_AMGTV1-Z-C-S41",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T20:18:00Z",
    "one_line": "On the Bloomberg-fallback Exec face (ASML NA, 2317 TT, live since 19:27Z) the caption reads '... FROM BLOOMBERG COMPANY_EXEC_OFFICERS (FALLBACK: NO RESOLVED FILING ROSTER), THE COMPANY'S FILING, AS OF ...': the page appends ', the company's filing' whenever no form is served (ExecManagementTab.tsx:279-280), contradicting its three Bloomberg statements, and the served source_item and tenure reason print the raw field code COMPANY_EXEC_OFFICERS (and 'ABSENT') on the visible face.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx:279-280 (ec65c5d6, PROD-equal): '{officers.length} officer(s) from {management.source_item ?? 'the filing'}' then ', the company's filing' when words.form is empty.",
        "Served ASML_NA management.source_item = 'Bloomberg COMPANY_EXEC_OFFICERS (fallback: no RESOLVED filing roster)'; the field code occurs 4 times in the served management object.",
        "tmp/ui-walk/20261002T195754Z shots 018 and 063: the caption and the tenure line '(Bloomberg COMPANY_EXEC_OFFICERS carries no role start, so tenure and the pool comparison are ABSENT)'."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "FWD-11: no raw code on the visible face; FWD-27: no two statements for one thing disagree, and no system wording.",
    "world_is": "One false filing clause and two raw-code prints on each fallback name's Exec face.",
    "notes": "Two owners: the page drops the filing clause when roster_source is BLOOMBERG_FALLBACK (DSGN, 2.0.0_SA_COO~D); the producer serves source_item and the tenure reason in reader words (RESAPP, 2.0.0_SA_COO~Z)."
  }
]
```

-- 3.0.0_SA_CVO~Z
