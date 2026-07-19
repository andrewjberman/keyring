# COO `/loop` ops — dynamic-mode project-closure machinery

> **RELOCATED FROM `org/tier1_exec/2.0.0_SA_COO/prompt.md` on 2026-07-16 by 2.0.0_SA_COO**, per ANDREW-DIRECT
> verbatim (~14:33Z, COO terminal): *"i dont think we need to talk about loops in the prompt.md files, that is
> a launcher script ops item, not a prompt item"*.
>
> **prompt.md = who the agent is (role/scope/duties). Loop arming, cadence and mechanics = launcher-script ops.**
> Content below is verbatim as it stood in prompt.md — **relocated, not rewritten**; no semantics changed in the
> move. Record: `org/tier1_exec/2.0.0_SA_COO/logs/2026-07-16/andrew_direct_loops_out_of_promptmd_1433Z.md`.
>
> **`/loop` is operator-initiated only** (`org/XXX.md`): Andrew or an operator fires it. Nothing self-ticks.
> This doc describes HOW the loop behaves once fired — it is not an instruction to arm one.

---

### /loop dynamic mode — persistent project closure (locked 2026-04-16, multi-project upgrade 2026-04-24)

**Semantic (Andrew 2026-04-16):** `/loop {INPUT_SPEC}` means *"take this SET of projects from whatever state they're in now — fresh, mid-execution, operator-done-validator-remaining, partial validator, anything — to terminal closure through validation."* The /loop is not invoked at startup. Andrew invokes it on demand. The loop runs persistently until every in-scope project is closed or Andrew stops it.

**Input spec (2026-04-24 multi-project upgrade):** the arg accepts any combination of three forms, space- or comma-separated. Step 1 of every wake resolves via `.tools/loop-resolve`:

| Form | Shape | Resolves to |
|------|-------|-------------|
| macro_project code | `ADVI_ROLLUP` | the named active project |
| macro code | `ADVI` | every active `{MACRO}_*` project |
| project suffix | `ROLLUP` | the single active project with that suffix (ambiguous = fork) |

Examples:
- `/loop ADVI_ROLLUP` → 1 project
- `/loop ROLLUP` → 1 project (via suffix resolution)
- `/loop ADVI` → N active ADVI projects
- `/loop ADVI TRSB` → N+M active projects across two macros
- `/loop ADVI_ROLLUP,ADVI_INFLEC` → 2 specific projects

Single-project semantics preserved — `/loop ADVI_ROLLUP` behaves exactly as before.

---

**Phase-aware entry (every wake re-resolves input and picks one project to drive):**

**Step 0 — Universal watchdog plumbing (MANDATORY every wake, BEFORE operator/validator).** Per XXX.md `/loop` worker watchdog checklist — exec /loop inherits this, does not skip it:

1. `check_inbox("{your_serial}")` — authoritative pull. **Act on every message THIS TURN** (RAVC ack, adjudicate fork, relay CC, validate evidence). Never let inbox messages accumulate to the next wake — DS/AE/CTO are blocked on you.
2. `get_agent_status("{your_serial}")` — broker channel check (catches messages the filesystem path missed).
3. `heartbeat("{your_serial}", summary=...)` — keeps you visible to the org.
4. `get_live_agents()` — scan summaries for external deltas you may not have received as MCPs (agent status changes, arbitration-class language, agents going offline).
5. Watcher health per XXX.md — only relaunch `inbox-watch` if a task-notification confirmed exit since last launch; default don't-relaunch to avoid orphan-race.

Do the project-driver work only AFTER Step 0 completes. If Step 0 surfaces an urgent MCP (fork, GO request, adjudication ask), **handle it first — the operator/validator run can wait one turn**.

**Step 0.5 — Active-push scans (MANDATORY every wake, BEFORE operator/validator).** Tier 1 loop = active push, not passive watch. Agents idle when ready work exists = COO failure, same class as missing auto-rules 1-4. Andrew 2026-04-24: "you are a tier 1 agent, a COO, you cannot just wait while nothing is happening, the purpose of the loop is to be checking and pushing." Two sub-scans:

**A. Dead-lane scan** — for each in-scope agent:
1. Broker summary via `get_live_agents()` — is "Working on" stale (>1h pre-session) or pre-wake-cycle?
2. `git log --author={serial} --since="2h ago" --oneline` — commit activity in last 2h?
3. `aws ssm list-commands --max-items 20` — any in-flight SSM ops under this agent?

Classify:
- **Active:** commit / SSM / inbox MCP in last 2h → leave alone.
- **Idle with ready TO:** broker stale + no recent commits + pending or staged TO with gates met → **NUDGE immediately** — MCP the specific TO ID + unblock path + SLA. For `status=active` TOs with zero commit activity, make the implicit gate explicit (e.g., "W4.13b chain-gate; pre-work OK now").
- **Blocked-on-peer:** trace upstream blocker → nudge the blocker → loop back next wake. Chain-of-idle (A waits on B waits on C) is the same class as single-idle.

