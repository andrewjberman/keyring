# IRPT_BCKEND -- round 96 L8 adjudication (~P)

<sweep_watermark>2026-10-09T05:18Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2; tree on box/dell2), 2026-10-09 ~05:2xZ. L8 input: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_96_P_DRAIN_END_20261009.md @6dea768ce8` (msg 2494). IB-pr-387 complete,
0 judgment criteria, MAY-CLOSE. 1 row dismissed below; D2-W198-S2 graduates OPEN in `remediations/REMEDIATION_v36.md`. ARMED: 0.

**For the analysis:** a lone `ALL` string is left unrestricted at `served.py` and is refused only downstream (uploads.py INVALID_INPUT).
C-FIRM says ALL never admits; that holds per route only where a downstream check exists. D2-W198-S2 asks for the rule to be proven
on every route behind `served.py`, or for a lone `ALL` to fail closed there.

```json
[
  {
    "id": "IRPT_BCKEND-C-S321",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T05:18:25Z",
    "one_line": "Round 96 row dismissed: D2-W198-S1 (IB96-1-AC2's whole-suite clause could not be met while 4 drained tests asserted the behaviour IB-pr-387 removes; AMENDMENT 1 @f237da2821 granted the two files and the change is tighten-only -- two admissions became refusals; _authz 303 of 303).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-D2-W198-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "IB-pr-387 complete under AMENDMENT 1, drained @da8abeb411; round-close-check --round 96 MAY-CLOSE (this seat's read). D2-S27 belongs to round 94 (IB-pr-383, open) and waits for it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row IRPT_BCKEND-D2-W198-S1",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_96_P_DRAIN_END_20261009.md @6dea768ce8"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Resolved by an issuer amendment that only tightens."
  }
]
```
