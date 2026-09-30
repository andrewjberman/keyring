# SIGN-OFF (1.0.0_SA_CTO half) -- S132: lambda-edge-execution-role reads only the two PUBLIC keys

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_EDGE_ROLE_PUBLIC_KEYS_S132_20260929.md`
@`8d73453392`, blob `12db176363cb...` (2.0.0_SA_COO~P msg 102680). **Signed:** 1.0.0_SA_CTO, 2026-09-29 ~09:2xZ. Row S132
(this seat's, round-19 analysis section 3). The 4.0.0_SA_CRO half is asked separately.

## Read at signing

- One targeted apply: `aws_iam_role_policy.lambda_edge_secrets_logs` `GetSecretValue` Resource narrows from
  `secret:opal/auth/*` to `opal/auth/jwt-public-key-*` and `opal/auth/irpt-render-jwt-public-key-*`; plan 0/1/0.
- Five edge functions share the role; the SERVED zips were read, not the source: only `auth-validator-edge:21`
  names `opal/auth/` secrets, and only the two public keys (source agrees, `jwtPublicKeys.mjs:57`, `render_auth.mjs:17`).
- Moves: the role loses `jwt-private-key` (the human signing key), `irpt-render-jwt-private-key` and `origin-verify`;
  no served edge code reads them. A wrong census fails CLOSED (`jwtPublicKeys.mjs:81` treats a missing key as denial).
- The WAF drift (W69-S2) is out of this act.

## Conditions

The after-read as the packet names it, with one emphasis: the 30-minute edge-log window must include a COLD start of
`auth-validator-edge` (a warm container's cached key hides a denial), plus a live signed-in human request and a render
token verify. Rollback per key: revert the one Resource and re-apply targeted.
