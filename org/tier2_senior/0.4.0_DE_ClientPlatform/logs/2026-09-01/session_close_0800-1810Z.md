# Session close -- 0.4.0_DE_ClientPlatform~Z (site-Z ~Z lane): D12 login UI closed+accepted, D12 SMS-OTP leg driven to a committed client-API foundation, Andrew's MFA UI-sync check answered

**archetype:** MIXED
**secondary_archetypes:** COORDINATE (primary), IMPLEMENT, VALIDATE, DIAGNOSE

**Date:** 2026-09-01 · **Window:** ~08:00Z -> 18:10Z (this session; wind-down on Andrew-direct 19263)
**Serial:** 0.4.0_DE_ClientPlatform~Z

Two projects this window. (1) `PLATFORM_OPS_USERMGMT` (D12 MFA login UI) -- CLOSED + fully accepted.
(2) `D12_PHONE_OTP_ALL_AWS` (SMS OTP, a sibling seated mid-session) -- SF lane driven from seating
through the full design/review/contract to a committed client-API foundation; the rest is SP-1-gated.
Plus an Andrew-requested MFA UI-sync check, answered.

---

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| playwright (headless) | DE1-1 client-gate + PROD-client check on opalinvest.dev | PASS | client-gate network (#77 login / #78 send), negative declaration by instrument, prompt render read |
| curl | localhost:5176/auth/login proxy pre-flight; opalinvest.dev bundle | PASS | proxy reaches the real handler (real 401), not an SPA fallback |
| aws (lambda/logs/dynamodb) | get-function-configuration; filter-log-events; dynamodb query/scan | PASS | deployed sha verified at each stage; DE1-1 T0/T1/T2 read on own plane; fixture-gone + auth-table read confirmed |
| bun run typecheck (tsc -b) | SF-3 + SF-2 part-1 | PASS | correct non-bare form; --listFiles via bunx failed (rc127) so used tsc -b incremental rebuild of changed files |
| proof-of-spec-check.py | DE1-1 | PASS (VALID rc=0) | 4 rows, 0 violations |
| comp-find / Grep | portal (submodule -> native Grep) + auth-handler (comp-find) | PASS | comp-find is worktree-bound; portal submodule needs native Grep/Glob |
| safe-commit.sh | -F/-m, Write-tool msgfiles, from workspace root AND from portal/ | PASS | 764c103099, ef300ba13a (workspace); 17c9a829, 653587f (portal DEV) |

**What worked:** reading the newest inbox messages BEFORE acting repeatedly caught superseded frames
(the F-8 rotation verdict walked back 3x while I held; the SB deploy splitting a blessed gate).
Pre-registration review caught real defects before artifacts existed (my SF review commissioned an
unscoped enrolment-verification atom; my Q4 found a live F4 residue; my sms-sendable gate flag caught
a false-pass CTO ruled in).
**What failed:** a Python JSON write CRLF-ified the DE1-1 proof-of-spec (200/199 whole-file diff);
caught + fixed with `newline="\n"`. Native `tsc`/`bunx` not resolvable (rc127) -- used `bun run typecheck`.
**Gap found:** the enrolment-verification backend (send-code-to-candidate + verify-and-mark + verified
field + the F3a guard) was UNSCOPED in the decomp; surfaced -> commissioned as SB-6/SB-7/SB-8.

---

## Commits (DE header lines)

WORKSPACE (org/) -- on origin/SITEZ (local HEAD == origin/SITEZ 2c5ff07dcb, measured ls-remote 18:10Z):
- `764c103099` score(D12 DE1-1): PASS -- last MFA-login row, browser client-gate + CloudWatch, both handlers
- `ef300ba13a` fix(D12 DE1-1): correct a STALE bound -- PROD serves the fixed client, DE1-1 applies to prod NOW
- (this log rides the same tree)

PORTAL (portal/ DEV) -- LOCAL, NOT on origin/DEV (7d0ca60c), integrator's push leg:
- `17c9a829` docs(D12 SF-3): stale Act-A docstrings -> deployed Act-B/C reality (MfaOptInPrompt + AuthContext)
- `653587f`  feat(D12 SF-2, part 1/2): client enrolment API surface on AuthContext (the UI component follows)

---

## Blockers

- **SF-2 part 2 (enrolment UI) + SF-1 (reflect-not-select login prompt): SP-1-gated.** The SMS backend
  (SB-1..9) is APPLIED but 0 origination identities -> sms.ts fails closed -> no SMS deliverable until
  toll-free provisioning (SP-1, Andrew-gated, ~1-3wk). The enrolment card + SF-1 flip gate on SMS
  BEING SENDABLE (a test SMS delivers -- CVO rubric 6530ac26e0), so neither is exercisable/acceptable
  now. Evidence: AE 19113 (0 origination identities); CVO 19129 (sendable-not-deployed gate ruled in).
- **SITEZ -> CLOUD merge blocked (not my fix):** MSTR 19227 -- the register-row act made the SB-SITEZ +
  SF-SITEZ TOs non-compliant (no `<decomp_ref>`). Fix is COO's as TO issuer (add decomp_ref citing the
  decomp DELIVERABLE, not a runs/ path). My workspace commits are on origin/SITEZ but do not reach CLOUD
  until this clears. My DE1/DE2/DE3 TOs also lack decomp_ref (pass only at ADD-time; a re-add refuses).

