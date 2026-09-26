# Deploy Completion Record
**Date opened:** 2026-09-26T16:07:03.193225+00:00
**Status:** OPEN
**Deploy:** irpt-ycharts-generate-role: READ NORMALIZED_PORTFOLIO + RETAIN REQUEST_COMPOSITION (~Y patch @e5daacce0b; CTO 101275)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| G1 | activation | aws_iam_role_policy.generate | safe-apply of the saved plan 0/1/0; replan No changes |  | OPEN |
| V1 | verify | IAM simulation | K5's two denied actions (GetObjectVersion on normalized_portfolios; PutObject on request_compositions) DENIED before -> ALLOWED after for the generate role; a foreign prefix still denied (negative arm) |  | OPEN |

## Log

- 20260926T160703Z OPENED by 2.0.0_SA_COO~P with 2 leg(s)
