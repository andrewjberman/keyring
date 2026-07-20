<task_order>
<metadata>
  <to_id>PORTAL_AUTHHARD.WS2a</to_id>
  <project>PORTAL_AUTHHARD (Portal Auth/Authz + Abuse-Resistance Hardening)</project>
  <title>Session lifecycle phase 2a -- add the status==active re-check to refresh() so a disabled user cannot mint fresh access tokens for the 7-day refresh window. One-line fix; co-deploys with WS1 + WS8 in the auth-handler Lambda. (Phase 2b revocation primitive is a separate Wave-2 TO.)</title>
  <assigned_to>0.7.0_AE_CloudOps~B</assigned_to>
  <issued_by>1.0.0_SA_CTO~B</issued_by>
  <issued_date>2026-07-20</issued_date>
  <status>COMPLETE -- exercised GREEN 2026-07-20 (portal-auth-v1.20.0). Shipped the minimal one-liner (status==active re-check in refresh(); 500/indistinguishable from login's disabled path -- no login-contract change). EXERCISED: disabled user /auth/refresh -> HTTP 500 + ZERO tokens minted; active user refresh -> 200; re-enable -> 200. Frontend grep closed my required-confirm (AuthContext.tsx nothing branches on refresh status). CVO GREEN @0ce2731bf (CVO V-1: PRD acceptance text reconciled 401->no-fresh-token; security property met). (Follow-up: 500->403 map is grep-grounded-safe but deliberately not taken this wave.)</status>
  <dispatch_held>false</dispatch_held>
  <priority>HIGH -- Wave 1 (closes the disabled-user window; the sharp part of G3).</priority>
  <references>
    <ref type="prd">docs/architecture/PORTAL_AUTHHARD_PRD.md WS-2 (phase 2a)</ref>
    <ref type="brief">docs/briefs/PORTAL_AUTH_HARDENING_BRIEF_20260720.md G3</ref>
    <ref type="grounding">auth-handler/src/auth.ts:53-55 (login checks status) vs auth.ts:92-116 (refresh does getUser at :98, !user guard at :100, but NEVER re-checks status) -- re-grounded by CTO~B @HEAD 2026-07-20</ref>
    <ref type="proposal">Andrew proposal S4.3/S5.3/S6.10 + S7.4 (session tests); Priority 4</ref>
  </references>
</metadata>

<scope>
refresh() (auth.ts:92-116) looks the user up and guards on !user, but -- unlike login() (auth.ts:53-55) -- it never
re-checks user.status. So a DISABLED or removed user holding a valid refresh-token cookie keeps minting fresh 15-min
access tokens for the full 7-day refresh window.

DELIVERABLE: add the same status guard login() has, into refresh(), immediately after the user lookup:
    if (user.status !== 'active') { throw new Error('Account disabled'); }
(placed after the !user guard at ~L100, before generateAccessToken at L114). Match login()'s exact error string so
the failure mode is indistinguishable to a caller (no new enumeration signal).

SCOPE BOUNDARY: this TO is ONLY the one-line status re-check (phase 2a). The full revocation primitive -- a token
version/tokenGen claim that lets disable/password-reset/"revoke all sessions" invalidate LIVE access tokens before
they expire -- is WS-2 phase 2b, a separate Wave-2 TO (it is an arch change touching BOTH verifiers). Do not build
2b here.

DISCIPLINE: co-deploy with WS1 + WS8 in ONE auth-handler build+deploy cycle. Terraform-only Lambda deploy;
safe-commit; commit-gate; update source map. Arch-gate is trivial here (one line) but still batched into the WS1
arch-gate review.
</scope>

<acceptance>
EXERCISE-based (Rule 22a) -- the value of this TO is the proof, not the diff:
- [ ] Disable a test user (status != active in the users table) WHILE they hold a valid refresh-token cookie, then
      call /auth/refresh with that cookie -> it ACTUALLY 401s (or the mapped error), and NO new access token is
      minted. Capture the real response.
- [ ] An ACTIVE user's /auth/refresh still succeeds (no regression to the normal path).
- [ ] The error is indistinguishable from login()'s disabled-account error (no new enumeration signal).
- [ ] Deployed in the shared auth-handler cycle; RAVC to CTO~B (CC MSTR); CVO exercise-verify (this is exactly the
      proposal S7.4 session test -- "disable a user while logged in... verify the timing").
</acceptance>
</task_order>
