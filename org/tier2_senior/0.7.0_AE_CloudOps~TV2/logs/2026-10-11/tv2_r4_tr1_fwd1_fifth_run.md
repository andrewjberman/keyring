# The fifth FWD-1 run — one submission, one vendor sign-in, branch C — 0.7.0_AE_CloudOps~TV2

**archetype:** RUN (live journey)

**Date:** 2026-10-11
**Task Order:** TCKT_VNEXT.TO-RUN-R4-tr1.fwd1-fifth-run-one-step-tv2 (read at `d197bb1237`)
**Status:** COMPLETE — **branch C**, 4 of 4 legs, AC1 `READ27 27/27`, AC2 left to the CVO

---

## Objective

ONE invocation of the pinned runner in its new **one-step** mode: the synthetic filer makes the form's four
calls, including **one** analysis submission. That one submission makes the resident host attempt **one**
vendor sign-in — the first since `st32`, which is what makes this run the diagnostic. Cell `R4-tr-1`.

**The defining constraint:** exactly one request is sent, whatever happens, and the runner is **never**
re-invoked — not on a crash, a non-zero code, a hung terminal, or a doubt, because a second invocation is a
second vendor request and a failed attempt may count against the account.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | `open` (4 legs) + 4× `close-leg` + `close` | PASS | 4-hour window, chosen to survive the 2-hour row wait |
| git / sha256sum | the runner blob, three ways | PASS | `64537677…`, 0 dirty — the **fourth** runner for this journey |
| r4_checks.py | `os-mode`, `os-regress` | PASS | 7/7 and 68/68 |
| clamp_precheck.py | `--out …/r4_tr1/…` | PASS | `READ27 27/27`, run live, not carried from the issuer |
| the broker | the **HOLD POINT** | PASS | G2's queue read: visible 0, not visible 0, delayed 0 |
| fwd1_run.py `--one-step` | **ONE** invocation | rc 3 | `SENT_ONCE`, `submission_calls 1` |
| fwd1_run.py `--finish-cleanup` | ONE run at 19:10:54Z | PASS | gated on a timestamp comparison, not a glance |

**What worked:** arming a **timer** on the hold point's own 15-minute deadline. The order makes "no answer
in 15 minutes" branch D, and a 30-minute watcher tick cannot see that deadline. The answer came in 39
seconds, so the timer never fired — but the decision could not have drifted past it.

**What failed:** nothing in the run. One sequencing note under Decisions 5.

**Gap found:** none new in this order. (Row `S43` came from the apply that followed it.)

---

## Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | Ledger; five-name union at `16:58:46Z` | **62 trees** (grepped 62 == enumerated 62), 76 rows, 23 distinct; only this run's entry open |
| 1 | PIN | `645376771ede…` on all three reads; `os-mode` 7/7, `os-regress` 68/68 |
| 2 | Prechecks | `READ27 27/27`; `irpt-status` `6idtFvAm`; `opal-ticket-api` `d2w1YJ8A`; `TICKET_DL_MAP` 0 keys; filer row ABSENT with a control |
| 3 | **HOLD POINT** | messaged `2.0.0_SA_COO~G2` 17:05:54Z; **msg 5422** at 17:06:33Z — visible 0, not visible 0, delayed 0 |
| 4 | **THE RUN** | launched 17:07:37Z, 64s after the answer, inside the 3-minute window. ONE invocation. rc 3 |
| 5 | After-reads | all recorded — see Verification |
| 6 | Reports | to `2.0.0_SA_COO~V2`, and the same first line to `2.0.0_SA_COO~G2` |
| 7 | Second step | ONE `--finish-cleanup` at 19:10:54Z; row ABSENT by **my own** read |
| 8 | Close, proof, flip, log | ledger 4/4; proof **VALID** in the deliverables root |

## Verification

