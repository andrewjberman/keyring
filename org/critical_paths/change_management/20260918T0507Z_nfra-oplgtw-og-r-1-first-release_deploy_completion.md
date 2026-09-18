# Deploy Completion Record
**Date opened:** 2026-09-18T05:07:24.309664+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-r-1 first release: integrated Gateway build, OAuth cutover, Schwab flag OFF
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | ec2-baked-asset | opal-gateway /opt/opal-gateway | SSM sha256sum digest match vs the deployed build input, file by file, denominator printed (OGR1-AC4) |  | OPEN |
| L2 | verify | post-deploy live checks: 401 resource challenge, discovery metadata, zero Schwab tools registered, error count vs baseline, restricted-profile principal count, renamed-role assume/deny | OGR1-AC3,AC5,AC6,AC7,AC9,AC12,AC13 PASS-by-output |  | OPEN |
| L3 | git | EC2_MANIFEST.json services.opal-gateway.deployed_commit | git commit hash of safe-ec2-deploy.sh's own manifest-update commit |  | OPEN |

## Log

- 20260918T050724Z OPENED by 0.9.0_WK_NFRA_OPLGTW~2 with 3 leg(s)
