<task_order>
<metadata>
  <to_id>PORTAL_AUTHHARD.WS3</to_id>
  <project>PORTAL_AUTHHARD</project>
  <title>MFA for privileged roles -- native TOTP step-up (NOT Cognito, arch-decided A.1) gated on admin/internal/Dev/architect. Enrollment + verify + amr claim. DESIGN-FIRST -> CTO~B arch-gate. Wave 2.</title>
  <assigned_to>0.7.0_AE_CloudOps~B</assigned_to>
  <issued_by>1.0.0_SA_CTO~B</issued_by>
  <issued_date>2026-07-20</issued_date>
  <status>complete -- SPRING-CLEAN 2026-08-25 (S2): <project> field repaired from "PORTAL_AUTHHARD (Portal Auth/Authz + Abuse-Resistance Harden" to PORTAL_AUTHHARD, which is closed. Closed as a record act, not a work verdict. Prior status: ISSUED -- QUEUED after WS-2b + WS-6. DESIGN-FIRST; no build before CTO~B arch-gate. Build-vs-Cognito is DECIDED (native TOTP, PRD A.1) -- do NOT re-open it.</status>
  <dispatch_held>true</dispatch_held>
  <priority>HIGH -- Wave 2 (privileged accounts on a single human-chosen password today).</priority>
  <references>
    <ref type="prd">docs/architecture/PORTAL_AUTHHARD_PRD.md WS-3 + Appendix A.1 (native-TOTP-not-Cognito decision, grounded)</ref>
    <ref type="brief">docs/briefs/PORTAL_AUTH_HARDENING_BRIEF_20260720.md G2</ref>
    <ref type="grounding">jwt.ts: bespoke RS256, custom claims (sub/name/role/tier/firmId/userType/advisorRole); ZERO Cognito in the auth path (both verifiers = jwt.verify on the public key). login() verifies password then mints tokens (auth.ts:48-73). -- CTO~B @HEAD 2026-07-20</ref>
    <ref type="proposal">Andrew proposal S6.3 (MFA required for admins / privileged-data / infra operators; may stay optional for low-privilege)</ref>
  </references>
</metadata>

<scope>
The portal auth path is pure email+password+bcrypt -- no MFA anywhere, including admin / tier:internal / userType:Dev
superadmin / advisorRole:architect. Arch-decided (PRD A.1, grounded): BUILD native TOTP in auth-handler; do NOT adopt
Cognito (a Cognito migration rebuilds the entire sound+exceeds stack -- disproportionate blast radius reintroducing
tenant-isolation risk).

DELIVERABLE (DESIGN-FIRST -- bring me the design before build):
1. A per-user TOTP secret, stored SERVER-SIDE ONLY (never returned through any endpoint; encrypted at rest --
   DynamoDB default SSE is acceptable, or a dedicated store -- state your choice).
2. An ENROLLMENT flow (provision secret + QR/otpauth URI to the user once, confirm with a first code before activating).
3. A step-up at login: after password verify, IF the user is privileged (role:admin || tier:internal ||
   userType:Dev || advisorRole:architect) AND MFA-enrolled, REQUIRE a valid TOTP before minting tokens. Optional for L0.
4. An amr:['pwd','otp'] (or mfa:true) claim minted into the token so genuinely sensitive routes can require step-up.
5. TOTP verification via a mature library (e.g. otplib) shipped in a LAMBDA LAYER (Deploy Rule 3 -- deps in layers,
   no pip/npm -t into source). Time-window tolerance + replay protection stated.
6. Composes with WS-2b: an MFA reset / re-enrollment bumps the token_version (revokes live sessions).

DISCIPLINE: DESIGN-FIRST -> CTO~B arch-gate (the gating predicate, the secret storage, the enrollment + replay
handling, the claim). Then Terraform-only Lambda deploy (+ the layer), safe-apply, safe-commit, commit-gate, source-map.
Any new IAM (e.g. reading a TOTP-secret store) = scoped least-privilege + post-apply simulate-principal-policy
(one --resource-arns/call + isolated positive control). NO alarms (Andrew ruling, PRD A.3).
</scope>

<acceptance>
EXERCISE-based (Rule 22a):
- [ ] DESIGN arch-gated by CTO~B BEFORE build.
- [ ] A privileged (e.g. admin/internal) test account, MFA-enrolled, CANNOT complete login without a valid current
      TOTP code (exercise end-to-end: password-only -> rejected/challenged; password + valid code -> tokens minted).
      Capture real responses.
- [ ] An L0 (non-privileged, non-enrolled) account logs in UNAFFECTED (no MFA prompt).
- [ ] The TOTP secret is never returned by any endpoint (grep the responses; exercise /auth/me and enrollment).
- [ ] Replay: a just-used code (or one outside the window) is rejected.
- [ ] Blast-contained + verified-deleted test user(s) (Wave-1 lifecycle discipline: ledger open@create/closed@verified-delete).
- [ ] RAVC to CTO~B (CC MSTR); CVO independent exercise-verify.
</acceptance>
</task_order>
