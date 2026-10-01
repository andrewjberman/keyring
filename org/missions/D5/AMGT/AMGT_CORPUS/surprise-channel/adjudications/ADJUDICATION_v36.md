# AMGT_CORPUS ROUND 31 -- L8 COMPILE (one issuer direct act; no judgment criterion)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-01 ~10:3xZ
**Input:** `2.0.0_SA_COO~X`'s `ROUND31_DRAIN_END_PACKET.md` @`b958b0058d` (2,406 B, read to EOF), msg 27757.
**L7:** `CRPS-ag-1` is an issuer direct act (portal `c6aacc68`, `ModelTab.tsx`, 5 lines), graded by `checks/round31/face31.cjs`
(base 2 of 4, after 4 of 4). No judgment criterion.
**Read by this seat:** `tmp/ui-walk/20261001T102125Z/shots/030-BA-Model.png`.

---

## 1. RE-READ BY THIS SEAT

- The growth line reads **"No year-on-year growth rows: the model block serves none and this page computes none."** It now names
  the model block where it presupposed a pack (v35 section 1's residue, closed).
- The footer reads "Showing 147 fiscal figures from the model block".
- **No "pack" appears anywhere on BA's Model tab** as read on the PNG (subtitle, sheet, footnote, growth line, team-case lines,
  footer, versions, what-moved, inputs). The packet's census reasoning (keep "the research team's pack" only inside a SERVED team
  case, where the workbook is real) is sound, and BA serves no team case, so its absence here is expected.
- Rounds 28-30 stand: "CONSENSUS (BLOOMBERG)", per-row precision, "Figures in USD" once, the four marked rows and their footnote.

**Outside this cell, noticed on the same PNG** (header, DSGN and RESAPP surfaces): the readings line now says "chatter: ranked
October 1st, 2026 (1 names)". That is a plural mismatch, and today's chatter ranking carries one name. Not CORPUS's; noted for the
owners' rounds.

## 2. THE FINDING THE PACKET ROUTES

DSGN's frozen round-14 `modelhistory.cjs` reads 1 of 3 at base because it anchors the pre-round-28 empty sentence. This is a
cross-project check drift from CORPUS's wording change, told to `2.0.0_SA_COO~D`. The history framing itself holds (face31 arm 4).
It is DSGN's to re-anchor; it is no defect in this round.

## 3. DISPOSITIONS

No new rows. `Z-S74` and `Z-S76`'s producer label are carried past Friday.

## 4. L10 PRECONDITION

1. **Every task order terminal:** the one cell is a landed direct act. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** none open. **MET (vacuous)**
3. **Every judgment criterion graded:** 0. **MET (vacuous)**

**CORPUS's Friday face, as this seat has read it across rounds 28-31:** the sheet's shape, labelled consensus, sheet precision, one
currency statement, and no presupposed pack. It is complete on local DEV `c6aacc68`. It reaches PROD only after site-Z DEV reaches
origin (v35 section 2).

---

```json
[
  {
    "id": "AMGT_CORPUS-Z-C-S37",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-01T10:35:00Z",
    "one_line": "L8 round 31: BA's Model tab carries no 'pack' anywhere (growth line now 'the model block serves none and this page computes none'); rounds 28-30 stand; CORPUS's Friday face complete on local DEV c6aacc68; outside CORPUS, the header reads 'chatter: ranked October 1st, 2026 (1 names)'.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7: CRPS-ag-1 is an issuer direct act, portal c6aacc68 (ModelTab.tsx), face31.cjs base 2/4 -> 4/4 per the packet.",
        "tmp/ui-walk/20261001T102125Z/shots/030-BA-Model.png: 'No year-on-year growth rows: the model block serves none and this page computes none.'; 'Showing 147 fiscal figures from the model block'; no 'pack' string on the Model tab; header readings 'chatter: ranked October 1st, 2026 (1 names)'."
      ]
    },
    "adjudicates": [
      "AMGT_CORPUS-Z-C-S36"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet @b958b0058d asserts every visible 'pack' presupposition on the Model tab reworded and none left on BA's real run.",
    "world_is": "True on the PNG.",
    "notes": "FOR THE ROUND-31 ANALYSIS: CORPUS's Friday face is done on local DEV; DSGN re-anchors modelhistory.cjs; the '(1 names)' header line belongs to its writer."
  }
]
```
