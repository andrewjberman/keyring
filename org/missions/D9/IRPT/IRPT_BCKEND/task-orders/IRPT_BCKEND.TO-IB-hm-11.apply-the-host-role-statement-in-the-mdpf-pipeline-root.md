# TO IRPT_BCKEND.TO-IB-hm-11 -- APPLY the `mdpf-pipeline` leg of the signed HMAC list producer pair: ONE inline-policy change on the host role (`aws_iam_role_policy.mdpf_runner`: the statement `IrptHmacListStageAssumeRole` and nothing else), only when no other ledger touches that root; then the QA re-run IF the first QA recorded an AccessDenied on the assume (packet blob e6d82eb31f; CTO half msg 10336 ruling 1)

<to_id>IRPT_BCKEND.TO-IB-hm-11</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>13</round>
<workstream>~PM</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the signed pair: packet `deliverables/2.0.0_SA_COO~P2/NEVER_WIDEN_HMAC_LIST_PRODUCER_PAIR_PACKET_AND_COO_HALF.md` (blob `e6d82eb31f2c84f0d3935846c4d2f3e6ddd7bf0d`; its section 3 "Host-role identity statement" and section 4 Branch A step 1 second plan) with the CTO half `deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_HMAC_LIST_PRODUCER_CTO_HALF.md` (**ruling 1: the `mdpf-pipeline` leg is part of the apply; that root has N = 2 writers, this pair and `4.0.0_SA_CRO~DDD`'s MDPF_CANON FWD-10 (c5dd8b293a, ledger `mdpf-gold-fwd10-cottonwood-supervised-20261017.json`); IB2 plans and applies this leg ONLY when no other ledger touching that root is open, reads every live worktree, prints the denominator, and plans from a HEAD that contains c5dd8b293a; a plan line beyond the one inline-policy change is a STOP; ruling 2: apply the statement whether or not it is strictly required**) and ADDENDUM 1 section 3 (its Branch B) and section 4 (the QA re-run) | **Decomp cell:** `IB-hm-11` (decomposition section 249) | **outcome_ref:** FWD-21 | **The text is already committed:** IB-hm-10 (merged 2d2c906b87) added the name module `irpt_hmac_list_stage_role_name` and the statement to `infra/aws/terraform/mdpf-pipeline/iam.tf` (21 lines added, 0 deleted). **You add NOTHING; this order applies it.** | **Not in this order:** the `directory` root (IB-hm-5); the reader grants (the laptop CTO's lane, XA-0e3e).

---

## WORKER FACE

**Cell `IB-hm-11` (inlined).** Paths you post are `file:///` absolute URIs or markdown links to them, with the repo-relative form for another box (CLAUDE.md rule 33). No secret value, account or household identifier, and no number by firm in any record. A STOP is reported to the issuer and writes nothing further.

