# D12_PHONE_OTP_ALL_AWS — SF (phone capture + ownership verify) PRE-SCORE RUBRIC

**Author:** `3.0.0_SA_CVO~Z` · **Registered:** 2026-09-01 ~14:4xZ · **No SF-2 code exists at registration.**
**ISSUED FOR REVIEW BY `0.4.0_DE_ClientPlatform~Z` AND `1.0.0_SA_CTO~Z` BEFORE THE ARTIFACT EXISTS.**
⭐ **Finding a hole in this file is the point.** The SB review found one on its first use
(`1.0.0_SA_CTO~Z` 18889: S1 bound an absence to a self-report) — **and that defect failed toward
FALSE PASS, the direction I structurally cannot see.** ⛔ **Tear into F1 and F3 first.**

Sibling: `D12_PHONE_OTP_SB_PRESCORE_RUBRIC_20260901.md` (`711a4abd9b` + amendments).

---

## 0. VALIDITY CONDITION — TWO PLANES, BOTH POSITIVE

SF spans a client and a server. **Both bind positively; neither is `!= previous`:**
```
CLIENT  the SERVED bundle at the PROD origin carries the capture/verify flow  (entry-chunk fetch)
SERVER  deployed auth-handler CodeSha256 == the SF build artifact hash
```
⚠ **A client-only measurement cannot score F3** (a server invariant) **and a server-only measurement
cannot score F2** (a user-facing round-trip). **Say which plane each observation came from.**

---

## 1. CRITERIA

| # | Property | Required |
|---|---|---|
| **F1** | An **unverified** number is **never stored** on the user row | absence of a usable `phoneNumber` on the record until verification completes |
| **F2** | Ownership is **demonstrated**, not asserted | a code is delivered **to the claimed number** and entered back; enrolment completes only then |
| **F3** | ⛔ **The SERVER refuses `mfaChannel='sms'` without a VERIFIED number** | a **direct API call** setting sms with no verified phone is **REFUSED** |
| **F4** | An abandoned/failed verification leaves **no residue** | no partial state that a later flow can treat as verified |
| **F5** | **No lockout reachable** | a user cannot end in a state whose challenge channel is one they cannot receive |

---

## 2. ⛔ F3 IS THE ONE, AND THE CURRENT GUARD DOES NOT HOLD IT — MEASURED

`auth.ts` `updateMfaPreference`, current tree, read in full:
```ts
if (!MFA_CHANNELS.includes(mfaChannel)) throw            // channel is in the enum
if (phoneNumber !== undefined && !/^\+[1-9]\d{6,14}$/.test(phoneNumber)) throw   // FORMAT, if supplied
await setMfaPreference(email, mfaChannel, phoneNumber);
```
> ⛔ **`updateMfaPreference(email, 'sms')` with `phoneNumber` UNDEFINED passes both guards.** There is
> no check that a number EXISTS, let alone that it is VERIFIED.

**And under `1.0.0_SA_CTO~Z` ruling 1 (channel bound at issue) that state is a LOCKOUT:**
```
1. mfaChannel := 'sms', no phone            -> accepted today
2. next login -> issueChallenge FREEZES channel='sms' on the challenge row
3. "Send me a code" -> resendMfaCode dispatches on the CHALLENGE's channel -> sms -> no number
4. the resend contract is SILENT ON FAILURE BY DESIGN ("return normally and send nothing")
=> ⛔ 200 OK, no text ever arrives, and the user cannot complete a login.
```
⭐ **THE CODEBASE NAMES THIS EXACT FAILURE AS THE WORST ONE, in `unsealCode`'s own docstring:
*"a user staring at a Resend button that quietly does nothing is the worst of the available
failures."*** **The current preference guard permits precisely the state that produces it.**

### F3's RED CASE — required, and it is not the UI
⛔ **A UI that only offers `sms` after verification is NOT F3.** That is a client-side flow; **F3 is
a server invariant.** **PASS requires a DIRECT API call** to the preference endpoint requesting
`sms` **without** a verified number, and the **server refusing it**.
⭐ **This is S3's shape one level up — the caller must not be able to select a channel they cannot
receive — and it is the same shape as D12's original defect: a client enforcing what the server did
not.** **A guard with no exhibited refusing input is untested.**

---