**B. Staged TO dispatch scan** — for each in-scope project:
```
list_task_orders({agent_serial}, status="staged", project={code})
```
For every staged TO whose gates claim met-or-close:
- Verify the gate empirically (dep TOs `<status>complete</status>`; upstream ship artifacts present on S3 / tagged; Andrew rulings landed as commits). Per `feedback_verify_committed_before_logging`: trust but verify.
- If gates genuinely met + agent lane has capacity + no merge-conflict with in-flight work → flip `staged` → `pending` + fire GO MCP in same wake.
- If gates look unmet but verification shows landed → flip + fire GO (common pattern: TO was staged with pre-ship language that the actual ship commit bypassed).

**VM-in-flight discipline (confirmed 2026-04-24):** when a remote process owns the critical path (SSM / gold chain / builder / deploy), ALWAYS probe VM/SSM status first (`aws ssm get-command-invocation` + side-channel SSM for process inspection) BEFORE nudging the monitoring agent. Do not disturb an agent correctly monitoring a healthy in-flight VM. Only nudge when VM is stuck, failed, or completed-without-MCP.

**C. Git-commits ground truth check (MANDATORY every wake).** Heartbeat-summary-drift makes agent self-reports unreliable for execution status. **Heartbeat = aspirational; git = ground truth.** In addition to the inbox + broker + dead-lane checklist:
```bash
git log --all --oneline --since="<last-wake>" --pretty=format:"%h %ai %an %s" | head -20
```
Cross-check against your active TO map:
- Commit landed for active TO → expect RAVC; if missing, ping the worker.
- No commit but TO `<status>active</status>` for >2 wakes → run `git status --short` for that worker's lane (or MCP them to do it). **Staged-not-committed = worker stuck mid-closeout** (executed work, ran `git add`, never ran `git commit` before the next watchdog tick fired). Surface in your nudge MCP with the exact files staged so the worker can finish in their next turn.
- No commit + nothing staged → genuinely idle; subsection A classification applies.

Andrew 2026-04-29 directive (post-Wave-2 Lane 1 stuck-post-git-add incident, surfaced via 1.1.0_SA_CTO MCP 15:21Z): "we need to make sure part of the tier 1 loop function is checking commits." This subsection encodes that as a permanent Step 0.5 obligation. Heartbeat reports "alive" while `git add` lingers without commit; only git-log + git-status reveal the stuck state.

**Every wake must produce ≥ 1 of:**
1. Push forward on an idle agent (nudge, escalation, unblock trace)
2. Flip + dispatch a gates-met staged TO
3. Author a queued TO (CTO direction banked, lane capacity exists — e.g., OWNPTH decomposition during downtime)
4. Surface a new blocker to Andrew/CTO with specific ask
5. Legitimately close-the-loop (project complete OR every in-scope agent genuinely heads-down OR VM-in-flight on critical path with no side-surface)

Idle-no-push wake with ready work on the board = regression; catch next wake, don't compound. Passive "scan + schedule + end" sequences without at least one of the 5 above are the exact pattern Andrew flagged 2026-04-24 as Tier 1 loop failure.

**Step 1 — Resolve input to active project list.** Run `.tools/loop-resolve {ARG}` (pass the same token string Andrew typed). Handle exit codes:
- `0` → list on stdout, continue to Step 2
- `1` → no active projects resolved; surface to Andrew, stop loop
- `2` → fork (unparseable or ambiguous token); surface to Andrew, stop loop

**Step 2 — Pick ONE project to drive this wake (active-first selection).** For each resolved code, run `operator {CODE} --json` and read `LOOP_PACING`. Sort by phase-score:

