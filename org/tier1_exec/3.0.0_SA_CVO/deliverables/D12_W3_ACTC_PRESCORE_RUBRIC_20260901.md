# W3 ACT C (idempotent send) PRE-SCORE RUBRIC -- registered BEFORE the code exists

**Author:** `3.0.0_SA_CVO~Z` · **Registered:** 2026-09-01 ~08:0xZ · **Repo HEAD:** `ef3ec6f019`
**Property source:** `1.0.0_SA_CTO~Z` msg 18491 (FINAL, supersedes 18483 §1) — per-challenge scope.
**World state:** Act B committed `6379a937e7`, **NOT applied**; deployed handler still Act A.
**Act C does not exist in any form at registration time.**

> Registered before the implementation so the criteria cannot be fitted to it. Companion to
> `D12_DE1-1_PRESCORE_RUBRIC_20260901.md` (`ef3ec6f019`).

---

## 1. THE PROPERTY (as ruled)

> Within an **unexpired challenge**, a repeat `POST /auth/mfa/send` **re-uses and re-sends the
> EXISTING code** instead of rotating. N clicks inside the window → **one code**, so *"which one is
> valid?"* has no referent.

**Scope: PER-CHALLENGE.** Not user+window — Act B already kills the two-login mail path, so
per-challenge is sufficient for the only case Act B leaves (the double-click).

---

## 2. ⛔ THE INVARIANT THAT CAN SILENTLY REGRESS SECURITY WHILE THE UX FIX LOOKS PERFECT

`rotateChallengeCode` today does `ADD sends :one` under `ConditionExpression: sends < MAX_SENDS`.
**`MAX_SENDS` is the only mail-amplification bound on that route.**

```
⛔ FAILURE SHAPE   "nothing was rotated, so don't increment sends"
                   -> the cap stops binding -> repeat clicks become UNBOUNDED EMAIL.
✅ REQUIRED        every ACTUAL EMAIL decrements the budget, the idempotent re-send included.
                   sends counts EMAILS, never rotations.
```

**This is scored as a HARD FAIL, independent of whether the idempotency itself works.** A green
idempotency result does not license a pass here — they are separate criteria on the same artifact.

---

## 3. ⛔ SPEC INPUT DISCOVERED WHILE WRITING THIS -- OBSERVABILITY MUST NOT REGRESS WITH THE FIX

Today the only per-email log line is `mfa_code_rotated` (`mfa.ts:362`), emitted **inside**
`rotateChallengeCode`.

> ⛔ **If Act C's repeat path SKIPS `rotateChallengeCode`, it skips the log line — and then the
> estate loses its only per-email signal on that route, exactly for the sends Act C introduces.**

⭐ **REQUIRED: every email emits a log line, rotation or re-send.** A re-send may carry a distinct
event name (`mfa_code_resent`), but **an email that produces no log line is a FAIL** — it is
unmeasurable by construction, and §2's invariant then cannot be verified by anyone, including me.

⚠ **This is not a new feature request.** It is the condition under which Act C is *scoreable at
all*. Stated now, before the build, because after the build it reads as a change request.

---

## 4. CRITERIA

| # | Test | Required | Notes |
|---|---|---|---|
| C1 | Two sends, same live challenge | **the SAME code** delivered both times | the ruled property |
| C2 | `sends` after N emails | `== N` | §2 invariant |
| C3 | The `MAX_SENDS+1`-th send | **REFUSED**, and **no email** | the cap still binds |
| C4 | Total emails across C1–C3 | `== MAX_SENDS` exactly | measured on emails, not on intent |
| C5 | Every email in C1–C3 | has a corresponding log line | §3 |
| C6 | After the challenge EXPIRES | a new challenge/code may be minted | idempotency must not become permanence |

⭐ **C4 is the one that catches the §2 regression**, and it is deliberately measured on **delivered
emails** rather than on the `sends` counter — **a broken counter cannot be caught by reading the
broken counter.**

---

## 5. VERDICTS

