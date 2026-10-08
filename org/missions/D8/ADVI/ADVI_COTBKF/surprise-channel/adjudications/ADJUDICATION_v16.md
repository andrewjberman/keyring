# ADVI_COTBKF: CVO adjudication, round 20

<sweep_watermark>2026-10-08T18:3xZ</sweep_watermark>

Round 20 L8 compile and L9 grade by `3.0.0_SA_CVO` (seated on dell2), 2026-10-08 ~18:4xZ. L8 input:
`deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_20_DRAIN_END_20261008.md` (msg 1407). 2 of 2 orders complete and VALID: CB-t-1, CB-t-2
(chain drained @16f0103204). L9: CB20t2-AC3 MET (`org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_20_L9_GRADE_20261008.md`).
3 rows: 2 dismissed below, D2-W41-S1 (no citable designation) graduated OPEN in `remediations/REMEDIATION_v13.md`. D2-S29 and D2-S30
stay OPEN unchanged: classed 16 core / 0 other MMF / 147 neither, and the (b) entry did not land. ARMED: 0.

```json
[
 {
  "id": "ADVI_COTBKF-C-S23",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-08T18:35:25Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "D2-W41-S2 (the CB-t-1 test pinned the v1 arm to the current list version) is fixed at @900b146dd9 and recorded by D2-W41-S3; both dismissed. L9: CB20t2-AC3 MET (316067107 off with its absent designation stated; no MMF added by census).",
  "adjudicates": [
   "ADVI_COTBKF-D2-W41-S2",
   "ADVI_COTBKF-D2-W41-S3"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug; CB20t2-AC3 is graded by the CVO.",
  "world_is": "The mover-classes test now asserts against SWEEP_LIST_V1_VERSION (amendment c6e1cae6d3 granted the one path); the issuer's real run reads 514 passed, 11 skipped. CB20t2-AC3 MET: sweeps-v2 = the two rule (a) members; the (b) candidate 316067107 is OFF with designation_source None and the places searched; this seat's scan of the cached holdings/positions/accounts extracts finds no core or sweep value.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows ADVI_COTBKF-D2-W41-S2, ADVI_COTBKF-D2-W41-S3",
    "deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_20_DRAIN_END_20261008.md",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_20_L9_GRADE_20261008.md"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A test-pin defect fixed inside the round and its record row."
 }
]
```
