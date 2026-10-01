# Deploy Completion Record
**Date opened:** 2026-10-01T15:31:57.241739+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261001T155012Z
**Deploy:** NFRA_OPLGTW OG-rl-2 /hx/mail LISTING narrow gateway release (train slot 5) on live e3567ce5f7
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~15
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| upload | s3-prefix | opal-313476888478-lambda-artifacts ec2/opal-gateway/opal-gateway-<release sha>.tar.gz and -latest with git-ref=release sha | deploy's own upload success lines + head-object git-ref | deploy log: INFO uploaded s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-0a1d9079c6.tar.gz (+ latest); base guard equal e3567ce5f7 at the early and immediately-before-upload reads; head-object on -latest: git-ref 0a1d9079c682c640e619612f804257681c5db357, ETag 6201fccf, 463612 bytes, LastModified 2026-10-01T15:33:58Z; prior object opal-gateway-e3567ce5f7.tar.gz intact (ETag 9b440e69, 460595 bytes) | CLOSED 20261001T155010Z |
| install_verify | ec2-baked-asset | i-07dccb1615503ac99 /opt/opal-gateway release 0a1d9079c6 on live e3567ce5f7 | SSM deploy Success + /health 200 + shipped md5 == release + tools 65 -> 65 + ENABLED_INTEGRATIONS and .env key set unchanged (46) + MAIL_SENDER_TABLE count 3 and L1 set hash MATCH + /ms/* and by-id /hx/* as before + rl2.AC1.sh LIST ARMS 9 of 9 | deploy SSM 747cc4ba-c5ff-4a4f-8851-546883a6ef1d Success (OK MAIL_SENDER_TABLE read host-side from the shipped deploy/mail_sender_table.txt (3 entries); OK opal-gateway active; /health ok; /mcp unauth 401); verify SSM a25dbdb3-82e3-44c7-bb04-82e8998c2c25 at 15:37:31Z (about 3 min after the restart, row Z-W15-S18) and 49fa771c-7556-4a53-a615-6ef5ae01d2ba at 15:38:25Z: /health 200; 92 of 92 shipped files md5 == release bytes (0 NOT-OK); tools 65 -> 65, name list byte-equal to BEFORE; ENABLED_INTEGRATIONS unchanged (7 ids); .env 46 -> 46 keys same set; MAIL_SENDER_TABLE 3 items, L1 set hash MATCH (process env and shipped file, host-side, never printed); /ms/* 401/401/200/401/401 and by-id /hx/* 401/401 as before, listing route 404 -> 401; rl2.AC1.sh LIST ARMS 9 of 9 RESULT: PASS exit=0 (15:38:53Z) | CLOSED 20261001T155011Z |
| manifest | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway deployed_commit=release sha on wk-NFRA_OPLGTW-15-r8 | safe-commit hash + rl2.AC2.sh PASS | safe-commit 1686678d5080ba16be4f7ce0657ffb1965327b26 on wk-NFRA_OPLGTW-15-r8: EC2_MANIFEST.json services.opal-gateway deployed_commit=0a1d9079c682c640e619612f804257681c5db357 previous=e3567ce5f788f45195bec065f4d2fc5a68a38cd3 deployed_at 2026-10-01T15:34:29Z deployed_by 0.9.0_WK_NFRA_OPLGTW~15; rl2.AC2.sh PASS read after this ledger close | CLOSED 20261001T155011Z |
| rollback_proven | verify | rollback tree /c/tmp/og-rb5 at e3567ce5f7 with DEPLOY_BASE_REF=release sha and OG_MAIL_SENDER_TABLE from criterion.py (artifact 94 of 94 == live S3, built not uploaded; or executed if a verify fails) | rollback command named + artifact equality read | no rollback was needed (every verify, L1 and AC1 passed). Rollback tree /c/tmp/og-rb5 at e3567ce5f788f45195bec065f4d2fc5a68a38cd3 (clean, mcportal a3bff71ffa); the prior S3 object opal-gateway-e3567ce5f7.tar.gz is intact (ETag 9b440e69, 460595 bytes) and its 94 files equal the og-rb5 built tree file by file (diff -rq empty, 94 of 94, re-read after the release). Re-deploy command: cd /c/tmp/og-rb5 && OG_MAIL_SENDER_TABLE=<from criterion.DEFAULT_AUTHORS, shell only> DEPLOY_BASE_REF=0a1d9079c682c640e619612f804257681c5db357 HALT_ACK=1 AGENT_NAME=0.9.0_WK_NFRA_OPLGTW~15 bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh | CLOSED 20261001T155012Z |

## Log

- 20261001T153157Z OPENED by 0.9.0_WK_NFRA_OPLGTW~15 with 4 leg(s)
- 20261001T155010Z LEG upload closed: deploy log: INFO uploaded s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-0a1d9079c6.tar.gz (+ lat
- 20261001T155011Z LEG install_verify closed: deploy SSM 747cc4ba-c5ff-4a4f-8851-546883a6ef1d Success (OK MAIL_SENDER_TABLE read host-side from the shipped deploy/mai
- 20261001T155011Z LEG manifest closed: safe-commit 1686678d5080ba16be4f7ce0657ffb1965327b26 on wk-NFRA_OPLGTW-15-r8: EC2_MANIFEST.json services.opal-gateway de
- 20261001T155012Z LEG rollback_proven closed: no rollback was needed (every verify, L1 and AC1 passed). Rollback tree /c/tmp/og-rb5 at e3567ce5f788f45195bec065f4d2fc5
- 20261001T155012Z CLOSED -- all 4 legs proven
