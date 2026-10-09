# Deploy Completion Record
**Date opened:** 2026-10-09T06:57:04.155441+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261009T082829Z
**Deploy:** IRPT_DASHBD DB-b-78: apply the R37 activity-and-lot release to irpt-49f-reporting-gold-lambda -- signed against packet sha256 848dd8640688c28cb62ffab109c4d55ea4e5348bc5286400a824d8e1405fd40b (COO half, CTO half GIVEN); artifact built sha256 ciTGx5UVE3BJ4mMgwlzSYCDpYBkvtefHbNlT2KCxh5Y= (MSTR msg 2680); targeted plan 0/3/0
**Authored by:** 0.9.0_WK_IRPT_DASHBD~55
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | 18 pins + 3 tf files restored to efeb21df71 + artifact upload (sha256 ciTGx5UVE3BJ4mMgwlzSYCDpYBkvtefHbNlT2KCxh5Y=) + targeted plan | Plan: 0 to add, 3 to change, 0 to destroy | 18 pins set + re-read (all sha256 equal, c0afa6f55e on origin/CLOUD) in lambda-source-map.json @86cf34a68d; artifact uploaded version pPnoTZs86qlqo2waxfP4h2ogXwq3hoR5 (prior latest HJZgXM5o8nsaP1ED.7K_OJ2cCuD_RrMX) sha256 ciTGx5UVE3BJ4mMgwlzSYCDpYBkvtefHbNlT2KCxh5Y=; iam.tf locals.tf lambda.tf restored to efeb21df71 bytes sha256 2c0ed377/5fe82384/9ae18719 = packet; targeted terraform plan -out: Plan: 0 to add, 3 to change, 0 to destroy; anchor CodeSha256 Mex71Y5g re-read live before | CLOSED 20261009T070123Z |
| D1 | activation | safe-apply of the saved plan, infra/aws/terraform/investor-reporting/reporting-gold | Apply complete, 3 changed | HALT_ACK-free SAFE_APPLY_TERRAFORM=main terraform.exe .tools/safe-apply.sh -chdir=infra/aws/terraform/investor-reporting/reporting-gold apply r37.tfplan, 2026-10-09 07:03Z: Apply complete! Resources: 0 added, 3 changed, 0 destroyed. | CLOSED 20261009T070452Z |
| V1 | verify | readback CodeSha256 + source map record + population dry_run | CodeSha256 = source map, dry_run under 1740.8 MB and 765 s, 0 objects written | get-function-configuration CodeSha256 ciTGx5UVE3BJ4mMgwlzSYCDpYBkvtefHbNlT2KCxh5Y= = source map deployed_code_sha256 @54713f105d (anchor Mex71Y5g differs); population dry_run date=2026-10-07 RequestId 07de1f15-d5d2-4175-9107-42ec114ac0d0 7604 accounts lots rows 569121 (realized 3245 unrealized 565876) REPORT Duration 334666.89 ms Max Memory Used 1632 MB of 2048 (under 765000 ms and 1740.8 MB), 0 objects written (returns 1132/1132; four new prefixes 0/0) | CLOSED 20261009T071425Z |
| A1 | verify | first fire A1-A7 incl A4 DELTA=0 and A7 18 member hashes | fire request id + A1..A7 read | first fire (ad-hoc population backfill of 2026-10-07 by the issuer's ruling, RequestId fe78f9ad-2bb7-4b51-b7be-46be579745c8, after the {} fire a692669c found 2026-10-08 SOURCE_LAG): A1 0 CLASS_SKIPPED 0 LOTS_SKIPPED all LANDED, Duration 343501.19 ms Max Memory 1652 MB; A2 identity within allowance; A3 keys equal; A4 returns data.parquet sha256 eb3e2627 byte-equal before/after, 20-account local delta 0; A5 grant five gold PutObject prefixes + GetItem only; A6 class identity 6681/6681 within 1e-9; A7 18 of 18 zip member hashes = pins table. Scheduled 11:41Z fire stays the organic acceptance | CLOSED 20261009T082828Z |

## Log

- 20261009T065704Z OPENED by 0.9.0_WK_IRPT_DASHBD~55 with 4 leg(s)
- 20261009T070123Z LEG P1 closed: 18 pins set + re-read (all sha256 equal, c0afa6f55e on origin/CLOUD) in lambda-source-map.json @86cf34a68d; artifact upl
- 20261009T070452Z LEG D1 closed: HALT_ACK-free SAFE_APPLY_TERRAFORM=main terraform.exe .tools/safe-apply.sh -chdir=infra/aws/terraform/investor-reporting
- 20261009T071425Z LEG V1 closed: get-function-configuration CodeSha256 ciTGx5UVE3BJ4mMgwlzSYCDpYBkvtefHbNlT2KCxh5Y= = source map deployed_code_sha256 @54
- 20261009T082828Z LEG A1 closed: first fire (ad-hoc population backfill of 2026-10-07 by the issuer's ruling, RequestId fe78f9ad-2bb7-4b51-b7be-46be57974
- 20261009T082829Z CLOSED -- all 4 legs proven
