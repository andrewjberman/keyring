# 4.0.0_SA_CRO~B change plan -- GC and script ops (2026-10-08 ~17:3xZ)

Answers 1.0.0_SA_CTO msg 107019 (Andrew-direct ~17:1xZ: timing, and no overlap with 2.0.0_SA_COO~C).
**Fences honoured:** nothing below writes `infra/aws/terraform/nfra-ctlpln-identity/` or `org/devices/`. The reaper
has no worktree mode and never removes a worktree, so `C:/tmp/wk-ctlpln-14` and `wk-ctlpln-16` are untouched by
construction. A process working in them belongs to 2.0.0_SA_COO~C's session and is never a target.
Worktree for every row: `C:\Users\AndrewBerman\Desktop\wt-cro-b-gc`; 0.0.0_AB_MSTR lands each branch.

| # | Change | Write paths | Branch | Expected finish (UTC) |
| --- | --- | --- | --- | --- |
| 1 | Session map + MSYS link + unattended mode + scheduled-task installer | `.tools/kill-maint.ps1`, `.tools/kill-maint-task.ps1` (new), `org/tier1_exec/4.0.0_SA_CRO~B/deliverables/*`, `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261008_164xZ_*` | `cro-b/gc-sessions` | committed ~17:3xZ; landing is 0.0.0_AB_MSTR's |
| 2 | Install the unattended task on the laptop | Windows Task Scheduler only (no repo write); records to `org/mcp/agent-spawn-audit.log` | -- | ~18:0xZ, after row 1 lands and Andrew rules on cadence |
| 3 | Install on dell1 / dell2 / site Z | each box's Task Scheduler, by that box's MSTR | -- | on Andrew's rollout call |
| 4 | Long-term P1 comms watchers | `org/mcp/inbox-watch.sh`, `.tools/agentbus-sqs.sh`, `.tools/agentbus-consumer.py`, `.claude/settings.local.json` | new, per package | not started; on Andrew's go |
| 5 | Long-term P2 broker / poller / server | `org/mcp/broker.py`, `org/mcp/agent-poller.py`, `org/mcp/hook_launch_poller.py`, `org/mcp/server.py` | new | not started; on Andrew's go |
| 6 | Long-term P3 safe-* residue | `.tools/safe-merge.sh`, `.tools/safe-commit.sh`, `.tools/safe_deploy_core.py` | new | not started; **overlaps 4.0.0_SA_CRO~A (GitOps)** on safe-commit / safe-merge, so it is coordinated with ~A before any edit |
| 7 | Long-term P4 Monitor warn hook | `.claude/settings.json` (one PreToolUse entry), `.tools/hooks/monitor-bound-warn.sh` (new) | new | not started; on Andrew's go |
