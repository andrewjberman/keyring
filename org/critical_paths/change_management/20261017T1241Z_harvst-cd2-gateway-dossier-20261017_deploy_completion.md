# Deploy Completion Record
**Date opened:** 2026-10-17T12:41:11.092032+00:00
**Status:** OPEN
**Deploy:** AMGT_HARVST HVST-cd-2: opal-gateway serves no dossier field built from a misfiled report (release cut on live 9d5b712557, two files)
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| BEFORE | verify | opal-gateway before-state | cd2_before.out: three planes at 9d5b712557, /health 200, 127 tools, UNH control counts |  | OPEN |
| CUT | git | rel-amgt-harvst-cd2 on 9d5b712557 | two-path diff, merge^1 equality, 7 test files pass, host-owner note cd2_hostowner_note.out |  | OPEN |
| DEPLOY | activation | opal-gateway service (i-07dccb1615503ac99) | safe-ec2-deploy.sh from the release branch, health check green; restart window start/end UTC; rollback = opal-gateway-9d5b712557.tar.gz |  | OPEN |
| AFTER | verify | opal-gateway after-state | cd2_after.out: /health 200 and 127 tools equal to before; C-9 ref ask recorded |  | OPEN |
| SERVED | verify | harvest_get_research KMB_US_Equity and UNH_US_Equity | cd2_served.out three lines PASS |  | OPEN |

## Log

- 20261017T124111Z OPENED by 0.7.0_AE_CloudOps~SC1 with 5 leg(s)
