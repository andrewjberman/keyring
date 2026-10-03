# Deploy Completion Record
**Date opened:** 2026-10-03T23:38:17.006863+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP round 66 AMGT-ap-4: one code-only redeploy of opal-amgt-scoped-api at pin b642e313f9 (carries c20fd8cc98 tone_reason, ap-1 FWD-39 word cloud, ap-2 FWD-36 price 90/365); memory stays 1769
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | opal-313476888478-lambda-artifacts research/opal-amgt-scoped-api.zip | new VersionId + byte count + content-sha256 read back by the uploader |  | OPEN |
| L2 | activation | opal-amgt-scoped-api code-only safe-apply at pin b642e313f9 | new CodeSha256 off lPTMo20T + MemorySize still 1769 + 0-diff replan, proven from the plan JSON |  | OPEN |
| L3 | verify | AC1 c19 AC2 c18 AC3 c22 on deployed, plus regressions c9 c10(30-day) c11-c14 c17, c15 cold on the day route, and the ADDED range-route cold read | each verdict line with exit=0; rollback VersionId 5xO0vR9UWlx.XI59G0KNLJyAsjMKOes4 if a graded criterion fails or c15 exceeds 5 s |  | OPEN |

## Log

- 20261003T233817Z OPENED by 0.7.0_AE_CloudOps~A with 3 leg(s)
