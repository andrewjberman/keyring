# Incident Brief — 2026-05-27

**Host:** ANDREW (Windows 11 Enterprise 10.0.26100, 31.7 GB RAM)
**Author:** diagnostic session, post-incident
**For:** Lead agent — rectification + system fortification
**Status:** Both incidents observed same day; one user-visible crash, one ongoing degradation pattern

---

## TL;DR

Two distinct but compounding failure modes were observed on 2026-05-27:

1. **WindowsTerminal.exe leaked virtual memory from ~14.9 GB → 18.3 GB over ~17 minutes and crashed in the Intel iGPU driver at 15:58:14.** Knock-on crashes hit SentinelAgent (3:51 PM), git-credential-manager (multiple, including a hard `OutOfMemoryException`), and PatchMyPC. Root cause is a WT/Intel-GPU driver interaction under heavy scrollback + GPU-accelerated rendering, *not* a Microsoft Office process as initially hypothesized.
2. **Agent fleet generated a commit storm: 119 concurrent `bash.exe` processes driven by ~13 ws agents auto-committing through `safe-commit.sh` + `owned-paths-check.sh` pre-commit hook (~30s/commit).** A standalone `python broker.py` (MCP broker, PID 3812) hot-looped for 6h45m, burning 8158 CPU-seconds (~33% of one core continuously) on 10.7 MB of RAM — classic busy-wait. Total system CPU sat at 72% idle; perceived slowness was CPU starvation from the swarm, not RAM exhaustion (RAM was 15.8/31.7 GB used).

Both are fixable in scripting/orchestration. WT leak is mitigated for now by lowering `historySize` to 2000 in `settings.json`; the deeper fix is GPU driver + WT version.

---

## Incident 1 — WindowsTerminal VM leak → Intel iGPU crash

### Timeline (from Windows Event Log, System + Application channels)

| Time | Event | Detail |
|---|---|---|
| 15:40:56 | Resource-Exhaustion #2004 | WT (PID 18500) at **14.9 GB** virtual; SentinelAgent 1.95 GB; vmmemWSL 1.84 GB |
| 15:45:56 | Resource-Exhaustion #2004 | WT at **15.7 GB**; SentinelAgent 1.96 GB; vmmemWSL 1.82 GB |
| 15:50:56 | Resource-Exhaustion #2004 | WT at **17.1 GB**; SentinelAgent 1.94 GB |
| 15:51:04 | Service Control Manager #7031 | **SentinelAgent terminated unexpectedly**, auto-restart in 20s |
| 15:50:26 | .NET Runtime #1026 | git-credential-manager: `System.OutOfMemoryException` |
| 15:56:20 | Resource-Exhaustion #2004 | WT at **18.3 GB** (final warning) |
| 15:57:16 | .NET Runtime #1026 | git-credential-manager: `System.IO.FileLoadException` |
| 15:57:22 | .NET Runtime #1026 | git-credential-manager: `System.IO.FileLoadException` |
| **15:58:14** | **Application Error #1000** | **WindowsTerminal.exe 1.24.2605.12001 crashed** |
| 15:58:40 | Application Error #1000 | PatchMyPC-HomeUpdater crashed (0xe0434352) |

### Root cause

```
Faulting application: WindowsTerminal.exe   v1.24.2605.12001
Faulting module:      igd10umt64xe.DLL      v32.0.101.6737
                      (C:\Windows\System32\DriverStore\FileRepository\
                       iigd_dch.inf_amd64_9711ec5d8e932518\)
Exception code:       0xc0000005  (access violation)
Fault offset:         0x00000000000c568e9
```

Access violation inside the Intel integrated GPU user-mode driver. The leak pattern + crash-in-GPU-driver matches a known class of WT issues where AtlasEngine/D3D resources accumulate under heavy scrollback churn and the iGPU driver faults on the bloated state.

### Mitigation already applied this session

Edited `%LOCALAPPDATA%\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json` to add `"historySize": 2000` to `profiles.defaults` (default was 9001). Only affects newly-opened tabs.

### Recurrence confirmed in same session

