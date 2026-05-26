# /ws-charter cycle #25 — MSTR BLOCKED-ASK 130522Z 3-item cluster FIX

**archetype:** IMPLEMENT
**secondary_archetypes:** SCRIBE, COORDINATE

**Date:** 2026-05-26
**UTC tick:** ~13:15Z (cycle #24 +24min; cron-fire was due at :17Z, this fired manually mid-cycle on watcher exit)
**Author:** `1.0.0_SA_CTO` (ws CTO)
**Tier-0 commit hash at authoring:** `2904f08e7` (this cycle's ship)

---

## Classification

**FIX** — structural-fix cluster within active LD-0099 / Andrew-direct scope; no new PRD; covers (a) lane widening for cross-tier startup-doc authoring, (b) mechanical ship of MSTR's blocked working-tree edits, (c) cross-fabric routing of a config asymmetry.

## Inbox classification

- Cycle-start (cron tick): `[BLOCKED-ASK] 3-item Andrew-direct lane + broker + startup-doc cluster (post-LD-0099)` from `0.0.0_AB_MSTR` at 130522Z — classified as ANDREW_DIRECTION-proxy (MSTR carrying Andrew direct sovereign 2026-05-26T~12:43-13:00Z authority).
- Mid-cycle (watcher exit during commit push): `[DRIVE] twin authoring ask: ADHC_CDNCOHT PRD v0.1 + ADHC_LEDGEH canonicalize` from `2.0.0_SA_COO` at 131322Z — classified as DRIVE_ESCALATION (FIX consideration) but with explicit "no urgency / no SLA / two-project leverage" framing; banked for cycle #26 substantive slot.

## MSTR BLOCKED-ASK action breakdown

### ASK 1 — .owned-paths.yaml lane widening

**Andrew quote:** "all tier 0 and tier 1 agents need to be able to modify XXX.md and startup docs"

**Implementation:** new lane `TIER0_TIER1_STARTUP_DOCS` (7 serials: MSTR + ws CTO/COO/CVO + CL CTO/COO/CVO) added near BASE_EXEC. Applied via path entries:
- `org/XXX.md` (both entries — line 624 original + line 1065 duplicate-for-clarity) lane: BASE_EXEC → TIER0_TIER1_STARTUP_DOCS
- 5 longest-match overrides before the `org/ref/**: ANY_EXEC` catch-all:
  - org/ref/COO_STARTUP.md
  - org/ref/RAVC_PROTOCOL.md
  - org/ref/SESSION_LOG_STANDARD.md
  - org/ref/TASK_ORDER_PROTOCOL.md
  - org/ref/PROMPT_CONSTRUCTION_PROCESS.md

**Scope observation:** the 5 listed files match the startup-class semantic exactly. Remaining org/ref/* content (prompts/, RAVC sub-files) stay in ANY_EXEC; if MSTR or a future audit identifies more startup-class candidates, single-file longest-match overrides fold in cleanly without schema disturbance.

### ASK 2 — org/XXX.md MSTR-startup ship

**Source:** LD-0099 c7dee9cd5 committed with "excl org/XXX.md" because MSTR lacked BASE_EXEC lane authority. The MSTR-drafted edits sat in ws CTO working-tree post-commit.

**Mechanical verification:** `git diff HEAD -- org/XXX.md` showed exactly 39-line delta matching LD-0099 §M2 (MSTR-startup ordering expansion: register → /watcher → CronCreate arming → Tier-0 substrate → /mstr-review once → get_live_agents + spawn missing canonical-Tier-1-set via FORCE_SPAWN → /govern) + §M4 (/govern restoration) + §"Tab-title default" paragraph (OSC 0 escape + Host.UI.RawUI.WindowTitle paired in spawn-agent.ps1 + ajb.ps1). No unrelated drift. Staged + committed via .tools/safe-commit.sh.

**Chicken-and-egg closure note:** the ASK 1 lane widening + ASK 2 file ship were committed atomically — ASK 1 makes MSTR-future XXX.md edits flow without scribe pass; ASK 2 ships the current MSTR-drafted edits. Combined, MSTR now has direct lane authority on org/XXX.md going forward.

### ASK 3 — feature_clb/.mcp.json absolute-path fix

**Routing decision:** cross-routed to `1.1.0_SA_CTO` via MCP `[CROSS-FABRIC FIX]` same cycle. The file lives on COMP branch in feature_clb worktree (verified via `cd feature_clb && git branch --show-current` = COMP); ws CTO can't commit it from ajb_workspace tree (different worktree, different branch). Per LD-0088 cross-fabric cwd, CL CTO is positioned to ship.

**MSTR's diagnosis empirically verified this cycle:**
- `feature_clb/org/mcp/server.py` EXISTS as 47832-byte 2026-04-21-dated file (pre-LD-0034).
- `feature_clb/.mcp.json` has `cwd: ajb_workspace` BUT `args: ["org/mcp/server.py"]`.
- Empirical: dual liveness.json files (ws + feature_clb each holding separate Tier-1 sets) confirm Claude Code resolves `args` paths relative to `.mcp.json` location BEFORE invoking python — `cwd` only affects server runtime CWD.
- Fix: update `args` to absolute path `["C:\\Users\\AndrewBerman\\Desktop\\ajb_workspace\\org\\mcp\\server.py"]`.
- Effect: .mcp.json is read at Claude Code session START — existing sessions unaffected; new sessions / restarts pick up the new path. Eliminates feature_clb stale broker instance.

**Fix recipe + lane endorsement + post-ship validation rubric** dispatched to CL CTO via MCP `20260526T131543Z_1.0.0_SA_CTO__CROSS-FABRIC_FIX__feature_clb_.mcp.json.md`. Will relay CL CTO commit hash to MSTR when it lands.

## Commits + MCPs this cycle

| Action | Hash / MCP-ID |
|---|---|
| ASK 1 + ASK 2 atomic ship | `2904f08e7` (ws-side, pushed to origin/CLOUD) |
| ASK 3 cross-routing | MCP to 1.1.0_SA_CTO at 131543Z |
| MSTR RAVC-ACK | MCP to 0.0.0_AB_MSTR at 131604Z (`ASK 1+2 SHIPPED 2904f08e7; ASK 3 cross-routed to CL CTO`) |
| ws COO twin-ask ACK + banking | MCP to 2.0.0_SA_COO at 131619Z (banked for cycle #26 substantive slot) |
| Per-tick cycle log | this file |

## Standing posture (unchanged)

- AC9-window quiet hold per LD-0097 §B continues.
- ws COO twin-ask (ADHC_CDNCOHT PRD v0.1 + ADHC_LEDGEH canonicalize) is exactly the slack-cycle posture LD-0097 §B envisioned — doc-only authoring, no infra churn. Cycle #26 plan provisional: both PRDs in one commit if scope holds.
- ASK 3 lands as RAVC2 close-out when CL CTO confirms.

## Authority chain

Andrew direct sovereign 2026-05-26T~12:43-13:00Z (4-message stack post-reboot return) → MSTR LD-0099 c7dee9cd5 + LD-0090 §3 ALWAYS-PROCEED → MSTR BLOCKED-ASK 130522Z routing to ws CTO (BASE_EXEC ws-canonical-host) → this cycle's atomic ship + cross-fabric routing.

## Next-cycle expected state

- If CL CTO ships ASK 3 → ACK to MSTR + closure of MSTR BLOCKED-ASK 130522Z cluster.
- Cycle #26 (cron tick :47Z): ws COO twin-ask substantive — ADHC_CDNCOHT PRD v0.1 + ADHC_LEDGEH canonicalize.
- If MSTR / Andrew traffic preempts cycle #26 substantive slot, twin-ask defers to cycle #27.

ws-charter-cycle:0025 class:FIX
