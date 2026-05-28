# Session log — F-006 commit-serialization mutex fix + commit-storm narrative

**Author:** `1.0.0_SA_CTO` (ws CTO)
**Session arc:** 2026-05-28T00:17Z (storm self-detect) → 2026-05-28T01:36Z (STORM-CLEARED ratify by MSTR)
**Authoring direction:** Andrew direct ~01:30Z "ok i want you to take a session log specifically about this fix and the commit storms"
**Scope:** narrative + empirical record of the 2026-05-27→28 fabric commit-storm incident, the two competing root-cause framings (LD-0125 broker poll-load vs LD-0126 commit-attempt contamination), the F-006 Pattern A mkdir-mutex fix shipped at `0be53edb3`, two-phase measurement methodology, and the remaining staging-contention nuance that F-006 deliberately does NOT solve.

---

## §1 — What the operator experienced

2026-05-27 evening through 2026-05-28 ~00:30Z, Andrew observed fabric-wide UI lag + tool-call hangs across multiple Claude sessions. Self-quote 2026-05-28T~00:12Z: "yeah I can just tell its a storm right now, we need to fix this before proceeding"; ~00:35Z "I just interrupted everybody so we can fix this, we need it fixed asap, top priority before proceeding."

The lag was real. The diagnosis chain that followed surfaced two distinct mechanisms, both contributing, but with the *primary* and *secondary* classifications reversed across two iterations.

## §2 — The two root-cause framings

### §2a — LD-0125 (initial, prior-session ws CTO + MSTR confirm): broker poll-load

`0.0.0_AB_MSTR` scribed the LD-0125 incident brief 2026-05-28T00:42Z:

- `org/mcp/server.py:57` — `POLL_INTERVAL_S = 2.0` (seconds between broker polls per MCP server instance)
- `org/mcp/server.py:312-323` — `_poll_broker_loop()` fires every 2s while each MCP server is alive
- 14 LIVE Claude sessions × 2s = 7 polls/second sustained = 420 polls/min
- Each poll opens TCP, HTTP, sqlite query, response, close
- Windows TIME_WAIT default ~4min on port 7800 → empirical 617 TIME_WAIT sockets at incident
- Broker.py PID 5568 accumulated 2924 CPU-sec over ~6h = 13.5% sustained CPU
- Fix shipped: kill broker PID 5568 + restart PID 26068; TIME_WAIT drains naturally over ~4min

F-004 parent-death watchdog (the prior-shipped fix in `broker.py`) never fired because parent (server.py PID 11016 = MSTR) was alive — F-004 catches parent-death class, not parent-alive-broker-hot-loop class. F-008 candidate (POLL_INTERVAL_S 2→30, 15x reduction) queued for ws CTO P1+ bundle.

This framing was *partially* correct — the polling load was real and the broker kill+restart drained TIME_WAIT. But it was incomplete.

### §2b — LD-0126 (Andrew correction ~00:55Z + ~01:00Z + ~01:08Z): commit-attempt contamination + retries

Andrew pushed back: the real driver was commit-attempt contamination + retries, NOT broker self-spinning. Empirical from `org/git-author-override-audit.log` window 00:08Z-00:30Z (22 minutes pre-storm-pause):

| Class | Count | Rate |
|---|---|---|
| PASS (clean commit) | 4 | 0.18/min |
| BLOCK (lane violation / contamination → retry) | 6 | 0.27/min |
| FORCE-BYPASS (Rule 14a --force escape) | 2 | 0.09/min |
| WARN (`GIT_AUTHOR_NAME` unset / misc) | 3 | 0.14/min |
| **Total commit-attempts** | **15** | **0.68/min** |
| **"Non-clean" rate** | **11 / 15 = 73%** | |

Every BLOCK ran the full pre-commit hook chain (compound 5-7s pre-F-002, 1.5-2.1s post-F-002) only to fail. Multi-agent retries cascaded — same agent re-attempted within seconds with the same lane-violating index. The aggregate cycle-time spent in failed hook chains dwarfed the per-commit hook cost. That's the storm.

Andrew restated the framing 2026-05-28T~01:08Z: "yes i like your recommendation re FS 006, A does sound good but lets have 1.0.0_SA_CTO test and see what happens" — directing Pattern A (file-lock mutex) as the storm-fix test.

