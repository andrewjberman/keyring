# TO ADVI_COTBKF.TO-CB-cj-1.crm-match-grant -- round 88 CB-cj-1: GRANT -- one builder-named role with `s3:GetObject` on the ONE CRM key, and its ARN added to the READ deny's readers; nothing else moves

<!-- ===================== WORKER FACE -- this is the WHOLE of the executing seat's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round88.md</decomp_doc> (round 88), cell `CB-cj-1`.
<owned_cells>CB-cj-1</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~CB1</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no rule, schedule or cadence is added; the grant lives for one job and is removed the same UTC day by `CB-cj-3`.
comp-iam: RUN by the executing seat BEFORE the apply -- DENOMINATOR: 2 policy documents read (the new role's inline policy and the cottonwood firm bucket policy), 3 simulator calls on the new role (the one key, one other key under the prefix, list and put); the expectation is the one key ALLOWED and the other three NOT allowed; BLIND: the lens reads the plan and the simulator, not the live bucket after the apply (the read-back is that), and it cannot see a principal outside this account.
comp-adversary: RUN by the issuer -- the record's checker fails any policy action but `s3:GetObject`, any resource but the one key, any plan change beyond the role, its policy and the bucket policy, any moved LIST or WRITE deny; BLIND: the exception in the bucket policy is prefix-wide (the one-key bound is the role's own allow, ruled and accepted by the CTO half), the trust names the agents' shared shell user so any seat could assume the role during its life (the job's record lists every AssumeRole event: CTO condition C1), and a policy simulator is not the live bucket (the job's `head-object` is the live read).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE ACT -- `CB-cj-1` (round 88, WORLD)

PENDING. You act only after every precondition below is read and recorded. Until then do nothing and say which one is missing.

### 1a. Preconditions (each recorded in the record)

1. **The pair is signed on BOTH halves at current bytes.** Read at HEAD of `box/dell1`: `org/missions/D8/ADVI/ADVI_COTBKF/ledger/NEVER_WIDEN_R88_CRM_MATCH_GRANT_COO_HALF.md` (sha256 `472df1c92c5927d6c714d1ab5bb3f13096d2456b0662f2524f388be17ed3bbc3`) and `NEVER_WIDEN_R88_CRM_MATCH_GRANT_CTO_HALF.md` (it binds that sha256). If the COO half's bytes differ from the sha256, or the CTO half is absent, STOP.
2. **C3: the CVO has signed the PRD again.** `python .tools/prd-signoff.py status ADVI_COTBKF` must read `ADMITTED` with the ratified-text half `SIGNED` by `3.0.0_SA_CVO` at the PRD version that carries Andrew's one-job exception in C-RESTRICTED. A `REFUSED` or `WITHHELD` reading is a STOP. Record the output line.
3. **The clock.** Run `date -u +%H:%MZ`. Apply only when at least THREE HOURS remain before 23:59Z of the UTC day (that is, no later than 20:59Z) and not before 00:05Z: the job and the withdrawal must both fit before 23:59Z of that SAME day (the CTO's C2: the withdrawal is absolute; the CTO's msg 6158: the withdrawal runs as the job's NEXT act, 23:59Z is only the backstop). Outside that window STOP and report the earliest start.
4. **Your own preconditions for terraform:** the real backend and terraform on this box (the earlier break-glass role was applied by `0.7.0_AE_CloudOps~CB2` under `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.7.0_AE_CloudOps~CB2/breakglass_targeted_apply_report.md`: read it for the method). If terraform or the backend is not usable here, STOP and say which.

### 1b. Steps

1. **Ledger** (NEVER-2): open `org/critical_paths/change_management/<UTC>_advi-cotbkf-r88-crm-match-grant_deploy_completion.md` with its `.open_deploys/` sentinel BEFORE the plan; its ROLLBACK line names the removal (`CB-cj-3`: destroy the role and its policy, remove the reader ARN, re-plan reads no changes) and its DEADLINE line names `23:59Z` of today. Name in the entry every principal that can reach the key after the apply (the console user, the break-glass role, this role).
2. **The Terraform change**, in `infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf` ONLY (read lines 185-290 first):
   - a second `opal_name` module instance for the role, `system "cloudops"`, scope = `local.lgic_crm_scope.long`, `function "crm-match"`, `kind "role"`: the NAME comes from the builder, never typed. If the builder REFUSES (a missing registry row), add the row under `infra/logic/registry/` and say so; do not type a name;
   - `aws_iam_role` for it: trust = `sts:AssumeRole` for exactly ONE principal, the agents' shell user (read it once with `aws sts get-caller-identity --query Arn` and take that user's ARN as a `data "aws_iam_user"` like the console user's), no wildcard, no service; `max_session_duration = 3600`;
   - `aws_iam_role_policy` for it: Allow `s3:GetObject` on `arn:aws:s3:::<bucket>/commonwealth/cottonwood/bronze/crm/date=2026-06-23/CRM_CottonwoodCapitalAdvisors.zip` and NOTHING else (no version action, no list, no put); the bucket and key parts derived from `local.lgic_crm_bucket` and `local.lgic_crm_prefix` plus the date part and file name as literals of the one key;
   - `local.lgic_crm_readers` gains the role's ARN, derived from its builder-made name exactly as `lgic_crm_role_arn` is (a new role's ARN is unknown at plan time). It must NOT enter `lgic_crm_writers`.
   Commit it in your own linked worktree (CLAUDE.md rule 14b) and land it on `box/dell1` through `.tools/safe-merge.sh`; apply from the shared tree at that commit.
3. **Plan, targeted** at exactly the new role, its policy and `aws_s3_bucket_policy.lgic_firm`. Read the saved plan JSON: the role and policy are CREATED, the cottonwood firm bucket policy is UPDATED IN PLACE (its Deny statements: only the read-deny's readers list gains the role's ARN; the LIST deny and the WRITE deny are byte-equal), every other resource is a no-op. Any other change is the STOP (read AMENDMENT 1 below: the TCKT exemption is carved out of the worktree, so the plan must read 2 to add and 1 to change). Run `python infra/aws/terraform/shared-infra/tests/check_restricted_prefix.py` before and after and keep both outputs.

**AMENDMENT 1 (2.0.0_SA_COO~C1, 2026-10-15 ~19:4xZ), on the CTO's ruling amendment 6 (msg 6172), after your STOP of msg 6168: THE CARVE.** Your plan also carried the unapplied TCKT_VNEXT exemption (`89beb84dd9`, `51f1051aa1`, `infra/logic/registry/exemptions.json`), another project's change under another pair. It is carved out, not applied and not waited for:
- Plan AND apply from your worktree with `infra/logic/registry/exemptions.json` held at its content before `89beb84dd9` (`git show 89beb84dd9^:infra/logic/registry/exemptions.json`), in the WORKTREE ONLY, NEVER committed, NEVER landed on `box/dell1`. Land only the `.tf` change (and a registry row for the role's function if the builder asked for one). Record the carve in the ledger entry (live state keeps NO TCKT exemption exactly as now; its own apply adds it later).
- The carved plan must read EXACTLY **2 to add** (the role and its inline policy) and **1 to change** (the cottonwood firm bucket policy), and the policy diff must be exactly the role's ARN in the READ deny's readers. If the INFLECTION bucket policy (or any other) also changes, because the shared readers list puts the ARN there too, that is a change outside the pair: STOP and report, it is not accepted on effective-access grounds.
- Add the key `carve` to `GRANT_RECORD.json`: `{"exemptions_json_held_at": "89beb84dd9^", "never_committed": true, "plan_adds": 2, "plan_changes": 1}`; `plan_summary.other_changes` stays 0.

4. **Simulator** (comp-iam / `simulate-principal-policy`): the new role: the one key ALLOWED for `s3:GetObject`; another key under the same prefix, `s3:ListBucket` on the prefix, and `s3:PutObject` on the key NOT allowed.
5. **Apply**: `bash .tools/safe-apply.sh`, scoped to those addresses. Never a bare `terraform apply`.
6. **Read back** (live, each recorded): `aws iam get-role` (the ARN, the CreateDate, the trust principal, the max session), the inline policy (action and resource), the bucket policy statements (the readers list; the list and write denies unchanged), `check_restricted_prefix.py` still green (the agents' own user is still refused on the key).
7. **The record** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.7.0_AE_CloudOps~CB1/GRANT_RECORD.json` with exactly these top-level keys: `role_name`, `role_arn`, `created_utc`, `trust_principal`, `max_session_seconds`, `policy_actions`, `policy_resources`, `bucket_policy_reader_added`, `list_deny_unchanged`, `write_deny_unchanged`, `plan_summary` (`{"adds", "changes", "destroys", "other_changes", "saved_plan"}`), `simulator` (`{"key_allowed", "other_key_denied", "list_denied", "put_denied"}`), `apply_commit`, `ledger_entry`, `cvo_resigned_ref` (the sign-off line of precondition 2), `pair` (the two half paths and the COO half's sha256), `deadline_utc` (23:59Z of today as an ISO time), `not_established`; and a short `.md`. No account number, no CRM content, no secret.
8. **Report ONCE** to `2.0.0_SA_COO~C1` (the role name and ARN, the session-name rule the job will use, the deadline, AC1) and copy `1.0.0_SA_CTO~DELL1`. Then stop: the job is not yours.

## 2. BOUNDS

- **Grant.** The `<paths>` block below. No other change to Terraform, IAM, S3 or any other bucket: not the break-glass role, not the console user, not `lgic_crm_writers`, not the LIST or WRITE deny, not any other firm bucket. No S3 read or write of the CRM prefix or any object in it by you: `head-object` included (it belongs to the job).
- **NEVER** bare `terraform apply` (use `safe-apply`), `aws lambda update-function-code`, a destroy (that is `CB-cj-3`'s), a `--force` or a gate override. A half-landed grant (the role without the exception, or the reverse) is the STOP: do not leave it, tell the COO at once; `CB-cj-3` removes whatever landed.
- The role must be removable by the withdrawal alone: do not attach it to anything, do not widen its trust, do not add a second statement.

## 3. SURFACES

<paths>
infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf
infra/logic/registry/
infra/aws/terraform/shared-infra/tests/
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.7.0_AE_CloudOps~CB1/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.7.0_AE_CloudOps~CB1/ADVI_COTBKF.TO-CB-cj-1.proof_of_spec.json`.
<criterion id="CB88cj1-AC1" cell_refs="CB-cj-1"><invocation>timeout 60 python org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/round88/checks/crm_checks.py grant --file org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.7.0_AE_CloudOps~CB1/GRANT_RECORD.json</invocation><expect>^CRM-GRANT: OK role=set plan_other_changes=0 bad=-$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape and discipline: the one action, the one key, no other plan change, the reader is the role, the list and write denies unchanged, the ledger, the CVO re-sign and the deadline named.

## 5. WHEN YOU ARE DONE

Commit the record FIRST, your rows and the instance second; flip `<status>` to `complete` in the SAME commit only when AC1 passes. Report once to `2.0.0_SA_COO~C1`, copy `1.0.0_SA_CTO~DELL1`: the role name and ARN, the plan summary, the simulator results, the apply commit, AC1 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** PENDING at the cut (the spawn is the GO; the seat reads every precondition itself). Conditions (all, read by the executing seat): the pair signed on both halves; PRD ratified-text half SIGNED by the CVO (C3); the clock window. Executor: `0.7.0_AE_CloudOps~CB1`, a lane seated for this project. Authority: Andrew-direct 2026-10-15 ~19:0xZ, "I agree with (a), let's see what we can do with that for now."

<status>pending</status>
<round>88</round>
<workstream>~C1</workstream>
<to_id>ADVI_COTBKF.TO-CB-cj-1</to_id>
<slot>~CB1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<direct_act>false</direct_act>
<worker_class>worker</worker_class>
