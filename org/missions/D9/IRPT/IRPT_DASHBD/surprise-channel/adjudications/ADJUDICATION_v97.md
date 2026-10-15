# IRPT_DASHBD: CVO adjudication, round 131 (workstream B-49F, ~D2): the Cottonwood report-build handler

<sweep_watermark>2026-10-15T17:40Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T17:40Z, on msg 8480 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND130_132_131_B49F_DRAIN_END_20261015.md` @27847c126a, blob 1e264c2eb8; rounds 130 and 132 are ADJUDICATION_v96 and v98). Graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md`. One order, TO-DB-b-263 (WORLD by its infra path; worker ~214; merged @3cc2e295c0). No judgment criterion. Re-run here on the landed tree: DB131-1-AC1..AC3, 3 of 3 PASS (rc 0). Proof VALID; `round-close-check --round 131 --workstream B-49F` MAY-CLOSE. The struck DB118-3-AC3 still FAILS (rc 1), unmet. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S34",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T17:40:00Z",
  "one_line": "Round 131 B-49F: the Cottonwood report-build handler (cell 1 of 4). 3 of 3 PASS re-run. Static: import-time third-party only pyarrow, boto3 and botocore; one put_object; one Event self-invoke; FLOOR_DAY 2026-07-10; no other firm. Probe on a fake S3: the floor, no overwrite, dry-run, refusals before any call, the oldest owed day, one chain. 21 tests. MERGED CODE ONLY, NOTHING DEPLOYED: the merge adds only infra/aws/lambda/investor-reporting/reporting-gold-cot/handler.py and its test under infra/, data/ and lib/. No Terraform root for it exists under infra/aws/terraform/investor-reporting/, and the source map has no entry for the builder name irpt-cot-reporting-gold-lambda (lib/opal_naming.py name()). The live function irpt-cot-reporting-gold-lambda does not exist (ResourceNotFoundException at 17:3xZ). The worker's deviation (D2-W214-S1: the FIRM literal was refused by the commit-time naming gate and now reads opal_naming.lookup) is accepted; it is the rule 30 direction. D2-S90 (~D2's ruling on D2-W216-S1, round 133's neutral token) is noted, not graded here. This handler is the consumer the CTO's ADDENDUM 1 erratum names for the 14.0.2 files; its Lambda-side load is not yet proven, since it has never run in AWS.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W214-S1"
  ],
  "spec_asserts": "CLAUDE.md rule 30: names and addresses are builder output; a build cell writes repo files only; a producer's self-report is verified against live state.",
  "world_is": "The report-build handler exists as tested repo code. No function, root, source-map entry or schedule exists for it in AWS or in the repo. Cells 2 to 4 (root, pair, apply) follow. FWD-1's Cottonwood thread is not met.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T17:2xZ: DB131-1-AC1..AC3 PASS rc 0; DB118-3-AC3 FAIL rc 1; proof-of-spec-check VALID rc 0 on ~214; round-close-check --round 131 verdict=MAY-CLOSE",
    "git log 3cc2e295c0^1..3cc2e295c0 --name-only under infra/ data/ lib/: reporting-gold-cot/handler.py and tests/test_reporting_gold_cot.py only",
    "aws lambda get-function irpt-cot-reporting-gold-lambda: ResourceNotFoundException; infra/aws/lambda/ci/lambda-source-map.json: no entry for that name",
    "investigation rows D2-W214-S1, D2-S90",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND130_132_131_B49F_DRAIN_END_20261015.md blob 1e264c2eb8 (msg 8480)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "One inert worker row, accepted. The code is merged, tested and verified undeployed."
 }
]
```
