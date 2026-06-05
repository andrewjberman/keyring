---
name: fabric-check
description: Deterministic, structured whole-fabric status — a 4-script suite covering both the AGENT axis and the PROJECT axis. AGENTS (fabric-check.py): telemetry-derived dual-signal liveness (LD-0070: LIVE<120s/ALIVE<600s/STALE) fused with the broker summary -> WORKING/IDLE/BLOCKED/SOVEREIGN/STALE-VERIFY/NEEDS-STATUS/DEAF, plus `--agents` mapping each live agent to its project with a one-line what-it's-doing. PROJECTS (fabric-projects.py): not-closed registered projects partitioned HOT (worked <72h) / COLD (>72h, still not closed), each with a <=2-sentence status. COMMITS (fabric-commits.py): scrapes git -> maps commits to project codes + authors, enriching both. Read-only, pure-filesystem/git, no MCP. Any agent ad hoc; COO chains it into /drive. Run: `python .tools/fabric-check.py` (agents, +--blocks/--agents/--json), `python .tools/fabric-projects.py` (--hot/--cold/--json), `python .tools/fabric-commits.py` (--project/--by-author/--json).
---

# /fabric-check — Fused Fabric Telemetry + Status

**One question answered:** *who is actually doing what right now, and what is stuck?*

`/fabric-check` is the canonical fabric-status display. It fuses the two signals the
fabric already produces and reconciles them:

1. **Objective liveness** — from PostToolUse telemetry (`org/mcp/agent_telemetry/*.jsonl`).
   Every tool call is timestamped; telemetry is real activity and **cannot be faked or
   go phantom**. Dual-signal (LD-0070 `TELEMETRY_LIVENESS_FRAMEWORK`):
   - `LIVE`  — most-recent `kind:work` entry within **120s** (dispatch-grade: expect a near-term response)
   - `ALIVE` — most-recent entry of ANY kind within **600s** (session alive, between work blocks / loop ticks)
   - `STALE` — last activity > 600s ago
2. **Declared status** — the broker `summary` (`org/mcp/liveness.json`), which the agent
   self-sets via `register_agent` / `heartbeat` / `set_summary`.

**Why fuse:** `get_live_agents()` derives liveness from the heartbeat file, which can read
LIVE for a session that crashed minutes ago (the phantom-live failure class). Telemetry is
ground truth; the summary is a claim. When they disagree — summary says "working on X" but
telemetry is STALE — `/fabric-check` flags it as **STALE-VERIFY** (stuck/dead, or a finished-
but-stale summary). That reconciliation is the whole point.

---

## The fabric suite — 4 deterministic scripts (2 axes)

`/fabric-check` now spans the **agent axis** AND the **project axis**, deterministically. Four
scripts, all read-only, all structured (human + `--json`):

| # | Script | Covers | Key invocations |
|---|---|---|---|
| 1 | `fabric-projects.py --hot` | **HOT projects** — not-closed, worked <72h. <=2-sentence status each. | `--hot` / `--cold` / (both) / `--json` |
| 2 | `fabric-projects.py --cold` | **COLD projects** — not-closed, >72h since work (closure-debt / stalled). | same script, `--cold` |
| 3 | `fabric-check.py --agents` | **Agent activity** — each live agent mapped to its project + a one-line what-it's-doing (telemetry + summary). | `--agents` (or folded into the full `fabric-check.py` run) |
| 4 | `fabric-commits.py` | **Commit scraper** — maps commits -> project codes + authors; ENRICHES hot/cold (last-activity + "what was done") and the agent->project mapping. | `--project CODE` / `--by-author` / `--json` |

