# Portal Authentication & Authorization Hardening Brief

**Author:** `0.0.0_AB_MSTR` · **For:** `1.0.0_SA_CTO` (PRD + arch-gate) · **Date:** 2026-07-20
**Status:** DRAFT — pending Andrew review; **do not dispatch to CTO until Andrew's GO**
**Source doc:** "Authentication and Authorization Hardening Proposal" (Andrew, `~/Downloads/`, 2026-07-20)
**Grounding vintage:** working tree @ HEAD `f1ee62c0a` (2026-07-20). All `file:line` citations resolve at this vintage.

---

## 0. What this is

The proposal is a strong, well-structured hardening plan whose own method is *"confirm these mechanics
against the real implementation."* This brief does exactly that: I read the deployed source and **grounded
every one of the proposal's "as understood" assumptions and open questions** against the actual portal
auth stack, then reduced the proposal's ~50 recommendations to the **real, grounded gaps** — with
`file:line` evidence so CTO's PRD starts from territory, not the map.

**Scope = the portal** (`opalinvest.dev`, the firm-scoped advisor dashboard) — matching the proposal.
It is NOT the agent fabric, the MCP/m365 gateway, or the ETL pipelines (adjacent auth surfaces, out of scope here).

**Method note (per Rule 22):** findings marked **GROUNDED** cite source I read. Findings marked
**CONFIRM** are live-behavior or config claims I could not fully verify from source and that need an
*exercise* (a request-manipulation test or a live AWS read), not a code read — flagged honestly rather
than asserted.

---

## 1. Bottom line

**The foundational model is sound, and in several dimensions our real implementation materially EXCEEDS
the proposal's "as understood."** The proposal's central worry — that the client could choose its own
firm/role via headers — **is already architecturally closed**: a single Lambda@Edge gate verifies the
JWT and *injects server-derived* `X-Firm-Id`/`X-User-Role` headers, overwriting anything the client sent.
On top of that we already run advisor-id scoping, per-account ownership-map scoping, tier-role gates, an
explicit cross-firm secret Deny, and a cross-firm S3-bypass detector.

**The gaps are concentrated on the *abuse-resistance and account-lifecycle* axis, not the tenant-isolation
axis** — exactly the opposite emphasis from where a reviewer usually fears the worst. The four that matter:
1. **No login abuse controls** (no per-account/IP throttle, no lockout, no failed-login logging). *HIGH.*
2. **No MFA** for any portal user, including admins/internal/superadmin. *HIGH.*
3. **No session revocation**, and `refresh()` doesn't re-check account status → a disabled user keeps
   minting tokens for the 7-day refresh window. *HIGH.*
4. **Detection is built but not delivered** — the FIRMSEP alarm SNS topic has **no subscriber**. *MEDIUM-HIGH.*

None require re-architecting. All are additive.

---

## 2. What is already TRUE and STRONG (confirm-and-keep — credit the team)

