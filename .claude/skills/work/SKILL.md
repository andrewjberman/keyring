---
name: work
description: Universal Tier-2/3 worker-loop body. Runs every 20m per LD-0072 ratification (Andrew sovereign 2026-05-26). Walks the worker's TO queue, executes substantive work, self-classifies blockers the moment they surface and MCPs lane COO with `[BLOCKED-ASK]` for unblock-routing. Tier-2/3 only (DS / AE / DE / DT / RD + tilde-lanes); non-worker invocations halt at Step 0. Coexists with /drive (COO scans + dispatches); /work executes worker's assigned work. /watcher folds inline.
---

# /work — Tier-2/3 worker-loop body

Universal worker self-execution + self-escalation loop. Replaces the prior implicit pattern where workers waited for COO /drive to detect their STALE state and surface blockers reactively (~30-60m latency). With /work, workers self-classify blockers the moment they surface and route directly to lane COO for unblock (~5-10m latency).

## When to invoke

- Auto-armed at session start via `CronCreate /work 20m` (per `org/XXX.md` Step 1b §F worker row)
- Each cron tick re-invokes this skill
- Manually OK via `/work` for an off-cycle tick if needed (e.g., immediately after RAVC2-Accept to pick up next TO)

Other tiers invoking `/work` should HALT at Step 0 (out of scope; Tier-1 execs use /ws-charter / /cl-charter / /drive / /spot-check / /mstr-review; Tier-0 MSTR uses /mstr-* and event-triggered skills).

---

## Step 0 — HALT-gate + identify

- Run `halt-gate-check.sh` (Andrew interrupt; HALT_ACK required if pending; STOP-class hard-blocks per `docs/architecture/HALTGT_SEVERITY_CONVENTION.md`)
- Confirm caller serial matches a Tier-2/3 worker pattern: `0.x.0_(DS|AE|DE|DT|RD)_*` with optional `~B`/`~C`/`~D`/`~E` lane suffix. If not, HALT.
- Identify your **lane COO**: the COO responsible for your pod. For ajb_workspace canonical: `2.0.0_SA_COO` (ws COO). Lane workers route blockers there. (If the agent is in a different fabric, lane COO is the corresponding-fabric COO per fabric convention.)

## Step 1 — Watcher + registration (fold inline; no stacking)

Fold `/watcher` Steps 1-5 inline per /watcher SKILL.md two-loop guard. Do NOT arm a separate /watcher ScheduleWakeup — /work cron is the primary loop:

- `get_agent_status("{serial}")` → `register_agent` if STALE (use full suffixed serial; lane agents register under suffix, not base — canonical memory `feedback_b_lane_orders_only_from_b_agents` + reference_agent_spawn_kill_methodology)
- `bash org/mcp/watcher-status.sh {serial}` → kill orphans + relaunch tracked watcher if needed
- Pull inbox (broker + filesystem)

## Step 2 — Inbox classification

Classify each inbox message into one of:

| Class | Routing |
|---|---|
| ANDREW_DIRECTION | Highest priority; classify substance per Step 3 work queue; if material change to active TO, surface to lane COO with `[ANDREW-DIRECT-CC]` for awareness |
| SENIOR_DISPATCH (COO/CTO/MSTR to me) | Read fully; integrate into Step 3 queue per dispatch instructions; ACK if dispatch requests confirmation |
| PEER_ASK | Read; if blocks my current work, classify as BLOCKED-ASK trigger in Step 4; otherwise queue for response after current TO completes |
| UNBLOCK_RECEIVED | The unblock to a `[BLOCKED-ASK]` I sent earlier; resume the blocked TO at Step 3 |
| CVO_FINDING (verify-channel / spot-check) | If finding cites my work, treat as ACK-or-fix; address in Step 3; non-blocking unless severity=ERROR/BLOCK |
| OTHER / informational | Bank; no action this tick |

**Per canonical memory `feedback_b_lane_orders_only_from_b_agents`:** lane (`~B`/`~C`/etc.) workers act on dispatches only from same-lane peers; base-serial orders bounce back for re-dispatch under the appropriate lane.

## Step 3 — TO queue walk + substantive work

For my TO directory (`org/tier2_senior/{serial}/task_orders/*.md` for Tier-2; `org/tier3*/{serial}/task_orders/*.md` for Tier-3 if applicable):

1. **Read TO `<status>` of each TO**:
   - `complete` → skip
   - `staged` + dispatch_held → skip (awaiting senior GO)
   - `dispatched` / `in_progress` → primary candidate for this tick
   - `pending` → secondary candidate
   - `blocked` → re-evaluate blocker (see Step 4); skip if blocker unchanged
