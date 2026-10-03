# Deploy Completion Record
**Date opened:** 2026-10-03T16:44:49.163567+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261003T171809Z
**Deploy:** NFRA_OPLGTW OG-rl-4: opal-gateway app release 4231bd2ddc -> af2d762970 (audit fields, symmetric shared-value refusal, .env quoting, roster counts, Tax identity host-side) + rosters secret key taxsma_workbook_identity, via safe-ec2-deploy.sh from /c/tmp/og-rel9
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~15
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| secret-key | verify | Secrets Manager gateway/principals/rosters gains taxsma_workbook_identity (value sha256 == host TAXSMA_WORKBOOK_IDENTITY) | new version id; new key sha256 MATCH host; every pre-existing key value hash unchanged | rl4_secret_key.py apply 16:4xZ: put version e018dce9 (AWSCURRENT), AWSPREVIOUS 37ec284b == before; pre-existing keys value hash unchanged 2 of 2; keys 2 -> 3; new key sha256 == identity export MATCH; identity export sha256 == host TAXSMA_WORKBOOK_IDENTITY MATCH (SSM ac3ac6a1); rl4_step13.out | CLOSED 20261003T165030Z |
| upload | s3-prefix | opal-gateway-latest.tar.gz and opal-gateway-af2d762970.tar.gz in the gateway artifact bucket | deploy wrapper output line with git-ref af2d762970; base guard declared 4231bd2ddc == live at both reads | uploaded s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-af2d762970.tar.gz (+ latest), both git-ref af2d7629702528c050860314a7867d8ea0cecfbf ETag 6b5a9b8a... (head-object 16:5xZ); base guard declared 4231bd2ddc == live ref at early and immediately-before-upload reads; rl4_phaseB_deploy.log | CLOSED 20261003T165956Z |
| install-verify | ec2-baked-asset | opal-gateway host /opt/opal-gateway running path + .env 50 keys | rl4_verify.sh after: md5 94 of 94 = release bytes, health 200, 50 keys + 50 process value hashes unchanged, 3 own-bearer reads, rl4.AC1 tr.AC1 ht.AC2 | deploy Success ssm:ca339db1, rc=0; rl4_verify.sh after VERIFY PASS 10 of 10 (SSM 6b1527ed): health 200, md5 94 of 94 == release, tools 65 to 65, env 50 names = before, 50 of 50 process value hashes identical, mail 200, teams 200, transcripts 403 meeting_not_allowed (accepted); rl4.AC1 4 of 4 PASS; tr.AC1 3 of 4 (stale arm 4, row Z-W15-S31) graded yes-with-stale-arm-4; ht.AC2 4 of 4 PASS; rl4_phaseB_verify_after.log | CLOSED 20261003T165956Z |
| manifest | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway deployed_commit af2d762970 previous 4231bd2ddc | committed hash | EC2_MANIFEST opal-gateway deployed_commit af2d762970 previous_deployed_commit 4231bd2ddc deployed_at 2026-10-03T16:55:49Z (the wrapper Time line, rl4_phaseB_deploy.out), hand edit on wk-NFRA_OPLGTW-15-r14; manifest blob 75017775125c committed in this ledger-close commit (git rev-parse <commit>:infra/aws/ec2/EC2_MANIFEST.json == 75017775125c); wrapper release-branch commit 51b7b1463b not merged | CLOSED 20261003T171749Z |
| rollback-proven | verify | rollback tree /c/tmp/og-rb9 at 4231bd2ddc equal to the live artifact, command + identity export recorded | diff -rq 97 of 97 equal (PHASE A) and verify PASS, or rolled back and re-verified | rollback tree /c/tmp/og-rb9 at 4231bd2ddc (HEAD re-read 17:13Z, clean) diff -rq 97 of 97 equal to S3 opal-gateway-4231bd2ddc.tar.gz and opal-gateway-latest at PHASE A (ANNOUNCE_OG-rl-4.md step 9); S3 head-object re-read 2026-10-03T17:13:32Z: opal-gateway-4231bd2ddc.tar.gz present, ETag 90196691876349cd..., 478107 bytes, git-ref 4231bd2ddc6fd975304ed5a2c097473bdd5b41a5; command + identity export (IDENTITY_SHA256 MATCH) recorded in ANNOUNCE_OG-rl-4.md; not executed, not needed: VERIFY PASS 10 of 10, rl4.AC1 PASS, rl4.AC2 PASS 17:05Z | CLOSED 20261003T171749Z |

## Log

- 20261003T164449Z OPENED by 0.9.0_WK_NFRA_OPLGTW~15 with 5 leg(s)
- 20261003T165030Z LEG secret-key closed: rl4_secret_key.py apply 16:4xZ: put version e018dce9 (AWSCURRENT), AWSPREVIOUS 37ec284b == before; pre-existing keys val
- 20261003T165956Z LEG upload closed: uploaded s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-af2d762970.tar.gz (+ latest), both git-re
- 20261003T165956Z LEG install-verify closed: deploy Success ssm:ca339db1, rc=0; rl4_verify.sh after VERIFY PASS 10 of 10 (SSM 6b1527ed): health 200, md5 94 of 94 == 
- 20261003T171749Z LEG manifest closed: EC2_MANIFEST opal-gateway deployed_commit af2d762970 previous_deployed_commit 4231bd2ddc deployed_at 2026-10-03T16:55:49
- 20261003T171749Z LEG rollback-proven closed: rollback tree /c/tmp/og-rb9 at 4231bd2ddc (HEAD re-read 17:13Z, clean) diff -rq 97 of 97 equal to S3 opal-gateway-4231bd
- 20261003T171809Z CLOSED -- all 5 legs proven
