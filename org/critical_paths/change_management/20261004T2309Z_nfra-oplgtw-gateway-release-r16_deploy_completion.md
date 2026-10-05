# Deploy Completion Record
**Date opened:** 2026-10-04T23:09:05.718802+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261004T231800Z
**Deploy:** NFRA_OPLGTW OG-rl-5: opal-gateway app release af2d762970 -> rel-nfra-oplgtw-r16 (R9 grain, R9a single-page fallback, dim_transaction data prefixes, query-path dim_asset guard deleted) via safe-ec2-deploy.sh from /c/tmp/og-rel10; never-widen COO a197f29422 CTO 75d651b7f4 (C1) CVO d370d16fe3 (Q1-Q3) SIGNED
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~15
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| upload | s3-prefix | opal-gateway-latest.tar.gz and opal-gateway-<release sha>.tar.gz in the gateway artifact bucket | deploy wrapper output line with git-ref <release sha>; base guard declared af2d762970 == live at both reads | uploaded s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-4b6b823fae.tar.gz (+ latest), both git-ref 4b6b823faec5288c714b70117fcd691239a2633f ETag d68dd6f7 479686 bytes (head-object 23:2xZ); base guard declared af2d762970 == live ref at the early and immediately-before-upload reads; rl5_phaseB_deploy.out | CLOSED 20261004T231740Z |
| install-verify | ec2-baked-asset | opal-gateway host /opt/opal-gateway running path + .env 50 keys | rl5_verify.sh after: md5 94 of 94 = release bytes, health 200, 65 tools, 50 key names unchanged, paging pages OK, census, held check, download control, census_after_other 14 per master, ungranted reads refused; rl4.AC1 ht.AC2 | deploy Success ssm:984ded12 rc=0 23:12Z; rl5_verify.sh after VERIFY PASS 15 of 15 (host read SSM 6d38ff36): health 200, md5 94 of 94 == release (incl. deploy contract), tools 65 to 65, env 50 names = before, dim_position rows page OK (161 matched), dim_asset rows page OK (49 returned, 0 unheld, held 49 < asset universe 2160), census servable 28+28 per master 0 lacking, dim_balance 14+14, dim_transaction 14+14, ungranted reads REFUSED, download REFUSED, grants_written 0; rl4.AC1 4 of 4 PASS; ht.AC2 4 of 4 PASS; rl5_phaseB_verify_after.out, RL5_PAGING.json | CLOSED 20261004T231740Z |
| manifest | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway deployed_commit <release sha> previous af2d762970 | committed hash | EC2_MANIFEST opal-gateway deployed_commit 4b6b823fae previous_deployed_commit af2d762970 deployed_at 2026-10-04T23:12:32Z (the wrapper Time line), hand edit on wk-NFRA_OPLGTW-15-r16 committed in the manifest commit of this order; wrapper release-branch commit e0b90e9945 not merged | CLOSED 20261004T231741Z |
| rollback-proven | verify | rollback tree /c/tmp/og-rb10 at af2d762970 equal to the live artifact, command recorded | diff 97 of 97 equal (PHASE A) and verify PASS, or rolled back and re-verified | rollback tree /c/tmp/og-rb10 at af2d762970 (HEAD re-read 23:2xZ, clean) 97 of 97 equal to S3 opal-gateway-af2d762970.tar.gz (rl5_cmp_rollback.out at PHASE A); S3 head-object re-read 23:2xZ: key present, ETag 6b5a9b8a, 478828 bytes, git-ref af2d762970; command DEPLOY_BASE_REF=4b6b823faec5288c714b70117fcd691239a2633f HALT_ACK=1 from /c/tmp/og-rb10 (nothing exported since OG-rl-4); not executed, not needed: VERIFY PASS 15 of 15 | CLOSED 20261004T231741Z |

## Log

- 20261004T230905Z OPENED by 0.9.0_WK_NFRA_OPLGTW~15 with 4 leg(s)
- 20261004T231740Z LEG upload closed: uploaded s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-4b6b823fae.tar.gz (+ latest), both git-re
- 20261004T231740Z LEG install-verify closed: deploy Success ssm:984ded12 rc=0 23:12Z; rl5_verify.sh after VERIFY PASS 15 of 15 (host read SSM 6d38ff36): health 200, 
- 20261004T231741Z LEG manifest closed: EC2_MANIFEST opal-gateway deployed_commit 4b6b823fae previous_deployed_commit af2d762970 deployed_at 2026-10-04T23:12:32
- 20261004T231741Z LEG rollback-proven closed: rollback tree /c/tmp/og-rb10 at af2d762970 (HEAD re-read 23:2xZ, clean) 97 of 97 equal to S3 opal-gateway-af2d762970.tar
- 20261004T231800Z CLOSED -- all 4 legs proven
