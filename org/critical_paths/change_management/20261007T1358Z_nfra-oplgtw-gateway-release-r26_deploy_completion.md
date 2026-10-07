# Deploy Completion Record
**Date opened:** 2026-10-07T13:58:18.901544+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-rl-12 PHASE B: opal-gateway release 240ac2fe5a -> rel-nfra-oplgtw-r26 feddb37244 (OG-al-2 scoped-concierge status-tool allowlist row WIDENS, Andrew's word; Z-S65 execution-id shape check NARROWS; OG-up-2 content-keyed re-send dedupe; RIV-rt-1 GET /rivalfunds/{day}/chart/{fund} ADDED; 5 shipped files, 5 source-only; consumers moved: the one opal-gateway.service on host i-07dccb1615503ac99 + the S3 artifacts opal-gateway-latest.tar.gz and opal-gateway-feddb37244.tar.gz; no ECS/Lambda task family, image or tag moved) via safe-ec2-deploy.sh from /c/tmp/og-rel21; never-widen COO 4d9d1208af CTO 78d524e001 CVO d293c39967 SIGNED
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~28
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| upload | s3-prefix | opal-gateway-latest.tar.gz and opal-gateway-<release sha>.tar.gz in the gateway artifact bucket | deploy wrapper output line with git-ref <release sha>; base guard 240ac2fe5a == live |  | OPEN |
| install-verify | ec2-baked-asset | opal-gateway host /opt/opal-gateway running path + .env 51 keys | r26_verify.sh after: md5 97 of 97 = release bytes (5 differ from live), health 200, 66 tools, 51 names with every value sha256 equal, four route arms, floor rl4.AC1 + ht.AC2 |  | OPEN |
| installed-reads | verify | installed code on the host: status tool allowlist, scoped consent, id-shape arms, portal login, real holder | RL12_ALLOW.json + RL12_FLOOR.json from the installed tree with host digests; scoped concierge admitted for status tool, unnamed tool denied, consent 9, 66 tools, refused ids (slash and dot) 0 requests, accepted id OK, login OK, real holder returned=distinct=held 0 unheld; any miss rolls back |  | OPEN |
| manifest | git | infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway deployed_commit <release sha> previous 240ac2fe5a | committed hash |  | OPEN |
| rollback-proven | verify | rollback tree /c/tmp/og-rb20 at 240ac2fe5a equal to the live artifact, command recorded | diff 97 of 97 equal and verify PASS, or rolled back and re-verified |  | OPEN |

## Log

- 20261007T135818Z OPENED by 0.9.0_WK_NFRA_OPLGTW~28 with 5 leg(s)
