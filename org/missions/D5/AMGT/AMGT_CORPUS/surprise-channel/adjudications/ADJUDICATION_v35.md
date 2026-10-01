# AMGT_CORPUS ROUND 30 -- L8 COMPILE (one issuer direct act; no judgment criterion)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-01 ~10:1xZ
**Input:** `2.0.0_SA_COO~X`'s `ROUND30_DRAIN_END_PACKET.md` @`18e8b11e4d` (2,578 B, read to EOF), msg 27731.
**L7:** `CRPS-af-1` is an issuer direct act (portal `2a0e1b7a`, `ModelTab.tsx`, 4 lines), graded by `checks/round30/face30.cjs`
(base 1 of 4, after 4 of 4). No order file, no judgment criterion.
**Read by this seat:** `tmp/ui-walk/20261001T095654Z/shots/030-BA-Model.png`.

---

## 1. RE-READ BY THIS SEAT

- The footer under the team-case lines reads **"Showing 147 fiscal figures from the model block"**. No "of N ... rendered" and no
  "not in the pack" appears on the Model face.
- Round 29's sheet stands unchanged (ADJUDICATION_v34): "Reported figures and Bloomberg consensus estimates, from the model block";
  "CONSENSUS (BLOOMBERG)" over 2026E-2028E; per-row precision; "Figures in USD" once; four marked rows with one footnote.
- **The residue the issuer named, confirmed on the PNG:** "No year-on-year growth rows: the pack carries none and this page computes
  none." still sits above the team cases and presupposes a pack. One sentence, outside ruling 1's literal scope; the CTO's call.

## 2. A FACT FOR THE PROMOTE

The packet records push state LOCAL: origin CLOUD `0abf99fcd4` and origin portal DEV `2879d65b` carry none of CORPUS rounds 28-30's
portal commits (chain through `2a0e1b7a`). The same holds for DSGN rounds 14-16's portal work on site-Z DEV (their close records:
LOCAL). A DEV-to-PROD promote by 23:59 ET is cut from origin DEV, so these rounds reach PROD only after `0.0.0_AB_MSTR~Z` pushes
site-Z DEV. That is the integrator's act on Andrew's word, not a finding against this round.

## 3. DISPOSITIONS

No new rows. `Z-S74` (INERT) and `Z-S76`'s producer label are carried past Friday per the round-29 analysis.

## 4. L10 PRECONDITION

1. **Every task order terminal:** the round's one cell is a landed direct act. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** none open. **MET (vacuous)**
3. **Every judgment criterion graded:** 0. **MET (vacuous)**

---

```json
[
  {
    "id": "AMGT_CORPUS-Z-C-S36",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-01T10:10:00Z",
    "one_line": "L8 round 30: BA's Model footer reads 'Showing 147 fiscal figures from the model block' (no 'of N rendered', no 'not in the pack'); round 29's sheet stands; residue confirmed: 'No year-on-year growth rows: the pack carries none ...' still presupposes a pack; push state LOCAL -- origin portal DEV 2879d65b carries none of CORPUS r28-30, so a PROD promote needs MSTR's push first.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7: CRPS-af-1 is an issuer direct act, portal 2a0e1b7a (ModelTab.tsx), face30.cjs base 1/4 -> 4/4 per the packet.",
        "tmp/ui-walk/20261001T095654Z/shots/030-BA-Model.png: 'Showing 147 fiscal figures from the model block'; 'No year-on-year growth rows: the pack carries none and this page computes none.'; 'CONSENSUS (BLOOMBERG)'; 'Figures in USD'.",
        "Packet @18e8b11e4d push state: origin CLOUD 0abf99fcd4; origin portal DEV 2879d65b does not carry rounds 28-30."
      ]
    },
    "adjudicates": [
      "AMGT_CORPUS-Z-S74"
    ],
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The drain-end packet @18e8b11e4d asserts the footer re-worded, its two sibling lines re-worded, and one residue named.",
    "world_is": "True on the PNG; the growth-rows line still presupposes a pack; none of this is on origin portal DEV yet.",
    "notes": "FOR THE ROUND-30 ANALYSIS: the growth-rows sentence if a further face cell is wanted before 22:00Z; the PROD promote waits on site-Z DEV reaching origin."
  }
]
```
