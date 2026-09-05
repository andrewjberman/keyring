# Platform Attack-Surface Assessment -- opalinvest.dev portal, opal-gateway MCP, opalinvest.com website

| | |
|---|---|
| **Date** | 2026-09-02 |
| **Author** | 1.0.0_SA_CTO~Z (site Z) |
| **Trigger** | Andrew-direct at the CTO~Z terminal: *"I want to explore the fortification of our platform security... analyze what endpoints are available to the public and how we are defending... do we have WAF/Rate limiting on [login]? How do we track and remediate unusual activity there? Once users are successfully logged in, how protected are our internal endpoints?... opal-users-v2 DDB table and associated opal-partner-* DDB RBAC tables, are these adequately encrypted/protected? How does the lambda edge factor into JWT verification... assess the server we provisioned for opalinvest.com and the server for the opal-gateway mcp (and its associated ALB)."* |
| **Method** | READ-ONLY. Every claim below names its plane: DESIRED (Terraform / source at working-tree HEAD), APPLIED (live AWS read at 16:5xZ-17:2xZ), or EXERCISED (a request actually made). Nothing was exercised against production; the two HIGH findings are stated from APPLIED configuration plus source, and the one-line proof for each is given so a seat can exercise it under Andrew's word. |
| **Scope** | Account 313476888478, us-east-1. Portal: CloudFront EVTSA9VEHNZVH, HTTP API 7k3ed8px20, REST API f61h681z9g, Lambda@Edge auth-validator-edge, auth-handler, DynamoDB identity/RBAC tables. Servers: EC2 opal-gateway + ALB opal-gateway, EC2 opal-website-wp. |
| **Not built** | Nothing. Every remediation is a proposal; the WAF/monitoring items fall under the standing moratorium and are Andrew's call. |

## Findings, ranked by consequence

### F1 -- HIGH -- The portfolio REST API is reachable with NO authentication at its own endpoint

**What:** `opal-portal-api` (REST, id `f61h681z9g`, EDGE-optimized, stage `/prod`) has **zero authorizers**
(`get-authorizers` -> `[]`), **no resource policy**, and its `execute-api` endpoint is enabled. Every one
of its 20 method-bearing resources is `authorizationType: NONE` (measured on two, and the authorizer set
is empty, which covers the denominator). They include WRITES:

```
PUT  /api/private/portfolio/optimization-autosave/{fund}/{account}   -> opal-pm-optimization-autosave-put
POST /api/private/portfolio/export-and-submit                          -> opal-portfolio-excel-generator
GET  /api/private/portfolio-management/upload-urls                     -> opal-pm-upload-urls (presigned S3 PUT URLs)
POST /api/public/market-update/save | generate | regenerate
```

**Why it is open:** the ONLY authentication on this API is CloudFront behavior 21 (`/api/private/portfolio*`
-> viewer-request `auth-validator-edge`). A request sent straight to
`https://f61h681z9g.execute-api.us-east-1.amazonaws.com/prod/api/private/...` never passes through
CloudFront, so the edge function never runs, and nothing behind it checks a token:

