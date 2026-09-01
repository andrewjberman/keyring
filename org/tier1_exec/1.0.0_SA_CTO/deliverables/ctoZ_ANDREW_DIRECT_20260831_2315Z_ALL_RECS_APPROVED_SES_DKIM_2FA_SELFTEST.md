# ANDREW-DIRECT 2026-08-31 ~23:15Z -- "All recs approved" + three new instructions

**Channel:** the site-Z terminal, direct to `1.0.0_SA_CTO~Z`, in response to `/open-calls` (4 cards).
**Recorded:** 2026-08-31T23:15:20Z (measured, `date -u`). **Recorded by:** `1.0.0_SA_CTO~Z`.
**Broadcast:** same turn to `0.0.0_AB_MSTR~Z` and `2.0.0_SA_COO~Z` per org/XXX.md.

---

## HIS WORDS, VERBATIM AND ENTIRE

> All recs approved. Make sure that on the email otp we should be properly set up with SES now that
> its no longer sandboxed. The only thing we will want to clarify is the DNS/DKIM/DMARC and health of
> that service so these things don't go to spam. Furthermore, we will want to do the testing for 2FA
> on my account so we know it works before pushing anything to clients

⛔ **THE PHRASING IS THE RULING. Nothing below re-words it; the readings are stated separately so a
reader can see which is his and which is mine.**

---

## PART A -- WHAT "ALL RECS APPROVED" RESOLVES

The four cards he was answering, with the rec he approved:

| Call | Decision now RULED |
|---|---|
| 1 | **D12 and D7 are placed on SITE Z.** The rest of the register's placement is DEFERRED, not decided. |
| 2 | **The unattended-ticket reminder is OUT of the alarm hold.** Build it. |
| 3 | **Remembered device = 30 days, revocable by sign-out-everywhere.** |
| 4 | **Email OTP only for now; SMS later behind his separate word.** |

### Scope limits on Part A -- read these before acting wider

⛔ **CALL 2 LIFTS ONE THING BY NAME, NOT THE MORATORIUM.** The approved rec was scoped to the
unattended-ticket reminder and argued from it being *"a message to a human inbox about a human's own
work queue, not a monitor on a serving layer."* **The GLOBALALARM hold stands for everything else.**
Nobody may read this as general permission to build alerts, monitors, SNS subscribers or freshness
checkers. A hold lifted by name is lifted for that name.

⛔ **CALL 1 PLACES TWO DIRECTIVES, NOT THE REGISTER.** His ~21:1xZ ruling made device ownership one
whole-register call after the comb; the approved rec explicitly proposed ruling D12 + D7 now and
**deferring the other ten**. So the whole-register decision remains open for D0-D6, D8-D11.

⛔ **CALL 4 IS A SEQUENCING ANSWER, NOT A SCOPE CUT.** He asked for user choice of channel
(email or text). Email-first does not retire the SMS leg; it removes a vendor decision from the
critical path. **SMS still needs his explicit per-use word before any vendor egress.**

⚠ **THE REGISTER EDIT IS NOT MINE.** Placement fields live in `org/missions/DIRECTIVES.yaml`, whose
owner is `0.0.0_AB_MSTR`. This record is the authority; the edit is routed, not taken.

---

## PART B -- THE THREE NEW INSTRUCTIONS

### B.1 SES readiness for email OTP
His words: *"Make sure that on the email otp we should be properly set up with SES now that its no
longer sandboxed."*
**Reading:** verify, do not assume. He states sandbox exit as fact; the instruction is to confirm the
service is actually configured for this use. **A stated premise is still measured before it is built
on** -- and if the account is NOT out of sandbox, that is a finding to report, not a thing to fix
quietly.

### B.2 Deliverability -- DNS / DKIM / DMARC
His words: *"The only thing we will want to clarify is the DNS/DKIM/DMARC and health of that service
so these things don't go to spam."*
**Reading:** a one-time-code mail that lands in spam is a **broken login**, not a degraded one. This
is therefore an ACCEPTANCE CONDITION of the MFA workstream, not a follow-up. "Clarify" is his word --
the deliverable is a measured statement of the current state, and any gap named.
⛔ **This is a DIAGNOSTIC, and it is NOT a licence to build a monitor.** See the Call-2 scope limit.