After the crash, the replacement WindowsTerminal (PID 31428, started 15:59:05) was already at **1.87 GB working set / 773 CPU-seconds after ~2 hours**. Without intervention this would have repeated the crash overnight. The historySize change should slow but not eliminate the trajectory while a heavy agent swarm is generating scrollback.

### Recommended hardening for lead agent

1. **Pin the WT scrollback override across all dev hosts** via a managed `settings.json` template; the per-user default of 9001 lines × N tabs × heavy-output agents is the load bearer.
2. **Update or roll back the Intel graphics driver** — current is `32.0.101.6737` (Feb 2026 build). Test newer iGPU driver OR switch WT to the legacy DX engine: `"experimental.useAtlasEngine": false` in `profiles.defaults` while the driver issue is open.
3. **Cap GPU acceleration in agent-host terminals**: if agents are writing huge volumes of output, prefer `conhost`/pipes over interactive WT panes; the agents don't need a GPU-rendered terminal.
4. **Add a watchdog** that alerts when any single WT/console process exceeds 4 GB VM — that's the inflection point before the resource-exhaustion detector starts firing.
5. **Decouple Rio**: a second Rio terminal (PID 8940) was sitting at 2.4 GB idle. Either pick WT *or* Rio for agent output; running both compounds the pressure.

---

## Incident 2 — Agent swarm: commit storm + orphaned MCP broker

### Symptoms at observation time

- System CPU: **72.3%** with no user-foreground load
- 15.8 / 31.7 GB RAM used (not the bottleneck)
- 27.7 / 65.9 GB commit (42%; healthy)
- Visible UI lag, terminal stalls, git operations hanging on index lock

### Process census

| ProcessName | Count |
|---|---|
| **bash.exe** | **119** |
| python.exe | 17 |
| powershell.exe | 9 |
| claude.exe | 4 (the ws agents) |
| git.exe (instantaneous) | 4 |

### Evidence — the commit-cycle pattern

Cmdlines on the live bash processes consistently match this shape:

```
"C:\Program Files\Git\bin\bash.exe" -c -l "shopt -u extglob 2>/dev/null || true && eval 'git add <path> && .tools/safe-commit.sh --a..."
"C:\Program Files\Git\bin\bash.exe" -c -l "... git fetch origin CLOUD --quiet && cat org/tier1_exec/3.0.0_SA_CVO/.spot-check-checkpoint ..."
```

Each `safe-commit.sh` invocation spawns a parent bash → calls git → which spawns a child bash for the `owned-paths-check.sh` pre-commit hook. Observed long-running bash children were burning **15-19 CPU-seconds each**, which is consistent with the user-reported "~30s per commit" pre-commit hook plus git-index-lock wait time.

### Smoking gun — actual storm spike at 17:52:39

In a single 1-second window, **18 bash processes spawned simultaneously**:

```
bash 33700  17:52:38
bash 29956  17:52:38
bash  3340  17:52:38
bash 32780  17:52:39
bash  7880  17:52:39
bash  4148  17:52:39
bash  6508  17:52:39
bash 26680  17:52:39
bash  4456  17:52:39
bash  8448  17:52:39
bash 14380  17:52:39
bash 31144  17:52:40
bash 26448  17:52:40
bash 33064  17:52:40
bash 38748  17:52:40
bash 30140  17:52:40
bash 35980  17:52:40
bash 14756  17:52:40
```

This is N agents racing for `.git/index.lock` with a 30-second pre-commit hook. The user-reported observation (lock starvation + hook latency) is structurally correct; this trace is the proof.

### Orphaned MCP broker

```
PID:        3812
Command:    python.exe C:\Users\AndrewBerman\Desktop\ajb_workspace\org\mcp\broker.py
Started:    11:05:47  (6h 45m runtime at observation)
CPU time:   8158 sec  (~33% of one core, sustained, the entire day)
Memory:     10.7 MB
Parent PID: 20276  (DEAD — no longer in process table)
```

10.7 MB resident + 8158 CPU-seconds = a tight loop with no I/O wait. Tiny memory rules out leak; sustained CPU on a parentless process rules out healthy event-driven design. The parent vanishing without reaping the child is the orchestration bug — `broker.py` is now an orphan still consuming a core. **(Process was killed by the user during this session; this section is forensic.)**

