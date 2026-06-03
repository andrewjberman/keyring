# 0.7.0_AE_CloudOps — Session 2026-06-03 ~1424Z

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, COORDINATE

## Context
Andrew-direct keep-warm thread + COO redirect to MDPF_SCOPED.OPS1 closure verify. Two parallel threads this tick.

## Keep-warm (Andrew-direct, follow-on to brief 91df57398)
- Andrew probed the deeper symptom: deep ADVI drilldown -> pause ~10min -> click -> "no data".
- Root-caused on FE: global QueryClient (main.tsx:37-60) is correct (smart cold-start retry + session cache), but L3/L4 PII drilldown queries override with gcTime:0 + retry:false. gcTime:0 = legit PII eviction; retry:false serves NO PII purpose and defeats both global smart-retry AND opal-partners-data's 503-for-retry contract -> cold-Lambda 503 on deep click = false-empty.
- Wrote RD-actionable companion brief: docs/briefs/advi-books-publicprofile-coldstart-false-empty-fe-brief-20260603.md (b5af4ccc2). Two-layer fix: FIX1 (drop retry:false, keep gcTime:0) + FIX2 (warm-ping).
- CTO disposition: FIX1 ships standalone (no gate); FIX2 backend ?warm=1 stays held for keep-warm PRD/Andrew GO.
- RD shipped FIX1 same hour (portal DEV 21be552d, VALGATE PASS). I RAVC-validated the diff: 4x retry:false removed on AdvisorBookView.tsx :186/:202/:212/:234 + AdvisorPublicProfile.tsx:294, gcTime:0 retained, exec-summary:303 left as-is, regression-guard comment citing brief. PASS.
- My backend ?warm=1 branch: HELD (no deploy) pending Andrew GO. Will send RD the endpoint contract when it lands.

## MDPF_SCOPED.OPS1 (COO redirect)
State-check first (no rework). Gate status:
- AC1 fresh data: SAT (6/2 run complete, freshness-stale alarm OK).
- AC2 timer fix: SAT (enforcer-v1.0.5 exclusion; 6/2 reached all-5-complete = no mid-run kill).
- AC3 staleness alarm: SAT (mdpf-daily-freshness-stale deployed mdpf-pipeline-v1.1.0, OK).
- AC4 >=2 consecutive scheduled clean: RUN#1 (6/2 15:00Z) CLEAN — scheduled StartInstances by mdpf-daily-trigger, all 5 stages 15:12:44Z, NO external StopInstances API (clean self-stop vs 6/1 enforcer-kill signature). RUN#2 = today 15:00Z = TIME-GATE.
- AC5 eclipse: SAT (characterized + accepted 6/2).
- AC6 RAVC2: staged; send on run#2 verify.
- COO ACK'd plan. /work cron (20m) catches run#2 after ~15:13Z completion -> verify -> AC6 RAVC2 to COO+CTO. If stall: RCA + BLOCKED-ASK.

## Compiler Tools
None this tick — verification was AWS-live (ec2 describe, cloudtrail lookup-events, cloudwatch describe-alarms, s3 ls) + portal submodule git diff validation + FE source trace. No gold/silver edit or portal-component author by me (RD authored FIX1), so no comp-* row matched. comp-iam/comp-routes will apply when the keep-warm backend ?warm=1 TO is authored on GO.
