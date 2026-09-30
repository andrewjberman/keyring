# TO MDPF_SECCLASS.TO-SC-e12 -- round 5 SC-e-12 (W6-S2, AE lane, PARKED): narrow shared-infra's bd_securities_access after a printed consumer census of partners-lambda-role

<to_id>MDPF_SECCLASS.TO-SC-e12</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.7.0_AE_CloudOps</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-30</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>lane</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>~M</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `SC-e-12` (`decompositions/MDPF_SECCLASS_DECOMP_R5.md`) |
**outcome_ref:** FWD-5 | **depends_on:** none

**PARKED at issuance.** `0.7.0_AE_CloudOps` is dark (not relaunched by the 2026-09-30 13:0xZ word). The order un-parks
when that seat registers LIVE on the broker; the issuer then delivers this file's path in one message. Nothing waits on
it: the E18_IAM half (@a7a6d286f2) is true of `bd-pipeline/iam.tf` alone and says so.

---

## WORKER FACE

### THE CELL

`SC-e-12`. Row `MDPF_SECCLASS-W6-S2` (channel `surprise-channel/investigations/INVESTIGATION_v1.md`): the live,
unconditional grant of `dynamodb:Scan, GetItem, PutItem, UpdateItem, BatchWriteItem` on BOTH `bd-securities` and
`etf-classifications` for `bd-exporter-ec2-role` is `infra/aws/terraform/shared-infra/main.tf`
`aws_iam_policy.bd_securities_access` (`:395-412` at CLOUD 1554e7c8c8), attached by
`aws_iam_role_policy_attachment.ec2_bd_securities` (that role) and `aws_iam_role_policy_attachment.lambda_bd_securities`
(`partners-lambda-role`, a second consumer). Until it is narrowed, FWD-5's IAM read cannot report zero writers of
`bd-securities`, and the FWD-7 scheduled classifier's conditional put on absence is a code guarantee only (CTO half,
@a7a6d286f2). The CTO's ruling (`ROUND2_3_ANALYSIS_MDPF_SECCLASS_20260930.md` @0a8deabc8e section 2): a separate
AE-lane order whose packet FIRST prints every consumer of `partners-lambda-role` (N consumers = N rules read, N printed)
and covers both branches.

**Build (DESIRED Terraform + a measured census; NO apply in this order -- the apply is its own act under its own halves):**
1. **Consumer census, before any edit.** Write
   `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R5_W6S2_CONSUMER_CENSUS.json`: every Lambda whose
   execution role is `partners-lambda-role` (`aws lambda list-functions`, auto-paginated, client-side count; the
   denominator = functions scanned), and for each, every DynamoDB action it performs on `bd-securities` or
   `etf-classifications`, read from its source in the repo (`comp-iam service <fn>` as the floor, then the boto3 call
   sites by reading the source; comp-iam models action, never resource). Print `W6S2-CENSUS functions_scanned=<n>
   partners_role_consumers=<n> bd_securities_writers=<n> etf_classifications_writers=<n>` and list them by name.
   Do the same for `bd-exporter-ec2-role`'s EC2 callers (the scripts under `data/black_diamond/scripts/` that touch
   either table): `E_18.detect_new_securities.py` (now a conditional `etf-classifications` put through the scheduled
   module and no `bd-securities` put), `B_01b.classify_new_securities.py`, `classification/seed_bd_securities.py`,
   `classification/classify_bd_securities.py`, and any other the census finds.
2. **The narrowing (desired bytes).** Edit `infra/aws/terraform/shared-infra/main.tf` so that
   `aws_iam_policy.bd_securities_access` grants READ (`Scan`, `GetItem`, `Query`) on both tables and NO write on
   `etf-classifications` (the E_18 write rides the inline `mdpf-secclass-scheduled-put-policy` on `bd-exporter-ec2-role`,
   applied 2026-09-30 13:56Z). Whether any `bd-securities` WRITE survives is decided by step 1: a consumer that still
   writes `bd-securities` keeps that one action, named per consumer in the evidence JSON; a consumer with no writer
   loses it. `terraform fmt` and `terraform validate`; a `terraform plan` on the shared-infra root is READ ONLY here
   and its resource lines go into the evidence JSON (expect 1 to change, 0 to add, 0 to destroy).
