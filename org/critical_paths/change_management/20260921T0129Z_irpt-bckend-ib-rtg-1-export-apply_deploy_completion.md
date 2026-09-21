# Deploy Completion Record
**Date opened:** 2026-09-21T01:29:12.175914+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260921T020047Z
**Deploy:** IRPT_BCKEND.TO-IB-rtg-1 arm (d)/(e) -- deploy irpt-export-render, export root, terraform update + IAM create, source_code_hash 9IMayS94if11cyKq51TbcyBG8cUwbbUWlQMlT9XhiaQ= -> cn8YKEP2oQdfvAjdpa32Wfp9oJqhAIMGkECv+H4vUg4=, prior live CodeSha256 read live (get-function-configuration) kept with build-store VersionId dECFEZtZArSJYdPy4.ImeVHBv6Q.jxBH as rollback source, both never-widen halves at HEAD naming packet blob 74a1004fde6e649c321f43d62cfbda5b61489b98
**Authored by:** 0.9.0_WK_IRPT_BCKEND~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | module.irpt_export_render.aws_lambda_function.this + aws_iam_role_policy.export_render_receipt | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha | APPLIED AND VERIFIED. safe-apply.sh (HALT_ACK=1, 25 routine general-fabric messages, none naming this act/export/irpt-export-render/IB-rtg-1) on aws_iam_role_policy.export_render_receipt (Creating -> Creation complete) and module.irpt_export_render.aws_lambda_function.this (Modifying -> Modifications complete): 'Apply complete! Resources: 1 added, 1 changed, 0 destroyed.' comp-tagauthz gate PASSED (0 candidate resources overwrite an access-granting tag); tombstone-gate CLEAN (1 create checked against 7 tombstones, no match). Served CodeSha256 read back via get-function-configuration == cn8YKEP2oQdfvAjdpa32Wfp9oJqhAIMGkECv+H4vUg4= (the built sha this ledger names). IAM policy irpt-export-render-receipt-policy read back via get-role-policy: exactly the two statements (ReadWriteExportReceiptOnly GetObject+PutObject on firms/*/generations/EXP-*/receipt.json; ListOnlyTheReceiptAddresses ListBucket prefix-conditioned) this packet declared. | CLOSED 20260921T020045Z |
| L2 | verify | export root post-apply | served CodeSha256 == cn8YKEP2oQdfvAjdpa32Wfp9oJqhAIMGkECv+H4vUg4= read back via get-function-configuration; re-plan 0 changes | Post-apply re-plan on the export root (terraform plan -detailed-exitcode, real backend): rc=0, 'No changes. Your infrastructure matches the configuration.' Arm-(d) subtraction gate re-confirmed: fresh 10-root plan taken pre-apply, 132 entries compared across all 10 roots, 0 paths subtracted (no data.aws_s3_object read-entry drift this run); export root showed EXACTLY 2 real changes (aws_iam_role_policy.export_render_receipt create + module.irpt_export_render.aws_lambda_function.this update, source_code_hash 9IMayS94if11cyKq51TbcyBG8cUwbbUWlQMlT9XhiaQ= -> cn8YKEP2oQdfvAjdpa32Wfp9oJqhAIMGkECv+H4vUg4=), matching the packet's declared set exactly; all 3 round-7 sibling roots (holdings, ops, performance) and all 6 non-round-7 roots (api, core, directory, intake, narrative, ycharts) read EMPTY after subtraction -- no pending sibling round-7 roots remain, rtg-1 was the last apply. Served CodeSha256 verified == cn8YKEP2oQdfvAjdpa32Wfp9oJqhAIMGkECv+H4vUg4= via get-function-configuration this run. | CLOSED 20260921T020046Z |

## Log

- 20260921T012912Z OPENED by 0.9.0_WK_IRPT_BCKEND~1 with 2 leg(s)
- 20260921T020045Z LEG L1 closed: APPLIED AND VERIFIED. safe-apply.sh (HALT_ACK=1, 25 routine general-fabric messages, none naming this act/export/irpt-ex
- 20260921T020046Z LEG L2 closed: Post-apply re-plan on the export root (terraform plan -detailed-exitcode, real backend): rc=0, 'No changes. Your infrast
- 20260921T020047Z CLOSED -- all 2 legs proven
