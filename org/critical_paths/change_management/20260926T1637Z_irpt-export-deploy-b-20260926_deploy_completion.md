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
| A0 | verify | synthetic human-read arm | deploy_b_human_arm.py before D1 == after D2 (49F/COT/INF incl. INF unarmed): status, ok, state, reason, sections identical; a difference = STOP + rollback reverse |  | OPEN |
| D2 | activation | performance root | plan exactly 1 add (render-grant read policy) / 1 change (code + env IRPT_EVIDENCE_BUCKET) / 0 destroy; safe-apply; CodeSha256 == artifact; replan No changes |  | OPEN |
| D3 | activation | export root export_render=on | plan 0/1/0 env only; safe-apply; readback IRPT_EXPORT_RENDER=on; replan No changes |  | OPEN |
| N1 | verify | negative arm (CTO 101013) | another attempt's token NAME refused to the host role; read after delete ParameterNotFound |  | OPEN |
| R1 | verify | AFTER read (step-6 window) | K6's account acc_bf96.. YTD == 0.06854 (else STOP + rollback); >= 30 s is a BLOCKING row on FWD-1 (S147), not a rollback |  | OPEN |
| irpt-performance-adapter | tf-lambda | module.irpt_performance_adapter.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20260926T163719Z OPENED by 2.0.0_SA_COO~P with 6 leg(s)
