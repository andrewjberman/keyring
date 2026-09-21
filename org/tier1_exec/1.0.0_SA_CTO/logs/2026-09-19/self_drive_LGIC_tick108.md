# /self-drive LGIC -- tick 108 (2026-09-19 ~23:2xZ)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260916_052xZ_LGIC_GOAL_AND_30M_SELF_DRIVE_ADJUDICATE.md`
**Scope:** `LGIC_NAMING, LGIC_ENFORCE, LGIC_CANON, LGIC_LGCTFM`. **Device:** laptop. **state: ARMED**

## The two reads (§0.8)

| read | result |
|---|---|
| **register** | ⭐ **1 genuinely open of 170** -- `LGIC_ENFORCE.TO-EN-h-1-r19.hand-remeasure`, **OPEN** |
| **inbox** | **2 unread** (both `OFFER-EXHAUSTED`) + 2 more arriving live on the new watcher -- all read, acked |

⭐ **ROUND 19 IS CUT AND RUNNING** (`3ed034c144`, `2.0.0_SA_COO~G`): **ONE cell, the hand-side
re-measure** -- exactly the round-18 analysis's take, cut within an hour of it landing. **The scope is
working and owes this seat nothing until it drains.**

## ⛔ 1. THE WATCHER DOES NOT RETIRE §0.8 -- THREE CLOCKS GAVE THREE ANSWERS ABOUT THE SAME TWO MESSAGES

`98378` and `98388` read **`OFFER-EXHAUSTED` on the broker** while the filesystem watcher had **already
drained them to `read/`**, and `98378`'s `[INBOX]` echo was inside a **rate-suppressed batch**.

> ⛔ **A message can be `[INBOX]`-DELIVERED AND BROKER-UNREAD AT THE SAME TIME.** The watcher tells you a
> FILE arrived; only an **ack** tells the FABRIC an agent read it. **The watcher cannot advance the broker
> clock and never could.**
> ⭐ **So the watcher and §0.8 are not substitutes and not redundant** -- I armed the watcher one tick ago
> and §0.8 is what caught these two anyway.

⚠ **And the suppression is the orphan's shape reproduced by RATE LIMITING rather than a dead pipe:**
`mv` commits the drain, the echo lands in a dropped batch. **On a burst the watcher is exactly as lossy
as an orphan, and the loss looks identical to a quiet inbox.**

## ⛔ 2. THE PS 5.1 `.Count` TRAP REPRODUCES ON A THIRD SERIAL -- AND IT FAILS **OPEN**

```
SCRIPT ROWS (wrapped @()): 1
SCRIPT ROWS (bare .Count): ''        <- EMPTY, not 0
PSVersion: 5.1.26100.9444
```

`2.0.0_SA_COO~G`'s finding (98393) holds verbatim here. **`'' -eq 0` is FALSE**, so the guard
`$stale.Count -eq 0` prints **"ORPHAN(S) PRESENT" on a clean serial** -- ⛔ **failing open in the one
census the skill now tells every seat to run.**

## ⛔ 3. I WAS IN THE ARM-TIME GAP MYSELF, WHICH MAKES IT STRUCTURAL

My census right after arming: **ONE script row, Pid `10956`, created `22:51:24Z`.** ⚠ **But I ran my
census BEFORE arming and never re-ran it after, so for a full hour I did NOT hold that pid.** This tick
is ~23:2xZ; **had I reconstructed my arm time from the tick clock the way `2.0.0_SA_COO~G` did, I would
have condemned Pid `10956` -- my own live watcher.** That seat was 12 minutes out; **I would have been
about thirty.**

⭐ **So it is not one seat's slip: it is structural for any seat whose arm predates its current tick --
after the first tick, every seat -- and the error always biases TOWARD reaping, because a later guessed
arm time selects MORE rows.**

## ⭐ 4. MY CONTRIBUTION: PUT THE GUARD ON **CARDINALITY**, UPSTREAM OF BOTH DEFECTS

`2.0.0_SA_COO~G`'s pid-complement fix is right and better than a clock -- **but it still depends on the
seat HAVING RECORDED the pid, a discipline I had already failed an hour before reading the message that
names it.**

> **IF THERE IS EXACTLY ONE SCRIPT ROW THERE IS NOTHING TO REAP, AND THAT IS DECIDABLE FROM THE CENSUS
> ALONE** -- no arm time, no recorded pid, nothing inferred. **The cardinality branch runs FIRST; the
> selector only ever runs at N>1, which is the only case that needs the subtracted term.**

**Why it is upstream rather than a third patch beside them:** it never needs the arm time (**defect 1
cannot fire**); it never computes `$stale` (**defect 2 is never reached on the common path**); and
⭐ **`2.0.0_SA_COO~G`'s own run PRINTED exactly one script row and STILL said "ORPHAN(S) PRESENT",
because the guard sat on the DERIVED value instead of on the CARDINALITY the census had just
measured.** **5 of 5 serials had exactly one row**, so it covers nearly every run.

## ⭐ 5. AND `2.0.0_SA_COO~G` CORRECTED MY OWN SENTENCE, SHARPLY

I wrote *"bind to the identity you hold, never a property you infer."* That seat found the sharper
version:

> ⛔ **"THE ARM TIME IS A FACT THE SEAT HOLDS ONLY IF IT ACTUALLY RECORDED IT."** Reconstructing it
> **turns a held fact back into an inferred one**, and the set complement is safe only if you genuinely
> hold the member being subtracted.

**My formulation was right and SILENT ABOUT THE ONE WAY IT BREAKS** -- which is the more useful half.

## ⭐ 6. EXERCISED MY OWN RECOMMENDATION THE SAME TICK -- AND IT BOUNDS THE ORPHAN CLASS

The Monitor hit its **30-minute cap** mid-tick (22 events delivered) and I re-armed. **This time I ran
the census IMMEDIATELY AFTER arming**, which is the discipline I had just recommended to three seats and
had myself failed an hour earlier:

```
SCRIPT ROW COUNT: 1
HEALTHY -- REAP NOTHING. HELD ARM PID: 27940 created 23:22:07Z     (task b1xoow814)
```

**The cardinality branch returned before any selector ran, and I now genuinely HOLD the subtracted term.**

⭐ **AND THE NEGATIVE CONTROL NOBODY HAS STATED, free from this run: the EXPIRED Monitor's script row
(Pid `10956`) IS GONE.** Exactly one row remains. ⛔ **So a Monitor EXPIRY reaps its own script row and
does NOT leave an orphan** -- which bounds the hazard: **orphans come from SESSION DEATH, not from the
30-minute expiry every seat hits several times an evening.** Without that bound a seat re-arming on
expiry would reasonably fear it is accumulating one orphan per half-hour.

## CARRIED

`IRPT_BCKEND` round-6 analysis (gated; its issuer still not consuming) · `S97` (CLOUD_OPS lane) ·
**`MEMORY.md` at 23.3KB** · **I have not exercised the N>1 selector at all** -- never had two script rows,
so only the guard preceding it is tested, and I said so in the send.

## Open calls at Andrew -- 5 (unchanged)

## Compiler Tools

`get_delivery_state` (4/6 -> 6/6) - `ack_messages` x3 - partitioned open-TO census (**caught r19's cut**)
- `Win32_Process` census **with the `@()` wrap AND the bare form side by side** (the read that reproduced
the trap) - `git log --format` - `send_message` 3 DELIVERED.

**PUSH STATE at write time:** LOCAL @`7a232ebb76` + this commit; `origin/CLOUD` `4071c4c5b0` (ls-remote).
**state: ARMED**
