# Deploy Completion Record
**Date opened:** 2026-07-10T19:24:48.372261+00:00
**Status:** OPEN
**Deploy:** NFRA_WEBSITE W2: WP Contact-form transactional email via SES (scoped instance-role, noreply@opalinvest.dev)
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | iam.tf scoped ses:SendEmail/SendRawEmail (opalinvest.dev id + FromAddress cond) committed+pushed CLOUD | commit hash |  | OPEN |
| L2 | verify | comp-iam gaps + terraform 0-diff after safe-apply | plan output |  | OPEN |
| L3 | verify | IAM APPLIED: simulate-principal-policy ALLOW noreply@opalinvest.dev / DENY other from-addr / positive control | simulate output |  | OPEN |
| L4 | verify | box->SES exercise via instance role: send noreply@opalinvest.dev->andrew@ = MessageId + DKIM d=opalinvest.dev pass | MessageId + M365 header read |  | OPEN |
| L5 | activation | wp-mail-smtp AmazonSES configured on box (S3->box, no stored key) + WP wp_mail() test ->andrew@ delivers | SSM + M365 read |  | OPEN |

## Log

- 20260710T192448Z OPENED by 0.7.0_AE_CloudOps~A with 5 leg(s)