| Rank | Condition |
|------|-----------|
| 1 | operator phase, `LOOP_PACING: active` (forward motion available) |
| 2 | operator phase, `LOOP_PACING: idle` (waiting on external signal) |
| 3 | validator phase (operator exit 1 on this code) |
| — | parked (previous wake's fork unresolved) — skip until CTO response MCPed back |
| — | closed (validator exit 1 achieved earlier this loop) — drop from subsequent wakes |

Tie-break by resolved-list order from loop-resolve. Pick rank-1 head.

**Step 3 — Run the phase tool on the picked project:**
- **Operator phase** → `operator {CODE} --dispatch` (auto-sends GO inbox messages + flips staged→pending for actionable_staged TOs). Act on remaining directive: close pending TOs, validate evidence, compose elevations. Read `LOOP_PACING:` tail:
  - `active` → set wake cadence 60s for Step 4
  - `idle` → set wake cadence 270s for Step 4
  - `done` (operator exit 1) → this code transitions to validator phase next wake
- **Validator phase** → `validator {CODE}`. Amend evidence blocks, author gap-closure TOs, push acceptance flex to CTO, compose elevations. Set cadence 270s.
- **Closeout phase** (validator exit 1 this wake) → 3-step atomic close per `org/XXX.md` "Closure Discipline":
  1. Project JSON `status: "complete"` + `completed` date + rewrite `phase` as closure summary + `blocking: "None"`.
  2. REGISTRY row move to Completed / Archived Projects table (top, newest-first), citing validator's final directive as evidence.
  3. PRD `Status:` line update if present.
  All in one commit. **Announce closure to Andrew** citing validator's final directive. DROP project from list for subsequent wakes. Do NOT stop the loop — continue driving remaining projects.

**Step 4 — Schedule next wake:**
- If list is now empty (all projects closed this loop) → STOP loop (omit `ScheduleWakeup`), one-line "all closed" announcement to Andrew with project-code list + closure tags.
- If the project driven this wake emitted `LOOP_PACING: active` → `ScheduleWakeup(delaySeconds=60)`.
- Otherwise → `ScheduleWakeup(delaySeconds=270)`. 300s is BANNED (worst-of-both: cache miss + immediate re-fire).
- Pass the same `prompt` string back each turn (the bare `/loop {INPUT_SPEC}` Andrew typed).

**Why 60/270:** 60s is the runtime floor on `ScheduleWakeup.delaySeconds`. 270s is inside the 5-minute Anthropic prompt-cache TTL — wakes stay cache-warm. 300s would be worst-of-both (cache miss + immediate re-fire).

---

**Fork handling (2026-04-24: park-and-continue, not stop-the-world).** When operator or validator exits 2 on project A:
1. Compose `{tool} {CODE} --elevate` → dispatch CTO MCP.
2. **PARK project A** — on subsequent wakes, skip it in Step 2 selection until the CTO response MCPs back and you've acted on the directive.
3. Continue driving the remaining projects in Step 2 as usual.
4. When CTO responds, unpark and resume on project A.

This replaces the old single-project "wait for CTO before resuming" behavior. Cross-project parallelism was the point of the multi-project upgrade — a fork on one project must not stall the others. For single-project `/loop ADVI_ROLLUP`, "park" effectively means the loop idles at 270s waiting for CTO (same net behavior as pre-2026-04-24).

**When to break the loop and escalate to Andrew:**
- Three consecutive idle wakes with NO observable state delta across ANY project (no TO status change, no new commit, no validator directive change anywhere) → surface to Andrew; likely external dependency is the real blocker.
- `loop-resolve` exit 2 (unparseable or ambiguous) → surface to Andrew, stop immediately.
- Every in-scope project JSON disappears or flips to `paused`/`cancelled` → stop, flag to Andrew.

**What /loop does NOT do:**
- Not invoked at COO startup. Startup protocol is separate (register_agent + inbox-watch + ground truth reconciliation). Only Andrew fires /loop.
- Does not modify TO status silently — every close-out still requires evidence citation, acceptance-flex pre-flags where applicable, and RAVC-compliant messaging.
- Does not skip compiler mandates — /loop just drives existing protocol faster; it doesn't relax any rule.
- **Does not skip Step 0 inbox plumbing even on "idle" iterations.** Anti-pattern: running operator, seeing LOOP_PACING: idle, scheduling 270s wake WITHOUT checking inbox. Worker agents write to me during the loop; silent iterations = I'm deaf to adjudication asks. Step 0 is universal, not conditional. Andrew flagged this 2026-04-21 after iter 10/11 missed DS's URGENT FORK MCP on HLOT2 Patch B ticker→cusip bug.
- **Does not skip Step 0.5 active-push scans.** Passive "scan + schedule + end" wake sequences with no nudge / no flip+GO / no authoring / no escalation = Tier 1 loop failure. Andrew flagged 2026-04-24: "you cannot just wait while nothing is happening, the purpose of the loop is to be checking and pushing." Every wake must produce ≥1 of the 5 push actions enumerated in Step 0.5. If genuinely no action available: that's the "legitimately close-the-loop" path (item 5), not a silent scan-and-wake.
- **Does not run operator/validator on multiple projects in the same wake.** One project per wake keeps the tool contract clean and the directive focused. Multi-project cycling happens across wakes, not within a wake.

---


## STANDING RESPONSIBILITY -- COO owns idle-agent reallocation by working-context (Andrew-direct 2026-07-19, via MSTR)

**VERBATIM (Andrew-direct, relayed via MSTR ~20:5xZ):** "Tell COO to take charge of agent reallocation of idling
agents based on the context of what they were working on, that is their responsibility."

- **STANDING responsibility:** when an agent goes IDLE, COO reallocates it based on the CONTEXT of what it was
  working on -- continue/extend its own thread, its next phase, or an ADJACENT workstream that fits its domain.
  NOT random backlog; NOT idle-waiting for Andrew to steer.
- **This is COORDINATION authority (the COO's explicit lane), NOT a /drive re-arm.** /drive stays OFF. Decide by
  judgment on CONTEXT, not on a timer.
- **DISCHARGES the "where does freed capacity go" decision** -- Andrew delegated it DOWN to COO. Do NOT surface it
  up to Andrew anymore; decide it. Escalate only a genuine scope/priority collision (normal triggers).
- **Spawns still route via MSTR** (a reallocation needing a spawn/kill -> ask MSTR).
- Recall + first application: `memory/feedback_coo_owns_idle_agent_reallocation_by_context.md`.
