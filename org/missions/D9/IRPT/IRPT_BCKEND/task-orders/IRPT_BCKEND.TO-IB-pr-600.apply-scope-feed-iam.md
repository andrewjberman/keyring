# TO IRPT_BCKEND.TO-IB-pr-600 -- APPLY the Scope account feed's IAM pair: ONE new resource `aws_iam_role_policy.inf_gold_layer_scope_feed` on the inf gold runner role (Put/Get on the two scope_account_returns prefixes of opal-data-assets, prefix-conditioned ListBucket; packet blob cea5395ee7; COO half @afc428c27c, CTO half @d0bf7c5ea7)

<to_id>IRPT_BCKEND.TO-IB-pr-600</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
<workstream>~PO</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the signed IAM pair `deliverables/2.0.0_SA_COO~P2/NEVER_WIDEN_SIGNOFF_PACKET_SCOPE_FEED_IAM_PAIR.md` (blob `cea5395ee74000806a28ab8eca32156e0af94639`; READ IT ALL: the HCL, the rollback and the after-reads are its sections), COO half `deliverables/2.0.0_SA_COO~P2/NEVER_WIDEN_SCOPE_FEED_IAM_PAIR_COO_HALF.md`, CTO half `deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_SCOPE_FEED_IAM_PAIR_CTO_HALF.md` (conditions 1 to 5), on your STOP at gate (f) of IB-pr-596 (msg 8548) and the CTO's ruling (msg 8553) | **Decomp cell:** `IB-pr-600` (decomposition section 226) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Cell `IB-pr-600` (inlined).** Your STOP on IB-pr-596 found that `inf-gold-layer-ec2-role` cannot put the Scope feed's keys: `address()` puts them in `opal-data-assets/orion/inflection/`, and the role's `s3-scoped-inf` reaches `opal-data-inf` only. The CTO ruled the address right (doctrine R4) and the grant the remedy. **This order applies that grant, ONE resource, and proves it both ways. It writes no S3 object and does not start IB-pr-596.** Paths you post are `file:///` absolute URIs or markdown links to them, with the repo-relative form for another box (CLAUDE.md rule 33). No bucket key, account or household identifier goes in any record beyond what the criteria name.

**Do, in this order. A STOP is reported to the issuer and writes nothing further.**

