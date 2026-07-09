# Deploy Completion Record
**Date opened:** 2026-06-26T14:28:56.243161+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260626T143158Z
**Deploy:** PIECE-2 Delta-2: cot-exporter-ec2-role GetSecretValue on blackdiamond/cot/otp-gateway-token (firm-sep Deny-bd intact)
**Authored by:** 0.6.0_AE_PartnerETL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit iam.tf Delta-2 | hash pushed | commit 9992f3523 pushed 0c715e034..9992f3523 CLOUD | CLOSED 20260626T143157Z |
| L2 | verify | terraform apply 0-diff on cot_exporter_policy | plan shows no changes post-apply | safe-apply: 0 added/1 changed/0 destroyed; post-apply plan = No changes (0-diff) | CLOSED 20260626T143158Z |
| L3 | verify | firm-sep belt intact: get-role-policy Deny-bd live + gateway-token read scoped to cot only | aws iam get-role-policy output | get-role-policy: DenyCrossFirmBuckets s3:* Deny on opal-data-bd+inf LIVE; CotOtpGatewayTokenRead = GetSecretValue on blackdiamond/cot/otp-gateway-token-* ONLY (read-only, cot-scoped, never 49f) | CLOSED 20260626T143158Z |

## Log

- 20260626T142856Z OPENED by 0.6.0_AE_PartnerETL with 3 leg(s)
- 20260626T143157Z LEG L1 closed: commit 9992f3523 pushed 0c715e034..9992f3523 CLOUD
- 20260626T143158Z LEG L2 closed: safe-apply: 0 added/1 changed/0 destroyed; post-apply plan = No changes (0-diff)
- 20260626T143158Z LEG L3 closed: get-role-policy: DenyCrossFirmBuckets s3:* Deny on opal-data-bd+inf LIVE; CotOtpGatewayTokenRead = GetSecretValue on bla
- 20260626T143158Z CLOSED -- all 3 legs proven
