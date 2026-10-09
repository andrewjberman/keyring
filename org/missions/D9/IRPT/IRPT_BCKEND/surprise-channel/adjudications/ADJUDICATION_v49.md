# IRPT_BCKEND -- rounds 106 and 108 L8 adjudication (~P)

<sweep_watermark>2026-10-09T12:14Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2; tree on box/dell2), 2026-10-09 ~12:1xZ. L8 input: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_106_108_P_DRAIN_END_20261009.md @2f6fe31ad8 (msg 3251)`. 0 judgment criteria.
7 rows dismissed below; D2-S46 and D2-W268-S1 graduate OPEN in `remediations/REMEDIATION_v38.md`. ARMED: 0 in these rounds.

**For the analysis:** 9 `_contracts` tests are red at HEAD from other cells' in-flight work (D2-S46). A red suite at HEAD hides the next
regression; it needs one owner and a date.

```json
[
  {
    "id": "IRPT_BCKEND-C-S325",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T12:14:35Z",
    "one_line": "Rounds 106 and 108 rows dismissed: D2-S43 with its resolution D2-S47 (the unguarded census passes at HEAD once /original is declared), D2-S44 (the packet's python -I invocation cannot import its modules; the run used the interpreter that can, recorded), D2-W268-S2 with its disarm D2-S45 (ARMED: the irpt-status candidate changes 10 members vs live; no IB-pr-405 apply is cut until its pair rules on the 7 foreign members), D2-W268-S3 (the include option unpublished -- published by IB-pr-407), D2-W270-S1 (IB108-1-AC3 reads the response schema's own properties, not the $ref; the data-level sibling points at the definition -- as built).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-D2-S43",
      "IRPT_BCKEND-D2-S47",
      "IRPT_BCKEND-D2-S44",
      "IRPT_BCKEND-D2-W268-S2",
      "IRPT_BCKEND-D2-S45",
      "IRPT_BCKEND-D2-W268-S3",
      "IRPT_BCKEND-D2-W270-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "round-close-check MAY-CLOSE for rounds 105, 106, 107 and 108 (this seat's reads); IB-pr-405 and IB-pr-407 complete 3/3, not released (irpt-status waits on IRPT_ANLREQ release 1's after-reads, CTO ADDENDUM 17).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-S43, D2-S47, D2-S44, D2-W268-S2, D2-S45, D2-W268-S3, D2-W270-S1",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_106_108_P_DRAIN_END_20261009.md @2f6fe31ad8 (msg 3251)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Resolved by a later cell, disarmed by a hold, or a recorded tooling note."
  }
]
```
