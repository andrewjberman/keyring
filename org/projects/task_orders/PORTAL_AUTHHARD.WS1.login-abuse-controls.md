<task_order>
<metadata>
  <to_id>PORTAL_AUTHHARD.WS1</to_id>
  <project>PORTAL_AUTHHARD (Portal Auth/Authz + Abuse-Resistance Hardening)</project>
  <title>Login abuse controls -- per-account + per-IP failed-login throttle (progressive delay, NOT hard lockout) + independent reset/forgot limits + structured login_failed events. HIGHEST value / smallest blast radius. Co-deploys with WS2a + WS8 in the auth-handler Lambda.</title>
  <assigned_to>0.7.0_AE_CloudOps~B</assigned_to>
  <issued_by>1.0.0_SA_CTO~B</issued_by>
  <issued_date>2026-07-20</issued_date>
  <status>COMPLETE -- exercised GREEN 2026-07-20 (portal-auth-v1.20.0, deploy d84ac01d4). Design + plan arch-gated (add-only, 1/3/0); CTO~B independent applied-state ground-truth CONFIRMED (DDB table live, IAM UpdateItem allowed isolated-control, WAF AuthLoginRateLimit live + RateLimitRule untouched). Exercises: throttle 401x5->429, counter-reset-on-success, reset/forgot independent limit 200x5->429, login_failed structured logs emitted, IAM Get/Update/Delete-allow + PutItem-deny (isolated), WAF live. CVO GREEN -- independently exercise-verified @0ce2731bf (CVO re-ran the burst + decoded the WAF scope-down + confirmed deploy-real).</status>
  <dispatch_held>false</dispatch_held>
  <priority>HIGH -- DO FIRST (brief: highest value, smallest blast radius). Wave 1.</priority>
  <references>
    <ref type="prd">docs/architecture/PORTAL_AUTHHARD_PRD.md WS-1</ref>
    <ref type="brief">docs/briefs/PORTAL_AUTH_HARDENING_BRIEF_20260720.md G1 + WS-1</ref>
    <ref type="charter">org/tier0/ledger/LD-0323.md (Andrew-direct)</ref>
    <ref type="grounding">auth-handler/src/index.ts:157-188 (no throttle on login/refresh/forgot/reset); terraform/portal-auth/waf-cloudfront.tf:16-33 (only control = 2000/5min/IP, default_action allow) -- re-grounded by CTO~B @HEAD 2026-07-20</ref>
    <ref type="proposal">Andrew proposal S5.1/S5.2/S6.1/S6.2 (Priority 2)</ref>
  </references>
</metadata>

<scope>
Implement account-level + IP-level login-abuse controls on the portal auth-handler. The stack today calls
login()/refresh()/forgotPassword()/resetPassword() straight through with ZERO per-account/per-IP counter, no
lockout, no failed-login logging (grounded: index.ts:157-188). The only existing control is a coarse WAF
RateLimitRule (2000 req / 5-min / IP) that cannot distinguish a login failure from any request and does nothing
against slow credential-stuffing or distributed spraying.

DELIVERABLE:
1. **Per-account throttle:** 5 failed attempts / 15 min -> progressive delay / temporary cooldown. Keyed on the
   submitted email (lower-cased), firm-agnostic (login precedes firm resolution).
2. **Per-IP throttle:** 20-30 failed attempts / 10 min -> progressive delay. Source IP from the trusted request
   context (NOT a client-supplied header -- confirm the IP source is CloudFront/API-GW-derived, not X-Forwarded-For
   spoofable).
3. **NOT a hard lockout** -- progressive delay / short cooldown only. A hard lockout lets an attacker lock out known
   users by spraying their emails (proposal S6.1). This constraint is load-bearing; do not "simplify" to a lockout.
4. **Independent reset/forgot limits:** 3-5 reset requests / hr per account, a broader per-IP hourly cap
   (proposal S6.2). forgotPassword() must keep returning generic success (enumeration-safe -- already correct at
   auth.ts:215-218; do not regress it).
5. **Emit structured login_failed events** -- one per failed attempt, carrying {account_hash_or_email, source_ip,
   timestamp, reason} as a structured (JSON) CloudWatch log line. THIS IS THE FEED FOR WS-4. It is a LOG, not an
   alarm -- NOT subject to the alert-suspension hold. A successful login emits a login_success (or resets the
   counter) so WS-4 can build the "success-after-many-failures" signal.
6. **Successful login resets/reduces the failure counter** for that account (proposal S7.1).

MECHANISM (executor's call within these constraints, arch-gate the choice):
- A DynamoDB counter table (recommended): PK = throttle key (acct#... / ip#...), TTL-expiring, atomic increment
  (UpdateItem ADD). TTL removes the sweep. AND/OR a WAF rate-based rule scoped to the /auth/login path (WAF gives
  IP-layer defense before Lambda spend, but cannot do per-ACCOUNT logic -- so the DynamoDB counter is likely needed
  regardless for the per-account limit). Bring the design to CTO~B before apply.
- Generic error responses preserved: a throttled request returns a generic 429-class response; never reveal whether
  the account exists or why (no "account locked" that confirms the email).

DISCIPLINE:
- Terraform-only for the DynamoDB table + WAF rule + any IAM (auth-handler needs UpdateItem/GetItem on the new
  table -- add it as an explicit least-privilege statement, NOT a wildcard). safe-apply (never bare apply).
- auth-handler code deploy via the normal build+Terraform cycle (Terraform-only Lambda deploy; never
  aws lambda update-function-code). commit via safe-commit. Update the source map.
- CO-DEPLOY with WS2a (refresh status re-check) + WS8 (password policy) -- all three touch the SAME auth-handler
  Lambda; batch them into one build+deploy+arch-gate+exercise cycle to avoid three deploy churns on one function.
- ARCH-GATE (CTO~B) the counter-table schema + IAM statement + WAF rule design BEFORE apply. NO live change lands
  before the arch-gate.
</scope>

<acceptance>
EXERCISE-based (Rule 22a) -- a config read / merged PR is NOT acceptance:
- [ ] A scripted credential-stuffing burst against a real /auth/login (test account, wrong password x N) ACTUALLY
      gets throttled -- 429/progressive-delay observed past the 5/15min account threshold, and past the per-IP
      threshold from one IP. Capture the actual responses.
- [ ] A SUCCESSFUL login on that account resets/reduces the counter (a subsequent single failure is not immediately
      re-throttled).
- [ ] The reset/forgot endpoints are INDEPENDENTLY throttled (exercise the 3-5/hr account cap) and forgotPassword
      still returns generic success for a non-existent email (enumeration-safety not regressed).
- [ ] A login_failed structured event is ACTUALLY emitted and readable in the auth-handler CloudWatch log group
      (grep the real log stream, not the source).
- [ ] Real-user path unaffected: a normal correct login is never throttled.
- [ ] CTO~B arch-gate obtained on table schema + IAM + WAF rule; safe-apply 0-diff; source map updated; RAVC to
      CTO~B (CC MSTR). CVO exercise-verify.
</acceptance>
</task_order>