1. **Gates (READ ONLY).** (a) Both halves read SIGNED or GIVEN at blob `cea5395ee74000806a28ab8eca32156e0af94639` and `git hash-object` of the packet equals it. (b) **One change at a time:** if any ledger under `org/critical_paths/change_management/` names the `inf-pipeline` Terraform root or the role `inf-gold-layer-ec2-role` and reads OPEN, or another seat's window is open on it, STOP. (c) Print `lib/opal_naming.address()` for the bronze and silver layers of source `orion`, scope `inflection`, table `scope_account_returns` (a dummy `date=` and object name); the two ARN prefixes in the packet's HCL must equal that output character for character; a difference is a STOP and a row (the packet is then wrong: report, do not edit). (d) The live role's attached inline policies: print the names (no new one of the same name may exist).
2. **Open the NEVER-2 ledger entry** (`python .tools/deploy_ledger.py open ...`) under `org/critical_paths/change_management/` BEFORE the first write, naming the one resource, the root `infra/aws/terraform/inf-pipeline`, this order and the rollback (the one-resource destroy); commit its `.open_deploys` sentinel at once.
3. **Add the resource.** In your own worktree add the packet's HCL VERBATIM as `aws_iam_role_policy.inf_gold_layer_scope_feed` to `infra/aws/terraform/inf-pipeline/iam.tf` (beside `inf_gold_layer_s3`); nothing else in that file or root changes. Commit with `.tools/safe-commit.sh` on your own lane.
4. **Plan, apply through `safe-apply`.** The plan must read `1 to add, 0 to change, 0 to destroy` at that address ONLY; any other diff is a STOP (do not apply). Apply through `safe-apply`, never bare `terraform apply`. Re-plan: no changes. Read the policy back from the role (`get-role-policy`): two statements, no `s3:DeleteObject`, no `kms:` action; record its sha256.
5. **After-reads 1 to 4 of the packet (CTO half condition 2), by `aws iam simulate-principal-policy` on the role:** ALLOWED: PutObject on one bronze feed key and on one silver feed key, GetObject on one feed key, ListBucket with prefix `orion/inflection/silver/scope_account_returns/`. DENIED (implicitDeny or explicitDeny): PutObject on the sibling key `orion/inflection/silver/fact_positions/x`; DeleteObject on a feed key; PutObject on an unrelated bucket; ListBucket with prefix `orion/inflection/silver/fact_positions/`. Controls: allowed on `opal-data-inf/orion/inflection/x`, denied on an unrelated bucket. **A simulation that ALLOWS any denied arm is Branch B the same turn.** Use keys built from `address()` output with a dummy date; never type one.
6. **The read-ABSENT-first proof on the RUNNER (CTO half condition 3).** With `s3:ListBucket` granted only under an `s3:prefix` condition, a HEAD on a MISSING key may answer 403, not 404. On the runner instance (through SSM, read only), run the feed's own `S3Ops.exists` (take the class from `data/inf/manual_api/pull_inflection_scope_account_returns.py` at HEAD, lines 339 to 362, unchanged) with the instance role against ONE known-absent feed key (a `date=1900-01-01` silver key built from `address()`; confirm it is absent first by a listing with its exact prefix). Record the answer: `ABSENT` (the call returned False) or the error code. **It must read ABSENT.** Any other answer is a STOP and a row; the fix is the feed's code (a prefix-scoped ListObjectsV2), never a wider grant, and the issuer cuts that build cell before IB-pr-596 resumes. Write NOTHING to S3 in this step.
7. **On any trigger of Branch B** (a plan that differs, a simulation that allows a denied arm, a failed apply after a partial write): apply the one-resource destroy through `safe-apply` (`0 to add, 0 to change, 1 to destroy`, that address only), read back that the role no longer carries the policy, set `rollback_performed` true and report at once. An exists() answer other than ABSENT is NOT a rollback trigger: the grant stays (it is inert until IB-pr-596 runs) and you report the STOP.
8. **Close the ledger entry** only after step 6 is written; then write the record `deliverables/0.7.0_AE_CloudOps~IB2/IB232-1_apply_record.json`:
`{"gates":{"packet_blob":"cea5395ee74000806a28ab8eca32156e0af94639","both_halves_signed":true,"plan":{"add":1,"change":0,"destroy":0,"addresses":["aws_iam_role_policy.inf_gold_layer_scope_feed"]},"arns":{"prefixes_printed":true,"equal_address_output":true},"one_change_at_a_time":true,"ledger_opened_before_apply":true},"ledger_entry":"org/critical_paths/change_management/<file>","apply":{"through":"safe-apply","added":1,"changed":0,"destroyed":0,"replan_no_changes":true,"policy_readback":{"statement_count":2,"delete_action_present":false,"kms_action_present":false,"policy_sha256":"<64 hex>"},"rollback_performed":false},"simulation":{"allowed":{"put_bronze_feed_key":"allowed","put_silver_feed_key":"allowed","get_feed_key":"allowed","list_with_feed_prefix":"allowed"},"denied":{"put_sibling_fact_positions_key":"implicitDeny","delete_feed_key":"implicitDeny","put_other_bucket":"implicitDeny","list_sibling_prefix":"implicitDeny"},"controls":{"inf_bucket_allowed":true,"unrelated_bucket_denied":true}},"exists_read":{"ran_on_runner":true,"key_was_known_absent":true,"answer":"ABSENT"},"counters":{"function_updates":0,"lambda_invokes":0,"other_iam_changes":0,"schedule_changes":0,"keys_written":0,"existing_keys_changed":0,"secrets_printed":0}}`. The record carries no account, household or client identifier and no ARN.

**Criteria (run each under `timeout 120` from the repository root, record the output and exit code verbatim):**