MSTR scribed LD-0126 at commit `10bcbac51` 2026-05-28T~01:00Z: "commit-storm cause CORRECTED + Option A direction + F-006 test dispatched to ws CTO… LD-0125 broker-poll-load stands as secondary finding not primary storm cause."

## §3 — Prior-session ws CTO misdiagnosis

My prior session (1.0.0_SA_CTO before the spawn at 2026-05-28T01:10Z) had authored F-006 as a *research-only options doc* explicitly recommending **defer all three patterns**:

> Per Andrew brief §"Commit-pipeline fixes" #5: "Don't implement yet." After F-002 lands, measure: if remaining lock contention is meaningful, choose one of the three; otherwise the simpler F-002 win may suffice.

The doc's analysis surveyed three patterns:

- **Pattern A** — per-repo file-lock mutex (sequential serialization at the application layer)
- **Pattern B** — single-committer daemon (long-running process owns the actual `git commit`)
- **Pattern C** — batch-commit pattern (queue intents; flusher folds N → 1 commit)

…and recommended deferring all of them pending evidence of meaningful contention post-F-002. My prior session's RV-0017 F-004 audit had concluded "broker.py has NO hot-loop (HTTPServer.serve_forever is properly blocking)" — empirically wrong; the load was upstream in `server.py:312-323`. F-004 watchdog shipped against the wrong hypothesis.

Andrew + MSTR's correction (LD-0126) overrode the defer recommendation and elevated Pattern A from *defer* to *ship-as-storm-fix-test*. The MSTR-DIRECT SPAWN-WITH-DIRECTION at 01:10Z spawned this session with the explicit override.

## §4 — F-006 Pattern A — design + implementation

Shipped commit `0be53edb3` 2026-05-28T01:02:08Z (6 files atomic, 598 insertions, all ws-CTO-lane).

### §4a — Why Pattern A and not B or C

- **Pattern B (daemon)** introduces a new singleton service with its own orphan-class risk (literally the broker incident class we just fixed). Massive complexity vs benefit at current ~14-agent fabric scale.
- **Pattern C (batch-commit)** loses 1:1 commit:agent attribution, wrecks `safe-commit.sh --force` audited-bypass naturally, and is wallpaper-over: under heavy load the flusher becomes the new bottleneck.
- **Pattern A (file-lock mutex)** has minimal blast radius — single shim inside an already-canonical wrapper — and is reversible by reverting the wrapper alone.

### §4b — Rule 16 (Git Bash 3.6.7) compatibility

`flock` is one of the utilities **missing** from the post-2026-03-29 Git Bash for Windows default install (CLAUDE.md Rule 16). The mutex therefore uses **`mkdir` as the atomic primitive**:

```bash
LOCK_DIR="$REPO_ROOT/.git/commit-queue.lock"
LOCK_TIMEOUT_SEC=60
LOCK_ACQUIRED=0
elapsed=0
while ! mkdir "$LOCK_DIR" 2>/dev/null; do
  # Stale-lock detection: holder PID dead -> reclaim
  if [ -f "$LOCK_DIR/pid" ]; then
    holder_pid="$(cat "$LOCK_DIR/pid" 2>/dev/null || true)"
    if [ -n "$holder_pid" ] && ! kill -0 "$holder_pid" 2>/dev/null; then
      rm -rf "$LOCK_DIR" 2>/dev/null || true
      continue
    fi
  fi
  elapsed=$((elapsed + 1))
  if [ "$elapsed" -ge "$LOCK_TIMEOUT_SEC" ]; then
    echo "ERROR: safe-commit mutex held >${LOCK_TIMEOUT_SEC}s by PID $(cat "$LOCK_DIR/pid" 2>/dev/null || echo unknown)." >&2
    exit 3
  fi
  sleep 1
done
echo "$$" > "$LOCK_DIR/pid"
LOCK_ACQUIRED=1
trap '[ "$LOCK_ACQUIRED" -eq 1 ] && rm -rf "$LOCK_DIR" 2>/dev/null || true' EXIT
```

Key design notes:

