# ADVI_SNPLBK Thread Orchestration and Task Order Issuance — 2.0.0_SA_COO

**Date:** 2026-03-10
**Start Time:** 18:00
**End Time:** 18:30

## Objective

Diagnose the Snapshot Lookback regression on the Distribution tab (Segment Analytics panel).
The quarterly "time machine" strip (current + 3 prior quarters) stopped rendering. Project
ADVI_SNPLBK was registered by Andrew; COO was tasked with thread orchestration and task order issuance.

---

## Work Completed

### 1. Pre-Flight Investigation

Identified key source files before thread creation:
- Script 09: `data/black_diamond/scripts/gold/09_generate_partner_analytics.py` -- produces quarterly lookback data
- DistributionTab: `portal/src/pages/AdvisorIntelligence/tabs/DistributionTab.tsx` -- consumes lookback data
- Types: `portal/src/pages/AdvisorIntelligence/types.ts` -- `PartnerAnalyticsViewWithPeriods`, `hasTimeMachine()`
- API endpoint: `portal/src/api/endpoints/advisor-intelligence.ts` -- passthrough fetch, no transforms
- Publisher: `infra/aws/lambda/bd-pipeline/bd-portal-publisher/lambda_function.py` -- partner_analytics DISABLED (line ~1745)

### 2. Thread ADVI_SNPLBK-001 (Pattern 0 Diagnostic Variant)

| Field | Value |
|-------|-------|
| Thread ID | ADVI_SNPLBK-001-snapshot-lookback-regression-diagnosis |
| Participants | DS (opening) + DE + RD (round robin, 3 turns each) |
| Model | gpt-5.2 |
| Tools | Enabled |
| Outcome | DE + RD converged. Both cleared their boundaries. |

**Thread conclusion:** Two candidates identified:
- A) Backend: S3 quarterly JSON missing q1/q2/q3 (current-only output)
- B) Frontend: granularity mismatch (fetching monthly/annual file while strip is hardcoded to q1/q2/q3)

Both agents requested DS confirm the S3 payload shape as the single discriminator.

### 3. COO Post-Receipt S3 Verification

Inspected the live S3 object directly:

```
s3://opal-data-bd/gold/partner_analytics/header_metrics_quarterly.json
```

| Check | Result |
|-------|--------|
| `views.geo` keys | `current, q1, q2, q3` |
| `views.adv` keys | `current, q1, q2, q3` |
| `views.nna` keys | `current, q1, q2, q3` |
| `periods` keys | `current, q1, q2, q3` |
| `views.geo.current` keys | `donut, distribution, metrics` |

**Verdict: Backend is fully intact. Regression is frontend-only.**

### 4. Frontend Call-Site Verification

Verified from repo code:
- `AdvisorIntelligence.tsx:79`: `useState<GranularityOption>('quarterly')` -- defaults to quarterly
- `AdvisorIntelligence.tsx:87`: `getPartnerAnalytics(granularity)` -- uses state variable
- `DistributionTab.tsx`: does NOT receive a `granularity` prop; strip is hardcoded to `q1/q2/q3`
- Granularity toggle exists in `PartnerAnalytics.tsx:921` (Month/Quarter/Year buttons)

**Key finding:** If user switches granularity to monthly/annual, the data refetches with
`m1/m2/m3` or `y1/y2/y3` keys, but DistributionTab strip is hardcoded to `q1/q2/q3`.
This would cause the strip to collapse. However, the default is quarterly, so this alone
does not explain a permanent regression. Live browser debugging is needed.

### 5. Task Orders Issued

| Task Order | Agent | File |
|------------|-------|------|
| ADVI_SNPLBK.001.snapshot-lookback-frontend-fix | 0.4.0_DE_ClientPlatform | `org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/` |
| ADVI_SNPLBK.001.snapshot-strip-visual-fix | 0.4.2_RD_AdvisorIntelligence | `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/task_orders/` |

DE leads the investigation (runtime debugging). RD supports with strip component fixes if
the root cause is a granularity mismatch requiring dynamic period keys.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Backend cleared -- no DS task order needed | S3 JSON verified complete by COO |
| DE leads frontend investigation | DE owns API wiring and page-level data flow |
| RD depends on DE diagnosis | RD should not change strip until root cause is confirmed |
| Granularity mismatch is primary hypothesis | Only plausible FE-side cause given intact backend data |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/threads/staging/run-ADVI_SNPLBK-001-snapshot-lookback-diagnosis.sh` | Thread staging script | No |
| `org/threads/ADVI_SNPLBK-001-snapshot-lookback-regression-diagnosis/` | Thread folder (auto-generated) | No |
| `org/projects/ADVI_SNPLBK.json` | Phase updated, thread status complete | No |
| `org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/ADVI_SNPLBK.001.snapshot-lookback-frontend-fix.md` | DE task order | No |
| `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/task_orders/ADVI_SNPLBK.001.snapshot-strip-visual-fix.md` | RD task order | No |
| This file | Session log | No |

---

## Blockers

None. All artifacts produced. Waiting on DE to perform runtime diagnosis.

---

## Current State

**Status:** COMPLETE
**Active branch:** CLOUD

Thread ADVI_SNPLBK-001 completed with DE + RD convergence. COO verified the S3 backend
data is intact (all quarterly period keys present). Two task orders issued: DE to diagnose
and fix the frontend root cause, RD to support with strip component changes if needed.
The primary hypothesis is a granularity mismatch where the Distribution tab's strip is
hardcoded to q1/q2/q3 keys but doesn't adapt when the user toggles to monthly/annual.

---

## Next Steps

1. **[0.4.0_DE_ClientPlatform] Runtime diagnosis** -- use browser DevTools to inspect the
   actual `analyticsData` object at runtime and confirm which file is being fetched and
   whether period keys are present in the parsed response
2. **[0.4.0_DE_ClientPlatform] Fix** -- implement the frontend fix based on root cause
3. **[0.4.2_RD_AdvisorIntelligence] Strip component update** -- after DE confirms root
   cause, update strip to handle all granularity period keys if needed
4. **[0.4.0_DT_ClientPlatform] Push** -- DT pushes the fix to portal DEV after QA

**Do NOT:**
- Modify Script 09 or any backend gold scripts (data is correct)
- Modify bd-portal-publisher Lambda (partner_analytics correctly disabled)

---

## Commits

### Commit: `org(2.0.0_SA_COO): ADVI_SNPLBK -- thread orchestration, diagnosis, task orders`

| File | Description |
|------|-------------|
| `org/projects/ADVI_SNPLBK.json` | Project registration |
| `org/threads/staging/run-ADVI_SNPLBK-001-snapshot-lookback-diagnosis.sh` | Thread staging script |
| `org/threads/ADVI_SNPLBK-001-snapshot-lookback-regression-diagnosis/` | Thread folder (7 messages, context, THREAD.json, TURN.json) |
| `org/tier1_exec/2.0.0_SA_COO/logs/2026-03-10/advi_snplbk_thread_and_task_orders.md` | This session log |
| `org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/ADVI_SNPLBK.001.snapshot-lookback-frontend-fix.md` | DE task order: diagnose + fix granularity mismatch in DistributionTab |
| `org/tier2_senior/0.4.0_DE_ClientPlatform/threads/ADVI_SNPLBK-001-..._0.4.2_RD_AdvisorIntelligence.md` | DE thread receipt |
| `org/tier2_senior/0.4.0_DE_ClientPlatform/logs/2026-03-10/advi_snplbk_001_snapshot_lookback_fix.md` | DE session log from task order execution |