**How they compose:** `fabric-commits` is the shared enrichment layer — `fabric-projects` uses it
for each project's last-activity (the hot/cold cut) + recent-commit context, and `fabric-check
--agents` uses it to map agents to the projects they've been committing to. "Worked on" =
max(project-JSON mtime, latest commit referencing the code). "Not closed" = status not in
complete/closed/cancelled/merged.

## Invocation (agent axis)

| Form | Use |
|---|---|
| `/fabric-check` | Full agent view (buckets) + the agent->project activity map. Any agent, any time. |
| `/fabric-check blocks` | Triage — DEAF + BLOCKED + SOVEREIGN + STALE-VERIFY. COO `/drive` uses this. |
| `/fabric-check agents` | Just the agent->project activity map (one line each). |
| `/fabric-check json` | Machine-readable rows. |

Mechanically: `python .tools/fabric-check.py` (`--blocks` / `--agents` / `--json`) for agents;
`python .tools/fabric-projects.py` (`--hot` / `--cold`) for projects. Read-only, pure-filesystem.

---

## The buckets — and what each means

| Bucket | Meaning | Who acts |
|---|---|---|
| **DEAF / UNREACHABLE** | unread messages piling in the top-level inbox + telemetry-quiet (>600s) but recently-active (<2h) — the lane's Monitor isn't delivering and (post-LD-0157) it has no self-tick to re-arm. Critical for `~A` lanes the broker can't push to. | **COO: respawn-request to MSTR** (a respawn re-arms its Monitor + lets it process the backlog). It CANNOT be tasked until then. |
| **WORKING** | telemetry LIVE/ALIVE + summary describes active work | nobody — flowing |
| **IDLE / AVAILABLE** | declared idle/available/parked/standing-by (telemetry-quiet is expected) | nobody — but a candidate for reallocation if there is queued work |
| **BLOCKED** | declared blocked, or holding/pending a ruling/decision | **COO: resolve or escalate EACH this cycle** |
| **SOVEREIGN-DECISION REQUEST** | a block whose resolution needs an Andrew/MSTR ruling | **COO declares it**; MSTR rules via `/govern` if Andrew silent 1 turn |
| **STALE-VERIFY** | summary reads as work but telemetry > 600s — stuck/dead session OR a stale summary | **COO: confirm the owner is alive** (could be a single-point stall) |
| **NEEDS-STATUS** | alive but summary declares no clear state (empty / ambiguous) | nudge the agent to set an explicit state token |

**DEAF is the post-LD-0157 reachability guard.** With worker/CTO self-tick loops retired, a lane
whose persistent Monitor dies (the occasional exit-143) no longer has a self-tick to re-arm it —
so it goes silently unreachable (unread inbox accrues, no telemetry). `~A` lanes are most exposed
(the broker suffix-strips their push, so the Monitor poll is their only delivery path). DEAF
detection (unread + quiet + recently-active) is how COO's centralized `/drive` catches these; the
fix is a respawn (MSTR creator-destroyer) which re-arms the Monitor. The deeper root-cause
(Monitor-death resilience + `~A` event-delivery) is charted to infra.

The bottom line `FABRIC-CHECK-RESULT blocked=N sovereign=N stale_verify=N needs_status=N`
is machine-parseable for chaining; `ACTION-REQUIRED:` states whether a COO move is owed.

---

## The status taxonomy — what agents SHOULD declare

`/fabric-check` infers state from loose phrasing, but the fabric is clearer when every agent's
summary leads with an explicit state token. Set your summary (via `register_agent` /
`heartbeat` / `set_summary`) to one of:

- `WORKING: <task>` — actively working; name the task.
- `IDLE: available` — no work assigned; ready for dispatch.
- `BLOCKED: <blocker>` — waiting on a dependency; name exactly what.
- `BLOCKED-SOVEREIGN: <decision needed>` — blocked AND the block needs an Andrew/MSTR ruling.

An alive agent whose summary declares none of these lands in **NEEDS-STATUS** — the signal to
fix the summary. (Past-tense "did X" descriptions are not a state declaration; say what you
are doing NOW.)

---

## For COO — `/drive` integration (the load-bearing use)

The crucial work of `/drive` is keeping the fabric *flowing*. Most advancement is event-driven
and self-healing — but the failure mode `/drive` exists to catch is the **single block that
holds up a whole project, sometimes the whole fabric**. `/fabric-check blocks` is how COO finds
those each cycle. On every `/drive` cycle:

1. Run `python .tools/fabric-check.py --blocks`.
2. For **each BLOCKED** agent → resolve it (dispatch the unblocking move through the normal
   authority chain) OR escalate it (`[STUCK]` to MSTR per the LD-0026 chain) — this cycle. A
   block left un-acted is the exact failure `/drive` prevents.
3. For **each SOVEREIGN-DECISION REQUEST** → COO **declares it**: route the decision to Andrew
   (and CC MSTR). If the nature of a BLOCKED item is that it needs sovereign discretion, COO
   must reclassify it as sovereign and declare it — do not sit on it as a normal block.
4. For **each STALE-VERIFY** → confirm the owner is actually alive (telemetry says it has not
   called a tool in >10min while its summary claims work). If dead/stuck → respawn-request to
   MSTR or re-dispatch; if just a stale summary → nudge a refresh. A stuck owner IS a
   single-point stall.
5. For **NEEDS-STATUS** → nudge the agent to set an explicit state token (status hygiene).

This does not replace `/drive`'s project-axis classification — it is the agent-axis input that
feeds it (it makes Step 2b deterministic). A block surfaced by `/fabric-check` becomes a
`/drive` dispatch or escalation like any other.

---

## The sovereign-decision-request flow (end to end)

This closes the loop Andrew specified:

1. A worker/lane hits a block that needs a sovereign call → it declares
   `BLOCKED-SOVEREIGN: <decision>` in its summary (or surfaces `[SOVEREIGN]`-tagged to COO).
2. COO's `/drive` `/fabric-check` surfaces it under SOVEREIGN-DECISION REQUESTS. **COO declares
   it** — routes the decision to Andrew, CC MSTR. COO does not resolve a sovereign-class block
   itself.
3. If `/govern` is running, MSTR's `/govern` loop checks for COO sovereign-decision-requests
   each cycle. Per Article XVI (ALWAYS-PROCEED) + the LD-0090 1-turn rule: **if Andrew has not
   responded within one operating cycle, MSTR issues the ruling** (bounded by the Directives +
   Stakes Matrix; a genuinely S3/S4-sovereign item still waits for Andrew). The ruling is
   ledgered and routed back down so the block clears.

So a sovereign block never sits: worker declares → COO declares up → Andrew rules, or MSTR
rules in his stead after one silent cycle.

---

## The canonical ~lane (tilde) liveness check (LD-0155 incident)

`/fabric-check` is the **authoritative liveness check for `~A`/`~B`/... tilde lanes**, and the
structural fix for the `get_live_agents` false-death incident (2026-06-05, Andrew-direct):

- `get_live_agents` prunes any serial whose **heartbeat** `last_seen_epoch` exceeds 600s
  (`_clean_stale`), so a tilde lane that is actively working (fresh telemetry) but has not
  heartbeated in >10min **vanishes from the live-set** — read as dead when it is alive.
- `get_agent_status("...~A")` then **falls back to the base serial** when `~A` is absent, so it
  reports the base lane's status — which *looks* like a suffix-strip but is really the masked
  false-death. The stale `live_agents_by_marker.json` is not a reliable backstop either.
- **Telemetry is the only reliable tilde-lane liveness signal**, and that is what `/fabric-check`
  reads (per-serial `…~A.jsonl`, suffix preserved). It cannot false-death an active lane.

**Doctrine:** never infer a tilde lane is dead from `get_live_agents`-absence. Verify via
`/fabric-check` (telemetry-freshness). The broker-side fix (migrate `get_live_agents` /
`get_agent_status` liveness from heartbeat-pruning to telemetry-derived per LD-0070) is charted
to the infra lane; `/fabric-check` covers the gap until it lands.

## Notes

- **Read-only.** `/fabric-check` never writes, never dispatches, never spawns. It is a lens.
  Acting on what it shows is the caller's job (COO via `/drive`; any agent ad hoc).
- **Telemetry > broker for liveness.** Prefer `/fabric-check`'s telemetry-derived liveness over
  a bare `get_live_agents()` when you need to know if an agent is *really* working (e.g. before
  routing time-sensitive work, or diagnosing a stall).
- **Engine:** `.tools/fabric-check.py` (canonical). Thresholds + taxonomy live there; tune in
  one place. Design: this file + `docs/architecture/TELEMETRY_LIVENESS_FRAMEWORK.md`.
