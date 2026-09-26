# Deploy Completion Record
**Date opened:** 2026-09-26T17:19:11.267368+00:00
**Status:** OPEN
**Deploy:** Row S148 (CTO 101347): explicit Deny on ssm:GetParameter* for irpt-ycharts-runner-role outside /irpt/render-token/*; then N1 re-run; then export deploy (B) D3 back ON (cross-ref ledger irpt-export-deploy-b-20260926)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| F1 | activation | export root aws_iam_role_policy.render_host_parameter_fence | plan exactly 1 add; safe-apply; replan No changes |  | OPEN |
| N2 | verify | N1 re-run after the fence | host: token Get+Delete allowed, any other name (incl. a foreign SecureString) DENIED; export role 4 of 4; ~Y's 40 resident pairs still met |  | OPEN |
| D3B | activation | export_render back ON | plan 0/1/0 env off -> on; safe-apply; readback; replan No changes |  | OPEN |

## Log

- 20260926T171911Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
