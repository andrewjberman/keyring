# Deploy Completion Record
**Date opened:** 2026-10-17T12:41:11.092032+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261017T150806Z
**Deploy:** AMGT_HARVST HVST-cd-2: opal-gateway serves no dossier field built from a misfiled report (release cut on live 9d5b712557, two files)
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| BEFORE | verify | opal-gateway before-state | cd2_before.out: three planes at 9d5b712557, /health 200, 127 tools, UNH control counts | cd2_before.out at 383fba549f (LOCAL): three planes at 9d5b712557, /health 200, 127 tools md5 9a593c84, UNH control 21+3 / 4+1 | CLOSED 20261017T124513Z |
| CUT | git | rel-amgt-harvst-cd2 on 9d5b712557 | two-path diff, merge^1 equality, 7 test files pass, host-owner note cd2_hostowner_note.out | rel-amgt-harvst-cd2 1753c741d9 parent 9d5b712557; whole-repo diff 2 paths; merge^1 equality IDENTICAL; 38 tests pass; cd2_hostowner_note.out at 383fba549f (LOCAL) | CLOSED 20261017T124513Z |
| DEPLOY | activation | opal-gateway service (i-07dccb1615503ac99) | safe-ec2-deploy.sh from the release branch, health check green; restart window start/end UTC; rollback = opal-gateway-9d5b712557.tar.gz | cd2_deploy.out at 25699bc8e5 (LOCAL): rel-amgt-harvst-cd2 1753c741d9 on base 9d5b712557, DEPLOY_BASE_REF=9d5b712557, stale-base guard EQUAL at both checkpoints, SSM 4588aa93 Success, rc=0 at 15:01:28Z; restart window 15:00:55Z upload / 15:01:19Z unit restart / 15:02:22Z health 200 | CLOSED 20261017T150806Z |
| AFTER | verify | opal-gateway after-state | cd2_after.out: /health 200 and 127 tools equal to before; C-9 ref ask recorded | cd2_after.out at 25699bc8e5: /health 200 and 127 tools names md5 9a593c84 equal to before; host app tree 133 files, only app/harvest_research.py changed af2d662f -> 6d9e0dd3; EC2_MANIFEST.json deployed_commit 1753c741d9 previous 9d5b712557; C-9 ask to the issuer | CLOSED 20261017T150806Z |
| SERVED | verify | harvest_get_research KMB_US_Equity and UNH_US_Equity | cd2_served.out three lines PASS | cd2_served.out at 25699bc8e5: SERVED_KMB_DOSSIER=PASS (team_sheet read at source only), SERVED_CONTROL=PASS (UNH 21+3 / 4+1 equal, misfiled_fields_excluded []), TOOLS_AND_HEALTH_EQUAL=PASS; proof-of-spec-check VALID rc=0 | CLOSED 20261017T150806Z |

## Log

- 20261017T124111Z OPENED by 0.7.0_AE_CloudOps~SC1 with 5 leg(s)
- 20261017T124513Z LEG BEFORE closed: cd2_before.out at 383fba549f (LOCAL): three planes at 9d5b712557, /health 200, 127 tools md5 9a593c84, UNH control 21+3 
- 20261017T124513Z LEG CUT closed: rel-amgt-harvst-cd2 1753c741d9 parent 9d5b712557; whole-repo diff 2 paths; merge^1 equality IDENTICAL; 38 tests pass; cd
- 20261017T150806Z LEG DEPLOY closed: cd2_deploy.out at 25699bc8e5 (LOCAL): rel-amgt-harvst-cd2 1753c741d9 on base 9d5b712557, DEPLOY_BASE_REF=9d5b712557, sta
- 20261017T150806Z LEG AFTER closed: cd2_after.out at 25699bc8e5: /health 200 and 127 tools names md5 9a593c84 equal to before; host app tree 133 files, only
- 20261017T150806Z LEG SERVED closed: cd2_served.out at 25699bc8e5: SERVED_KMB_DOSSIER=PASS (team_sheet read at source only), SERVED_CONTROL=PASS (UNH 21+3 / 
- 20261017T150806Z CLOSED -- all 5 legs proven

## Amendment 2 (0.7.0_AE_CloudOps~SC1, 2026-10-17T14:58Z) -- fresh window, base and rollback
- Base: live 9d5b7125571520b977401634a01935924f4c9787 (manifest, artifact git-ref and instance agree, re-read 14:51Z). Release: rel-amgt-harvst-cd2 @1753c741d988faa05fa424386bcd9aa0c5efbf71, two paths.
- Restart window (UTC) intended: start no earlier than 2026-10-17T14:58Z, end by 2026-10-17T15:50Z. Actual start and end are recorded in cd2_after.out.
- Before (C-6): /health 200, MCP tool-name count 127, names md5 9a593c843feb61c2753d8c08a84eb61d. Control UNH_US_Equity: dossier_fields 21+3, continuation_fields 4+1 (C-7).
- Rollback: ec2/opal-gateway/opal-gateway-9d5b712557.tar.gz (897815 B), redeployed through the same script with DEPLOY_BASE_REF the then-live ref.
