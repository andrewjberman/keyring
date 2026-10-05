# Deploy Completion Record
**Date opened:** 2026-10-05T02:14:31.388486+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-rl-6: opal-gateway app release 4b6b823fae -> rel-nfra-oplgtw-r17 e91819e281 (OG-q-7: dim_asset downloads open held-only under C3) via safe-ec2-deploy.sh from /c/tmp/og-rel11; never-widen COO 1a21759226 CTO de3381d39f (no condition) CVO 9c7fa957a3 (R1-R2) SIGNED
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~15
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| upload | s3-prefix | opal-gateway-latest.tar.gz and opal-gateway-<release sha>.tar.gz in the gateway artifact bucket | deploy wrapper output line with git-ref <release sha>; base guard declared 4b6b823fae == live at both reads |  | OPEN |
| install-verify | ec2-baked-asset | opal-gateway host /opt/opal-gateway running path + .env 50 keys | rl6_verify.sh after: md5 94 of 94 = release bytes, health 200, 65 tools, 50 key names unchanged, download OK held-only with discriminator, empty-holdings refusal, query equal; rl4.AC1 ht.AC2 |  | OPEN |
| manifest | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway deployed_commit <release sha> previous 4b6b823fae | committed hash |  | OPEN |
| rollback-proven | verify | rollback tree /c/tmp/og-rb11 at 4b6b823fae equal to the live artifact, command recorded | diff 94 of 94 equal (PHASE A) and verify PASS, or rolled back and re-verified |  | OPEN |

## Log

- 20261005T021431Z OPENED by 0.9.0_WK_NFRA_OPLGTW~15 with 4 leg(s)
