# TO ADVI_COTBKF.TO-CB-cj-3.crm-match-withdrawal -- round 88 CB-cj-3: WITHDRAWAL -- the role and its reader exception removed the day the job ends, a re-plan reading no changes, every AssumeRole event on the role listed, the ledger closed

<!-- ===================== WORKER FACE -- this is the WHOLE of the executing seat's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round88.md</decomp_doc> (round 88), cell `CB-cj-3`.
<owned_cells>CB-cj-3</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~CB1</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a removal; nothing is scheduled.
comp-iam: RUN by the executing seat after the apply -- DENOMINATOR: 2 reads (`get-role` on the role, which must return `NoSuchEntity`, and `get-role` on the break-glass role as the positive control, which must return an ARN) plus 1 bucket-policy read for the readers list; BLIND: it sees IAM and the bucket policy, not a session already issued from the role (a session lives up to 3600 s after the delete; the AssumeRole list shows it).
comp-adversary: RUN by the issuer -- the record's checker fails any withdrawal that left the role or the reader, any re-plan with a change, any record without the AssumeRole list, and any record that does not say whether data events were read; BLIND: CloudTrail lags by up to about 15 minutes, so an AssumeRole event after the delete would not yet show (the record states the time of the last read and runs a second read once, after at least 15 minutes, and states what it found); and a trail that does not record S3 data events cannot show the GET (the record says so).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE ACT -- `CB-cj-3` (round 88, WORLD)

STAGED. You act only on the issuer's UN-PARK AMENDMENT (in this file's record face) or at the backstop below, whichever comes first.

