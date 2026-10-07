# ADVI_COTBKF: CVO adjudication, round 5

<sweep_watermark>2026-10-07T09:15Z</sweep_watermark>

Round 5 L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-07 ~09:2xZ. L8 input: `deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_5_DRAIN_END_20261007.md @453e5e0b3a` (msg 236). 3 of 3 orders complete and VALID:
CB-e-1 @9014a21b22, CB-e-3 @9fea452b9d, CB-e-4 @ece9baad7a. 0 JUDGMENT criteria. 5 rows: the round's S10, S11, W19-S1 and S12, and S9, which
this seat filed at round 4 and compiles here. 2 dismissed by C-S11 below; 3 graduated in `remediations/REMEDIATION_v3.md`, all OPEN. ARMED
after: S9 and S12 (both BLOCKING) and W12-S1 (carried from REMEDIATION_v2). No --apply ran this round.

```json
[
 {
  "id": "ADVI_COTBKF-C-S11",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-07T09:25Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "S10 (S9's cause measured by its disarm owner) and S11 (the ruling-C list of this lane's calendar-dependent artifacts on dell2) are dismissed; their effects are carried on S9 and W12-S1.",
  "adjudicates": [
   "ADVI_COTBKF-S10",
   "ADVI_COTBKF-S11"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "S10: with NYSE_HOLIDAYS_FALLBACK extended in-process to 2010-2023, the dell2 run of commonwealth_account_links.py equals the laptop deliverable on 1,450 of 1,450 rows; the unpatched dell2 run differs on 11 rows in some column (this seat's round-4 compare, on status and new_account only, counted 3). So the cause is the calendar fallback, and S9 stays ARMED until a covering calendar is where the apply runs. S11 lists the two artifacts: the committed census day figures and the scratch links run; neither is served, landed or graded REALIZED (this seat's CB4d1-AC3 grade was NOT MET and its CB4d2-AC3 grade read the laptop deliverable against raw transactions, not the calendar).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows ADVI_COTBKF-S10, ADVI_COTBKF-S11",
    "deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_5_DRAIN_END_20261007.md @453e5e0b3a",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_4_L9_GRADE_20261007.md @2114a2a7a2"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A cause measurement and an inventory, each carried on the ARMED rows they serve."
 }
]
```
