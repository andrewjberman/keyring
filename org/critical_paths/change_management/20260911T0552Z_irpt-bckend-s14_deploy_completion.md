# Deploy Completion Record
**Date opened:** 2026-09-11T05:52:02.615760+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260911T061554Z
**Deploy:** IRPT_BCKEND IB-s-14 -- the export worker and its role, first apply of the investor-reporting/export root
**Authored by:** 0.9.0_WK_IRPT_BCKEND~4
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | worktree branch wk-irpt_bckend-1-4 commit of the export package, the terraform root and the source-map entry | commit hash | commits 1beda4bf49 (the export package, the completed root, the CI maps and this ledger opened), e3fe224e30 (the repo-relative path that was an IndexError in /var/task, plus the two controls that catch it and a wrong walk depth) and ed38c92999 (capabilities reports per-contract availability instead of dying of it) on wk-irpt_bckend-1-4 -- LOCAL; a worker never pushes | CLOSED 20260911T061531Z |
| L2 | s3-prefix | s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-export-render.zip | head-object ContentLength + content-sha256 equal to the built zip | s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-export-render.zip -- build-and-upload.sh reported SHA256 HSuSKsWzsnqS4tIO/b+Zu4hYdpx2RNZxmeqavv7XwUw= and the write VERIFIED; re-read here by head-object: ContentLength=28254 and Metadata content-sha256 identical. The ADHC_DRIFTD.002 parity check refused the first build until download.py was registered in files[], which is why the cell's own source ships whole | CLOSED 20260911T061531Z |
| L3 | activation | terraform apply of infra/aws/terraform/investor-reporting/export (aws_iam_role.export_render + its logs policy + module.irpt_export_render) | safe-apply output | safe-apply.sh -chdir=infra/aws/terraform/investor-reporting/export apply, three runs: 'Apply complete! Resources: 4 added, 0 changed, 0 destroyed.' (aws_iam_role.export_render, aws_iam_role_policy.export_render_logs, the log group and module.irpt_export_render.aws_lambda_function.this), then '0 added, 1 changed, 0 destroyed' twice as the two invoke-found defects were corrected. FOUR ADDS AND NOTHING DESTROYED across all three: no existing bucket, table, Lambda, route or behavior was touched, and the irpt-common layer was READ by name, never modified | CLOSED 20260911T061531Z |
| L4 | verify | get-function-configuration irpt-export-render CodeSha256 equals the built zip sha256, the irpt-common layer is attached, an invoke reports its renderer absence, and a 0-diff plan on the root | verbatim CLI output | get-function-configuration irpt-export-render: CodeSha256 = HSuSKsWzsnqS4tIO/b+Zu4hYdpx2RNZxmeqavv7XwUw= -- byte-identical to the built zip, so the served bytes are verified against the BUILD INPUT and not by filename. State=Active, LastUpdateStatus=Successful, Layers[0]=arn:aws:lambda:us-east-1:313476888478:layer:irpt-common:2, Role=irpt-export-render-role. An invoke of the DEPLOYED function returns statusCode 200 and REPORTS what it cannot do rather than failing: renderer=unavailable with its reason, and contract_validators naming all three export contracts UNAVAILABLE at /var/_contracts -- the irpt-common layer carries PerformanceReport and NarrativePacket only, and extending it is outside this order's paths (a row, never an override). The 0-diff plan is S14-AC2 | CLOSED 20260911T061554Z |

## Log

- 20260911T055202Z OPENED by 0.9.0_WK_IRPT_BCKEND~4 with 4 leg(s)
- 20260911T061531Z LEG L1 closed: commits 1beda4bf49 (the export package, the completed root, the CI maps and this ledger opened), e3fe224e30 (the repo-re
- 20260911T061531Z LEG L2 closed: s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-export-render.zip -- build-and-upload.sh reported SHA256
- 20260911T061531Z LEG L3 closed: safe-apply.sh -chdir=infra/aws/terraform/investor-reporting/export apply, three runs: 'Apply complete! Resources: 4 adde
- 20260911T061554Z LEG L4 closed: get-function-configuration irpt-export-render: CodeSha256 = HSuSKsWzsnqS4tIO/b+Zu4hYdpx2RNZxmeqavv7XwUw= -- byte-identic
- 20260911T061554Z CLOSED -- all 4 legs proven
