# Deploy Completion Record
**Date opened:** 2026-10-05T14:17:53.799140+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-rl-6 Phase C-B: opal-gateway app release e91819e281 -> rel-nfra-oplgtw-r17c 37be3485db (/yearinreview OWNER-ONLY behind its own fail-closed roster key YEARINREVIEW_VIEW_ALLOWED_EMAILS; .env 50 -> 51 names) via safe-ec2-deploy.sh from /c/tmp/og-rel13; never-widen COO f6fdd4047b CTO 86e34b783d (no condition) CVO 9c23533619 (T1-T2) SIGNED
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~15
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| upload | s3-prefix | opal-gateway-latest.tar.gz and opal-gateway-<release sha>.tar.gz in the gateway artifact bucket | deploy wrapper output line with git-ref <release sha>; base guard declared e91819e281 == live at both reads |  | OPEN |
| install-verify | ec2-baked-asset | opal-gateway host /opt/opal-gateway running path + .env 51 keys (50 + YEARINREVIEW_VIEW_ALLOWED_EMAILS) | rl7_verify.sh after: md5 96 of 96 = release bytes, health 200, 65 tools, 51 names with 50 prior value sha256 equal, new key digest = sha256(andrew@opalinvest.com), T2 arms on the deployed host (non-owner 403, owner 200, none 401, forged 401, empty/missing roster 403), host-local 401 x2, public 302, r17 download re-read; rl6.AC1 rl4.AC1(R17B baseline) ht.AC2 |  | OPEN |
| manifest | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway deployed_commit <release sha> previous e91819e281 | committed hash |  | OPEN |
| rollback-proven | verify | rollback tree /c/tmp/og-rb12 at e91819e281 equal to the live artifact, command recorded | diff 94 of 94 equal and verify PASS, or rolled back and re-verified |  | OPEN |

## Log

- 20261005T141753Z OPENED by 0.9.0_WK_NFRA_OPLGTW~15 with 4 leg(s)