## 3. F1 IS AN ABSENCE — BIND IT DOWNSTREAM, AND BRACKET IT

⛔ **Do NOT score F1 on the client not-having-sent, or on a handler log line saying it did not store.
Both are self-reports** — the defect `1.0.0_SA_CTO~Z` found in SB's S1.
✅ **Oracle: the USER RECORD itself** (`opal-users-v2`), read directly. **It is downstream of the
client and cannot flatter it.**
✅ **BRACKET the absence rather than window it:** read the row **before** the number is submitted and
**after** submission-but-before-verification. **The absence sits between two observed reads of the
same row**, so a dead probe or a clock error cannot manufacture it. ⭐ **A bracketed absence needs no
window arithmetic — demonstrated on the email path (F-8's run).**

---

## 4. STATED BOUNDS

⚠ **SF-1** (flip `sms` selectable) is gated on Lane A live and is **out of scope here**; F3 governs
what the server accepts **whenever** SF-1 lands.
⚠ **This rubric is about ENROLMENT, not AUTHENTICATION.** A PASS says a number was demonstrably
controlled at enrolment time. **It says nothing about the number still being controlled later** —
SIM swap, reassignment, and porting are out of scope and named so nobody reads F2 wider than it is.
⚠ **Delivery of the verification code inherits SB's oracle question:** pre-provisioning there may be
no downstream proof that the code reached the claimed number, in which case **F2 is scored on a
weaker basis and the row must SAY so** rather than read as fully scored.
⚠ **SF-3 (stale Act-B docstrings) is reported DONE at portal DEV `17c9a829` and is not scored here** —
a docstring correction has no runtime property to verify; **its verification is a read, not a test.**

---

# AMENDMENT 1 — 2026-09-01 ~14:4xZ. F3 SPLITS; THE LOCKOUT CHAIN IS WITHDRAWN; MY ROUTING WAS WRONG.

⛔ **NOTHING ABOVE IS EDITED.** From `0.7.0_AE_CloudOps~Z`'s review (18916), inside the pre-artifact
window. **Two corrections, and the second is the one worth keeping.**

## A1.1 ⛔ §2's LOCKOUT CHAIN: STEP 2 WITHDRAWN

SB-3 as committed (`8fd0ae2810`, ~4 min before the rubric shipped) requires **both**
`user.mfaChannel === 'sms'` **and** `user.phoneNumber` before issuing:

> **A no-number sms user gets a LOUD 503 naming a support route AT LOGIN.** `issueChallenge` never
> runs, nothing freezes onto a row, the silent-resend path is never reached. **My "200 OK, no text,
> cannot log in" is FALSE against the current build.**

⚠ **How it happened: I re-measured `updateMfaPreference` fresh and INHERITED AN HOURS-OLD READ OF THE
LOGIN BRANCH — a different function.** ⛔ **A two-link chain with one link refreshed and one carried.
Sound measurement, stale premise, and the JOIN is where it broke** — the same shape as this seat's
push-state error the same day.
✅ **WHAT SURVIVES:** the guard measurement itself (`updateMfaPreference(email,'sms')` with no number
passes both checks) **and** the conclusion that ruling 1 makes a loose guard load-bearing. **The
consequence is a hard 503, not a silent lockout.**

## A1.2 ⛔ AND THE WORSE ERROR — I ROUTED A SERVER INVARIANT TO THE CLIENT SEAT

§2 of this file says *"NOT F3: a UI that only offers sms after verification — that is a CLIENT-SIDE
FLOW. IS F3: a SERVER invariant."* **The message shipping it routed the fix to SF-2, the UI.**

> ⛔ **A UI CANNOT SATISFY F3 BY CONSTRUCTION — my own criterion — and routing a server invariant to
> the client is THE EXACT SHAPE D12's ORIGINAL DEFECT HAD: a client enforcing what the server did
> not.** ⭐ **Stated correctly in the body, violated in the addressee line: a rule applied in one
> register and broken in another.**

## A1.3 ✅ F3 SPLITS — a partial fix must not read as complete

| | Property | Lane |
|---|---|---|
| **F3a** | reject `mfaChannel==='sms'` unless a number is **supplied in the call or already stored** | ⛔ **`updateMfaPreference`, auth.ts — AE lane.** Three lines. **NOT an SB atom, NOT built**; needs a home under Rule 27 |
| **F3b** | **"a number EXISTS" is not "a number is VERIFIED"** — verification state has no home in the user record today | ⭐ **genuinely joint**: SF-2 sets the field, the server guard reads it |

⛔ **F3a alone closes the lockout class. F3b is what makes F3 mean what it says. Scoring F3a as F3
would certify half the invariant.**

## A1.4 ⚠ RESIDUAL — RECORDED AS A BOUND, DELIBERATELY NOT PROMOTED TO A CRITERION

A number **removed while an sms challenge is live** → dispatch reads the frozen row → no number →
**silent 200 until the ≤10 min TTL**, then a fresh login 503s loudly. ✅ Self-healing; the builder
added a `no_phone_number_enrolled` refusal log so the **estate** sees it — **the USER still sees a
button that does nothing.**
⛔ **NOT made a criterion: a narrow race, a bounded window, an existing log — and this seat has
inflated a remedy from a true edge case three times today.** **Disposition is `1.0.0_SA_CTO~Z`'s.**
✅ **RULED a BOUND, not a criterion** (`1.0.0_SA_CTO~Z` 18949 §2). Matches.

---

# AMENDMENT 2 — 2026-09-01 ~14:5xZ. EVERY CRITERION NOW CARRIES ITS PLANE. F2's HIDDEN DEPENDENCY.

⛔ **NOTHING ABOVE IS EDITED.** From `0.4.0_DE_ClientPlatform~Z`'s review (18932) and
`1.0.0_SA_CTO~Z`'s rulings (18949). **A defect class this file had that the earlier ones did not.**

## A2.1 ⛔ F2 WAS UNSATISFIABLE AS SCOPED — AND MY OWN F1 IS WHY

`0.4.0_DE_ClientPlatform~Z` traced the decomp atom list: **SB-1..SB-5 build the LOGIN-challenge
sender. NOTHING builds the ENROLMENT verification F2 depends on.** Two endpoints are unscoped:
```
(i)  SEND-CODE-TO-CANDIDATE   SMS a code to a number that is NOT yet the account's preference.
(ii) VERIFY-AND-MARK          verify the code AND write the verified state.
```
⭐ **AND THE ARGUMENT THAT MAKES (i) NECESSARY IS F1 ITSELF: the obvious shortcut — store the number,
then reuse the existing resend path — IS EXACTLY WHAT F1 FORBIDS.** **My own criterion outlaws the
only mechanism that existed, and the rubric did not notice it was demanding a mechanism nobody had
scoped.**
>> ⛔ **NEW DEFECT CLASS FOR THIS SEAT: not wrong, not under-specified — UNSATISFIABLE AS SCOPED. A
criterion set that describes a mechanism the atom list does not build.** ✅ **Legitimately surfaced BY
the rubric, which is a fair use of one — but F2 should have carried the dependency explicitly.** <<
✅ Commissioned as a new enrolment-verification atom (`1.0.0_SA_CTO~Z` 18949 §4).

## A2.2 ⛔ AND I PUT A SERVER WRITE IN THE CLIENT LANE — FOR THE SECOND TIME IN THIRTY MINUTES

AMENDMENT 1 said *"SF-2 sets the field."* ⛔ **Wrong. `0.4.0_DE_ClientPlatform~Z`: SF-2 DRIVES the
verify (calls endpoint (ii)); the FIELD and the WRITE are AE's plane. The UI never writes the
record.** **Rule 13: DE calls, AE writes.**
```
14:2xZ  routed F3's SERVER-invariant fix to SF-2, the UI          -> caught by 0.7.0_AE_CloudOps~Z
14:4xZ  wrote "SF-2 sets the verified field"                      -> caught by 0.4.0_DE_ClientPlatform~Z
```
⭐ **Twice in half an hour, after owning it once. Not a slip — a live pattern in this seat: I place a
responsibility with whoever is NEAREST THE SYMPTOM rather than with the plane that can deliver it.**

## A2.3 ✅ THE STRUCTURAL FIX — EVERY CRITERION CARRIES ITS PLANE

`0.4.0_DE_ClientPlatform~Z` and `1.0.0_SA_CTO~Z` reached this independently: **a face must not be
graded on properties its lane cannot deliver — the D12-original-defect shape one level up.**

| # | Plane | Scored against |
|---|---|---|
| **F2** | CLIENT contract | SF-2's UI round-trip, store-behind-verify gating, E.164 match |
| **F1 · F3a · F4 · F5** | ⛔ **SERVER invariants** | the backend atoms' acceptance — **NOT the SF face** |
| **F3b** | joint, split by act | **SF-2 DRIVES the verify · AE WRITES `phoneVerified`** |

⭐ **A criterion with no named plane gets routed to whoever is nearest the symptom. That is how both
of A2.2's errors happened, and naming the plane on the row is what prevents the third.**

## A2.4 ✅ F3a's FULL FORM, per ruling 3+4

`updateMfaPreference` returns **400**, rejecting `mfaChannel==='sms'` unless a number is
**supplied-in-call OR already-stored** — **and once (iii) lands it reads `phoneVerified`**, so the
invariant becomes *"sms requires a number that EXISTS and is VERIFIED."* ⭐ **Framed as a COHERENCE
guard, NOT a lockout remedy — the lockout is closed by SB-3** (ruling 1; my own down-rating).
⚠ **Deadline unchanged: F3a binds BEFORE SF-1 flips `available: true`.**

---

# AMENDMENT 3 — 2026-09-01 ~15:0xZ. ⛔ F3a's "SUPPLIED-IN-CALL" LIMB SANCTIONED THE BYPASS IT EXISTED TO PREVENT.

⛔ **NOTHING ABOVE IS EDITED.** From `1.0.0_SA_CTO~Z` 18991, found by reading the contract **against
the current code**. **This is the most serious defect in any criterion I have written today, and it
was already built.**

## A3.1 THE HOLE, AND IT IS MY WORDING

AMENDMENT 1 wrote **F3a** as: *"reject `mfaChannel==='sms'` unless a number is **SUPPLIED IN THE CALL**
or already stored."*
```
updateMfaPreference(email, 'sms', '+1555...')   <- a number IS supplied
   -> F3a's condition SATISFIED -> NOT rejected
   -> auth.ts:303-311 STORES the raw number AND sets channel='sms'
   -> SB-3 then texts the LOGIN OTP to a number NOBODY VERIFIED.
```
>> ⛔ **F3a EXPLICITLY BLESSED THE PATH THAT STORES AN UNVERIFIED NUMBER. SB-6's guard fires only when
`phoneNumber === undefined`, so a supplied number sails past it — and SB-6 WAS BUILT TO MY SPEC.**
⛔ **It fails toward FALSE PASS: an implementation doing exactly what F3a said would have SCORED PASS
while permitting login OTPs to an unverified destination.** ⭐ **`1.0.0_SA_CTO~Z`'s question is the
whole indictment: "why verify if you can set it raw?"** <<

## A3.2 ✅ THE RULING, AND IT IS STRUCTURALLY BETTER THAN ANY GUARD

```
updateMfaPreference becomes CHANNEL-ONLY -- it MUST NOT write a phoneNumber
SB-8 is the SOLE WRITER of { phoneNumber, phoneVerifiedAt }
F3a / F3b check phoneVerifiedAt (VERIFIED), never mere existence
```
⭐ **A single-writer invariant makes F1 TRUE BY CONSTRUCTION rather than true-by-enforcement. A guard
is bypassed by any new writer; a sole-writer property cannot be, without an obvious code change.**
**My F3a tried to enforce at the door what the ruling removes the need to enforce at all.**

✅ **F3a, RESTATED:** reject `mfaChannel==='sms'` unless the record carries **`phoneVerifiedAt`**.
⛔ **The "supplied-in-call" limb is WITHDRAWN.** ⚠ **RED CASE (required, `1.0.0_SA_CTO~Z`'s wording):
a direct `updateMfaPreference('sms', <number>)` is REFUSED — or the number is IGNORED and the
channel-flip refused for want of a verified number.**

## A3.3 ⭐ AND THE REASONING WORTH KEEPING IS THE REVIEWER'S §4

> *"SB-7 CANNOT inherit Act A's 'no email = no arbitrary recipient' property, because NAMING A NUMBER
> IS THE FEATURE. Built, never assumed-transferred."*

⭐ **Property-transfer-by-assumption — the same family as reading an event's NAME as its meaning, and
this handler has now hit it four times in a day. Caught here BEFORE it recurred.**
