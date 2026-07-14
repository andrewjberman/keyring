# Deploy Completion Record
**Date opened:** 2026-07-14T20:11:07.512872+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260714T201534Z
**Deploy:** TCKT_CENTER CF behaviors x2 on portal-auth (CTO dispatch 200837Z pre-signed; tickets wildcard + exact twin)
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | plan 0/1/0 distribution in-place + safe-apply (HALTGT) + 0-diff | apply rc=0, replan No changes | plan 0/1/0 distribution in-place; safe-apply rc=0 Apply complete; 0-diff replan No changes | CLOSED 20260714T201533Z |
| L2 | verify | EXERCISE: unauthenticated curl through CF returns authorizer JSON 401/403 NOT SPA HTML, both paths; tag portal-auth-v1.19.0 pushed | curl evidence + tag on origin | EXERCISED both paths unauthenticated through CF (d2n2nzpeqf34ge): /api/scoped/tickets AND /api/scoped/tickets/probe-123 both return HTTP 401 application/json {error: Missing or invalid Authorization header} -- the authorizer speaking, NOT SPA HTML; tag portal-auth-v1.19.0 pushed | CLOSED 20260714T201533Z |

## Log

- 20260714T201107Z OPENED by 0.7.0_AE_CloudOps with 2 leg(s)
- 20260714T201533Z LEG L1 closed: plan 0/1/0 distribution in-place; safe-apply rc=0 Apply complete; 0-diff replan No changes
- 20260714T201533Z LEG L2 closed: EXERCISED both paths unauthenticated through CF (d2n2nzpeqf34ge): /api/scoped/tickets AND /api/scoped/tickets/probe-123 
- 20260714T201534Z CLOSED -- all 2 legs proven
