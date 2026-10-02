# Deploy Completion Record
**Date opened:** 2026-10-02T07:24:26.432266+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP round 61 AMGT-ak-2 (land before 11:13Z if it can): the code-only redeploy of the company name (every price bar and bubble carries a company name) -- one artifact upload FROM A WORKTREE AT 63e78fe4f7 (not CLOUD HEAD: HARVST drain fdd7442696 moved transport.py and load_window_grade.py after it), one code-only safe-apply on opal-amgt-scoped-api. Never-widen pair COO f234d5aa12 / CTO 02d032ee67; build commit 63e78fe4f7; base CodeSha256 UnSqZgCDkSxM3J3roY8d+iVGZp+8JB1XnM/phfZrmeo= re-read LIVE 072330Z and unmoved; rollback artifact VersionId 1DFcRU3xDzUsi84yZnWv985DDF1MymMn
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | build + upload ONE artifact to s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip from a worktree at 63e78fe4f7 | CONTENT-DIFF graded both directions: EXACTLY CHANGED 3 and the set equal to [lib/research/api/scoped_amgt.py, lib/research/api/monthly_chatter.py, org/standards/NAMING_SCHEMA.json], ADDED 0, REMOVED 0, zero files outside the list, packaged denominator printed, fabricated-path control; prior and new S3 VersionId read back from S3 |  | OPEN |
| L2 | activation | ONE code-only safe-apply on infra/aws/terraform/harvest, applied from the SAVED plan | the plan read BEFORE applying: only the function source hash changes, resource count stated, NO destroy / IAM / route / gateway / alias; prior and new CodeSha256 + LastModified read back from LIVE state, not from the apply rc |  | OPEN |
| L3 | verify | AC1 b1_names.py --where deployed at the TO literal invocation | C0 PASS; C1-C4 PASS on the deployed function (0 of 94 rows unnamed on TRENDING/PRICE and BREAKOUT/PRICE; RMS_FP_Equity named; 0 of 95 chatter rows by ticker; the RMS overlay serves the row name); EVERY PRICE BAR AND BUBBLE CARRIES A COMPANY NAME: YES; exit=0; plus the previously-unnamed keys display_name and name_source printed beside their pre-act ticker values with one positive control (CTO condition 2) |  | OPEN |
| L4 | verify | AC2 round-60 aj_overlay_name.py --where deployed as the regression guard | C0-C4 PASS on the deployed function (every ranked row overlay display_name equals the row own; AMD and TSM named; the identity block unchanged); EVERY BAR OPENS ONTO ITS OWN NAME: YES; exit=0 |  | OPEN |

## Log

- 20261002T072426Z OPENED by 0.7.0_AE_CloudOps~A with 4 leg(s)