### EDR amplification

SentinelOne scans every process launch. At >100 process launches per minute from the commit storm, SentinelAgent was observed at **~1.9 GB private bytes during the earlier crash window** (17× its idle baseline of ~110 MB). The MSP stack (SentinelOne + Huntress + CyberCNS + Splashtop) idles at ~230 MB total working set; the 1.9 GB ballooning is *reactive* to the workload, not a fault of the EDR itself, but it materially compounds CPU and I/O cost per commit.

### Recommended hardening for lead agent

**Scripting fixes (broker.py + agent loop):**
1. **Eliminate the broker hot-loop**. Whatever poll/wait construct exists in `broker.py` is missing a sleep or blocking on a non-blocking primitive. Audit for `while True:` without `time.sleep`, `asyncio` loops awaiting non-awaitable returns, or `select`/`recv` on a non-blocking socket without a backoff. Add a process-self-watchdog: if parent PID disappears (`os.getppid() == 1` on Linux / parent-handle invalid on Windows), the broker should exit, not orphan.
2. **Add backoff** on every retry loop (exponential, jittered).
3. **Reap children explicitly** — the parent of broker.py died without cleanup. Use a process group / job object so killing the orchestrator kills the tree.

**Commit-pipeline fixes (the actual bottleneck):**
4. **Serialize commits per repo** — agents currently race the index lock. A simple per-repo mutex (file lock on `.git/commit-queue.lock`, or a single committer process that agents enqueue to) eliminates the 18-bash spike.
5. **Batch commits** — instead of each agent committing on every step, agents push staged changes into a queue and a single committer flushes every N seconds or N changes. Cuts commits per cycle by ~10×.
6. **Profile and optimize `owned-paths-check.sh`**. The user surfaced this as a forward observation. A 30-second pre-commit hook is the single largest multiplier on the storm — if it drops to 3 seconds, the storm becomes invisible even at current concurrency. Likely candidates: replace per-file shell loops with a single `git diff --name-only` + awk pass; cache the owned-paths manifest; short-circuit on no-op diffs.
7. **Drain the worker pool** as the COO's bandwidth-rationalization recommendation suggested. Concurrency >= (pre-commit-hook-seconds / target-cycle-seconds) guarantees lock starvation; pick concurrency from that formula, not by adding workers until things break.

**Observability fixes:**
8. **Per-host process-count alarms.** Threshold: >50 concurrent bash (or >20 concurrent git) is always pathological on a dev workstation. Alert before lock starvation hits user-visible UI lag.
9. **Per-agent commit-rate metric.** Expose commits/min per ws agent; this is the leading indicator for the storm.
10. **Orphan detection.** Periodically enumerate processes whose parent PID no longer exists; broker.py would have been caught immediately.

---

## Cross-cutting observations

- The two incidents are **not causally linked** but they amplify each other: agent-driven scrollback feeds WT's leak; WT's death takes git-credential-manager with it (mid-commit), which then makes agents retry, which deepens the commit storm.
- **The user's hypothesis (Outlook / MS apps spiking on open) was incorrect.** No Office process appeared in any resource-exhaustion top-consumers list during the incident window. Worth recording so the lead agent doesn't chase that thread.
- The system has substantial headroom (16 GB RAM free, 38 GB commit headroom). The bottleneck is **CPU + process-launch rate + git-index-lock**, not memory. Fixes should target launch fan-out and hook latency, not RAM.

---

## Action checklist for lead agent

- [ ] Audit `broker.py` for the hot-loop; add backoff + self-watchdog
- [ ] Implement per-repo commit serialization
- [ ] Profile `owned-paths-check.sh`; target <5s
- [ ] Set max concurrent ws agents based on `hook_time / cycle_time` formula
- [ ] Add process-count + orphan-process alarms
- [ ] Validate WT historySize override is in the host-config template
- [ ] Test Intel iGPU driver update or fall back to legacy WT renderer
- [ ] Choose WT *or* Rio for agent output; don't run both