2. **Select highest-priority dispatched/in_progress TO** (or fall back to pending if no in-progress)
3. **Execute substantive work** on selected TO per its AC contract:
   - Read TO body + linked PRD + acceptance criteria
   - Run pre-commit gate per CLAUDE.md Rule 14 (.tools/ds-commit-gate.sh for `.py` edits)
   - Follow the deploy cycle per TO's classification (DS: Rule 13 S3 upload + comp-pipescript deployed MATCH; AE: safe-ec2-deploy.sh + EC2_MANIFEST.json; etc.)
   - Use `.tools/safe-commit.sh` per Rule 14a for commits
4. **If TO completes this tick**:
   - Update TO `<status>complete</status>` + commit per closure discipline
   - RAVC2-Request to lane COO with evidence
   - Per CLAUDE.md Closure Discipline: 3-step atomic (JSON status flip + REGISTRY row move + PRD Status line) if SINGULAR-MOMENT project close

## Step 4 — Conditional blocker handling (the LD-0072 core innovation)

If at any point during Step 3 substantive work I cannot make further progress on the selected TO due to a blocker:

### §4a — Classify the blocker

Pick the most specific class:

| Class | Examples | Routes to (suggested unblocker class) |
|---|---|---|
| `architectural` | Need design decision (e.g., A vs B implementation path); need PRD interpretation; need scope ratification | CTO |
| `operational` | Need access to a resource; need IAM grant; need TO sequencing call | COO (self-resolve) or AE |
| `verify` | Need verification of a prior commit / artifact / claim; need /verify-channel-style independent check | CVO |
| `sovereign` | Need Andrew direct decision; need S3/S4 procurement; need principal-strategy call | Andrew (via MSTR) |
| `peer-resource` | Need another worker's artifact / commit / coordination | Named peer (specify in body) |

### §4a.1 — MCP escalation ladder — chain-of-command binding (LD-0116 sovereign edict)

**Tier-2/3 workers MUST NOT MCP MSTR directly.** Per LD-0116 (Andrew sovereign direct 2026-05-27T~17:18Z) + Constitution Art. VI:

- Worker `[BLOCKED-ASK]` / `[CONSULT-REQUEST]` / `[SYNC-ASK]` / `[RAVC2-Request]` / `[SPAWN-ACK]` / status updates → **lane COO ONLY**
- Worker architectural questions / CONSULT → **lane CTO** via direct or via lane COO routing
- COO routes upward to CTO + MSTR per existing /drive cascade pattern
- CTO routes upward to MSTR + Andrew per existing /ws-charter / /cl-charter cascade pattern

**Direct worker → MSTR MCP is BANNED.** Going-forward dispatch pattern post-LD-0116:

```
COO ALLOCATION-REQUEST → MSTR
MSTR spawn-agent.ps1 [unchanged]
MSTR SPAWN-WITH-DIRECTION-SUBSTRATE → COO (single MCP)
COO authors/forwards to Worker per their lane
Worker → COO (ACKs, BLOCKED-ASK, etc.)
COO summarizes upstream to MSTR via /drive cycle ground-truth
```

**MSTR will bounce any T2/3 MCP with redirect-to-COO/CTO + not act on substantive content; will CC the responsible T1.**

Constitutional grounding: Art. VI ("govern through the org; do not bypass"). LD-0116 makes explicit that bypass includes any MCP routing direction, not just substantive task delegation. Chain-of-command is structural.

Override: explicit per-instance Andrew instruction (realistically never per LD-0116 framing).

### §4b — MCP lane COO with `[BLOCKED-ASK]`

```
to: <lane COO serial>
subject: [BLOCKED-ASK] {TO-ID} -- {one-line blocker summary}
body:
  - **Blocker description:** what specifically prevents progress (concrete; not "stuck")
  - **Suggested unblocker class:** {one of the 5 classes from §4a}
  - **TO ref:** path to TO file + TO ID
  - **Current TO state:** what's been done; what was about to happen when blocker hit
  - **Unblock concretely needed:** the specific action / decision / artifact required to resume
  - **Standing posture:** what I'll do while waiting (next TO in queue, or pure standby)
```

Per LD-0072 §4 route-via-COO design: workers uniformly route blockers to lane COO regardless of suspected unblocker class. COO has context-density (knows population + alive + capable); single point of routing update if hierarchy changes.

### §4c — Update TO + continue

- Update TO `<status>blocked</status>` with blocker note
- Commit + push (so the blocker is visible to /drive scan + audit trail)
- Continue Step 3 with NEXT available TO if any; otherwise proceed to Step 5

### §4d — Resume on UNBLOCK_RECEIVED

When Step 2 classifies an inbox message as UNBLOCK_RECEIVED for a `[BLOCKED-ASK]` I sent:
- Re-read the TO
- Update TO `<status>in_progress</status>`
- Resume Step 3 with the now-unblocked TO as primary

## Step 5 — Cycle log

Per HYBRID convention (mirroring /ws-charter LD-0062 ratification):

