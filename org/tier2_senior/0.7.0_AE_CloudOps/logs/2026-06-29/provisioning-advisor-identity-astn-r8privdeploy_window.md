# 0.7.0_AE_CloudOps — provisioning + advisor-identity + ASTN + R8-PRIV-deploy window (2026-06-29)

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DEPLOY, DIAGNOSE, COORDINATE

Window = since the prior log (`lambdamap-durable-sfn-reconcile-r8priv_window.md`). Several Andrew-direct
threads landed; all grounded against live/served state.

## Summary of work

**1. User provisioning (Andrew-direct; DT+DE offline -> AE owns, W4a precedent).** ADVI_INFUSR (2 inflection)
+ ADVI_COTUSR (3 cottonwood) -> 5 real users into opal-users-v2 + opal-partner-*; both project JSONs flipped
complete (39f7ea265), COO-accepted, PROD-login-verified (200/JWT both firms). Cottonwood domain CLEAN-REPLACE
cottonwood.com->cottonwoodmail.com in all 3 places (create_user_v2 FIRMS 9fb12fa50 / FIRM#META.domain DDB /
portal firmAccess.ts 21f2178d CI-deployed DEV). 3 prior @cottonwood.com accounts confirmed throwaway (orphaned,
no migration). Inflection pw=InflectionWealth7 (Andrew correction), cottonwood pw=Goldto6k2026!.

**2. "Advisor Identity Unavailable" diagnosis + fix (Andrew screenshot).** Root cause: the Advisor-Intelligence
Profile tab resolves the JWT `advisorId` claim, minted at login from opal-partner-{firm}.advisorKey; I'd
provisioned patrick/noel with empty advisorKey -> advisorId='' -> the error. FIXED patrick (= Patrick Scanlan,
advisorKey=patrick_scanlan already in the portal allow-list) via partner-table backfill; JWT now carries
advisorId=patrick_scanlan (live-decoded). NOEL = ops/back-office (Andrew ruling), NOT an advisor -> advisorId
null by design; DE gated the FE Profile tab on a resolved advisorId (portal adda3e0e) so bookless viewers get
Distribution-only. Clean A/B coordination with 0.4.0_DE (no double-fix).

**3. Canonical per-PARTNER provisioning scripts (Andrew-direct, recurrence-prevention).**
`users/scripts/partners/` {partner_contracts.py + provision_{49financial,inflection,cottonwood}.py + README}
(bcaf386e2) + OPS/back-office `--ops` user-type (ba8c3faa1). Each ENFORCES the firm contract fail-closed:
49f+inflection REQUIRE advisor fields (inflection ALSO validates the key against the portal layout.ts
allowedAdvisorKeys); cottonwood/--ops firm-level REJECT advisor fields. Wraps create_user_v2 + read-back
verifies. 6/6 + 4/4 enforcement assertions pass (incl the exact patrick + noel cases).

**4. Structured firstName/lastName on opal-users-v2 (Andrew-direct).** backfill_user_names.py backfilled all 44
PROFILEs (additive UpdateItem SET, never touched passwordHash; login 200 post-backfill) + corrected patrick/noel
full names; create_user_v2 now writes firstName/lastName for new users (8d297711f).

**5. Drift + duplicate cleanup, opal-users-v2 (Andrew-direct).** Backed up all 45 PROFILEs first. Removed drift:
firmRole (1)/advisorId (1)/password_hash (19, kept canonical passwordHash that auth prefers; only-snake
user@opalinvest.com copied to canonical first). Deleted 2 dups: yang@opalinvest.com (malformed orphan) +
usr_379860be7479 ("Test User" dup of user@opalinvest.com). Verified: 43 PROFILEs, zero residual drift, no dup
emails, login still 200. (DDB-direct ops, no git commit; backfill script committed 8d297711f.)

**6. ASTN_WSJFT faithfulness-gate fix (Andrew-direct + CTO 180911Z).** Removed the verify_facts DROP gate in
analyze.py (was nuking ~90% of good articles -> ~1 article/email 3+ days) -> kept=facts[:3], accuracy stays
prompt-enforced (ae7eb9efb); deleted dead verify_facts/_VERIFY_SYS; config.py vestigial-var cleanup + E402 fix
(7978aca4a). S3-artifact-push deploy (the transient box pulls at 3am-ET; manifest cfd625c9d). Verify = the 3am-ET
digest total_articles_out (~1 -> ~5-9).

**7. NFRA_OPLMCP.R8-PRIV gateway deploy -> served-verify -> complete.** Deployed ~B's fail-closed audit
args-allowlist (838d8790b) to the live m365-gateway S3->EC2->restart (43763af4e), on-box md5-verified
(440b6f08==local), systemd active/health ok/401 intact. CVO served-verified (an undeclared content tool ->
args={_omitted: fail-closed} in Athena, zero leak); TO complete + scope-hold lifted (8d381884e).

