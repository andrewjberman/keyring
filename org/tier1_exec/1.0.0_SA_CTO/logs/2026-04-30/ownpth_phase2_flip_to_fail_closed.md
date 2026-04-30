# ADHC_OWNPTH Phase 2 — Flip to Fail-Closed (TO 5 ship)

**Author:** 1.0.0_SA_CTO
**Date:** 2026-04-30 (Eastern, ~08:30 ET)
**Trigger:** Andrew directive (Option B — flip today, no ride-out) after CTO state-of-play surfacing the OWNPTH options.

---

## Summary

Single-commit ship of ADHC_OWNPTH TO 5. Hook flipped from warn-mode to fail-closed in the same commit as the false-positive YAML exception classification. Canary 2-test PASS confirmed block-mode is live and the false-positive class (CTO/COO authoring task orders into pod folders) is now permitted.

---

## Context

Phase 1 (warn-mode) shipped 2026-04-24. Original plan: 7-day observe window (TO 4) → flip to block (TO 5) ~2026-05-01. Andrew chose to flip 24h early after CTO state-of-play presented the options.

**Sufficient-evidence rationale for the override:**
- TO 8 (`aa004108b`, 2026-04-29) closed the 4th-post-wrapper sweep at the loudest known offender (record-terraform-deploy.sh).
- Zero sweep incidents observed in the ~36 hours since TO 8 ship.
- Recent audit log (24h pre-flip) showed only one WARN class repeating: COO authoring task orders into pod folders (~12 entries on 2026-04-29). This is a pure false-positive — handled by YAML exception, not a sweep.
- Cost of waiting another 24h: marginal. Cost of flipping now: same YAML work either way.

---

## Changes

### 1. `.owned-paths.yaml`

- `rollout_phase: 1` → `rollout_phase: 2`.
- 8 new lane definitions: `POD1_OR_EXEC`, `POD2_OR_EXEC`, `POD3_OR_EXEC`, `POD4_OR_EXEC` (incl. tilde-suffix and underscore-suffix DS variants), `SHARED_OPAL_ETL_OR_EXEC`, `SHARED_PARTNER_ETL_OR_EXEC`, `SHARED_CLOUD_OPS_OR_EXEC`, `ANY_EXEC_OR_AE`.
- 11 new path overrides for task_orders/*.md (tier1_exec + 9 tier2_senior agent folders) — opens task-order authoring to (lane-owner OR exec) without widening parent home folders.
- 5 widened existing rules:
  - `org/projects/REGISTRY.md`: ANY_EXEC → ANY_EXEC_OR_AE
  - `org/projects/*.json`: ANY_EXEC → ANY_EXEC_OR_AE
  - `.tools/git-hooks/**`: CLOUD_OPS_OR_ETL → ANY_EXEC_OR_AE
  - `.owned-paths.yaml`: BASE_EXEC → ANY_EXEC_OR_AE
  - `portal` (submodule pointer file): UNDEFINED → ANY (added explicit rule)

### 2. `.tools/git-hooks/owned-paths-check.sh`

Line 27: `MODE="${OWNED_PATHS_MODE:-warn}"` → `MODE="${OWNED_PATHS_MODE:-block}"`.

This makes block-mode the default. The `OWNED_PATHS_MODE=warn` env var still works as a per-commit override; the YAML's `rollout_phase` field stays as documentation.

### 3. Project state

- `org/projects/ADHC_OWNPTH.json` phase narrative updated: TO 4 TRUNCATED; TO 5 COMPLETE; 8 of 9 TOs COMPLETE.
- `org/projects/REGISTRY.md` row updated: Phase 2 LIVE — fail-closed.
- TO 5 file evidence block populated with flip date, override path, YAML changes, hook change, canary test, rollback command, 48h follow-up.

---

## Canary tests (pre-commit)

Both run 2026-04-30T12:45Z UTC against the modified hook + YAML.

**Test 1 — out-of-lane should BLOCK:**
```
GIT_AUTHOR_NAME="0.1.0_DE_MarketIntelligence ..."
OWNED_PATHS_STAGED_FILES="data/orion/scripts/gold/INF_I_D03.composition_artifacts.py"
bash .tools/git-hooks/owned-paths-check.sh
```
Result: EXIT 1 + ERROR banner + BLOCK audit entry. ✓

**Test 2 — false-positive class should PASS:**
```
GIT_AUTHOR_NAME="1.0.0_SA_CTO ..."
OWNED_PATHS_STAGED_FILES="org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/SOME.001.md"
bash .tools/git-hooks/owned-paths-check.sh
```
Result: EXIT 0 + PASS audit entry. ✓ (This is the dominant pre-flip WARN class — now permitted.)

---

## Compiler Tools

| Tool | Result | Notes |
|------|--------|-------|
| `python -c "yaml.safe_load(...)"` | YAML OK; rollout_phase=2; lanes=23; paths=104 | YAML parses cleanly post-edits. |
| `bash -n .tools/git-hooks/owned-paths-check.sh` | OK | Bash syntax clean post-mode-flip. |
| `bash .tools/git-hooks/owned-paths-check.sh` (canary 1) | EXIT 1 | Block-mode active for out-of-lane. |
| `bash .tools/git-hooks/owned-paths-check.sh` (canary 2) | EXIT 0 | False-positive class now permitted. |

---

## 48h follow-up obligation

Per TO 5 acceptance §6: scan `org/git-author-override-audit.log` for BLOCK events at 2026-05-02. Triage real violations vs YAML gaps. Surface gaps as YAML diffs immediately; do NOT auto-revert without Andrew directive.

Likely-to-trip false-positive classes I didn't yet widen (will surface as BLOCK and need YAML follow-up if recurring):
- AE 0.6.1 editing `data/orion/scripts/gold/orion-gold-dispatch.sh` and INF_I_D0* scripts (currently POD4 lane; AE was authoring during INFGRD chain rerun work).
- AE editing `org/mcp/inbox-watch.sh` during PUSHFIX work (currently BASE_EXEC).
- Tilde-form-alias (1.0.0_SA_CTO_B etc.) editing `docs/architecture/*` — should be fixed by ADHC_OWNPTH.009 if/when AE 0.7 ships it.

---

## Rollback path

Single-line revert: `git revert --no-edit {{COMMIT_HASH}}` (reverts both YAML widening + hook mode flip atomically). Or to flip mode-only without losing YAML changes: edit `.tools/git-hooks/owned-paths-check.sh` line 27 back to `MODE="${OWNED_PATHS_MODE:-warn}"`.

---

## RAVC4 plan

- MCP `2.0.0_SA_COO` — TO 4 truncated by Andrew override; Phase 2 live; 48h follow-up scan calendar entry.
- MCP `0.7.0_AE_CloudOps` — Phase 2 live FYI (AE owns hook ecosystem, will see violations in audit log; tilde-form alias fix TO 9 still standing-low).
