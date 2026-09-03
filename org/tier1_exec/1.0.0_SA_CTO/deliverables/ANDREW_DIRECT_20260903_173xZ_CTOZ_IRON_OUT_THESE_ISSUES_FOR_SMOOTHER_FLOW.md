# ANDREW-DIRECT 2026-09-03 ~17:3xZ at the `1.0.0_SA_CTO~Z` terminal -- iron out these issues for a smoother flow

**VERBATIM, the whole word:**

> have COO accept it and flip the status and also note this becuse we need to iron out these kinds of issues for a smoother flow

The first clause was relayed to `2.0.0_SA_COO~Z` (19879) the same turn. This record is the second clause.

## What "this" is

The immediate instance: `TO-OP-S-2` had a complete proof instance (S2-AC1..AC5 all PASS) and a closed deploy ledger,
while the decomposition still read `OP-s-2 IN-FLIGHT`. **The work and its evidence were finished; the record saying so
was a separate later act by a different seat.** From outside, "done but not yet written down" and "not done" are the
same string.

"These kinds of issues" is the wider class, and today produced six of them, all measured. They share one shape:
**a record and the world it describes drift apart, and the reader cannot tell which one is stale.** None of them is a
wrong action by any seat. Every one cost time.

## The six, each with its instance, its cost and its fix

**1. THE RECORD LAGS THE FINISHED WORK.** *Instance:* `TO-OP-S-2` above; also `OP-s-5` and `OP-s-8` reading
`IN-FLIGHT` while their round-1 orders are accepted. *Cost:* a status read gives the wrong answer, and a reader
cannot distinguish "deliberately still in flight for a round-2 limb" from "finished but not written down."
*Fix:* when a cell is deliberately in flight because a later limb remains, one clause on the row saying so -- the two
states then read differently. *Status:* proposed to `2.0.0_SA_COO~Z` in 19879 as an observation for its judgment.

**2. A SPEC NAMES A THING BY A PHRASE THAT DOES NOT MATCH WHERE IT LIVES.** *Instance:* `TO-OP-S-2` called the
S2-AC2 fixture "the demo firm's COMMITTED demo credentials". The worker searched for a demo-**firm** credential,
found none, and filed row Z-S45 reporting the credential does not exist. It does: it is a portal **test-user**
credential at `.claude/skills/frontend-dev/portal-test-login.env`, committed and Andrew-sanctioned since
2026-08-06. *Cost:* one blocked acceptance leg, one false-absence row, and a credential offered at this terminal
that was never needed. *Fix:* **name a fixture by its committed PATH, never by a description.** *Status:* MADE --
`2.0.0_SA_COO~Z` amended the face @e899fb7b88 within minutes of the finding, and the leg then passed.

**3. ABSENCE OF PROOF READ AS ABSENCE OF ACT.** *Instance:* the `opsec-r2b` ledger carried L5/L6 with `proof: null`,
and this seat's restart package told a respawned worker to re-run an apply **that had already run** at 13:21:50Z.
*Cost:* a live worker was one step from acting on a false instruction; `0.0.0_AB_MSTR~Z` caught it (Z-S42).
*Fix:* the ledger records a PROOF; it does not record that the act was attempted. An `attempted_at` stamp distinct
from `proof` would make "did it happen" answerable without inference. NEVER-2 already tells a reader to measure the
artifact -- the gap is that nothing prompts them to. *Status:* PROPOSED, nobody's yet; the instrument that settled it
(point-in-time recovery's earliest-restorable timestamp, which cannot precede the switch-on) is banked in Z-S44.

**4. A LOAD-BEARING ADDRESS INVISIBLE TO THE INSTRUMENT AGENTS USE.** *Instance:* `org/XXX.md` Step 1b-F -- named by
every launch prompt as the only source of truth on loop authorization -- was the one subsection written in bold
rather than as a heading, so a heading-shaped probe reported it ABSENT and a worker concluded it does not exist.
*Cost:* asymmetric -- safe for a seat with no authorization, unsafe for a seat that has one, which would find nothing
and be unable to tell revocation from looking in the wrong place. *Fix:* make the address discoverable by the
instrument that is actually used on it. *Status:* MADE -- routed by `2.0.0_SA_COO~Z` (19863), landed @3bde8d1bac.

**5. AN ACCEPTANCE CRITERION WRITTEN AGAINST AN INSTRUMENT THE EXECUTING SEAT CANNOT RUN.** *Instance:* S2-AC3 was
written against custom CloudWatch metrics, and `opal-portal-data-proxy` cannot emit them at all -- every invocation
is denied on `PutMetricData` (Z-S46, confirmed on a second plane and bounded at 1 of 55 by Z-S48). *Cost:* an
acceptance leg with no working instrument; the worker found another route and passed, but only after surfacing it.
*Fix:* a criterion should name an instrument, and the issuing seat should confirm the executing seat can run it --
or the criterion carries an explicit fallback. *Status:* PROPOSED, the issuer's.

**6. A RESPAWNED SEAT THAT COMES UP AS A PROCESS BUT NEVER BECOMES A SEAT.** *Instance:* the first respawn of
`0.7.0_AE_CloudOps~S` ran 14 minutes with zero broker registration, unread inbox, and 12.6 CPU-seconds against its
sibling's 35.1 from the same spawn batch. *Cost:* 17 minutes of a lane that looked alive and was not. *Fix:*
`2.0.0_SA_COO~Z` investigated before retrying and set its own bound -- one retry, then it becomes a device question
rather than a seating one. That is the right shape. *Status:* HANDLED; cause still unmeasured and deliberately not
attributed to the API issues that prompted the kill.

## The one that is this seat's own, stated because it is the largest single source of friction today

Five times today this seat attached a **correctly measured fact** to a **consequence it had not checked**: a plan
line read as an outcome; a null proof read as a null act; a worktree row count read as a committed row count; a
subtraction across two planes read as a census; and a "no fourth instance" claim whose instrument could only see one
of the two classes it was quantifying over. Every one was caught by another seat or by this seat's own later
measurement, and every one is corrected on the record.

**The pattern is not missing evidence.** It is evidence measured on one plane and spent on a claim about another.
The cheap guard, applied consistently, is one question before the sentence ships: *does the thing I measured actually
establish the thing I am about to say?* Four of the five would have died on it. The fifth needed one extra command
that already existed.

## What is asked of whom

- `2.0.0_SA_COO~Z`: item 1's clause, if it agrees; item 5 is its call as issuer. Item 2's fix it already made.
- `3.0.0_SA_CVO~Z` and `0.0.0_AB_MSTR~Z`: item 3's `attempted_at` proposal touches the deploy-ledger contract, which
  is neither seat's alone -- surfaced here rather than edited.
- Nothing is asked of Andrew. This is the note he asked for, not a queue for him.
