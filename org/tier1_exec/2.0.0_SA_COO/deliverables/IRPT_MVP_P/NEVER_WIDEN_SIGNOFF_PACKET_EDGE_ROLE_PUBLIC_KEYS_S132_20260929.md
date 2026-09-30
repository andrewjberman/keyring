# Never-widen sign-off packet -- the Lambda@Edge role reads only the two public keys (row S132)

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Author and operator:** `2.0.0_SA_COO~P`, 2026-09-29 ~09:0xZ.
**Ordered by:** 1.0.0_SA_CTO ROUND-19 ANALYSIS section 3 (S132 P2 to ~P, shared auth; "never-widen halves, a LIVE
before/after of the human-token path"). **Order:** TO-IB-pr-213, drained @e408bbe9df (P21-3-AC1 PASS). **Ledger:**
`irpt-edge-role-public-keys-s132-20260929` (P1 closed).

## 1. What ships -- one IAM statement, one root, targeted

`infra/aws/terraform/portal-auth/iam.tf`, `aws_iam_role_policy.lambda_edge_secrets_logs` (role
`lambda-edge-execution-role`): the `secretsmanager:GetSecretValue` Resource changes:
- before: `arn:aws:secretsmanager:us-east-1:313476888478:secret:opal/auth/*`
- after: `...:secret:opal/auth/jwt-public-key-*` and `...:secret:opal/auth/irpt-render-jwt-public-key-*`

The logs statement is unchanged. Apply: `.tools/safe-apply.sh apply -target=aws_iam_role_policy.lambda_edge_secrets_logs`.
The targeted plan is 0/1/0 (main tree, `.tools/terraform.exe`, 08:2xZ).

**Not in this act:** the portal-auth root carries pre-existing drift on
`aws_wafv2_web_acl.opal_cloudfront_protection` (row W69-S2, rule `known-bad-inputs` visibility config). The targeted
apply leaves it untouched, and it stays a row for its owner.

## 2. Who reads what -- the census the narrowing rests on

- **Sharing the role:** 5 Lambda@Edge functions: auth-validator-edge, cache-control-injector, public-data-router,
  shared-advisor-router, shared-advisor-router-response (list_functions, us-east-1, 66 versions).
- **SERVED bytes:** the versions every CloudFront distribution's behaviours associate, 5 in all, read from the
  deployed zips (not the source):

| served version | `opal/auth/<name>` literals in its code |
|---|---|
| auth-validator-edge:21 | `irpt-render-jwt-public-key`, `jwt-public-key` |
| cache-control-injector:2 | none |
| public-data-router:7 | none |
| shared-advisor-router:26 | none |
| shared-advisor-router-response:5 | none |

- **Source agrees:** `jwtPublicKeys.mjs:57` (`opal/auth/jwt-public-key`, imported by the validator's `index.mjs:78`)
  and `render_auth.mjs:17`. `origin-verify` appears in `index.mjs` only as a header value (`X-Origin-Verify`), never
  as a secret read.

## 3. Blast radius -- both branches

- **Moves:** the role can no longer read `opal/auth/jwt-private-key` (the HUMAN signing key),
  `opal/auth/irpt-render-jwt-private-key` (the render signing key) or `opal/auth/origin-verify`. No served edge code
  reads any of the three, per section 2, so no request path changes.
- **Unchanged:** reads of the two public keys by the validator, which is the human-token and render-token verify
  path; every other statement; the edge code (no version moves).
- **Failure mode if the census were wrong:** a verify-time GetSecretValue on a denied name raises AccessDenied in
  the edge. The validator treats a missing or malformed key as a DENIAL, not a pass (`jwtPublicKeys.mjs:81`), so the
  failure fails closed, and the after-read catches it.

## 4. Apply protocol

1. Both halves at HEAD naming this file's blob.
2. BEFORE (recorded 08:17:43Z; re-read at apply): the IAM policy simulator for the role on each `opal/auth` secret.
   All 5 read `allowed` today.
3. `.tools/safe-apply.sh apply -target=aws_iam_role_policy.lambda_edge_secrets_logs` (halt gate; HALT_ACK=1 only on 0
   STOP items).
4. Read back: `get-role-policy` shows exactly the two public-key Resources. `p21_3_live_after_read.py` PASS.
5. AFTER: the simulator. The two public keys read `allowed`; the two private keys and `origin-verify` read
   `implicitDeny`.
6. **The human-token path, live:** one real signed-in portal request through CloudFront after the apply answers as
   before (the CRO's next walk, or a ~D page read), and the validator's regional logs show 0
   AccessDenied/GetSecretValue errors over the first 30 minutes. A cached key in a warm container hides a denial
   until cold start, so the 30-minute read includes at least one cold start (Init line) of auth-validator-edge.
7. Re-plan the targeted resource: No changes.

**Rollback per key:** revert the Resource in `iam.tf` (e408bbe9df's one statement) and re-apply it targeted; the old
wildcard returns in one apply.

## What the halves sign against

This file's committed blob; e408bbe9df; the section 2 census; the targeted apply of section 4.
