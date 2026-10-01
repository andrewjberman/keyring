# Deploy Completion Record
**Date opened:** 2026-10-01T10:38:58.641507+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261001T105017Z
**Deploy:** NFRA_OPLGTW OG-rl-1 TRNSPT-DEPS narrow gateway release (train slot 3) on live 2c0f84966d
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~15
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| secrets | activation | blackdiamond/cot/otp-gateway-token rotated (new value put, AWSPREVIOUS holds the old); gateway/transcripts/bearer, gateway/mail/bearer, gateway/principals/rosters present | describe-secret versions: AWSCURRENT + AWSPREVIOUS on cot; /otp/health old=401 new=200 | K1 MASTER_ADMIN_PRINCIPALS MATCH + WRITE_CAPABLE_PRINCIPALS MATCH (sha256, host-side, before the put); cot otp-gateway-token put 2026-10-01T10:42:59Z: new VersionId 80ab5930 AWSCURRENT, old f5210e57 AWSPREVIOUS (describe-secret); gateway/transcripts/bearer, gateway/mail/bearer, gateway/principals/rosters present (host read them: deploy printed OK principal rosters read host-side and valid, master_admin 1 pair, write_capable 1 pairs); on /otp/health AWSPREVIOUS 401, AWSCURRENT 200 (SSM 636356a3) | CLOSED 20261001T105016Z |
| upload | s3-prefix | opal-313476888478-lambda-artifacts ec2/opal-gateway/opal-gateway-<release sha>.tar.gz and -latest with git-ref=release sha | deploy's own upload success lines + head-object git-ref | deploy log: uploaded s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-daa56d81ac.tar.gz (+ latest); head-object on -latest: git-ref daa56d81ac7c91795f1a9c47b2c2430cb3879e24, ETag b78383f9, 457214 bytes, LastModified 2026-10-01T10:43:27Z; base guard equal 2c0f84966d at early and immediately-before-upload reads; prior object opal-gateway-2c0f84966d.tar.gz intact (ETag c3b1e02e, 444479 bytes) | CLOSED 20261001T105016Z |
| install_verify | ec2-baked-asset | i-07dccb1615503ac99 /opt/opal-gateway release daa56d81ac on live 2c0f84966d | SSM deploy Success + /health 200 + 91 files md5 == release + tools 60 -> 65 + ENABLED_INTEGRATIONS unchanged + .env 39 -> 46 keys + /ms/* as before + rl.AC1.sh ARMS 6 of 6 | deploy SSM e6f13c38-88b1-4977-ac8c-35686a02826e Success (OK: opal-gateway active, /health ok, /mcp unauth 401); verify SSM 636356a3-1ad5-4814-b002-54a91862c716 Success at 10:44:50Z (32 s after deploy end): /health 200; 91 of 91 shipped files md5 == release bytes (0 NOT-OK); tools 60 -> 65, added find_online_meeting inspect_email_attachment list_email_filtered list_meeting_transcripts read_meeting_transcript, removed none; ENABLED_INTEGRATIONS unchanged (7 ids); .env keys 39 -> 46, added TRANSCRIPT_BEARER TRANSCRIPT_BEARER_LABELS TRANSCRIPT_MEETING_ALLOWLIST MAIL_BEARER MAIL_BEARER_LABELS MAIL_SENDER_TABLE MAIL_PDF_MAX_BYTES, removed none; /ms/* 401/401/200/401/401 same as before; rl.AC1.sh ARMS 6 of 6 refused-or-metadata RESULT: PASS exit=0 (10:45:51Z) | CLOSED 20261001T105016Z |
| manifest | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway deployed_commit=release sha on wk-NFRA_OPLGTW-15-r8 | safe-commit hash + rl.AC2.sh PASS | safe-commit 05ca371e006a1cb3e65852c886a1b05c8d54c2cb on wk-NFRA_OPLGTW-15-r8: EC2_MANIFEST.json services.opal-gateway deployed_commit=daa56d81ac7c91795f1a9c47b2c2430cb3879e24 previous=2c0f84966dc452d367ab1e4fc5d4849f08c1625e deployed_at 2026-10-01T10:43:56Z deployed_by 0.9.0_WK_NFRA_OPLGTW~15 | CLOSED 20261001T105017Z |
| rollback_proven | verify | rollback tree /c/tmp/og-rb4 at 2c0f84966d with DEPLOY_BASE_REF=release sha (artifact 92 of 92 == live S3, built not uploaded; or executed if a verify fails) | rollback command named + artifact equality read | no rollback was needed (every verify and AC1 passed). Rollback tree /c/tmp/og-rb4 at 2c0f84966d (mcportal a3bff71ffa); the prior S3 object opal-gateway-2c0f84966d.tar.gz is intact (ETag c3b1e02e, 444479 bytes) and its 89 non-dashboard files equal the og-rb4 tree file by file (0 differ; 92 files incl. dashboard, built-vs-live identical 92 of 92 at PHASE A). Re-deploy command: cd /c/tmp/og-rb4 && OG_MASTER_ADMIN_PRINCIPALS=<shell only> OG_WRITE_CAPABLE_PRINCIPALS=<shell only> DEPLOY_BASE_REF=daa56d81ac7c91795f1a9c47b2c2430cb3879e24 HALT_ACK=1 bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh | CLOSED 20261001T105017Z |

## Log

- 20261001T103858Z OPENED by 0.9.0_WK_NFRA_OPLGTW~15 with 5 leg(s)
- 20261001T105016Z LEG secrets closed: K1 MASTER_ADMIN_PRINCIPALS MATCH + WRITE_CAPABLE_PRINCIPALS MATCH (sha256, host-side, before the put); cot otp-gateway-t
- 20261001T105016Z LEG upload closed: deploy log: uploaded s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-daa56d81ac.tar.gz (+ latest);
- 20261001T105016Z LEG install_verify closed: deploy SSM e6f13c38-88b1-4977-ac8c-35686a02826e Success (OK: opal-gateway active, /health ok, /mcp unauth 401); verify S
- 20261001T105017Z LEG manifest closed: safe-commit 05ca371e006a1cb3e65852c886a1b05c8d54c2cb on wk-NFRA_OPLGTW-15-r8: EC2_MANIFEST.json services.opal-gateway de
- 20261001T105017Z LEG rollback_proven closed: no rollback was needed (every verify and AC1 passed). Rollback tree /c/tmp/og-rb4 at 2c0f84966d (mcportal a3bff71ffa); t
- 20261001T105017Z CLOSED -- all 5 legs proven
