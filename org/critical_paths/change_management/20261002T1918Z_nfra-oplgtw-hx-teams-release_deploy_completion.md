# Deploy Completion Record
**Date opened:** 2026-10-02T19:18:28.353781+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-rl-3: opal-gateway app release 3a7d6a7dc8 -> 4231bd2ddc (/hx/teams routes + TEAMS_BEARER env), via safe-ec2-deploy.sh from /c/tmp/og-rel8
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~15
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| upload | s3-prefix | opal-gateway-latest.tar.gz and opal-gateway-4231bd2ddc.tar.gz in the gateway artifact bucket | deploy wrapper output line with git-ref 4231bd2ddc |  | OPEN |
| install | ec2-baked-asset | opal-gateway host /opt/opal-gateway running path + .env 50 keys | rl3_verify.sh after: host md5 94 of 94 = release bytes, health 200, env 48 to 50, tool list unchanged |  | OPEN |
| manifest | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway deployed_commit 4231bd2ddc previous 3a7d6a7dc8 | committed hash |  | OPEN |
| rollback | verify | rollback tree /c/tmp/og-rb8 at 3a7d6a7dc8 proven equal to the live artifact before the act, command recorded | diff -rq 96 of 96 equal (PHASE A) and ht.AC2-AC4 PASS or rolled back |  | OPEN |

## Log

- 20261002T191828Z OPENED by 0.9.0_WK_NFRA_OPLGTW~15 with 4 leg(s)