**WHEN.** The withdrawal is the job's NEXT act: the issuer un-parks you the moment the job's record is written (the CTO's msg 6158: "withdrawn when the job ends"). The BACKSTOP, absolute (the CTO's C2): at **23:30Z** of the UTC day the role was created (`deadline_utc` in `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.7.0_AE_CloudOps~CB1/GRANT_RECORD.json` is that day's 23:59Z), you run this order WITHOUT waiting for any message, even if the job is still reading. A half-landed grant at any time (the role without the exception, or the reverse) is also a trigger: run it at once.

### 1a. Steps

1. **Read** the grant record (the role name and ARN, the ledger entry) and the job record if it exists (`.../deliverables/0.9.0_WK_ADVI_COTBKF~177/JOB_RECORD.json`; its start and end times). Note the UTC time. Do not read any CRM content and do not read the job's links file.
2. **Remove**: the Terraform change of `CB-cj-1` reverted (the role, its inline policy and the role's ARN in `local.lgic_crm_readers`; the module instance for the name), in `infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf` only: a revert commit in your own worktree landed on `box/dell1` through `.tools/safe-merge.sh` (rule 14b), then a targeted `safe-apply` at the same addresses (`bash .tools/safe-apply.sh`; never a bare apply). The plan before it must show exactly: the role and its policy DESTROYED and the cottonwood firm bucket policy UPDATED IN PLACE (the readers list loses the ARN); any other change is the STOP (say what, and do not apply it).
3. **Prove it is gone** (live, each recorded): `aws iam get-role` on the role returns `NoSuchEntity` and `get-role` on the break-glass role returns an ARN (the positive control); the bucket policy's three CRM Deny statements read as they did before the grant (compare to the pre-grant text in the grant record's `plan_summary.saved_plan` or the ledger entry); `python infra/aws/terraform/shared-infra/tests/check_restricted_prefix.py` green; a **re-plan** of the whole `shared-infra` root reads `0 to add, 0 to change, 0 to destroy`, saved as evidence.

**AMENDMENT 1 (2.0.0_SA_COO~C1, 2026-10-15 ~19:4xZ), on the CTO's ruling amendment 6 (msg 6172): THE WITHDRAWAL IS PLANNED THE SAME CARVED WAY.** Plan and apply the removal from your worktree with `infra/logic/registry/exemptions.json` held at its content before `89beb84dd9` (`git show 89beb84dd9^:infra/logic/registry/exemptions.json`), worktree only, never committed, so the withdrawal never applies the TCKT_VNEXT exemption either. The carved plan must read exactly 2 to destroy (the role and its policy) and 1 to change (the cottonwood bucket policy, losing the ARN); anything else is the STOP. The final CLEAN RE-PLAN of step 3 is read in the same carved worktree and reads `0 to add, 0 to change, 0 to destroy` EXCEPT for the TCKT exemption, which it will still show as an unapplied change on the cottonwood and inflection policies (name it in the record as the carved remainder: it is not yours and not a failure). Add `carve` to `WITHDRAWAL_RECORD.json` as in the grant record.

4. **C1: every AssumeRole event on the role.** From CloudTrail (`aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=AssumeRole`, paginated, over the window from the role's `created_utc` to now; filter those whose request names the role's ARN): list EVERY event with its time, the session name and the calling identity's ARN TYPE and name (the user name only, never an access key). Print the denominator (events scanned and events kept). Mark any session name other than `cotbkf-crm-match-177` as a FINDING. Run the read once now and once more after at least 15 minutes (CloudTrail lag), and state the time of each.
5. **S3 data events.** Say plainly whether the trail records S3 data events for the firm bucket (`aws cloudtrail get-event-selectors` on the trail that covers it). If it does, list the `GetObject` events on the one key in the same window (time, session name, bytes where recorded: no more). If it does not, write `data_events_recorded: false` and do not look further.
6. **The record** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.7.0_AE_CloudOps~CB1/WITHDRAWAL_RECORD.json` with exactly these top-level keys: `withdrawn_utc`, `trigger` (`job_ended` | `backstop` | `half_landed`), `role_deleted` (true only after the live `NoSuchEntity`), `reader_removed` (true only after the policy read), `positive_control` (the break-glass `get-role` returned an ARN), `replan` (`{"add", "change", "destroy", "saved"}`), `assume_role_events` (a list of `{"time", "session_name", "caller_type", "caller_name"}`), `assume_role_events_stated` (true), `assume_role_scan` (`{"scanned", "kept", "first_read_utc", "second_read_utc"}`), `findings` (sessions other than the job's, else empty), `data_events_recorded` (true or false), `data_events_stated` (true), `get_object_events` (a list or empty), `ledger_closed` (true only when closed), `revert_commit`, `not_established`; and a short `.md`. No account number, no CRM content, no key id, no secret.
7. **Close** the ledger entry (the `deploy_completion` file and the `.open_deploys/` sentinel) naming the revert commit and the clean re-plan. Report ONCE to `2.0.0_SA_COO~C1`, copy `1.0.0_SA_CTO~DELL1`: the trigger, the removal proof, the re-plan line, the AssumeRole list (counts and any finding), AC1 and the FULL commit hash.

## 2. BOUNDS

- **Grant.** The `<paths>` block below. You remove exactly what `CB-cj-1` created and nothing else. You do not touch the break-glass role, the console user, the LIST or WRITE deny, `lgic_crm_writers`, any other bucket, or any other resource; a re-plan that shows a change you did not make is a finding to report, not something to apply.
- **NEVER** a bare `terraform apply` or `destroy` (use `safe-apply`), a `--force`, a gate override. Do NOT read the CRM zip or the job's links; do NOT `head-object` the key.
- If the removal cannot be completed (for example a plan with another change, or an apply error), say so at once to `2.0.0_SA_COO~C1` and `1.0.0_SA_CTO~DELL1`, leave the ledger entry OPEN with the exact state, and do not proceed with anything else; the backstop does not excuse leaving it unreported.

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
Instance at `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.7.0_AE_CloudOps~CB1/ADVI_COTBKF.TO-CB-cj-3.proof_of_spec.json`.
<criterion id="CB88cj3-AC1" cell_refs="CB-cj-3"><invocation>timeout 60 python org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/round88/checks/crm_checks.py withdrawal --file org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.7.0_AE_CloudOps~CB1/WITHDRAWAL_RECORD.json</invocation><expect>^CRM-WITHDRAWAL: OK events=\d+ bad=-$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape and discipline: the role and the reader both gone, the re-plan clean (0 0 0), the AssumeRole list present and stated, whether data events are recorded stated, the ledger closed.

## 5. WHEN YOU ARE DONE

Commit the record FIRST, your rows and the instance second; flip `<status>` to `complete` in the SAME commit only when AC1 passes. Report once as step 7 says.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** STAGED at the cut. Un-park: the job's record written (the issuer's amendment), or 23:30Z of the grant day (backstop, no message needed), or a half-landed grant. Executor: `0.7.0_AE_CloudOps~CB1`. Authority: Andrew-direct 2026-10-15, "I agree with (a), let's see what we can do with that for now."; CTO ruling amendment 5 and the pair's conditions C1 and C2.

<status>staged</status>
<round>88</round>
<workstream>~C1</workstream>
<to_id>ADVI_COTBKF.TO-CB-cj-3</to_id>
<slot>~CB1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<direct_act>false</direct_act>
<worker_class>worker</worker_class>
