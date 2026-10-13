# Deploy Completion Record
**Date opened:** 2026-10-13T20:28:12.085369+00:00
**Status:** OPEN
**Deploy:** ADVI_FIRMBKTS TO-FB-j-15 (round 7, DEC-12): add a third WriteOnly basic event_selector (S3 objects on opal-data-bd, opal-data-inf, opal-data-cot) to aws_cloudtrail.organization (opal-organization-trail, us-east-1); prior selectors saved at org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FBL/TRAIL_SELECTORS_BEFORE.json (management All + ReadOnly on 49financial/bd/cot/inf); rollback = remove the third selector block and safe-apply, or aws cloudtrail put-event-selectors with the saved prior document; cost: write data events are billed (Andrew ruled DEC-12 YES on that basis); trail only, no bucket/KMS/policy touched
**Authored by:** 0.7.0_AE_CloudOps~FBL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | safe-apply plan -target=aws_cloudtrail.organization in shared-infra: 0 to add, 1 to change, 0 to destroy, the one change the third selector | the plan summary line and the selector diff |  | OPEN |
| L2 | activation | safe-apply apply on the saved plan; apply UTC printed | the apply result line and the UTC time |  | OPEN |
| L3 | verify | get-event-selectors read back saved as TRAIL_SELECTORS_AFTER.json (3 selectors, write on exactly bd/inf/cot), trail IsLogging true, AC1 TRAILSEL OK | the AC1 output line and IsLogging |  | OPEN |
| L4 | git | tf change plus instance, ledger close and status flip committed via safe-commit | commit hash |  | OPEN |

## Log

- 20261013T202812Z OPENED by 0.7.0_AE_CloudOps~FBL with 4 leg(s)
