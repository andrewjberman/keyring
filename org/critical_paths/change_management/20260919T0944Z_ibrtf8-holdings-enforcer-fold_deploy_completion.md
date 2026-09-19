# Deploy Completion Record
**Date opened:** 2026-09-19T09:44:29.561799+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260919T100559Z
**Deploy:** IB-rtf-8: holdings forked enforcer folded onto shared _authz module, irpt-holdings deployed
**Authored by:** 0.9.0_WK_IRPT_BCKEND~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L2 | verify | live route re-test: abby_horton served with disclosure, cross-firm+other-firm refused, pre-fold negative control | battery + live reads | battery_ib_rtf_8.py arm_e_live_proof, this run: abby_horton/49financial served k=21 unprojected_grant={count:12,denominator:33,kinds:{UNPROJECTED-ID:12}} (k+count==denominator); cross-firm swap refused EMPTY_GRANT; inflection/cottonwood refused EMPTY_GRANT; pre-fold fork (blob 8f849457be) on the SAME real request refused UNPROJECTED_GRANT whole (read as count=0, the false negative) | CLOSED 20260919T100537Z |
| irpt-holdings | tf-lambda | module.irpt_holdings.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | irpt-holdings served=78XvypHOpeybejwKd5KLCwNcgat2jbQr6O3PhdwaFSU= built=78XvypHOpeybejwKd5KLCwNcgat2jbQr6O3PhdwaFSU= MATCH=True; TF apply 0 added/1 changed/0 destroyed; replan detailed-exitcode=0 (No changes) | CLOSED 20260919T100506Z |

## Log

- 20260919T094429Z OPENED by 0.9.0_WK_IRPT_BCKEND~1 with 2 leg(s)
- 20260919T100506Z LEG irpt-holdings closed: irpt-holdings served=78XvypHOpeybejwKd5KLCwNcgat2jbQr6O3PhdwaFSU= built=78XvypHOpeybejwKd5KLCwNcgat2jbQr6O3PhdwaFSU= MAT
- 20260919T100537Z LEG L2 closed: battery_ib_rtf_8.py arm_e_live_proof, this run: abby_horton/49financial served k=21 unprojected_grant={count:12,denomina
- 20260919T100559Z CLOSED -- all 2 legs proven
