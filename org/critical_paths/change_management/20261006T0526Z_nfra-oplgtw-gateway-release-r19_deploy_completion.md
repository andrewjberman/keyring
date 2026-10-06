# Deploy Completion Record
**Date opened:** 2026-10-06T05:26:21.962969+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261006T054208Z
**Deploy:** NFRA_OPLGTW OG-rl-7 A1 PHASE B+D: opal-gateway app release 37be3485db -> rel-nfra-oplgtw-r19b cf4b036e62 (R22: OA-e-10 NOT carried; 2 behaviour files: admin_refusals.py sender fields from entry args only, envelope.py docstring-only; server.py byte-equal to live so /login unchanged; 21 gateway files) via safe-ec2-deploy.sh from /c/tmp/og-rel15; never-widen COO 0e93179a50 CTO add7a9166f (no condition) CVO e79b976d9b (V1-V3) SIGNED
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~15
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| upload | s3-prefix | opal-gateway-latest.tar.gz and opal-gateway-<release sha>.tar.gz in the gateway artifact bucket | deploy wrapper output line with git-ref <release sha>; base guard declared 37be3485db == live at both reads | uploaded s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-cf4b036e62.tar.gz (+ latest), both git-ref cf4b036e62b5074600086e1d670dc3c6bdab004f ETag 49668365 498101 bytes (head-object 05:3xZ, latest LastModified 2026-10-06T05:31:04Z); base guard declared 37be3485db == live ref at the early and immediately-before-upload reads; r19b_phaseB_deploy.out; prior artifact opal-gateway-37be3485db.tar.gz still present ETag 4f2054e2 497941 bytes git-ref 37be3485db | CLOSED 20261006T054207Z |
| install-verify | ec2-baked-asset | opal-gateway host /opt/opal-gateway running path + .env 51 keys | r19b_verify.sh after: md5 96 of 96 = release bytes, health 200, 65 tools, 51 names with every value sha256 equal, sender arm AS_GIVEN/NULL, /login host-local before == after (no identity; synthetic verified identity), floor rl4.AC1 + ht.AC2 | deploy Success ssm:d5522c68-1282-4110-9d27-0cdd2e3727b5 05:31Z; r19b_verify.sh after host+AFTER checks 7 of 7 PASS (r19b_phaseB_verify_after.out; ssm 52733cab): health 200 MainPID 685344->711489, md5 96 of 96 == release, tools 65 to 65, .env 51 names unchanged with 51 of 51 value sha256 equal, sender arm on the installed code AS_GIVEN/NULL/other-tool None (3 of 3), scratch removed; CVO V2 /login host-local record BEFORE (ssm ae30d826) == AFTER, 12 LOGIN_REC arms and installed server.py md5 b13b1e54 equal; floor rl4.AC1 4 of 4 (ssm 90031012, b80a85e7), ht.AC2 4 of 4 at 51 keys (ssm 03783435) | CLOSED 20261006T054207Z |
| manifest | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway deployed_commit <release sha> previous 37be3485db | committed hash | EC2_MANIFEST opal-gateway deployed_commit cf4b036e62 previous_deployed_commit 37be3485db deployed_at 2026-10-06T05:31:52Z (the wrapper Time line), hand edit on wk-NFRA_OPLGTW-15-r19 committed f28efba900; wrapper release-branch commit 23e942ea37 not merged | CLOSED 20261006T054207Z |
| rollback-proven | verify | rollback tree /c/tmp/og-rb14 at 37be3485db equal to the live artifact, command recorded | diff 96 of 96 equal and verify PASS, or rolled back and re-verified | rollback tree /c/tmp/og-rb14 at 37be3485db (HEAD and clean re-read 05:2xZ) 96 of 96 equal to the host-read md5 list == live artifact (r19b_cmp_rollback.out at PHASE A2, re-compared at step 9); S3 artifact opal-gateway-37be3485db.tar.gz present ETag 4f2054e2 497941 bytes git-ref 37be3485db; command DEPLOY_BASE_REF=cf4b036e62b5074600086e1d670dc3c6bdab004f HALT_ACK=1 from /c/tmp/og-rb14; NOT executed: no verify failure, no roll-back | CLOSED 20261006T054207Z |
| drain-back | git | R16 drain-back: git diff <deployed> CLOUD -- infra/aws/ec2/opal-gateway empty; LINEAGE_R18 CLOUD-only list updated | recorded diff output | r19b_phaseD_drainback.out: git diff --stat cf4b036e62 CLOUD(471b596e23) -- infra/aws/ec2/opal-gateway EMPTY (0 files; gateway tree object 06b952d55f both); before the act 21 files +1097/-68; no merge needed; LINEAGE_R18.json 16 shipped items removed to r19b_shipped, 2 REVERTED_PENDING_RECUT records remain, committed f28efba900 | CLOSED 20261006T054207Z |

## Log

- 20261006T052621Z OPENED by 0.9.0_WK_NFRA_OPLGTW~15 with 5 leg(s)
- 20261006T054207Z LEG upload closed: uploaded s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-cf4b036e62.tar.gz (+ latest), both git-re
- 20261006T054207Z LEG install-verify closed: deploy Success ssm:d5522c68-1282-4110-9d27-0cdd2e3727b5 05:31Z; r19b_verify.sh after host+AFTER checks 7 of 7 PASS (r19b
- 20261006T054207Z LEG manifest closed: EC2_MANIFEST opal-gateway deployed_commit cf4b036e62 previous_deployed_commit 37be3485db deployed_at 2026-10-06T05:31:52
- 20261006T054207Z LEG rollback-proven closed: rollback tree /c/tmp/og-rb14 at 37be3485db (HEAD and clean re-read 05:2xZ) 96 of 96 equal to the host-read md5 list == l
- 20261006T054207Z LEG drain-back closed: r19b_phaseD_drainback.out: git diff --stat cf4b036e62 CLOUD(471b596e23) -- infra/aws/ec2/opal-gateway EMPTY (0 files; ga
- 20261006T054208Z CLOSED -- all 5 legs proven
