# Deploy Completion Record
**Date opened:** 2026-10-04T20:47:59.245273+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261004T215010Z
**Deploy:** NFRA_SPRINTWIN H3/H4: daily-sprint-generator image move (window + union + QA home) and role policy grants; QA trace (FWD-1). Never-widen pair signed: CTO @e92e21fef3, COO @740fb88d8b. Image tag consumers: 1 (the function).
**Authored by:** 4.0.0_SA_CRO~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD on origin carrying lambda_function.py blob d284642a32 + census scripts + device census script | ls-remote hash + blob read at that hash | origin CLOUD 740fb88d8b (ls-remote read 20:4xZ, pushed by 0.0.0_AB_MSTR~Z on Andrew-direct ~20:3xZ); at that hash lambda_function.py blob d284642a32 (== the image's committed bytes), commit_census.py f1ccc03abd (== @6c491b6e9d), .tools/sprint-device-census.py 103ad09a7d (site Z ran this blob from origin/CLOUD: 8265 commits, put etag MATCH) | CLOSED 20261004T204841Z |
| L2 | activation | image from committed bytes (git archive) pushed to ECR daily-sprint-generator:latest by the laptop MSTR | ECR digest read back + in-image lambda_function.py blob == d284642a32; 446603c3 still held (describe-images) | laptop 0.0.0_AB_MSTR (bus 82cd8a7f via 0.0.0_AB_MSTR~Z msg 29253): git archive 740fb88d8b infra/aws/lambda/daily_sprint_generator, docker build --provenance=false --sbom=false --platform linux/amd64, pushed :latest digest sha256:4e5987ce58505c727cb9fd6635641cf40599e4b0d9b93d569f080ad8a41ea694 (describe-images read-back; site Z read the same digest at 21:28Z); in-image /var/task/lambda_function.py blob d284642a32 == committed. Rollback 446603c3 held (6 images listed at 21:28Z). New images pushed: 1 of the 4 allowed (CTO condition 2). | CLOSED 20261004T213930Z |
| L3 | activation | safe-apply: aws_iam_role_policy.sprint update + -replace aws_lambda_function.sprint + aws_lambda_permission.sprint | Apply complete + get-function ResolvedImageUri == L2 digest + 0-diff re-plan | safe-apply (HALT_ACK=1; halt-gate messages: two routine base-slice items, 13d-old registry note and a routing pointer, not STOP-class) -replace aws_lambda_function.sprint + aws_lambda_permission.sprint: Apply complete! Resources: 2 added, 1 changed (aws_iam_role_policy.sprint), 2 destroyed. get-function ResolvedImageUri @sha256:4e5987ce58505c727cb9fd6635641cf40599e4b0d9b93d569f080ad8a41ea694 == L2 digest; State Active, LastUpdateStatus Successful; rule daily-sprint-generator-schedule target = the function ARN; unscoped re-plan: No changes (detailed-exitcode 0). Naming gate WARNs on the legacy daily-sprint-generator-* names only (rule 30 non-application, R19). | CLOSED 20261004T214256Z |
| L4 | verify | QA trace: invoke {qa:true}; pages + report JSON + watermark at the QA home read back; no write under daily-reports/ | invoke result + read-back lines + daily-reports/ listing unchanged | QA trace (FWD-1 hop H4), invoke {qa:true} 21:43:42Z-21:46:19Z StatusCode 200, FunctionError null: ok true, head b7f2fb4dc7 (origin), window 2026-10-03T21:05:36Z..2026-10-04T21:05:36Z, devices reported sitez 21:05:36Z + laptop 21:34:58Z, missing none, 386 commits (by_kind and by_project each sum 386), 50 not yet pushed (laptop 48, sitez 2), one repair pass. Read back at s3://opal-data-portal-v2/sprint/global/platinum/qa_page/date=2026-10-04/: Desktop + Mobile html 47941 B, report JSON 26317 B, watermark 477 B. daily-reports/ untouched: 69 objects before and after; the 10-04 pages still 20:12:59Z. Rendered headless: the area chart's hour labels read 17 18 ... 23 00 ... 17 (window start 17:05), 'now 17:05 ET'. One model-authored flow diagram draws a NaN marker (break_after typed as a stage name), surprise row NFRA_SPRINTWIN-Z-S4. | CLOSED 20261004T215010Z |

## Log

- 20261004T204759Z OPENED by 4.0.0_SA_CRO~Z with 4 leg(s)
- 20261004T204841Z LEG L1 closed: origin CLOUD 740fb88d8b (ls-remote read 20:4xZ, pushed by 0.0.0_AB_MSTR~Z on Andrew-direct ~20:3xZ); at that hash lambda
- 20261004T213930Z LEG L2 closed: laptop 0.0.0_AB_MSTR (bus 82cd8a7f via 0.0.0_AB_MSTR~Z msg 29253): git archive 740fb88d8b infra/aws/lambda/daily_sprint_
- 20261004T214256Z LEG L3 closed: safe-apply (HALT_ACK=1; halt-gate messages: two routine base-slice items, 13d-old registry note and a routing pointer, n
- 20261004T215010Z LEG L4 closed: QA trace (FWD-1 hop H4), invoke {qa:true} 21:43:42Z-21:46:19Z StatusCode 200, FunctionError null: ok true, head b7f2fb4d
- 20261004T215010Z CLOSED -- all 4 legs proven
