---
name: goal-set
description: Point yourself at a goal and let the org drive it to a verified finish. Asks up to 3 quick questions about what you want (answer fewer, or just hand over the goal -- no pushing), crystallizes that into a goal, then ARMS A SELF-DRIVING LOOP -- /loop [interval] <Drive the goal to completion; /verify at completion and adjust if necessary>. The loop ticks the goal forward each wake, /verify (mechanical/declarative/semantic) gates completion, and it adjusts until /verify is SOUND. Use when you say "/goal-set" or "/goal-set <rough idea>". The CEO, an exec, or any agent handed a goal runs it.
---

# /goal-set -- set a goal, arm a loop that drives it to a verified finish

Three moves, no ceremony: **ask a little, set the goal, arm a loop that drives and
verifies itself.** `/goal-set` just kicks it off -- `/loop` is the engine, `/verify` is the gate.

## 1. ASK -- up to 3 quick questions (fewer is fine)
Ask at most three, and only what you actually need:
1. **What do you want to do?** (the goal)
2. **Any constraints / must-haves?** (scope, deadline, what to avoid)
3. **What does "done" look like?** (how you'll know it's finished -- the `/verify` target)

The principal can answer one, skip the rest, or just hand you the goal -- take what they
give and don't push. A clear goal up front may need zero questions.

## 2. SET THE GOAL
Crystallize the answers into one clear goal statement (plus the "done" criteria, if
given). Say it back in a sentence so they can correct it. That statement is what the
loop drives to.

## 3. ARM THE LOOP
Write a self-driving loop -- the goal becomes its standing directive:

```
/loop [5m] <Drive "<the goal>" to completion. /verify at completion and adjust if necessary.>
```

- **Interval** is yours to set -- 5m is a sane default; stretch it for a big goal.
- **Each wake** the loop drives the goal forward: decompose it, do the next step, or
  dispatch to workers as the size warrants.
- **At completion** it runs `/verify` -- mechanical / declarative / semantic, grounded
  against the real artifact, never a "done" claim.
- **If `/verify` is not SOUND**, it ADJUSTS (fix the gap, re-drive) and keeps looping.
- **Escalate, don't spin:** a real blocker or no-progress-across-wakes goes up the chain.

## Done = /verify SOUND
The loop stops driving when `/verify` comes back **SOUND** against the "done" criteria.
Report what was built + the verify evidence, then stand the loop down.

## Notes
- Lean by design: ask a little -> set the goal -> the loop + `/verify` do the rest. No
  upfront PRD ceremony unless the goal is big enough to warrant decomposing inside the loop.
- `/goal-set` is the kick-off; the durable machinery is `/loop` (drive) + `/verify` (gate).
- Pairs with the curriculum: this is "run your goal," self-driving (training M14).
