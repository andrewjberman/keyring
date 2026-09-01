# D12_PHONE_OTP_ALL_AWS — SB (SMS sender) PRE-SCORE RUBRIC

**Author:** `3.0.0_SA_CVO~Z` · **Registered:** 2026-09-01 ~14:2xZ · **No SMS code exists at registration.**
**ISSUED FOR REVIEW BY THE GRADED SEAT BEFORE THE ARTIFACT EXISTS** — `0.7.0_AE_CloudOps~Z` asked for
them unsoftened (msg 18849 §5). ⭐ **This is the protocol four of my own defective criteria taught me
tonight: the builder holds the implementation a criterion must survive, and found every one of them.**
**Finding a hole in this file is the point. Amendments are free until the artifact exists.**

Parity source: `D12_DE1-1_PRESCORE_RUBRIC_20260901.md` (`ef3ec6f019`) ·
`D12_W3_ACTC_PRESCORE_RUBRIC_20260901.md` (`57dd460e6c`), both scored PASS on the email path.

---

## 0. VALIDITY CONDITION

Deployed auth-handler `CodeSha256` **==** the SMS build artifact hash — a **positive** match.
⛔ **NOT `!= the Act-C build`**, which any unrelated redeploy clears. Until it holds, every criterion
below is `NOT-SCOREABLE`, never `PASS`.

---

## 1. CRITERIA

| # | Property | Required | Parity source |
|---|---|---|---|
| **S1** | **Act B parity.** A login on an sms-channel account issues a challenge and **sends nothing** | `mfa_challenge_issued` PRESENT · **no SEND-EVENT** between login and the opt-in click · SEND-EVENT PRESENT after | DE1-1 T0/T1/T2 |
| **S2** | **Act C parity.** N sends against one live challenge deliver **ONE code**, never rotating | same code all N times; it is the code sealed **at issue** | Act C C1 |
| **S3** | **Channel authority.** The caller cannot select the delivery channel | a caller-supplied channel is **ignored or refused**; delivery follows the server-side fact | *new — §2* |
| **S4** | **Oracle binding.** SMS emits `mfa_code_sent` with a **`channel` parameter** | **no new event name**; `mfa_challenge_issued` carries the real channel, not the `'email'` literal | *new — §3* |
| **S5** | **Budget.** `sends` counts **every delivery, email and SMS, on one counter** | `sends < deliveries` ⛔ HARD FAIL · `==` ✅ · `>` ✅ not a fail (fail-closed) · `MAX_SENDS+1` REFUSED with **no delivery** | Act C C2/C3/C4 **as amended** |
| **S6** | **Channel stability** | ⛔ **SEE §4 — THIS IS A FORK, NOT A VERDICT** | — |

⭐ **S5 is measured on DELIVERIES, not on the counter** — a broken counter cannot be audited with the
broken counter. On the email path that oracle was the SES `Send` metric; **the SMS analogue must be
named by the builder, and it must be DOWNSTREAM of the handler.**
⚠ **S5 read-timing, carried from Act C AMENDMENT 2:** any count metric requires **two reads separated
in time that agree**. A single immediate read is inadmissible — CloudWatch aggregation lag reads LOW,
and low is indistinguishable from a missing delivery.

## 2. S3 — THE INPUT THAT MUST MAKE IT REFUSE

⛔ **A guard with no named refusing input is untested.** S3 passes only with a **RED case exhibited**:
a send request that names a channel the server-side fact does not, and the delivery going by the
**server's** channel (or being refused) — never the caller's.
✅ Precedent in the existing design: `resendMfaCode` takes only a `challengeId` and resolves the
**recipient** server-side — *"the challenge names its own recipient; the caller does not."* **Channel
is the same class of fact.**

## 3. S4 — WHY THE PARAMETER, NOT A NEW NAME

A new event name would leave **every census keyed on `mfa_code_sent` silently under-counting —
including the C2/C4 invariants certified four hours ago**, which would go quietly stale rather than
fail. ✅ Accepted by the builder without qualification (18849 §4).

---

## 4. ⛔ S6 IS A FORK. IT CANNOT BE PRE-REGISTERED AS PASS/FAIL UNTIL THE DESIGN RULES.

`0.7.0_AE_CloudOps~Z` surfaced (18849 §2) that the TO's option **(b)** resolves the channel **at send
time from the current user record**, so it is **not stable for the life of a challenge**:

> login while set to email → UI says *"check your email"* → preference flipped in another tab →
> Resend → **the code arrives by SMS while the UI says email.** And the login response already handed
> the client a `channel` at issue, so the client is told one thing and a later send does another.

```
IF (b) SHIPS   S6 EXPECTED-FAIL, recorded as a KNOWN BOUND, NOT scored as a defect.
               The behaviour is the specified behaviour.
IF (c) SHIPS   (channel written to the challenge row at issue, from the user record)
               S6 REQUIRED: the delivery channel of every send on a challenge equals the channel
               returned in that challenge's login response. Scored, and a mismatch is a FAIL.
```
⛔ **REGISTERING BOTH BRANCHES NOW IS THE WHOLE POINT: whichever way `1.0.0_SA_CTO~Z` rules, the
criterion is already written and cannot be fitted to the outcome afterwards.**

⭐ **AND THE OBSERVATION THAT MAY BEAR ON THE RULING — Act C made the CODE idempotent; (b) leaves the
CHANNEL non-idempotent.** Andrew's complaint was *"which code is real?"*; the (b) analogue is
*"where will it go?"* **Same class of confusion, different axis.** ⚠ **I am not arguing for (c) —
architecture is `1.0.0_SA_CTO~Z`'s and (b) is the frozen spec. Recording the symmetry because it is
verification-relevant and cheapest to see now.**

---

## 5. STATED BOUNDS — so a PASS is not over-read

⚠ **BILLABLE MULTI-SESSION VOLUME IS OUT OF SCOPE AND EXPECTED TO REMAIN OPEN.** Two live challenges
carry two budgets, so `2 × MAX_SENDS` deliveries are reachable — **structurally the known
multi-session bound, but the denominator changes in KIND from free email to billable SMS** (builder's
sharpening, 18849 §3, and it is a better mechanism than the one I gave). **The only real bound is a
per-user/per-window cap, which is a NEW control outside this TO.** ⛔ **A PASS here is NOT a claim
about spend.** ⚠ And per the standing moratorium **no alarm or monitor is in scope**; SP-2's spend cap
is `1.0.0_SA_CTO~Z`'s leg.
⚠ **Provisioning (SP-1/SP-2) is Andrew-gated. Until sandbox exit, any "delivery" is a sandbox
delivery** — S5's downstream oracle must state which plane it measured, and a sandbox count is not a
production one.
⚠ **This rubric governs SB only.** SF (phone capture + ownership-verify) is a separate face and needs
its own criteria — **notably that an unverified number is never stored, which is an ABSENCE claim and
will need a bracket, not a window.**
