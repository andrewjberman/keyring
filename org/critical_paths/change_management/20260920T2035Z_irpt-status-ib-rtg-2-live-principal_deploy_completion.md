# Deploy Completion Record
**Date opened:** 2026-09-20T20:35:38.317971+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260920T205415Z
**Deploy:** IRPT_BCKEND.TO-IB-rtg-2 arm (e) -- bounded test principal (rtf-9 packet blob a1f36b95b2 mechanism, NEW epoch) exercising irpt-status's three routes post-apply, then full rollback
**Authored by:** 0.9.0_WK_IRPT_BCKEND~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 1.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | K1/K1b test principal created, login exercised | DynamoDB put_item + consistent read-back + login HTTP 200 | K1 created 2026-09-20T20:37:26Z (PK USER#usr_irptrtg2_1789936645), K1b created same tick, consistent read-back True for both; login POST /auth/login -> HTTP 200, claims firmId=49financial advisorKey=abby_horton | CLOSED 20260920T205414Z |
| L2 | verify | status-summary/status-job/analysis-report requests resolve NOT_FOUND or SERVED, never UNSUPPORTED_OPERATION | battery output | 3 of 3 routes exercised (status-summary, status-job negative control, analysis-report) -- all NOT_FOUND http 200, 0 DEFECT-STILL-PRESENT (UNSUPPORTED_OPERATION); see IB-rtg-2_R73-AC1_battery_output.txt lines 30-34 | CLOSED 20260920T205414Z |
| L3 | verify | full rollback: K1b+K1 deleted, refresh refused, token 401 after exp, no residue | battery output | K1b+K1 DeleteItem verified by failing consistent GetItem (2 of 2); refresh HTTP 404 REFUSED; access token 401 REFUSED after exp 20:52:35Z; prefix scan after: 0/0/0 residue | CLOSED 20260920T205415Z |

## Log

- 20260920T203538Z OPENED by 0.9.0_WK_IRPT_BCKEND~2 with 3 leg(s)
- 20260920T205414Z LEG L1 closed: K1 created 2026-09-20T20:37:26Z (PK USER#usr_irptrtg2_1789936645), K1b created same tick, consistent read-back True for 
- 20260920T205414Z LEG L2 closed: 3 of 3 routes exercised (status-summary, status-job negative control, analysis-report) -- all NOT_FOUND http 200, 0 DEFE
- 20260920T205415Z LEG L3 closed: K1b+K1 DeleteItem verified by failing consistent GetItem (2 of 2); refresh HTTP 404 REFUSED; access token 401 REFUSED af
- 20260920T205415Z CLOSED -- all 3 legs proven