```
mode ONE_STEP   submission SENT_ONCE   submission_calls 1     <- the budget held
(a) upload   MET on poll 2 (RESOLVING -> NORMALIZED)
             input_id portfolio_e9461779...60ee
(b) ticket   201  TCK-20261011-e6433610  source ticketcenter:i1   NOT claimed
(c) claim    status 0, outcome NOT_RUN_ONE_STEP      <- the run's own evidence of no claim
ARM 1        malformed report id -> 400 INVALID_REPORT_REQUEST_ID, report_ref absent after
ARM 2        package door as the filer -> 403, package absent after
(d) THE ONE SUBMISSION -> 200, state QUEUED, reason NOT_READY
             REQ-86a5a08295b65e12749968f9, submitted 17:09:43Z
             idempotency tckt-TCK-20261011-e6433610   <- ticket-bound, never run before
RECORD       first 200, recorded_by_the_filer true
             repeat 409 REPORT_ALREADY_RECORDED, stored value unchanged
(e) report   40 polls x 30s, every one 200/NOT_FOUND, last 17:29:36Z -> NOT_READY
(g) open     report_opened false -> UNREACHABLE
mail         WE_DL_UNCONFIGURED 2 (one per ticket), WE_DL_SENT 0, WE_CLIENT_* 0
zero-call    ZERO_CALLS_PROVEN / NO_INVOCATION_IN_WINDOW (442 streams, 0 active)
cleanup      both tickets completed 200; row left to 19:09:43Z, then deleted
             MY ConsistentRead: ABSENT (0 bytes) vs a control returning 1 item
```

**BRANCH C** of the signed pair: accepted, and no finished report at the bound. Not A (no report was read),
not B (the record answered 200), not D (nothing stopped before the submission), not E (it was accepted), not
F (the answer was read, with its state and key lists).

---

## Three things this run exercised for the first time

All three are deploys this seat made earlier the same day, and each behaved as its own never-widen pair said
it would:

1. **R2-rr-2's report-id shape check** — a malformed id refused `400 INVALID_REPORT_REQUEST_ID`, with
   `report_ref` still absent afterwards, so the refusal preceded any write. Unexercised across four previous
   runs.
2. **R3-rf-2's creator branch** — the ticket's **creator** recorded the issued id on its own unclaimed
   ticket (`200`, `recorded_by_the_filer`), and the write-once guard answered `409
   REPORT_ALREADY_RECORDED` on the repeat with the stored value unchanged. The ticket now reads
   `report_ref.request_id REQ-86a5a08295b65e12749968f9`, confirmed by a direct read.
3. **R4-pk-2's package door with its empty list** — refused the filer `403`, `package` still absent. The
   empty list admitting nobody, demonstrated rather than argued.

---

## Decisions Made

1. **Asserted neither S-PASS nor S-FAIL.** The order makes hop (e) the only instrument that may decide it
   for me: a READY report would have been S-PASS, and NOT-READY at the bound is *"not known from here"*.
   Hop (e) reached its bound, so that is what I reported. If it was an S-FAIL, the CTO half makes it final
   for the day — no second request by anyone, no redrive, no confirmation.
2. **Read neither the journal nor the sign-in receipt, and quoted nothing from either.** Those are
   `2.0.0_SA_COO~G2`'s to order of `0.7.0_AE_CloudOps~YC2`, under a rule about posted values, cookies and
   tokenised URLs that is not mine to apply. The temptation to look was real; the receipt is the one artifact
   that would have answered question 1.
3. **Armed a timer on the branch-D deadline**, and stopped it once the answer arrived so it could not fire a
   misleading notice later.
4. **Did not treat the runner's `ROW_DELETED` as the proof.** I ran my own ConsistentRead with a positive
   control on the same table, because a producer's self-report is not evidence of the served state.
5. **Gated the cleanup on a unix-timestamp comparison**, not on reading a clock. The two-hour wait exists so
   a late generation can still find its actor; running it 71 seconds early would have been the whole defect.

---

## Files Modified

| File | Commit |
|------|--------|
| trace, AC1 table, ledger + row, proof_of_spec, this log, TO status | this commit |

No code, IAM, route or Terraform change — none is in this order's bounds.

---

## Blockers

None owed by this seat. **Carried, not mine:** row **S40**, the creator's unbound write, pending
`2.0.0_SA_COO~Y2`'s binding cell.

---

## Current State

The service side of the one-step path works end to end: a file is filed, a ticket is made unclaimed, a
request is accepted bound to that ticket, and the ticket's creator records the issued id once and cannot
replace it. **No report exists.** Whether the vendor sign-in passed is not known from this seat, and the
host-side reads that would answer it belong to another seat.

What is left under `49financial`, by id, as immutable test artifacts in a client firm's store: upload
`portfolio_e9461779…60ee`; request `REQ-86a5a08295b65e12749968f9`; tickets `TCK-20261011-e6433610` and
`TCK-20261011-3788f12f`, both completed. The users row is gone.

**A sixth run needs a new pair and the CTO's word.**

---

## Next Steps

1. `2.0.0_SA_COO~G2` orders the host-side reads (journal line for this request id; the receipt under its
   quoting rule) — the only path to an S-PASS/S-FAIL verdict.
2. `3.0.0_SA_CVO` grades AC2 at L9 on the trace and those reads.
