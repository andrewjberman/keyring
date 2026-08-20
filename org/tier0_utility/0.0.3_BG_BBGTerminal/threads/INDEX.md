# threads/INDEX.md -- the ONE unconditional read before any reply

**Seeded 2026-08-20 (M7, PRD sec12.5, CTO~Z msg 2705).** Owner: this seat. `threads/**` is my
own writable surface -- the agent owns its own memory.

## WHY THIS FILE EXISTS -- read once, it is the whole design

**RESOLUTION PRECEDES CREATION.** Before recording anything, resolve the inbound **chat id**
here. A chat id appears **exactly once**. If it is listed, you write into the dir it names.
**If and only if it is absent do you create a dir -- and you add the row in the same act.**

This makes a fork *impossible*, not *discouraged*. On 2026-08-20 I created a second dir for a
chat that already had one, in good faith, following the old convention exactly as written --
and the cost landed the same day: a standing Andrew-direct instruction sat in the half I did
not open, and I broke it. The slug axis is *date-started + topic*; a continuous 1:1 has
neither a single start date nor a single topic, so the person -- the thing recall is actually
keyed on -- was never an axis at all.

>> **THE FAILURE THAT MATTERS IS THE READ, NOT THE STORE.** The memory *held* the `.ST`
context on 2026-08-20 and the serve re-derived it from raw Teams history anyway. **Memory
that exists but is not reached is indistinguishable from memory that does not exist -- and it
is worse, because it reads as covered on every audit.** Recall "passed" that day: I read *a*
thread dir. Just not the one with the instruction in it.

**So: every daily entry records its recall denominator** -- which dirs were read, out of how
many resolved for that person. An unread memory becomes visible the same day it happens.

## ID -> DIR MAP (a chat id appears exactly ONCE)

| Chat / channel id | Canonical dir | Person / subject |
|---|---|---|
| `19:2e21f8e5-55ca-45c1-91b9-a4607bf28d4f_517aa5ee-b4d0-425a-b493-5a22ff77ac4f@unq.gbl.spaces` | `2026-08-07-andrew-capability-roster/` | Andrew Berman -- 1:1 DM |
| `19:2e189a40973d4d7091f4dbe2689282c7@thread.tacv2` | *(not yet created -- TICKET class, see below)* | Opal Client Tickets channel |

**Retired forks (redirect stubs, never rows above):**
`2026-08-20-andrew-responsiveness-test/` -> merged into `2026-08-07-andrew-capability-roster/`.

## STANDING BLOCK -- Andrew Berman

Verbatim-anchored; **these are read before replying, not looked up after.**

1. **<=2-3 sentences per Teams block** (Andrew-direct 2026-08-07 12:55Z). *Breached 2026-08-20;
   corrected in-thread.*
2. **Latency/age answers carry a NUMBER, not an adjective** (evidenced 2026-08-20).
3. **Chat-history backfill: DECLINED and CLOSED** (Andrew-direct 2026-08-20) -- do not re-raise.
4. **He is the only consumer of this seat** (his words, 2026-08-20) -- it bounds every design.
5. **He tests without warning.** Every inbound is live.
6. **Serve rule (CTO~Z, ruled):** a figure read from a POSITIONAL path carries its identifying
   field projected in the same call. See
   `../deliverables/SERVE_RULE_POSITIONAL_PATHS_CARRY_THEIR_IDENTIFIER.md`.

**Recurrence:** the ST model is a repeat subject (08-11 index integrity, 08-20 YTD). He probes
the seat's own machinery as readily as the data (capability roster 08-07, polling interval
08-20) -- answer those with measurements.

**Owed in-thread:** the A5 live positive -> confirm and retire the interim re-send rule in the
same message. Do not manufacture it.

## !! TWO SHAPES -- Rule 24(iv), NAMED, NOT ONE SCHEMA

**A person-thread and a ticket are not the same kind of thing, and one store over both fails
the one-remedy test:**

| | Person-thread | Ticket |
|---|---|---|
| bounded? | **no** -- continuous, never closes | **yes** -- closing it is the point |
| keyed on | identity (chat id) | reference |
| lifecycle | none | opened -> acknowledged -> answered -> closed |
| what it must surface | continuity, recurrence, standing instructions | current state + its vintage |

The ticket class, when it lands, is **POINTERS + OBSERVED-STATUS-WITH-VINTAGE -- never a
second home for ticket content.** A second copy of a ticket's state is a second source of
truth, and the one that goes stale is the one someone quotes.
