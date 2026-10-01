# Deploy Completion Record
**Date opened:** 2026-10-01T10:38:58.641507+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-rl-1 TRNSPT-DEPS narrow gateway release (train slot 3) on live 2c0f84966d
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~15
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| secrets | activation | blackdiamond/cot/otp-gateway-token rotated (new value put, AWSPREVIOUS holds the old); gateway/transcripts/bearer, gateway/mail/bearer, gateway/principals/rosters present | describe-secret versions: AWSCURRENT + AWSPREVIOUS on cot; /otp/health old=401 new=200 |  | OPEN |
| upload | s3-prefix | opal-313476888478-lambda-artifacts ec2/opal-gateway/opal-gateway-<release sha>.tar.gz and -latest with git-ref=release sha | deploy's own upload success lines + head-object git-ref |  | OPEN |
| install_verify | ec2-baked-asset | i-07dccb1615503ac99 /opt/opal-gateway release daa56d81ac on live 2c0f84966d | SSM deploy Success + /health 200 + 91 files md5 == release + tools 60 -> 65 + ENABLED_INTEGRATIONS unchanged + .env 39 -> 46 keys + /ms/* as before + rl.AC1.sh ARMS 6 of 6 |  | OPEN |
| manifest | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway deployed_commit=release sha on wk-NFRA_OPLGTW-15-r8 | safe-commit hash + rl.AC2.sh PASS |  | OPEN |
| rollback_proven | verify | rollback tree /c/tmp/og-rb4 at 2c0f84966d with DEPLOY_BASE_REF=release sha (artifact 92 of 92 == live S3, built not uploaded; or executed if a verify fails) | rollback command named + artifact equality read |  | OPEN |

## Log

- 20261001T103858Z OPENED by 0.9.0_WK_NFRA_OPLGTW~15 with 5 leg(s)
