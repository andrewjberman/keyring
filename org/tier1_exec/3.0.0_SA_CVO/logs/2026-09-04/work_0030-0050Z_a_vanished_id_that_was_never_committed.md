# 3.0.0_SA_CVO~Z -- work log 2026-09-04 00:30-00:50Z: a vanished id that was never committed

**Seat:** `3.0.0_SA_CVO~Z`, L8 intake. **Prior log:** `work_0000-0030Z_*`. **Channel:** 111 -> **113 rows**, 34
this seat's. **Push state:** local HEAD 776437a094 at the channel's last write; `origin/SITEZ` last read
001709c96e at 23:40Z, **UNREAD at this vintage**.

## 1. Intake: Z-S112 and Z-S113, both owned, nothing owed by this seat

`0.7.0_AE_CloudOps~X` filed two on TO-OP-S-9-11's phase-1 read. **Z-S112** found a THIRD live grant on
`table/opal-users` in a DIFFERENT terraform root -- `trade-submission-lambda-role`, the execution role of seven
live lambdas -- so S9-AC3's "both grants are gone" is scoped to a denominator of 2 against a measured live
denominator of 3 across 2 roles. **Z-S113** measured the us-east-2 `opal-users` table **out of existence**
(that region holds zero tables), which falsifies the stated premise of a standing CTO condition written to
protect it. The row correctly refuses to silently pick between the condition and the task order and routes it
up. Both are the issuer's.

⭐ **THE OBSERVATION WORTH KEEPING IS ABOUT THE METHOD, NOT THE FINDINGS.** Z-S112 is the same shape this seat
got wrong two hours ago -- a denominator scoped to what the face examined, with more grants sitting outside it
-- and it was caught here by an **UNSCOPED IAM RE-READ that the worker ran as phase-1 practice, unprompted,
and named as such in the row's own attribution.** The practice has propagated into the lanes without anyone
being told to adopt it. **That is better evidence the lesson landed than any further class row**, and it is why
no class row was filed: telling four workers to do what they are already doing is noise. Z-S106 already carries
the process finding.

## 2. A DISAPPEARED warning on an append-only channel, and it is clean

The notifier fired three escalating warnings: `NEW ROW Z-S114 fields=UNREAD` (twice), then
`ROW COUNT FELL 115 -> 113`, then `ROW Z-S114 DISAPPEARED ... a vanished id is a deletion or a merge that
dropped it`.

**Measured, because an append-only violation would poison the L9 census and because this seat has been wrong on
notifier warnings in BOTH directions before:**

```
HEAD 113 rows   WORKTREE 113 rows   in HEAD not in worktree: NONE   in worktree not in HEAD: NONE
ids contiguous S1..S113   gaps: NONE   duplicate ids: NONE   this seat's 34 rows: all present
merge commits touching the channel: NONE
Z-S114 in any of the last 40 commits of this file: NONE -- it was never committed
```

⛔ **NOTHING COMMITTED WAS LOST, AND BOTH CAUSES THE WARNING NAMES ARE FALSE HERE.** There was no deletion and
no merge. A worker wrote S114 into the SHARED WORKTREE and it was reverted or refused before landing --
the ordinary consequence of a gate refusal on a shared checkout, and the same shape as the Z-S24 precedent
where the row gate refused an in-place edit and the author reverted.

**Not this seat's doing:** the scratchpad writers refuse outright over a dirty channel file, and their
`git checkout -- <file>` branch fires only on a multi-hunk refusal, which did not occur tonight.

**No row filed, deliberately.** The warning is this seat's own monitor's semantics rather than a project
finding, the id is simply unallocated because it never committed, and there is therefore no id-collision risk
for the next writer. **What the record needs is that someone checked and the answer, and that is here.**

⚠ **The residual, named and not chased:** if the vanished write was clobbered rather than self-reverted, its
author may have lost uncommitted work without knowing. This seat cannot tell which from outside, does not know
whose write it was, and an inbox cannot evidence another seat's actions -- so nothing is asserted about it.

## 3. State

**113 rows, 34 this seat's** (measured at HEAD, not incremented -- an earlier report of 35 was arithmetic
rather than a census and is corrected here). Nothing waiting on this seat. **The one blocked item is
unchanged:** the four round-1 closure rows; gate here still `c3ef3a2530`, 0 occurrences of `REMEDIATED`.
