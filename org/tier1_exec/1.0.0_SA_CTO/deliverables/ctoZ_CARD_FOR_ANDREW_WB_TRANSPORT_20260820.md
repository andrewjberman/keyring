# CARD FOR ANDREW — the ticket-nudge transport. **This supersedes every earlier version.**

**Author:** 1.0.0_SA_CTO~Z · **Date:** 2026-08-20 ~22:38Z · **Status:** FINAL. Ferry this one.
**Superseded:** the 10:1 numbers, the "13s is smaller than the wake hop" sentence, and the 30s premise. **All three were mine and all three are struck.**

---

## THE QUESTION HE ASKED

> *"if it was possible for the lambda to just hit the agent direct somehow that would be the best case
> scenario and there doesnt need to be polling at all. Could we do something like that"*

## THE ANSWER

**Yes — except for the last hop, which is the part that isn't.** A Lambda can detect a new ticket
instantly. **It cannot reach this box.** It cannot write a local file, and it can never hold the gateway
credential, because that credential's refresh is an interactive OAuth challenge only a Claude Code client
can answer. So something local has to consume it, and **an event-driven accelerator whose last hop is a
poll is not an accelerator.**

## THE NUMBERS (measured floor + wake hop; the schedule arithmetic is modelled)

```
                        detect     + wake     total
  today, 5-min           ~150s      +14s      ~164s
  1-minute schedule       ~30s      +14s       ~44s      <- costs NOTHING
  stream + new consumer  ~1-2s      +14s       ~16s      <- costs a lot
```

> **A SCHEDULE CHANGE BUYS ~120 SECONDS FOR NOTHING.**
> **THE STREAM BUYS A FURTHER ~28 SECONDS** — for the estate's **first DynamoDB stream**, a **new standing
> local process**, and a new failure domain.

**MY RECOMMENDATION: take the schedule change, drop the stream.** It does not foreclose the stream later
if you want the last 28 seconds.

## WHY THIS IS SAFE TO DECIDE NOW

- **The wake hop is MEASURED** — 14.13s, real traffic, three clocks (`0.0.3_BG_BBGTerminal`). It is a
  *warm-schema* figure, so the true floor is **that or higher** — and every second higher **shrinks the
  stream's advantage**, never the schedule change's.
- **The 1-minute floor is MEASURED, and 30s is REFUTED** — the Task Scheduler engine refuses `PT30S` at
  registration; `PT1M` accepts on the identical path.
- **The conclusion is insensitive to the floor** (`3.0.0_SA_CVO~Z`): it stays right-side-up at **every
  floor below ~180s** and inverts only above it — **three times the settled value.** Nobody needs to
  reopen this on floor grounds.
- **It survives its own weakest assumption.** The one real datum on arrival timing sits *above* the
  model's expectation, and re-running at that pessimistic end leaves the ordering unchanged, **because the
  same assumption inflates the backstop it is compared against.**

## THE HONEST BOUNDS

- The **schedule arithmetic is modelled**, not measured — uniform arrival within a cycle. If tickets
  cluster at a known hour it shifts. **The measured parts are the wake hop and the floor.**
- **A 1-minute schedule has a cost nobody has priced**: ~5× the invocations of a local task, plus this
  box's load tolerance. Cheap, not free.
- **This does not touch the email DL**, which you already authorized as the first line — and the DL is
  what makes this an optimization rather than a dependency.

## WHAT I GOT WRONG, since it reached you

I carded **10:1** and *"the remaining 13 seconds is smaller than the wake hop we cannot remove."* **Both
rested on a 30-second schedule I had not verified.** The engine refuses 30 seconds. The real ratio is
**4.3:1**, and the stream's margin (~28s) is **larger** than the wake hop, not smaller. **The
recommendation did not change; my reason for it did**, and you should have the reason that survives rather
than the one that sounded better.
