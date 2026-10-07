# Deploy Completion Record
**Date opened:** 2026-10-06T23:54:51.931165+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261007T000440Z
**Deploy:** NFRA_OPLGTW OG-rl-10 PHASE B: opal-gateway HOTFIX release 2c27f3a795 -> rel-nfra-oplgtw-r24 9d3e2eb3fc (CTO R32: the opal_portal service login moves from the raw API Gateway host to the front door www.opalinvest.dev; ONE shipped file app/integrations/opal_portal/integration.py, +6/-6) via safe-ec2-deploy.sh from /c/tmp/og-rel18; never-widen COO 86dae82982 CTO d274986e8d CVO 49470c5691 SIGNED
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~28
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| upload | s3-prefix | opal-gateway-latest.tar.gz and opal-gateway-<release sha>.tar.gz in the gateway artifact bucket | deploy wrapper output line with git-ref <release sha>; base guard declared 2c27f3a795 == live at both reads | uploaded s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-9d3e2eb3fc.tar.gz (+ latest), both git-ref 9d3e2eb3fce3ceabbf06f6c1819451894291be05 ETag 102ef89c 501049 bytes (head-object 00:0xZ, LastModified 2026-10-06T23:59:27Z/:29Z); base guard declared 2c27f3a795 == live ref at the early and immediately-before-upload reads; r24_phaseB_deploy.out; prior artifact opal-gateway-2c27f3a795.tar.gz still present ETag fb2994ea 501084 bytes git-ref 2c27f3a795 | CLOSED 20261007T000440Z |
| install-verify | ec2-baked-asset | opal-gateway host /opt/opal-gateway running path + .env 51 keys | r24_verify.sh after: md5 96 of 96 = release bytes (1 differs from live: opal_portal/integration.py), health 200, 65 tools, 51 names with every value sha256 equal, installed integration is the release file and its login is OK through www.opalinvest.dev, floor rl4.AC1 + ht.AC2 | deploy Success ssm:659e1f35-6ac4-47bf-87cb-9aa91f1cf44b 23:59:57Z; r24_verify.sh after VERIFY PASS 7 of 7 (r24_phaseB_verify_after.out): health 200 MainPID 717079->746072, md5 96 of 96 == release (1 differs from live: opal_portal/integration.py f8d19990->cc08e21e), tools 65 to 65, .env 51 names unchanged with 51 of 51 value sha256 equal, installed integration md5 cc08e21e login OK auth host www.opalinvest.dev (separate host process), scratch removed; floor rl4.AC1 4 of 4 (RESULT PASS), ht.AC2 4 of 4 at 51 keys (RESULT PASS) | CLOSED 20261007T000440Z |
| installed-login | verify | installed opal_portal integration's own _PortalSession.token() on the host with the real service secret, in process | RL10_LOGIN.json body login OK auth_host www.opalinvest.dev installed_code true served_release <release sha> grants_written 0 and the host RL10_DIGEST; a login that is not OK rolls back | RL10_LOGIN.json (ssm 85fa53f0-e25f-487a-aa17-8603c0485e24, Success): installed code md5 cc08e21e staged=False, body login OK auth_host www.opalinvest.dev installed_code true served_release 9d3e2eb3fce3ceabbf06f6c1819451894291be05 grants_written 0; RL10_DIGEST 79f13138 in host output; no token, email or credential recorded; no upload or trigger route called | CLOSED 20261007T000440Z |
| manifest | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway deployed_commit <release sha> previous 2c27f3a795 | committed hash | EC2_MANIFEST opal-gateway deployed_commit 9d3e2eb3fc previous_deployed_commit 2c27f3a795 deployed_at 2026-10-06T23:59:57Z (the wrapper Time line), hand edit on wk-NFRA_OPLGTW-24-28 committed cba8c1e345; the wrapper's own release-branch manifest commit failed its owned-paths lane check (deploy LANDED, edit left uncommitted in /c/tmp/og-rel18, not merged) | CLOSED 20261007T000440Z |
| rollback-proven | verify | rollback tree /c/tmp/og-rb17 at 2c27f3a795 equal to the live artifact, command recorded | diff 96 of 96 equal and verify PASS, or rolled back and re-verified | rollback tree /c/tmp/og-rb17 at 2c27f3a795 (HEAD and git status clean re-read 23:5xZ) 96 of 96 equal to the live artifact (r24_cmp_rollback.out at PHASE A) and the host md5 re-read 96 of 96 at step 9 (ssm a4c1cc66); S3 artifact opal-gateway-2c27f3a795.tar.gz present ETag fb2994ea git-ref 2c27f3a795; command DEPLOY_BASE_REF=9d3e2eb3fce3ceabbf06f6c1819451894291be05 HALT_ACK=1 from /c/tmp/og-rb17; NOT executed: no verify failure, login OK, no roll-back | CLOSED 20261007T000440Z |

## Log

- 20261006T235451Z OPENED by 0.9.0_WK_NFRA_OPLGTW~28 with 5 leg(s)
- 20261007T000440Z LEG upload closed: uploaded s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-9d3e2eb3fc.tar.gz (+ latest), both git-re
- 20261007T000440Z LEG install-verify closed: deploy Success ssm:659e1f35-6ac4-47bf-87cb-9aa91f1cf44b 23:59:57Z; r24_verify.sh after VERIFY PASS 7 of 7 (r24_phaseB_ve
- 20261007T000440Z LEG installed-login closed: RL10_LOGIN.json (ssm 85fa53f0-e25f-487a-aa17-8603c0485e24, Success): installed code md5 cc08e21e staged=False, body logi
- 20261007T000440Z LEG manifest closed: EC2_MANIFEST opal-gateway deployed_commit 9d3e2eb3fc previous_deployed_commit 2c27f3a795 deployed_at 2026-10-06T23:59:57
- 20261007T000440Z LEG rollback-proven closed: rollback tree /c/tmp/og-rb17 at 2c27f3a795 (HEAD and git status clean re-read 23:5xZ) 96 of 96 equal to the live artifac
- 20261007T000440Z CLOSED -- all 5 legs proven
