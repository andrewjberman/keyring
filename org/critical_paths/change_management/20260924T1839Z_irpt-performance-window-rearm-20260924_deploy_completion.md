# Deploy Completion Record
**Date opened:** 2026-09-24T18:39:51.481279+00:00
**Status:** OPEN
**Deploy:** irpt-performance-adapter: series-window fix dd1811bbaa + ONE re-armed one-use COT plan (Andrew f0bd1c267e)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| B1 | verify | artifact build: bd_selected.py row re-pinned to dd1811bbaa, one member differs | census vs deployed 07lSH03z: 61 of 61 names equal, exactly bd_selected.py differs | build-and-upload.sh investor-reporting irpt-performance-adapter (BAU_PARITY_SKIP=1 for the three local build tools, as at 7a8d2a4ca3) with the bd_selected.py row re-pinned 7a8d2a4ca3 -> dd1811bbaa (blob sha256 b6dbaf50..); artifact NuIaCuqnx5BbfCq9WdXtJMuNLzC4dM3IrA8Ap8b0/Wk= 364216 bytes, S3 version stlLoLdtJ7a7FXhl205hUSB2dFbJbXDS, write VERIFIED; census vs deployed xG9..VR5J (07lSH03z): 61 of 61 names equal, exactly bd_selected.py differs | CLOSED 20260924T184212Z |
| A1 | activation | module.irpt_performance_adapter + env plan | safe-apply of the saved plan; readback CodeSha256 = built sha; IRPT_PERF_VENDOR_EGRESS_AUTHORIZED = new plan sha | safe-apply (HALT_ACK=1, .tools/terraform.exe 1.9.8, backend worktree performance root, var-file in the session scratchpad, never in the repo) of the saved plan 0/1/0: source_code_hash 07lSH03z -> NuIaCuqn, s3_object_version xG9..VR5J -> stlLoLdt, env plan approval_ref 9b36d8a481 card 2 -> f0bd1c267e, IRPT_PERF_VENDOR_EGRESS_AUTHORIZED 106eaa0e -> 99052771; Apply complete 0 added 1 changed 0 destroyed at 18:46:48Z; readback CodeSha256 NuIaCuqnx5BbfCq9WdXtJMuNLzC4dM3IrA8Ap8b0/Wk= LastModified 18:46:42Z, egress sha 99052771fbf4d0822beffd734e4fff955da4b53812a64d257ba0bc941e5e9ef3; use row PERFORMANCE_USE#99052771.. absent (unspent) | CLOSED 20260924T184805Z |
| V1 | verify | performance root re-plan | terraform plan -detailed-exitcode rc=0 with the var-file; State Active, LastUpdateStatus Successful | terraform plan -detailed-exitcode with the var-file rc=0 No changes at 18:47Z; State Active, LastUpdateStatus Successful, Handler runtime.lambda_handler, 1536 MB | CLOSED 20260924T184805Z |
| R1 | git | deploy recorder | record-terraform-deploy commit | record-terraform-deploy.sh investor-reporting --function irpt-performance-adapter --deploy-ledger 97fa08b076 --code-sha256 NuIaCuqn..: commit c67c4143e9 on irpt-p-publish-20260923 (source map commit 8f3f42c751) | CLOSED 20260924T184911Z |
| S1 | verify | served journey | Andrew's signed-in request on acc_d486fc94..: PERFORMANCE_ACCEPTED row + a READY report, or the use's named refusal read from the log |  | OPEN |

## Log

- 20260924T183951Z OPENED by 2.0.0_SA_COO~P with 5 leg(s)
- 20260924T184212Z LEG B1 closed: build-and-upload.sh investor-reporting irpt-performance-adapter (BAU_PARITY_SKIP=1 for the three local build tools, as a
- 20260924T184805Z LEG A1 closed: safe-apply (HALT_ACK=1, .tools/terraform.exe 1.9.8, backend worktree performance root, var-file in the session scratchpa
- 20260924T184805Z LEG V1 closed: terraform plan -detailed-exitcode with the var-file rc=0 No changes at 18:47Z; State Active, LastUpdateStatus Successful
- 20260924T184911Z LEG R1 closed: record-terraform-deploy.sh investor-reporting --function irpt-performance-adapter --deploy-ledger 97fa08b076 --code-sha2
