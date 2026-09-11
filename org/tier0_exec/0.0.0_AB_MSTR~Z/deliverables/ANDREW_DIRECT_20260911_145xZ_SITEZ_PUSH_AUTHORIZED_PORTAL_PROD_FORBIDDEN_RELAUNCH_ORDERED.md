# ANDREW-DIRECT 2026-09-11 ~14:5xZ -- SITEZ push authorized, portal PROD forbidden, relaunch ORDERED

**archetype:** COORDINATE

**Channel:** Andrew-direct at the `0.0.0_AB_MSTR` (laptop) terminal, relayed verbatim to this seat
over the agent bus as MessageId `db01766b-c4ff-4f49-b996-7f41a5d46250`, 2026-09-11T14:52:48Z.

**Received by:** `0.0.0_AB_MSTR~Z`.

## THE ORDER, VERBATIM AND ENTIRE

> "They should not be pushing any portal work to prod, they can commit/push to DEV only when it
> relates to PORTAL. However if they want to push to SITEZ for ajb_workspace, that's fine. In either
> case they need to see who was last online pre-reboot and bring them back and get that device up to
> speed."

## WHAT IT AUTHORIZES, AND WHAT IT DOES NOT

| surface | standing |
|---|---|
| SITEZ / `ajb_workspace` push | **AUTHORIZED** -- "if they want to push to SITEZ for ajb_workspace, that's fine" |
| portal **PROD** | **FORBIDDEN, FLAT** -- "should not be pushing any portal work to prod". No qualifier, no condition |
| portal **DEV** | **PERMITTED ONLY FOR PORTAL WORK** -- "only when it relates to PORTAL". The constraint is on the **CONTENT**, not the branch: a DEV push carrying non-portal work is outside his word |
| relaunch of the pre-reboot seats | **ORDERED** -- "see who was last online pre-reboot and bring them back and get that device up to speed" |

**THIS SUPERSEDES THE HOLD.** Twenty minutes earlier `0.0.0_AB_MSTR` correctly told this seat to hold
`@9dfe8e1115`, because Andrew's prior word ("push cloud sure but wait on DEV") named CLOUD and DEV and
not SITEZ. **He has now named SITEZ.** The hold was right when given and is discharged by a later
ruling, not by anyone's reinterpretation of the earlier one.

> **The asking is what produced the ruling.** This seat declined to read "push cloud" as reaching
> SITEZ and said so rather than widening. Recorded because the cheap move -- assuming the authority --
> would have produced the same push with no ruling behind it, and nothing would have looked different.

## WHAT THIS RULING DOES *NOT* REACH -- stated because the adjacency is the hazard

⛔ **THE CLOUD->SITEZ MERGE LEG IS STILL GATED AND HE HAS NOT GIVEN IT.** "Push SITEZ is fine" is not
"merge CLOUD into SITEZ". They are different acts with different blast radii: the push publishes this
device's own commits; the merge imports 119 CLOUD commits into this branch and is the precondition for
the audit-archive repair. This seat's `/integrate` run was **assess-only** and nothing in tonight's
word changes that. Flagged by `0.0.0_AB_MSTR` in the same message and agreed here.

⛔ **"UP TO SPEED" IS NOT INTERPRETED, BY EITHER MSTR.** He said bring them back and get the device up
to speed. What each returning seat then does is **that seat's own startup law, its own record and its
own lane** -- not a re-tasking from an MSTR. Relaying, not adjudicating.

## THE FIVE TO RELAUNCH, FROM THIS SEAT'S OWN PRE-REBOOT ROSTER

| serial | runtime | pre-reboot log |
|---|---|---|
| `1.0.0_SA_CTO~Z` | codex | @1d36e8df4c |
| `2.0.0_SA_COO~Z` | claude | @23783dd2b6 |
| `2.0.0_SA_COO~ZZZ` | claude | @b8386bea24 |
| `3.0.0_SA_CVO~Z` | codex | **NEVER LOGGED** |
| `4.0.0_SA_CRO~Z` | codex | @c187072692 |

**`3.0.0_SA_CVO~Z` is the one seat with no log of its own to resume from.** Its owed acts (the v0.4
ratified-text sign; round-4 L8/L9/L10) are carried in the `1.0.0_SA_CTO~Z` and `2.0.0_SA_COO~ZZZ`
logs, so nothing waits on it -- but it must be **told** that at launch rather than left to discover it
by finding an empty logs dir.

## THE ORPHANED-LAUNCHER TRAP -- DOES NOT APPLY HERE, AND WHY

`0.0.0_AB_MSTR` hit this on the laptop this morning and flagged it so this seat would not hunt for it:
`start-codex-seat.ps1` runs codex INLINE and `-NoExit` leaves the launcher shell holding the seat's
`OPAL_SPAWN_MARKER_v1` serial, so a dead codex seat can leave a LIVE launcher window with zero
children, and `/mstr-spawn` step 1b then refuses the relaunch as a duplicate until the shell is
reaped.

**A REBOOT CLEARS ALL OF IT.** This box booted 2026-09-11T14:10:36Z and this seat measured **zero
`codex.exe`** -- so there are no stale markers and no orphan shells. Spawn clean.

⚠ **STILL RUN PROCESS TRUTH FIRST ON EACH SERIAL** -- not for orphans, but because **Andrew launches
seats by hand and the spawn tool's own checks are blind to an Andrew-launched session.** He is at this
device.

## ACTS TAKEN BY THIS SEAT UNDER THIS RULING

Recorded as they are executed; see the session's commits.

1. This record, committed on this seat's serial.
2. SITEZ push of the held `@9dfe8e1115` plus this record -- **authorized tonight, not inferred.**
3. Relaunch of the five, process truth first on each serial.

**NOT done:** the CLOUD->SITEZ merge (gated), any portal push of any kind (PROD forbidden; DEV is
permitted only for portal content and this seat is carrying none), any re-tasking of a returning seat.
