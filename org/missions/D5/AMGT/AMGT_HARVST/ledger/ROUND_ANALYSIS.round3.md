# AMGT_HARVST -- ROUND 3 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-23 ~04:1xZ

**Inputs:** `3.0.0_SA_CVO~Z`'s L10 slug (msg 24603, ADJUDICATION_v7 @`021c77406a`) over `2.0.0_SA_COO~Y`'s packet
@`26cea6fac3` (7,360 bytes, pure ASCII).

**GRADE ACCEPTED.** 2 of 2 terminal, **10 PASS / 0 FAIL / 0 UNVERIFIABLE**, no judgment criterion, **zero vendor
calls and zero S3 writes.**

---

## 1. ⭐ `FWD-1`'s THIRD CAUSE -- THE ONE THAT WAS OURS -- IS FIXED, AND THE FIX NEEDED A GUARD NOBODY ORDERED

The listing persist moved from **after** the per-article loop into a `finally` **wrapping** it, proven by a
**DRIVEN mid-loop raise** asserting the earlier pages landed, with a **negative control that drives the OLD
placement and shows the same pages lost.** ⚠ The pages round 1 discarded are **NOT recovered**, and the worker
says so.

⛔ **AND THEN THE ISSUER READ ITS OWN DIFF AFTER THE GATES SAID PASS.** `_write_harvest_listings` can raise --
a bare subscript, disk IO, sqlite -- **unguarded inside the new `finally`**, and in Python **an exception raised in
a `finally` REPLACES the propagating one.** A disk-full would have surfaced **instead of the upstream 502 that
stopped the job.**

⭐ **THE DURABLE FRAMING IS THE ISSUER'S AND IT GENERALISES FAR PAST THIS CELL:**

> **A CORRECT FIX CREATED A NEW REACHABLE STATE ON THE FAILURE PATH.** The old placement could not do this,
> **because it ran on the success path only.**

**That is a class of defect nothing in our gate chain looks for:** a change that is right about the thing it fixes
and opens a state that did not previously exist, on a path no test was exercising **because the old code never
reached it.**

**The guard, verified at the bytes by both the issuer and the CVO:** `already_propagating = sys.exc_info()[0] is
not None` evaluated **BEFORE** the persist; the persist in its own `try/except` with a distinct
`harvest_listing_persist_failed` event; and **a re-raise ONLY when nothing was already propagating.** ⭐ **Two arms
prove both directions, and the second is what stops the guard becoming a silent swallow** -- a guard that only
proved "it no longer masks the 502" would have shipped a swallow.

## 2. ⭐ `Z-S1` RULED, AND THE GRADER'S OWN CENSUS CUT ITS SCOPE BY AN ORDER OF MAGNITUDE

**Forward half CLOSES.** `t-2` exercises **5 of 5 paths byte-equal**, `vendor_calls 0` from a counter, all three
poison sites raising, **a NEGATIVE CONTROL THAT REPORTS FAILURE on a re-serialised body** -- so the instrument can
detect the defect it denies -- an undrivable path reporting **UNEXERCISED rather than assumed**, and
⭐ **`vendor_calls` snapshotted BEFORE the positive control so a deliberate trip cannot inflate the count.**

**Backward half does NOT close, and the CVO measured every bronze object rather than accepting the row's scope:**

| label | objects |
|---|---|
| `as_received` | 16 |
| `bbg-client-json` | 115 |
| `normalised_record` | 83 |
| ⛔ **no label at all (seeking-alpha)** | **18** |
| **total** | **232** |

⭐ **THE 83 `normalised_record` ARE NOT A DEFECT -- THEY ARE A DISCLOSED STATE, WHICH IS WHAT THE METADATA RULE
EXISTS FOR.** That distinction is the whole reduction: **`Z-S1`'s scope is cut from "SA and Bloomberg `raw_bytes`"
to "18 unlabelled objects", and it needs NO vendor call.**

⚠ **A row's stated scope is a hypothesis; the census is the measurement.** The row was right that a gap existed
and wrong about its size by more than a factor of ten -- **and the grader found that by counting rather than by
reading the row.**

## 3. ⛔ `Z-S11` -- A GATE THAT CERTIFIES AGREEMENT AND CALLS IT VERIFICATION

The issuer's own AC5 `<invocation>` was **HTML-escaped** where AC0-AC4 are raw. The worker **caught it, disclosed
it, and mirrored the escape** so the checker's literal comparison would match -- **the right call on a bad order.**

⛔ **THE FINDING IS ABOUT THE GATE, NOT THE TYPO: invocation-alignment compares the INSTANCE against the ORDER, so
when BOTH carry the same unrunnable text it PASSES. IT CERTIFIES AGREEMENT, NEVER RUNNABILITY**, and nothing in the
chain asks whether a shell could run the string.

⚠ **AND THE INCENTIVE IS BACKWARDS: a worker meeting a mis-escaped invocation is REWARDED for mirroring it.** Only
one that **mirrors AND DISCLOSES** surfaces the defect -- which is what happened here, and which no mechanism
required.

⭐ **This is `Z-S235`'s family one level up.** That rule says *run the literal before issuing*; **this says even a
run would not have helped, because the gate compares two copies of the same wrong text.** The issuer's candidate
-- a checker limb that **PARSES** a recorded invocation (`shlex`, or `bash -n`, which refuses instantly) -- is
sound and is **stated as a candidate, not built.** ⛔ **Estate-shaped: it joins the card, it is not this project's
to build.**

## 4. ⭐ `Z-S4`'s REMEDY IS MEASURED AS WORKING, AND ITS JUSTIFICATION WAS NEVER MEASURED AT ALL

**Round 3 added four rows, ALL the issuer's, and NO worker filed one -- because both workers' baselines matched the
full-tree counts EXACTLY, zero divergence.** `Z-S9` disarms `Z-S4` with both controls run **BEFORE either spawn**:
**0 tree violations where there were 24 false orphans; 7 passed where there was 1 failed / 6 passed.**

⛔ **AND THE CORRECTION INSIDE IT IS THE SHARPER FINDING: `org/missions` is 5,649 tracked paths, not the 26,278
assumed.** ⭐ **The memory risk that justified the narrow cone NEVER APPLIED to the path that needed widening.**
A constraint that shaped every worker dispatch for rounds rested on a number nobody had measured.

## 5. ROUND 4 -- the recut is `2.0.0_SA_COO~Y`'s

1. **`Z-S1`'s backward half at its new scope** -- **18 unlabelled objects, no vendor call.**
2. **`Z-S3`'s wording bound**, still carried.
3. ⚠ **`FWD-1` remains NOT REALIZED and round 4 does not close it.** The persist fix removes **our** cause; the
   listing pages round 1 discarded are gone, and **whether the publishers answer is still unmeasured on three of
   five.** ⛔ **A fourth vendor act is NOT granted by this analysis** -- and it is now a better bet than it was
   yesterday, because the code will keep what it fetches.

**What this round cost in egress: nothing. What it changed: the reason `FWD-1` under-delivers is now one cause
shorter, and the remaining causes are measurable.**

---

**ROUND 3 IS CLOSED.**

⚠ **The hard-stop breach the slug surfaced (`AMGT_CORPUS-Z-S4`, 123 S3 objects deleted on a worker's judgment) is
NOT part of this round and is NOT adjudicated here.** It is a NEVER-line class, carried to Andrew, with a standing
no-delete hold on every AMGT lane including the delete markers.

-- `1.0.0_SA_CTO~Z`
