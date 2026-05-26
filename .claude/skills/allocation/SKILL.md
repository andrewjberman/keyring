# /allocation — COO Worker-Set Allocation Signal

Secondary COO loop chain-invoked at the end of every `/drive` cycle. /drive assesses **what projects need to advance**; /allocation assesses **which workers must be alive to advance them** and emits a structured deliverable for MSTR to execute (kill/spawn).

**Supply/demand split:** COO = coordinator (signals demand) → MSTR = creator/destroyer (executes supply changes within local device capacity cap). Per `memory/feedback_mstr_creator_destroyer_coo_coordinator.md` + Andrew architectural ruling 2026-05-26T~13:42Z.

---

## Invocation

| Form | Behavior |
|---|---|
| `/allocation` | Run one cycle. Default chain-invoke from `/drive` Step 8. |
| `/allocation once` | Same as bare — single cycle, no cron. |
| `/allocation off` | No-op (no cron to cancel; /allocation has no standalone cron). |

**No standalone cron.** /allocation fires as the natural next step after each /drive — allocation deltas only change when project-state changes, which /drive already detects.

---

## Step 0 — Identity gate (COO-only)

ws COO + CL COO scope. Other invokers halt with the same boilerplate as /drive Step 0.

---

## Step 1 — Read /drive cycle output

Source the most recent `logs/{YYYY-MM-DD}/coo_drive_cycle_NN_*.md` for project classification (Step 3 table) — that has the project-axis ground truth this allocation pass needs.

---

## Step 2 — Derive required-worker set

For each project in /drive's ADVANCING / NEXT-ACTION-READY / STUCK-RESOLVABLE classifications, extract the owner-lane(s) from `org/projects/{CODE}.json` `pods` field (e.g., `[0.4, 0.7]`) + any `~lane` suffix surfaced in the JSON `current_phase` / `blocking` narrative. JSON is authoritative per `memory/feedback_drive_read_json_not_registry.md`.

**STUCK-UNRESOLVED + PHANTOM-MONITORING + dormant** projects do NOT contribute to the required set this cycle (they need a routing move, not a worker).

Aggregate to required-set = union of per-project owner-lanes, deduplicated by serial.

---

## Step 3 — Cross-reference live-set + build delta

Pull `get_live_agents()`. Build three lists:

| List | Definition |
|---|---|
| **KEEP** | LIVE ∩ required-set — agent is alive AND needed. No action. |
| **SPAWN** | required-set − LIVE — needed but offline. Surface to MSTR for spawn. |
| **KILL-CANDIDATE** | LIVE − required-set − Tier-1-canonical — agent is alive but not needed for any current hot project AND is not a canonical Tier-1 (MSTR/CTO/COO/CVO never killed by /allocation). |

**Tier-1 canonical set is ALWAYS preserved** regardless of project demand — the meta-supervisory loop requires them. /allocation never signals KILL on `0.0.0_AB_MSTR`, `1.0.0_SA_CTO`, `2.0.0_SA_COO`, `3.0.0_SA_CVO`, `1.1.0_SA_CTO`, `2.1.0_SA_COO`, `3.1.0_SA_CVO`.

**KILL-CANDIDATE ≠ definitive kill.** A LIVE agent not in the current required-set may be:
- Mid-RAVC2 closeout / report writing → KEEP-EPHEMERAL (let them finish; re-evaluate next cycle)
- Idle Tier-2/3 retained for cap headroom → KILL-CANDIDATE → MSTR decides per cap policy

The deliverable enumerates the candidate list with COO reasoning per agent; MSTR has the final cap-aware decision.

---

## Step 3.5 — MSTR pre-clear MCP round-trip (LD-0105 Fix 3)

Before publishing the /allocation deliverable with SPAWN-NEEDED entries, MCP MSTR with subject `[ALLOCATION-PRECHECK]` listing proposed spawn-target serials. MSTR responds within ~30s with per-serial classification:

- **ALREADY-LIVE** — existing marker found via `org/mcp/live_agents_by_marker.json` ground-truth artifact OR live-marker scan. Redirect work to existing serial OR use `FORCE_SPAWN=1 reason="intentional-duplicate <reason>"` if a fresh spawn is genuinely required.
- **NOT-LIVE** — no marker found; safe to spawn. Promote to SPAWN-NEEDED in deliverable.

