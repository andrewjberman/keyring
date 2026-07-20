<task_order>
<metadata>
  <to_id>PORTAL_AUTHHARD.WS8</to_id>
  <project>PORTAL_AUTHHARD (Portal Auth/Authz + Abuse-Resistance Hardening)</project>
  <title>Password policy -- raise validatePassword minimum to >=12, permit passphrases + password managers, reject a commonly-breached list. Set-time only (NO login-time lockout of existing users). Co-deploys with WS1 + WS2a in the auth-handler Lambda.</title>
  <assigned_to>0.7.0_AE_CloudOps~B</assigned_to>
  <issued_by>1.0.0_SA_CTO~B</issued_by>
  <issued_date>2026-07-20</issued_date>
  <status>COMPLETE (mechanism) -- exercised GREEN 2026-07-20 (portal-auth-v1.20.0). EXERCISED: <12 rejected at set-time; breached 'password1234' (>=12) rejected (breached gate independent of length); passphrase-with-spaces accepted (200); existing sub-12 user (11-char direct-bcrypt-write) STILL logs in -> 200 (no lockout, boundary held). CVO-pending. COVERAGE RESIDUAL (label the basis): the breached list shipped is a curated top-N HEAD, not the full top-10k -- the full list needs a one-time SecLists/Pwned import (off-Opal egress -> Andrew word) OR a local file drop; swap breached-passwords.ts only. Tracked follow-up, not blocking the mechanism.</status>
  <dispatch_held>false</dispatch_held>
  <priority>LOW-MEDIUM -- Wave 1 (bundled, low effort, same Lambda).</priority>
  <references>
    <ref type="prd">docs/architecture/PORTAL_AUTHHARD_PRD.md WS-8</ref>
    <ref type="brief">docs/briefs/PORTAL_AUTH_HARDENING_BRIEF_20260720.md G7</ref>
    <ref type="grounding">auth-handler/src/password.ts:22-27 (validatePassword = length>=8 only; bcrypt cost 12 at :3). Shared by changePassword/resetPassword/adminCreateUser (auth.ts:176,238,289) -- re-grounded by CTO~B @HEAD 2026-07-20</ref>
    <ref type="proposal">Andrew proposal S6.4 (password standards)</ref>
  </references>
</metadata>

<scope>
validatePassword (password.ts:22-27) requires length >= 8 only -- no >=12 minimum, no breached-password rejection.
It is the single set-time gate, shared by changePassword / resetPassword / adminCreateUser.

DELIVERABLE:
1. Raise the minimum to **>= 12 characters**.
2. **Permit long passphrases and password managers** -- favor length + uniqueness over composition rules; do NOT add
   forced-character-class or forced-rotation rules (proposal S6.4 explicitly argues against them). A 40-char
   passphrase with spaces must pass.
3. **Reject a commonly-breached-password list.** Prefer a bundled top-N breached list (offline set) over a live
   HaveIBeenPwned range call on the auth hot path -- if a live call is proposed, it must NOT sit on the login path
   and must fail-open on vendor error (never block a legitimate set on an API timeout). Bring the choice to CTO~B.
4. Keep the error messages generic/non-enumerating; message copy should guide toward a passphrase.

CRITICAL BOUNDARY (do NOT cross): this is a **set-time** control only (new / changed / reset / admin-created
passwords). Do **NOT** add any login-time check that rejects an existing user whose stored password is < 12 -- that
would lock out current users on a hash they cannot change without logging in. Existing users are migrated by being
prompted to update on their next change, never by a login-time rejection. bcrypt hashes are opaque to length, so
existing logins are unaffected by construction -- keep it that way.

DISCIPLINE: co-deploy with WS1 + WS2a in ONE auth-handler cycle. If a breached-list data file is bundled into the
Lambda, keep it out of the login hot path (loaded only on set-time paths). Terraform-only Lambda deploy;
safe-commit; commit-gate; source map.
</scope>

<acceptance>
EXERCISE-based (Rule 22a):
- [ ] Setting a new password of length < 12 is REJECTED at set-time (exercise via changePassword or the admin
      create path). Capture the real rejection.
- [ ] A long passphrase WITH SPACES (e.g. >= 12 chars, multiple words) is ACCEPTED.
- [ ] A known-breached password (e.g. a top-list entry) is REJECTED.
- [ ] An EXISTING user with an old sub-12 password STILL LOGS IN successfully (no lockout) -- exercise a real login
      with a pre-existing short-password test account.
- [ ] No breached-list lookup happens on the /auth/login hot path (set-time only).
- [ ] Deployed in the shared auth-handler cycle; RAVC to CTO~B (CC MSTR); CVO exercise-verify.
</acceptance>
</task_order>
