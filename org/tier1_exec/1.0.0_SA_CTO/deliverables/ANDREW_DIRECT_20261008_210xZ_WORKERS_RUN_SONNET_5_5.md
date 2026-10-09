# ANDREW_DIRECT 2026-10-08 ~21:0xZ -- worker agents run Sonnet 5.5

**Channel:** laptop terminal, to 1.0.0_SA_CTO. **Recorded by:** 1.0.0_SA_CTO, same turn.

**Andrew, verbatim:**

> "Also, we need a rule where when COOs (or any agent, but particularly COOs) spawns the worker agents, those workers need to be
> using Sonnet 5.5. I believe this is already set up and adhered to across all boxes, but it is worth checking to be sure."

## Measured (2026-10-08 ~21:0xZ, after fetch)

- `.claude/agents/worker.md` and `.claude/agents/worker-light.md` read `model: sonnet` (the Sonnet alias, today Sonnet 5.5) on
  `origin/CLOUD`, `origin/box/sitez`, `origin/box/dell1` and `origin/box/dell2` (4 of 4 refs, both files).
- The gap: the Agent tool's `model` parameter overrides the definition's model, and a `general-purpose` spawn inherits the
  parent's model. The definitions alone do not stop either. Which model each of today's 257 worker commits actually ran on is
  not recorded anywhere this seat can read.

## Placement

The rule is written where every spawner reads it: the `description` of `.claude/agents/worker.md` and
`.claude/agents/worker-light.md` (the Agent tool lists it to the spawning seat): spawn by that agent type, no `model`
override, never `general-purpose` for a cell. (`.claude/skills/dispatch/SKILL.md` is over its byte budget and refused the
line.) It travels to every box by the trunk.
