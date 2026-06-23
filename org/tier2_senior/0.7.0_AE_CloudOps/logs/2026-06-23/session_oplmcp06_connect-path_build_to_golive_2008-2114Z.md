# Session: OPLMCP.06 connect-path -- Model-B OAuth-AS build + go-live cutover (0.7.0_AE_CloudOps~B)
**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DEPLOY, DIAGNOSE

## Summary
Built and went LIVE with the OPLMCP.06 connect-path: the m365-mcp-gateway is now its own OAuth 2.1
authorization-server facade (Model-B), so Claude Code's remote-MCP client can connect. `/mcp` now
returns `401 + WWW-Authenticate: Bearer resource_metadata=...` (the no-popup fix) instead of a
302-to-Entra. Full build (~800 LOC), CTO architecture-gated at 3 checkpoints, atomic split-apply
cutover under a deploy-completion ledger, live-verified end-to-end through the ALB. Two in-window
catches handled clean (auto-shutdown whitelist; deploy stale-process bug). Andrew connect-ready.

## Work done
- **G0 grounding:** read the gateway app (server/identity/token_broker/config/tools/blocklist/
  context) + alb.tf + deploy-to-ec2.sh vs the committed brief. Confirmed reuse points: token_broker
  = the App-2 delegated MSAL/Graph leg; GuardMiddleware = the /mcp Bearer-flip point.
- **GATE-3 design checkpoint -> CTO:** 6 decisions (App-2 bridge; /callback dual-flow state-branch;
  RS256 new-key-secret; aud pin; in-mem single-worker stores; broader ALB bypass path-set). CTO
  CONFIRMED all 6 + conditions; folded in.
- **Build (commit 63e61ca77, ds-gate clean, 31/31 standalone logic tests pass):**
  - `app/oauth_as.py` (NEW): RS256 issue/validate of the gateway's OWN tokens (aud strict =
    `https://mcp.opalinvest.dev/mcp`); JWKS; PKCE S256-only; DCR-facade (loopback-only); in-mem
    code/PKCE/pending stores (single-use 60s codes, PKCE+redirect+identity-bound); AS metadata docs.
  - `app/server.py`: AS routes (/.well-known/{oauth-protected-resource,oauth-authorization-server,
    jwks.json}, /register, /authorize, /token) + /callback dual-flow branch + GuardMiddleware
    per-path flip (/mcp=gateway-Bearer 401+WWW-Authenticate, /login=access-layer-header) + boot-
    refuse-if-workers>1.
  - `app/token_broker.py`: `redeem_code_for_email` (bridge learns email from id_token) + Fernet
    blob helpers. `app/config.py`: issuer/mcp_resource_url/gateway_scopes + RS256 key (file/inline) + TTLs.
  - Infra (terraform validate clean): `alb.tf` 2 precise listener rules; `secrets-iam.tf` 4th-secret
    grant; `deploy-to-ec2.sh` JWT-key + .env wiring; systemd `--workers 1`.
- **Deploy (CTO DEPLOY-GO 204811Z, split-apply ordering):** S1 create JWT-key secret (boto3, kid
  ac4c49e6c8bec6d4) -> ledger OPEN -> APPLY-A (grant, 1 change) -> code-deploy -> on-box /mcp->401
  HARD GATE -> APPLY-B (2 rules) -> S5 live-through-ALB VERIFIED -> ledger CLOSED 4/4 -> tag v1.3.0.

## Deployment Sequence + Verification (AE)
| step | action | result |
|---|---|---|
| S1 | create secret opal/mcp/m365-gateway-jwt (RSA-2048 PKCS8 PEM, boto3) | CREATED ...-lKbCyS, kid ac4c49e6c8bec6d4 |
| APPLY-A | safe-apply -target=aws_iam_role_policy.gw_golive | `0 added, 1 changed, 0 destroyed`; live policy = 4 ARNs |
| S4 | safe-ec2-deploy (S3->SSM, restart) | ssm:bc1bdf1c Success; on-box: active / health 200 / `OK: AS metadata serves` / `/mcp unauth -> 401` |
| APPLY-B | safe-apply -target=2 listener rules | `2 added, 0 changed, 0 destroyed` (pri 10/20) |
| S5 | curl live https://mcp.opalinvest.dev | /mcp->401+WWW-Authenticate; /.well-known/*->200; jwks kid==ac4c49e6c8bec6d4; /authorize->307 Entra App-2; / root->302 ALB-OIDC; plan 0-diff |
| S6 | tag + push --follow-tags | m365-mcp-gateway-v1.3.0 pushed |

