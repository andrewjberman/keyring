# Deploy Completion Record
**Date opened:** 2026-09-21T01:29:12.175914+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND.TO-IB-rtg-1 arm (d)/(e) -- deploy irpt-export-render, export root, terraform update + IAM create, source_code_hash 9IMayS94if11cyKq51TbcyBG8cUwbbUWlQMlT9XhiaQ= -> cn8YKEP2oQdfvAjdpa32Wfp9oJqhAIMGkECv+H4vUg4=, prior live CodeSha256 read live (get-function-configuration) kept with build-store VersionId dECFEZtZArSJYdPy4.ImeVHBv6Q.jxBH as rollback source, both never-widen halves at HEAD naming packet blob 74a1004fde6e649c321f43d62cfbda5b61489b98
**Authored by:** 0.9.0_WK_IRPT_BCKEND~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | module.irpt_export_render.aws_lambda_function.this + aws_iam_role_policy.export_render_receipt | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha |  | OPEN |
| L2 | verify | export root post-apply | served CodeSha256 == cn8YKEP2oQdfvAjdpa32Wfp9oJqhAIMGkECv+H4vUg4= read back via get-function-configuration; re-plan 0 changes |  | OPEN |

## Log

- 20260921T012912Z OPENED by 0.9.0_WK_IRPT_BCKEND~1 with 2 leg(s)
