# OPLMCP OTP-fetch gateway endpoint -- build plan (0.7.0_AE_CloudOps)

**Dispatch:** COO 205432Z (build) + 205509Z (token namespace). CTO owns the m365-delegated/token arch
(coordinate before build). 0.6.0 = consumer (box side, 7d45b85a1). Durable path, NO deadline.

## What it is
A thin Bearer-auth'd REST endpoint ON THE EXISTING m365-mcp-gateway (mcp.opalinvest.dev) that the
bd-49f-auto-login box POSTs to during a BD login, to fetch the 6-digit OTP from Andrew's mailbox via
the gateway's already-held Andrew-delegated Graph token, returning ONLY the code.

## Grounding (read, not assumed)
- The gateway EXISTS + is production (infra/aws/ec2/m365-mcp-gateway/app/, ALB+OIDC, t4g.nano, uvicorn
  :8080, AutoShutdown=disabled). I built OPLMCP.01/.02/.03/.07.
- DIRECT PRECEDENT: `/teams/poll` (server.py:309) -- a Bearer-gated plain-JSON REST endpoint that does
  a per-user Graph read for the teams-watch monitor. The OTP endpoint is the same shape with 2 deltas.
- `token_broker.get_token(email)` (token_broker.py:73) already does MSAL `acquire_token_silent` ->
  silent refresh from the per-user encrypted (Fernet) cache; raises NeedsLogin if no usable token.
  So "auto-refresh Andrew's token" is MSAL-NATIVE + already working -- the NEW bit is the liveness probe.
- `graph.call(token, "GET", "/me/messages", params=...)` (graph.py:22) is the mail primitive;
  `list_recent_email`/`search_email` (tools.py) show the exact $filter/$search/$select usage.

## Design (mirrors /teams/poll; 2 deltas)
1. **Route**: `POST /otp/fetch` added to server.py routes. GuardMiddleware only guards /mcp + /login,
   so /otp/fetch passes to its own handler which enforces ITS OWN gate (like the OAuth endpoints).
2. **Auth = STATIC shared bearer** (delta 1): handler loads the box->gateway token from SM
   (blackdiamond/49f/otp-gateway-token, COO-settled namespace) and constant-time-compares it to the
   presented `Authorization: Bearer`. 401 on mismatch. (NOT the per-user OAuth JWT -- the box is a
   machine, not a user.)
3. **Identity = FIXED Andrew mailbox** (delta 2): `email = OTP_MAILBOX` (config) ->
   `token = token_broker.get_token(OTP_MAILBOX)` (Andrew's persisted delegated cache, silent-refresh).
   NeedsLogin -> 503 {"needs_login":true} + fire the liveness alert (Andrew must re-auth).
4. **Search**: body {sender, subject, since, pattern}. `graph.call(token,"GET","/me/messages",
   params={"$filter":"receivedDateTime ge {since}","$orderby":"receivedDateTime desc","$top":10,
   "$select":"subject,from,receivedDateTime,body"})` then in-handler filter by sender (+ subject
   contains) and regex the newest match's body with `pattern` (default `Authorization code:\s*(\d{6})`).
5. **Return ONLY the code** (ROE): `{"code":"NNNNNN"}` -- NOTHING else (no subject/sender/body echoed).
   404-style {"code":null,"found":false} if no match in window. Read-only (no message mutation).

## Infra deltas (my lane)
- **Secret**: provision `blackdiamond/49f/otp-gateway-token` (random 32B bearer) in SM.
- **Gateway IAM**: add `secretsmanager:GetSecretValue` on that ARN to m365-mcp-gateway-role (it reads
  App secrets + Fernet today; add the OTP bearer). Box role already covers it via 49f/* (no box change).
- **ALB**: add a listener rule for `/otp/*` forwarding to the gateway target group WITHOUT
  authenticate-oidc (mirror the existing /teams/poll rule in alb.tf).
- **Config (.env)**: OTP_MAILBOX, OTP_BEARER_SECRET_ID=blackdiamond/49f/otp-gateway-token.
- **Deploy**: code via safe-ec2-deploy.sh (S3-artifact, Rules 7-12); TF via safe-apply; deploy-completion
  ledger; CVO certs the realized IAM + the return-only-code ROE.

## CTO reliability rider -> liveness probe (my plan; CTO to concur)
- `GET /otp/health` (static-bearer or internal): does `get_token(OTP_MAILBOX)` -> {"ok":true} or
  {"needs_login":true}. EventBridge schedule (e.g. every 6h) -> tiny probe -> if needs_login, publish to
  opal-critical-surface-alerts (the SNS topic my egress-check limb already watches for deliverability).
  So a lapsed Andrew-refresh is caught + alerted BEFORE a BD login needs the OTP -- no silent SPOF.
- Reuses the watch-the-watcher pattern (critical-alarm-egress.yaml / comp-surface-check egress-check).

## CTO coordination questions (the arch-GO gate -- CTO owns this design)
1. **AUTH MODEL = the pivotal decision** (CVO 205801Z + 0.5.0 grounding sharpened it). Two models:
   (A) STATIC shared bearer (blackdiamond/49f/otp-gateway-token), validated in-handler -- simple, but a
       new bespoke auth path on the gateway.
   (B) GATEWAY OAUTH CLIENT: the box is a registered client holding a gateway REFRESH-TOKEN (stateless
       RS256 JWT, sub=andrew@opalinvest.com, per 0.5.0's grounding). It exchanges it at /token for a
       gateway access token, then calls /otp/fetch with the EXISTING per-user Bearer guard (_bearer_email
       -> email=andrew -> get_token(andrew)). Reuses ALL the existing auth + no static-bearer code; the
       "fixed mailbox" becomes the token's own sub. Cleaner -- BUT a sub=andrew token can hit /mcp +
       /teams/poll too, so it needs SCOPE/audience restriction to OTP-only (a gateway scope the box's
       token carries + /otp/fetch requires). CVO/0.5.0 lean (B). CTO: which model, and if (B) the scoping?
   (Everything below assumes the model you pick; the rest of the design is model-agnostic.)
2. OTP_MAILBOX = andrew@opalinvest.com? (The BD OTP lands in Andrew's mailbox -- you proved it.) Confirm
   his delegated cache is the one on the gateway box.
3. Liveness design: concur with /otp/health + EventBridge + SNS(opal-critical-surface-alerts)? Or a
   different probe you prefer?
4. ROE: return-only-{code}, read-only, no echo -- confirm sufficient.
5. Scope: land on the EXISTING gateway (reuse the token cache) -- confirm (vs a separate service).

## Sequence (on CTO arch-GO)
code (server.py /otp/fetch + /otp/health + graph helper + config) -> deploy-vendor -> safe-ec2-deploy
to the gateway -> secret + IAM via safe-apply -> ALB rule -> verify (curl with the bearer, live OTP read
dry-run) -> ledger close -> hand 0.6.0 the URL (https://mcp.opalinvest.dev/otp/fetch) + secret-id ->
CVO cert. NOT tonight-urgent.
