# Deploy Completion Record
**Date opened:** 2026-09-19T09:44:29.561799+00:00
**Status:** OPEN
**Deploy:** IB-rtf-8: holdings forked enforcer folded onto shared _authz module, irpt-holdings deployed
**Authored by:** 0.9.0_WK_IRPT_BCKEND~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L2 | verify | live route re-test: abby_horton served with disclosure, cross-firm+other-firm refused, pre-fold negative control | battery + live reads |  | OPEN |
| irpt-holdings | tf-lambda | module.irpt_holdings.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20260919T094429Z OPENED by 0.9.0_WK_IRPT_BCKEND~1 with 2 leg(s)
