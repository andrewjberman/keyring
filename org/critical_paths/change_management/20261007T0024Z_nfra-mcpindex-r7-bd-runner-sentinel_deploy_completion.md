# Deploy Completion Record
**Date opened:** 2026-10-07T00:24:31.171357+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261008T222217Z
**Deploy:** MX-s-18 PHASE B: bd-49f-runner decides completeness itself + one IAM statement for the sentinel read-back (halves COO @27501e83dd, CTO AMENDMENT 1 @02b8f2267a, MX-s-18 alone)
**Authored by:** 0.7.0_AE_CloudOps~MI
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 30.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | s3-prefix | upload bd-pipeline/bd-49f-runner.zip with content-sha256 metadata; read size + VersionId + metadata back | yes | Uploaded 2026-10-07T00:47:41Z. Read back: VersionId FDxfrLHMGsYonkwadrCWZE11sYtKPhw., Size 6936, Metadata content-sha256 9PbO1/mVokBTWGNn8NjjTyjkhWvBdZ6pZk2zcCE0/eY= -- equal to the local zip's computed sha and to the signed pin. The rollback version AVNCLX4FqgXkDQwMLgoYD86veMQzY8mQ is still retrievable (5,199 B, content-sha256 q37ovM/F07p39ObyY6bML9tmIEXDN1S/OhyJv1oDH00=), verified by head-object --version-id. | CLOSED 20261007T005326Z |
| P1 | verify | ONE saved plan targeted to module.bd_49f_runner + aws_iam_role_policy.bd_49f_runner_policy reads 0 to add, 2 to change, 0 to destroy | yes | ONE saved plan, targeted to module.bd_49f_runner + aws_iam_role_policy.bd_49f_runner_policy, read 'Plan: 0 to add, 2 to change, 0 to destroy' -- the CTO condition-2 number exactly. Diff audited line by line: 7 added lines forming EXACTLY ONE statement (Sid ReadBackBdBronzeSentinel, Effect Allow, Action [s3:GetObject], Resource [arn:aws:s3:::opal-data-bd/bronze/*/_BRONZE_COMPLETE.json]) and ZERO removed lines. Changed attributes: the policy's jsonencode Statement list, and the Lambda's last_modified / s3_object_version / source_code_hash. Nothing else. The rendered Resource equals the literal the half names, which is what makes the derived terraform reference admissible. Log .scratch/plan18.log. | CLOSED 20261007T005326Z |
| R1 | verify | after safe-apply: deployed CodeSha256 == the built zip sha 9PbO1/mVokBTWGNn8NjjTyjkhWvBdZ6pZk2zcCE0/eY= | yes | safe-apply at 2026-10-07T00:49:58Z: 'Apply complete! Resources: 0 added, 2 changed, 0 destroyed', rc=0; comp-tagauthz PASSED, tombstone-gate CLEAN. Deployed CodeSha256 read back at 00:51:24Z = 9PbO1/mVokBTWGNn8NjjTyjkhWvBdZ6pZk2zcCE0/eY=, equal to the built zip; LastModified 2026-10-07T00:50:44Z, python3.12, 1024 MB, 900 s timeout. | CLOSED 20261007T005326Z |
| R2 | verify | after safe-apply: simulate-principal-policy GetObject on the sentinel key reads allowed (row Z-W24-S11 disarm) | yes | simulate-principal-policy on bd-49f-runner-role at 00:51Z: s3:GetObject ALLOWED on bronze/2026-10-07/_BRONZE_COMPLETE.json AND on bronze/2026-10-08/_BRONZE_COMPLETE.json (the key tomorrow's run reads); PutObject still allowed. Row Z-W24-S11 DISARMED on this applied read, per amendment A1. TWO CONTROLS, because 'allowed' alone does not prove the grant stayed narrow: (i) NARROWNESS -- bronze/2026-10-07/some_other_object.json reads implicitDeny, so the grant did NOT widen to bronze/*; (ii) FIRM-SEP -- opal-data-cot/bronze/2026-10-07/_BRONZE_COMPLETE.json reads explicitDeny, so DenyCotPlane still wins and CLAUDE.md NEVER#1 holds. | CLOSED 20261007T005326Z |
| V1 | verify | the 2026-10-08 00:00Z scheduled run log line -- OK after read-back, or WARN naming tables | yes | Read 2026-10-08T22:2xZ by 2.0.0_SA_COO~MI (issuer; the author seat is dark after the site Z reboot). Scheduled run 2026-10-08T00:00:19Z, RequestId 9c228e2b-4c66-424e-ba30-170c887d7ea5, log stream 2026/10/08/[$LATEST]67db8870...: line "OK: bronze sentinel emitted for 2026-10-08 (tables=[(transactions, 2026-10-08), (realized, 2026-10-08)])" -- the deployed code prints it only after head_object reads the key back (lambda_function.py:189-198). RESULT sentinel=emitted, failed=[], auth_dead=False; allocations and unrealized rejected as header-only snapshots (pre-existing reject path, not in landed). Independent read: s3api head-object opal-data-bd bronze/2026-10-08/_BRONZE_COMPLETE.json LastModified 2026-10-08T00:11:37Z, 277 B, VersionId Wkk3SufwV3Rc9WX35irXe7FUTo5WBuXl; control 10-07 key 00:11:33Z 277 B. | CLOSED 20261008T222217Z |
| bd-49f-runner | tf-lambda | module.bd_49f_runner.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | module.bd_49f_runner.aws_lambda_function.this modified in place (6s), 0 added 0 destroyed. Identity proven by CodeSha256 9PbO1/mVokBTWGNn8NjjTyjkhWvBdZ6pZk2zcCE0/eY= rather than by filename or by the apply's own rc. | CLOSED 20261007T005326Z |

## Log

- 20261007T002431Z OPENED by 0.7.0_AE_CloudOps~MI with 6 leg(s)
- 20261007T005326Z LEG U1 closed: Uploaded 2026-10-07T00:47:41Z. Read back: VersionId FDxfrLHMGsYonkwadrCWZE11sYtKPhw., Size 6936, Metadata content-sha256
- 20261007T005326Z LEG P1 closed: ONE saved plan, targeted to module.bd_49f_runner + aws_iam_role_policy.bd_49f_runner_policy, read 'Plan: 0 to add, 2 to 
- 20261007T005326Z LEG R1 closed: safe-apply at 2026-10-07T00:49:58Z: 'Apply complete! Resources: 0 added, 2 changed, 0 destroyed', rc=0; comp-tagauthz PA
- 20261007T005326Z LEG bd-49f-runner closed: module.bd_49f_runner.aws_lambda_function.this modified in place (6s), 0 added 0 destroyed. Identity proven by CodeSha256
- 20261007T005326Z LEG R2 closed: simulate-principal-policy on bd-49f-runner-role at 00:51Z: s3:GetObject ALLOWED on bronze/2026-10-07/_BRONZE_COMPLETE.js
- 20261008T222217Z LEG V1 closed: Read 2026-10-08T22:2xZ by 2.0.0_SA_COO~MI (issuer; the author seat is dark after the site Z reboot). Scheduled run 2026-
- 20261008T222217Z CLOSED -- all 6 legs proven
