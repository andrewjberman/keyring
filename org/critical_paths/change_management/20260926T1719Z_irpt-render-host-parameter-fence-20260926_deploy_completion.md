# Deploy Completion Record
**Date opened:** 2026-09-26T17:19:11.267368+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260926T173120Z
**Deploy:** Row S148 (CTO 101347): explicit Deny on ssm:GetParameter* for irpt-ycharts-runner-role outside /irpt/render-token/*; then N1 re-run; then export deploy (B) D3 back ON (cross-ref ledger irpt-export-deploy-b-20260926)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| F1 | activation | export root aws_iam_role_policy.render_host_parameter_fence | plan exactly 1 add; safe-apply; replan No changes | TF @1ebb09b4c5 (export/b2_render.tf render_host_parameter_fence, name irpt-export-render-host-parameter-fence-policy after the naming gate); plan 1 add / 0 / 0; safe-apply 'Apply complete! Resources: 1 added, 0 changed, 0 destroyed.'; replan exit 0. Census: host scripts 1 name (render_export.cjs:87); ~Y's resident census @4735d05d4a 0 parameter reads; CloudTrail 0 in 7 days (control 12/12). | CLOSED 20260926T172648Z |
| N2 | verify | N1 re-run after the fence | host: token Get+Delete allowed, any other name (incl. a foreign SecureString) DENIED; export role 4 of 4; ~Y's 40 resident pairs still met | LIVE (no candidate policy) iam_simulate_pairs: irpt-ycharts-runner-role fence pairs 7 of 7 met -- ssm:GetParameter + DeleteParameter on /irpt/render-token/* ALLOWED; GetParameter on /irpt/walk-principal/x/password (a foreign SecureString path) and /opal/other DENIED; GetParameters /opal/other DENIED; GetParametersByPath /opal DENIED; PutParameter on the token DENIED. irpt-export-render-role 4 of 4 (Put+Delete token, no Get, no human JWT key). ~Y's 40 resident pairs 40 of 40 still met. | CLOSED 20260926T172649Z |
| D3B | activation | export_render back ON | plan 0/1/0 env off -> on; safe-apply; readback; replan No changes | Export deploy (B) D3 back ON under this fence (cross-ref ledger irpt-export-deploy-b-20260926, whose D3 leg recorded the first on + rollback): b2_render.tf default 'on' @f35dfe003c, plan 0/1/0 (IRPT_EXPORT_RENDER off -> on), safe-apply 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.', readback on, replan exit 0. | CLOSED 20260926T173119Z |

## Log

- 20260926T171911Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260926T172648Z LEG F1 closed: TF @1ebb09b4c5 (export/b2_render.tf render_host_parameter_fence, name irpt-export-render-host-parameter-fence-policy aft
- 20260926T172649Z LEG N2 closed: LIVE (no candidate policy) iam_simulate_pairs: irpt-ycharts-runner-role fence pairs 7 of 7 met -- ssm:GetParameter + Del
- 20260926T173119Z LEG D3B closed: Export deploy (B) D3 back ON under this fence (cross-ref ledger irpt-export-deploy-b-20260926, whose D3 leg recorded the
- 20260926T173120Z CLOSED -- all 3 legs proven
