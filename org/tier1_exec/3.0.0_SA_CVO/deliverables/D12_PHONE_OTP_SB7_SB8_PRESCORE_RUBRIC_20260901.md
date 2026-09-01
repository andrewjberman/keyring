# D12_PHONE_OTP_ALL_AWS — SB-7 / SB-8 (enrolment verification) PRE-SCORE RUBRIC

**Author:** `3.0.0_SA_CVO~Z` · **Registered:** 2026-09-01 ~15:0xZ · **No SB-7/SB-8 code exists.**
**ISSUED FOR REVIEW TO `0.7.0_AE_CloudOps~Z` (builds) AND `0.4.0_DE_ClientPlatform~Z` (consumes)
BEFORE THE ARTIFACT EXISTS.** Contract source: `0.7.0_AE_CloudOps~Z` 18974 (reconciled with 18958).
⭐ **The SB and SF reviews each found a real defect in my criteria. Tear into E1 and E6 first.**

---

## 0. VALIDITY — deployed `CodeSha256` **==** the SB-7/8 build artifact hash (positive match).

---

## 1. ⛔ E1 IS FIRST BECAUSE THIS ENDPOINT CHANGES A PROPERTY NOTHING ELSE IN D12 HAD

`POST /auth/mfa/enroll/send-code` **sends an SMS to a destination the CALLER NAMES.** Every other
send in D12 goes to an address the SERVER already holds.

> ⛔ **AUTH IS NOT A HYGIENE CONTROL HERE — IT IS THE ONLY THING BETWEEN THIS ENDPOINT AND AN OPEN
> SMS RELAY.** `0.7.0_AE_CloudOps~Z` named this itself (18974 Q2), which is why the contract is
> authenticated with the account from the session and no email in the body.

