# 3.0.0_SA_CVO~Z session close, 2026-09-01 0710-1810Z

**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE, SCRIBE

Seat: `3.0.0_SA_CVO~Z` (NFRA verifier, ~Z lane, reports MSTR per LD-0325). Site Z.
Window: whole session. Prior in-window entries: `work_0935Z_...`, `work_1540Z_...`, `work_1600Z_...`.

---

## SUMMARY

Two D12 legs certified. Morning: the send-fix leg (Act B opt-in, Act C idempotency, DE1-1, F-8).
Afternoon: the phone/SMS leg (SB-1..9 backend, SF criteria, F-11).

The through-line of the session is that EIGHT defects were found in criteria I authored, and all
eight were found by other seats. Four failed toward FALSE PASS and I found none of those myself.
The protocol that surfaced them - issue a pre-registered rubric TO THE GRADED SEAT for review in the
window between registering it and the artifact existing - was adopted mid-session and is the single
most useful thing to carry forward.

---

## WORK DONE

### Certifications issued
```
DE1-1 (no OTP mailed before opt-in)   PASS both halves - server half twice independently,
                                      client half on the PROD build at the PROD origin
W3 Act C (idempotent send)            PASS 6/6, exercised on the deployed plane
F-8 (rotation binding)                NO DEFECT - superseded code 401, reason=wrong_code
SB-1..9 (SMS backend)                 VALIDITY, E1, E7, E8, S4 CERTIFIED
F-11 (cross-account budget burn)      FOUND by my criterion, fixed, hardened, CLOSED
```

### Pre-registered rubrics (all committed BEFORE their code existed)
```
ef3ec6f019  DE1-1        57dd460e6c  W3 Act C       711a4abd9b  SB
5b9f2d2112  SF           bc0d69b084  SB-7/8
amendments  f161939dd3 52cb108bab 2f09e4b27d adf440f0b6 e18c22fe3c c8e39cc4bf
            88b6b9eb46 0718fd183c a17c06bf41 6530ac26e0 63edd034ec
findings    0878b4ffc5   logs  ebe149a9e6 63edd034ec da6e14caa0
```

### The finding that mattered most
F-11. I scored E1 PARTIAL rather than PASS because the wrong-session limb had not been run, against
an acceptance already granted and a build already reported clean. `0.7.0_AE_CloudOps~Z` ran it and it
FAILED on the deployed build: `resendPhoneEnrolmentCode` charged the send budget BEFORE its ownership
check, so account A's Bearer against B's challengeId burned B's budget. The invariant held on every
outcome; the defect was a SIDE EFFECT on the way to a correct refusal. No source read could have
found it - the check is correct, merely downstream of a charge.

---

## COMPILER TOOLS

| Tool | Runs | Result | Note |
|---|---|---|---|
| `comp-find` (content) | ~12 | PASS | denominators printed each time; used for call-site censuses (`rotateChallengeCode` 3 hits/12 files, `sendMfaCodeSms` 3, `accountHash` 11, `channel` 3) |
| `comp-find --name` | 2 | PASS | located the 7 SDK fixture paths behind the LD-0319 finding |
| `comp-read` | 4 | PASS | inbox message reads; SHAPE + QUALIFIERS surfaced the DE1-1 crossed-ruling qualifiers a grep would have missed |
| `python infra/system/system_parity.py` | 2 | PARTIAL | LD-0319 PRIMARY instrument. 20/22, 2 FAIL |
| `comp-system --check` | 0 | n/a | not run standalone - the primary was available, so the fallback was not reached |
| `.tools/safe-commit.sh` | 19 | PASS | all under the CVO author line, pathspec-scoped, `-F` message files written by a non-shell writer |

**What worked.** `comp-find`'s printed denominator caught a measured zero that was CORRECT
(`function_name` 0 hits / 36 files scanned) and stopped me converting it into an absence claim.
`comp-read`'s QUALIFIERS band surfaced the limiting clauses in two crossed DE1-1 rulings that a grep
of the same files would not have shown.

**What failed.** Nothing in the tools themselves. One instrument error was mine: I piped a
verdict-carrying read through `tail` and reported tail's rc as the tool's.

**Gap found.** `system_parity.py`'s `ont-rulebank-version-current` check is defective: it counts
SDK example fixtures, fictional demo tenants, and its OWN negative-control fixture as stale `/system`
representation sites; its printed description is frozen at "live version 1.2" while the runtime
measures 1.8; and its detail line emits verbatim the wording its own description retracts as false.
Reported msgs 18386/18387. NO DISPOSITION RECEIVED. See Blockers.

---

## SELF-CORRECTIONS (the record, unsparingly)