**Do, in this order:**
1. **Gates (READ ONLY).** (a) The CTO half reads SIGNED at blob `e6d82eb3`; `git hash-object` of the packet equals its blob. (b) **One change at a time, the CTO's condition:** read EVERY live worktree (`git worktree list --porcelain`, then `git -C <wt> ls-tree -r --name-only HEAD org/critical_paths/.open_deploys/`), union them, print the denominator; if ANY open ledger names the `mdpf-pipeline` Terraform root or the role `mdpf-daily-runner-ec2-role`/`mdpf_runner`, or another seat's window is open on it, **STOP and report which ledger** (this order waits; the issuer re-sends it when the ledger closes). The ledger `mdpf-gold-fwd10-cottonwood-supervised-20261017` reads OPEN at the time of this cut. (c) The tree you plan from contains `c5dd8b293a` AND `2d2c906b87` (`git merge-base --is-ancestor` each against HEAD, positive control beside). (d) The time is outside 13:20Z to 14:00Z on a weekday. (e) Print the live host role's inline policy statement Sids (names only) so the before-state is recorded; the new Sid `IrptHmacListStageAssumeRole` must not exist yet.
2. **Open the NEVER-2 ledger entry** (`python .tools/deploy_ledger.py open ...`) under `org/critical_paths/change_management/` BEFORE the first write, naming the one resource, the root `infra/aws/terraform/mdpf-pipeline`, this order and the rollback (the revert of the two additions and the reverse plan); commit its `.open_deploys` sentinel at once.
3. **Plan, then apply through `safe-apply`.** `terraform validate`, then a plan to a planfile that must read **0 to add, 1 to change, 0 to destroy** at `aws_iam_role_policy.mdpf_runner` ONLY (the `policy` document only; the module adds no resource); any other line, or any drift from another seat's undeployed change, is a STOP and nothing is applied. Apply the planfile through `bash .tools/safe-apply.sh`, never bare `terraform apply`. Re-plan: no changes.
4. **Read the policy back from the host role** (`get-role-policy`): exactly one new statement with Sid `IrptHmacListStageAssumeRole`, Action `sts:AssumeRole`, Resource the stage role's ARN (no wildcard); the 49F statement `IrptDirectory49fAssumeSourcePrincipal` and every other statement byte-equal to the before-state (compare statement by statement).
5. **The assume simulation** (`aws iam simulate-principal-policy` on the host role, resource ARNs built from `lib/opal_naming.py name()` / the account id, never typed): ALLOWED `assume_the_stage_role` (`sts:AssumeRole` on the stage role); DENIED `assume_an_unrelated_role` (a role the host has no statement for), `assume_the_stage_role_with_another_action_than_assume` (e.g. `sts:TagSession`... any other `sts:` action on that ARN that no statement grants), `any_wildcard_resource_assume`. A denied arm that ALLOWS is Branch B the same turn (ADDENDUM 1 section 3(d): revert the two additions and `safe-apply` the reverse plan).
6. **The QA re-run decision (ADDENDUM 1 section 4).** Read the record of IB-hm-5 (`deliverables/0.7.0_AE_CloudOps~IB2/IBhm5_apply_record.json`, field `qa.assume_succeeded_before_mdpf_leg`). If it is **true** (the assume worked before this leg) or the record does not exist yet, **no re-run**: record `qa_rerun_needed` false and `qa_runs_after_the_leg` 0. If it is **false**, run EXACTLY ONE more QA run exactly as IB-hm-5 step 8 (the refresh function's own manual invoke for ONE firm, outside the fire window) and record the four checks PASS or FAIL; this is the only invoke this order may make.
7. **Close the ledger entry** only after step 6 is written; then write the record `deliverables/0.7.0_AE_CloudOps~IB2/IBhm11_apply_record.json`:
`{"gates":{"packet_blob":"e6d82eb31f2c84f0d3935846c4d2f3e6ddd7bf0d","both_halves_signed":true,"worktrees_read":{"count":<n>,"denominator_printed":true},"no_other_ledger_open_on_the_root":true,"head_holds_c5dd8b293a":true,"head_holds_2d2c906b87":true,"ledger_opened_before_apply":true,"outside_the_fire_window":true},"terraform":{"plan":{"add":0,"change":1,"destroy":0,"addresses_changed":["aws_iam_role_policy.mdpf_runner"]},"applied_through":"safe-apply","replan_no_changes":true},"policy_readback":{"new_statement_sid":"IrptHmacListStageAssumeRole","new_statement_count":1,"statement_49f_unchanged":true,"other_statements_unchanged":true,"wildcard_in_new_statement":false},"simulation":{"allowed":{"assume_the_stage_role":"allowed"},"denied":{"assume_an_unrelated_role":"implicitDeny","assume_the_stage_role_with_another_action_than_assume":"implicitDeny","any_wildcard_resource_assume":"implicitDeny"}},"qa":{"qa_rerun_needed":true|false,"qa_runs_after_the_leg":0|1,"list_key_exists_and_fresh":"PASS","line_count_equals_the_session_count":"PASS","no_plain_sha256_of_a_known_fake_id":"PASS","directory_output_byte_unchanged":"PASS"},"counters":{"other_iam_changes":0,"other_terraform_roots_applied":0,"lambda_invokes_beyond_the_one_qa_run":0,"secrets_printed":0,"per_firm_numbers_recorded":0}}` (the four QA check fields only when a re-run was made). The record carries no account, household or client identifier, no ARN and no number by firm.

**Criteria (run each under `timeout 120` from the repository root, record the output and exit code verbatim):**

<criterion id="IBHM11-AC1" cell_refs="IB-hm-11"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r255/p255_cells.py" . IBHM11-AC1</invocation><expect>IBHM11-AC1 PASS</expect></criterion>
<criterion id="IBHM11-AC2" cell_refs="IB-hm-11"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r255/p255_cells.py" . IBHM11-AC2</invocation><expect>IBHM11-AC2 PASS</expect></criterion>
<criterion id="IBHM11-AC3" cell_refs="IB-hm-11"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r255/p255_cells.py" . IBHM11-AC3</invocation><expect>IBHM11-AC3 PASS</expect></criterion>

<expected_criteria>IBHM11-AC1, IBHM11-AC2, IBHM11-AC3</expected_criteria>

What the checks grade: AC1 both halves signed, the root's writers counted from every live worktree with the denominator printed, no other ledger open on the root, the plan taken from a HEAD that holds both commits, the ledger opened first, outside the fire window; AC2 the plan 0/1/0 at the one address, applied through safe-apply, a clean re-plan, the new statement read back with the 49F statement and every other statement unchanged and no wildcard; AC3 the assume simulation (one allowed arm, three denied), the QA re-run decision recorded as a fact (zero or exactly one run, never more), the counters. Do not edit the checks. If the order STOPS, the criteria are not run; report the stop and its reason to the issuer.

## BOUNDS

- **Grant:** the `infra/aws/terraform/mdpf-pipeline` root's apply through `safe-apply` (the planfile of step 3 only); the ledger entry; your record folder; reads: IAM role policy and simulation, the function configuration, worktree ledgers; at most ONE manual invoke of `irpt-directory-refresh` for one firm (step 6, only on the branch it names). **No change to `iam.tf` or any file (the text is committed), no other root, no other IAM, no schedule, no S3 write, no deletion beyond Branch B.**
- **Refusal clause:** STOP and report, writing nothing further, on any of: a half not signed at the blob; an open ledger or window on the root or the role (the report names it); a HEAD missing either commit; a plan that differs from 0/1/0 at the one address; a simulation that allows a denied arm; a changed 49F or other statement at read-back. A STOP is reported, not worked around; a grant is never widened.
- **Row ids:** put the row text in your report; the issuer appends it as `IRPT_BCKEND-D2-S<k>`. **Report under 150 words.**
- **Your queue:** the filled-report switch-on and IB-hm-5 go before this order; this order waits on the other writer's ledger by its own gate (b) and is re-sent by the issuer when that ledger closes.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-hm-11.apply-the-host-role-statement-in-the-mdpf-pipeline-root.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 249 (round 13, workstream ~PM), cell `IB-hm-11`.
<owned_cells>IB-hm-11</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBHM11-AC1, IBHM11-AC2, IBHM11-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_BCKEND.TO-IB-hm-11.apply-the-host-role-statement-in-the-mdpf-pipeline-root.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- one changed resource (the inline policy of the shared host role `mdpf_runner`: one added statement, sts:AssumeRole on the one stage role ARN); the plan is 0/1/0 and the rollback is the revert of the two committed additions with the reverse plan (ADDENDUM 1 section 3(d)); the grant lets the host role assume a role that holds one secret read and three list-key writes and nothing else (the stage role's trust already names the host role); the root has a second writer (MDPF_CANON FWD-10) whose ledger gates this order.
comp-iam: RUN -- the change IS an IAM change under its own signed pair (packet blob e6d82eb31f, CTO half msg 10336 ruling 1 and ruling 2); the simulation arms in step 5 are the measure.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache surface is touched.
comp-adversary: RUN -- p255_cells.py IBHM11 dry-run at base on dell2 2026-10-17 ~08:0xZ: AC1, AC2, AC3 FAIL (no record). Positive control (control255.py) over synthetic roots with stub halves and synthetic records: the clean record and the clean-with-re-run record PASS all three; 31 negatives plus the no-record cases each fail their own arm (a wrong blob, an unsigned half, zero worktrees read, a denominator not printed, another ledger open, HEAD missing either commit, the ledger not first, inside the fire window, a plan with two changes or an add or a destroy or another address, not safe-apply, a dirty re-plan, the new statement missing, the 49F or another statement changed, a wildcard in the new statement, the assume not allowed, an unrelated role or a wildcard assume allowed, the re-run fact missing or inconsistent with the runs, two re-runs, a re-run check failing, another IAM change or root applied, a per-firm number, a long digit run), 0 unexpected. Not measured by me: the plan's own counts, any drift in the root from other seats' undeployed changes, the simulation results (each read by the seat and each a STOP).
lane: the paths block IS the grant; seat `0.7.0_AE_CloudOps~IB2` (dell2). Class WORLD.
</preflight>
