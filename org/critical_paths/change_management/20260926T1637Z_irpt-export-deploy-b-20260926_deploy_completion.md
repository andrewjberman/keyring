# Deploy Completion Record
**Date opened:** 2026-09-26T16:37:19.327805+00:00
**Status:** OPEN
**Deploy:** Export deploy (B) per packet v2 a40cad5a (CTO + CRO halves): D1 adapter code (render ports + S143 Orion household + S147 S3 pool), D2 render_grant.tf + IRPT_EVIDENCE_BUCKET, D3 export_render=on; rollback reverse (D3, D2, D1)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A0 | verify | synthetic human-read arm | deploy_b_human_arm.py before D1 == after D2 (49F/COT/INF incl. INF unarmed): status, ok, state, reason, sections identical; a difference = STOP + rollback reverse | deploy_b_human_arm.py (fresh selection through the real route, the edge's trusted headers): BEFORE (pre-D1) and AFTER D2 -> COMPARE 3 firms IDENTICAL: 49F ok:false OBJECT_NOT_COVERED (synthetic subject, ReportDenied), COT DEPENDENCY_UNAVAILABLE, INF DEPENDENCY_UNAVAILABLE (plan b spent = unarmed); receipts DEPLOY_B_ARM_BEFORE_20260926.json / DEPLOY_B_ARM_AFTER_D2_20260926.json | CLOSED 20260926T165501Z |
| D2 | activation | performance root | plan exactly 1 add (render-grant read policy) / 1 change (code + env IRPT_EVIDENCE_BUCKET) / 0 destroy; safe-apply; CodeSha256 == artifact; replan No changes | D1 artifact Zs2OK7C5.. (publish, 69 members, dev tools absent, import differential 0 new); plan 1 add (irpt-performance-render-grant-read-policy) / 1 change (source_code_hash jbojcl -> Zs2OK7C5, s3_object_version, env + IRPT_EVIDENCE_BUCKET) / 0 destroy with the live plan values as vars; safe-apply 'Apply complete! Resources: 1 added, 1 changed, 0 destroyed.'; readback CodeSha256 Zs2OK7C5.. Active/Successful, IRPT_EVIDENCE_BUCKET set, plan sha 01209afb kept, 9 env keys; replan exit 0 | CLOSED 20260926T165502Z |
| D3 | activation | export root export_render=on | plan 0/1/0 env only; safe-apply; readback IRPT_EXPORT_RENDER=on; replan No changes | APPLIED then ROLLED BACK. On: b2_render.tf default 'on' @30bd11bd38, plan 0/1/0, safe-apply, readback IRPT_EXPORT_RENDER=on, replan No changes. N1 then FAILED (below), so D3 was reversed the same turn: default 'off' @7d7fa146e6, plan 0/1/0 (on -> off), safe-apply 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.', readback IRPT_EXPORT_RENDER=off, replan exit 0. While on: 0 /irpt/render-token/* names existed and 0 irpt-export-render events -- no token was ever minted. Served state = D1+D2 live, render OFF. | CLOSED 20260926T170715Z |
| N1 | verify | negative arm (CTO 101013) | another attempt's token NAME refused to the host role; read after delete ParameterNotFound | FAILED (the reason D3 is rolled back). iam_simulate_pairs.py: irpt-export-render-role 4 of 4 met (Put+Delete on /irpt/render-token/*, no Get, no human JWT key). irpt-ycharts-runner-role (the render host, export/iam.tf:192) 3 of 5 met: ssm:GetParameter ALLOWED on /opal/other and /irpt/walk-principal/x/password, via the AWS-managed AmazonSSMManagedInstanceCore attached to that shared host role -- so the host could read ANOTHER attempt's token, against CTO ruling (a) 101013 ('host role Get + Delete on the prefix, nothing else of Parameter Store'). Row IRPT_BCKEND-S148. | CLOSED 20260926T170715Z |
| R1 | verify | AFTER read (step-6 window) | K6's account acc_bf96.. YTD == 0.06854 (else STOP + rollback); >= 30 s is a BLOCKING row on FWD-1 (S147), not a rollback |  | OPEN |
| irpt-performance-adapter | tf-lambda | module.irpt_performance_adapter.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | same as D2: code Zs2OK7C5.. served == built artifact; replan No changes | CLOSED 20260926T165502Z |

## Log

- 20260926T163719Z OPENED by 2.0.0_SA_COO~P with 6 leg(s)
- 20260926T165501Z LEG A0 closed: deploy_b_human_arm.py (fresh selection through the real route, the edge's trusted headers): BEFORE (pre-D1) and AFTER D2
- 20260926T165502Z LEG D2 closed: D1 artifact Zs2OK7C5.. (publish, 69 members, dev tools absent, import differential 0 new); plan 1 add (irpt-performance-
- 20260926T165502Z LEG irpt-performance-adapter closed: same as D2: code Zs2OK7C5.. served == built artifact; replan No changes
- 20260926T170715Z LEG D3 closed: APPLIED then ROLLED BACK. On: b2_render.tf default 'on' @30bd11bd38, plan 0/1/0, safe-apply, readback IRPT_EXPORT_RENDER
- 20260926T170715Z LEG N1 closed: FAILED (the reason D3 is rolled back). iam_simulate_pairs.py: irpt-export-render-role 4 of 4 met (Put+Delete on /irpt/re