### B.3 Self-test on his account before any client exposure
His words: *"we will want to do the testing for 2FA on my account so we know it works before pushing
anything to clients"*
**Reading, and it is the sharpest item here: this is a STAGED-ROLLOUT GATE.** He is not asking for a
test case, he is naming an ordering -- **his account first, clients only after.** It binds the
MFA workstream's acceptance and belongs in the PRD as a gate rather than a step.
⚠ **It also implies MFA must be enable-able PER ACCOUNT rather than globally at first**, or the gate
cannot be satisfied -- you cannot test on one account before clients if the switch is fabric-wide.
**That is my inference from his ordering, NOT his words, and it is flagged as an inference.**

---

## CONSEQUENCES FOR THE TWO PRDs

`docs/architecture/D12_PLATFORM_OPS_PRD.md`:
- open decision 2 (remembered-device TTL) -> **CLOSED: 30 days, revocable by sign-out-everywhere**
- open decision 4 (SMS vendor) -> **DEFERRED by his word; email leg proceeds**
- open decision 1 (placement) -> **CLOSED: SITE Z**
- **NEW acceptance gate** from B.3, and **NEW acceptance condition** from B.2
- open decision 3 (auth-handler vs Cognito) -> unaffected; already ruled by CTO arch-gate

`docs/architecture/D7_TICKET_VNEXT_PRD.md`:
- WS-5's reminder leg -> **UNGATED by his word.** Cell was BLOCKED-AT-ANDREW; it is now READY.
- open decision 7 (placement) -> **CLOSED: SITE Z**

---

## WHAT THIS RECORD DOES NOT DO

It does not cut task orders (stage 3 owners do that, now that placement exists), does not edit the
register, does not lift any hold beyond the one he named, and does not authorize vendor egress.

---

## PART C -- ANDREW-DIRECT ~23:5xZ, a second ruling the same night

**Channel:** site-Z terminal, direct to `1.0.0_SA_CTO~Z`. **Recorded by:** `1.0.0_SA_CTO~Z`.
**Broadcast:** same turn, msg 17217/17218, BEFORE this record was written because a seating decision
was pending on it.

### HIS WORDS, VERBATIM AND ENTIRE

> D12 first.

**What he was answering:** `2.0.0_SA_COO~Z`'s fork (17212) -- run D7 OPAL_TICKET_VNEXT in PARALLEL
with D12, or BEHIND it? Its rec was *behind, and start D7 with its architecture read*. My relay added
that the read needs no new seat.

### WHAT IT RESOLVES
- **D12 IS THE PRIORITY; D7 IS BEHIND IT.** The COO rec's rank 1 is ruled.
- **NO NEW LANES SEATED FOR D7.** D7's five READY cells cannot go to an existing seat (Rule 27: one
  Tier-2 instance = one project, and `~Z` is D12's), so cutting them would have meant seating 2-3 new
  lanes and taking the fabric from 4 seats to 6-7 near midnight. That does not happen on an inferred
  authorization.
- The COO's refusal to address D7's TOs to a ROLE CLASS instead of an instance stands: **a class with
  no instance reads as ISSUED and is held by NOBODY** -- measured on this fabric this week, one such
  TO sat three days looking complete.

### ⛔ WHAT IT DOES NOT RESOLVE -- NAMED, NOT DECIDED
He ruled on a message carrying BOTH the COO's rec AND my addition that the zero-cost D7 architecture
read could proceed alongside. **Two words rank D12 over D7; they do not say whether that read is
authorized or whether D7 stops entirely.** Both readings are coherent.
⭐ **AN APPROVAL OF A RANKING IS NOT AN APPROVAL OF EVERY ITEM IN THE MESSAGE THAT ASKED FOR IT.** I am
specifically NOT reading my own proposal as approved because it shared a message with the question he
answered -- that is the exact shape by which a seat widens a sovereign word in its own favour, and the
fact that the act would cost nothing is what makes it tempting rather than what makes it safe.
**D7 is treated as PARKED until he says otherwise.** Nothing is lost by waiting.

### CONSEQUENCE FOR THIS SEAT
"D12 first" applied to `1.0.0_SA_CTO~Z` means this seat's own next act is a **D12** act -- cells
2.3/2.4, which the stage-3 decomp records as CTO-held -- and NOT the D7 read it just proposed.

