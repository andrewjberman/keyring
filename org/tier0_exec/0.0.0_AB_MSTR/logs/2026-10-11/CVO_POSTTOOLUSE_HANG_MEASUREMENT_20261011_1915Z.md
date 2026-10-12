# Killed laptop CVO session: the PostToolUse "1/2" hang on a Write -- measurement (for 1.0.0_SA_CTO, msg 108392)

Measured by 0.0.0_AB_MSTR on the laptop, 2026-10-11 ~19:1xZ. No fix made.

## Which hooks fire on a Write

Two PostToolUse hooks match a Write, so the status line reads `1/2` when one has finished:

1. User level, `C:/Users/AndrewBerman/.claude/settings.json`: matcher `Edit|Write|MultiEdit`, command
   `python C:/Users/AndrewBerman/.claude/plugins/frontend-dev/hooks/auto_visual_test.py`. It acts only on files under
   `portal/src/`; for any other path it calls `sys.exit(0)` at once (lines 35-53). An `org/...md` Write exits immediately.
2. Project level, `.claude/settings.json`: matcher `*`, command `bash .tools/hooks/post-tool-hooks.sh || true`. Job 1 is
   telemetry: it appends one row per tool call to `org/mcp/agent_telemetry/<serial>.jsonl` (line 206-208). Job 2 (commitment
   detection) runs only on `mcp__opal-agent-comms__send_message`, so not on a Write.

## Which one did not finish

The killed session was session `f7f1e7e5...`, serial file `3.0.0_SA_CVO`. Its telemetry rows in
`org/mcp/agent_telemetry/3.0.0_SA_CVO.jsonl` run steadily to `2026-10-11T18:16:02.505Z` (a `Monitor` call, just after its
`register_agent` as ~L at 18:15:39Z). There is NO row for the Write. Because the telemetry row is written by
`post-tool-hooks.sh` itself, the hook that never finished is `post-tool-hooks.sh`, the project wrapper (hook 2 above),
with the plugin hook the `1` that had finished.

## How long it actually ran

The `24m 21s` on that status line is very likely the TURN's elapsed clock, not the hook's own time: the same position shows the
turn timer in other sessions' status lines (for example the CTO tab's "Schlepping... (16m 40s)" at 16:20Z). The session was killed at
`18:21:59Z` (`org/mcp/agent-spawn-audit.log` KILL line). So the Write's hook hung for at most about 6 minutes:
from after 18:16:02Z to 18:21:59Z.

## What in the wrapper can block

- Its only blocking read is the stdin read, bounded: `HOOK_INPUT="$(timeout 10 cat ...)"` (line 47).
- No lock is taken: no `mkdir` lock, no `flock`, no git call. The rest is jq and `>>` appends.
- `org/mcp/hook_errors.log` has no line between 18:00Z and 18:39Z (no JSONL_WRITE_FAIL, no unresolved-serial warning).

## Coincident laptop events in that window (the manager's own)

- `18:16:59Z KILL-MAINT-RUN ... targets=0 killed=0` (govern 18:00Z tick, `-Unattended`): it stopped nothing.
- The box pass at about 18:17Z (`box-sync.sh box`): `read-tree -m -u` under safe-commit's lock, which the hook does not take.

Neither touches the wrapper's path by design. They are the only laptop-side acts in the window, and are named so the CTO can
rule them in or out.

## Not established

- Which line of `post-tool-hooks.sh` was executing: the process is gone, and the hook logs nothing on entry. A Windows-side hang
  of an MSYS spawn (jq or the `>>` append on the 10.7 MB telemetry file) fits the evidence. Nothing here proves it.
- Whether the MSTR's own session hit the same: it runs the same two hooks; its tool calls in 18:16-18:22Z completed normally.

## A measurement that would settle it next time

Have the wrapper write one timestamped line on entry and one on exit, with its pid, to a side log. A hang then names its own
step. That is a change to `org/mcp/hooks/post-tool-hooks.sh` (its canonical source) and is the CTO's to order, not done here.
