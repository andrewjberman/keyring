---
name: drive
description: COO-scoped operational driver skill. Reads hot-registry (active projects in `org/projects/*.json`), classifies each project's current state against most-recent commit + RAVC2 trail + named blocker, and **dispatches the next-action OR resolving move** through the COO's normal authority chain. Hard gate per invocation = ≥1 project-advancement action OR per-project attestation that monitoring path is real. "All standing by" is NEVER an acceptable terminal state. `/drive` arms a 20m recurring cron + runs one cycle now; `/drive 30m` / `1h` / `90s` overrides cadence; `/drive once` runs a single cycle no cron; `/drive off` cancels any running cron. COO-only — other agents invoking halt at Step 0. Per LD-0056 (CY-0102 sovereign architectural directive Andrew 2026-05-25T04:50Z) — institutionalizes COO as primary operational driver; MSTR /govern refocuses to Tier-1 loop-health meta-supervisor.
---

# /drive — COO Operational Project Driver

The project-axis analogue to `/spot-check`'s agent-commit-grain alignment-sweep + /charter's architectural-authoring focus. **/drive's job is to make projects move.** Every invocation pulls hot-registry, classifies each active project, and fires the dispatch that advances it (or routes the resolving move). No reporting-without-acting.

**Authority anchor:** LD-0056 + Andrew sovereign 2026-05-25T~04:50Z verbatim — *"the COO layer 2.0 and 2.1 need to be the primary operational drivers... a skill that runs at startup for the COOs which is some kind of /drive loop that assesses hot registry projects and moves them along."*

---

## Invocation forms

| Form | Behavior |
|---|---|
| `/drive` | Run one cycle now + arm a 20m recurring cron (default). |
| `/drive 30m` / `1h` / `90s` / `15m` | Run one cycle now + arm a recurring cron at the given cadence. |
| `/drive once` | Run one cycle. Do NOT arm a cron. |
| `/drive off` (or `stop`) | Cancel any existing `/drive` cron via `CronList` + `CronDelete`. No cycle. |

Recommended cadence: **20m default while ACTIVE projects > 0; 30m when ACTIVE = 1-2 + all advancing; 60m only when ACTIVE = 0 (rare).** Never disable while ACTIVE > 0 — that is the failure mode this skill exists to prevent.

---

## Step 0 — Identity gate (COO-only)

This skill is scoped to **2.0.0_SA_COO** (ws fabric) and **2.1.0_SA_COO** (CL fabric). If the invoker is not a COO, halt with:

> `/drive is a COO-scoped skill. Your serial is {serial}, not a COO. If you want project-advancement, MCP your division's COO directly with the ask; the COO will handle from its own session per Constitution Art. VI delegation discipline.`

If COO, continue.

---

## Step 1 — Arm / cancel cron per invocation form

| Invocation | Cron action |
|---|---|
| `/drive` (no arg) | `CronList` → if `/drive` cron exists, leave it; else `CronCreate` 20m default |
| `/drive Xm` | `CronList` → `CronDelete` any existing `/drive` cron → `CronCreate` at given cadence |
| `/drive once` | No cron action |
| `/drive off` / `stop` | `CronList` → `CronDelete` any existing `/drive` cron → exit (no cycle) |

---

## Step 2 — Hot-registry read (fabric-scoped)

**ws COO** reads `org/projects/*.json` from ajb_workspace.
**CL COO** reads `feature_clb/org/projects/*.json` from feature_clb worktree.

Per LD-0042 fabric-scoping discipline: a COO drives only their fabric's registry. Cross-fabric coordination flows through MSTR or joint CTO+COO consult.

```bash
# Per project, extract status + current_phase + last-touched timestamp
for f in <registry-glob>; do
  code=$(basename "$f" .json)
  status=$(jq -r '.status // "unknown"' "$f")
  phase=$(jq -r '.current_phase // .phase // "n/a"' "$f")
  if [ "$status" = "active" ]; then
    echo "$code | $phase"
  fi
done
```

Build the hot list: all `status: active` projects + any `status: dormant`/`on-hold`/`needs-sovereign-call` that surface a blocker requiring routing (queue-hygiene escalation, not silent stale).

---

## Step 3 — Per-project classification (the core)

For each project on the hot list, classify into one of 5 states:

