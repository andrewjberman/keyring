# Deploy Completion Record
**Date opened:** 2026-10-06T05:26:21.962969+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-rl-7 A1 PHASE B+D: opal-gateway app release 37be3485db -> rel-nfra-oplgtw-r19b cf4b036e62 (R22: OA-e-10 NOT carried; 2 behaviour files: admin_refusals.py sender fields from entry args only, envelope.py docstring-only; server.py byte-equal to live so /login unchanged; 21 gateway files) via safe-ec2-deploy.sh from /c/tmp/og-rel15; never-widen COO 0e93179a50 CTO add7a9166f (no condition) CVO e79b976d9b (V1-V3) SIGNED
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~15
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| upload | s3-prefix | opal-gateway-latest.tar.gz and opal-gateway-<release sha>.tar.gz in the gateway artifact bucket | deploy wrapper output line with git-ref <release sha>; base guard declared 37be3485db == live at both reads |  | OPEN |
| install-verify | ec2-baked-asset | opal-gateway host /opt/opal-gateway running path + .env 51 keys | r19b_verify.sh after: md5 96 of 96 = release bytes, health 200, 65 tools, 51 names with every value sha256 equal, sender arm AS_GIVEN/NULL, /login host-local before == after (no identity; synthetic verified identity), floor rl4.AC1 + ht.AC2 |  | OPEN |
| manifest | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway deployed_commit <release sha> previous 37be3485db | committed hash |  | OPEN |
| rollback-proven | verify | rollback tree /c/tmp/og-rb14 at 37be3485db equal to the live artifact, command recorded | diff 96 of 96 equal and verify PASS, or rolled back and re-verified |  | OPEN |
| drain-back | git | R16 drain-back: git diff <deployed> CLOUD -- infra/aws/ec2/opal-gateway empty; LINEAGE_R18 CLOUD-only list updated | recorded diff output |  | OPEN |

## Log

- 20261006T052621Z OPENED by 0.9.0_WK_NFRA_OPLGTW~15 with 5 leg(s)
