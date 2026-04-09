# ADVI_49PUSH.010 + .017 -- Dead Code Removal + CI Gold Path Ban

**Agent:** 0.4.0_DS_ClientPlatform~A
**Date:** 2026-04-09
**Task Orders:** ADVI_49PUSH.010, ADVI_49PUSH.017
**Status:** Both complete. Portal commit pending DT push.

---

## .010 -- Dead Code Removal

### Verification Results

All comp-* and grep checks run before removing anything.

| Check | Result |
|-------|--------|
| comp-trace advisor_rolling_flows | Not in graph -- no nodes matching |
| comp-trace architect_leaderboard | Not in graph -- no nodes matching |
| comp-routes trace getAdvisorRollingFlows | No serving route |
| comp-pipescript consumers D_00 | advisor_rolling_flows + architect_leaderboard NOT in consumer list |
| grep portal/src for rolling_flows | Only types.ts definitions, no component imports |
| grep portal/src for architect_leaderboard | No references anywhere |

### Findings

- **D_00.portal_aggregates.py** -- `build_advisor_rolling_flows` and `build_architect_leaderboard` already removed in a prior session. No action needed.
- **advisor-intelligence.ts** -- `getAdvisorRollingFlows` already removed in a prior session. No action needed.
- **lib/s3_layout.py** -- No `ADVISOR_ROLLING_FLOWS` or `ARCHITECT_LEADERBOARD` constants. No action needed.
- **types.ts** -- 9 dead type definitions still present (RollingFlowsDataPoint, RollingFlowsWindowKey, AdvisorRollingSeries, AdvisorRollingFlowsResponse, StackedBarPeriodKey, AdvisorBarEntry, AdvisorRolling1YSeries, AdvisorRollingFlowsResponseV2). None imported outside types.ts. **Removed.**

Also committed incidental advisor-intelligence.ts JSDoc updates (gold/ -> platinum/ path comments, no functional change).

### Commit

| SHA | Branch | Change |
|-----|--------|--------|
| `155556b` | portal/DEV | Dead rolling flows types removed from types.ts; JSDoc comments updated |
| `9212c35c` | CLOUD | Parent repo: portal submodule pointer + TO reassignment files |

**Portal push:** DT must push portal/DEV to remote. Portal commit is staged.

---

## .017 -- CI Gold Path Ban

### Finding

`scripts/ci/check-no-gold-paths.sh` already exists (written by a prior session). Full implementation:
- Scans portal/src/pages/AdvisorIntelligence/, advisor-intelligence.ts, shared-advisor-router, opal-partners-data
- LEGACY escape hatch supported
- opal-partners-data is WARNING not ERROR
- Exit 0/1 per spec
- Works in Git Bash on Windows

### Run Result

```
0 errors, 39 warnings (non-blocking), exit 0
```

0 errors means ADVI portal code and shared-advisor-router are clean of gold/ references.
39 warnings are all in opal-partners-data (non-ADVI gold/ routes that pre-date platinum migration).
These are expected and non-blocking per spec.

### No changes needed. Task is complete as-is.

---

## Files Modified

| File | Change |
|------|--------|
| `portal/src/pages/AdvisorIntelligence/types.ts` | Removed 9 dead rolling flows type definitions (lines 1061-1123) |
| `portal/src/api/endpoints/advisor-intelligence.ts` | JSDoc comment updates only (gold/ -> platinum/ in @remarks) |

---

## Next Steps

[DT 0.4.0_DT_ClientPlatform] Push portal/DEV to remote after reviewing portal commit `155556b` (dead types removal).

No AE action needed for .010 or .017.
