# Deploy Completion Record
**Date opened:** 2026-09-10T23:04:05.467811+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260910T231318Z
**Deploy:** IRPT IB-s-1: irpt-directory-search Lambda + irpt-directory-role, and the QA directory objects in three firm buckets
**Authored by:** 0.9.0_WK_IRPT_BCKEND~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | wk-irpt_bckend-1-2 source commit for the runner, handler and TF root | commit hash on the worker branch (LOCAL, never pushed) | 3654197107 on wk-irpt_bckend-1-2 (LOCAL; a worker never pushes). 11 files, 2947 insertions. git status --porcelain infra/aws/lambda/ = empty, so build-and-upload's committed-source gate is satisfied. | CLOSED 20260910T230424Z |
| L2 | s3-prefix | opal-313476888478-lambda-artifacts investor-reporting/irpt-directory-search.zip | head-object ContentLength + content-sha256 metadata == the built zip sha256 | head-object s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-directory-search.zip -> ContentLength=5497, VersionId=woeOoLg5DL7qM_xwuX7ntbuVVMmOkFg0, Metadata.content-sha256=7OOoRBhYUc9t8pjV48MJR7erKIifjFFdOJu3zdH4enk= == the sha256 build-and-upload computed over the built zip. Verified by CONTENT (size + sha metadata), never by filename. | CLOSED 20260910T230516Z |
| L3 | activation | terraform apply of infra/aws/terraform/investor-reporting/directory (state key investor-reporting/directory/tfstate) creating irpt-directory-role and irpt-directory-search | safe-apply output + get-function-configuration CodeSha256 | safe-apply.sh (HALT-GATE passed after the session serial file was written) -> 'Apply complete! Resources: 4 added, 0 changed, 0 destroyed.' Created: aws_iam_role.irpt_directory (irpt-directory-role), aws_iam_role_policy.irpt_directory, module.irpt_directory_search.aws_lambda_function.this (irpt-directory-search), module.irpt_directory_search.aws_cloudwatch_log_group.lambda. 0 changed and 0 destroyed = no existing resource touched. role_arn arn:aws:iam::313476888478:role/irpt-directory-role | CLOSED 20260910T230916Z |
| L4 | s3-prefix | QA directory objects under investor-reporting/qa/directory/ in opal-data-bd, opal-data-inf, opal-data-cot | head-object on each firm latest.json | head-object on all 3 of 3 firm QA pointers (investor-reporting/qa/directory/latest.json): opal-data-bd 275 B ETag 6f13651d866579d69290e02d2bb34992; opal-data-inf 273 B ETag c19333fa02e5624d4b9fb6789478f6a9; opal-data-cot 273 B ETag b9122ed1f7b1cc3e52727f8970b2ba4c. The dated objects landed with an in-runner ContentLength==built-size verify: 49F 2026-09-09 4509 entries, INF 2026-09-10 293, COT 2026-09-09 260; 5062 of 5062 valid against DirectoryEntry.schema.json. | CLOSED 20260910T231257Z |
| L5 | verify | 0-diff terraform plan on the directory root (criterion S1-AC2) and the IB-s-1 battery arm (f) | plan No changes + battery ARM f PASS | terraform plan -no-color -input=false -lock=false on infra/aws/terraform/investor-reporting/directory AFTER the apply -> 'No changes. Your infrastructure matches the configuration.' rc=0 (criterion S1-AC2). Apply read 4 added / 0 changed / 0 destroyed, so no existing resource was touched. Battery arm (f) grades the served CodeSha256 against the artifact's own content-sha256 in the same run. | CLOSED 20260910T231257Z |

## Log

- 20260910T230405Z OPENED by 0.9.0_WK_IRPT_BCKEND~2 with 5 leg(s)
- 20260910T230424Z LEG L1 closed: 3654197107 on wk-irpt_bckend-1-2 (LOCAL; a worker never pushes). 11 files, 2947 insertions. git status --porcelain infra
- 20260910T230516Z LEG L2 closed: head-object s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-directory-search.zip -> ContentLength=5497, 
- 20260910T230916Z LEG L3 closed: safe-apply.sh (HALT-GATE passed after the session serial file was written) -> 'Apply complete! Resources: 4 added, 0 cha
- 20260910T231257Z LEG L4 closed: head-object on all 3 of 3 firm QA pointers (investor-reporting/qa/directory/latest.json): opal-data-bd 275 B ETag 6f1365
- 20260910T231257Z LEG L5 closed: terraform plan -no-color -input=false -lock=false on infra/aws/terraform/investor-reporting/directory AFTER the apply ->
- 20260910T231318Z CLOSED -- all 5 legs proven
