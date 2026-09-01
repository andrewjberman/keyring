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
