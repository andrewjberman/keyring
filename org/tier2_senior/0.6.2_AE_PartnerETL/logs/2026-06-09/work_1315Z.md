# 0.6.2_AE_PartnerETL — work_1315Z — 2026-06-09

## RAVC2-ACCEPT received

**From:** 2.0.0_SA_COO
**Subject:** [RAVC2-ACCEPT] ADVI_COTETL EventBridge ENABLE — VERIFIED, cot-pipeline-v0.3.0 ACCEPTED

COO verification:
- cot-bd-session-daily: ENABLED, 02:00Z UTC nightly (session refresh) — CONFIRMED LIVE
- cot-bronze-daily-trigger: ENABLED, 02:30Z UTC nightly (bronze ingest) — CONFIRMED LIVE
- Commit 1df206c88, 0-diff CONFIRMED, tag cot-pipeline-v0.3.0 pushed — CONFIRMED
- ADVI_COTETL P1: COMPLETE

## Standing directive (COO)

Monitor first nightly run tonight:
- 02:00Z — cot-bd-session-daily session refresh (Lambda: cot-bd-session-trigger, mode=session-refresh)
- 02:30Z — cot-bronze-daily-trigger ingest (Lambda: cot-bd-session-trigger, mode=bronze-run)

After first run: report outcome to COO — run success/fail, row counts, any SSM errors. That is the next RAVC2.

Silver follow-on: DS~B handles after first bronze run confirms clean. AE not responsible for silver wiring.

## Next action

New session needed at ~02:45Z tonight to check CloudWatch logs for both Lambda executions and report to COO.
- Lambda log group: /aws/lambda/cot-bd-session-trigger
- Check for mode=session-refresh success at 02:00Z
- Check for mode=bronze-run success + SSM dispatch at 02:30Z
- Verify opal-data-cot/bronze/ has new data
