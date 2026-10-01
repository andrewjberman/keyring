# Deploy Completion Record
**Date opened:** 2026-10-01T18:46:25.229194+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-tr-1 Tax SMA workbook route narrow gateway release, capability ON (train slot 6) on live 0a1d9079c6
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~15
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| upload | s3-prefix | opal-313476888478-lambda-artifacts ec2/opal-gateway/opal-gateway-<release sha>.tar.gz and -latest with git-ref=release sha | deploy's own upload success lines + head-object git-ref |  | OPEN |
| install_verify | ec2-baked-asset | i-07dccb1615503ac99 /opt/opal-gateway release 3a7d6a7dc8 on live 0a1d9079c6 | SSM deploy Success + /health 200 + shipped md5 == release + tools 65 -> 65 + .env 46 -> 48 keys (+TAXSMA_WORKBOOK_BEARER, +TAXSMA_WORKBOOK_IDENTITY) + ENABLED_INTEGRATIONS unchanged + /ms/* and /hx/* as before + M1 arm (mail and transcripts bearers read 401 UNAUTHORIZED_CAPABILITY on the Tax route) + tr.AC1.sh TAX ARMS 4 of 4 |  | OPEN |
| manifest | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway deployed_commit=release sha on wk-NFRA_OPLGTW-15-r8 | safe-commit hash + tr.AC2.sh PASS |  | OPEN |
| rollback_proven | verify | rollback tree /c/tmp/og-rb6 at 0a1d9079c6 with DEPLOY_BASE_REF=release sha (artifact 95 of 95 == live S3, built not uploaded; or executed if a verify fails) | rollback command named + artifact equality read |  | OPEN |

## Log

- 20261001T184625Z OPENED by 0.9.0_WK_NFRA_OPLGTW~15 with 4 leg(s)
