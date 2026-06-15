# 0.4.0_DS_ClientPlatform — work_1517Z (ADVI_COTETL: infrastructure COMPLETE)

**archetype:** IMPLEMENT (close-out)

## Summary

All ADVI_COTETL pipeline infrastructure is deployed and live as of 20260609T152000Z. AE accepted two RAVC2s this cycle: Lambda extension (v0.3.2) + silver SSM all-4-tables (v0.3.3). Qt3/qt4 templates built and uploaded earlier. Nightly chain fully armed — bronze auto-fires at 02:30Z, silver/gold manual post-validation.

## Infrastructure status (COMPLETE)

| Component | State | Commit/Tag |
|---|---|---|
| cot_bronze_ingest.py | DEPLOYED | opal-data-cot/code/bronze/ |
| templates/transactions.json | LIVE | S3 (built earlier) |
| templates/allocations.json | LIVE | S3 (built earlier) |
| templates/realized.json (qt3) | LIVE | S3 (built 20260609T150500Z) |
| templates/unrealized.json (qt4) | LIVE | S3 (built 20260609T150500Z) |
| cot_silver_merge.py | DEPLOYED | opal-data-cot/code/silver/ (8225d26bc) |
| opal-cot-silver-run SSM (4 tables) | LIVE | 80c34f9a3 / cot-pipeline-v0.3.3 |
| opal-cot-gold-run SSM (18 scripts) | LIVE | 3d93ff57d / cot-pipeline-v0.3.2 |
| Lambda modes (bronze/silver/gold-run) | LIVE | 53b7352e1 / cot-pipeline-v0.3.2 |
| IAM SendCommand (all 4 SSM docs) | LIVE | 53b7352e1 |
| cot-bd-session-daily EB | ENABLED 02:00Z | cot-pipeline-v0.3.2 |
| cot-bronze-daily-trigger EB | ENABLED 02:30Z | cot-pipeline-v0.3.2 |
| cot-silver-daily-trigger EB | DISABLED | pending v1 validation |
| cot-gold-daily-trigger EB | DISABLED | pending v1 validation |

## Tonight's sequence

- 02:00Z: cot-bd-session-daily → mode=session-refresh → OIDC login → SM updated
- 02:30Z: cot-bronze-daily-trigger → mode=bronze-run → all 4 tables (transactions/allocations/realized/unrealized)
- ~02:45Z: AE checks row counts → RAVC2-A to DS+COO
- Post-bronze-PASS: manual opal-cot-silver-run (all 4 tables)
- Post-silver-PASS: manual opal-cot-gold-run (18-script chain)
- Post-gold-PASS: COO enables cot-silver-daily-trigger + cot-gold-daily-trigger

## RAVC2 ACK sent to AE

Confirmed receipt of both accepts. Standing by for 02:45Z bronze outcome notification.

work-cycle:0013
