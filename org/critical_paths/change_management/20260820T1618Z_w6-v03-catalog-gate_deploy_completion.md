# Deploy Completion Record
**Date opened:** 2026-08-20T16:18:53.877579+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260820T162318Z
**Deploy:** OPAL_ANALYST W5-V03: catalog v0.3 + graphql_plumbing gate SHIP-TOGETHER to opal-gateway (@96dcb4a66a)
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | gateway tree tarball (carries v0.3 catalog + v0.3 gate atomically) -> lambda-artifacts/ec2/opal-gateway/ | deploy artifact sha + manifest | gateway tree tarball built + uploaded (single artifact carries v0.3 catalog + v0.3 gate atomically -- ship-together by construction); manifest committed @8e748abeaa | CLOSED 20260820T162010Z |
| L2 | activation | safe-ec2-deploy opal-gateway: single artifact = ship-together by construction; service restart | SSM Success + on-box version 0.3 | safe-ec2-deploy opal-gateway SUCCESS; single artifact = no catalog-only/gate-only split path exists; service restarted, health retry held | CLOSED 20260820T162010Z |
| L3 | verify | on-box exercise 16/16 vs DEPLOYED v0.3 catalog + rows 4/7 re-exercise + endpoint ALLOW/DENY/floor + R1 census 0-over-4MB | SSM battery + curl rows | on-box exercise 16/16 vs DEPLOYED v0.3 (incl O-1 rider + both mutants); deployed catalog sha 29079a8fda...df42 == the ferry's certified emit sha 29079a8fda; version 0.3 on-box; LIVE endpoint (localhost, the correct plane -- /query/v0 falls to ALB OIDC externally): ALLOW 200 serve w/ data, ROW-4 held-at-andrew 403 carrying the NEW v0.3 verdict_state note ('verdict_state=pending-andrew'), ROW-7 floor 403, off-catalog 403, unauth 401. R1 census 0-over-4MB (tier3 3.81MB + valuation 2.18MB both clear the 4MB cap; nothing routes to CTO). Ship-together verified by construction (single artifact) | CLOSED 20260820T162318Z |

## Log

- 20260820T161853Z OPENED by 0.7.0_AE_CloudOps with 3 leg(s)
- 20260820T162010Z LEG L1 closed: gateway tree tarball built + uploaded (single artifact carries v0.3 catalog + v0.3 gate atomically -- ship-together by c
- 20260820T162010Z LEG L2 closed: safe-ec2-deploy opal-gateway SUCCESS; single artifact = no catalog-only/gate-only split path exists; service restarted, 
- 20260820T162318Z LEG L3 closed: on-box exercise 16/16 vs DEPLOYED v0.3 (incl O-1 rider + both mutants); deployed catalog sha 29079a8fda...df42 == the fe
- 20260820T162318Z CLOSED -- all 3 legs proven
