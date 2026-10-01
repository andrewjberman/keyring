# Deploy Completion Record
**Date opened:** 2026-10-01T12:25:51.668359+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP round 59 AMGT-ai-2 (DEMO-BLOCKING, land before 22:00Z): the code-only redeploy of the price identity join -- one artifact upload, one code-only safe-apply on opal-amgt-scoped-api. Never-widen pair COO e52b6d1bb5 / CTO 45e3aefae0; build commit e52b6d1bb5; base CodeSha256 g9H0TW2garLGS0zMoLmJgFQU8a/6ZJUGMwJaYFSkc/c= re-read LIVE and unmoved; rollback artifact VersionId hj5ITKr5Ct9Mn3ySEvztrK9eG.bnsHho
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | build + upload ONE artifact to s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip | CONTENT-DIFF graded both directions: EXACTLY files 350, IDENTICAL 349, CHANGED 1 (lib/research/api/scoped_amgt.py), ADDED 0, REMOVED 0, zero files outside the list, and the 2 peer-drifted lib/opal_data_harvest files MEASURED not-packaged; prior and new S3 VersionId |  | OPEN |
| L2 | activation | ONE code-only safe-apply on infra/aws/terraform/harvest, planned from a tree at CLOUD HEAD and applied from the SAVED plan | the plan read before applying: only the function source hash changes, resource count stated, NO destroy / IAM / route / gateway / alias; prior and new CodeSha256 + LastModified read back live |  | OPEN |
| L3 | verify | AC1 (ai_price_identity.py --where deployed) PLUS the CTO half's condition-3 reads, which the criterion does not print | C0 PASS; C1-C6 PASS for BOTH the TRENDING and BREAKOUT price axes (0 rows without security_key, 0 without display_name, 0 raw-key labels, every key covered, score_pct kept); EVERY PRICE BAR OPENS AND NAMES A COVERED SECURITY: YES; exit=0. AND, read off the deployed body per axis: the unkeyed count (62 -> 0), the display_name count (94 of 94) and the company-name count; AND a 200 on /security/AMD_US_Equity/overlay and /security/TSM_US_Equity/overlay, which is what 'the bar opens' means |  | OPEN |
| L4 | verify | AC2 (ag_1_served.py --what post) as the regression guard on round 57's outcomes | C0 PASS; FWD-32, FWD-33 and FWD-34 still YES on the deployed function; THE DEPLOYED FUNCTION SERVES THE FRIDAY FEED: YES; exit=0 |  | OPEN |

## Log

- 20261001T122551Z OPENED by 0.7.0_AE_CloudOps~A with 4 leg(s)
