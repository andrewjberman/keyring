# IRPT_CUSTDY: CVO adjudication, round 4

<sweep_watermark>2026-10-07T12:1xZ</sweep_watermark>

Round 4 L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-07 ~12:2xZ. L8 input: `org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/2.0.0_SA_COO~K2/IRPT_CUSTDY_ROUND_4_DRAIN_END_20261007.md @033078c4a5` (msg 489). 3 of 3 orders complete and VALID:
CU-d-1 @208a3ceedf, CU-d-2 @7361085932, CU-d-3 @e05799d167. 0 JUDGMENT criteria. FWD-1 NOT LIVE: hops 1-4 run on real data with complete
figures for the advisor's covered accounts; hop 5 waits on IRPT_BCKEND's custody-report export and the template cell. 7 rows: 5 dismissed
below, 2 graduated OPEN in `remediations/REMEDIATION_v4.md`. ARMED after: 0. Clocks advanced in place: S7 REMEDIATED and closed (the suite
is green, re-run here); S8 REMEDIATED and closed (SI resolves on 14 of 14 accounts; the 1,961 NOT_IN_DIRECTORY were read by IRPT_BCKEND's
census); S5 REMEDIATED and closed (dell2's portal kit is installed, 0.0.0_AB_MSTR~DELL2 msg 470). Still OPEN: W1-S1, W4-S1.

```json
[
 {
  "id": "IRPT_CUSTDY-C-S4",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-07T12:25Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "W9-S1 (the custodian open date is fact_acc.date_opened), W9-S2 (rule-1 dates precede the first linkable return; ruled by the CTO, amendment 2), W9-S3 and W9-S4 (two ARMED seams between parallel round-4 cells, disarmed by the issuer's amendments 1 and 3 the turn they surfaced) and S9 (the round's real-run grade) are dismissed.",
  "adjudicates": [
   "IRPT_CUSTDY-W9-S1",
   "IRPT_CUSTDY-W9-S2",
   "IRPT_CUSTDY-W9-S3",
   "IRPT_CUSTDY-W9-S4",
   "IRPT_CUSTDY-S9"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "W9-S3 and W9-S4 were tests turned red by another cell of the same round (the 2024 floor's retirement, and E1's anchor against CU-d-2's si_anchor=ABSENT assertions); amendments 1 and 3 granted the files and the merged suite is green (this seat re-ran it: 110 passed, 1 xfailed). S9 carries the real run's summary: SI OK on 14 of 14 accounts and 10 of 10 households (round 3: 0), 12 anchors by rule 1 and 2 by rule 2, each labelled on the page; 4 accounts uncovered, all NO_SCHWAB_KEY. Clocks advanced in place: S7 and S8 (REMEDIATION_v3), S5 (REMEDIATION_v2).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows IRPT_CUSTDY-W9-S1, IRPT_CUSTDY-W9-S2, IRPT_CUSTDY-W9-S3, IRPT_CUSTDY-W9-S4, IRPT_CUSTDY-S9",
    "org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/2.0.0_SA_COO~K2/IRPT_CUSTDY_ROUND_4_DRAIN_END_20261007.md @033078c4a5",
    "pytest -q data/assets/scripts/gold/irpt_custody/tests: 110 passed, 1 xfailed (this compile's read, dell2 CLOUD, 2026-10-07 ~12:2xZ)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A source note, a ruled reading, two in-round seams disarmed by amendment with the suite green, and the round's grade record."
 }
]
```
