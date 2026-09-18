# Deploy Completion Record
**Date opened:** 2026-09-18T08:44:57.673210+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-rtc-7: the 49 Financial source principal applied under sign-off (K1-K4 directory root create/update, K3 mdpf-pipeline targeted)
**Authored by:** 0.9.0_WK_IRPT_BCKEND~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | aws_iam_role.irpt_49f_directory_read + aws_iam_role_policy.irpt_49f_directory_read (K1+K2, directory root) | TF apply 0 destroy + post-apply get-role/get-role-policy |  | OPEN |
| L2 | activation | aws_iam_role_policy.mdpf_runner (K3, mdpf-pipeline root, TARGETED) | TF targeted apply 1 to change/0 add/0 destroy + post-apply get-role-policy sha256 |  | OPEN |
| L3 | verify | negative control (N1-N5) + 49f third-directory fire + writer census unchanged | SSM transcripts + writer census output |  | OPEN |
| irpt-directory-refresh | tf-lambda | module.irpt_directory_refresh.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20260918T084457Z OPENED by 0.9.0_WK_IRPT_BCKEND~1 with 4 leg(s)