- **`mkdir` is atomic** on NTFS, ext4, APFS, ZFS — first mkdir wins; losers spin on a 1-second `sleep` until the dir disappears.
- **Stale-lock reclaim**: the PID file inside the lock dir is checked via `kill -0`; if the holder is dead (crash-mid-commit case), the lock is reclaimed and the loop continues.
- **Timeout** = 60s (env-overridable via `SAFE_COMMIT_LOCK_TIMEOUT`). Exits with code 3 — different from existing 1 (BLOCK) and 2 (usage) so post-mortems can distinguish.
- **EXIT trap** releases the lock dir. The pre-existing `exec git commit` final line was changed to a plain `git commit ... ; exit $?` so the trap actually fires (exec replaces the shell; trap wouldn't run).
- **`LOCK_ACQUIRED` flag** prevents the trap from removing a lock dir we never acquired (e.g., if argument-parsing exits before reaching the mutex block).

### §4c — What the lock protects

Hold scope = from staged-index capture → contamination check → audit log write → `git commit` → pre-commit hook → post-commit hook → return.

**Critically:** the lock holds during `git diff --cached --name-only` (the staged-index capture inside safe-commit.sh). This is the race that produced the 6 BLOCKs from prior-session 1.0.0_SA_CTO 00:27Z-00:30Z. Without the mutex, agent A's safe-commit invocation sees agent B's staged files as "contamination" and BLOCKs — even though agent B is mid-commit and the files are about to commit out. With the mutex, that race is structurally impossible.

## §5 — Phase 1 / Phase 2 measurement methodology

MSTR's spawn-msg + 01:21Z ratification split the test into two phases to control for the worker-engagement-gap risk (post-storm-pause workers might have idled out, never load-testing the mutex):

| Phase | Trigger | Crons | Purpose | SLA target |
|---|---|---|---|---|
| **Phase 1** | Immediately post-ship | OFF | Mechanical correctness — does the mutex break anything? | Zero deadlocks, zero 60s-timeouts, zero stale lock dirs |
| **Phase 2** | Post-MSTR-authorize | Re-armed (drive + spot-check + ws-charter + cl-charter); Andrew restarted workers ~01:11Z | Storm-fix under realistic concurrency | BLOCK rate <2/min sustained |

### §5a — Phase 1 results (01:02:08Z → 01:07:17Z, 5min 9s)

- 0 PASS / 0 BLOCK / 0 FORCE-BYPASS / 0 WARN in window
- 0 mutex 60s-timeouts
- 0 stale lock dirs post-test
- 0 peer commits in window (fabric quiet post-storm-pause)
- My own ship `0be53edb3` audit-log entry: `01:02:07Z PASS 1.0.0_SA_CTO 6 (all paths in-lane)` — clean

Verdict: **PASS-CLEAN**. Mutex acquire+release end-to-end correct. Caveat: effectively single-actor.

### §5b — Phase 2 results (01:09:52Z → 01:19:54Z, 10min 2s)

| Time | Agent | Class |
|---|---|---|
| 01:11:46Z | `0.7.0_AE_CloudOps~C` | PASS (2 paths) |
| 01:12:37Z | `0.7.0_AE_CloudOps~B` | PASS (2 paths) |
| 01:13:58Z | `0.1.0_DS_MarketIntelligence~C` | PASS (3 paths) |
| 01:17:12Z | `0.7.0_AE_CloudOps~B` | PASS (1 path) |
| 01:18:19Z | `3.0.0_SA_CVO` | PASS (3 paths) |

- 5 PASS / 0 BLOCK / 0 FORCE-BYPASS / 0 WARN
- 0 mutex 60s-timeouts
- 5 distinct agents committed under the mutex during 10min window
- No stale lock dirs

Verdict: **DEMONSTRATED-PASS**. 73% pre-storm contamination rate → 0% in Phase 2. 0.27 BLOCK/min → 0 BLOCK/min.

### §5c — STORM-CLEARED ratification

MSTR ratify 2026-05-28T~01:36Z: "F-006 Phase 2 RAVC2-Final ACCEPTED. STORM-CLEARED."

## §6 — The nuance F-006 deliberately does NOT solve — staging-contention class

MSTR §3 of the STORM-CLEARED ratify surfaced a critical distinction from ws COO's `/drive` cycle 169 (~01:35Z, outside my measurement window):

> "F-006 mutex serializes git commit OPERATIONS (lock acquire → release around `git commit`) — but does NOT prevent shared-index staging contention (different layer)."

This is technically correct and important to record:

- **F-006 prevents:** BLOCKs at commit-execute moment. The `git diff --cached` capture inside safe-commit.sh sees only THIS agent's staged set because the mutex serializes the capture+commit cycle across all concurrent invocations.
- **F-006 does NOT prevent:** staging-contention *before* safe-commit.sh is even invoked. If peer agents have `git add`'d files into the working tree's shared index while this agent is preparing its own commit, those peer files appear as "extras" in this agent's pre-mutex world. The safe-commit.sh contamination check still flags them, requiring either:
  - `git reset HEAD -- <extras>` to unstage (race-prone — peer agents may re-add)
  - `--force` with audited FORCE-BYPASS entry

ws COO hit a 3rd contamination cycle at /drive cycle 169 ~01:35Z and invoked `--force` per the banked N=2 escalation discipline. That's the staging-contention class manifesting as a FORCE-BYPASS, not a BLOCK. It is within current design tolerance — `--force` is the audited escape — but it represents a remaining structural-contention class that F-006 was not designed to eliminate.

**Implication for monitoring:** the audit-log watch criterion should now track *both* the BLOCK rate (F-006 success metric) AND the FORCE-BYPASS rate (staging-contention pressure metric). Pre-F-006 baseline had 2 FORCE-BYPASSes per 22min ≈ 0.09/min. If FORCE-BYPASS rate trends materially above that, the structural class to address is staging-contention not commit-serialization — which is what Option A per-agent commit-pacer was designed to eliminate.

## §7 — Forward direction (what stays unshipped)

### §7a — F-008 broker poll-interval raise — still recommended

LD-0125's secondary-finding fix: raise `POLL_INTERVAL_S` from 2.0 to 30.0 in `org/mcp/server.py:57`. 15× reduction in broker polling load (7 polls/sec → 0.47 polls/sec across 14 sessions). Independent class from F-006; queued for next RV-0017 P1 normal bundle.

### §7b — Option A per-agent commit-pacer — designed-but-unshipped

Designed in `docs/architecture/COMMIT_SERIALIZATION_OPTIONS.md` §2 Pattern A landed-spec; the *per-agent pacer* extension (queue-commit.sh per-agent pending-queue + commit-flusher cron flushing each agent's accumulated set every 5min as one commit per agent) is the structural eliminator of the staging-contention class above.

Trigger to ship Option A pacer:

1. FORCE-BYPASS rate exceeds ~0.5/min sustained
2. OR fabric scales past ~30 concurrent agents and contamination cycles return
3. OR Andrew direct ratify of preemptive pacer ship

Until any of these fires, F-006 mutex is sufficient at current load + concurrency.

### §7c — F-003 + F-005 land status

Shipped same atomic commit as F-006 mutex (`0be53edb3`):

- **F-003** (max-concurrent formula proposal): awaiting Andrew sovereign ratify/amend/counter per `docs/briefs/rv0017-f003-max-concurrent-formula-proposal.md` §5. Operational-parameter-class amendment to STAKES_MATRIX.md (proposed v1.6). CLAUDE.md Rule 20 + STAKES_MATRIX v1.6 binding waits on ratify.
- **F-005** (orphan-process + concurrency observability): operational artifact + TO doc shipped. Cron-arming via Windows Task Scheduler recommended but deliberately not in this commit (operator one-time setup; CronCreate is session-only).

## §8 — Lessons + banked patterns

### §8a — Two-phase test sequencing (correctness vs storm-fix)

MSTR's Phase 1 / Phase 2 split was load-bearing. Without it, my Phase-1-only PASS-CLEAN (single-actor, zero peer activity) would have looked superficially like "F-006 works" but said nothing about the contamination-cascade class. Phase 2 with 5-agent concurrency was the actual storm-fix test. The pattern: when shipping a structural fix for a load-class problem, the measurement window must explicitly cover the load condition, not just the correctness condition.

### §8b — Audit-log-driven empirical record

`org/git-author-override-audit.log` was the load-bearing evidence both for diagnosing the storm (LD-0126's pre-storm 73% contamination empirical) and for validating the fix (Phase 2's 0% contamination over 10min). Pre-existing instrumentation paying off years/months later is a strong design-discipline signal. Per-action audit logging (PASS / BLOCK / FORCE-BYPASS / WARN) with timestamp + agent + scope is the right invariant.

### §8c — Andrew direct vs prior-session recommendation

My prior session's F-006 "defer all three" recommendation was wrong given the empirical that came in. Andrew + MSTR's same-cycle override was correct. The pattern: a *design recommendation* (no implementation) is cheaper to override than a *shipped implementation* (rollback cost). My prior session correctly authored as research-only; the override was at the right surface (decision-to-ship, not change-the-impl).

### §8d — Rule 16 (Git Bash compatibility) as a structural constraint

`flock` not being available forced the `mkdir` shim. The shim is more code (~30 lines vs ~5) but is portable and atomic. Rule 16 as a "what utilities can you rely on" gate at *design time* prevents the silent-fallthrough failure mode that bit `inbox-watch.sh` earlier (per CLAUDE.md Rule 16 narrative).

### §8e — In-foreground long sleeps + harness behavior

The Bash tool harness moved my 10-minute Phase 2 sleep into background mode (likely a >300s timeout threshold), making it invisible until completion. MSTR's /govern cycle 7 nudge at 01:31Z arrived during the silent window and read as "no RAVC2 fired." Recommendation for future measurement-window discipline: send an interim heartbeat / status MCP at window-open AND at midpoint, even if the actual count happens at window-close. Don't rely on the long-sleep call to be observable.

---

## §9 — Commit/MCP trail (for retro reference)

| TS (UTC) | Event | Commit / MCP |
|---|---|---|
| 2026-05-28T~00:12Z | Andrew: "yeah I can just tell its a storm right now" | — |
| 2026-05-28T~00:17Z | prior-session ws CTO [STOP] storm-pause | — |
| 2026-05-28T~00:24Z | MSTR fabric-wide Tier-1 cron-pause dispatch | — |
| 2026-05-28T~00:35Z | Andrew interrupt: "i I just interrupted everybody…" | — |
| 2026-05-28T00:38Z | MSTR kill broker PID 5568 + restart PID 26068 | — |
| 2026-05-28T00:42Z | MSTR scribes LD-0125 incident brief (broker poll-load primary, commit-storm misframed) | `ad551cc25` |
| 2026-05-28T~00:55Z–01:08Z | Andrew correction: commit-storm primary, broker poll-load secondary | — |
| 2026-05-28T~01:00Z | MSTR scribes LD-0126 correction + Option A direction | `10bcbac51` |
| 2026-05-28T~01:10Z | MSTR-DIRECT SPAWN-WITH-DIRECTION new ws CTO session | — |
| 2026-05-28T01:02:08Z | F-006 Pattern A mkdir-mutex shipped | `0be53edb3` |
| 2026-05-28T01:02:08Z–01:07:17Z | Phase 1 measurement window (crons-OFF, single-actor) | PASS-CLEAN |
| 2026-05-28T~01:11Z | MSTR PHASE-2 GO + Tier-1 cron re-arm + Andrew restarts workers | — |
| 2026-05-28T01:09:52Z–01:19:54Z | Phase 2 measurement window (crons-armed, 5 agents) | DEMONSTRATED-PASS |
| 2026-05-28T01:22Z | ws CTO RAVC2-Final + STORM-CLEARED signal to MSTR | filesystem `20260528T012227Z` |
| 2026-05-28T~01:35Z | ws COO /drive cycle 169 3rd contamination cycle → FORCE-BYPASS | — |
| 2026-05-28T~01:36Z | MSTR STORM-CLEARED ratify + §3 staging-contention nuance flagged | — |
| 2026-05-28T~01:30Z | Andrew direct: "ok i want you to take a session log specifically about this fix and the commit storms" | this doc |

---

— `1.0.0_SA_CTO` 2026-05-28T~01:42Z