| Class | Detection | Action |
|---|---|---|
| **ADVANCING** | Commit / RAVC2 / dispatch in trailing N hours touching this project AND named owner is alive + active (cross-check broker LIVE + recent commit-by-serial). **Verify the monitoring path is real** — agent isn't monitoring a dead SSM (CY-0102 anchor: DS~D was "monitoring" SSM `5b18ffe4` that SIGKILL'd ~24h prior). | No new dispatch; record "ADVANCING owner={serial}, last-commit={ts}, next-RAVC2-ETA={time}" attestation. **Re-verify next /drive tick** — phantom monitoring detected here re-classifies to STUCK. |
| **NEXT-ACTION-READY** | Phase gate met (prior phase RAVC2-Accepted OR upstream artifact landed) AND next TO not yet dispatched AND named owner alive | **Author + dispatch the next-phase TO this turn** through normal COO `/charter` integration. Record TO ref + recipient + RAVC2-expected. |
| **STUCK-RESOLVABLE** | Blocker identified with named resolver path (peer can absorb, CTO can rule, MSTR can spawn, Andrew gate can clear). | **Route the resolving move this turn**: MCP to resolver with specific resolving ask + cite project + cite blocker + expected response window. |
| **STUCK-UNRESOLVED** | Blocker present + no clear resolver in chain OR resolver tried + non-responsive >1 /drive cycle | **Surface to MSTR via `[STUCK]` subject** with: project code, blocker description, prior-resolution attempts, COO recommendation. MSTR routes per LD-0026 backstop chain. |
| **PHANTOM-MONITORING** | Broker shows owner LIVE + summary says "monitoring X" + but X is verifiably dead (SSM terminated, deploy completed, upstream RAVC2 already landed) | **Route status-sync MCP through owner's chain** + ask for current-state heartbeat refresh + dispatch next-action OR explicit stand-down. Banking observation each occurrence for /mstr_review trail. |

**Magnitude-sanity heuristic** (per /govern Step 1(b) parallel discipline) — for any numeric claim a project log surfaces (dollar amount, count, ratio), apply quick magnitude-vs-context sanity check; implausible magnitude routes as **verify-channel candidate finding**, not a routine project-axis item.

---

## Step 4 — Hot-work assessment + dispatch quality check

For each NEXT-ACTION-READY or STUCK-RESOLVABLE dispatch, verify quality before firing:

1. **Does the dispatch advance THIS project's critical path** — not generic backlog-chew?
2. **RAVC2 deliverable bounded** — returnable in defined window with clear acceptance criteria?
3. **Owner role-fit** — recipient is the right hands for this surface (DS for data, AE for cloud, DE for portal, DT for trading)?
4. **Coordination-cost vs unblocking-value** — is the MCP cost proportional to the project advancement it unlocks?

If 3+ "no" → re-scope the dispatch OR reclassify project (probably STUCK-UNRESOLVED).

**Lane discipline** (per /stimulus-scan parallel): a `~B`/`~C`/`~D` lane agent takes dispatch only from same-lane exec; phantom `~lane` (TO assigned but no live agent) re-routes to live base/lane.

---

## Step 5 — DISPATCH (mandatory; no "suggested action" without firing)

Fire every classified action via `mcp__opal-agent-comms__send_message` in this same /drive cycle. **No agent leaves a /drive cycle in a stuck-without-routing state.**

**Per dispatch:**
- Subject prefix: `[DRIVE]` for project-advancement TOs; `[STUCK]` for MSTR escalations; `[SYNC]` for phantom-monitoring resyncs
- Body MUST cite: project code + phase + dispatch reason + expected RAVC2 window
- TO authored via existing `/charter` integration when full TO format needed; light MCP when nudge/sync suffices

**Cap discipline:** if a /drive cycle would produce >5 dispatches, surface top-5 + flag rest as "cycle bound; carry-forward next tick". The 20m cadence ensures carry-forward catches the remainder.

---

## Step 6 — Hard gate (THE skill's bite)

Before exiting the cycle, verify:

**Per /drive invocation: ≥1 project-advancement action fired OR per-project explicit attestation that monitoring path is real + ETA holds.**

**FORBIDDEN terminal states:**
- "All projects standing by" — projects don't stand by; they advance, stick, or get resolved. If they're standing by, the owner is mid-RAVC2 (verify) OR there's an unfired NEXT-ACTION (dispatch) OR the project is actually `dormant` not `active` (queue-hygiene to MSTR).
- "Lower-touch window holds" — that was the CY-0099/0100/0101 failure-mode framing per LD-0056. NOT a valid /drive verdict.
- Receipt-acks of prior /drive findings without new project-advancement action — receipt-acks are bookkeeping, not driving.

If the gate fails: the /drive cycle records `gate_status: FAILED` and the next cycle re-prioritizes finding genuine project advancement. Repeated gate-failure across 3 consecutive cycles = COO surfaces to MSTR with "I cannot find genuine project advancement; consider re-scoping project queue OR explicit Andrew gate-clear" finding.

---

## Step 7 — Emit findings table + log

Write the cycle output to `org/tier1_exec/{COO_SERIAL}/drive_log_{YYYYMMDDTHHMMZ}.md`:

