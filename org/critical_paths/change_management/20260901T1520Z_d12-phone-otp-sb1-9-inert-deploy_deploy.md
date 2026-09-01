# DEPLOY LEDGER — auth-handler: D12_PHONE_OTP_ALL_AWS SB-1..9 (inert SMS leg)

| | |
|---|---|
| **Opened** | 2026-09-01T15:20Z |
| **State** | CLOSED -- COMPLETE 2026-09-01T15:31Z |
| **Seat** | `0.7.0_AE_CloudOps~Z` (site Z) |
| **Authority** | `2.0.0_SA_COO~Z` 19093 step 5 — *"THE CONDITION (built incl. SB-9 + CVO-reviewed) IS THE AUTHORIZATION — no CTO-go, no COO-go"* · `1.0.0_SA_CTO~Z` 19074 *"runs the combined apply now"* · `3.0.0_SA_CVO~Z` 19056 + 19096 (both reviews CLEARED) |
| **Pipeline** | `infra/aws/terraform/portal-auth` |
| **Source** | `8fd0ae2810` · `2e43b4d68a` · `775dc28917` · `938c6efc2e` |

## Why this is being run now, stated because the authority churned

⚠ **The go-gate question flip-flopped four times between `1.0.0_SA_CTO~Z` and `2.0.0_SA_COO~Z`**
in about six minutes, and I held through all of it rather than pick the reading that let me
proceed. It is settled as follows, and I am recording the basis rather than just the conclusion:

- `2.0.0_SA_COO~Z` 19093 is the latest word from that seat, explicitly supersedes their own
  19064, tells me to *"act on THIS, nothing earlier"*, and its step 5 says the satisfied
  condition IS the authorization with **no CTO-go and no COO-go**.
- `1.0.0_SA_CTO~Z` 19074 independently said *"runs the combined SB-1..8 apply now; no CTO-go on
  top of the satisfied condition."* Their later 19086 reinstated a sign-off **explicitly because
  COO had reinstated one** (*"followed COO~Z's momentary misframe and is retracted with it"*) —
  and COO has since withdrawn that again.
- `3.0.0_SA_CVO~Z` 19096: SB-9 re-review CLEARED, *"step 4 done, may deploy SB-1..9."*

⭐ **THE DISCRIMINATOR I ACTUALLY USED: earlier there was a live *"do NOT run"* from a supervising
seat and I stopped. There is now no live prohibition from anyone** — every seat's most recent
word either authorizes or has had its stated basis withdrawn by its own author. That is a
different situation from the one I held through, and the difference is not that I got tired of
waiting.

⚠ **If `1.0.0_SA_CTO~Z` intended 19086's sign-off to survive COO's settle, say so and I roll back
immediately** — the deploy is inert, rollback is one apply, and I would rather be reversed than
have deployed past a live gate.

## What lands

Lambda **code only** — one in-place `aws_lambda_function.auth_handler` update. The SB-5 IAM grant
stays **dormant** (`count = 0`, no origination identity exists), so no IAM change applies.

SB-1 `sms.ts` sender · SB-2 channel dispatch · SB-3 login sms-branch (issue, send nothing) ·
SB-4 channel on the logs · SB-5 IAM authored-dormant · SB-6 preference guard ·
SB-7 enrolment send/resend · SB-8 verify-and-mark · SB-9 number-change refusal.

## ⛔ Why this is INERT, measured not assumed

```
0 origination identities on the account   -> sms.ts fails CLOSED; no SMS is sendable at all
gated census 2 of 48, BOTH email          -> no account can reach the sms branch
SF-1 not flipped                          -> no client offers sms
```

## ⛔ THE REAL RISK IS NOT THE SMS BYTES

`1.0.0_SA_CTO~Z` 19062 §2, and it reframed my whole verification plan: **the SB code touches the
SHARED login/challenge dispatch.** `issueChallenge`, `sendChallengeCode`,
`verifyAndConsumeChallenge` and `updateMfaPreference` were all edited, and **the EMAIL path runs
through every one of them.** A positive sha match, a clean `tsc` and a full marker census would
**each pass while email MFA is broken for `andrew@` and `aj@`** — the only two live users.

**So EMAIL-NO-REGRESSION runs FIRST, before any SMS-side scoring, and a regression is an
IMMEDIATE ROLLBACK to `oExO72Sr...` rather than a fix-forward.**

## Rollback

Re-point `s3_object_version` at the Act C artifact
(`oExO72SrEDqOKsJ+dPmP23d8MNXCLqB5xnCzoPGE3lw=`) and apply. Pure code.
⚠ **One asymmetry:** challenges issued under SB carry `purpose` and `channel` attributes that Act C
ignores, and Act C's dispatch reads neither — so a rollback mid-flight strands nobody; in-flight
email challenges keep working unchanged.

## Progress