3. **Both branches.** In the evidence JSON, for each consumer: what it does today that the new policy still allows,
   and what it does today that the new policy would DENY, with the call site. A DENY branch that is not a retirement
   the PRD names (FWD-5: the per-firm classifiers retire) is a stop: write it as a surprise row and do not narrow past
   it.
4. **The half.** Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_W6S2_GRANT_20260930.md`
   (`## The act`, `## Blast radius`, `Rollback per key`): the plan lines, the census counts, both branches per
   consumer, and the rollback (re-apply the prior bytes of the policy, one resource).

### ACCEPTANCE

<criterion id="SC5-e12-AC1" cell_refs="SC-e-12"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R5_CHECKS/r5_w6s2_census.py</invocation><expect>W6S2-CENSUS</expect></criterion>
`SC5-e12-AC1` -- the consumer census prints its denominator and the per-role writer counts, and the evidence JSON names every consumer.

<criterion id="SC5-e12-AC2" cell_refs="SC-e-12"><invocation>terraform -chdir=infra/aws/terraform/shared-infra validate -no-color</invocation><expect>Success</expect></criterion>
`SC5-e12-AC2` -- the narrowed policy validates.

<criterion id="SC5-e12-AC3" cell_refs="SC-e-12"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_W6S2_GRANT_20260930.md</invocation><expect>HALF-READY</expect></criterion>
`SC5-e12-AC3` -- the half is ready for the issuer and the CTO to sign.

<expected_criteria>SC5-e12-AC1,SC5-e12-AC2,SC5-e12-AC3</expected_criteria>

Dry-run at the base 2026-09-30 14:2xZ: AC1 no such check (FAIL as expected); AC2 validates today on the UNNARROWED
bytes (the criterion binds the file after step 2); AC3 no such half (FAIL as expected).

## BOUNDS

- **Grant.** The `<paths>` block below plus this order's file. Build scaffolding goes under `.scratch/`, uncommitted.
- **DESIRED only.** No `terraform apply`, no IAM change on the live account, no table write. `terraform plan` is a
  read. The apply is a separate act under COO and CTO halves and a change_management ledger entry.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-AE-S<k>`), and do not weaken the test to pass.

<paths>
infra/aws/terraform/shared-infra/main.tf
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R5_W6S2_CONSUMER_CENSUS.json
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R5_CHECKS/r5_w6s2_census.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_W6S2_GRANT_20260930.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R5.md</decomp_doc> (round 5), cell `SC-e-12`.
<owned_cells>SC-e-12</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC5-e12-AC1, SC5-e12-AC2, SC5-e12-AC3. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.7.0_AE_CloudOps/MDPF_SECCLASS.TO-SC-e12.shared-infra-bd-securities-grant-narrowing.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC5-e12-AC1,SC5-e12-AC2,SC5-e12-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the census line and the per-consumer list, the policy diff, the plan lines, both branches per consumer, the
half's path, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule change.
comp-iam: RUN -- 1 file read (shared-infra/main.tf :395-412, the unconditional grant on both tables; two attachments); BLIND: the live consumer set of partners-lambda-role is unmeasured at the cut (step 1 measures it, and comp-iam models action not resource).
comp-adversary: RUN -- 1 row read (W6-S2, ARMED), 1 ruling read (ROUND2_3_ANALYSIS section 2), 1 half read (E18_IAM CTO half: "does NOT sign bd-securities PutItem removed"); BLIND: whether any partners-lambda-role function writes bd-securities today is unmeasured.
lane: the <paths> block IS the grant.
</preflight>

Source: 1.0.0_SA_CTO rounds 2-3 analysis @0a8deabc8e (section 2, row W6-S2; section 4 item 3).
