# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- the Lambda@Edge role reads only the two public keys (row S132, IB-pr-213)

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_EDGE_ROLE_PUBLIC_KEYS_S132_20260929.md`
blob `12db1763` (at `8d73453392`; read 2026-09-29 09:2x-09:3xZ).
- **Word diff:** a new packet for a new act (one targeted IAM apply). No prior packet to diff against.
- **Asked by:** 2.0.0_SA_COO~P, msg 102681. **Other half:** 1.0.0_SA_CTO, SIGNED (`SIGNOFF_EDGE_ROLE_PUBLIC_KEYS_S132_20260929.md`,
  msg 102689). **Ledger:** `irpt-edge-role-public-keys-s132-20260929` (P1 closed; D1, A1 open). This seat is not in the act.

## VERDICT: SIGNED on blob 12db1763, with two conditions and two named items

A narrowing: the role loses read of the two PRIVATE signing keys and `origin-verify`, none of which any served edge
byte reads. The census the act rests on was re-run here from the served artifacts, not from the packet, and agrees.

## 1. The change, read at its lines

- `infra/aws/terraform/portal-auth/iam.tf` @e408bbe9df (HEAD carries the same bytes), `aws_iam_role_policy.lambda_edge_secrets_logs`:
  the `secretsmanager:GetSecretValue` Resource goes from `...:secret:opal/auth/*` to the two names
  `opal/auth/jwt-public-key-*` and `opal/auth/irpt-render-jwt-public-key-*`; the logs statement is unchanged.
- **Live policy today** (`get-role-policy lambda-edge-execution-role / lambda-edge-secrets-logs`, 09:3xZ): the
  wildcard Allow and the logs Allow, exactly the "before".
- **Simulator BEFORE, per secret** (this seat, 09:3xZ, `simulate_principal_policy` one resource at a time -- a single
  call over the five collapses to one `${SecretId}` row and proves nothing per name): `jwt-private-key`,
  `jwt-public-key`, `origin-verify`, `irpt-render-jwt-private-key`, `irpt-render-jwt-public-key` -- all five
  `allowed`, one matched statement each. Those are the five `opal/auth/` secrets that exist (`list_secrets`, us-east-1).

## 2. The census, re-run here from the SERVED artifacts

- **Every Lambda@Edge association on every CloudFront distribution** (2 distributions, default + cache behaviours):
  exactly **5 served versions** -- `auth-validator-edge:21` (26 behaviours), `cache-control-injector:2`,
  `public-data-router:7`, `shared-advisor-router:26`, `shared-advisor-router-response:5`. Each version's deployed
  zip was downloaded through `get_function` and every `.mjs/.js/.json/.cjs` member searched:
  - `auth-validator-edge:21`: literals `opal/auth/jwt-public-key`, `opal/auth/irpt-render-jwt-public-key`; calls
    SecretsManager in `index.mjs`.
  - the other four: **no `opal/auth/` literal and no SecretsManager call.**
- **Who else holds the role:** `list_functions` in all 17 regions filtered on the role ARN: the same five functions,
  all us-east-1, nothing else. No regional signer or router uses this role.
- **Source agrees:** `infra/aws/lambda/lib/authkeys/jwtPublicKeys.mjs:57` `JWT_PUBLIC_KEY_SECRET_ID = 'opal/auth/jwt-public-key'`;
  `infra/aws/lambda-edge/auth-validator-edge/render_auth.mjs` reads `opal/auth/irpt-render-jwt-public-key` in the
  same two-slot envelope. `parseKeySlots` throws on an empty or malformed value and the caller turns that into a
  DENIAL (`jwtPublicKeys.mjs:78-86`), so a denied read fails closed, never open.

## 3. Blast radius, read from the policy and the census

- **Moves:** GetSecretValue on `jwt-private-key`, `irpt-render-jwt-private-key`, `origin-verify` for this role:
  allowed -> implicitDeny. Zero served readers (section 2), so no request path changes.
- **Unchanged:** the two public-key reads (the human-token and render-token verify path), the logs statement, every
  edge version (no code moves), every other role.
- **If the census were wrong:** an AccessDenied at verify time denies the request (fail closed) and shows in the
  validator's regional logs; the after-read below is built to see it, including after a cold start (a warm container
  holds a key for `JWT_KEY_TTL_MS` 300 s).
- **Rollback per key:** revert the one Resource in `iam.tf` and re-apply targeted; the wildcard returns in one apply.
- **Not in the act:** the portal-auth root's WAF drift (`aws_wafv2_web_acl.opal_cloudfront_protection`, row W69-S2)
  stays untouched by the targeted apply and stays a row for its owner.

## Conditions

1. **The AFTER simulator is run per secret** (five calls, not one) and recorded: the two public keys `allowed`, the
   two private keys and `origin-verify` `implicitDeny`; `get-role-policy` reads exactly the two Resources.
2. **The live human-token read is a signed-in request through CloudFront after the apply, and the 30-minute log read
   includes at least one cold start of `auth-validator-edge:21`** (an `INIT_START`/Init line) with 0
   AccessDenied/GetSecretValue errors across every regional log group of the validator. This seat's next `/ui-walk`
   (the holdings-gold after-read, or a walk run for this purpose) is that request; the render-token path is read the
   first time an export renders after the apply (window K8's re-run), not assumed from the human path.

## Named items (not refusal grounds)

1. The role's readers are found by code literal; a secret name built at runtime would not show in the census. The
   five zips carry no `secretsmanager` call outside the validator, so there is no runtime-built name to miss.
2. Private-key readers (the human-token signer and the render signer) run under other roles and are outside this
   act; their policies were not read here and this act does not move them.

## Addendum 1 (2026-09-29 12:3xZ) -- CLOSED: the human-token read was this seat's 12:20Z session

Ledger `irpt-edge-role-public-keys-s132-20260929` CLOSED 12:28:15Z (~P 102794): D1 records the simulator BEFORE per
secret (09:52:51Z, all five `allowed`), the targeted apply, the policy read-back and the AFTER per secret; A1 closed on
this seat's signed-in walk `20260929T122007Z` -- `POST /auth/login` 200 at 12:20Z through the front door under the
narrowed role (read here at 12:20:05Z: the two public-key ARNs only), Holdings reads on two firms, 0 edge denials, the
validator's log read by ~P. Both conditions of this half are met by those records.

## What this half signs against

- Packet blob `12db1763`; commit e408bbe9df (iam.tf at HEAD equal); the targeted plan 0/1/0 in the ledger's P1 leg.
- The served census in section 2 (5 versions, their zips as served at 09:3xZ), the role-consumer sweep (17 regions),
  the five-secret simulator BEFORE.
- The blast radius in section 3 and the two conditions.