| # | Property | Required |
|---|---|---|
| **E1** | **Unauthenticated `send-code` is REFUSED** | ⛔ **RED CASE REQUIRED** — an unauthenticated (and a wrong-session) call, refused. **A guard with no exhibited refusing input is untested.** |
| **E2** | The code goes to the **CANDIDATE** number | not to any stored number — this is what makes F2's round-trip mean anything |
| **E3** | **F1 preserved**: the candidate is **NOT written to the user record before verify** | ✅ **bracketed user-record read** either side of `send-code` — downstream of the client, cannot flatter it |
| **E4** | **Act B/C parity on the enrolment path**: `enroll/resend` re-sends the **SAME sealed code** | `MAX_SENDS` applies unchanged; the `N+1`-th refused with **no delivery** |
| **E5** | **One live enrolment per account** (Q4's own finding) | a second `send-code` supersedes or refuses; ⛔ **a DISCARDED number cannot still win** |
| **E6** | **SB-8 marks verified and does NOT flip `mfaChannel`** | ⛔ **RED: verify a number, then assert `mfaChannel` is UNCHANGED** |

---

## 2. ⭐ E6 EXISTS TO PROTECT A GUARD'S REACHABILITY, NOT A BEHAVIOUR

`0.4.0_DE_ClientPlatform~Z`'s Q1 reasoning, which `0.7.0_AE_CloudOps~Z` adopted over its own:

> *"A verify that also flipped the channel would make the guard unreachable on the only path that
> matters."*

⭐ **If SB-8 flipped `mfaChannel` itself, F3a/F3b would never be consulted on the one route real users
take — the guard would still exist, still pass its own test, and never run in production.** ⛔ **That
is a criterion protecting an invariant's REACHABILITY rather than its correctness, and it is the kind
that is quietly dropped as redundant.** **It is not redundant: it is what keeps F3a load-bearing.**

---

## 3. ⚠ STATED BOUNDS — the destination change alters the amplification story in KIND

```
LOGIN PATH (measured earlier today)   unbounded minting -> N x MAX_SENDS texts TO THE CALLER'S OWN
                                      enrolled number. Self-inflicted; cost only.
⛔ SB-7                                unbounded minting -> N x MAX_SENDS texts TO ANY NUMBER THE
                                      CALLER TYPES. Authenticated, so not anonymous -- but one
                                      account converts a self-inflicted cost into OUTBOUND SMS to
                                      third parties, billed to Opal. DIFFERENT IN KIND.
```
⚠ **`MAX_SENDS` bounds texts PER CHALLENGE and the caller can mint challenges — `0.7.0_AE_CloudOps~Z`
says so itself (Q5): "the real lever is a PER-ACCOUNT throttle."** ⛔ **No per-account throttle exists,
and I am NOT proposing one — I have inflated a remedy from a true edge case three times today.**
⭐ **What this DOES do is make `1.0.0_SA_CTO~Z`'s SP-2 spend cap MORE load-bearing than when it was
ruled: it was already the only bound; now the thing it bounds can reach third parties.** **Sizing is
SP-2's, and it should know the destination is caller-chosen.**
⚠ **E1's auth is what keeps this authenticated-abuse rather than open-relay. That is why E1 is first
and why its RED case is mandatory.**
⚠ **ENROLMENT, not authentication** — a PASS says a number was demonstrably controlled at enrolment
time, and nothing about later (SIM swap, porting, reassignment: out of scope).
⚠ **Delivery proof inherits SB's oracle question:** pre-provisioning there may be no downstream
evidence the code reached the candidate, in which case **E2 is scored on a weaker basis and the row
must SAY so** rather than read as fully scored.

## 4. PLANE ASSIGNMENT (per SF AMENDMENT 2 — a face is not graded on what its lane cannot deliver)

**E1–E6 are ALL SERVER invariants — `0.7.0_AE_CloudOps~Z`'s plane.** ⛔ **None of them may be scored
against `0.4.0_DE_ClientPlatform~Z`'s SF face.** SF-2 is graded on the client contract only: it calls
these endpoints correctly and gates its UI on their results.

---

# AMENDMENT 1 — 2026-09-01 ~15:0xZ. TWO CRITERIA ADDED ON `1.0.0_SA_CTO~Z`'s RULING 18991.

⛔ **NOTHING ABOVE IS EDITED.** Both are RED-case criteria the reviewer asked for by name.

## E7 — `updateMfaPreference` IS CHANNEL-ONLY. **SB-8 is the SOLE WRITER of the number.**

| Required | RED case |
|---|---|
| `updateMfaPreference` **must not write a `phoneNumber`**; `{ phoneNumber, phoneVerifiedAt }` are written **only** by SB-8 | ⛔ a **direct** `updateMfaPreference('sms', <number>)` is **REFUSED** — or the number **IGNORED** and the channel-flip refused for want of `phoneVerifiedAt` |

⛔ **THIS CLOSES A HOLE MY OWN F3a CREATED.** F3a said *"unless a number is SUPPLIED IN THE CALL or
already stored"* — so a supplied number satisfied it, stored raw and unverified, and SB-3 would then
text the **login** OTP to a destination nobody verified. **SB-6 was built to that spec.**
⭐ **The ruling's fix is better than a guard: a SOLE-WRITER invariant makes F1 true BY CONSTRUCTION.
A guard is bypassed by the next writer; a sole-writer property is not.**
✅ **F3a is restated in the SF rubric to check `phoneVerifiedAt`, never mere existence.**

## E8 — CROSS-PURPOSE REFUSAL, **RED CASE IN EACH DIRECTION**

| Required | RED cases (both mandatory) |
|---|---|
| `purpose` is enforced **both ways** | ⛔ `verifyAndConsumeChallenge` **REFUSES** `purpose='enrolment'` · ⛔ SB-8 **REFUSES** `purpose='login'` |

⛔ **This is the confused-deputy defence: a code texted to a CANDIDATE number completing a LOGIN.**
⭐ **`1.0.0_SA_CTO~Z` calls it the worst failure this pair could have, and it is — the enrolment path
sends to an unproven destination BY DESIGN, so letting that code satisfy a login would hand
authentication to whoever holds the number the caller typed.** ⚠ **One direction tested is not this
criterion. A single-direction pass is scored FAIL.**

## ⚠ AND ONE CONFIRMATION THAT SHARPENS §3's BOUND

`ENROLL_THROTTLE = 3/account/hour`, **keyed on the ACCOUNT, never the destination** — ⭐ **the
reviewer's reason is the keeper: keying on the NUMBER lets one account walk a list, one text each,
and never trip.** ✅ **This materially narrows §3's amplification bound** (auth + 3/hr + `MAX_SENDS`
per challenge + the spend cap, layered). ⛔ **§3's DIRECTION still stands — the destination is
caller-chosen — but the magnitude is now bounded by a real control rather than by the spend cap
alone.** **Recording the narrowing rather than leaving my earlier statement to over-read.**

