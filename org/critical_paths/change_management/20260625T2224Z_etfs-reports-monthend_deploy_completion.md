# Deploy Completion Record
**Date opened:** 2026-06-25T22:24:33.983750+00:00
**Status:** OPEN
**Deploy:** ETFS month-end report cloud-run: transient EC2 + orchestrator Lambda + EventBridge 1st@10ET + SES email
**Authored by:** 0.5.0_AE_OpalETL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| git | git | commit etfs-reports TF root + orchestrator Lambda + source-map + manifest | hash pushed |  | OPEN |
| artifact | s3-prefix | render_month_end.py -> s3 ec2/etfs-reports/ | aws s3 ls confirm | aws s3 ls s3://opal-313476888478-lambda-artifacts/ec2/etfs-reports/ -> render_month_end.py 32020 bytes 2026-06-25 18:24:52 | CLOSED 20260625T222511Z |
| tf-apply | tf-lambda | etfs-reports root: EC2 + role + orchestrator Lambda + 2 schedulers + SNS | 0-diff-apply |  | OPEN |
| verify | verify | manual orchestrator {mode:run} invoke renders+emails last-month report | invoke-output + S3 report + email sent |  | OPEN |

## Log

- 20260625T222433Z OPENED by 0.5.0_AE_OpalETL with 4 leg(s)
- 20260625T222511Z LEG artifact closed: aws s3 ls s3://opal-313476888478-lambda-artifacts/ec2/etfs-reports/ -> render_month_end.py 32020 bytes 2026-06-25 18:24:
