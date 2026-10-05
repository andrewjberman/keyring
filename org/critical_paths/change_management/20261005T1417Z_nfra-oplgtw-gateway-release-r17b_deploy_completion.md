# Deploy Completion Record
**Date opened:** 2026-10-05T14:17:53.799140+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261005T153246Z
**Deploy:** NFRA_OPLGTW OG-rl-6 Phase C-B: opal-gateway app release e91819e281 -> rel-nfra-oplgtw-r17c 37be3485db (/yearinreview OWNER-ONLY behind its own fail-closed roster key YEARINREVIEW_VIEW_ALLOWED_EMAILS; .env 50 -> 51 names) via safe-ec2-deploy.sh from /c/tmp/og-rel13; never-widen COO f6fdd4047b CTO 86e34b783d (no condition) CVO 9c23533619 (T1-T2) SIGNED
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~15
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| upload | s3-prefix | opal-gateway-latest.tar.gz and opal-gateway-<release sha>.tar.gz in the gateway artifact bucket | deploy wrapper output line with git-ref <release sha>; base guard declared e91819e281 == live at both reads | uploaded s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-37be3485db.tar.gz (+ latest), both git-ref 37be3485db9a00522c55a260666f708336c918f3 ETag 4f2054e2 497941 bytes (head-object 15:3xZ); base guard declared e91819e281 == live ref at the early and immediately-before-upload reads; rl9_phaseB_deploy.out | CLOSED 20261005T153246Z |
| install-verify | ec2-baked-asset | opal-gateway host /opt/opal-gateway running path + .env 51 keys (50 + YEARINREVIEW_VIEW_ALLOWED_EMAILS) | rl7_verify.sh after: md5 96 of 96 = release bytes, health 200, 65 tools, 51 names with 50 prior value sha256 equal, new key digest = sha256(andrew@opalinvest.com), T2 arms on the deployed host (non-owner 403, owner 200, none 401, forged 401, empty/missing roster 403), host-local 401 x2, public 302, r17 download re-read; rl6.AC1 rl4.AC1(R17B baseline) ht.AC2 | deploy Success ssm:1af86a41-9355-4bb0-b470-d745c57046bf rc=0 14:22Z; rl7_verify.sh after host+AFTER checks 19 of 19 PASS (host read + AFTER ssm ids in rl9_phaseB_verify_after.out): health 200 MainPID 664116->685344, md5 96 of 96 == release, tools 65 to 65, .env 51 names = 50 + YEARINREVIEW_VIEW_ALLOWED_EMAILS, the 50 prior value sha256 equal 50 of 50, new-key digest == sha256(andrew@opalinvest.com); T2 arms ON THE DEPLOYED HOST (installed code, venv, separate process, test ES256 key swapped for the ELB key = deployed bytes, test signing key; 11 of 11 across owner/empty/missing, loaded files md5 == release): verified non-owner 403 no page bytes + audit DENIED/roster, owner 200, no identity 401, forged 401, empty and missing roster owner 403; real service host-local no-identity 401 and forged-header 401; public 302 to login.microsoftonline.com; r17 download re-read unchanged (OK, 49 returned 0 unheld, held 49 < universe 2160, empty-holdings REFUSED, query equal, grants_written 0); floor: rl4.AC1 (R17B baseline) 4 of 4 PASS; rl6.AC1 PASS after the manifest commit ab3d9965f2 (rl9_rl6.AC1_after_manifest.out; its first read before the manifest commit FAILED served_release False, row S51); ht.AC2 3 of 4 on its hard-coded env_keys 50, 4 of 4 with that one constant 51 (rl9_ht_AC2_env51_equivalent.out; row S50, no roll-back). The owner's real signed-in 200 is UNEXERCISED until Andrew opens the page | CLOSED 20261005T153246Z |
| manifest | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway deployed_commit <release sha> previous e91819e281 | committed hash | EC2_MANIFEST opal-gateway deployed_commit 37be3485db previous_deployed_commit e91819e281 deployed_at 2026-10-05T14:22:36Z (the wrapper Time line), hand edit on wk-NFRA_OPLGTW-15-r17 committed ab3d9965f2; wrapper release-branch commit a21a1146a2 not merged | CLOSED 20261005T153246Z |
| rollback-proven | verify | rollback tree /c/tmp/og-rb12 at e91819e281 equal to the live artifact, command recorded | diff 94 of 94 equal and verify PASS, or rolled back and re-verified | rollback tree /c/tmp/og-rb12 at e91819e281 (HEAD and clean re-read 14:2xZ before the act) 94 of 94 equal to S3 opal-gateway-e91819e281.tar.gz (rl8_cmp_rollback.out at PHASE C-A2); S3 head-object re-read after the act: key present, ETag 69bd2701, 480201 bytes, git-ref e91819e281 unchanged; command DEPLOY_BASE_REF=37be3485db9a00522c55a260666f708336c918f3 HALT_ACK=1 from /c/tmp/og-rb12; not executed (no roll-back: row S50 states why) | CLOSED 20261005T153246Z |

## Log

- 20261005T141753Z OPENED by 0.9.0_WK_NFRA_OPLGTW~15 with 4 leg(s)
- 20261005T153246Z LEG upload closed: uploaded s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-37be3485db.tar.gz (+ latest), both git-re
- 20261005T153246Z LEG install-verify closed: deploy Success ssm:1af86a41-9355-4bb0-b470-d745c57046bf rc=0 14:22Z; rl7_verify.sh after host+AFTER checks 19 of 19 PASS
- 20261005T153246Z LEG manifest closed: EC2_MANIFEST opal-gateway deployed_commit 37be3485db previous_deployed_commit e91819e281 deployed_at 2026-10-05T14:22:36
- 20261005T153246Z LEG rollback-proven closed: rollback tree /c/tmp/og-rb12 at e91819e281 (HEAD and clean re-read 14:2xZ before the act) 94 of 94 equal to S3 opal-gate
- 20261005T153246Z CLOSED -- all 4 legs proven