---

## PART D -- ANDREW-DIRECT 2026-09-01 ~00:4xZ, answering /open-calls (5 cards)

**Channel:** site-Z terminal, direct to `1.0.0_SA_CTO~Z`. **Broadcast:** same turn (17245/17246/17247),
correction first because a production change had been authorized on a false premise.

### HIS WORDS, VERBATIM AND ENTIRE

> 1.) Both the password reset and the otp code, from support and noreply respectively, came to top of
> inbox no junk. 2.) Reseat them. 3.) That's fine let's move it to noreply. 4.) Amend it. 5.) This is
> no issue.

### WHAT EACH RESOLVES

| # | Call | RULED |
|---|---|---|
| 1 | OTP inbox or junk | **INBOX, top, no junk.** ⭐ **W1-10 CLOSES. WS-2's deliverability acceptance condition is MET.** |
| 2 | Re-seat `3.0.0_SA_CVO~Z` | **RE-SEAT.** Infra-class respawn -> `0.0.0_AB_MSTR~Z`'s lane. |
| 3 | support@ -> noreply@ | **AUTHORIZED -- but on a premise I have since FALSIFIED. See below.** |
| 4 | SES use-case amendment | **AMEND IT.** |
| 5 | `opalinvest.dev` renewal access | **"no issue" -- CLOSED, not deferred.** Do not re-raise it. |

### ⛔ ITEM 1 CARRIED A SECOND FACT THAT FALSIFIED ITEM 3's PREMISE

He answered the inbox question AND volunteered that **a password reset from `support@` also arrived.**
My call-3 card asserted *"Your existing password-reset mail is broken ... First real forgot-password
click gets nothing."* **IT IS NOT BROKEN. He received one.**

**MEASURED AT SOURCE after his message.** The live handler `opalinvest-auth-handler` runs as
`opalinvest-auth-lambda-role`, which carries **TWO** SES grants:
- `opalinvest-auth-permissions` -- Allow `ses:SendEmail` on `*`, Condition `ses:FromAddress =
  noreply@opalinvest.dev`
- `ses-send-email` -- Allow `ses:SendEmail` on `identity/*`, **Condition: NONE**

⭐ **IAM IS A UNION OF ALLOWS AND THERE IS NO DENY.** The second statement grants exactly what the
first one's condition excludes. `support@` was never blocked.
⚠ **WHY THE SIMULATION RETURNED implicitDeny IS UNMEASURED.** Candidates: the wrong role
(`portal-auth-lambda-role` also exists) or a resource ARN not matching `identity/*`. **Not asserted.**
The falsification of its CONCLUSION is measured; the cause of the bad simulation is not.

### ⛔ THE REAL DEFECT IS THE INVERSE, AND THE AUTHORIZED FIX WOULD BURY IT

Someone wrote a `FromAddress` condition intending to constrain what this role may send as. **THAT
CONDITION CONSTRAINS NOTHING.** Repointing `support@ -> noreply@` resolves a symptom that does not
exist and **leaves the control that is actually broken**, while making every future reader believe
sending is restricted to `noreply@`. That is worse than the status quo, because it manufactures false
confidence in a control.

**STATE OF ITEM 3: HELD, NOT EXECUTED.** His word authorizes it and his word is not in question --
but the basis I gave him was false, and a sovereign authorization obtained on a false premise is not
one I will execute silently. The corrected picture is with him. A single auth sender is a coherent
reason to do it anyway; that is his to give knowingly. **`0.7.0_AE_CloudOps~Z` instructed to HOLD.**
⛔ **AND NO IAM POLICY IS TO BE WIDENED OR NARROWED ON THIS.** The two-Allow structure is a finding
with its own owner and gate; nothing is failing today.

### WHOSE ERROR

**MINE.** `0.7.0_AE_CloudOps~Z` reported the simulation accurately, labelled it **APPLIED, NOT
EXERCISED**, and wrote *"so not 'production is broken now'; it is 'the first real send fails'"* -- a
correctly bounded claim. **I compressed that into "WILL FAIL on first use" and put it to Andrew as an
open call.** The seat's bound was the thing I dropped. Fourth instance tonight of carrying a claim one
rung past its evidence, and the first to reach a production authorization.
⭐ **`APPLIED, NOT EXERCISED` WAS THE TELL.** An unexercised negative is exactly what a single real
observation destroys -- and one did, from the principal, unprompted.

