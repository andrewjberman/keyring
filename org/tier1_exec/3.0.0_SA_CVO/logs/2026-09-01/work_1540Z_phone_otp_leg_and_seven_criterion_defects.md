# 3.0.0_SA_CVO~Z — D12_PHONE_OTP_ALL_AWS: certified, and seven defects in my own criteria

**Window:** ~14:14Z–15:40Z, site Z · **Seat:** `3.0.0_SA_CVO~Z` · Sibling log: `work_0935Z_…` (the send-fix leg).
**Subject:** the SMS leg — SB-1..9 (backend) + SF (client), pre-registered criteria and certification.

---

## 1. CERTIFIED

```
VALIDITY  gmJnyiaSC… built == deployed @15:23:40Z, POSITIVE match      ✅
S4/SB-4   channel as a PARAMETER on the existing event, live flow      ✅
E7        refusal + number NOT STORED, read off the USER RECORD        ✅
E8        both directions, separate challenges, correct codes, control ✅
E1        unauthenticated limb only                                    ⚠ PARTIAL
```
⛔ **E1 is PARTIAL because the WRONG-SESSION limb was never run** (censused: 0 mentions). **A 401
without a token proves auth is REQUIRED; it does not prove the account comes from the SESSION** — and
only the second excludes an authenticated user driving another account's enrolment. The source
supports it; that is exactly why it may not be scored as exercised. **Closing it needs TWO fixtures
and the fixture is deleted — the cheap moment has passed.** Disposition is `1.0.0_SA_CTO~Z`'s.

**Rubrics (all registered BEFORE their code existed):** `711a4abd9b` SB · `5b9f2d2112` SF ·
`bc0d69b084` SB-7/8, plus amendments `e18c22fe3c` `c8e39cc4bf` `88b6b9eb46` `0718fd183c` `a17c06bf41`
`6530ac26e0`.

---

## 2. ⛔ SEVEN DEFECTS IN MY OWN CRITERIA — ALL SEVEN FOUND BY OTHER SEATS

**This is the useful part of the log. The DIRECTION is the finding.**

```
1  DE1-1 scored on `mfa_code_rotated` -- an IMPLEMENTATION event Act C deletes   -> false PASS
2  Act C C2 "sends == N" -- a two-sided test for a ONE-SIDED invariant           -> false FAIL
3  Act C C4 -- no read-timing clause; CloudWatch lags, low reads as missing      -> false FAIL
4  "record explicit start/end UTC" -- a browser window filtering server stamps   -> false PASS
5  F3a "…or a number SUPPLIED IN THE CALL" -- blessed storing an unverified one  -> false PASS
6  F2 -- demanded a mechanism the atom list did not build (my own F1 forbade
      the only shortcut that existed)                                            -> UNSATISFIABLE
7  "SF-1 gated on Lane A live" -- the apply SPLIT it into deployed-vs-sendable   -> false PASS
```

⭐ **THE ASYMMETRY IS THE LESSON: a false-FAIL criterion is challenged by the seat it accuses, so it
surfaces. A false-PASS criterion is challenged by NOBODY, because everyone it touches is content.**
**Four of the seven were false-PASS and I found none of them.**

⛔ **AND #7 IS THE ONE TO REMEMBER: it was CORRECT WHEN WRITTEN.** Before the apply, "code deployed"
and "SMS sendable" were co-extensive — both false. **The apply split them and a harmless phrase became
a false-pass, with nothing about the text changing.** ⭐ **So the pre-artifact review window must stay
open until the ARTIFACT, not until the words are agreed.**

✅ **The protocol that caught them:** issue the rubric to the GRADED SEAT for review, in the window
between registering it and the artifact existing, saying plainly that finding a hole is the point.
**Amend only while no artifact exists; append, never edit; verify the original survived —
`N insertions, 0 deletions`.**

---

## 3. REUSABLE INSTRUMENT NOTES

- ⭐ **A destructive test affords ONE conclusive attempt per subject.** A verify consumes the
  challenge, so each E8 direction needed its own. `0.7.0_AE_CloudOps~Z`: *"I would have reused one,
  and the second would have failed for the wrong reason while looking like a genuine refusal."*
  **Control first, own subject.** Same shape broke the F-8 design this morning.
- ⭐ **A marker count is DESIRED-plane.** `mfa_purpose_mismatch = 2` says two refusal SITES exist; it
  cannot say two refusals were TAKEN, nor that they are in different functions with opposite
  predicates. **Two sites in one place counts the same.**
- ⭐ **A clearance is of a COMMIT, not of a name.** I cleared `775dc28917`; SB-9 folded in afterwards
  and the deployed artifact was no longer the reviewed one. ⛔ **And I then cited `42c96e00c2` for
  content that was not in it** — I read the WORKING TREE and reported `git log -1`. **`git show
  <commit>:<path>` before citing.**
- ⭐ **A sha match establishes NOT-the-old-build. It never establishes IS-the-new-one, and never
  CAN-IT-WORK.** Positive match against the build artifact, then a byte census, then exercise.
- ⭐ **`1.0.0_SA_CTO~Z`'s ordering call was the leg's most valuable message:** the positive sha, a
  clean `tsc` and the marker census would EACH have passed with email MFA broken for both pilots.
  **Run the LIVE regression before the inert proof.**
- ⭐ **A guard with no exhibited refusing input is untested** — every RED case needs its own positive
  control, or a refusal is indistinguishable from a broken route.

---

## 4. OPEN

⚠ **E1's wrong-session limb** — PARTIAL, needs two fixtures, `1.0.0_SA_CTO~Z`'s call.
⚠ **SB-9's refusal: 400 vs 500** — unverified by me; refuses safely either way, direct-API-only.
⚠ **SP-1** (toll-free number + carrier verification) held at `1.0.0_SA_CTO~Z` pending Andrew. **Until
it lands: no SMS is sendable, SF-1 must NOT flip, and F2 is UNCOMPUTABLE.** ⭐ SF-1's gate is now
*"a test SMS actually DELIVERED"* on the downstream oracle — **not "SP-1 provisioned"**, which a
provisioned-but-broken identity would pass.
⚠ **Act C's transitional legacy-mint branch** — still unexercised; unreachable since ~09:06Z.
⚠ **LD-0319 parity (non-D12, still no disposition):** `ont-rulebank-version-current` counts demo
tenants and its own negative-control fixture as stale, desc frozen at v1.2 while measuring 1.8.
Reported 18386/18387. **Surfaced, not chased.**
