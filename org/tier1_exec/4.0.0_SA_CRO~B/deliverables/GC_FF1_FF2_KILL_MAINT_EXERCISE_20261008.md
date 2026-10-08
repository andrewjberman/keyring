# GC FF1 + FF2: kill-maint.ps1 patch exercise (laptop, 2026-10-08 ~16:1xZ)

**Author:** 4.0.0_SA_CRO~B. **Order:** CTO FAST FIX ruling item 5,
`org/tier1_exec/1.0.0_SA_CTO/deliverables/FAST_FIX_RULINGS_20261008_162xZ.md` @7c000ba1b6 (msg 106982).
**Lands:** 0.0.0_AB_MSTR. **Patched file:** `.tools/kill-maint.ps1` (scripts mode and the kill step; apps mode untouched).
**Rollback:** revert the one commit.

## What changed

1. **FF1, whole-tree stop.** Execute runs `taskkill /T /F /PID`, never `Stop-Process -Id`. It skips a target with a
   claude process beneath it, and a PID that has exited or been reused since the snapshot (CreationDate re-read).
2. **FF2, four classes.**
   - ORPHAN: bash/py outside every live claude tree, older than the Monitor cap. The Bash-tool-shell exemption is
     dropped.
   - NATIVE: typeperf/awk/gawk/tail/timeout under the same rule.
   - REPLACED: an older inbox-watch or agent-poller copy for one serial, or an older agentbus watch. The newest copy is
     kept.
   - ORPHANED: an inbox-watch or agent-poller whose serial has no live `server.py` PID in `org/mcp/liveness.json`.
     If liveness is unreadable, this class is off for the run.
3. **New age floor, `-MonitorCapSeconds 1860`, for anything outside a live claude tree.** A live seat's Monitor reads
   a DEAD Windows parent (this seat's own watcher, PID 2444), so ancestry cannot tell a live Monitor from a leaked
   one. The harness kills every Monitor at 1800 s.
4. **Never targets:** broker/server/agentbus-consumer; anything matching `[\/]drain-`; and in-flight
   `safe-(commit|merge|deploy|apply).sh`, `commit-worker.sh`, `commit-gate.sh`, `terraform`.
5. **New parameters:** `-OnlyPid` (spot-kill) and `-LivenessPath`. Owner-keyed rows kept are printed as KEEP.

## Arms (re-run against the patched script)

| Arm | Plant | Result |
| --- | --- | --- |
| A | bash `typeperf -si 1 \| awk`, wrapper stopped with Stop-Process (harness-style) | typeperf + awk survived (2 + 2 incl. B). The patched dry run listed both pairs as NATIVE and both pipeline subshells as ORPHAN. Execute: 0 typeperf, 0 awk after |
| B | the same tree left intact | listed (wrapper ORPHAN). Execute: `stopped tree PID 13720 (+3 descendant(s))` |
| C | the same pipeline under `timeout 4 bash -c` | rc 124; patched dry run: no typeperf/awk target |
| REPLACED | two fake `inbox-watch.sh 9.9.9_GC_TEST~R stream` (owner made live in a test liveness file) | older 17160 targeted, newest 20700 KEEP (copies=2); after Execute 17160 dead, 20700 alive |
| ORPHANED | fake `inbox-watch.sh 9.9.9_GC_TEST~X stream` (owner absent) | targeted; stopped with its sleep child |
| Negative control | this seat's live watcher 2444 and every live seat's watcher/poller | KEEP in every run; 2444 alive after Execute |

The exercise ran with `-MonitorCapSeconds 5 -MinAgeSeconds 3`, and Execute ran with `-OnlyPid` set to the nine plant
PIDs. Result: `DONE: killed 4, failed 0`; the other five were already gone, taken by their tree's stop.

**Found during the exercise:** at a 5 s cap, a LIVE seat's in-flight `safe-apply.sh` (terraform apply) and
`safe-commit.sh` showed as ORPHAN, because their Windows parents were dead MSYS forks. This led to the never-target
in-flight rule above; re-run after it: 0 targets. The UNPATCHED script has the same exposure with only its 60 s floor:
a `/kill scripts go` today can stop a live seat's commit or apply that has run past 60 s.

## Census of record (defaults, real liveness, 16:18:48Z)

```
owners: 5 serial(s) with a live MCP server ... ; Monitor cap 1860s
--- owner-keyed infra KEPT (owner live; newest copy) ---
  KEEP agent-poller 0.0.0_AB_MSTR / 1.0.0_SA_CTO / 4.0.0_SA_CRO / 4.0.0_SA_CRO~A / 4.0.0_SA_CRO~B (copies=1 each)
  KEEP inbox-watch  0.0.0_AB_MSTR / 1.0.0_SA_CTO / 4.0.0_SA_CRO / 4.0.0_SA_CRO~A / 4.0.0_SA_CRO~B (copies=1 each; ~B = PID 2444)
OK: no kill targets found. Nothing to do.
```

## Residual risk (not closed by this patch)

- A legitimate `run_in_background` job outside a claude tree, other than safe-*/terraform, that runs past 31 minutes
  (for example, a long gold run) is an ORPHAN target. The dry-run read before `go` is the check.
- A seat that armed a watcher without registering shows its watcher as ORPHANED.
- CTO gap 5 (a hung `claude.exe` shields its tree) is not addressed.
