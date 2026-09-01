# CTO~Z session-close -- MFA enabled for Opal staff cohort, flow verified synced, fabric wind-down

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT (production MFA enablement), VALIDATE (write + sync verification), COORDINATE (DE sync check, wind-down)

Window: since last session-close log `cf2ef501de` -> 2026-09-01 ~17:48Z. Seat `1.0.0_SA_CTO~Z` (site Z).

## Summary

Andrew-direct 2026-09-01 ~17:2xZ, verbatim: "let's push MFA to all opal users now." Executed the
unambiguous, safe core and held/excluded the genuinely-forking populations after grounding the actual
user table (NOT the phrase "all users" -- the table spans 5 firms + service + test accounts).

**DONE -- enabled email MFA on 13 opal-capital NAMED STAFF** via direct `update-item` on `opal-users-v2`
(conditional, idempotent): `SET mfaChannel='email', mfaEnabled=true` -- the EXACT two fields
`setMfaPreference` writes (db.ts:338/353). Accounts: adam, alyssa, austin, jeanette, jim, keith, lauren,
manav, menachem, michael, wade, wayne, yang @opalinvest.com. Verified on fresh scan: 15 profiles now
mfaEnabled=true (the 13 + andrew@/aj@ pilot), all 13 = email channel, **0 stray**, machine accounts OFF.

**Scope decisions (Andrew, this session):**
- Partner-firm advisors (49financial x11 / cottonwood x5 / inflection x6): **HELD** ("No partner firms yet...
  test locally with opal users... once I get word back it was smooth we push global").
- Test/regression/demo (~9): **EXCLUDED** ("exclude on call 2").
- Machine/service accounts `svc-bbgtml@` (F-7) + `cot-verify-internal@`: **excluded** -- headless, would
  lock out. Confirmed still mfaEnabled=false.
- jim/keith/wayne (created 2025-12-29 by andrew@, never a recorded login, still mustChangePassword=true):
  Andrew: "They're real, leave them on." LEFT ON.

**Channel = EMAIL ONLY.** SMS still gated on SP-1 (toll-free carrier verification, weeks out, Andrew-gated).
SES is production (`ProductionAccessEnabled: true`), so email delivery is not gated.

**UI-flow sync VERIFIED (Andrew asked, routed to surface owner 0.4.0_DE~Z; report 19260):** the direct-flip
users are FIELD-IDENTICAL to any email-MFA user -- the email login gate reads ONLY mfaEnabled+mfaChannel
(auth.ts:104-105); every phone-field read is on the SMS/enrolment path, never email login->send->verify.
Completion proven on the deployed build (RIAv5cTF): andrew@ real prod login 07:43Z + AE 12/12 email exercise
+ Yang live this session. Promote-gap CLEAN: origin/DEV == origin/PROD byte-identical on all auth files;
served PROD = portal-v2.1.174 / 529f3093 is the current flow.

**One live false-alarm, resolved:** Yang hit `Cannot read properties of undefined (reading 'email')` -- a
STALE cached bundle (pre-MFA-promote); hard-refresh fixed it. Served bundle is correct; no code defect. The
operational takeaway (any of the 13 with an old tab open hits this until refresh) is folded into the heads-up
note offered to Andrew.

## Compiler Tools

No py_compile / ruff / commit-gate run: this window made **no code or repo edits** -- the work was
operational (production DynamoDB writes) + fabric coordination + read-only verification. Rule-20/commit-gate
checks ride implementing code TOs, of which there were none here.
- **comp-rail (Rule 21):** a `grep` segment was correctly GATED and routed to native `Grep` (`db.ts` MFA
  contract) -- rail behaved. Native `Grep`/`Read` + `git show origin/PROD:<path>` (MSYS_NO_PATHCONV for
  slashed refs) used for served-plane source reads.
- **aws (operational):** `dynamodb scan`/`update-item` (conditional), `lambda get-function-configuration`,
  `sesv2 get-account`. All operational reads/writes, not the IAM-inspection class.
- **What failed:** the first `update-item` batch -- all 13 rc=252 ParamValidation (client-side, request never
  sent, table untouched). Root cause: native Windows Python `print` emits `\r\n`, `read` left a trailing CR
  in `$PK` -> a control char inside the `--key` JSON. Fix: `| tr -d '\r'`. Banked as a memory.

## Current State (handoff, zero prior context)

- **`opal-users-v2` (prod, us-east-1):** 15 PROFILE rows mfaEnabled=true / mfaChannel=email = andrew@, aj@,
  + the 13 staff above. Machine accts svc-bbgtml@ / cot-verify-internal@ = false. Partner firms + test/demo =
  false (held/excluded). Reversible (flag flip) if a different rollout is wanted.
- **Deployed backend:** `opalinvest-auth-handler` CodeSha256 `RIAv5cTFNKIH2X04tAuB7zen7gzDIrXgjdlN8ftN+7w=`
  @15:54:25Z -- Act B (login issues, sends nothing) + `POST /auth/mfa/send` live (index.ts:186).
- **Served frontend:** portal-v2.1.174 / origin/PROD 529f3093. Stale docstrings in MfaOptInPrompt.tsx +
  AuthContext.tsx (say /auth/mfa/send "does not exist yet") fixed in DE's SF-3 @17c9a829 -- LOCAL/unpushed,
  cosmetic, rides next promote.
- **Records:** D12 reconciliation confirmed by COO (19254): decomp_ref @5b736ec484, blocking cell + last_updated
  landed. Minor open: `PLATFORM_OPS_USERMGMT.json` dep_stage still REGISTERED (MSTR's field; routed).

## Next Steps

- **Fabric wind-down IN PROGRESS (Andrew-direct):** 6 seats directed to /log + report (msgs 19261-19266, all
  DELIVERED). Collecting confirmations; **ping Andrew when all 7 seats reported** [1.0.0_SA_CTO~Z].
- **Heads-up note to the 13** (with hard-refresh caveat): offered to Andrew, awaiting his word.
- **Global (partner-firm) rollout:** HELD pending Andrew's "word back" the local test was smooth+easy.
- **SMS factor:** remains gated on SP-1 provisioning (Andrew-gated) [held at this seat].
