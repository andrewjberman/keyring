# An unknown cash leg no longer emits a clean MEASURED return -- row S6 limb (a), unblocked earlier than I predicted -- 0.4.0_DS_ClientPlatform~S

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE

**Date:** 2026-10-01 04:50Z to 05:10Z
**Task Order:** `IRPT_DASHBD.TO-DB-b-1` (pending)
**Status:** IN PROGRESS -- emit still HELD on rows S4/S6(c) with the dark issuer
**Workspace CLOUD commit:** `6915ceb469`. LOCAL; origin/CLOUD `0abf99fcd4` (ls-remote read).

---

## Objective

Row `IRPT_DASHBD-S6` limb (a) and part of (b) (REVIEW.md F04). **My own row said these waited on
S4/S5.** Re-examined after PRD v0.4 and they do not: ruling 17 defines the path for a knowably
incomplete `F_t`, so routing an unknown cash leg onto it applies an existing ruling instead of
making a new method choice. I took the work early rather than honour a prediction I had made
before the ruling existed.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| commit-gate | 3 runs | PASS | |
| safe-commit + gates | 1 commit | PASS | |
| planted mutant + control | direct `classify_and_sum` on real partition date=2026-09-25 | PASS | the only test that distinguishes "no unknowns found" from "the detector never fires" |
| live dry-run | 5 accounts x 10 trading days, graded | PASS | 50 rows, unchanged |

**What worked:** the mutant/control pair. The live data carries zero unknowns on that partition,
so a green run proved nothing on its own.
**What failed:** nothing.
**Gap found:** none new.

---

## Work Completed (`6915ceb469`)

Four conditions each mean `F_t` is incomplete for an account, and every one was tallied into
`census` -- a whole-day aggregate no row can be rejected on -- while that account's return was
emitted as a clean `MEASURED` number:

| condition | what happened before |
|---|---|
| malformed amount | `to_numeric(errors="coerce").fillna(0.0)` -> the transaction was worth 0.00 |
| unkeyed code | omitted from the EXTERNAL filter |
| UNRESOLVED class | omitted from the EXTERNAL filter |
| unreadable cash direction | counted, then dropped |
| transaction partition ABSENT | identical to a partition with no rows |

The malformed-amount mask is now taken BEFORE the fill, because the fill is what hid it. All four
accumulate into a per-account `cash_unknown` map beside the in-kind `unvalued` map, and
`FlowCache` carries an explicit absent-partition flag the flow window inherits. The three causes
reach ruling 17's path (null / `NOT_MEASURABLE` / `FLOW_UNRECONCILED`) and stay distinguishable in
`_incomplete_reason` and the branch counts -- one remedy does not move all three (Rule 24 (iv)).

**The judgment is named, not buried.** Ruling 17 names the in-kind case explicitly and these two
by implication only. The direction is strictly conservative: a day can only move FROM measured TO
flagged. A missing partition arguably belongs in the declared-but-never-emitted `SOURCE_LAG` state
instead -- the issuer's method call.

### Verified with a planted mutant

| run | result |
|---|---|
| CONTROL, real partition unmodified (2,006 rows) | 0 `cash_unknown` accounts, all five counters 0 -- no false positive |
| MUTANT, one cash amount replaced with `"not-a-number"` | 1 account (`0010314939`), `cash_unknown_malformed_amount` 1, victim present in the per-account map |

**Latent, not active, and said so in the commit:** that partition carries zero unknowns. Across the
561-partition history the census recorded 106 UNRESOLVED cash rows and 6 unkeyed rows, which would
now flag their account-days instead of vanishing from `F_t`.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Take S6(a) now despite my own row saying later | The prediction predated ruling 17. Honouring it would have been deference to my own stale note, not to a dependency. |
| No new surprise row for that change of plan | S7 was warranted because it corrected an OWNERSHIP error that would misroute work. Doing work earlier than predicted misroutes nothing; the commit message carries the reasoning. |
| Keep the four causes separate | Different owners, different remedies. A single "incomplete" tally would hide which one carried the round. |
| Leave `first_seen` durable-inception alone | Genuinely coupled to S6(c)'s interval grain AND needs a persistence decision (a new artifact). Recorded in S6 already. |

---

## Blockers

- **`2.0.0_SA_COO~P` DARK** -- rows S4, S6(c)(d)(e), S7, the TO text amendment, the two contract
  edits rulings 17-18 name.
- **Nothing on Andrew. Nothing on the CTO.**

---

## Current State

Everything in this seat's lane that is not downstream of the issuer's boundary, fee-basis or
interval decision is now done. The producer refuses an emit three ways (no thresholds, a
SUPERSEDED thresholds file, no comparability ceiling), never substitutes a different population's
return, grades only inside a measured comparability domain, checks the value it actually emits,
and no longer reads an unknown input as a zero. Nothing is in S3; no thresholds file exists; the
change-management ledger is not opened.

---

## CORRECTION, 05:0xZ -- `2.0.0_SA_COO~P` IS LIVE, AND THIS SESSION'S THREE LOGS SAY OTHERWISE

**The claim:** all three of today's logs from this seat, and several commit messages, state that
`2.0.0_SA_COO~P` is DARK and that rows S4/S6/S7 are parked on a dead serial.

**Measured:** `get_agent_status("2.0.0_SA_COO~P")` reads **LIVE, PID 20708, last seen 12s ago**,
`WORKING: ... IRPT_DASHBD TO-DB-b-1 amendment to rulings 17-19`. It is not dark and it is already
working the amendment this seat is waiting on. Its own next-step 2 names the account-grain flow
term.

**Where the false claim came from:** `1.0.0_SA_CTO`'s broker summary line, which read
"BLOCKED-SOVEREIGN items: ... COO ~P/~M/~Y dark". I read that in the live-agents listing during
startup and carried it for the rest of the session without ever running the one-call instrument
that answers it. `get_live_agents` was in front of me twice and I did not re-read the row.

**Why this is the same defect I spent the session documenting.** Row S3's lesson is that I read an
improvement as a correctness proof; row S7's is that I inferred ownership from authorship instead
of resolving the lane. This is the third instance of one pattern: **an inherited claim acted on
without its own instrument.** CLAUDE.md rule 24 (i) names the tell exactly -- "an inherited claim
has no denominator to narrow: the tell is grammatical ... ask which instrument produced it and
what that instrument can see." A seat's summary line is a free-text self-report about OTHER seats;
it is not a liveness instrument and cannot be one.

**What it cost, stated honestly:** nothing irreversible, but it was not free. I broadcast "(DARK)"
in my own broker summary for roughly 40 minutes, so every seat reading the roster inherited it from
me as well -- the stale-record propagation this workspace's own doctrine warns about. And I told
Andrew twice that the round was blocked on a dead issuer when it was blocked on a live one actively
writing the fix, which is a materially different situation: the first invites intervention, the
second needs none.

**Corrected:** broker summary fixed; one message sent to `2.0.0_SA_COO~P` (04:57Z) clearing its own
stale "BLOCKED on Andrew: the DB-b-1 emit" and asking that the amendment cover row S4's three
defects as well as the CTO's rulings. The earlier logs are left as written -- history is not
rewritten -- and this section is the pointer.
