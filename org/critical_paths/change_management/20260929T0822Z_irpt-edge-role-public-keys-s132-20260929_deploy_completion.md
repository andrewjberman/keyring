# Deploy Completion Record
**Date opened:** 2026-09-29T08:22:09.693501+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260929T122815Z
**Deploy:** S132: the Lambda@Edge role (lambda-edge-execution-role, lambda-edge-secrets-logs) reads only the two public keys -- targeted apply in portal-auth (IB-pr-213 @e408bbe9df); WAF drift in the same root left untouched (W69-S2)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | targeted plan | -target=aws_iam_role_policy.lambda_edge_secrets_logs: 0/1/0, Resource opal/auth/* -> the two public-key ARNs | Main tree, .tools/terraform.exe (the W69-S1 substitute not used here), 08:2xZ: plan -target=aws_iam_role_policy.lambda_edge_secrets_logs -lock=false: Plan 0/1/0, Resource arn:...:secret:opal/auth/* -> [opal/auth/jwt-public-key-*, opal/auth/irpt-render-jwt-public-key-*], nothing else. The untargeted root also carries pre-existing WAF drift (aws_wafv2_web_acl.opal_cloudfront_protection, row W69-S2), deliberately NOT in this act. | CLOSED 20260929T082301Z |
| D1 | activation | targeted safe-apply | halves at HEAD; simulator BEFORE; safe-apply -target; readback policy; simulator AFTER; edge logs 0 AccessDenied; re-plan targeted 0 | Both halves at HEAD naming blob 12db1763: CTO 3911da0867 (102687), CRO @c88e9e5713 (102695, two conditions). Simulator BEFORE per secret 09:52:51Z: all 5 opal/auth secrets allowed. safe-apply -target=aws_iam_role_policy.lambda_edge_secrets_logs (halt gate 28 routine DEV-freeze pairs, 0 STOP, HALT_ACK=1) rc 0 at ~10:01Z: 0 added, 1 changed, 0 destroyed. READBACK live get-role-policy: GetSecretValue Resources = [opal/auth/jwt-public-key-*, opal/auth/irpt-render-jwt-public-key-*] (p21_3_live_after_read.py P21-3-AC1 PASS). Simulator AFTER per secret (five calls) 10:02:30Z: jwt-public-key allowed, irpt-render-jwt-public-key allowed, jwt-private-key implicitDeny, irpt-render-jwt-private-key implicitDeny, origin-verify implicitDeny. Targeted re-plan: No changes (detailed-exitcode 0). The WAF drift (W69-S2) untouched. W69-S1 disarmed: the apply ran from the main tree with .tools/terraform.exe. Rollback: revert iam.tf's statement (e408bbe9df) + targeted re-apply. | CLOSED 20260929T100339Z |
| A1 | verify | the human-token path | a real signed-in portal request through CloudFront after apply answers as before (no 5xx/deny from the edge) | Human-token path LIVE under the narrowed role: 4.0.0_SA_CRO signed-in walk 20260929T122007Z (msg 102790) -- POST /auth/login 200 at 12:20Z through the front door, Holdings read on 49F ..0090 and INF ..4944, 0 edge denials seen by the page; role GetSecretValue Resource = the two public-key ARNs only. auth-validator-edge regional logs (/aws/lambda/us-east-1.auth-validator-edge; us-east-1 366 events, us-east-2/us-west-2/us-west-1 0) 12:00-12:35Z: 90 requests, 6 cold starts (Init) at 12:20:22Z, 0 AccessDenied / GetSecretValue errors. | CLOSED 20260929T122815Z |

## Log

- 20260929T082209Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260929T082301Z LEG P1 closed: Main tree, .tools/terraform.exe (the W69-S1 substitute not used here), 08:2xZ: plan -target=aws_iam_role_policy.lambda_e
- 20260929T100339Z LEG D1 closed: Both halves at HEAD naming blob 12db1763: CTO 3911da0867 (102687), CRO @c88e9e5713 (102695, two conditions). Simulator B
- 20260929T122815Z LEG A1 closed: Human-token path LIVE under the narrowed role: 4.0.0_SA_CRO signed-in walk 20260929T122007Z (msg 102790) -- POST /auth/l
- 20260929T122815Z CLOSED -- all 3 legs proven
