# Deploy Completion Record
**Date opened:** 2026-10-04T20:47:59.245273+00:00
**Status:** OPEN
**Deploy:** NFRA_SPRINTWIN H3/H4: daily-sprint-generator image move (window + union + QA home) and role policy grants; QA trace (FWD-1). Never-widen pair signed: CTO @e92e21fef3, COO @740fb88d8b. Image tag consumers: 1 (the function).
**Authored by:** 4.0.0_SA_CRO~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD on origin carrying lambda_function.py blob d284642a32 + census scripts + device census script | ls-remote hash + blob read at that hash | origin CLOUD 740fb88d8b (ls-remote read 20:4xZ, pushed by 0.0.0_AB_MSTR~Z on Andrew-direct ~20:3xZ); at that hash lambda_function.py blob d284642a32 (== the image's committed bytes), commit_census.py f1ccc03abd (== @6c491b6e9d), .tools/sprint-device-census.py 103ad09a7d (site Z ran this blob from origin/CLOUD: 8265 commits, put etag MATCH) | CLOSED 20261004T204841Z |
| L2 | activation | image from committed bytes (git archive) pushed to ECR daily-sprint-generator:latest by the laptop MSTR | ECR digest read back + in-image lambda_function.py blob == d284642a32; 446603c3 still held (describe-images) |  | OPEN |
| L3 | activation | safe-apply: aws_iam_role_policy.sprint update + -replace aws_lambda_function.sprint + aws_lambda_permission.sprint | Apply complete + get-function ResolvedImageUri == L2 digest + 0-diff re-plan |  | OPEN |
| L4 | verify | QA trace: invoke {qa:true}; pages + report JSON + watermark at the QA home read back; no write under daily-reports/ | invoke result + read-back lines + daily-reports/ listing unchanged |  | OPEN |

## Log

- 20261004T204759Z OPENED by 4.0.0_SA_CRO~Z with 4 leg(s)
- 20261004T204841Z LEG L1 closed: origin CLOUD 740fb88d8b (ls-remote read 20:4xZ, pushed by 0.0.0_AB_MSTR~Z on Andrew-direct ~20:3xZ); at that hash lambda