```
## /drive cycle — <UTC timestamp>

| Project | Class | Owner | Last-touch | Action |
|---|---|---|---|---|
| ADVI_DEMOV1 | ADVANCING | 2.0.0_SA_COO cross-lane | 175min | attest LD-0055 SSM 73e0cb52 routine compute, Phase 5 ETA 13-16Z |
| ADVI_VALFIN | NEXT-ACTION-READY | 0.4.0_DS~D | 4.7h | dispatched VALFIN.012 M-1 phase-B |
| ADVI_INFETL | STUCK-RESOLVABLE | 0.5.0_AE | 8h | routed CTO architectural ruling ask |
| ADVI_SHARED | STUCK-UNRESOLVED | unclear | 12h | escalated to MSTR [STUCK] |

Dispatches fired this cycle: 3
Gate status: PASS (3 advancement actions)
```

Commit log file under COO author line via `.tools/safe-commit.sh --author "2.0.0_SA_COO <2.0.0_SA_COO@opal.agent>" ...`.

---

## Step 8 — Update last-/drive marker + heartbeat

```bash
date -u +%s > org/mcp/.last-drive-{coo_serial}
```

Heartbeat to broker with summary reflecting drive cycle output (e.g., `"drive tick 12: 3 dispatches fired (DEMOV1 attest, VALFIN.012 dispatched, INFETL routed CTO); next tick +20m"`).

---

## Coexistence with /loop and /stimulus-scan

- **`/loop` continues as COO's general supervisory wrapper** — pulls inbox, fires heartbeat, runs `/watcher` health check, monitors in-flight SSM. `/drive` is invoked **inside** `/loop` body on the 20m cadence (sooner-of: cron fire OR loop tick where 20m elapsed since last /drive).
- **`/stimulus-scan` is the agent-axis observation skill** — classifies agents (ACTIVE/IDLE/STALE/etc.) + dispatches to fix STALE agents. `/drive` is the project-axis driver — classifies projects + dispatches to advance them. Both run from COO `/loop`; they complement, not duplicate. **/stimulus-scan asks "is each agent working?"; /drive asks "is each project moving?"**
- **`/charter` is the TO/PRD authoring skill** — `/drive` calls `/charter` when a full TO needs authoring vs a light MCP nudge.

---

## Risks + mitigations

- **Over-driving the fabric** — dispatching 5+ MCPs per tick across 4 projects = exec-level signal-to-noise to workers. Mitigation: cap discipline (Step 5) + RAVC2-bounded dispatch quality check (Step 4) + lane discipline.
- **Race with /spot-check fix-and-route pattern** — CVO `/spot-check` may also surface drift on alignment-metadata. If COO `/drive` and CVO `/spot-check` are firing on the same project, lane discipline applies: CVO owns alignment-metadata fixes within its scope; COO owns operational-advancement dispatches; conflict routes to MSTR per LD-0033 Q5.
- **False-positive STUCK classification on long-compute projects** — a project in a multi-hour SSM/transform/RAVC2 window may show no commits for 12h+ while genuinely advancing. Mitigation: ADVANCING classification requires the monitoring path verification (Step 3) — owner alive + summary references a verifiable in-flight artifact (SSM command-id checked via `aws ssm list-commands`, CloudWatch log polling, etc.). If monitoring path is real, classify ADVANCING + attest; if dead, classify PHANTOM-MONITORING.
- **CL-fabric path differences** — CL COO operates against `feature_clb/` worktree paths; this skill body uses ws paths as exemplars. CL COO substitutes their fabric's project registry + log paths. **Fabric-scoped per LD-0042; no cross-fabric driving.**

---

## Notes

- **Authority anchor:** LD-0056 (CY-0102 sovereign architectural directive Andrew 2026-05-25T04:50Z). The layer-of-concerns reorganization makes COO the primary operational driver; this skill is the executable artifact.
- **Coexistence with /govern:** MSTR /govern now verifies /drive (+ /charter + /spot-check) loop-health each cycle. If COO /drive hasn't fired in N hours OR shows repeated gate-failures, /govern routes loop-health correction to COO. /drive itself is COO-owned; /govern doesn't run /drive — it verifies it.
- **First-fire observation banking** — first 5 /drive cycles per COO produce empirical thresholds for tuning (cadence, dispatch cap, classification edge cases). Surface in next `/mstr_review` reporting parallel to class-6 §2.2 + CL_STALL_CHECK V1 threshold paradigms.
- **Charter:** there is no separate charter doc this V1; the skill body IS the charter. If empirical use surfaces need for separate detailed doctrine doc (parallel to `org/tier1_exec/3.0.0_SA_CVO/SPOT_CHECK.md`), author at `org/tier1_exec/2.0.0_SA_COO/DRIVE.md` post-empirical-tuning.
- Design + law: LD-0056 + `/govern` SKILL.md Notes section (light note this cycle; full slim deferred LD-0057+).
