# Deploy Completion Record
**Date opened:** 2026-10-02T19:18:28.353781+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261002T192923Z
**Deploy:** NFRA_OPLGTW OG-rl-3: opal-gateway app release 3a7d6a7dc8 -> 4231bd2ddc (/hx/teams routes + TEAMS_BEARER env), via safe-ec2-deploy.sh from /c/tmp/og-rel8
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~15
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| upload | s3-prefix | opal-gateway-latest.tar.gz and opal-gateway-4231bd2ddc.tar.gz in the gateway artifact bucket | deploy wrapper output line with git-ref 4231bd2ddc | uploaded s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-4231bd2ddc.tar.gz (+ latest); base guard declared 3a7d6a7dc8 == live ref at both reads | CLOSED 20261002T192922Z |
| install | ec2-baked-asset | opal-gateway host /opt/opal-gateway running path + .env 50 keys | rl3_verify.sh after: host md5 94 of 94 = release bytes, health 200, env 48 to 50, tool list unchanged | deploy Success ssm:d96df88a; rl3_verify.sh after VERIFY PASS 9 of 9 (SSM 85a08afd): health 200, md5 94 of 94 == release, tools 65 to 65, env 48 to 50 keys; ht.AC2 SERVED ARMS 4 of 4 PASS; ht.AC3 BEARER ARMS 2 of 2 PASS | CLOSED 20261002T192922Z |
| manifest | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway deployed_commit 4231bd2ddc previous 3a7d6a7dc8 | committed hash | EC2_MANIFEST opal-gateway deployed_commit 4231bd2ddc previous 3a7d6a7dc8, commit 1437d1315f | CLOSED 20261002T192923Z |
| rollback | verify | rollback tree /c/tmp/og-rb8 at 3a7d6a7dc8 proven equal to the live artifact before the act, command recorded | diff -rq 96 of 96 equal (PHASE A) and ht.AC2-AC4 PASS or rolled back | rollback tree /c/tmp/og-rb8 at 3a7d6a7dc8 diff -rq 96 of 96 equal to live S3 artifact at PHASE A; command recorded in ANNOUNCE_OG-rl-3.md; not executed, not needed: VERIFY PASS 9 of 9, AC2 and AC3 PASS | CLOSED 20261002T192923Z |

## Log

- 20261002T191828Z OPENED by 0.9.0_WK_NFRA_OPLGTW~15 with 4 leg(s)
- 20261002T192922Z LEG upload closed: uploaded s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-4231bd2ddc.tar.gz (+ latest); base guard 
- 20261002T192922Z LEG install closed: deploy Success ssm:d96df88a; rl3_verify.sh after VERIFY PASS 9 of 9 (SSM 85a08afd): health 200, md5 94 of 94 == release,
- 20261002T192923Z LEG manifest closed: EC2_MANIFEST opal-gateway deployed_commit 4231bd2ddc previous 3a7d6a7dc8, commit 1437d1315f
- 20261002T192923Z LEG rollback closed: rollback tree /c/tmp/og-rb8 at 3a7d6a7dc8 diff -rq 96 of 96 equal to live S3 artifact at PHASE A; command recorded in AN
- 20261002T192923Z CLOSED -- all 4 legs proven
