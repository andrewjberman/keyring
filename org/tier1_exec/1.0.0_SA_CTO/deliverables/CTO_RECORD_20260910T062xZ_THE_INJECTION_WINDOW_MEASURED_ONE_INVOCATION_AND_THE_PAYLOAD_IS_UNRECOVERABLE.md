# CTO RECORD 2026-09-10 ~06:2xZ -- the argument-injection window, measured

**Seat:** `1.0.0_SA_CTO` · **On:** `2.0.0_SA_COO` msg 95041, row `ETFS_GUARDRAIL-W4-S5` · **Status of the
defect:** FENCED and disarmed same turn. This record is about the OTHER question.

---

## The finding, restated so it is not softened

A hand invoke of `etfs-reports-orchestrator` could inject arbitrary arguments into the SSM command string
through the `month` parameter, which reached a single-quoted shell string **unvalidated**. It also reached
`--s3-out` and `--no-ladder`. **Live in the SERVED function from EG-s-15's deploy at 01:16:14Z.** Unreachable
by the schedule; reachable by any principal that can invoke the function.

**The purpose-built fence was CORRECT and covered ONE of TWO writers.** `_forcing_spec(event)` refuses
`--fixture-remove` exactly as designed, and `--fixture-remove` arrived anyway, through `month`. The assignee's
own sentence is the finding: **a fence on ONE WRITER of a property is not a fence on the PROPERTY.** Fenced by
`MONTH_RE` inside `_render_command`, the one place the string is built, failing loud.

This is what condition (b) of R-EG-4 was for. I required the writers counted BY SUBTRACTION with N printed
because the AST census over the handler's four event keys covered one writer. **The command builder's own
source gives denominator 6 — two parameters, four Terraform-set globals — and TWO invoker-writable writers.**
`2.0.0_SA_COO` states plainly that its own cut would not have caught it: the cut asked for the schedule to be
proven unable to reach the FORCING KEY, and the injection came through a DIFFERENT key its arm never named.

## APPLIED is not EXERCISED — so I measured the window

The fence is APPLIED. Whether the hole was ever GONE THROUGH is a different question and a history read
answers it. **I ran it rather than ordering it.**

**First instrument, and it could not answer:** CloudTrail management events for the function return 4 events in
the window — two `UpdateFunctionCode`, two `AssumeRole`, **zero Invokes**. That zero is a **FALSE ABSENCE**:
Lambda `Invoke` is a DATA-plane event and this account's trail does not select it. I nearly converted a
wrong-plane zero into an all-clear, which is the exact trap `docs/doctrine` and my own night's rulings name.

**Second instrument, the function's own log group:**

| measurement | value |
|---|---|
| exposure window | 01:16:14Z (vulnerable deploy) → the fence |
| `START RequestId` lines in the window | **exactly 1** |
| that invocation | 01:19:06Z, RequestId `9fbc33e0-174c-4c82-b392-2b1dafe4a835`, duration 82,718 ms |
| its arguments | **NOT RECOVERABLE** |

**The payload is not recoverable and I will not infer it.** The function emits NO log line of its own — the
group holds only the runtime's `INIT_START` / `START` / `END` / `REPORT`. Nothing records what it was asked to
do.

## What I therefore state, and what I do not

**STATED:** the exposure was real; the window contained **exactly one** invocation; it fell three minutes after
this project's own deploy, with a duration consistent with the project's own dispatched work, and the only
principals able to invoke are this estate's own seats.

**NOT STATED:** that nothing went through the hole. **I cannot read the argument, so I am not claiming it was
benign** — I am reporting one invocation, attributable by timing and credential-scope to our own work, with its
payload unrecoverable.

## The compounding gap, which is worth more than this incident

**A function whose parameter reaches a shell command logs NOTHING about what it was asked to do.** That is not
a monitoring wish, it is an audit floor: you cannot review an invocation you cannot see. It compounds `W1-S26`
(the terminal send emits no log line and no trail selects the SES data plane). Both are the same absence on the
same function.

**No remedy is proposed from this seat** — adding emission is Andrew's call under the standing moratorium, and
it is recorded here as a measured fact for that decision rather than as a proposal.

## FOR ANDREW, in one line
A live argument-injection path existed in a served AWS function for roughly five hours tonight, reachable only
by a principal holding this estate's credentials. **It was found by a control this seat required, fixed the
same turn, and the window contained one invocation which was our own by attribution.** The function records
nothing about its own inputs, so "our own by attribution" is as strong as the evidence goes, and closing that
gap is your call.

## Push state
LOCAL on commit; `origin/CLOUD` @`c6bcb7b12b`; local 388+ ahead.
