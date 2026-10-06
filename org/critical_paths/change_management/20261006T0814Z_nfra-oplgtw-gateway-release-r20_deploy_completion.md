# Deploy Completion Record
**Date opened:** 2026-10-06T08:14:05.193028+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261006T082527Z
**Deploy:** NFRA_OPLGTW OG-rl-8 PHASE B+D: opal-gateway app release cf4b036e62 -> rel-nfra-oplgtw-r20 2c27f3a795 (R24 as amended R25: /login tier admit backstop in login_admit_decision + gw_login audit record audit.log_login; engine.py RSS-poll ctypes reuse OG-fl-1; 3 shipped behaviour files server.py audit.py engine.py; 5-file commit incl 2 test files) via safe-ec2-deploy.sh from /c/tmp/og-rel16; never-widen COO 1eeeb17ff6 CTO c94393604a (no condition) CVO fcd7f4c457 (W1-W3) SIGNED
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~15
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| upload | s3-prefix | opal-gateway-latest.tar.gz and opal-gateway-<release sha>.tar.gz in the gateway artifact bucket | deploy wrapper output line with git-ref <release sha>; base guard declared cf4b036e62 == live at both reads | uploaded s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-2c27f3a795.tar.gz (+ latest), both git-ref 2c27f3a7958de0aa644374cdd08fc188a27e9e3f ETag fb2994ea 501084 bytes (head-object 08:2xZ, latest LastModified 2026-10-06T08:17:19Z); base guard declared cf4b036e62 == live ref at the early and immediately-before-upload reads; r20_phaseB_deploy.out; prior artifact opal-gateway-cf4b036e62.tar.gz still present ETag 49668365 498101 bytes git-ref cf4b036e62 | CLOSED 20261006T082526Z |
| install-verify | ec2-baked-asset | opal-gateway host /opt/opal-gateway running path + .env 51 keys | r20_verify.sh after: md5 96 of 96 = release bytes, health 200, 65 tools, 51 names with every value sha256 equal, /login arms 10 of 10 (CVO W2: non-restricted ADMITTED reason tier_graph_tools, restricted REFUSED, one gw_login per request, no address/token/state), engine RSS equal, floor rl4.AC1 + ht.AC2 | deploy Success ssm:1658e1c2-4346-4aae-96e5-63791aea96d3 08:17Z; r20_verify.sh after host+AFTER 8 of 8 PASS (r20_phaseB_verify_after.out; ssm 2f790a7e): health 200 MainPID 711489->717079, md5 96 of 96 == release, tools 65 to 65, .env 51 names unchanged with 51 of 51 value sha256 equal, /login arms 10 of 10 on the installed code (synthetic host-local, separate process): non-restricted ADMITTED reason tier_graph_tools, analyst identity ADMITTED, restricted REFUSED 403 deny_list, server-held ADMITTED, 8 gw_login records per 8 requests, no address/token/state; fail-closed tier arm REFUSED tier_unresolvable; engine RSS poll 3 of 3 (own poll 61.6 MiB == /proc); scratch removed; floor rl4.AC1 4 of 4 (ssm bc5f4148, 5ecb9caa), ht.AC2 4 of 4 at 51 keys (ssm 98f6c688) | CLOSED 20261006T082526Z |
| manifest | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway deployed_commit <release sha> previous cf4b036e62 | committed hash | EC2_MANIFEST opal-gateway deployed_commit 2c27f3a795 previous_deployed_commit cf4b036e62 deployed_at 2026-10-06T08:17:45Z (the wrapper Time line), hand edit on wk-NFRA_OPLGTW-15-r20 committed c67e5f236d; wrapper release-branch commit 3326bba6b1 not merged; file_checksums untouched (row S65) | CLOSED 20261006T082526Z |
| rollback-proven | verify | rollback tree /c/tmp/og-rb16 at cf4b036e62 equal to the live artifact, command recorded | diff 96 of 96 equal and verify PASS, or rolled back and re-verified | rollback tree /c/tmp/og-rb16 at cf4b036e62 (HEAD and clean re-read 08:1xZ) 96 of 96 equal to the host-read md5 list == live artifact (r20_cmp_rollback.out at PHASE A; live re-read 96 of 96 at step 9, ssm 6cd2bbba); S3 artifact opal-gateway-cf4b036e62.tar.gz present ETag 49668365 498101 bytes git-ref cf4b036e62; command DEPLOY_BASE_REF=2c27f3a7958de0aa644374cdd08fc188a27e9e3f HALT_ACK=1 from /c/tmp/og-rb16; NOT executed: no verify failure, no roll-back | CLOSED 20261006T082526Z |
| drain-back | git | R16 drain-back (CVO W3): git diff <deployed> CLOUD -- infra/aws/ec2/opal-gateway empty; LINEAGE_R18 CLOUD-only list updated | recorded diff output | r20_phaseD_drainback.out: git diff --stat cf4b036e62 CLOUD(2b26a3ca4a) before the act 5 files +620/-27; AFTER git diff 2c27f3a795 CLOUD -- infra/aws/ec2/opal-gateway EMPTY (0 files; gateway tree object 46e8445c36 both); no merge needed (CLOUD == release since f237f0b676); LINEAGE_R18 cloud_only_remaining 0, no r20 item listed, file outside order paths so not edited | CLOSED 20261006T082526Z |

## Log

- 20261006T081405Z OPENED by 0.9.0_WK_NFRA_OPLGTW~15 with 5 leg(s)
- 20261006T082526Z LEG upload closed: uploaded s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-2c27f3a795.tar.gz (+ latest), both git-re
- 20261006T082526Z LEG install-verify closed: deploy Success ssm:1658e1c2-4346-4aae-96e5-63791aea96d3 08:17Z; r20_verify.sh after host+AFTER 8 of 8 PASS (r20_phaseB_v
- 20261006T082526Z LEG manifest closed: EC2_MANIFEST opal-gateway deployed_commit 2c27f3a795 previous_deployed_commit cf4b036e62 deployed_at 2026-10-06T08:17:45
- 20261006T082526Z LEG rollback-proven closed: rollback tree /c/tmp/og-rb16 at cf4b036e62 (HEAD and clean re-read 08:1xZ) 96 of 96 equal to the host-read md5 list == l
- 20261006T082526Z LEG drain-back closed: r20_phaseD_drainback.out: git diff --stat cf4b036e62 CLOUD(2b26a3ca4a) before the act 5 files +620/-27; AFTER git diff 2
- 20261006T082527Z CLOSED -- all 5 legs proven
