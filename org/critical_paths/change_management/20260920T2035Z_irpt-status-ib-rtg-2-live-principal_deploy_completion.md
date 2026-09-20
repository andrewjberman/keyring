# Deploy Completion Record
**Date opened:** 2026-09-20T20:35:38.317971+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND.TO-IB-rtg-2 arm (e) -- bounded test principal (rtf-9 packet blob a1f36b95b2 mechanism, NEW epoch) exercising irpt-status's three routes post-apply, then full rollback
**Authored by:** 0.9.0_WK_IRPT_BCKEND~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 1.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | K1/K1b test principal created, login exercised | DynamoDB put_item + consistent read-back + login HTTP 200 |  | OPEN |
| L2 | verify | status-summary/status-job/analysis-report requests resolve NOT_FOUND or SERVED, never UNSUPPORTED_OPERATION | battery output |  | OPEN |
| L3 | verify | full rollback: K1b+K1 deleted, refresh refused, token 401 after exp, no residue | battery output |  | OPEN |

## Log

- 20260920T203538Z OPENED by 0.9.0_WK_IRPT_BCKEND~2 with 3 leg(s)
