# Deploy Completion Record
**Date opened:** 2026-10-16T17:08:24.046620+00:00
**Status:** OPEN
**Deploy:** AMGT_HARVST HVST-cc-7 (fresh entry after the HOLD, issuer GO msg 6917): deploy the three D1-S29 fixes to the opal-gateway service (EC2 i-07dccb1615503ac99; restarts every MCP tool for every principal on every box): release cut on the LIVE deployed commit d14445961d, six paths only, safe-ec2-deploy.sh opal-gateway; C-6: MCP tool-name count (127 at the last record) and /health read before and after; RESTART WINDOW recorded here. Rollback (Branch F): redeploy previous_deployed_commit 38fe44d5cb (tarball ec2/opal-gateway/opal-gateway-38fe44d5cb.tar.gz) through the same script.
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| BEFORE | verify | cc7_before.out | live commit (manifest, artifact plane, instance) equal, six-path diff, tests pass, previous tarball key, tool-name count and /health BEFORE |  | OPEN |
| DEPLOY | verify | opal-gateway i-07dccb1615503ac99 | safe-ec2-deploy.sh opal-gateway from the release branch, restart window UTC recorded |  | OPEN |
| AFTER | verify | cc7_after.out | /health 200, tool-name count equal to BEFORE (C-6), manifest deployed_commit/previous_deployed_commit recorded |  | OPEN |
| SERVED | verify | cc7_served.out | three served reads PASS: resolve PG candidates, UNH EPS claim, KMB research exclusion |  | OPEN |

## Log

- 20261016T170824Z OPENED by 0.7.0_AE_CloudOps~SC1 with 4 leg(s)
