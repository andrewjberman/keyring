# Deploy Completion Record
**Date opened:** 2026-10-07T04:29:23.881834+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261007T044327Z
**Deploy:** NFRA_OPLGTW OG-rl-11 PHASE B: opal-gateway release 7d65a28db0 -> rel-nfra-oplgtw-r25 240ac2fe5a (OG-up-1 send split + status tool, 65->66 tools; NFRA_OPALAI OA-f-14 scoped consent 17->9; 5 shipped files, 3 source-only) via safe-ec2-deploy.sh from /c/tmp/og-rel20; never-widen COO 8a769f4b54 CTO 62a89fbf07 CVO a4a47a0ba6 SIGNED
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~28
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| upload | s3-prefix | opal-gateway-latest.tar.gz and opal-gateway-<release sha>.tar.gz in the gateway artifact bucket | deploy wrapper output line with git-ref <release sha>; base guard 7d65a28db0 == live | uploaded s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-240ac2fe5a.tar.gz (+ latest), both git-ref 240ac2fe5abde944f15358ab563cb4b2ab63f09f ETag ba8a5d0b 507381 bytes (head-object LastModified 2026-10-07T04:33:02Z/:04Z); base guard declared 7d65a28db0 == live ref at the early and immediately-before-upload reads; r25_phaseB_deploy.out; prior artifact opal-gateway-7d65a28db0.tar.gz still present ETag 8e2e4ef3 501673 bytes git-ref 7d65a28db0 | CLOSED 20261007T044326Z |
| install-verify | ec2-baked-asset | opal-gateway host /opt/opal-gateway running path + .env 51 keys | r25_verify.sh after: md5 97 of 97 = release bytes (5 differ from live), health 200, 66 tools, 51 names with every value sha256 equal, floor rl4.AC1 + ht.AC2 | deploy Success ssm:6893cb67-a659-4357-a868-3d71decbfdb1 04:33:31Z; r25_verify.sh after VERIFY PASS 5 of 5 (r25_phaseB_verify_after.out): health 200 MainPID 751051->758081, md5 97 of 97 == release (5 differ from live), tools 65 to 66 (+opal_data_refresh_status only), .env 51 names unchanged with 51 of 51 value sha256 equal; floor rl4.AC1 4 of 4 (RESULT PASS), ht.AC2 4 of 4 at 51 keys (RESULT PASS) | CLOSED 20261007T044326Z |
| installed-reads | verify | installed code on the host: status tool, scoped consent, portal login, real holder | RL11_SEND.json + RL11_SCOPES.json + RL11_FLOOR.json from the installed tree with host digests; scoped silent acquire OK, probes all 200, status tool OK, login OK, real holder returned=distinct=held 0 unheld; any miss rolls back | installed code (staged=False; integration md5 239f74db, identity_scope 314d8430, token_broker a99942f0): RL11_SEND.json ssm 5dc9f1f8 (status tool OK SUCCEEDED, 66 tools, max_inline_wait_s 22, RL11S_DIGEST 5fc98cff); RL11_SCOPES.json ssm b4f39973 (unscoped 17, scoped 9 subset, silent acquire OK, 9 of 9 probes 200, site resolve 200, RL11C_DIGEST 90272b3a); RL11_FLOOR.json (portal login OK ssm bbcbb99b; real holder 2150 = 2150 = 2150, 0 unheld on query and download ssm 6c47ffdc); grants_written 0; no rollback trigger fired; no /login, no confirm=True send, no /trigger; r25_phaseB_postdeploy.out | CLOSED 20261007T044326Z |
| manifest | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway deployed_commit <release sha> previous 7d65a28db0 | committed hash | EC2_MANIFEST opal-gateway deployed_commit 240ac2fe5a previous_deployed_commit 7d65a28db0 deployed_at 2026-10-07T04:33:31Z (the wrapper Time line), hand edit on wk-NFRA_OPLGTW-25-28 committed with this ledger close; the wrapper's own release-branch manifest commit failed its owned-paths lane check (deploy LANDED, edit left uncommitted in /c/tmp/og-rel20, not merged; row Z-W28-S8 expected) | CLOSED 20261007T044327Z |
| rollback-proven | verify | rollback tree /c/tmp/og-rb19 at 7d65a28db0 equal to the live artifact, command recorded | diff 96 of 96 equal and verify PASS, or rolled back and re-verified | rollback tree /c/tmp/og-rb19 at 7d65a28db0 (HEAD and git status clean re-read 04:41Z) 96 of 96 equal to the live artifact (r25_cmp_rollback.out at PHASE A); host md5 re-read 96 of 96 at step 9 (ssm fe3364e3); S3 artifact opal-gateway-7d65a28db0.tar.gz present ETag 8e2e4ef3 git-ref 7d65a28db0; command DEPLOY_BASE_REF=240ac2fe5abde944f15358ab563cb4b2ab63f09f HALT_ACK=1 from /c/tmp/og-rb19; NOT executed: no verify failure, no rollback trigger | CLOSED 20261007T044327Z |

## Log

- 20261007T042923Z OPENED by 0.9.0_WK_NFRA_OPLGTW~28 with 5 leg(s)
- 20261007T044326Z LEG upload closed: uploaded s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-240ac2fe5a.tar.gz (+ latest), both git-re
- 20261007T044326Z LEG install-verify closed: deploy Success ssm:6893cb67-a659-4357-a868-3d71decbfdb1 04:33:31Z; r25_verify.sh after VERIFY PASS 5 of 5 (r25_phaseB_ve
- 20261007T044326Z LEG installed-reads closed: installed code (staged=False; integration md5 239f74db, identity_scope 314d8430, token_broker a99942f0): RL11_SEND.json 
- 20261007T044327Z LEG manifest closed: EC2_MANIFEST opal-gateway deployed_commit 240ac2fe5a previous_deployed_commit 7d65a28db0 deployed_at 2026-10-07T04:33:31
- 20261007T044327Z LEG rollback-proven closed: rollback tree /c/tmp/og-rb19 at 7d65a28db0 (HEAD and git status clean re-read 04:41Z) 96 of 96 equal to the live artifac
- 20261007T044327Z CLOSED -- all 5 legs proven
