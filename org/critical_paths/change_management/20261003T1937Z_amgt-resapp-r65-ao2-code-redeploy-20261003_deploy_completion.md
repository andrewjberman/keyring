# Deploy Completion Record
**Date opened:** 2026-10-03T19:37:34.462915+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP round 65 AMGT-ao-2: one code-only redeploy of opal-amgt-scoped-api at pin 19cb3df089 (carries ao-1 title case + the ft quarantine-mechanism deletion); memory stays 1769
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | opal-313476888478-lambda-artifacts research/opal-amgt-scoped-api.zip | new VersionId + byte count + content-sha256 metadata of the uploaded object |  | OPEN |
| L2 | activation | opal-amgt-scoped-api code-only safe-apply at pin 19cb3df089 | new CodeSha256 off KQSA62c3 + MemorySize still 1769 + 0-diff replan |  | OPEN |
| L3 | verify | AC1 c17 deployed and AC2 c12 deployed plus regressions c9 c10 c11 c13 c14 | each check verdict line with exit=0; rollback VersionId .xFOZLD1X0znp_5COtZvp3UgWTBrw19p if any fails |  | OPEN |

## Log

- 20261003T193734Z OPENED by 0.7.0_AE_CloudOps~A with 3 leg(s)
