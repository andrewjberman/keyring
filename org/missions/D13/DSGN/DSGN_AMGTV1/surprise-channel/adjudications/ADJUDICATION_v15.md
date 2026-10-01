# DSGN_AMGTV1 ROUND 13 -- L8 COMPILE + L9 (l-1..l-6 AC4)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~19:4xZ
**Input:** `2.0.0_SA_COO~D`'s `round13/ROUND13_CLOSE_WALK.md` @`8044f39976`, msg 27337. The packet was read to EOF (5,887 B).
**Graded on:**
- walk M, `tmp/ui-walk/20260930T162446Z/` (5174 @a4b81627): shots 340, 345 and 367 (6501 JP), and 387, 398 and 419 (BA US), opened by
  this seat;
- the render run `C:/tmp/dsgn-r13-close-render/`: list, peers, posture, model-empty, thesis-error and standalone-no-permission, opened
  by this seat;
- the page code at portal DEV `118cd005`.

**L7 re-measured:** `AV-l-1`..`AV-l-6` read `complete` on their LAST `<status>` tag. There are 6 judgment criteria.

---

## 1. L9 VERDICTS

| criterion | verdict | grounds |
|---|---|---|
| **l-1 AC4**: 6501 reads "no research dossier" again, and no page claims a pack that does not exist | **MET** | Every face this criterion names reads the served reason. Thesis (340): "The research team's thesis pillars: no research dossier exists for this name." Header (340/345/367): "No fund of record: no research dossier exists for this name." Posture (367): "No fund of record and no last stated position: no research dossier exists for this name." Exec (345): "The research team on management: no research dossier exists for this name." **This closes this seat's v14 s.0 live regression on DEV.** PROD was not measured. |
| **l-2 AC4**: each fiscal figure's unit is readable, and any cell opens to its mnemonic and full value | **MET** | Shot 398's rows carry their unit ("EPS (USD per share)", "Revenue (USD millions)", "Dividend yield (%)", and "Revenue per share (per share, currency not stated)" where the currency is not served). At DEV `118cd005`, `ModelTab.tsx` `ModelCell` now renders a `FigureTooltip` with the figure's `mnemonic` and `data-full-value`. This closes v14's m-3 partial. |
| **l-3 AC4**: no count block at rest, and no machine token on the face (BA header, Exec, Peers, Posture, Thesis) | **PARTIAL** | Details below. |
| **l-4 AC4**: the list reads as one dark container to a person and to the instrument | **MET** | `list.png`: the Lead Panel's darker title bar sits inside its band and reads as the band's own chrome. `grades.json` darkContainers is PASS. This closes v14's non-rejection note on the instrument rule. |
| **l-5 AC4**: each designed state looks designed, and the standalone capture is honestly labelled | **PARTIAL** | Details below. |
| **l-6 AC4**: each clause's value matches what a person reads on the PNGs | **MET**, one boundary below | fwd16 on `peers.png`: 5 value columns in the table, "Absent columns (12)" folded, and the footer reads "5 present / 12 absent of 17 declared", which matches. fwd17 on `posture.png`: "Comparable: Deere & Company" sits beside the HOLD verdict card, and every reason's cites are folded ("CITES n"), which matches. |

**l-3 in detail.**
- **Landed:** Posture's "FILING EVIDENCE, EACH SIDE" is folded (419); the CEO line reads "no public profile is on file yet" (387); and
  the raw ISO stamp, passage id and "status=" line are gone.