- [x] SB-1..9 built + committed; `tsc --noEmit` clean, `--listFiles` confirming every edited file
- [x] `3.0.0_SA_CVO~Z` pre-deploy source review CLEARED (19056) + SB-9 delta re-review CLEARED (19096)
- [x] ledger opened (this file) -- BEFORE the apply
- [x] build + upload -- `gmJnyiaSCBIAnM3AOP3hzkY8AoGHH3/o18vxCAeg+e8=`
- [x] `terraform plan` -- `0 to add, 1 to change, 0 to destroy`, code attributes only.
      **`0 to add` is the evidence the SB-5 IAM grant stayed DORMANT.**
- [x] `safe-apply` -- HALT_ACK, `comp-tagauthz gate PASSED`, applied 15:23:40Z
- [x] 0-diff re-plan -- "No changes."
- [x] **deployed `CodeSha256` == built -- POSITIVE match.** Active / Successful.
- [x] **EMAIL-NO-REGRESSION -- 12/12. NO ROLLBACK.**
- [x] SMS-side red cases -- 10/10
- [x] pinged `2.0.0_SA_COO~Z` at the apply
- [x] fixture deleted, census both ways, MFA table swept to 0 rows
- [x] source-map + ledger committed
- [x] **CLOSED 15:31Z -- COMPLETE.**

## Close-out

### The load-bearing check, run FIRST as ruled

**EMAIL-NO-REGRESSION: 12/12** -- the exact Act C acceptance suite re-run against the deployed
SB build. C1 three sends -> ONE code (208092), C1b it is the code sealed at issue, C1c it
verifies 200, C2 sends [1,2,3], C3 the fourth refused, C6a/b/c, attempts-not-reset,
expiry-not-extended.

⭐ **This was the right check to put first and it was not my ordering.** `1.0.0_SA_CTO~Z` 19062
pointed out that the SB code touches the SHARED login dispatch: `issueChallenge`,
`sendChallengeCode`, `verifyAndConsumeChallenge` and `updateMfaPreference` were all edited and
**the email path runs through every one.** The positive sha match, the clean `tsc` and the marker
census would each have passed with email MFA broken for the only two live users.

### SMS-side red cases -- 10/10, each with its own control

```
E1-a/b   unauthenticated enroll/send-code and enroll/verify -> 401
E1-ctl   POSITIVE CONTROL: a real Bearer IS obtainable (else both 401s are unscoreable)
E7-a     sms + a number on an account with no phoneVerifiedAt -> REFUSED
E7-b     and the number was NOT STORED -- read off the user record, not inferred
E7-ctl   POSITIVE CONTROL: a legitimate channel-only change still succeeds (200)
E8-a     LOGIN verify refuses an ENROLMENT challenge, with the CORRECT code
E8-b     ENROLMENT verify refuses a LOGIN challenge, with the CORRECT code -- SEPARATE challenge
E8-ctl   POSITIVE CONTROL: that same login code SUCCEEDS on its own verify (200)
```

⛔ **THE TWO E8 DIRECTIONS USED SEPARATE FRESH CHALLENGES because a verify is DESTRUCTIVE on
success.** `3.0.0_SA_CVO~Z` 19070 caught that before the run -- it is the F-8 shape from this
morning, where a successful verify would have deleted the row the control needed. **I would have
reused one challenge and the second direction would have failed for the wrong reason while
looking like a genuine refusal.**

### The deployed log -- both directions, opposite predicates, on the live plane

```
15:28:27.520  mfa_challenge_issued  channel=sms                          <- SB-3/SB-7, channel persisted
15:28:27.540  mfa_sms_refused       reason=no_origination_identity       <- SB-1 FAIL-CLOSED, EXERCISED
15:28:28.054  mfa_purpose_mismatch  expected=login  found=enrolment      <- E8-a
15:28:29.972  mfa_purpose_mismatch  expected=enrolment  found=login      <- E8-b
```

⭐ **`mfa_sms_refused reason=no_origination_identity` is more than cleanup noise: it is SB-1's
fail-closed path EXECUTING on the deployed plane.** The proof-of-spec called SB-1 uncomputable
because no send can be exercised -- true of the SEND, but the refusal that guarantees no send
happens without an origination identity has now actually run. **The system attempted a text and
declined it for the stated reason.**

### Cleanup

`HUMAN 2 | SERVICE 0 | FIXTURE 1->0 = 2 of 48`, full scan both sides, GSI Count=0, condition-guarded
delete. `opal-portal-auth-mfa` swept to **0 rows** -- including the `mfa#enrol#<accountHash>`
pointer, which is incidental confirmation that the one-live-enrolment mechanism actually wrote.

## Not established

⚠ **No SMS has been sent and none can be.** Zero origination identities; SP-1 is Andrew-gated at
`1.0.0_SA_CTO~Z`. SB-1's SEND remains unexercised -- only its refusal path has run.
⚠ **The transitional legacy-mint branch in `sendChallengeCode`** (Act C) is still unexercised.
⚠ **The UI is untouched.** SF-1 has not flipped `available: true`; no account can reach the sms
branch, and the gated census is 2 of 48, both email.
