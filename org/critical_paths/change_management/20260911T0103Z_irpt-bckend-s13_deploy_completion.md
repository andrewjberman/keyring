# Deploy Completion Record
**Date opened:** 2026-09-11T01:03:44.231072+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260911T013606Z
**Deploy:** IRPT_BCKEND IB-s-13 -- the narrative Lambda and its read-only role, first apply of the investor-reporting/narrative root
**Authored by:** 0.9.0_WK_IRPT_BCKEND~4
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | worktree branch wk-irpt_bckend-1-4 commit of the narrative package, the terraform root and the source-map entry | commit hash | commit a12b0df4e7 on wk-irpt_bckend-1-4 (LOCAL; a worker never pushes): the narrative package (events/evidence/prose/handler/event_policy), 37 offline tests, four fixtures, the completed terraform root and the irpt-narrative source-map entry | CLOSED 20260911T013604Z |
| L2 | s3-prefix | s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-narrative.zip | head-object ContentLength + content-sha256 equal to the built zip | build-and-upload.sh investor-reporting irpt-narrative: SHA256 nuMb7eMlN8ou41LSSUOsUDR8T5U5uilo7N1XUcwU1IQ= size 53013, import-closure OK for 4 packaged .py files; write VERIFIED by the script and re-read here by head-object (ContentLength=53013, Metadata content-sha256 identical) at s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-narrative.zip | CLOSED 20260911T013605Z |
| L3 | activation | terraform apply of infra/aws/terraform/investor-reporting/narrative (aws_iam_role.narrative + two read-only policies + module.irpt_narrative) | safe-apply output | safe-apply.sh -chdir=infra/aws/terraform/investor-reporting/narrative apply: 'Apply complete! Resources: 5 added, 0 changed, 0 destroyed.' -- aws_iam_role.narrative, aws_iam_role_policy.narrative_logs, aws_iam_role_policy.narrative_news_read, the log group and module.irpt_narrative.aws_lambda_function.this. FIVE ADDS AND NOTHING CHANGED OR DESTROYED: no existing bucket, table, Lambda, route or behavior was touched, and the news producers were read, never written. | CLOSED 20260911T013605Z |
| L4 | verify | get-function-configuration irpt-narrative CodeSha256 equals the built zip sha256, the layer is attached, and a 0-diff plan on the root | verbatim CLI output | get-function-configuration irpt-narrative: CodeSha256 = nuMb7eMlN8ou41LSSUOsUDR8T5U5uilo7N1XUcwU1IQ= -- byte-identical to the built zip, so the served bytes are verified against the BUILD INPUT and not by filename. State=Active, LastUpdateStatus=Successful, Layers[0]=arn:aws:lambda:us-east-1:313476888478:layer:irpt-common:2, Role=irpt-narrative-role. An invoke of the DEPLOYED function over its offline fixture returns statusCode 200 with contract_validated=true, prose VALIDATED, asserts_causation=false, 9 events and 42 cited-evidence rows. | CLOSED 20260911T013605Z |

## Log

- 20260911T010344Z OPENED by 0.9.0_WK_IRPT_BCKEND~4 with 4 leg(s)
- 20260911T013604Z LEG L1 closed: commit a12b0df4e7 on wk-irpt_bckend-1-4 (LOCAL; a worker never pushes): the narrative package (events/evidence/prose/han
- 20260911T013605Z LEG L2 closed: build-and-upload.sh investor-reporting irpt-narrative: SHA256 nuMb7eMlN8ou41LSSUOsUDR8T5U5uilo7N1XUcwU1IQ= size 53013, i
- 20260911T013605Z LEG L3 closed: safe-apply.sh -chdir=infra/aws/terraform/investor-reporting/narrative apply: 'Apply complete! Resources: 5 added, 0 chan
- 20260911T013605Z LEG L4 closed: get-function-configuration irpt-narrative: CodeSha256 = nuMb7eMlN8ou41LSSUOsUDR8T5U5uilo7N1XUcwU1IQ= -- byte-identical t
- 20260911T013606Z CLOSED -- all 4 legs proven
