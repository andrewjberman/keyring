# ADVI_COTBKF: CVO adjudication, round 18

<sweep_watermark>2026-10-08T07:53Z</sweep_watermark>

Round 18 L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-08 ~08:1xZ. L8 input: `deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_18_DRAIN_END_20261008.md @99a88375ab` (msg 1224). 3 of 3 orders complete and
VALID: CB-r-1 @40d40e22e4, CB-r-2 @e4ab655cf9 (SERVED, applied under the pair, ledger closed), CB-r-3 @afc9554189; 0 judgment criteria. This
seat read the served index back against its pin. 2 rows: D2-W39-S2 dismissed below, D2-W39-S1 (the sweep-pair double count) graduated
OPEN in `remediations/REMEDIATION_v11.md`. Clocks: D2-S26 (REMEDIATION_v9) and D2-W35-S2 (REMEDIATION_v10) REMEDIATED and closed. ARMED: 0.
Still OPEN from earlier rounds: W12-S4, S7, W19-S1, D2-W26-S1.

```json
[
 {
  "id": "ADVI_COTBKF-C-S22",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-08T08:15Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "D2-W39-S2 (round 17's flow-month population came from the both-conventions comparison, not the committed grade) is dismissed; D2-S26 and D2-W35-S2 are closed in place.",
  "adjudicates": [
   "ADVI_COTBKF-D2-W39-S2"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "D2-W39-S2: the 937 / 242 of round 17 counted only months graded under both flow conventions; over the committed grade, external-flow months are 1,173 (316 MATCH). The class ranking does not depend on the gap. Clocks: D2-S26 (REMEDIATION_v9) REMEDIATED and closed -- the served index now carries page counts, read back by this seat against the pin. D2-W35-S2 (REMEDIATION_v10) REMEDIATED and closed -- the CTO's ruling is applied: 29,603 days read NON_POSITIVE_BASE (2,578 zero, 27,025 negative), the before arm reproduces round 17 exactly, and MATCH falls 1,973 -> 1,685 because those months now read UNGRADABLE instead of grading on a meaningless ratio.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation row ADVI_COTBKF-D2-W39-S2",
    "deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_18_DRAIN_END_20261008.md @99a88375ab",
    "org/critical_paths/change_management/20261008T0659Z_advi-cotbkf-r18-index-page-counts-20261008_deploy_completion.md",
    "s3://opal-data-assets/commonwealth/cottonwood/silver/document_index/date=2026-06-23/document_index.parquet: head VersionId 0aPGtfdm5pzHbMNqHP3KUHsFHGKYNS4t (1,430,564 B, 2026-10-08T07:12:08Z); 11,119 rows; page_count non-null and positive 11,087, null 32; every other column equal to the pin xS7loply3Eug2dT30ffGOyFgfQt7K8OM (this compile's read, dell2, 2026-10-08 ~08:1xZ)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A counting note that does not move the finding, and two remedies proven (one on the served table)."
 }
]
```
