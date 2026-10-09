# Deploy Completion Record
**Date opened:** 2026-10-09T03:52:19.900727+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261009T043356Z
**Deploy:** IRPT_DASHBD DB-b-70: apply the R35 activity-and-lot release to irpt-49f-reporting-gold-lambda (class + activity + realized + unrealized tables; targeted plan 0/3/0)
**Authored by:** 0.9.0_WK_IRPT_DASHBD~47
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | pins 0-4 + artifact rebuild + targeted plan | Plan: 0 to add, 3 to change, 0 to destroy | pins 0-4 set in lambda-source-map.json @d5c11dc683 (sha256 = packet file list); build-and-upload.sh uploaded artifact version HC1vHWTvwhpnVW1UUBhr5SQBKp2gWOfu (prior latest FzE_mt1vdAU3Jy3VQuWIDbGVuf5Rrjjn) sha256 2/aW4wIhBB8rahfTX7/E6HOW/BVWNGDvmp4uY0+JpYQ= @67ffc44b6a; targeted terraform plan -out: Plan: 0 to add, 3 to change, 0 to destroy; silver bucket policy has no read restriction (W23-S1) | CLOSED 20261009T035830Z |
| D1 | activation | safe-apply of the saved plan, infra/aws/terraform/investor-reporting/reporting-gold | Apply complete, 3 changed | HALT_ACK-free .tools/safe-apply.sh -chdir=infra/aws/terraform/investor-reporting/reporting-gold apply of the saved plan, 2026-10-09 03:59Z: Apply complete! Resources: 0 added, 3 changed, 0 destroyed | CLOSED 20261009T040157Z |
| V1 | verify | readback CodeSha256 + source map record + dry_run | CodeSha256 = source map, dry_run under 85% of 900 s / 2048 MB, 0 objects written | get-function-configuration irpt-49f-reporting-gold-lambda CodeSha256 2/aW4wIhBB8rahfTX7/E6HOW/BVWNGDvmp4uY0+JpYQ= = source map deployed_code_sha256 @443bd67448 (anchor Mex71Y5g... differs); dry_run {dry_run:true} RequestId ef733674-6c4d-4f9f-b6e4-045778c0a185 REPORT Duration 29367.78 ms, Max Memory Used 304 MB of 2048, 0 objects written (gold prefixes before/after: returns 1132/1132, other four 0/0); caveat: 2026-10-08 SOURCE_LAG no balance partition so lots stage not exercised | CLOSED 20261009T040453Z |
| A1 | verify | first fire A1-A6 incl A4 DELTA=0 | fire request id + A1..A6 read | SUPERSEDED: release rolled back under AMENDMENT 2 (CTO ruling msg 2393) before any organic or ad-hoc first fire; no first fire was run, A1 to A6 not read; sizing condition 1 unmet (W47-S5) and four members at older pins (W47-S4) | CLOSED 20261009T043356Z |
| R1 | activation | AMENDMENT 2 rollback: artifact copy-object of the anchor version, Terraform root and source map restored, targeted plan 0/3/0, one safe-apply | Apply complete 3 changed; live CodeSha256 = Mex71Y5g...Z44=; role write statement = returns prefix only | AMENDMENT 2 rollback 2026-10-09: s3api copy-object of FzE_mt1vdAU3Jy3VQuWIDbGVuf5Rrjjn onto the key gave latest version HJZgXM5o8nsaP1ED.7K_OJ2cCuD_RrMX with content-sha256 Mex71Y5gk9RYE9q885knj3Ph12xV2Y9eVqMl3uJ1Z44= @0709c0a960 bfd71e73c9; targeted plan 0 to add, 3 to change, 0 to destroy; safe-apply: Apply complete! Resources: 0 added, 3 changed, 0 destroyed.; get-function-configuration CodeSha256 Mex71Y5gk9RYE9q885knj3Ph12xV2Y9eVqMl3uJ1Z44= (LastModified 2026-10-09T04:31:10Z); role policy write statement WriteTheAccountReturnDailyPrefixOnly = account_return_daily/* only; source map stamped @310380d8cd | CLOSED 20261009T043355Z |

## Log

- 20261009T035219Z OPENED by 0.9.0_WK_IRPT_DASHBD~47 with 4 leg(s)
- 20261009T035830Z LEG P1 closed: pins 0-4 set in lambda-source-map.json @d5c11dc683 (sha256 = packet file list); build-and-upload.sh uploaded artifact ve
- 20261009T040157Z LEG D1 closed: HALT_ACK-free .tools/safe-apply.sh -chdir=infra/aws/terraform/investor-reporting/reporting-gold apply of the saved plan,
- 20261009T040453Z LEG V1 closed: get-function-configuration irpt-49f-reporting-gold-lambda CodeSha256 2/aW4wIhBB8rahfTX7/E6HOW/BVWNGDvmp4uY0+JpYQ= = sour
- 20261009T04xxZ LEG R1 added by 0.9.0_WK_IRPT_DASHBD~47 (AMENDMENT 2 on CTO ruling msg 2393)
- 20261009T043355Z LEG R1 closed: AMENDMENT 2 rollback 2026-10-09: s3api copy-object of FzE_mt1vdAU3Jy3VQuWIDbGVuf5Rrjjn onto the key gave latest version 
- 20261009T043356Z LEG A1 closed: SUPERSEDED: release rolled back under AMENDMENT 2 (CTO ruling msg 2393) before any organic or ad-hoc first fire; no firs
- 20261009T043356Z CLOSED -- all 5 legs proven
