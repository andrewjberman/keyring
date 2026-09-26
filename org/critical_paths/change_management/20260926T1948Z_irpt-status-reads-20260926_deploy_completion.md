# Deploy Completion Record
**Date opened:** 2026-09-26T19:48:33.031592+00:00
**Status:** OPEN
**Deploy:** IRPT hops 8-9: irpt-status packages interactive_access.py (A) and irpt-status-role gains s3:GetObjectVersion on its four families (B); ~Y HOPS_8_10 @acd17573d7, CTO 101466
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | irpt-status artifact + apply | census vs deployed pfAr3uZE (exactly +interactive_access.py); safe-apply; readback CodeSha256; 0-diff replan |  | OPEN |
| B1 | activation | irpt-status-role policy (ops root) | plan names only the one statement's actions; safe-apply; readback policy; 0-diff replan |  | OPEN |
| V1 | verify | ~Y's proofs on the served code | status_read_proof.py no overlay 4/4 Opal owner-reads; iam_hop8_pairs.py simulate 10/10 |  | OPEN |

## Log

- 20260926T194833Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
