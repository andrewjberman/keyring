# CTO Session - ADVI_REBORN leaderboard fees x roles fix

**Agent:** 1.0.0_SA_CTO  
**Date:** 2026-04-13  
**Project:** ADVI_REBORN

## Objective

Resolve the Advisors tab leaderboard audit finding where `Fees=Fee-Paying` plus a role toggle returns the `Fees=All` role-filtered value.

## Work Completed

- Read `docs/briefs/advi-leaderboard-fees-roles-interaction-bug.md`
- Ran compiler-tool pass against the leaderboard production and serving path
- Verified the gold producer, platinum summary transformer, and frontend reducer
- Wrote PRD addendum at `docs/architecture/ADVI_REBORN_LEADERBOARD_FEES_ROLES_FIX.md`
- Updated project and exec dashboards to reflect the reopened leaderboard follow-up under `ADVI_REBORN`

## Findings

1. `D_00c.portal_leaderboard.py` already emits nested per-role fee buckets:
   - `role_breakdown[role].fee_paying`
   - `role_breakdown[role].no_fee`
2. `D_04.client_portal_summary.py` strips those nested buckets when constructing `platinum/firm/leaderboard.json` because `_LEADERBOARD_ROLE_FIELDS` only preserves scalar role fields.
3. `portal/src/pages/AdvisorIntelligence/tabs/AdvisorsTab.tsx` then falls back to all-role values via `(data[feeView] ?? data)`, which silently drops the active fee filter whenever nested buckets are absent.
4. This is therefore backend-first, but not a fresh DS schema invention. The DS work is a platinum passthrough correction on `D_04`, followed by DE removal of the unsafe fallback.

## Decisions Made

- Keep this inside `ADVI_REBORN`, not a new project.
- Sequence work as DS then DE.
- Backend remains authoritative; frontend must consume shipped buckets and fail closed if they are missing.

## Files Modified

- `docs/architecture/ADVI_REBORN_LEADERBOARD_FEES_ROLES_FIX.md`
- `org/projects/ADVI_REBORN.json`
- `org/projects/REGISTRY.md`
- `org/tier1_exec/1.0.0_SA_CTO/prompt.md`
- `org/compiler-tools-log.md`
- `org/tier1_exec/1.0.0_SA_CTO/logs/2026-04-13/advi_reborn_leaderboard_fees_roles_fix.md`

## Compiler Tools

| Tool | Command | Result |
|---|---|---|
| `comp-build` | `python -m org.modules.graph.cli build` | PASS. Graph rebuilt: 655 nodes, 293 edges. |
| `comp-trace` | `python -m org.modules.graph.cli trace employee_leaderboard --direction both --all` | PASS. Traced `D_00c.portal_leaderboard:build_employee_leaderboard` to `gold/artifacts/employee_leaderboard.json`. |
| `comp-blast` | `python -m org.modules.graph.cli blast build_employee_leaderboard` | PASS. Blast radius is the leaderboard artifact. |
| `comp-routes` | `python -m org.modules.graph.routes_cli trace getEmployeeLeaderboard` | PASS. Confirmed serving route to `gold/artifacts/employee_leaderboard.json` via `shared-advisor-router`. |

## Current State

`ADVI_REBORN` is still active. Existing pending REBORN follow-ups remain, and the leaderboard fees x roles bug is now explicitly scoped as a new DS then DE follow-up inside the same project.

## Next Steps

- COO issues DS TO for `D_04.client_portal_summary.py`
- After DS ships and regenerates `platinum/firm/leaderboard.json`, COO issues DE TO to remove the fallback and validate the audit matrix