## Compiler Tools
| tool | run | result | note |
|---|---|---|---|
| comp-which | "what is the m365-mcp-gateway ALB listener doing" | ran comp-grep fallback | surfaced the .02 ledger; gateway not graph-modeled (that IS .07) so no rich tool fits |
| comp-iam / comp-aws / comp-blast | (not run on the gateway) | N/A | `comp-iam service m365-mcp-gateway` returns "no service matching" -- the gateway is NOT on the comp-* graph until OPLMCP.07. So IAM/blast/aws graph tools cannot model it yet. |

**What worked:** comp-which routed to the on-rails comp-grep and surfaced the .02 ledger (live-state
corroboration). ds-commit-gate clean on all .py.
**What failed / gap:** the gateway is not graph-backed until OPLMCP.07, so comp-iam (the AE minimum
after an iam.tf change), comp-aws, comp-blast all return no-match for it. Per the comp-rail governing
principle (mandatory IFF an associated graph backs the target), the live ALB-listener / IAM-policy /
SSM inspections were raw-aws with inline `# rail-checked:` markers (no graph + mutable live state +
the never-trust pre/post-deploy ground-truth). OPLMCP.07 closes this gap (brings the gateway onto the graph).

## Two in-window catches (DIAGNOSE)
1. **ec2-auto-shutdown-enforcer stopped the box 13s after the first deploy** (3.0h idle-ceiling kill,
   idle because nobody had connected). Andrew-direct whitelist: `AutoShutdown=disabled` tag (the
   enforcer's ONLY exemption) applied live + durable in main.tf (e4d16d432). Supersedes the 2026-06-05
   universal zero-exemptions for THIS always-on service.
2. **First on-box smoke's AS-doc curl 404'd** -> root cause: `systemctl enable --now` is a NO-OP on an
   already-running service, so the OLD .02 process kept serving stale code (on-disk md5 passed while
   the RUNNING process was stale -- the never-trust-the-file lesson). Fixed to `restart` (e4d16d432);
   redeploy proved new code serves (AS 200 + /mcp 401). The on-box HARD GATE caught it before APPLY-B.

## Blockers
None. (G4 = CVO independent entry-point re-verify is in-flight + Andrew's own connect test -- both
event-driven, not blocked.)

## Current State (zero-context handoff)
- **LIVE:** m365-mcp-gateway is the OAuth-AS at `https://mcp.opalinvest.dev`. `/mcp` = gateway Bearer
  (401+WWW-Authenticate). Discovery + DCR + PKCE authorize/token + Entra App-2 bridge + RS256
  own-tokens all live + verified. Instance i-07dccb1615503ac99 (t4g.nano), whitelisted always-on.
- **Auth model:** /mcp = gateway-issued RS256 Bearer (kid ac4c49e6c8bec6d4, aud=https://mcp.opalinvest.dev/mcp,
  iss=https://mcp.opalinvest.dev, scope=mcp). /login + GUI + everything-else still ALB-OIDC (App-1,
  tenant 6810043e). Bypass rules: pri10 [/mcp,/mcp/*,/authorize,/token,/register] + pri20 [/callback,
  3x /.well-known] forward-no-OIDC.
- **Secrets:** opal/mcp/m365-gateway-jwt (RSA private PEM) read on-box -> /opt/m365-mcp-gateway/.jwt_key.pem
  (chmod 600); .env has GATEWAY_JWT_PRIVATE_KEY_FILE + GATEWAY_WORKERS=1.
- **Commits:** 63e61ca77 (build), e4d16d432 (restart-fix + whitelist), 3dbef84e4 (manifest), 5c5049f13
  (ledgers). Tag m365-mcp-gateway-v1.3.0. Ledger 20260623T2049Z_oplmcp06-connect-path CLOSED 4/4.
- **Code modules + line refs:** oauth_as.py (issue/validate/PKCE/stores/metadata), server.py
  (routes + GuardMiddleware), token_broker.py (redeem_code_for_email + encrypt/decrypt_blob).

## Next Steps
- **[3.0.0_SA_CVO]** independent entry-point re-verify (REQUESTED): unauth /mcp->401+WWW-Authenticate,
  /.well-known->200 metadata-only, jwks kid==ac4c49e6c8bec6d4, full-JWT-validation (aud/alg/exp),
  /authorize->Entra-bridge, path-precision (/mcpfoo NOT bypassed), per-user isolation. RAVC verdict.
- **[Andrew]** connect test: `claude mcp add --transport http m365 https://mcp.opalinvest.dev/mcp` ->
  /mcp authenticate -> Entra login -> "list my recent emails" = the e2e proof.
- **[2.0.0_SA_COO / 1.0.0_SA_CTO]** project-level close of .06 after CVO verdict + Andrew-connect;
  relay done to MSTR. COO holds the formal Andrew-connect-ping until CVO's verdict.
- **[0.7.0_AE_CloudOps]** OPLMCP.07 graph-onboarding (queued) closes the comp-tool coverage gap above.
