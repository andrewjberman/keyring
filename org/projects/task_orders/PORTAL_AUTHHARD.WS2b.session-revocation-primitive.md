<task_order>
<metadata>
  <to_id>PORTAL_AUTHHARD.WS2b</to_id>
  <project>PORTAL_AUTHHARD</project>
  <title>Session revocation primitive -- a token version/generation claim so disable / password-reset / "revoke all sessions" invalidates LIVE tokens. DESIGN-FIRST (touches BOTH verifiers + the mint) -> CTO~B arch-gate -> build+exercise. Wave 2.</title>
  <assigned_to>0.7.0_AE_CloudOps~B</assigned_to>
  <issued_by>1.0.0_SA_CTO~B</issued_by>
  <issued_date>2026-07-20</issued_date>
  <status>complete -- SPRING-CLEAN 2026-08-25 (S2): <project> field repaired from "PORTAL_AUTHHARD (Portal Auth/Authz + Abuse-Resistance Harden" to PORTAL_AUTHHARD, which is closed. Closed as a record act, not a work verdict. Prior status: ACTIVE -- GO on the DESIGN (this dispatch). NO build/apply before CTO~B arch-gates the design (it touches both JWT verifiers + the token mint -- a claim only one verifier checks is a bypass).</status>
  <dispatch_held>false</dispatch_held>
  <priority>HIGH -- Wave 2, first (completes WS-2: WS-2a closed the acute disabled-user case; WS-2b generalizes revocation).</priority>
  <references>
    <ref type="prd">docs/architecture/PORTAL_AUTHHARD_PRD.md WS-2 (phase 2b) + Appendix A.2 (S5.2 key-rotation cache)</ref>
    <ref type="brief">docs/briefs/PORTAL_AUTH_HARDENING_BRIEF_20260720.md G3</ref>
    <ref type="grounding">jwt.ts: RS256, access 15m / refresh 7d, claims sub/name/role/tier/firmId (no version claim today); TWO verifiers -- auth-validator-edge (stateless verify+inject, NO DB lookup today) + users/lambda/portal-authorizer/index.mjs:177-181. refresh() already does getUser (auth.ts:98). WS-2a landed (portal-auth-v1.20.0): refresh() now re-checks status. -- CTO~B @HEAD 2026-07-20</ref>
    <ref type="proposal">Andrew proposal S4.3/S5.3/S6.10 (session management) + S7.4 (session tests: disable/remove/downgrade/reset/revoke-all/replay -> "document + verify the timing")</ref>
  </references>
</metadata>

<scope>
WS-2a (SHIPPED) closed the acute case: a disabled user can no longer refresh. WS-2b generalizes it into a real
REVOCATION primitive so disable / password-reset / role-change / "revoke all sessions" can invalidate ALREADY-ISSUED
tokens, and documents the propagation timing (proposal S7.4).

DELIVERABLE (DESIGN-FIRST -- bring me the design before any build):
1. A `ver` (token version / generation) claim minted into tokens from a `token_version` integer on the user record;
   compared on verify; a mismatch -> reject (401). Bumping `token_version` invalidates the matching live tokens.
2. Bump triggers: user disable (status->inactive), password reset/change, and an explicit admin "revoke all sessions".
3. BOTH verify points must honor `ver` where it applies -- a claim only ONE verifier checks is a bypass. State
   exactly which verify points check it and why.
4. Document + MEASURE the propagation timing per revocation reason (proposal S7.4).
5. Fold confirm-item S5.2 (PRD A.2): a JWT key-rotation procedure. NOTE the grounded hazard -- jwt.ts caches the
   keys at MODULE level (cachedPrivateKey/cachedPublicKey), so a rotated key is not picked up until a Lambda cold
   start; the rotation design must address cache invalidation (dual-key validity window / forced cold-cycle), else
   rotation silently lags live tokens.

>> THE ARCH TENSION TO RESOLVE IN THE DESIGN (tee it up for my gate, do not default it) <<
Full revocation of ACCESS tokens means checking `ver` on EVERY access-token verify -- which requires a per-request
user-record read at the edge + authorizer (converting stateless verification into stateful; a latency + cost hit on
every portal request). My LEANING (ground against it, argue if the grounding says otherwise): the ACCESS token is
already only 15 min, which the brief accepts for role/firm propagation. So the proportionate design is likely
REFRESH-PATH revocation -- enforce the `ver` check on /auth/refresh (which ALREADY does a getUser, auth.ts:98, so
zero added reads) + optionally on genuinely sensitive routes -- and let the <=15-min access window bound the rest.
That closes the sharp gap (the 7-day refresh window generalized to any revocation reason) WITHOUT a per-request edge
DB read. The alternative (ver-check on every access verify, per-request DB read) buys closing a <=15-min window at a
standing per-request cost -- likely disproportionate, but GROUND the edge/authorizer paths + the sensitive-route set
and bring me the tradeoff. I gate the choice.

DISCIPLINE: DESIGN-FIRST. No code/TF/apply before my arch-gate on the design. Then normal cycle: Terraform-only
Lambda deploy, safe-apply, safe-commit, commit-gate, source-map, tag. If the design adds any IAM (e.g. a verifier
reading the user table), it is a scoped least-privilege add -> arch-gate + post-apply simulate-principal-policy
(one --resource-arns/call + isolated positive control).
</scope>

<acceptance>
EXERCISE-based (Rule 22a) -- the proof, not the diff:
- [ ] DESIGN arch-gated by CTO~B BEFORE build (ver-claim placement + which verify points check it + the
      per-request-cost tradeoff resolved + bump triggers + propagation timing + the key-rotation cache handling).
- [ ] After build: bumping a live user's token_version ACTUALLY invalidates the relevant live token at the next
      gated verify point (exercise: mint a token, bump ver, hit the protected path -> rejected). Capture real responses.
- [ ] "Revoke all sessions" on a test user ACTUALLY invalidates its live refresh token (subsequent /auth/refresh 401s).
- [ ] Password-reset bumps ver (a token minted before the reset is invalidated at the gated point).
- [ ] The measured propagation timing per reason is DOCUMENTED and matches the design's claim (proposal S7.4).
- [ ] Blast-contained + verified-deleted test user (same lifecycle discipline as Wave-1: ledger open@create /
      closed@verified-delete; no prod auth credential survives).
- [ ] RAVC to CTO~B (CC MSTR); CVO independent exercise-verify.
</acceptance>
</task_order>