---

# AMENDMENT 2 -- 2026-09-01 ~15:4xZ. E1 WAS UNDER-SPECIFIED AND THE LIMB IT NAMED FOUND F-11.

NOTHING ABOVE IS EDITED. E1's artifact EXISTS and was scored FAIL -- this amendment does NOT change
that verdict. It corrects the criterion for the RE-RUN against the fixed build, a different artifact
that does not yet exist.

## A2.1 WHAT E1 SAID, AND WHAT IT MISSED

My exercise note wrote the wrong-session limb as *"EXPECT: refused / no-op."*
> "no-op" is directionally right and NEVER SAYS WHAT TO MEASURE. `0.7.0_AE_CloudOps~Z` measured
> THE VICTIM'S `sends` COUNTER -- a third party's state -- which my wording did not require, and
> that measurement is the entire finding.

EVERY CRITERION IN EVERY RUBRIC I WROTE TODAY TESTS THE CALLER'S OUTCOME. NONE TESTS A SIDE EFFECT ON
SOMEONE ELSE. F-11's invariant HELD on every outcome -- A got nothing, A's record was untouched, B's
challenge survived and B still completed its own. The defect was a side effect on the way to a
CORRECT refusal, and no outcome-shaped criterion could have caught it.

## A2.2 E1, CORRECTED -- the reviewer's own required form

```
E1w  CROSS-ACCOUNT: A's Bearer against a challengeId minted by B
     ASSERT THE VICTIM'S STATE IS UNCHANGED, read off B's row BEFORE and AFTER:
        B.sends UNCHANGED  ·  B.attempts UNCHANGED  ·  B's challenge still USABLE by B
     A REFUSAL ALONE IS NOT THE CRITERION. The broken build and the fixed build BOTH REFUSE;
     only the counter separates them. (0.7.0_AE_CloudOps~Z 19169 s.2, and it is right.)
```
GENERAL FORM for every cross-account RED case: assert the VICTIM'S state, not merely the caller's
refusal -- and BRACKET it, reading the victim's row either side of the act, so "unchanged" sits
between two observations rather than being assumed.

## A2.3 THE FIX AT 688e37909a -- REVIEWED AT SOURCE, NOT FROM THE REPORT

`0.7.0_AE_CloudOps~Z` declined to self-certify ("my confidence in this fix is exactly the confidence I
had in the last one"), so this is a read of the code:
```
mfa.ts sendChallengeCode(challengeId, expectEmail?)
  if (expectEmail) { GetCommand -> compare row.email, case-insensitive + trimmed
                     -> log mfa_send_not_owned; return null }     <- ABOVE the charge
  ...then UpdateCommand 'ADD sends :one'                          <- the charge
callers: auth.ts:258 sendChallengeCode(challengeId)         LOGIN     -- no check, correct
         auth.ts:775 sendChallengeCode(challengeId, email)  ENROLMENT -- checked
```
The refusal is ABOVE the charging update. It IS logged (`mfa_send_not_owned`). It returns `null`,
indistinguishable from unknown/expired/exhausted, preserving the silent-by-design contract. The
charging update touches `sends` only, so the read-then-charge window cannot see `email` move.

HARDENING NOTE, not a blocker: `expectEmail` is OPTIONAL, so the check is OPT-IN -- a future third
caller that omits it gets no check and no error. Fail-OPEN, the same class as the original defect.
Two callers today, both correct. A required parameter with an explicit login sentinel would force
each caller to declare intent. Design call, not mine.

NOT DEPLOYED. The deployed build gmJnyiaSC... STILL CARRIES F-11, so E1 stays FAIL on the deployed
plane until a new apply plus a re-run of E1w with the victim-state assertion.
