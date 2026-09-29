# Deploy Completion Record
**Date opened:** 2026-09-29T08:22:09.693501+00:00
**Status:** OPEN
**Deploy:** S132: the Lambda@Edge role (lambda-edge-execution-role, lambda-edge-secrets-logs) reads only the two public keys -- targeted apply in portal-auth (IB-pr-213 @e408bbe9df); WAF drift in the same root left untouched (W69-S2)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | targeted plan | -target=aws_iam_role_policy.lambda_edge_secrets_logs: 0/1/0, Resource opal/auth/* -> the two public-key ARNs | Main tree, .tools/terraform.exe (the W69-S1 substitute not used here), 08:2xZ: plan -target=aws_iam_role_policy.lambda_edge_secrets_logs -lock=false: Plan 0/1/0, Resource arn:...:secret:opal/auth/* -> [opal/auth/jwt-public-key-*, opal/auth/irpt-render-jwt-public-key-*], nothing else. The untargeted root also carries pre-existing WAF drift (aws_wafv2_web_acl.opal_cloudfront_protection, row W69-S2), deliberately NOT in this act. | CLOSED 20260929T082301Z |
| D1 | activation | targeted safe-apply | halves at HEAD; simulator BEFORE; safe-apply -target; readback policy; simulator AFTER; edge logs 0 AccessDenied; re-plan targeted 0 |  | OPEN |
| A1 | verify | the human-token path | a real signed-in portal request through CloudFront after apply answers as before (no 5xx/deny from the edge) |  | OPEN |

## Log

- 20260929T082209Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260929T082301Z LEG P1 closed: Main tree, .tools/terraform.exe (the W69-S1 substitute not used here), 08:2xZ: plan -target=aws_iam_role_policy.lambda_e
