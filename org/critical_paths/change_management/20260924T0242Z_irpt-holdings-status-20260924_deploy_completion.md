# Deploy Completion Record
**Date opened:** 2026-09-24T02:42:35.456096+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260924T024831Z
**Deploy:** IRPT Holdings success-status repackage: holdings/entry.py at 13012979e1 (CRO), CTO GO 100008, Andrew-direct fix the ready flag
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | safe-apply of the saved one-function plan (0/1/0: only s3_object_version / source_code_hash move) | apply output line | safe-apply of the SAVED plan .runtime/holdings-status/status.tfplan (sha256 af3b34e31168ac6e re-read before the act) from the backend worktree holdings root, HALT_ACK=1 over the routine base-inbox subjects: module.irpt_holdings.aws_lambda_function.this Modifications complete after 6s; Apply complete 0 added / 1 changed / 0 destroyed rc=0 at 2026-09-24T02:45:27Z; apply.log sha256 b7bda53f40ffbbe2 | CLOSED 20260924T024831Z |
| V1 | verify | get-function-configuration CodeSha256 == the built sha, layer irpt-common:5 / handler / env / role unchanged; re-plan rc 0 | readback + plan rc | get-function-configuration irpt-holdings: CodeSha256 3nc57No0b8rSnz9xbyenToYWgb91aoDT87RHrIJ5vAQ= LastModified 2026-09-24T02:45:22Z, Handler entry.lambda_handler, Layers [irpt-common:5], State Active, LastUpdateStatus Successful; Handler/Layers/Role/Env/Timeout/MemorySize equal to the 01:38Z sink readback (post-config.json x2 compared); re-plan -detailed-exitcode rc 0 No changes (post-plan.log). Member census: new zip Q1V60Swh 33 members vs deployed tndS2IuX 33 members, differing = [entry.py] exactly one, entry.py sha256 == pin bytes 6660c155 | CLOSED 20260924T024831Z |
| R1 | verify | record-terraform-deploy.sh irpt-holdings with the ledger commit and the code sha | recorder commit | record-terraform-deploy.sh investor-reporting --function irpt-holdings --deploy-ledger 61a03f2c26 --code-sha256 3nc57No0...: committed c29054e73c in irpt-p-publish-20260923; source map irpt-holdings deployed_code_sha256 3nc57No0... last_deployed_at 2026-09-24T02:46:41Z deploy_ledger 61a03f2c26 | CLOSED 20260924T024831Z |

## Log

- 20260924T024235Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260924T024831Z LEG A1 closed: safe-apply of the SAVED plan .runtime/holdings-status/status.tfplan (sha256 af3b34e31168ac6e re-read before the act) fro
- 20260924T024831Z LEG V1 closed: get-function-configuration irpt-holdings: CodeSha256 3nc57No0b8rSnz9xbyenToYWgb91aoDT87RHrIJ5vAQ= LastModified 2026-09-2
- 20260924T024831Z LEG R1 closed: record-terraform-deploy.sh investor-reporting --function irpt-holdings --deploy-ledger 61a03f2c26 --code-sha256 3nc57No0
- 20260924T024831Z CLOSED -- all 3 legs proven
