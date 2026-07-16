# ANDREW-DIRECT (recorded verbatim): loop content does not belong in prompt.md — it is launcher-script ops

**archetype:** SCRIBE
**Channel:** COO terminal (2.0.0_SA_COO session, direct mid-turn message)
**Time:** 2026-07-16 ~14:33Z (read from `date -u`, not derived)
**Recorded by:** 2.0.0_SA_COO, same turn per org/XXX.md "Andrew-direct instructions — RECORD + BROADCAST, same turn"

## VERBATIM

> "i dont think we need to talk about loops in the prompt.md files, that is a launcher script ops item, not a prompt item"

**NOT A PARAPHRASE. THE PHRASING IS THE RULING.**

## Context in which it was given

Immediately prior, COO surfaced that the COO launch prompt's loop-arming block cited the **LD-0204 /drive
carve-out (Andrew-direct 2026-06-18)** as its authority — an authority **deleted from XXX.md at `014de1937`**
and superseded by the LD-0288/0289/0293 standing `/drive`-OFF order. i.e. the launcher text was carrying a
retracted authority. Andrew's ruling responds to that: the defect class is not "the prompt cited the wrong
LD" — it is that **loop arming is being described in prompt.md at all.**

## The distinction drawn

| Concern | Home |
|---|---|
| **Loop arming / cadence / what to arm at launch** (`/loop`, `/drive`, crons) | **launcher script ops** |
| **Who the agent is, its role, scope, duties** | **prompt.md** |

## Measured scope (denominators printed, pre-edit)

- **38** `prompt.md` files total under `org/`.
- **23** contain `/drive|/loop|cron|self-tick|arm(ing)|/watcher|LD-0157|LD-0175|LD-0204` text.
- Worst offender: `org/tier1_exec/2.0.0_SA_COO/prompt.md` (**21** hits) — carries a ~130-line `/loop`
  dynamic-mode operational spec at lines ~262–408 (input-spec grammar, `.tools/loop-resolve` exit codes,
  wake steps, ScheduleWakeup mechanics, park semantics).

## SCOPE SURFACED, NOT ADJUDICATED (org/XXX.md: "SURFACE, DO NOT ADJUDICATE")

The matched lines are **two different classes**, and the ruling names only the first:

1. **LOOP OPS — in scope, unambiguous.** `/loop` spec blocks, `/drive` arming, cron cadence, LD-0157/0175/0204
   arming citations. Removed from prompt.md; the launcher script owns this.
2. **`/watcher` + ORPHAN-HAZARD — retained pending Andrew's word.** `org/XXX.md` Step 1b-F states
   **"`/watcher` is not a loop — it arms the persistent inbox Monitor once."** By the fabric's own definition
   this is **reachability mechanism, not loop ops**, so it is NOT covered by "loops" on the face of the
   ruling. It is also load-bearing prose (CLAUDE.md Rule 22b / the orphan-thief mechanism), and a bare
   prohibition loses to an agent's own instruments. **COO retained it and is surfacing the boundary rather
   than reading the ruling wider than it was spoken.**

**Open question for Andrew:** does the ruling extend to `/watcher`/Monitor-arming prose in prompt.md as well
(i.e. "go-live mechanics" = launcher ops too), or is it scoped strictly to loops (`/loop`, `/drive`, crons)?
COO's read: **scoped to loops**; `/watcher` stays until told otherwise.

## Related standing state (unchanged by this ruling)

- The **scoped `/drive` re-arm** (Andrew-direct 2026-07-16 ~01:5xZ, verbatim in `drive_log_20260716T0154Z.md`)
  is a **launcher/ops** matter and is untouched by this ruling: `/drive 20m` remains ACTIVE until
  OPAL_CONSOLIDATION is "completed and validated end to end, including all scheduled triggers and automation."
- This ruling changes **where loop instructions live**, not **whether the loop runs**.
