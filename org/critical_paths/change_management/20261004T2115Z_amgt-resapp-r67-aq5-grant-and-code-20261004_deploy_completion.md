# Deploy Completion Record
**Date opened:** 2026-10-04T21:15:42.374543+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP round 67 AMGT-aq-5: TWO legs under ONE entry -- (1) grant leg, ONE s3:GetObject statement ReadTheScannerSp500UniverseForCoveredNoBlock on the scanner sp500 universe object, targeted safe-apply on opal-amgt-scoped-api-grants; (2) code leg, build+upload ONE artifact at pin d8bafe6896 and ONE code-only safe-apply. memory stays 1769. Rollback: role policy at d8bafe6896; artifact VersionId Pj6GLEdKjRnDFwBjZzOSR2gYAsQPHilG / CodeSha256 FcVBPafwzuPI0RMFjOJJfYN/KeZe3YYns9uqTSOlalU=
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | opal-amgt-scoped-api-grants targeted safe-apply (grant leg, FIRST) | plan from show -json: ONE non-no-op resource (aws_iam_role_policy.scoped_amgt_api_grants, update) and nothing else; then simulate-principal-policy on opal-amgt-scoped-api-role for s3:GetObject on the one scanner key reads allowed (ONE --resource-arns, with an isolated positive control); 0-diff replan |  | OPEN |
| L2 | s3-prefix | opal-313476888478-lambda-artifacts research/opal-amgt-scoped-api.zip | new VersionId + byte count + content-sha256 read back by the uploader and independently by head-object; CONTENT-DIFF exactly files 356 IDENTICAL 350 CHANGED 5 ADDED 1 REMOVED 0 against FcVBPafw; size under 262144000 B and printed |  | OPEN |
| L3 | activation | opal-amgt-scoped-api code-only safe-apply at pin d8bafe6896 | new CodeSha256 off FcVBPafw + MemorySize still 1769 + no destroy/IAM/route/gateway change, proven from show -json; 0-diff replan |  | OPEN |
| L4 | verify | AC1 r67 c23, AC2 r67 c24, AC3 r67 c25+c26 on deployed, plus regressions r64 c9-c14, r65 c17, r66 c18/c19/c22, r64 c15 cold on the day route, and the RANGE route cold read | each verdict line with exit=0; c24 expects mismatches 0, old-reason 0, no-table-row 21 per window against a local read run beside it; rollback to VersionId Pj6GLEdKjRnDFwBjZzOSR2gYAsQPHilG if a graded criterion fails or any key 502s |  | OPEN |

## Log

- 20261004T211542Z OPENED by 0.7.0_AE_CloudOps~A with 4 leg(s)