<criterion id="IB232-1-AC1" cell_refs="IB-pr-600"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r232/p232_cells.py" . IB232-1-AC1</invocation><expect>IB232-1-AC1 PASS</expect></criterion>
<criterion id="IB232-1-AC2" cell_refs="IB-pr-600"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r232/p232_cells.py" . IB232-1-AC2</invocation><expect>IB232-1-AC2 PASS</expect></criterion>
<criterion id="IB232-1-AC3" cell_refs="IB-pr-600"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r232/p232_cells.py" . IB232-1-AC3</invocation><expect>IB232-1-AC3 PASS</expect></criterion>

<expected_criteria>IB232-1-AC1, IB232-1-AC2, IB232-1-AC3</expected_criteria>

What the checks grade: AC1 both halves signed at the packet blob, the plan 1/0/0 at the one address, the ARNs equal to `address()` output, one change at a time, the ledger opened first; AC2 applied through `safe-apply` 1/0/0, a clean re-plan, the policy read back with two statements and no Delete or KMS action, no rollback; AC3 the four allowed and four denied simulation arms with the controls, the `exists()` read on the runner reading ABSENT, the counters. Do not edit the checks. If the order STOPS, the criteria are not run; report the stop and its reason to the issuer.

## BOUNDS

- **Grant:** the one resource in `infra/aws/terraform/inf-pipeline/iam.tf` and its Terraform apply; the ledger entry; your record folder; reads: IAM role policies and simulation, bucket listings by exact prefix, the runner through SSM (read only). **No S3 object written or deleted, no Lambda invoke, no chain trigger, no other IAM, schedule, runner, catalog or Terraform change, no code object, no deletion beyond the one-resource rollback.**
- **Refusal clause:** STOP and report, writing nothing further, on any of: a half not signed at the blob; an open ledger or window on the root or the role; an ARN that differs from `address()` output; a plan that differs from 1/0/0 at the one address; a simulation that allows a denied arm; an `exists()` answer other than ABSENT. A STOP is reported, not worked around; a grant is never widened.
- **Row ids:** put the row text in your report; the issuer appends it as `IRPT_BCKEND-D2-S<k>`. **Report under 150 words.**
- **Your queue:** this order goes before IB-pr-596 (which resumes after it, and after the issuer's amendment); IB-pr-549's after-read (2026-10-16 14:15Z) stands.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/
infra/aws/terraform/inf-pipeline/iam.tf
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-600.apply-scope-feed-iam.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 226 (round 7, workstream ~PO), cell `IB-pr-600`.
<owned_cells>IB-pr-600</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB232-1-AC1, IB232-1-AC2, IB232-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_BCKEND.TO-IB-pr-600.apply-scope-feed-iam.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- one new inline policy on the inf gold runner role; the plan is 1/0/0 and the rollback 0/0/1 (the packet's sections "Root, address and plan shape" and "Rollback"); the grant is inert until IB-pr-596 runs, and reaches only the two feed prefixes of opal-data-assets.
comp-iam: RUN -- the change IS an IAM change under its own signed pair (packet blob cea5395ee7; COO half @afc428c27c; CTO half @d0bf7c5ea7); the simulation arms in step 5 are the measure.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p232_cells.py IB232-1 dry-run at base on dell2 2026-10-15 ~19:0xZ: AC1, AC2, AC3 FAIL (no record). Positive control in temp roots the run created itself (stub halves and packet, a synthetic record; removed): all three PASS; fifteen negatives plus the no-record cases each fail their own arm (wrong blob, two added, another address, ARNs unequal, ledger not first, not safe-apply, dirty re-plan, Delete in the policy, KMS in the policy, a sibling put allowed, a delete allowed, a feed put not allowed, an exists() 403, exists() not on the runner, a key written).
lane: the paths block IS the grant; seat `0.7.0_AE_CloudOps~IB2` (dell2). Class WORLD. Not measured by me: the live role's inline policy names, the `exists()` answer on the runner, the simulation results (each read by the seat and each a STOP).
</preflight>