---

## PART E -- ANDREW-DIRECT 2026-09-01 ~00:5xZ, answering /open-calls (2 cards)

**Channel:** site-Z terminal, direct to `1.0.0_SA_CTO~Z`. **Broadcast:** same turn, 17260/17261/17262.

### HIS WORDS, VERBATIM AND ENTIRE

> All of these functions should be noreply, there is nobody responding to these so noreply is the
> coreect point. on call 2, i want to test it with a few people first, including myself. I want to try
> logging in and seeing that MFA actually works.

### CALL 1 -- REPOINT AUTHORIZED, ON A REASON THAT IS HIS AND NOT MINE

⭐ **HIS BASIS IS SEMANTIC, NOT REMEDIAL: "there is nobody responding to these so noreply is the
correct point."** He gave it AFTER I told him the mailer was broken and then falsified my own claim in
front of him. **So the hold was discharged, not overridden** -- it was never a refusal of his word,
only a refusal to execute a sovereign authorization obtained on a premise we had since destroyed.
⛔ **"ALL of these functions"** -- WIDER than the two senders I named. The census is the criterion and
it must print its denominator; a census of two where he said all is not an answer.
⛔ **THE REPOINT FIXES NOTHING SECURITY-WISE AND THE COMMIT MUST SAY SO.** The
`opalinvest-auth-permissions` FromAddress condition is defeated by a second UNCONDITIONED
`ses-send-email` Allow on the same role. If the commit implies the sender restriction now holds, it
buries the broken control under a resolved symptom -- the precise false confidence this thread nearly
shipped. Executed as `D12_PLATFORM_OPS.W2-SITEZ` @`5486c79a07`.

### CALL 2 -- HE REJECTED BOTH OPTIONS I OFFERED

Ruled: **a NAMED PILOT** -- "test it with a few people first, including myself."
Not a client rollout, and **NOT WS-3-gated**, which was my recommendation. My rec was to wait for
remembered-device because every pilot user is otherwise challenged on EVERY login -- the thing he
himself called *"a little obnoxious."* **A small named cohort answers that objection in a way a full
rollout would not, so his call is coherent and mine was not the only sound reading.** Pilot users will
still feel per-login challenges until WS-3 ships; that cost is accepted, not overlooked.
⚠ **THE COHORT IS NOT NAMED AND MUST NOT BE INFERRED.** No account beyond his own is enabled until he
names them. Measured at the time of ruling: `mfaEnabled` TRUE on exactly **1 of 48** accounts.

### ⚠ MEASURED AND TOLD TO HIM BEFORE HE ATTEMPTS IT

*"I want to try logging in and seeing that MFA actually works."*
**HIS REAL ACCOUNT HAS MFA ENABLED AND HAS NEVER BEEN CHALLENGED.** Exactly ONE account has ever
produced an `mfa_challenge_issued` event -- hash `ab433ad547d5` -- and that was the **deleted test
account**, proven by both emails being addressed *"Hi D12 MFA Test"*. **W1-3's end-to-end exercise was
that account, not his.**
>> So his login is a FIRST EXERCISE, not a re-confirmation, and a failure must be read that way. <<
State verified ready: active, `mfaEnabled` true, `mfaChannel` email, `mustChangePassword` false.
Fallback given: do NOT use password reset as the escape hatch (his record carries the stale February
token traced earlier) -- MFA is one field and can be turned off in seconds.

### MY THREE LANE RULINGS -- decided under my own gate, NOT put to him

1. **`getUserPKByEmail` (`db.ts:66-84`) uses `Limit: 1` on a GSI with no uniqueness constraint.**
   Duplicate emails resolve NONDETERMINISTICALLY and every auth path routes through it. **The only
   real bug from the trace.** Surface the ambiguity; a second match is a data-integrity event.
2. **No test account may use a live human email address.** Cost tonight: two real emails to the
   principal, indistinguishable from production but for a greeting, and a false bug report.
3. **An endpoint sweep must not fire `/auth/forgot-password` against a live sender.** W1-6 was a
   correct test with a real outbound side effect.
⭐ None of the three is a criticism of W1 -- W1-6 found exactly what it was built to find.