- `portfolio_optimization_autosave_put/lambda_function.py:15` says *"Auth: Bearer token required (Cognito)"*.
  There is no verification code in the file -- the only other Authorization reference is a CORS header.
  **And the estate does not use Cognito and never has** (Andrew, 2026-09-02: *"We do not use Cognito,
  never have. Agents tend to make that claim for some reason."*). No `aws_cognito_*` resource is
  declared in Terraform and no user pool exists live. The docstring names a control that does not exist
  AND an identity system that does not exist -- a fabricated control claim, which is worse than a
  missing one because it satisfies the next reader.
- `portfolio_excel_generator/lambda_function.py`: no token or identity check at all.
- `opal_pm_upload_urls/lambda_function.py:45-46` derives identity from request headers `X-User-Email` /
  `X-User-Tier`. The edge sets those on the CloudFront path; on a direct call **the caller sets them**.
- The edge also injects `X-Origin-Verify` -- its value is the constant string `"cloudfront"`
  (`auth-validator-edge/index.mjs:392`) and **no downstream code checks it** (estate-wide search: the
  only file containing the header name is the edge function itself). It is decorative.

**Consequence:** unauthenticated writes to portfolio optimization state, unauthenticated Excel generation
(compute + S3), unauthenticated minting of presigned S3 upload URLs, unauthenticated market-update
regeneration. Also skips the CloudFront WAF entirely.

**Exercise (one line, Andrew's word before running -- it is a PROD write surface):** an OPTIONS or GET to
a read-only resource on the raw endpoint returning 200 rather than 401/403 proves the class without
mutating anything.

**Remediation, minimal:** attach a Lambda authorizer to every method (the HTTP API already has
`portal-jwt-authorizer`; the REST equivalent is one resource + one `authorizerId` per method), AND make
`X-Origin-Verify` a real secret: a value from Secrets Manager set as a CloudFront **custom origin header**
and required by the authorizer, so a request that did not come through CloudFront is rejected even with a
valid token. Fix the autosave docstring -- a comment claiming a control that does not exist aims the next
reader wrong. **The Cognito myth's footprint, measured:** the token appears in 25 first-party source files
(8 of the portfolio Lambdas, 3 Terraform api-gateway files, ticket-center, data_refresh, `firmAccess.ts`)
and 6 docs, with zero definitions, zero `aws_cognito_*` resources declared, and zero user pools live. Every
one is a mention that may be carrying the same false control claim; sweep them with the fix.

### F2 -- MEDIUM-HIGH -- The HTTP API's public routes are public WITHOUT the WAF, and one spends OpenAI

**What:** `opal-portal-data-proxy-api` (HTTP, `7k3ed8px20`, CloudFront's origin for `/auth/*` and `/api/*`)
carries the `portal-jwt-authorizer` (REQUEST) on **60 of 72 routes** including `$default` -- good, and it
is what makes F1 a REST-API-only problem. The 12 `NONE` routes: `OPTIONS /{proxy+}`, `OPTIONS /auth/{proxy+}`,
`ANY /auth/{proxy+}` (pre-auth by design), and nine data routes:

```
GET /v1/health/data-availability   GET /v1/market/rsi            GET /v1/market/rsi/details
GET /v1/sentiment/fear-greed       GET /v1/sentiment/fear-greed/details   GET /v1/sentiment/keywords
POST /v1/sentiment/keyword-intelligence    GET /v1/metadata/yang    GET /metadata/yang
```

Via CloudFront, `/v1/*` (behavior 23) requires a JWT at the edge and sits behind the WAF. **Directly at
`7k3ed8px20.execute-api...` they require nothing and no WAF applies.** `POST /v1/sentiment/keyword-intelligence`
is cache-first with a **live OpenAI fallback on a cache miss** (`portal_data_proxy/lambda_function.py:1440-1460`,
key from `_get_openai_api_key`): an unauthenticated caller supplying novel keywords converts each request
into vendor spend, bounded only by API Gateway's account-level throttle.

**Remediation:** require the authorizer on `/v1/*` (the CloudFront path already presents a JWT, so
nothing legitimate breaks), and the same origin-secret header as F1 for `/auth/*`, so credential-stuffing
cannot route around the WAF rate rule (see F4).

### F3 -- MEDIUM -- Detection is near zero: the login surface is defended but not watched

| control | state (APPLIED) |
|---|---|
| GuardDuty | **not enabled** (`list-detectors` -> `[]`) |
| Security Hub | not enabled |
| AWS Config recorder | none |
| WAF logging (CloudFront ACL) | **not configured** -- only 3-hour sampled requests + CloudWatch counts |
| CloudFront access logging | off |
| ALB access logging (opal-gateway) | off |
| CloudTrail | **multi-region, log-file validation ON** (`opal-organization-trail`) -- the one durable audit source |
| Alarms on the auth path | `FIRMSEP-*` (edge scoping/tier denials, ownership-map failures) + 2 Lambda-throttle alarms. **None** on WAF `AuthLoginRateLimit` blocks, on `auth_throttled` (429s), on failed logins, on `mfa_code_rejected`/`mfa_code_expired`. |

**Answer to "how do we track and remediate unusual activity at /login":** today it is tracked as
CloudWatch metrics from the WAF rules and as structured log lines from the auth handler
(`auth_throttled`, `mfa_code_rejected`, `mfa_code_expired`, `mfa_code_sent`), and remediated by nobody
unless a human reads them. The 09-02 OTP investigation reconstructed 14 days of MFA activity from those
logs in minutes, so the RAW MATERIAL is good; there is simply no trigger on it.

**Remediation (all monitor-class, Andrew's word):** enable GuardDuty (one switch, no code, ~immediate
value: credential-access and IAM anomaly findings); WAF logging to S3 or CloudWatch Logs; two alarms --
`AuthLoginRateLimit` BlockedRequests > 0 and a metric filter on `auth_throttled`; CloudFront + ALB
access logs to S3. WAF logging is the single most useful of these because without it a blocked attacker
is invisible after three hours.

### F4 -- MEDIUM -- The login throttle is per-account, fail-open, and IP-blind

`auth-handler/src/throttle.ts`: progressive per-account cooldown, never a hard lockout (correct -- a hard
lockout lets an attacker lock out a known user by spraying their email), 15-min window. Two properties
to know:

- **Fail-open**: `:112-114` -- if the throttle table read fails, `return; // fail-open`. A DynamoDB
  outage or throttling of `opal-portal-auth-throttle` removes the only per-account brake.
- **IP-blind by design**: the handler never reads a client address (`index.ts`: zero references to
  X-Forwarded-For / viewer address). The per-IP axis is delegated to the WAF `AuthLoginRateLimit`
  (100 req / 5 min / IP, scoped to the auth POST paths) -- which only applies on the CloudFront path.
  `ANY /auth/{proxy+}` is `NONE` at the API (correct, it is pre-auth), so a direct call to the
  execute-api endpoint faces no per-IP limit at all; only the per-account cooldown and API Gateway's
  account-wide default throttle stand between it and credential stuffing.

**Remediation:** the origin-secret header from F1 closes the bypass; consider fail-closed with a
short-circuit (return 429 when the throttle store is unreachable) -- the availability cost is bounded
and the security cost of fail-open is not.

### F5 -- MEDIUM -- The CloudFront WAF carries no managed rule groups

`opal-cloudfront-protection` (APPLIED == DESIRED): default **Allow**; `RateLimitRule` 2000/5min/IP block;
`AuthLoginRateLimit` 100/5min/IP block scoped to `/auth/login` + two sibling auth POST paths. **No**
AWSManagedRulesCommonRuleSet, KnownBadInputs, AmazonIpReputationList, or BotControl. Sampled requests
for the auth rule over the last 3 h: 0 -- consistent with no attack and with nobody looking.
By contrast the gateway's regional ACL `opal-gateway-waf` has IP-reputation ENFORCED and Common +
KnownBadInputs in COUNT mode.

**Remediation:** add IpReputationList (block) + Common + KnownBadInputs (count for a soak, then block)
to the CloudFront ACL; flip the gateway's two COUNT groups to block after reviewing their counts.

### F6 -- LOW-MEDIUM -- Identity and RBAC data stores: encrypted, unevenly protected, one legacy copy

| table | encryption (APPLIED) | PITR | deletion protection | note |
|---|---|---|---|---|
| `opal-users-v2` (48 profiles + firm rows) | KMS CMK `86cc6c40...`, rotation ON (365 d) | ON | **OFF** | credentials + MFA state |
| `opal-partner-49financial` (11) | KMS CMK | **OFF** | OFF | RBAC: plaintext `email`, `firmRole` |
| `opal-partner-cottonwood` (4) | KMS CMK | **OFF** | OFF | |
| `opal-partner-inflection` (7) | KMS CMK | **OFF** | OFF | |
| `opal-partner-demo` (1) | AWS-owned key | OFF | **ON** | inverted relative to the real firms |
| `opal-portal-auth-mfa` / `-throttle` | AWS-owned key | OFF | OFF | ephemeral, TTL-reaped; fine |
| **`opal-users` (LEGACY, 12 rows)** | KMS CMK | ON | OFF | **no live reader** in first-party source (only the 1.2 migration, an archived script, and the Terraform); the auth-handler role still holds GetItem/PutItem/UpdateItem/DeleteItem/Scan/Query on it **and on a us-east-2 copy** (`iam.tf:50-51`) |

The CMK policy is the standard DynamoDB via-service grant (`Principal AWS:*` conditioned on the DynamoDB
service), so **IAM on the table, not KMS, is the read gate**. The auth handler's grant is correctly scoped
(named tables; `opal-partner-*` GetItem only, because it derives the table per firm). The partner-data
Lambda takes `allowedFirmIds` from **authorizer context**, not from headers (`opal-partners-data:1640-1670`),
with one soft spot: an *internal* user with no `allowedFirmIds` is granted ALL as a migration fallback.
`comp-iam` is DESIRED-plane only and reports 24 policy blocks it could not attach and 2 unparsed Deny
statements, so "who else can read these tables" is NOT fully answered by this pass; a live
`simulate-principal-policy` sweep is the instrument.

**Remediation:** PITR + deletion protection on `opal-users-v2` and the three real partner tables; align
`opal-partner-demo`; snapshot-then-delete `opal-users` and remove its grant (and the us-east-2 ARN);
consider hashing `email` in the partner tables as the MFA/throttle tables already do.

### F7 -- LOW-MEDIUM -- Key and token lifecycle

- JWTs are RS256; the keypair `opal/auth/jwt-private-key` / `-public-key` was created **2026-04-06**
  and has **no rotation** configured (5 months). Both the edge and the API authorizer fetch the public
  key from Secrets Manager, so rotation is mechanically possible but has no runbook (dual-key overlap).
- Access token 15 min; refresh token 7 days; refresh `sub` is the **email**, not `userId` -- the F-10
  finding (delete + re-create on the same address re-binds a live refresh token to the new row).
- The `cross-firm-secret-deny` belt (explicit Deny on other firms' secrets for the auth handler) is in
  place -- a good pattern worth extending.

## What is working (so the list above is read in proportion)

- **Edge JWT verification** (`auth-validator-edge`): RS256 against the Secrets Manager public key, on
  every route except `/auth/*` and OPTIONS; advisor scoping against an ownership map, tier policy
  (L0/L1/L2), admin bypass rules -- with five `FIRMSEP-*` alarms on its denial metrics. This is the
  layer Andrew asked about: it verifies the token, then **injects** the identity (`X-User-*`, `X-Firm-Id`,
  `X-Advisor-Id`) for downstream. The firmId/userId "match" is: the JWT's `firmId`/`advisorId` claims
  must cover the requested firm/advisor path, checked at the edge for the S3 and API paths -- and
  re-derived independently at the HTTP API by `portal-jwt-authorizer`, which computes `allowedFirmIds`
  (own firm, plus descendants for admins) into the authorizer context the Lambdas actually trust.
  **That second check is why F1 is a REST-API-only hole and not an estate-wide one.**
- S3 data origins are OAC/OAI-only (bucket policies name the distribution); no bucket is directly
  readable.
- CloudFront: TLS floor `TLSv1.2_2021`, HTTP/2+3, WAF attached (APPLIED == DESIRED).
- Per-account throttle design; MFA on 31 of 48 accounts (email OTP, 30-min TTL as of 16:23Z today);
  SES production-grade with DKIM/SPF alignment.
- CloudTrail multi-region with validation.

## Workstream 2 -- the servers

### opal-gateway (MCP) + ALB `opal-gateway`

| | APPLIED |
|---|---|
| instance | `i-07dccb1615503ac99`, t4g.nano, IMDSv2 **required**, **no SSH key** (SSM), profile `opal-gateway-profile` |
| network | SG `opal-gateway-sg` allows **8080 only from the ALB's SG** -- the box has a public IP (13.221.151.249) but nothing can reach it directly |
| ALB | internet-facing; SG 80 + 443 from 0.0.0.0/0; 80 -> redirect; 443 policy `ELBSecurityPolicy-TLS13-1-2-2021-06`, ACM cert; target `opal-gateway-tg` :8080 healthy 1/1 |
| auth, default | `authenticate-oidc` (order 1) against Microsoft Entra (tenant `6810043e...`), session 7 d, `on-unauthenticated: authenticate` -> forward (order 2) |
| auth, forwarded AROUND OIDC | rule 10 `/mcp*`, `/authorize`, `/register`, `/token`; rule 20 `/.well-known/*`, `/callback`; rule 30 `/otp/fetch`, `/otp/health`; rule 31 `/ms/*` |
| what guards those | `/mcp*`: the app's own OAuth AS bearer (`oauth_as.validate_access_token`: RS256 signature, issuer, audience, expiry) + kill switch + per-user blocklist + per-identity rate limit (`server.py:91-168`). `/otp/fetch` and `/ms/*`: a **static capability bearer** (`otp.check_bearer`, `ms_ingest.check_bearer`). ALB-OIDC identity is signature-verified with the algorithm pinned (a prior `verify_signature=False` spoof hole was closed, `identity.py:83-95`). |
| WAF | regional `opal-gateway-waf`: rate 2000/5min block, IP-reputation **enforced**, Common + KnownBadInputs **COUNT only** |
| attributes | access logs **OFF**, deletion protection OFF, drop-invalid-header-fields OFF, desync mitigation defensive |

**Assessment:** the layering is right -- OIDC at the ALB for humans, per-protocol bearers for the
machine paths, WAF in front, the instance unreachable except via the ALB. Findings: (a) the two COUNT
groups should graduate to block; (b) ALB access logs on (the bearer paths are exactly where an abuse
pattern would show); (c) the static bearers for `/otp` and `/ms` want a rotation cadence and a
narrow scope -- a leaked one is a standing credential; (d) the instance's public IP is unnecessary
given the SG and should go; (e) deletion protection on the ALB.

### opal-website-wp (opalinvest.com)

| | APPLIED / DESIRED |
|---|---|
| instance | `i-0152e3fe2599fa630`, t3.small, Elastic IP 18.208.18.213, IMDSv2 required, no SSH key |
| network | SG 80 + 443 from 0.0.0.0/0 only -- **no admin port (7080), no SSH** |
| stack | OpenLiteSpeed + LSPHP 8.2 + local MariaDB + WordPress (Bricks); **no CloudFront, no WAF** -- by the original spec (*"NO RDS / Fargate / Lightsail / CloudFront"*) |
| hardening (`harden.sh`, DESIRED) | unattended OS security upgrades; fail2ban with a wp-login/xmlrpc filter; wp-config hardening; least-privilege DB user; site plugins wps-hide-login, wps-limit-login, Turnstile, safe-svg; nightly backup to `opal-website-backups` + DLM/AWS Backup snapshots |

**Assessment:** the box is well-behaved (no exposed admin ports, IMDSv2, patched, backed up). The
exposure is **WordPress itself**: core + plugin CVEs, `xmlrpc.php`, `wp-login.php`, with only host-level
fail2ban and plugins between them and the internet, and no request-level WAF. It is the largest
unmanaged attack surface in the estate. Findings: (a) put a WAF-capable edge in front -- CloudFront +
managed rules, or Cloudflare proxying the apex -- which reverses a line of the original spec and is
therefore Andrew's call; (b) confirm plugin auto-updates, not only OS; (c) consider restricting
`/wp-admin` and `xmlrpc.php` by source IP at the edge. Note `harden.sh` is DESIRED; whether fail2ban
is live on the box was not measured here (SSM would answer it).

### Two other running instances, for completeness

- `canonical-schwab-si2` (t3.large, public IP, **RDP 3389 from one /32**, IMDSv2 **optional**, key pair):
  acceptable as a scoped spike box; set IMDSv2 required.
- `inf-gold-layer-runner` (c6a.4xlarge, public IP, SG has **no ingress**, IMDSv2 required): unreachable;
  the public IP is unnecessary.

## Recommended order

1. **F1** -- authorizer on every REST method + a real origin secret. Days of work, closes an open write
   surface. Exercise first under Andrew's word.
2. **F2/F4** -- the same origin secret on `/auth/*` and `/v1/*` at the HTTP API; authorizer on `/v1/*`.
3. **F3** -- GuardDuty + WAF logging + two alarms (Andrew's word; monitor-class).
4. **F5** -- managed rule groups on the CloudFront ACL; graduate the gateway's COUNT groups.
5. **F6** -- PITR/deletion protection sweep; retire `opal-users`.
6. **F7** -- JWT key rotation runbook; F-10 (`sub` = userId).
7. Website edge WAF (spec decision); gateway ALB logs + static-bearer rotation.

## Bounds on this assessment

DESIRED != APPLIED != EXERCISED. Terraform and source were read at working-tree HEAD; live AWS was
read at the times stated; nothing was sent to a production endpoint. `comp-iam` covers only what
Terraform declares and could not attach 24 policy blocks or parse 2 Deny statements, so the IAM picture
is partial. The website's on-box state (fail2ban running, plugin versions) was not read. The API IDs
are not secrets but they are also not published; F1's exploitability rests on an attacker learning one,
which is not a control.
