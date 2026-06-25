# Deploy Completion Record
**Date opened:** 2026-06-25T22:24:33.983750+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260625T233200Z
**Deploy:** ETFS month-end report cloud-run: transient EC2 + orchestrator Lambda + EventBridge 1st@10ET + SES email
**Authored by:** 0.5.0_AE_OpalETL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| git | git | commit etfs-reports TF root + orchestrator Lambda + source-map + manifest | hash pushed | ed506fbd3 committed (TF root + orchestrator Lambda + source-map + ledger; EC2_MANIFEST handed to 0.7.0) | CLOSED 20260625T222559Z |
| artifact | s3-prefix | render_month_end.py -> s3 ec2/etfs-reports/ | aws s3 ls confirm | aws s3 ls s3://opal-313476888478-lambda-artifacts/ec2/etfs-reports/ -> render_month_end.py 32020 bytes 2026-06-25 18:24:52 | CLOSED 20260625T222511Z |
| tf-apply | tf-lambda | etfs-reports root: EC2 + role + orchestrator Lambda + 2 schedulers + SNS | 0-diff-apply | safe-apply: Apply complete 16 added 0 changed 0 destroyed; reporter i-070477bf35fc54409, orchestrator Lambda + 2 schedulers + SNS live; 0-diff plan verified | CLOSED 20260625T222948Z |
| verify | verify | manual orchestrator {mode:run} invoke renders+emails last-month report | invoke-output + S3 report + email sent | 4th orchestrator {mode:run}: SSM render Success rc=0, S3 has etf_ownership.pdf 189054B + .html 26854B (2026-05); both SES identities verified (andrew@opalinvest.com + opalinvest.dev = Success); orchestrator Lambda Errors=0 (email send no-throw to verified recipient); box self-stopped (finally). Caught+fixed 3 latent bugs pre-fire: stray-key crash (delete+DE guard ba57d9b12), instance-replace drift (ignore_changes), chromium full-chrome hang (headless-shell symlink, probe-proven). | CLOSED 20260625T233159Z |

## Log

- 20260625T222433Z OPENED by 0.5.0_AE_OpalETL with 4 leg(s)
- 20260625T222511Z LEG artifact closed: aws s3 ls s3://opal-313476888478-lambda-artifacts/ec2/etfs-reports/ -> render_month_end.py 32020 bytes 2026-06-25 18:24:
- 20260625T222559Z LEG git closed: ed506fbd3 committed (TF root + orchestrator Lambda + source-map + ledger; EC2_MANIFEST handed to 0.7.0)
- 20260625T222948Z LEG tf-apply closed: safe-apply: Apply complete 16 added 0 changed 0 destroyed; reporter i-070477bf35fc54409, orchestrator Lambda + 2 schedul
- 20260625T233159Z LEG verify closed: 4th orchestrator {mode:run}: SSM render Success rc=0, S3 has etf_ownership.pdf 189054B + .html 26854B (2026-05); both SE
- 20260625T233200Z CLOSED -- all 4 legs proven
