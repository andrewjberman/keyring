# Deploy Completion Record
**Date opened:** 2026-10-05T02:14:31.388486+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261005T022347Z
**Deploy:** NFRA_OPLGTW OG-rl-6: opal-gateway app release 4b6b823fae -> rel-nfra-oplgtw-r17 e91819e281 (OG-q-7: dim_asset downloads open held-only under C3) via safe-ec2-deploy.sh from /c/tmp/og-rel11; never-widen COO 1a21759226 CTO de3381d39f (no condition) CVO 9c7fa957a3 (R1-R2) SIGNED
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~15
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| upload | s3-prefix | opal-gateway-latest.tar.gz and opal-gateway-<release sha>.tar.gz in the gateway artifact bucket | deploy wrapper output line with git-ref <release sha>; base guard declared 4b6b823fae == live at both reads | uploaded s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-e91819e281.tar.gz (+ latest), both git-ref e91819e2819df8c8df5708bc66e4f4273bb1a834 ETag 69bd2701 480201 bytes (head-object 02:20Z); base guard declared 4b6b823fae == live ref at the early and immediately-before-upload reads; rl6_phaseB_deploy.out | CLOSED 20261005T022336Z |
| install-verify | ec2-baked-asset | opal-gateway host /opt/opal-gateway running path + .env 50 keys | rl6_verify.sh after: md5 94 of 94 = release bytes, health 200, 65 tools, 50 key names unchanged, download OK held-only with discriminator, empty-holdings refusal, query equal; rl4.AC1 ht.AC2 | deploy Success ssm:9c785d4b-20fb-41c8-adfd-25017cba93c2 rc=0 02:17Z; rl6_verify.sh after VERIFY PASS 12 of 12 (host read ssm:7a15cb94, AFTER run ssm:4a88837c): health 200, md5 94 of 94 == release, tools 65 to 65, env 50 names = before, download BEFORE REFUSED AFTER OK 49 returned 0 unheld held 49 < asset universe 2160, empty-holdings REFUSED asset_read_denied_unqualified, query held set == download held set, grants_written 0 state_store_written false; rl4.AC1 4 of 4 PASS; ht.AC2 4 of 4 PASS; rl6_phaseB_verify_after.out, RL6_DOWNLOAD.json | CLOSED 20261005T022336Z |
| manifest | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway deployed_commit <release sha> previous 4b6b823fae | committed hash | EC2_MANIFEST opal-gateway deployed_commit e91819e281 previous_deployed_commit 4b6b823fae deployed_at 2026-10-05T02:17:58Z (the wrapper Time line), hand edit on wk-NFRA_OPLGTW-15-r17 committed 37bd6ea0ad; wrapper release-branch commit 59cc25a023 not merged | CLOSED 20261005T022336Z |
| rollback-proven | verify | rollback tree /c/tmp/og-rb11 at 4b6b823fae equal to the live artifact, command recorded | diff 94 of 94 equal (PHASE A) and verify PASS, or rolled back and re-verified | rollback tree /c/tmp/og-rb11 at 4b6b823fae (HEAD re-read 02:2xZ, clean) 94 of 94 equal to S3 opal-gateway-4b6b823fae.tar.gz (rl6_cmp_rollback.out at PHASE A); S3 head-object re-read 02:20Z: key present, ETag d68dd6f7, 479686 bytes, git-ref 4b6b823fae; command DEPLOY_BASE_REF=e91819e2819df8c8df5708bc66e4f4273bb1a834 HALT_ACK=1 from /c/tmp/og-rb11; not executed, not needed: VERIFY PASS 12 of 12 | CLOSED 20261005T022336Z |

## Log

- 20261005T021431Z OPENED by 0.9.0_WK_NFRA_OPLGTW~15 with 4 leg(s)
- 20261005T022336Z LEG upload closed: uploaded s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-e91819e281.tar.gz (+ latest), both git-re
- 20261005T022336Z LEG install-verify closed: deploy Success ssm:9c785d4b-20fb-41c8-adfd-25017cba93c2 rc=0 02:17Z; rl6_verify.sh after VERIFY PASS 12 of 12 (host read
- 20261005T022336Z LEG manifest closed: EC2_MANIFEST opal-gateway deployed_commit e91819e281 previous_deployed_commit 4b6b823fae deployed_at 2026-10-05T02:17:58
- 20261005T022336Z LEG rollback-proven closed: rollback tree /c/tmp/og-rb11 at 4b6b823fae (HEAD re-read 02:2xZ, clean) 94 of 94 equal to S3 opal-gateway-4b6b823fae.tar
- 20261005T022347Z CLOSED -- all 4 legs proven
