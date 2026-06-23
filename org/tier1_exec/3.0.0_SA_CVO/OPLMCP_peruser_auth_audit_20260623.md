# NFRA_OPLMCP -- Per-user server-side auth AUDIT (CVO, Andrew-direct 2026-06-23)

**Author:** 3.0.0_SA_CVO | **Status:** BEGUN (kickoff: mechanism fully code-grounded; AWS-side + live-cert deepening open).
**Andrew's ask:** "how this server-side auth (in AWS rather than via MCP) works on a user-by-user basis" -- audit the per-user auth mechanism (how each user is authenticated AWS-side, not in the MCP protocol, and how their data is isolated user-by-user). Distinct-but-feeding the AC2 cert.
**Grounding:** Part 1 = SOURCE-CONFIRMED (gateway code file:line + the live wire). Part 2 findings = SOURCE-CONFIRMED code observations. Part 3 = the open verification items.

## 0. Project status (from COO, drive cycle-62, 2026-06-23)
OPLMCP.02 is at its FINAL gate. Done: AC1 (infra/in-repo/Terraform/EC2_MANIFEST), the .02 cutover (listener->authenticate-oidc, MOCK_GRAPH=0, ledger CLOSED, tag v1.2.0), AC3 impl (~B, the on-box knobs), AC5-go for the synthetic cert (CTO-granted). MOVING: .07 graph-onboarding + the mail-test (base-AE + ~B). The grounded-done (Andrew's personal ping) = CVO-AC2-PASS, which is legit-gated ONLY on Andrew/IT provisioning the synthetic test users (ESCALATED to Andrew -- outside-COO-power). So: one provisioning step from grounded-done.

## 1. THE MECHANISM -- how the per-user server-side auth works, end-to-end

The property is **a shared server, never a shared identity** (PRD S2). Authentication is done by the **AWS access layer, NOT the MCP protocol** -- exactly Andrew's framing. The per-user flow:

- **Step 0 -- connect (NOT auth):** the user's Claude (MCP client) connects to `https://mcp.opalinvest.dev/mcp`. The MCP protocol itself carries NO user auth -- the AWS layer in front does it.
- **Step 1 -- AWS ALB `authenticate-oidc` (App-1 "Login" Entra app):** the HTTPS listener's default action authenticates against Entra. Unauthenticated -> 302 -> Entra login [SOURCE-CONFIRMED live: client_id 53360468, scope=openid profile email, redirect /oauth2/idpresponse, AWSALBAuthNonce cookie]. The user logs in **as themselves**. On success the ALB sets `AWSELBAuthSessionCookie` and forwards to the EC2 target with a **signed `x-amzn-oidc-data` JWT** (signed with the regional ELB key).
- **Step 2 -- gateway GuardMiddleware (pure-ASGI; server.py:41-62) on /mcp + /login:**
  - `get_user_email` -> `_alb_oidc_identity` (identity.py:50-69): **VERIFIES the `x-amzn-oidc-data` ES256 signature against the regional ELB public key** (`public-keys.auth.elb.{region}.amazonaws.com/{kid}`), then extracts the email claim. This is the anti-forgery linchpin: a direct-to-box hit bypassing the ALB cannot forge identity (no ELB private key).
  - `enforce(email)` (blocklist.py:41-46): global KILL_SWITCH (file presence) + per-user blocklist (hot-reloaded file) -> 403 if denied.
  - `set_current_email(email)` (context.py): the verified email -> a **contextvar** (pure-ASGI so it propagates IN-TASK to the tool; BaseHTTPMiddleware would drop it -> identity bleed across concurrent requests -- the S2.7 invariant).
- **Step 3 -- per-user delegated token (token_broker.py):** the tool reads `get_current_email()` -> `get_token(email)`: loads THAT user's MSAL token cache (keyed **sha256(email)**, **Fernet-encrypted at rest**, 0o600), silently refreshes the user's **delegated** token; `NeedsLogin` if absent (one-time `/login` Microsoft consent -> `/callback` `redeem_code` writes the token into THAT email's cache; the OAuth state is Fernet-encrypted + 600s-TTL, carrying the email). The gateway **never holds an app-only/tenant-wide token.**
- **Step 4 -- Graph call (graph.py):** `call(token, ...)` sends the user's delegated token as Bearer -> **Microsoft Graph enforces that user's own permissions.** `/me/messages` returns only their mail. Cross-user access is impossible by construction (it is the user's own delegated token).

### The 5 per-user isolation layers (defense-in-depth)
1. **ALB OIDC** -- each user authenticates as themselves at Entra (AWS-side). No shared login.
2. **Signature-verify + SG-lock** -- ES256 verify of x-amzn-oidc-data (no forgery) + EC2 :8080 ingress SG-locked to the ALB SG (box unreachable except via the ALB).
3. **Pure-ASGI contextvar** -- per-request identity, concurrency-safe (no cross-request identity bleed).
4. **Per-user encrypted token cache** -- each user's own delegated token (Fernet, sha256(email)-keyed, 0o600); no app-only/shared token.
5. **Microsoft Graph per-user enforcement** -- the delegated token scopes every call; cross-user is rejected by Graph itself.

## 2. AUDIT FINDINGS (initial -- all SOURCE-CONFIRMED code observations)
- **F0 (POSITIVE, load-bearing):** the core per-user-scope is architecturally SOUND -- signature-verified identity + per-user delegated token + Graph enforcement = cross-user READ is impossible by construction; there is no app-only/tenant-wide path. The "shared server, never shared identity" stance holds at every layer.
- **F1 (LOW): `verify_aud=False`** (identity.py:62) -- the ALB-OIDC token audience is not checked. Mitigated by the ES256 signature (regional ELB key) + SG-lock. Residual: a token from another ALB in the same region/account would verify if it reached the box (the SG-lock prevents reach). Rec: document the rationale; bind issuer/aud if feasible.
- **F2 (MEDIUM, config-guard): the dev `header` identity provider** (identity.py:111-116, trusts `X-User-Email`) is a TOTAL per-user-scope bypass if `IDENTITY_PROVIDER=header` on a non-mock prod box. Live is `alb_oidc` [SOURCE-CONFIRMED .env], but NOTHING prevents header-mode at startup. Rec: a fail-closed startup assertion -- refuse to boot if `IDENTITY_PROVIDER=header` and not `MOCK_GRAPH`.
- **F3 (TRACKED = AC6): the Verified-Access provider** (identity.py:83-100) decodes UNVERIFIED (`verify_signature=False`, marked TODO). NOT active (alb_oidc). Risk only if VA is enabled without the signature-verify. AC6 (PRD S8) gates implement-or-waive.
- **F4 (INHERENT, document + harden): Fernet single-key blast-radius** -- all per-user token caches are encrypted with one FERNET_KEY (Secrets Manager, on-box). A box/key compromise exposes ALL users' delegated refresh tokens. Inherent to a delegated gateway; mitigated (SM not repo/image, 0o600, SG-lock, no app-only token). Rec: treat the box as the crown-jewel target; per-user revoke (cache delete) + key rotation + short TTLs.
- **F5 (LOW edge): consent-account divergence** -- `/callback` writes the redeemed token into the cache keyed by the **ALB-identity** email (the state), but the Microsoft auth-code is for whatever account the user picks at consent (`prompt=select_account`). A user could consent a DIFFERENT Microsoft account they control into their own gateway-identity cache. NOT a cross-user read of a non-consenting user (the token is delegated to whoever authed). Rec: at `/callback`, cross-check the redeemed token's UPN against the state email; reject mismatch.
- **F6 (VERIFY-LIVE = AC2 concurrency): contextvar concurrency-isolation** -- the pure-ASGI contextvar is the no-bleed guarantee. The AC2 cert's concurrency test verifies LIVE that concurrent A+B requests never cross identities (response or audit). Design SOUND; empirical proof rides the AC2 cert.

## 3. OPEN ITEMS / audit plan (to complete)
- **AWS-side deepening (comp-aws / comp-iam):** the ALB `authenticate-oidc` listener config (OIDC endpoints, session timeout/refresh), the SG ingress (source-SG, not CIDR), the gateway IAM (secrets-read scoped to the 2 ARNs + S3 artifact prefix). Confirms the AWS-side of the mechanism beyond the live 302 + .env grep.
- **Live AC2 cert (the empirical proof):** own-mail (A sees A) + cross-user isolation (A cannot reach B) + concurrency no-bleed, on the synthetic users -- F6's live proof + F0's empirical confirmation.
- **Disposition F2 + F5 recommendations** (the fail-closed header guard + the /callback UPN-check) -> CTO/AE if accepted (hardening, non-blocking for v1).
- The audit completes alongside the AC2 cert (the live run grounds F0/F6 to behavior).

## 4. Net (kickoff)
The per-user server-side auth model is architecturally SOUND (F0) -- AWS-layer authentication (not MCP), signature-verified identity, per-user delegated tokens, Graph-enforced isolation, defense-in-depth across 5 layers. Initial findings are hardening items (F2/F4/F5) + a tracked TODO (F3 = AC6) + the live proof (F6 = AC2), none contradicting the core model. Next: the AWS-side comp-aws/comp-iam grounding + the live AC2 cert.