| # | Proposal concern | Grounded reality | Evidence |
|---|---|---|---|
| A | §3/§6.5/§7.2 — client must not choose firm/role via headers | **Solved at the edge.** `auth-validator-edge` (viewer-request, the single centralized gate) verifies the RS256 JWT, then **injects** `x-user-*`/`x-firm-id`/`x-user-role` from the *verified payload*, overwriting client-supplied values. Downstream Lambdas never parse JWTs — they read trusted headers. | `lambda-edge/auth-validator-edge/index.mjs:206-395` (inject 382-392) |
| B | §4.1/§6.10 — token verification + short-lived tokens | **RS256 asymmetric** JWTs; private key in Secrets Manager; **15-min access / 7-day refresh**; issuer+audience checked on verify. Two independent verifiers (edge + API-GW authorizer). | `auth-handler/src/jwt.ts:10-13,87-122`; `users/lambda/portal-authorizer/index.mjs:177-181` |
| C | §4.6 — password storage | **bcrypt cost 12**, native per-hash salt; compare server-side only; hashes stripped from all API responses (`getCurrentUser` omits `password_hash`). | `auth-handler/src/password.ts:3-17`; `auth.ts:149` |
| D | §5.1/§7.1 — user enumeration | Login returns generic *"Invalid email or password"*; forgot-password **always** returns success. | `auth.ts:44-51,215-218`; `index.ts:178-182` |
| E | §4.6 — reset tokens short-lived + single-use | crypto-random 32 bytes, **1-hour expiry**, and **single-use**: `updatePassword` does `REMOVE reset_token, reset_token_expires` in the same write. | `auth.ts:220-226`; `db.ts:222` |
| F | §6.10 — refresh-token hygiene | `HttpOnly; Secure; SameSite=Strict` cookie. | `index.ts:94-97` |
| G | §3.4/§5.4/§7.3 — cross-tenant object access | **Multi-layer, and 404-not-403 as the proposal recommends.** Firm scope = injected `X-Firm-Id` + shared-advisor-router S3-key rewrite + `opal-partners-data` firm-scoped queries. Plus **advisor-id scoping (004a)**, **per-account/relationship ownership-map scoping (004c)**, and **tier-role gates (ROLGAT L0/L1/L2)** — all at the edge. | `auth-validator-edge/index.mjs:186-204,267-380`; `tier_policy.mjs` |
| H | §6.7/§6.11 — cross-firm credential isolation | An explicit **Deny** on `secretsmanager:* opal/bd/*` for the portal/auth/news roles (defense against an `opal/*` wildcard reaching a partner firm's Black Diamond creds). | `terraform/portal-auth/cross-firm-secret-deny.tf:45-61` |
| I | §6.9 — authz-denial observability | FIRMSEP suite: metric-filter alarms on `advisor_scoping_denied`, `tier_denied`, `ownership_map_fetch_failed`, `ownership_map_schema_mismatch`, router denials, **plus a CloudTrail alarm on direct-S3 access bypassing CloudFront**. | `terraform/portal-auth/cloudwatch-alarms.tf` |
| J | §3.4 — two data planes | Correctly separated: **firm-agnostic** data (market/AUM/benchmarks/news via `portal_data_proxy`, no firm-scoping *needed*) vs **firm-scoped** advisor/client data (edge-gated + key-rewritten). | `lambda/portal_data_proxy/lambda_function.py` (headers not firm-keyed by design) |

**Also note (transforms, not gaps):** we are **DynamoDB, not SQL** — so the proposal's SQL-injection,
parameterized-query, row-level-security, and DB-role items (§4.5/§6.6) mostly **do not apply as written**.
Access is parameterized `Key()`/`Attr()` conditions; there is no injectable query string. The equivalent
defense-in-depth is **IAM `dynamodb:LeadingKeys` conditions** on partner tables (see WS-5), not SQL views.

---

## 3. The REAL gaps (grounded, prioritized)

### G1 — No login abuse controls  ·  **HIGH**  ·  proposal §5.1/§5.2/§6.1/§6.2 (Priority 2)
`login()`, `forgotPassword()`, `resetPassword()` call straight through with **no per-account counter, no
per-IP counter, no lockout, no progressive delay, no failed-login logging** (grep of the whole auth-handler
for `rate|throttle|lockout|failed.attempt` = **0 hits**). The *only* control is the CloudFront WAF's single
`RateLimitRule` = **2000 req / 5-min / IP** — a coarse volumetric cap (≈400/min) that does nothing against
slow credential-stuffing or distributed spraying, and cannot distinguish a login failure from any other request.
- Evidence: `auth-handler/src/index.ts:157-188`; `waf-cloudfront.tf:16-33`.
- Consequence: online guessing and credential stuffing (the proposal's #1 realistic path) are unmitigated
  at the account level. bcrypt protects the *hash if stolen*; it does nothing against guessing the *login*.

### G2 — No MFA for any portal user  ·  **HIGH**  ·  §6.3 (Priority 4)
The portal auth path is pure email+password+bcrypt. There is **no TOTP, no Cognito MFA, no step-up** anywhere
in the auth-handler (grounded: the OTP/Cognito hits in the estate are all vendor-scraper logins and the
m365 gateway — none touch the portal). Admins, `tier:internal`, `userType:Dev` superadmin, and architect-tier
users all rest on a single human-chosen password.
- Evidence: `auth-handler/src/*` (no MFA); scoped grep confirmed OTP infra is inf-pipeline/m365 only.
- Priority framing: MFA for **privileged roles first** (admin / internal / Dev / L2-architect), optional for L0.

### G3 — No session revocation; disabled users keep a 7-day window  ·  **HIGH**  ·  §4.3/§5.3/§6.10 (Priority 4)
JWTs are stateless RS256 with **no denylist / no version claim**, so there is **no way to revoke a live token**.
Worse, `refresh()` looks the user up but **does not re-check `status === 'active'`** — only *initial login* does
(`auth.ts:53-55`). So a **disabled or removed user with a valid refresh-token cookie keeps minting fresh 15-min
access tokens for the full 7-day refresh window.** Role/firm changes likewise don't propagate until the *access*
token expires (≤15 min — acceptable) but the *disable* case is the sharp one.
- Evidence: `auth.ts:92-116` (refresh, no status check) vs `auth.ts:53-55` (login checks status); `jwt.ts:10-11`.
- The proposal's §7.4 session tests ("disable a user while logged in… the expected timing should be documented
  and verified") would fail here for the refresh path.

### G4 — Detection is built but not delivered; no auth-abuse alarms  ·  **MEDIUM-HIGH**  ·  §6.9 (Priority 2/5)
Two sub-findings:
- **(a) The alarms page nobody.** `cloudwatch-alarms.tf:258-259` states verbatim: *"opal-infrastructure-alerts
  currently has NO subscribers — wire an endpoint to actually page (open item, all FIRMSEP alarms)."* Every
  FIRMSEP cross-firm/scoping alarm and the S3-bypass rule fire into an **unsubscribed SNS topic.** A built,
  correct detector that reaches no human is not a control.
- **(b) No authentication-abuse telemetry.** All FIRMSEP alarms cover *authorization* denials (cross-firm
  scoping). There is **no failed-login metric, no per-account/per-IP failure alarm, no "success after many
  failures" signal** — because the auth-handler emits no login-failure log (see G1). The proposal's §6.9
  authentication signals have no source to alarm on.

### G5 — Least-privilege: a shared role + wildcard secrets on the auth plane  ·  **MEDIUM**  ·  §6.7/§6.11 (Priority 6)
`opal-portal-lambda-role` is a **single shared role behind 11 Lambdas, including the PUBLIC authorizer**, and
the portal/auth/news roles held `secretsmanager:* opal/*` **wildcards**. `cross-firm-secret-deny.tf` surgically
Denied `opal/bd/*` (good, shipped), but the underlying **wildcard→explicit-allowlist narrowing and per-function
role separation is explicitly "still being grounded"** (that TF file's own comment, lines 13-18). The proposal's
§6.7 ("a function that only reads basic info should not hold credentials capable of accessing all production
data") is a real, named, partially-open item here.
- Evidence: `cross-firm-secret-deny.tf:8-18`.

### G6 — No authenticated-request extraction / cost controls  ·  **MEDIUM**  ·  §5.5/§5.6/§6.8 (Priority 5)
Beyond the per-IP WAF cap there are **no per-user request ceilings, no max page/export sizes, no concurrency
limits, no high-cost-endpoint quotas.** Some data-proxy scans carry a `Limit`, but nothing bounds a *valid
account* from crawling all authorized records or fanning out the expensive endpoints (e.g. the on-demand
GPT keyword-intelligence route, or the recursive-descendant DynamoDB Scan the authorizer runs per admin
request — `portal-authorizer/index.mjs:79-111`). Compromised-account scraping (§5.5) and serverless cost
amplification (§5.6) are unmitigated.

### G7 — Password policy is min-8, no breached-password check  ·  **LOW-MEDIUM**  ·  §6.4
`validatePassword` requires **length ≥ 8 only** — no ≥12 minimum, no breached-password rejection.
- Evidence: `auth-handler/src/password.ts:22-27`.

### G8 — [CONFIRM] Direct-to-origin bypass of the edge scoping gates  ·  §4.4/§7.3
The 004a/004c/ROLGAT advisor/account/tier gates run **only at Lambda@Edge**. The API-GW authorizer
re-verifies the JWT but does **not** re-run those gates; S3 origins rely on shared-advisor-router. The edge
injects a **static** `X-Origin-Verify: cloudfront` (not a secret). **Confirm** that every origin (API GW +
the advisor-intelligence S3 origins) actually **rejects non-CloudFront requests** (OAC / a *secret* origin
header enforced at the origin), rather than only being *detected* after the fact by the (unsubscribed)
FIRMSEP.09 CloudTrail rule. If an authenticated non-admin can reach an origin directly, they bypass their
own advisor/account scoping (backend firm-scoping still contains cross-*firm*, but not within-firm advisor scope).
- This is the proposal's §4.4 ("can it be called outside the intended frontend?") — needs an *exercise*, not a read.

---

## 4. Recommended workstreams for CTO's PRD

Ordered to the proposal's own priority ladder, re-weighted by our grounded state (tenant isolation is
already strong, so it drops; account-lifecycle + abuse rise).

- **WS-1 — Login abuse controls (G1).** Per-account (5 fails / 15 min) + per-IP (20-30 / 10 min) failure
  throttle with progressive delay/cooldown (avoid hard lockout — a spray could lock out real users);
  independent reset/forgot limits; **emit structured `login_failed` events** (feeds WS-4). Likely a
  DynamoDB counter table + a small change in `auth.ts`/`index.ts`, and/or a WAF rate-based rule scoped to
  `/auth/login`. **Highest value; smallest blast radius.**
- **WS-2 — Session lifecycle + revocation (G3).** Minimum: add `status === 'active'` re-check to `refresh()`
  (one-line, closes the disabled-user window). Then a real revocation primitive — a token `version`/`tokenGen`
  claim compared against the user record, so disable / password-reset / "revoke all sessions" invalidates
  live tokens. Document the propagation timing (the proposal's §7.4 asks for exactly this).
- **WS-3 — MFA for privileged roles (G2).** TOTP step-up gated on `role:admin || tier:internal ||
  userType:Dev || advisorRole:architect`. Optional for L0. Decide build-vs-Cognito.
- **WS-4 — Wire the alarms + add auth-abuse alarms (G4).** (a) Subscribe a real endpoint to
  `opal-infrastructure-alerts` (closes the "pages nobody" gap for the *entire* existing FIRMSEP suite —
  cheap, high leverage). (b) Add metric filters + alarms on the WS-1 `login_failed` events (per-account,
  per-IP, one-IP-many-accounts, success-after-many-failures).
- **WS-5 — Authenticated extraction + cost controls (G6).** Per-user request ceilings, max page/export
  sizes, concurrency + quota on high-cost endpoints (GPT route, admin descendant-Scan), billing/usage
  alarms. Generous enough that real users never notice.
- **WS-6 — Least-privilege role split + secret de-wildcarding (G5).** Finish the grounded narrowing:
  split `opal-portal-lambda-role` by responsibility (esp. isolate the *public authorizer*), replace
  `secret:opal/*` wildcards with explicit per-role allowlists. Never-widen; CTO arch-gate.
- **WS-7 — Origin lock-down + the pentest plan (G8 + proposal §7).** Confirm/enforce origins reject
  non-CloudFront (OAC / secret origin header), then run the proposal's §7 request-manipulation suite
  (header spoof, cross-firm object, direct-endpoint, session-timing, scraping) as an *exercise* against a
  test account — the proposal is right that this must be done at the request layer, not the UI.
- **WS-8 — Password policy (G7).** Raise min length to 12, permit passphrases/managers, reject a breached-
  password list. Low effort.

**Acceptance discipline (per Rule 22a):** each WS is done only when its claim is *exercised* — e.g. WS-1 is
GREEN when a scripted burst against `/auth/login` actually gets throttled (not when the code merges); WS-2
when a disabled user's refresh actually 401s; WS-4 when a synthetic denial actually pages a human. A config
read is not acceptance for a behavioral control.

---

## 5. Confirm-items (need an exercise / live read, not a source read)

1. **G8 origin reachability** — can an authenticated user hit the API-GW / S3 origins directly, bypassing
   the edge gates? (request-manipulation test)
2. **JWT key rotation** — is there a rotation procedure for `opal/auth/jwt-private-key`? (revocation of last
   resort today, since there's no denylist.)
3. **WAF managed rules** — the WAF has only the one rate rule; confirm whether AWS Managed Rules
   (bad-inputs / SQLi / bot-control) are intentionally omitted.
4. **`allowedPages`/`allowedTabs` enforcement** — the authorizer passes these claims through; confirm a
   backend actually enforces them (else they're decorative).
5. **CloudTrail / billing alarms** — confirm account-level audit logging + billing alarms exist (proposal
   §6.11) — I did not ground these in the portal-auth tree.

---

## 6. One-line map (proposal → our state)

`server-side identity` ✅done · `token verify/short-lived` ✅done · `bcrypt` ✅done(cost12) ·
`enumeration-safe` ✅done · `reset single-use` ✅done · `cross-tenant isolation` ✅done+exceeds ·
`login throttle` ❌**WS-1** · `reset throttle` ❌**WS-1** · `MFA` ❌**WS-3** · `session revocation` ❌**WS-2** ·
`disabled-user on refresh` ❌**WS-2** · `alerting delivered` ❌**WS-4** · `auth-abuse alarms` ❌**WS-4** ·
`least-privilege roles` 🟡**WS-6** · `per-user/cost limits` ❌**WS-5** · `password ≥12 + breached` ❌**WS-8** ·
`SQL items` ⊘N/A(DynamoDB) · `origin lockdown` ❓**WS-7/confirm**

---

*Prepared by MSTR as a grounded companion to Andrew's proposal. Ready to dispatch to CTO (for a PRD + WS
decomposition, same flow as NFRA_SYSPARITY) on Andrew's GO.*