- **Commit-tag (100% of ticks with commits):** every tick's commit (if any) carries a `work-cycle:NNNN` trailer
- **Per-tick file (substantive ticks only, ~20-30% of ticks):** TO-completion / blocker-firing / UNBLOCK-resume ticks write `org/tier2_senior/{serial}/logs/<YYYY-MM-DD>/work_<HHMM>Z.md` (or `org/tier3*/...` for Tier-3)
- **NO-WORK ticks** (empty TO queue, all blocked, no inbox action): commit-tag only on the `register_agent`/heartbeat call; no per-tick file

## Step 6 — Heartbeat + report

```
heartbeat("{serial}", summary="<one-line tick outcome>")
```

Report (terse for NO-WORK; expanded for substantive classes):

```
/work {serial}
  TO QUEUE:     {N dispatched, M pending, K blocked, L complete}
  ACTION:       {selected TO + action taken + commit hash; OR "no actionable TO"; OR "BLOCKED-ASK fired"}
  CYCLE-LOG:    {commit-tag + file-path if substantive; commit-tag only otherwise}
  LOOP:         next cron tick in 20m
```

## Step 7 — No re-arm (cron handles cadence)

Cron auto-fires next tick at 20m interval. Do NOT call ScheduleWakeup — cron is the primary loop. Two-loop guard per /watcher SKILL.md.

---

## §Coexistence — /drive (COO) + /work (worker)

| Aspect | /work (worker) | /drive (COO) |
|---|---|---|
| Cadence | 20m | 15-20m |
| Role | execute MY assigned TOs; self-escalate blockers | scan hot-registry; dispatch work TO workers; route blockers |
| MCP target on blocker | lane COO | (whoever can unblock; COO is the router) |
| Output | TO advances + RAVC2s + BLOCKED-ASK MCPs | dispatches + routes + escalations |

**Complementary by design:** /drive surfaces work TO workers via dispatches; /work is how workers drive their assigned work forward + self-escalate. They meet at the COO/worker interface.

**Cadence offset:** 20m worker tick vs 15-20m COO tick means a blocker MCP'd at minute 0 is visible to COO /drive within ~5-15min (next /drive tick); unblock dispatch can fire same /drive cycle; worker picks up at next /work tick (~5-20min later). Total ~10-30min wall blocker→resume.

---

## §Worker discipline carry-forward from canonical memory

Cross-referenced behavioral rules that /work inherits:

- **Track in-flight TOs by artifact, not SLA** (`feedback_track_inflight_to_by_artifact_not_sla`): verify TO is progressing by commit/log on origin, never by "within SLA."
- **Surface phase artifacts during multi-phase execution** (`feedback_surface_phase_artifacts_during_execution`): send tracking exec each phase's terminal artifact (commit/deploy/emit/verdict) as you hit it; don't run heads-down to RAVC2.
- **Pre-commit gate for every `.py` edit** (CLAUDE.md Rule 14): `.tools/ds-commit-gate.sh <files>` before `git add`/`git commit`. Three checks must exit 0.
- **Commit via `.tools/safe-commit.sh`** (CLAUDE.md Rule 14a): pathspec-scoped to declared paths; aborts on contamination from concurrent agents.
- **Silver tier scope discipline** (CLAUDE.md Rule 17): silver = clean shape + preserved content; NO field-slimming, fillna, dropna, row-filtering. Business logic → gold.
- **`from __future__ import annotations` first import** (CLAUDE.md Rule 15): every `data/*/scripts/{gold,silver,bronze}/*.py` MUST begin with this for PEP-604 syntax on Python 3.9 runners.
- **Owned-paths discipline**: if a commit hits a path the worker isn't in `permitted_agents` for, the hook blocks. Route the path-class add to COO (canonical memory `feedback_tilde_lane_owned_paths_gap_route_to_coo`); do NOT --force.

---

## §Identity gate — non-worker invocations

If caller serial does not match Tier-2/3 worker pattern, halt at Step 0 with:

```
/work invoked by non-worker serial ({serial}). HALT.
This skill is Tier-2/3 only (DS / AE / DE / DT / RD + tilde-lanes).
Tier-1 execs: use /ws-charter (ws CTO) / /cl-charter (CL CTO) / /drive (COO) / /spot-check (CVO).
Tier-0 MSTR: use /mstr-review + event-triggered skills.
```

---

## §Notes

- Authority + design: LD-0072 ratified Andrew sovereign 2026-05-26 (`tier0_commit_hash` at LD-0072 commit)
- Startup-arming: `org/XXX.md` Step 1b §F worker row
- Two-loop guard: `.claude/skills/watcher/SKILL.md`
- Companion: `/drive` SKILL.md (COO scan + dispatch); `/ws-charter` SKILL.md (CTO authoring); `/spot-check` SKILL.md (CVO alignment)
- Empirical-anchor pattern reference: `memory/feedback_spawn_with_direction_fast_orient_pattern` (worker-side fast-orient on spawn)
- Cross-fabric: fabric-wide skill; ws workers + CL workers both use `/work` (single skill, lane-COO routing is per-fabric)