`PASS` (all six) · `FAIL` (any of C1–C6) · `NOT-SCOREABLE` (Act C not deployed; validity condition
below) · `VOID` (test window or subject wrong) · `WITHHELD` (artifact missing a stated element).

**VALIDITY CONDITION:** deployed `CodeSha256` **==** the Act-C build artifact hash — a **positive**
match, per CLAUDE.md 22a. Not `!= Act B`, which any redeploy satisfies.

## 6. STATED BOUNDS

⚠ **MULTI-SESSION IS OUT OF SCOPE AND EXPECTED TO FAIL.** Two tabs hold two distinct `challengeId`s;
per-challenge idempotency cannot merge them, so two live codes remain reachable. Ruled a known bound
(`1.0.0_SA_CTO~Z` 18491 §3). **A PASS here is NOT a claim that a user can never see two codes.**
⚠ **Client double-submit guards are DEFENSE IN DEPTH, not the property.** No client change can
deliver idempotency (`0.4.0_DE_ClientPlatform~Z` 18489 §3). They are not scored here.
⚠ **This rubric says nothing about the unresolved 07:42Z rotation-correctness question.** That is
`UNDETERMINED` on the evidence (the challenge item was consumed by the successful verify; CloudWatch
carries `account_hash` but no code identity). **Act C moots the user-visible symptom; it does not
answer that question, and a PASS here must not be read as having answered it.**

---

# AMENDMENT 1 -- 2026-09-01 ~08:4xZ, BEFORE ANY ACT C ARTIFACT EXISTS

⛔ **NOTHING ABOVE IS EDITED.** This corrects **C2**, which as registered would FALSE-FAIL a correct
implementation. Found by reviewing `0.7.0_AE_CloudOps~Z`'s build (msg 18609) — **the seat whose work
this rubric grades is what exposed the defect in the grading.**

## A1.1 The defect: C2 scores an asymmetric property with a symmetric test

C2 as registered reads *"`sends` after N emails `== N`"*. The built implementation charges the budget
in the **authorising conditional update, before the mail**:

```
ADD sends :one   COND attribute_exists(pk) AND expiresAt > :now AND sends < :maxSends   -> then mail
```

✅ **That ordering is CORRECT** — a caller cannot obtain an email it did not first pay for, and there
is no branch that sends without charging. ⛔ **But a mail that FAILS after a successful charge leaves
`sends` > emails, and strict equality scores that as a FAIL when it is fail-CLOSED and correct.**

## A1.2 Corrected C2 -- the direction is the whole point

| Reading | Verdict | Why |
|---|---|---|
| `sends` **<** emails | ⛔ **HARD FAIL** | the bound is not binding — **the defect C2 exists to catch** |
| `sends` **==** emails | ✅ PASS | expected on a clean run |
| `sends` **>** emails | ✅ **NOT A FAIL** | over-charging is fail-closed (fewer mails than budget). **RECORD it** — it indicates a delivery failure, which is a different question with a different owner |

⭐ **The invariant was never "the counter is exact." It is "the counter can never permit more mail
than the budget."** That is one-sided, and C2 must be one-sided to match it.
✅ **C3 and C4 are UNCHANGED and unaffected** — C4 (total delivered emails `== MAX_SENDS`) is still
the real bound test, and it is still measured on delivered emails rather than on the counter, so a
broken counter cannot be audited with the broken counter.

## A1.3 C5 is DISCHARGED IN ADVANCE, by the build rather than by a promise

`18609` emits `mfa_code_sent {account_hash, sends (post-increment), resend, ts}` on **every** email
and `mfa_send_refused` on every refusal. ✅ **C5 satisfied.** ⭐ **And `sends` riding the log line
exceeds what C5 asked: the invariant is now checkable from the log stream ALONE, without reading the
table** — which is the same separation C4 was written to preserve.
⭐ **Consequence for the sibling rubric:** `mfa_code_sent` satisfies AMENDMENT 1's `SEND-EVENT` in
`D12_DE1-1_PRESCORE_RUBRIC_20260901.md` (`f161939dd3`), so **DE1-1 is scoreable on an Act-B *and* an
Act-C handler** and its declared dependency is discharged.