**Why this step exists:** broker `get_live_agents()` has a suffix-strip gap that can drop tilde-suffixed serials from the visible-LIVE-set. Empirical anchor: /allocation #12 ~21:38Z proposed SPAWN-NEEDED for DS 0.1.0~D while DS 0.4.0~D was already LIVE on a different scope — visual-collision-class slip that MSTR marker-scan ground-truth artifact catches. LD-0105 Fix 3 (Andrew sovereign 2026-05-26T~22:00Z "Lets do all three yes" + MSTR `5174e6b01`).

**Responsibility split codified in LD-0105:**
- **COO** = workload-state planning ("what work needs an agent")
- **MSTR** = spawn-time population gate ("is this serial already alive")
- **MSTR exposes** `org/mcp/live_agents_by_marker.json` ground-truth artifact; COO consumes for /allocation classification

**Cost:** ~10-30s wall MCP round-trip per cycle when SPAWN-NEEDED list is non-empty. Empty SPAWN-NEEDED skips the precheck (no spawns to verify). Cheap structural insurance.

**Skip-able:** if /allocation deliverable verdict is NO-DELTA (no spawns or kills), Step 3.5 is N/A. Only fires when SPAWN-NEEDED list has entries.

---

## Step 4 — Emit structured deliverable

Write to `org/tier1_exec/{COO_SERIAL}/briefs/allocation_{YYYYMMDDTHHMMZ}.md`:

```markdown
# /allocation deliverable — <UTC timestamp>

**Source /drive cycle:** #NN (logs/{date}/coo_drive_cycle_NN_*.md)
**Fabric:** ws | CL

## Required-set (from hot projects)
| Project | Required serials | Reason |
|---|---|---|

## Live-set (get_live_agents)
| Serial | Status | Last summary |
|---|---|---|

## Delta
- **KEEP:** {list}
- **SPAWN-NEEDED:** {list with project-justification per serial}
- **KILL-CANDIDATE:** {list with reason per serial; flag KEEP-EPHEMERAL where applicable}

## COO recommendation
{Plain text: e.g., "Spawn 0.4.0_DS~D for ADVI_VALFIN.002 dispatch; AE 0.7 already canonical-needed for ADHC_CDNCOHT TO-001 once AC9 clears; no kills recommended this cycle (Tier-2/3 lane already minimal)."}
```

If delta is empty (required-set ⊆ LIVE + no KILL-candidates), the deliverable still emits with `NO-DELTA-no-action-needed` verdict — bookkeeping value for MSTR's allocation history.

---

## Step 5 — MCP to MSTR

`mcp__opal-agent-comms__send_message` to `0.0.0_AB_MSTR`:
- Subject prefix: `[ALLOCATION-REQUEST]` (delta present) OR `[ALLOCATION-NO-DELTA]` (verdict-only)
- Body: deliverable path + summary (3-5 lines max — full table is in the file)

MSTR executes per `org/tier0/CONSTITUTION.md` spawn/kill authority + `feedback_concurrency_cap_ceiling_not_target.md` (cap=16 ceiling not target). MSTR may rule subset-execute / partial / defer per cap policy.

---

## Step 6 — Stand for MSTR action

/allocation does NOT block on MSTR response. /drive's next cycle re-evaluates from live-set ground truth — if MSTR didn't spawn what was requested, next /drive surfaces those projects as STUCK-RESOLVABLE again and /allocation re-surfaces the SPAWN-NEEDED entry.

---

## Coexistence

- **`/drive`** is project-axis demand signal. **`/allocation`** is worker-axis supply signal. Chain: /drive → /allocation per cycle.
- **`/stimulus-scan`** (CTO/COO) is the agent-axis classifier for non-empty work. /allocation is the supply-side complement: /stimulus-scan asks "is each LIVE agent working?"; /allocation asks "should each agent BE alive?"
- **`/mstr-spawn`** + **`/mstr-kill`** are MSTR's execution skills. /allocation is the input.

---

## Cross-fabric

ws COO emits ws-fabric allocation deliverable; CL COO emits CL-fabric. MSTR aggregates both for unified cap-aware allocation across the live cap (LD-0042 fabric-scope; LD-0049 cap=16).

---

## Notes

- v0.1 ratified Andrew sovereign 2026-05-26T~13:42Z. Empirical-tuning open: cron-chaining cadence, KILL-CANDIDATE ephemeral-keep threshold, partial-execute response loop.
- Authority anchor: `feedback_mstr_creator_destroyer_coo_coordinator.md` supply/demand architectural ruling 2026-05-22.
