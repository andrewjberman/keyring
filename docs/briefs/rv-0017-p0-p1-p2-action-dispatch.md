# RV-0017 Action Dispatch — P0 / P1 / P2 to ws CTO

**Authoring:** `0.0.0_AB_MSTR` per RV-0017 ACCEPTED-SOVEREIGN Andrew 2026-05-27T~22:25Z
**Owner:** `1.0.0_SA_CTO` (ws CTO; toolchain + broker authority)
**Source:** `org/tier0/reviews/RV-0017.md` (commit `063a0393f`)
**Anchor incident:** `docs/briefs/incident-brief-2026-05-27-wt-crash-and-commit-storm.md`

---

## §1 — Priority order (Andrew direct dispatch flow)

> "Approved, dispatch P0 first, then P1 and P2"

Andrew explicitly sequenced — ship P0 to completion before opening P1; P2 is discretionary research after P1 lands.

---

## §2 — P0 (immediate; bandwidth-restore class)

### F-002 — Profile + optimize `.tools/git-hooks/owned-paths-check.sh` to <5s/commit

**Current pain:** ~30s/commit, observed empirically in the incident brief (Incident 2 §"Smoking gun"). Each `safe-commit.sh` invocation spawns parent bash → git → child bash for the hook. With ~13 concurrent ws agents auto-committing, the lock window starves at 30s × N agents.

**Target:** <5s/commit. Drop ratio collapses the storm-class even at the current 20-cap concurrency.

**Likely optimization candidates** (incident brief §"Commit-pipeline fixes" #6):
- Replace per-file shell loops with a single `git diff --name-only` + `awk` pass over the owned-paths YAML
- Cache the owned-paths manifest in-process (currently likely re-parsed per file)
- Short-circuit on no-op diffs (empty staged set = exit fast)
- Profile with `time bash .tools/git-hooks/owned-paths-check.sh <large staged set>` first to identify the actual hot path

**Acceptance:** 5-trial median wall-time on a representative staged-set < 5s; storm-class commit-cycle (5 concurrent agents committing) no longer produces user-visible UI lag.

### F-004 — Audit + harden `org/mcp/broker.py` (parent-death self-watchdog + backoff)

**Current pain:** orphaned PID 3812 hot-looped 8158 CPU-sec / 6h45m at 10.7 MB RSS with dead parent PID 20276. Classic busy-wait — tiny memory rules out leak; sustained CPU rules out healthy event-driven design (incident brief §"Orphaned MCP broker"). Killed by Andrew this session; forensic past tense.

**Three structural fixes** (incident brief §"Scripting fixes" #1-3):

1. **Eliminate hot-loop** — audit broker.py for `while True:` without `time.sleep`, `asyncio` loops awaiting non-awaitable returns, `select`/`recv` on non-blocking socket without backoff
2. **Add parent-death self-watchdog** — periodic check; if parent PID disappears (`os.getppid() == 1` on Linux / parent-handle invalid on Windows / Python `psutil.Process(os.getppid()).is_running()` check), broker exits gracefully rather than orphans
3. **Exponential + jittered backoff** on every retry loop
4. **Process-group / job-object reap** — parent that spawns broker should also reap on exit; child should be in process group / Windows job object so termination cascades

**Acceptance:** kill broker's parent process while broker is running → broker exits within 30s; CPU usage at idle (no inbound/outbound traffic) drops to <1% (currently 33% per incident).

---

## §3 — P1 (after P0 lands; structural-hardening class)

### F-003 — Formalize `max_concurrent` formula as fabric invariant

**Current pain:** LD-0115 raised cap 16→20 absent any formula. Per incident brief §"Commit-pipeline fixes" #7: `concurrency >= (pre-commit-hook-seconds / target-cycle-seconds)` guarantees lock starvation. We exceeded the structural ceiling.

**Spec:**
```
max_concurrent_workers = floor(target_cycle_seconds / hook_latency_seconds)
```

With current 30s hook + ~5min cycle target → max ~10. **After F-002 lands** (hook ~3s) + same 5min cycle → max ~100 (well above current 20 cap).

**Action items:**
- Sister-amendment to LD-0115 codifying the formula in `STAKES_MATRIX.md` (Andrew sovereign-class amendment — proposal authored ws CTO, ratified Andrew)
- Add a `.tools/check-concurrency.sh` reading current hook-latency from a recent measurement file + emitting recommended ceiling

**Acceptance:** Formula documented in Constitution sister-amendment + checked into MEMORY.md / CLAUDE.md operating discipline section.

### F-005 — Per-host process-count + orphan-process observability

**Two alarm classes:**

1. **Process-count alarm:** >50 concurrent bash OR >20 concurrent git on host = pathological state warning. Per incident brief §"Observability fixes" #8.
2. **Orphan-process detector:** periodic sweep (every N min) enumerates PIDs whose parent PID is no longer in process table; broker.py would have been caught immediately.

**Implementation hint:** could live in `org/mcp/orphan-detector.sh` cron'd every 5min; logs to `org/mcp/orphan-audit.log` + writes hot signal to MSTR inbox if threshold tripped.

**Acceptance:** detector successfully catches a synthetic orphan (kill parent of a sleep-loop child) within 1 cycle.

---

## §4 — P2 (discretionary research; after P1)

### F-006 — Commit-serialization architectural option

**Substrate research only** (incident brief §"Commit-pipeline fixes" #4-5):

Three patterns to evaluate:
1. **Per-repo file-lock mutex** — agents acquire `.git/commit-queue.lock` before `safe-commit.sh` runs
2. **Single-committer process** — agents enqueue staged changes to a daemon; daemon serial-commits
3. **Batch-commit pattern** — agents push to queue, single flusher writes every N seconds or N changes (cuts commits/cycle ~10x)

**Don't implement yet.** After F-002 lands, measure: if remaining lock contention is meaningful, choose one of the three; otherwise the simpler F-002 win may suffice.

**Acceptance:** trade-off doc at `docs/architecture/COMMIT_SERIALIZATION_OPTIONS.md` with measurement-driven recommendation.

---

## §5 — F-007 (Andrew direct)

WT iGPU driver update OR `experimental.useAtlasEngine: false` fallback. Out of ws CTO scope; Andrew's discretion to time. Surfaced here only for completeness.

---

## §6 — Workflow

For each finding-as-TO, follow standard `/ws-charter` cycle:
1. Read this brief + the RV-0017 §2 finding entry
2. Open a TO under `org/tier1_exec/1.0.0_SA_CTO/task_orders/RV0017-FXXX-{slug}.md`
3. PRD-light if substantive (F-002 + F-004 + F-006); direct-amend if mechanical (F-003 + F-005)
4. RAVC2 ws COO after each ship; CC MSTR on completion
5. P0 first — F-002 + F-004 ship before opening F-003/F-005; F-006 last

---

## §7 — Authority + audit

- **Authority chain:** RV-0017 ACCEPTED-SOVEREIGN Andrew 2026-05-27T~22:25Z + LD-0090 ALWAYS-PROCEED + LD-0028 cross-fabric Tier-0 law (where relevant for F-003 amendment)
- **MCP audit:** dispatch MCP to ws CTO from MSTR `20260527T~22:30Z`
- **Forward CC:** ws COO on dispatch (allocation visibility); ws CVO on F-003 amendment for independent ratify per Constitution Art XIV

— `0.0.0_AB_MSTR` 2026-05-27T~22:30Z — RV-0017 P0/P1/P2 action dispatch
