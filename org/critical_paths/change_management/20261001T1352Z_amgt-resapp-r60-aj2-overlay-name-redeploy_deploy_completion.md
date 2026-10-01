# Deploy Completion Record
**Date opened:** 2026-10-01T13:52:15.392622+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP round 60 AMGT-aj-2 (land before 22:00Z): the code-only redeploy of the overlay name (every bar opens onto its own name) -- one artifact upload, one code-only safe-apply on opal-amgt-scoped-api. Never-widen pair COO 9b4bf29d32 / CTO bc193c28b4; build commit 9b4bf29d32; base CodeSha256 E6PdHVFB9z1xUcvCRtNIALjgAaCzNtolAdzaKmCssvM= re-read LIVE and unmoved; rollback artifact VersionId q0Vf.FzuGpVovbH.xb2dumggs4k5kMKB
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | build + upload ONE artifact to s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip | CONTENT-DIFF graded both directions: EXACTLY files 350, IDENTICAL 349, CHANGED 1 (lib/research/api/scoped_amgt.py), ADDED 0, REMOVED 0, zero files outside the list, with a fabricated-path control; prior and new S3 VersionId |  | OPEN |
| L2 | activation | ONE code-only safe-apply on infra/aws/terraform/harvest, planned from a tree at CLOUD HEAD and applied from the SAVED plan | the plan read before applying: only the function source hash changes, resource count stated, NO destroy / IAM / route / gateway / alias; prior and new CodeSha256 + LastModified read back live |  | OPEN |
| L3 | verify | AC1 (aj_overlay_name.py --where deployed) -- the CTO's condition 3 is now INSIDE the criterion: it compares the overlay display_name to the row's for all 94 and checks identity_status, explicitly NOT the HTTP status | C0 PASS; C1-C4 PASS on the deployed function (every ranked row's overlay display_name equals the row's, 94 at the cut; AMD and TSM overlays carry the company name; the identity block unchanged with AMD/TSM MEASURED); EVERY BAR OPENS ONTO ITS OWN NAME: YES; exit=0; plus AMD's and TSM's overlay name read off the deployed body and the base CodeSha256 printed beside it |  | OPEN |
| L4 | verify | AC2 (ag_1_served.py --what post) as the regression guard on round 57's outcomes | C0 PASS; FWD-32, FWD-33 and FWD-34 still YES on the deployed function; THE DEPLOYED FUNCTION SERVES THE FRIDAY FEED: YES; exit=0 |  | OPEN |

## Log

- 20261001T135215Z OPENED by 0.7.0_AE_CloudOps~A with 4 leg(s)
