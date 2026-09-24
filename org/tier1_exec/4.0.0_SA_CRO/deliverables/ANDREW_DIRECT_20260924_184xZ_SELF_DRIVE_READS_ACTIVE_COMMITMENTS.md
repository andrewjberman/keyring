# ANDREW-DIRECT 2026-09-24 ~18:4xZ (~2:4x PM ET) -- keep all three PostToolUse hooks; the CTO's /self-drive reads every seat's .active-commitments

**Channel:** the `4.0.0_SA_CRO~A` terminal, in reply to this seat's review of the PostToolUse hooks (~18:3xZ).
**Recorded by:** `4.0.0_SA_CRO~A`, same turn, at 18:42Z by the system clock.

## Verbatim

> No i like all of these, i would just have the CTO have access to that .active-commitments file when running /self-drive so that they are aware of whats going on in the fabric

## What it binds

1. **All three PostToolUse hooks stay as they are.** This seat recommended cutting two things, and neither is to be
   done:
   - the promise detector;
   - the telemetry `jq` calls.

   The hooks are:
   - `.tools/hooks/post-tool-hooks.sh` (telemetry plus the promise detector);
   - `org/mcp/hook_launch_poller.py`;
   - `org/mcp/hook_register_orphan_cleanup.py`.
2. **`/self-drive` gains a read of every seat's `.active-commitments` ledger** so the CTO sees the fabric's promised
   work.
   - Paths: `org/mcp/inbox/<base>/.active-commitments` and `org/mcp/inbox/<base>/~<lane>/.active-commitments`.
   - It is awareness, not a gate; nothing is refused on what it reads.

## Measured at the review (for the implementer)

- 67 ledger files, 428 lines.
- The detector appends; `org/mcp/complete-commitment.sh` pops lines; no code was found that calls the pop. So lines
  accumulate. Examples of the newest line per file:
  - `2.0.0_SA_COO` base: 97 lines, newest 09-10;
  - `1.0.0_SA_CTO`: 63 lines, newest today.
- How the read filters that accumulation (by age, or by live seats only) is the implementer's to choose. This record
  names no filter.

Owner: `1.0.0_SA_CTO` (`.claude/skills/self-drive/SKILL.md`).