**8. P0 IDOR PoC (DE G1, COO-GO'd verify-before-build).** Ran the live PoC myself (no token pasted): patrick
(user) -> peter_lee book/mix-views/platinum-summary via the edge = ALL 401/403 "Advisor scope mismatch"; control
patrick->own (patrick_scanlan) = 200. The own-book gate IS enforced on the realistic edge path -> the source-read
IDOR hypothesis FALSIFIED live; residual = direct-API-GW bypass test + Lambda defense-in-depth (RAVC'd DE+COO).

**9. Also in-window (CVO/COO-dispatched, cite commits):** NFRA_COMPAWS.PHASE-0 G2 edge-census oracle increment-1
(8b915f081); dead-infra teardowns -- tier1 never-applied multi-account scaffold + deprecated tooling (c4dceebf7),
bd-time-machine dead lambda (1ecaa1389, apply-next), opal_users_v2 portal-auth twin de-dup (1f6fa344d, PITR-safe);
close-time-flip durable-fix spec routed COO+MSTR (b694340a0).

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| comp-iam service bd-cot-freshness-probe | PutMetricData grant pre-check (earlier window) | PASS | n/a this window |
| ds-commit-gate.sh | every .py edit (analyze/config/create_user_v2/partner_contracts/backfill + 3 scripts) | PASS | py_compile+ruff py39; caught F401/E402/E702, fixed |
| live aws (ec2/ssm/ddb/lambda/cloudwatch/secretsmanager) | provisioning + cleanup + R8-PRIV deploy verify + IDOR PoC | PASS | served/live grounding throughout (NEVER#7) |
| safe-ec2-deploy.sh m365-mcp-gateway | R8-PRIV gateway deploy | PASS | on-box md5 + systemd + 401 verified (wrapper charmap false-neg is banked) |

**What worked:** live-decode of the JWT pinned the advisor-identity root cause in one shot; the read-back-verify
in the per-partner scripts is the durable recurrence-prevention. **What failed:** safe-ec2-deploy ran the
astn box-side pull script locally (mkdir /opt fail) -> astn is an S3-artifact-push box (the box self-pulls at
start), used direct Rule-12 aws s3 cp. **Gap found:** create_user_v2 was firm-agnostic (let advisor users be
provisioned with no advisorKey = the broken-Profile-tab class) -> closed by the per-partner contract scripts.

## MCP traffic (~30 msgs handled)
GOs/rulings/RAVCs: COO Andrew-direct dispatches (ASTN, provisioning, drift-cleanup) + RAVC-ACCEPTs; CTO 180911Z
(ASTN spec), 184552Z (cottonwood clean-replace), Option-1a + 3-mint-stagger bless (prior window); DE 0.4.0
A/B/noel coordination + G1 IDOR + G3 advisorRole-49f heads-up; ~B R8-PRIV build handoff. Notable RAVC closes:
ADVI_INFUSR+COTUSR complete, R8-PRIV complete, IDOR-falsified-live.

## Blockers
None blocked-on-me. Residual external gates (not blockers): ASTN verify rides the 3am-ET nightly; patrick's
Profile-tab fix needs his re-login (after the portal DEV CI deploys DE's adda3e0e + my 21f2178d).

## Current State (handoff)
- **opal-users-v2**: 43 PROFILEs, clean schema -- canonical `passwordHash` (no `password_hash`), no PROFILE-level
  firmRole/advisorId drift, no dup emails; every PROFILE has firstName/lastName. Authoritative: role->PROFILE,
  firmRole->opal-partner-{firm}, advisorId->minted from partner advisorKey at login. Backup JSON in scratchpad.
- **5 new users LIVE + PROD-login-verified**: patrick@/noel@inflectionwealth.com (patrick=advisor patrick_scanlan;
  noel=ops/viewer, advisorId null by design), jay.rubottom/stephen.shipley/christa.bass@cottonwoodmail.com (firm-level).
- **Canonical provisioning**: `users/scripts/partners/` is the go-forward path (contract-enforced, ops-aware).
  `users/scripts/create_user_v2.py` writes firstName/lastName. `backfill_user_names.py` is re-runnable.
- **ASTN_WSJFT**: analyze.py fix LIVE in S3 (s3://opal-313476888478-lambda-artifacts/ec2/astn-wsjft/code/scripts/);
  box pulls at next 3am-ET run.
- **m365-gateway** (i-07dccb1615503ac99): R8-PRIV fail-closed audit args-allowlist LIVE + CVO-served-verified.

## Next Steps
- **[0.7.0_AE_CloudOps]** verify ASTN 3am-ET digest total_articles_out (~5-9); confirm patrick Profile tab resolves post his re-login; apply bd-time-machine teardown (1ecaa1389, plan 0/0/6).
- **[0.4.0_DE_ClientPlatform]** G3 advisorRole-is-49f-only: firm-scope the role-strip ladder + (with AE) strip spurious advisorRole from inflection partner rows; G1 IDOR direct-API-GW bypass test (if pursued) -> AE re-runs with the invoke URL.
- **[2.0.0_SA_COO]** sequence the PROD firmAccess promote (cottonwood client-view, low-pri, rides next DEV->PROD) + the G3/G1 TO + the close-time-flip durable-fix decision (b694340a0).
