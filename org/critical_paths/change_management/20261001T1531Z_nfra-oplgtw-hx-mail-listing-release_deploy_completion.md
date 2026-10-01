# Deploy Completion Record
**Date opened:** 2026-10-01T15:31:57.241739+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-rl-2 /hx/mail LISTING narrow gateway release (train slot 5) on live e3567ce5f7
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~15
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| upload | s3-prefix | opal-313476888478-lambda-artifacts ec2/opal-gateway/opal-gateway-<release sha>.tar.gz and -latest with git-ref=release sha | deploy's own upload success lines + head-object git-ref |  | OPEN |
| install_verify | ec2-baked-asset | i-07dccb1615503ac99 /opt/opal-gateway release 0a1d9079c6 on live e3567ce5f7 | SSM deploy Success + /health 200 + shipped md5 == release + tools 65 -> 65 + ENABLED_INTEGRATIONS and .env key set unchanged (46) + MAIL_SENDER_TABLE count 3 and L1 set hash MATCH + /ms/* and by-id /hx/* as before + rl2.AC1.sh LIST ARMS 9 of 9 |  | OPEN |
| manifest | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway deployed_commit=release sha on wk-NFRA_OPLGTW-15-r8 | safe-commit hash + rl2.AC2.sh PASS |  | OPEN |
| rollback_proven | verify | rollback tree /c/tmp/og-rb5 at e3567ce5f7 with DEPLOY_BASE_REF=release sha and OG_MAIL_SENDER_TABLE from criterion.py (artifact 94 of 94 == live S3, built not uploaded; or executed if a verify fails) | rollback command named + artifact equality read |  | OPEN |

## Log

- 20261001T153157Z OPENED by 0.9.0_WK_NFRA_OPLGTW~15 with 4 leg(s)
