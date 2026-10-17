# Deploy Completion Record
**Date opened:** 2026-10-17T00:08:28.056158+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261017T001601Z
**Deploy:** AMGT_HARVST HVST-cc-7 amendment 3 (GO msg 7057): deploy the three D1-S29 fixes to the opal-gateway service (EC2 i-07dccb1615503ac99; restarts every MCP tool for every principal on every box): release rel-amgt-harvst-cc7b @319c9413a2 cut on the LIVE deployed commit 4be300110e, six paths only, safe-ec2-deploy.sh opal-gateway; C-6: MCP tool-name count (127 served) and /health read before and after; RESTART WINDOW recorded here. Rollback (Branch F): redeploy 4be300110e (tarball ec2/opal-gateway/opal-gateway-4be300110e.tar.gz) through the same script.
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| BEFORE | verify | cc7_before.out | live commit (manifest, artifact plane, instance) equal, six-path diff, tests pass, rollback tarball key, tool-name count and /health BEFORE | cc7_before.out AMENDMENT 3 section: manifest, artifact plane and instance agree on 4be300110e; live diff of the six paths vs d14445961d empty; release 319c9413a2 six paths, 33 tests pass; rollback tarball opal-gateway-4be300110e.tar.gz; C-6 before health 200 tools 127 md5 9a593c84; precheck 77 of 77 | CLOSED 20261017T000856Z |
| DEPLOY | verify | opal-gateway i-07dccb1615503ac99 | safe-ec2-deploy.sh opal-gateway from the release branch, restart window UTC recorded | safe-ec2-deploy.sh opal-gateway rc=0 from rel-amgt-harvst-cc7b 319c9413a2, base 4be300110e (stale-base guard equal); restart window 00:10:02Z upload, 00:10:26Z unit start, 00:11:01Z health 200 | CLOSED 20261017T001213Z |
| AFTER | verify | cc7_after.out | /health 200, tool-name count equal to BEFORE (C-6), manifest deployed_commit/previous_deployed_commit recorded | cc7_after.out: health 200, tools 127 md5 9a593c84 equal to BEFORE (C-6); exactly 3 host app files changed; manifest deployed_commit 319c9413a2 previous 4be300110e (recording to trunk pending) | CLOSED 20261017T001213Z |
| SERVED | verify | cc7_served.out | three served reads PASS: resolve PG candidates, UNH EPS claim, KMB research exclusion | cc7_served.out: SERVED_RESOLVE_PG=PASS (PG candidates, PCG exact PCG_US_Equity), SERVED_EPS_CLAIM=PASS (20 of 20 figures carry basis; 10 of 10 IS_DIL_EPS_CONT_OPS carry NOT the reported), SERVED_KMB_RESEARCH=PASS (fbd50086c4065785 absent from research_reports, named in misfiled_reports_excluded) | CLOSED 20261017T001524Z |

## Log

- 20261017T000828Z OPENED by 0.7.0_AE_CloudOps~SC1 with 4 leg(s)
- 20261017T000856Z LEG BEFORE closed: cc7_before.out AMENDMENT 3 section: manifest, artifact plane and instance agree on 4be300110e; live diff of the six path
- 20261017T001213Z LEG DEPLOY closed: safe-ec2-deploy.sh opal-gateway rc=0 from rel-amgt-harvst-cc7b 319c9413a2, base 4be300110e (stale-base guard equal); res
- 20261017T001213Z LEG AFTER closed: cc7_after.out: health 200, tools 127 md5 9a593c84 equal to BEFORE (C-6); exactly 3 host app files changed; manifest depl
- 20261017T001524Z LEG SERVED closed: cc7_served.out: SERVED_RESOLVE_PG=PASS (PG candidates, PCG exact PCG_US_Equity), SERVED_EPS_CLAIM=PASS (20 of 20 figures
- 20261017T001601Z CLOSED -- all 4 legs proven
