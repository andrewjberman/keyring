# Deploy Completion Record
**Date opened:** 2026-10-07T04:29:23.881834+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-rl-11 PHASE B: opal-gateway release 7d65a28db0 -> rel-nfra-oplgtw-r25 240ac2fe5a (OG-up-1 send split + status tool, 65->66 tools; NFRA_OPALAI OA-f-14 scoped consent 17->9; 5 shipped files, 3 source-only) via safe-ec2-deploy.sh from /c/tmp/og-rel20; never-widen COO 8a769f4b54 CTO 62a89fbf07 CVO a4a47a0ba6 SIGNED
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~28
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| upload | s3-prefix | opal-gateway-latest.tar.gz and opal-gateway-<release sha>.tar.gz in the gateway artifact bucket | deploy wrapper output line with git-ref <release sha>; base guard 7d65a28db0 == live |  | OPEN |
| install-verify | ec2-baked-asset | opal-gateway host /opt/opal-gateway running path + .env 51 keys | r25_verify.sh after: md5 97 of 97 = release bytes (5 differ from live), health 200, 66 tools, 51 names with every value sha256 equal, floor rl4.AC1 + ht.AC2 |  | OPEN |
| installed-reads | verify | installed code on the host: status tool, scoped consent, portal login, real holder | RL11_SEND.json + RL11_SCOPES.json + RL11_FLOOR.json from the installed tree with host digests; scoped silent acquire OK, probes all 200, status tool OK, login OK, real holder returned=distinct=held 0 unheld; any miss rolls back |  | OPEN |
| manifest | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway deployed_commit <release sha> previous 7d65a28db0 | committed hash |  | OPEN |
| rollback-proven | verify | rollback tree /c/tmp/og-rb19 at 7d65a28db0 equal to the live artifact, command recorded | diff 96 of 96 equal and verify PASS, or rolled back and re-verified |  | OPEN |

## Log

- 20261007T042923Z OPENED by 0.9.0_WK_NFRA_OPLGTW~28 with 5 leg(s)
