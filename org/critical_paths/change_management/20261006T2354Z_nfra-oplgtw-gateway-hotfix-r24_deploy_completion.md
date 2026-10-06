# Deploy Completion Record
**Date opened:** 2026-10-06T23:54:51.931165+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-rl-10 PHASE B: opal-gateway HOTFIX release 2c27f3a795 -> rel-nfra-oplgtw-r24 9d3e2eb3fc (CTO R32: the opal_portal service login moves from the raw API Gateway host to the front door www.opalinvest.dev; ONE shipped file app/integrations/opal_portal/integration.py, +6/-6) via safe-ec2-deploy.sh from /c/tmp/og-rel18; never-widen COO 86dae82982 CTO d274986e8d CVO 49470c5691 SIGNED
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~28
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| upload | s3-prefix | opal-gateway-latest.tar.gz and opal-gateway-<release sha>.tar.gz in the gateway artifact bucket | deploy wrapper output line with git-ref <release sha>; base guard declared 2c27f3a795 == live at both reads |  | OPEN |
| install-verify | ec2-baked-asset | opal-gateway host /opt/opal-gateway running path + .env 51 keys | r24_verify.sh after: md5 96 of 96 = release bytes (1 differs from live: opal_portal/integration.py), health 200, 65 tools, 51 names with every value sha256 equal, installed integration is the release file and its login is OK through www.opalinvest.dev, floor rl4.AC1 + ht.AC2 |  | OPEN |
| installed-login | verify | installed opal_portal integration's own _PortalSession.token() on the host with the real service secret, in process | RL10_LOGIN.json body login OK auth_host www.opalinvest.dev installed_code true served_release <release sha> grants_written 0 and the host RL10_DIGEST; a login that is not OK rolls back |  | OPEN |
| manifest | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway deployed_commit <release sha> previous 2c27f3a795 | committed hash |  | OPEN |
| rollback-proven | verify | rollback tree /c/tmp/og-rb17 at 2c27f3a795 equal to the live artifact, command recorded | diff 96 of 96 equal and verify PASS, or rolled back and re-verified |  | OPEN |

## Log

- 20261006T235451Z OPENED by 0.9.0_WK_NFRA_OPLGTW~28 with 5 leg(s)
