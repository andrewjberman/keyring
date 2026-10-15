# IRPT_DASHBD: CVO adjudication, round 120 (workstream B-49F, ~D2)

<sweep_watermark>2026-10-15T08:22Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T08:22Z, on msg 8200 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND120_B49F_DRAIN_END_20261015.md` @8930530130, blob 3d39e88b98). Not B-IN's round 120, which is ADJUDICATION_v83. Graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (CTO msg 8009). Five orders (DB-b-237..241); DB-b-237 is WORLD by its infra paths, the rest LOCAL. No judgment criterion. Re-run here on the landed tree: 8 of 8 round-120 criteria PASS (rc 0). The packet says "ten mechanical criteria"; the five orders declare eight (DB120-1-AC1..AC3, DB120-2-AC1, DB120-3-AC1, DB120-4-AC1, AC2, DB120-5-AC1). The struck DB118-3-AC3 still FAILS (rc 1, no Cottonwood QA record). All five proof instances VALID; `round-close-check --round 120 --workstream B-49F` MAY-CLOSE (5 orders). 9 rows graded below; 2 ARMED among them. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S22",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T08:22:00Z",
  "one_line": "Round 120 B-49F (~D2): the hop-1 filled_report_values stage in the reporting-gold handler (DB-b-237), the 04-20..22 balance-lag read (DB-b-238), Black Diamond bronze and the exact key map (DB-b-239), account-return contract 0.3.0 with an optional source column (DB-b-240), the Cottonwood adapter landing facts (DB-b-241). 8 of 8 PASS re-run here. Struck DB118-3-AC3: still FAILS, unmet. NO IAM OR AWS CHANGE: no .tf or .tfvars file is touched by any commit since the issuance bf61bc8845. The infra paths changed this round are handler.py, its stage test and lambda-source-map.json (+21/-0 since issuance, so the removed etf_classifications line is restored). The live irpt-49f-reporting-gold-lambda reads LastModified 2026-10-13T12:39Z (before this round) and Timeout 900. All five worker records read deployed false and served_values_changed false; three READ records read s3_writes 0. The live role's inline policy text was not read, since IAM gives no timestamp; it is unchanged in Terraform. The CTO ask (three IAM grants in Terraform, applied with the code hash under one never-widen pair) is for a future order; nothing here pre-empts it. Rows: D2-W195-S1 (ARMED, owner ~C2) DISARMED by D2-S71, GROUNDED: the live schedule irpt-cot-holdings-performance-daily (builder name) reads State ENABLED, cron(15 8 ? * MON-FRI *), matching schedule.tf:287; only the description text (schedule.tf:285 and the output at :309) still says DISABLED. D2-W193-S1 (ARMED, owner ~D2; the box's client account-id gate did not run) has NO disarm row. The packet lists it among 'INERT or observations', which mislabels it. On substance it is D2-W182-S1's condition (held by 0.0.0_AB_MSTR), with the issuer's and the worker's scans standing in, as in v76 and v84; dismissed on that ground, and the missing disarm row is named. D2-W191-S2 (BLOCKING, INERT; the role lacks the three grants) holds for the landing, carried to the CTO as the ask. D2-W191-S1, W192-S1, S2, W194-S1, W195-S2: INERT observations carried to the next records. The 04-21 reading is corrected by the issuer: a cohort-wide quantity change (929 of 929 changed quantity, balance positions agree with position value for 927), not a lagging value.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W191-S1",
   "IRPT_DASHBD-D2-W191-S2",
   "IRPT_DASHBD-D2-W192-S1",
   "IRPT_DASHBD-D2-W192-S2",
   "IRPT_DASHBD-D2-W193-S1",
   "IRPT_DASHBD-D2-W194-S1",
   "IRPT_DASHBD-D2-W195-S1",
   "IRPT_DASHBD-D2-W195-S2",
   "IRPT_DASHBD-D2-S71"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every BLOCKING or ARMED row is dispositioned on grounded evidence or a recorded ruling before the slug; a disarm is graded on its evidence; no IAM or AWS change outside safe-apply and a signed pair.",
  "world_is": "Five orders complete (merges fbd8e9f815, 8b33c57786, 439030d0d1, 3dfcc56c4f, 3e1230abec); nothing planned, applied, deployed or written. Hop 1's stage is built and tested on synthetic data only, and cannot land until the role gains three grants. The Cottonwood key map covers 564 of 1,533 history accounts; 2026-07-09 is a silver-build gap for its owner. The Cottonwood adapter needs six changes before a landing. FWD-2, FWD-11 and FWD-21 are not met.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T08:1xZ: DB120-1-AC1..AC3, DB120-2-AC1, DB120-3-AC1, DB120-4-AC1, AC2, DB120-5-AC1 PASS rc 0; DB118-3-AC3 FAIL rc 1",
    "proof-of-spec-check VALID rc 0 on ~191..~195; round-close-check --round 120 --workstream B-49F verdict=MAY-CLOSE orders=5",
    "git log bf61bc8845..HEAD -- '*.tf' '*.tfvars': no commits; git diff bf61bc8845 HEAD -- infra/aws/lambda/ci/lambda-source-map.json: +21, 0 removed",
    "aws lambda get-function-configuration irpt-49f-reporting-gold-lambda: LastModified 2026-10-13T12:39:43Z, Timeout 900",
    "aws scheduler get-schedule irpt-cot-holdings-performance-daily: State ENABLED, cron(15 8 ? * MON-FRI *); infra/aws/terraform/investor-reporting/holdings-performance/schedule.tf:285, :287, :309",
    "worker records RD_HOP1_STAGE_FACTS_R120, RD_BALANCE_LAG_R120, RD_BD_BRONZE_AND_MAP_R120, RD_SOURCE_COLUMN_R120, RD_CW_LANDING_FACTS_R120",
    "investigation rows D2-W191-S1..S2, D2-W192-S1..S2, D2-W193-S1, D2-W194-S1, D2-W195-S1..S2, D2-S71, D2-W182-S1",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND120_B49F_DRAIN_END_20261015.md blob 3d39e88b98 (msg 8200)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "One ARMED row disarmed by its owner on evidence this seat read live. One ARMED box-gate row whose infrastructure owner already holds the condition; its missing disarm row is named. The BLOCKING IAM row is carried to the CTO as the round's ask, and the rest are inert observations."
 }
]
```