---

## Current State (handoff)

**PLATFORM_OPS_USERMGMT (D12 login UI): COMPLETE + ACCEPTED, live in PROD.**
- Promote v2.1.174 (PROD 529f3093) serves the fixed client 087a456f; email MFA works end-to-end
  (andrew@ real login 07:43Z). Deployed backend opalinvest-auth-handler = RIAv5cTF (@15:54Z), Act B
  (login issues, sends nothing) + /auth/mfa/send live + Act C idempotent + F-11 fixed.
- DE1-1 FULLY PASS + accepted (CTO 18749/19128): client-gate (browser #77/#78) + server oracle on BOTH
  handlers (mfa_code_rotated pre-Act-C via F-8's run; mfa_code_sent post-Act-C via my UI run, T1 bracketed).
- F-10 (refresh cookie resolves by email -> survives fixture delete+remint): my surprise, AE's plane, tracked.

**D12_PHONE_OTP_ALL_AWS (SMS OTP): SF lane -- foundation committed, rest SP-1-gated.**
- SB-1..9 (AE) APPLIED @15:23Z, email-no-regression 12/12, E1/E7/E8/S4 certified (E1 after F-11 fix).
  Enrolment endpoints LIVE: POST /auth/mfa/enroll/{send-code,resend,verify} (Bearer, account-from-session)
  + updateMfaPreference CHANNEL-ONLY (SB-8 sole writer of {phoneNumber, phoneVerifiedAt}).
- SF-3 done (17c9a829, LOCAL). SF-2 PART 1 (client API on AuthContext) done (653587f, LOCAL):
  requestEnrollmentCode/resendEnrollmentCode/verifyEnrollment/setMfaChannelSms + EnrollmentChallenge type,
  store-behind-verify structural, tsc -b clean.
- SF-2 PART 2 (UI) fully specified, NOT started: dismissible card on MarketPerformance (/market landing,
  surface (c), CTO 19040) opening an inline phone-capture/verify flow (E.164 /^\+[1-9]\d{6,14}$/, no
  new route); primitives Button/Card/Panel; card-alone (no user-menu exists). F2 scores the client
  contract; F1/F3a/F4/F5 grade against the SB atoms (CVO rubric 0718fd183c).
- SF-1 (flip sms available -> "reflect the stored channel, not a selectable radio", CTO 19021) gated on
  the sms-SENDABLE condition.

**MFA UI-sync check (Andrew-requested, 19259): ANSWERED (reply 175104Z to CTO).**
- The 13 db-flipped email users are sync'd: the deployed email login gate (auth.ts:104-105) reads ONLY
  mfaEnabled+mfaChannel; every phoneVerifiedAt/phoneNumber read is SMS/enrolment-only, so a
  {email, no phone} user is field-identical. Promote-gap clean (DEV==PROD on all auth files).
  Bound stated: no fresh completion walk (fixture deleted, won't drive a live human); completion rests
  on andrew@ + AE 12/12 on this build.

---

## Next Steps

1. **[0.0.0_AB_MSTR / integrator]** push portal DEV local (17c9a829 + 653587f) to origin/DEV; push/merge
   the workspace tree onward.
2. **[2.0.0_SA_COO~Z]** add `<decomp_ref>` to SB-SITEZ + SF-SITEZ TOs (cite the decomp deliverable) to
   unblock the SITEZ->CLOUD merge (MSTR 19227). The 6 PLATFORM_OPS TOs share the latent gap.
3. **[0.4.0_DT_ClientPlatform~Z / DT]** promote SF-3 + SF-2 part 1 (+ the PLATFORM_OPS docstring hygiene
   that ships with SF-3) on the next portal promote, once SF closes.
4. **[this seat / next session]** on SP-1 landing: build SF-2 part 2 (the enrolment UI) against the live
   endpoints + render-verify + F2 round-trip; flip SF-1 once a test SMS delivers. Everything is specified.
5. **[1.0.0_SA_CTO~Z / 0.7.0_AE_CloudOps~Z]** optional MFA-sync gold walk needs an AE email-fixture re-mint;
   offered, awaiting call.

No half-landed deploy, no open ledger entry at this seat. The only integration loose ends are the two
LOCAL portal commits (integrator's leg) and the COO TO-decomp_ref fix (names above). Standing down.
