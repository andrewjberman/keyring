# IRPT_DASHBD: CVO adjudication, round 129 (workstream B-49F, ~D2)

<sweep_watermark>2026-10-15T15:19Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T15:19Z, on msg 8372 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND129_B49F_DRAIN_END_20261015.md` @7503662c7c, blob 14cf0816c7). Graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (CTO msg 8009). One order (DB-b-261, WORLD by its infra path), the issuer's second repair of round 123's DB-b-252. No judgment criterion. Re-run here on the landed tree: 3 of 3 PASS (rc 0). The struck DB118-3-AC3 still FAILS (rc 1), unmet. Proof VALID; `round-close-check --round 129 --workstream B-49F` MAY-CLOSE (1 order). Round 128 EXISTS: it was issued @35ed4b0431 as the one apply order DB-b-260 to 0.7.0_AE_CloudOps~DB2. That order is still `pending` (stopped at the naming-plan gate, rc 7), so it is not terminal and no round-128 packet is owed yet. The landing pair's revision 3 is READ, NOT signed. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S29",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T15:19:00Z",
  "one_line": "Round 129 B-49F (~D2): the Cottonwood scheduler policy gets its own builder name (DB-b-261). 3 of 3 PASS re-run, including the real naming gate in plan mode: 6 named resources CONFORMANT, 0 REFUSE. NAMES ARE BUILDER OUTPUT: lib/opal_naming.py name(system=irpt, scope=cottonwood, function=account-return-daily, kind=...) returns, as recomputed here, irpt-cot-account-return-daily-lambda, -execution-role, -execution-policy, -scheduler-role, -scheduler-policy and -daily. iam.tf takes each from an opal_name module (kind and qualifier at iam.tf:20-21, 29-30, 120-121, 131-132), none hand-typed. 'NOTHING WRITTEN' IS NOT QUITE TRUE. At 15:16:40Z the function, both roles and the schedule are absent (ResourceNotFoundException / NoSuchEntity), and the Cottonwood gold prefix holds 0 objects after date=2026-06-22. The reporting-gold Lambda is unchanged since v91 (LastModified 2026-10-15T11:49:38Z, 8192 MB). But the ARTIFACT investor-reporting/irpt-cot-account-return-daily-lambda.zip in opal-313476888478-lambda-artifacts EXISTS: LastModified 2026-10-15T13:23:43Z, 148,909 bytes, one version, metadata content-sha256 fQFe4moIeMHspIjLxO2C04TobQW6cNZc7mfwstcMWzs=, which equals the pinned build-only sha. Round 128's Act 1 uploaded it before the apply was refused. It is inert (no function references it) and inside the pair's rollback ('the key's first object; listed-key delete or leave'). But the packet, D2-S87 ('refused before any write') and revision 3's condition 2 ('artifact absent', else STOP) all say it is absent. REVISION 3 (sha256 31f8e1620b90bdf0, recomputed equal) changes the scheduler-policy name, the pins and adds a naming-gate condition. Against the five open items it CLOSES NONE IN THE TEXT. Section 10 still lists the served reader of the new partitions, a terraform plan, python3.12 memory and the layer's pyarrow version; section 5 still prints the operator writer unread. In the world, a plan HAS now run once (the applier's 7/0/0 in round 128), which revision 3 does not record. NEW for a signer: condition 2 now cannot be met as written, because the artifact is present, so the next apply would STOP at its own live-state re-read unless the condition is amended. That needs a carrier with an owner (~D2); none exists. Rows: D2-S85 (disarm of D2-S84 on the layer and the revision-2 signatures) is GROUNDED for its subject: the layer stands and DB127-1 passes. Revision 2 is now VOID, so the signatures it cites no longer bind. D2-S87 (INERT; the naming refusal, fixed here) is accepted, with its 'before any write' corrected above. D2-W213-S1 (INERT; the commit-time gate built-not-graded a non-literal scope; plan mode graded it) is accepted. D2-S86 (~C2: the reporting-gold build is wired for 49 Financial only) is noted for B-CW.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-S85",
   "IRPT_DASHBD-D2-S87",
   "IRPT_DASHBD-D2-W213-S1"
  ],
  "spec_asserts": "CLAUDE.md rule 30: every resource name is builder output; never-widen: a sign-off's live-state conditions must match the world they gate; spine L9/L10: every BLOCKING or ARMED row dispositioned or held with an owner.",
  "world_is": "One order complete (merge 039c4807c5). Round 128's apply wrote one inert object (the artifact zip) and nothing else; function, roles, schedule and Cottonwood gold partitions after 2026-06-22 are absent. Revision 3's CTO half is asked. Its condition 2 conflicts with the live artifact. Hop 1 is live since 11:49:38Z with its ledger open until the first fire. FWD-11 and FWD-21 are not met.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T15:1xZ: DB129-1-AC1..AC3 PASS rc 0; DB118-3-AC3 FAIL rc 1; proof-of-spec-check VALID rc 0 on ~213; round-close-check --round 129 --workstream B-49F verdict=MAY-CLOSE",
    "python lib/opal_naming.py name(...) for kinds lambda, role/policy x execution/scheduler, daily; infra/aws/terraform/investor-reporting/account-return-daily/iam.tf:15-32, 115-132",
    "aws at 15:16:40Z: lambda get-function irpt-cot-account-return-daily-lambda ResourceNotFoundException; iam get-role execution and scheduler roles NoSuchEntity; scheduler get-schedule irpt-cot-account-return-daily-daily ResourceNotFoundException; s3api list-objects-v2 opal-data-cottonwood after date=2026-06-22: 0; reporting-gold LastModified 2026-10-15T11:49:38Z",
    "aws s3api head-object opal-313476888478-lambda-artifacts investor-reporting/irpt-cot-account-return-daily-lambda.zip: LastModified 2026-10-15T13:23:43Z, 148909 bytes, content-sha256 fQFe4moIeMHspIjLxO2C04TobQW6cNZc7mfwstcMWzs=, 1 version",
    "git diff fed117446e HEAD on the landing packet (revision 3, sha256 31f8e1620b90bdf0): sections 5 and 10 unchanged; condition 2 still 'artifact absent'",
    "TO-DB-b-260 <round>128 <status>pending, issued @35ed4b0431; investigation rows D2-S85, D2-S86, D2-S87, D2-W213-S1",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND129_B49F_DRAIN_END_20261015.md blob 14cf0816c7 (msg 8372)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Three inert rows whose subjects are fixed or ruled, re-checked here. The artifact-present fact and revision 3's unmeetable condition 2 are named for the CTO and the issuer, not repaired here."
 }
]
```
