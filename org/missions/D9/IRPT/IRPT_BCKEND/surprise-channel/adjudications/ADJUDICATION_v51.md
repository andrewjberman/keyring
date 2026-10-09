# IRPT_BCKEND -- rounds 94, 107 and 109-113 L8 adjudication (~P), and the directory release landed

<sweep_watermark>2026-10-09T14:31Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2; tree on box/dell2), 2026-10-09 ~14:3xZ. L8 input: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_109_113_P_DRAIN_END_20261009.md @32526fbde0 (msg 3453)`, with the runner landing read `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/s392/runner_landing_read_20261009.json @13cee15f72`.
0 judgment criteria; every round MAY-CLOSE. 13 rows dismissed below; 5 REMEDIATION_v34 rows closed in place, the four ARMED directory rows
disarmed by measurement; 3 graduate OPEN in `remediations/REMEDIATION_v39.md`. ARMED: 0 in these rounds.

**For the analysis:**
1. **The directory release is live at all three firms** (IB-pr-383 closed). Cottonwood's OVER_AGE deadline (2026-10-12) is averted, and
   Inflection carries its terminated account instead of a false 294 additions -- measured on the served objects.
2. **IB-pr-409 (narrative) has both halves**; its apply through IB-pr-401 completes TCKT_VNEXT's 27th route.
3. **A cleanup rule learned:** content-addressed retention rows are shared; walk the dependency tree before naming a key to delete (D2-S51).

```json
[
  {
    "id": "IRPT_BCKEND-C-S327",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T14:31:35Z",
    "one_line": "Rounds 94, 107 and 109-113 rows dismissed: D2-S22 (stale skeleton header, resolved by D2-S23), D2-S25 with D2-S55 and D2-S27 (the runner-host SendCommand refusal -- the grant landed and two live sends returned rc 0), D2-S29 (ARMED: the bundle was overwritten before seeding -- IB-pr-383 re-replayed against the live bundle and seeded 2 firms / 4 objects, ledger closed), D2-W269-S1 with D2-S53 (the e56 + IB-pr-403 bundle made the FWD-14 gate refuse -- IB-pr-410 keeps ticker= on SmartX nodes and the gate publishes both trees, 0 of 116,815 class lost), D2-W271-S1 and D2-W273-S1 (the red _contracts bisect: 5 fixed, 4 named -- carried by D2-S46), D2-W272-S1 with D2-S54 (ARMED: a row-listed internal caller classes OPAL_GLOBAL -- signed as built by the CTO, matching the six IB-pr-390 hosts), D2-S51 (the Y75 cleanup deleted a content-addressed retention row three later TEST requests share -- ruled no restore, the cleanup rule now walks the retention dependency tree first), D2-W275-S1 (no standalone document schema for the custody read; the response contracts carry the type). Closed in place, clocks only: D2-S13, D2-W187-S1, D2-W188-S1, D2-W188-S2, D2-W189-S1 (the four ARMED directory rows disarmed at 13:40:53Z by measurement).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-D2-S22",
      "IRPT_BCKEND-D2-S25",
      "IRPT_BCKEND-D2-S55",
      "IRPT_BCKEND-D2-S27",
      "IRPT_BCKEND-D2-S29",
      "IRPT_BCKEND-D2-W269-S1",
      "IRPT_BCKEND-D2-S53",
      "IRPT_BCKEND-D2-W271-S1",
      "IRPT_BCKEND-D2-W272-S1",
      "IRPT_BCKEND-D2-S54",
      "IRPT_BCKEND-D2-S51",
      "IRPT_BCKEND-D2-W273-S1",
      "IRPT_BCKEND-D2-W275-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "this seat's reads ~14:3xZ: each firm's served investor-reporting/directory/latest.json moved again at 14:11Z (49financial 4,725 entries as of 2026-10-08; cottonwood 271 as of 2026-10-08; inflection 295 as of 2026-10-09); inflection's dated directory carries carried_forward {terminated 1, held_in_source 0} with 294 ACTIVE entries and 1 TERMINATED -- not a false 294 additions; cottonwood landed well before its 2026-10-12 OVER_AGE; round-close-check MAY-CLOSE for rounds 94, 107, 109, 110, 111, 112, 113.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-S22, D2-S25, D2-S55, D2-S27, D2-S29, D2-W269-S1, D2-S53, D2-W271-S1, D2-W272-S1, D2-S54, D2-S51, D2-W273-S1, D2-W275-S1",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_109_113_P_DRAIN_END_20261009.md @32526fbde0 (msg 3453)",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/s392/runner_landing_read_20261009.json @13cee15f72",
        "this seat's reads ~14:3xZ: each firm's served investor-reporting/directory/latest.json moved again at 14:11Z (49financial 4,725 entries as of 2026-10-08; cottonwood 271 as of 2026-10-08; inflection 295 as of 2026-10-09); inflection's dated directory carries carried_forward {terminated 1, held_in_source 0} with 294 ACTIVE entries and 1 TERMINATED -- not a false 294 additions; cottonwood landed well before its 2026-10-12 OVER_AGE; round-close-check MAY-CLOSE for rounds 94, 107, 109, 110, 111, 112, 113"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Resolved by grants, re-replays, later cells, rulings, or measured landings."
  }
]
```