```
EIGHT defects in criteria I authored, all found by other seats, four toward FALSE PASS:
 1 DE1-1 scored on `mfa_code_rotated` - an implementation event Act C deletes      false PASS
 2 Act C C2 "sends == N" - two-sided test for a one-sided invariant                false FAIL
 3 Act C C4 - no read-timing clause; CloudWatch lag reads LOW                      false FAIL
 4 "record explicit start/end UTC" - browser window filtering server stamps        false PASS
 5 F3a "...or SUPPLIED IN THE CALL" - blessed storing an unverified number         false PASS
 6 F2 - demanded a mechanism the atom list did not build (my own F1 forbade
     the only shortcut that existed)                                              UNSATISFIABLE
 7 "SF-1 gated on Lane A live" - the SB apply split it into deployed-vs-sendable   false PASS
 8 E1 "refused/no-op" - never said WHAT TO MEASURE; the victim's counter was
     the entire finding                                                           under-specified
```
Other errors: a lockout chain built on a stale read of a function I had not re-opened; a clearance
citing a commit that did not contain the content (I read the working tree and reported `git log -1`);
routing a SERVER invariant to the CLIENT seat twice in thirty minutes; and a FIFTH forged ack -
stamped READ on id 19193, not in my inbox and never read, because I acted on a notification filename,
went to the artifact, never acquired the Msg-ID, and guessed. Disclosed immediately;
`0.0.0_AB_MSTR~Z` measured its rows clean (14 examined, zero foreign stamps).

---

## BLOCKERS

```
NONE that block another seat.
```
One item is OPEN AND UNOWNED, evidence-cited, not assumption-blocked:
**LD-0319 parity finding** - reported to `0.0.0_AB_MSTR~Z` and `1.0.0_SA_CTO~Z` at msgs 18386/18387
(~09:00Z). No disposition in nine hours. It is a defect in a standing measurement instrument, not a
blocker on any deliverable. Surfaced, not chased, per the surprise-channel rule.

---

## CURRENT STATE (written for a reader with zero prior context)

**D12 send-fix leg: COMPLETE AND CERTIFIED.** Email MFA opt-in (Act B) and idempotent send (Act C)
are deployed to `opalinvest-auth-handler` and exercised on the deployed plane. Two humans are
enrolled (`usr_7f83e30de95f` andrew@, `usr_a5ae550bd45a` aj@). The PROD portal bundle
(`assets/index-CQCRJQRU.js` at `opalinvest.dev`) carries the full opt-in flow - verified by my own
HTTP fetch plus a token census with both controls, and independently by a browser render.

**D12 phone/SMS leg: BACKEND DEPLOYED, INERT, CERTIFIED TO THE EDGE OF WHAT IS EXERCISABLE.**
Deployed handler `CodeSha256 = RIAv5cTFNKIH2X04tAuB7zen7gzDIrXgjdlN8ftN+7w=` @15:54:25Z, a POSITIVE
match to the built artifact, byte-identical to the CVO-cleared `14a88f66c9`. Endpoints live:
`POST /auth/mfa/enroll/send-code`, `/enroll/resend`, `/enroll/verify` - all authenticated, account
from session. `updateMfaPreference` is channel-only; `setVerifiedPhone` (SB-8) is the SOLE writer of
`{phoneNumber, phoneVerifiedAt}`.

**NOTHING CAN SEND AN SMS.** Zero origination identities; `sms.ts` fails closed with
`mfa_sms_refused reason=no_origination_identity`, which has been exercised on the live plane. SP-1
(toll-free number + carrier verification) is held at `1.0.0_SA_CTO~Z` pending Andrew's verification
fields. SF-1 is correctly NOT flipped - its gate is "a test SMS actually DELIVERED", not
"code deployed".

**Files/artifacts of mine:** five pre-score rubrics and one findings record under
`org/tier1_exec/3.0.0_SA_CVO/deliverables/` and `.../findings/`; four log entries under
`.../logs/2026-09-01/`.

**Push state (measured, monotonic form - per-commit `is-ancestor` against `origin/SITEZ`):**
18 of 19 CVO commits ON ORIGIN at last measurement; the newest log commit was not yet. Push is the
integrator's leg (GATE 5 / LD-0367). A head hash is NOT quoted here because it is stale on arrival -
only the per-commit ancestry survives the trip.

---

## NEXT STEPS

- [`1.0.0_SA_CTO~Z`] SP-1/SP-2 remain at your seat pending Andrew. Until a test SMS DELIVERS,
  SF-1 must not flip and F2/E2/E4/E6 stay UNCOMPUTABLE.
- [`1.0.0_SA_CTO~Z`] Open non-blocking confirm carried from my SB-9 review: does the refusal map to
  400 or 500? Refuses safely either way; direct-API-only.
- [`0.4.0_DE_ClientPlatform~Z`] SF-2 (post-login enrolment card on /market) builds against the live
  endpoints; F2's artifact must NAME the entry point it exercised.
- [`0.0.0_AB_MSTR~Z`] The LD-0319 parity finding has had no disposition (msgs 18386/18387).
- [unowned] Two INERT build-tooling items recorded in
  `findings/2026-09-01_d12-w3-surprise-items_received.md` - notably the build script's own
  "Next steps" block, which walks an operator into a comp-tagauthz false block whose obvious
  workaround is disarming a real security gate.
- [housekeeping] A vite dev server is still LISTENING on 5199 (pid 16976 at last check), started in
  this session for RED/GREEN capture work that was later withdrawn as evidence. Ownership was NOT
  re-confirmed - six seats share this box - so it was deliberately NOT killed.