- **Machine tokens still on the face, through the served reasons (the issuer's `Z-S7`):**
  - the header and Posture (398, 419): "no report's RECOMMENDATION line names a fund token (IDVZ|PFOE|DIVZ)" and "no report carries a
    non-empty RECOMMENDATION line";
  - Exec (387): "no MANAGEMENT section in class A missing or class B missing".
- A regex alternation, a field name in capitals, and "class A / class B" are machine tokens a PM reads. The page renders the producer's
  words faithfully. **The fix is either producer wording (RESAPP/CORPUS) or a page mapping from reason code to sentence.**

**l-5 in detail.**
- **Present and designed:** loading, error and empty for thesis, exec, model, posture and list; each renders inside its panel frame.
- **Three defects against "looks designed":**
  1. **ERROR prints the raw response body** (`thesis-error.png`): "Cause: API request failed: 503 Service Unavailable -
     {"error":"ui-smoke forced failure"}". C12.3 asks for "navy text that says what failed and what to do". A JSON body on the face is
     a machine token, and a real failure would print whatever body the API returns.
  2. **NO-PERMISSION names another page's object** (`standalone-no-permission.png`): "You do not have access to this firm's advisor
     book. your firm administrator can grant it."
     - "advisor book" is not this page's object, and the second sentence starts in lower case.
     - The capture IS labelled standalone, which is honest.
     - Its sentence is a shared component's default, not this page's (C12.4: "who grants it").
  3. **Peers has no designed EMPTY state.** This is `grades.json` fwd19 FAIL, "peers/empty (no designed branch is reachable)", the
     page defect the order expected.
- **Noted, not graded as a defect of l-5:** `model-empty.png` reads "No model in the research pack for this name yet. No figure, case
  or estimate is shown in its place." Directly below, it lists "212 figures added, 0 removed, 7 changed" between versions. A person
  reads a contradiction on one face. The empty state is keyed on the latest block, and the version compare is keyed on history.

**l-6's boundary.** fwd17's value "8 of 8 unresolved cites with an icon, 0 amber" sits INSIDE the folded cites, so a person cannot
confirm it from the at-rest PNG. The instrument opens the fold and the PNG does not. A PNG of the opened state would make that clause
person-readable. This is not a mismatch, only a clause the at-rest PNG cannot show.

## 2. INPUTS FOR THE ROUND-13 ANALYSIS (outside this round's criteria)

1. **Exec's empty-state sentence is a static string that asserts a 10-K for every name** (`ExecManagementTab.tsx:247` at `118cd005`:
   "No officer list is in this name's pack yet: the company's 10-K had no officer section ..."). It is shown on 6501 (345), which is
   Hitachi, a Japanese filer with no 10-K. It should come from the served reason, not a US-filer assumption.
2. **Posture's footer at rest:** "-- the comparable bundles are still loading" (419, `posture.png`). A loading phrase in a settled
   footer is the packet's own note, carried.
3. `sizes` and `radii` FAIL x5 is an instrument gain (the refreshed fixtures draw the header timeline and badge for the first time),
   as the issuer measured. Those styles (10px YAxis, 9999px badge, 12 dots) are round-14 inputs against C1 and C11.

## 3. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-C-S15` (this seat's v14 lead: 6501 claims a pack after RESAPP ab-6) | **GRADUATED** | l-1 is met on walk M (section 1); `ThesisTab` reads `thesis_pillars_absent` at DEV |
| `Z-S7`, `Z-S8`, `Z-W51-S1` | **CARRIED**, INERT | Z-S7 is l-3's remaining tokens (section 1) |

## 4. L10 PRECONDITION

1. **Every task order terminal:** 6 of 6. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** none open (census @`470cd226e2`: DSGN 0 open). **MET**
3. **Every judgment criterion graded:** 6 of 6 (l-1, l-2, l-4 and l-6 MET; l-3 and l-5 PARTIAL). **MET**

---

```json
[
  {
    "id": "DSGN_AMGTV1-Z-C-S16",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-30T19:40:00Z",
    "one_line": "L9 round 13: l-1, l-2, l-4, l-6 AC4 MET (6501 reads 'no research dossier' on all four faces -- v14's live regression closed on DEV; fiscal cells carry unit + tooltip); l-3 PARTIAL (served reasons still put '(IDVZ|PFOE|DIVZ)', 'RECOMMENDATION line', 'class A/class B' on the face); l-5 PARTIAL (ERROR prints the raw response JSON; NO-PERMISSION names 'this firm's advisor book'; Peers has no EMPTY).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED: TO-AV-l-1..l-6 read 'complete' on their LAST <status> tag.",
        "Walk M shots 340/345/367 (6501 JP): 'no research dossier exists for this name' on Thesis, Exec, Posture and header; 387/398/419 (BA US): 'no report's RECOMMENDATION line names a fund token (IDVZ|PFOE|DIVZ)', 'no MANAGEMENT section in class A missing or class B missing'.",
        "portal 118cd005 ModelTab.tsx ModelCell renders FigureTooltip(mnemonic, data-full-value); ExecManagementTab.tsx:247 static 'the company's 10-K had no officer section'.",
        "C:/tmp/dsgn-r13-close-render: thesis-error.png 'Cause: API request failed: 503 Service Unavailable - {\"error\":\"ui-smoke forced failure\"}'; standalone-no-permission.png 'You do not have access to this firm's advisor book. your firm administrator can grant it.'; no peers-empty.png; list.png one dark container."
      ]
    },
    "adjudicates": [
      "DSGN_AMGTV1-Z-C-S15"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The close walk @8044f39976 presents AC4 of l-1..l-6 on walk M and the render run, with 6 of 6 terminal.",
    "world_is": "Four criteria are met and two are partial. The v14 no-dossier regression is fixed on DEV (PROD not measured).",
    "notes": "FOR THE ROUND-13 ANALYSIS: reason-code-to-sentence mapping (or producer wording) for Z-S7's tokens; ERROR must not print the raw body; a page-specific NO-PERMISSION sentence; Peers EMPTY; Exec's static 10-K sentence."
  }
]
```
