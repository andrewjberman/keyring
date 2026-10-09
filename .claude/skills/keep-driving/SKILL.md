---
name: keep-driving
description: "Flip the keep-work-driving mode on or off in the cloud: the 10-minute open-calls scan (an open call makes the box CTO adjudicate) and the COO empty-tick rule (/next-calls --drive). One switch in S3 beside the per-box open-calls lists; every box reads it. `/keep-driving status`; `/keep-driving on|off [scan|empty_tick] [--box <box>] [reason]`; `/keep-driving inherit --box <box>`. Any seat may read; a flip is on Andrew's word."
---

# /keep-driving -- the cloud switch for the keep-work-driving mode

**Andrew-direct 2026-10-09 ~00:4xZ, verbatim:** *"I also want to be able to flip this mode on or off somewhere in the cloud, it
should be a switch that we use a skill to flip on and off, and the mode is checked via the open-calls jsons per box in aws or
something like that, should be tacked onto that process."* Approved option (a), ~00:5xZ: *"I like it, go with your rec"*.
Record: `org/tier1_exec/4.0.0_SA_CRO~B/deliverables/ANDREW_DIRECT_20261009_005xZ_KEEP_DRIVING_CLOUD_SWITCH.md`. Design of the
mode itself: `org/tier1_exec/4.0.0_SA_CRO~B/deliverables/DESIGN_KEEP_WORK_DRIVING_20261009.md`. Owner 4.0.0_SA_CRO~B.

**The switch:** `s3://opal-313476888478-globgrph/fabric/open-calls/v1/mode.json`, beside each box's `open_calls.json`.
Two parts: `scan` (the 10-minute nudge, `.tools/open-calls-scan.py`, which also carries the `/unblock` steps to the CRO, CTO,
CVO and COO) and `empty_tick` (a COO's empty `/canonical-drive` or `/closer-drive` tick runs `/next-calls --drive`). A box override beats the global value. **Absent or unreadable reads ON** (his
standing order), so the switch can pause the mode but never stop it by accident.

## Forms

| Andrew types | run |
|---|---|
| `/keep-driving status` (or bare) | `python .tools/open-calls.py mode get` |
| `/keep-driving off [scan\|empty_tick] [--box <b>] [reason]` | `python .tools/open-calls.py mode set --part <part, default all> --state off [--box <b>] --by <your serial> --reason "<his reason, or 'Andrew: off'>"` |
| `/keep-driving on [...]` | the same with `--state on` |
| `/keep-driving inherit --box <b> [part]` | `mode set --box <b> --part <part, default all> --state inherit ...` (drops the box override) |

Then print the tool's `KEEP-DRIVING ...` line back to him as it stands, and, for the scan, the last pass per box:
`python .tools/open-calls.py list --all --cloud` prints the switch line on top; each box's heartbeat
`fabric/open-calls/v1/box=<box>/scan.json` carries `mode` and `scanned_at` (a paused box reads `sent=no:mode-off`, never
silence).

## Rules

- **A flip is Andrew's act.** Run `set` only on his word in this session (or a relayed Andrew-direct naming the flip); record
  his words verbatim in the reason. Any seat may run `status`.
- The scan task stays installed on every box while off; the switch, not the task, decides. Nothing is lost while off: open
  calls stay queued and the first pass after `on` nudges at once.
- `set` refuses when the switch is unreadable (it would overwrite a value nobody read). Fix the read, then flip.
- Times to Andrew in US Eastern.
