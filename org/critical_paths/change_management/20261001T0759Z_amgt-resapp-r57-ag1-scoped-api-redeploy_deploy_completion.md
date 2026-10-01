# Deploy Completion Record
**Date opened:** 2026-10-01T07:59:08.173084+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP round 57 AMGT-ag-1: the ONE scoped-API redeploy that serves the Friday feed (FWD-32/33/34) -- item 0 CLOSURE_ROOTS, one artifact upload, one code-only safe-apply on opal-amgt-scoped-api. Never-widen pair COO 824a1fc3da / CTO dfe8802c2b; build commit 957a020416 (parent ef6c65c219 contains the ag-2 drain cb5f25b9de); base CodeSha256 /QP4upEVzTjnHV2bAeIXIud0k0DgjDDGrlMgtm0uo7o= re-read LIVE and unmoved; rollback artifact VersionId C9brZ5Qd6_.iSbxw3NKZOxHuDByQScll
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | item 0: CLOSURE_ROOTS gains lib.trading_calendar in build-and-upload-scoped-amgt.sh | the commit hash, the exact resulting line, bash -n OK, and the parent containing cb5f25b9de |  | OPEN |
| L2 | activation | build + upload ONE artifact to s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip at the build commit | --build-only rc=0 with lib/trading_calendar.py + lib/research/api/monthly_chatter.py + lib/research/coverage/covered_universe.py present in the zip; CONTENT-DIFF graded file-by-file against the COO half's list (expect files 350, IDENTICAL 336, CHANGED 8, ADDED 6, REMOVED 0) with ZERO files outside the list; prior and new S3 VersionId |  | OPEN |
| L3 | activation | ONE code-only safe-apply on infra/aws/terraform/harvest, planned from a tree at CLOUD HEAD | the plan printed and read before applying: only the function source hash changes, resource count stated, and NO destroy / IAM / route / gateway / alias change; prior and new CodeSha256 + LastModified read back live |  | OPEN |
| L4 | verify | AC1, the TO's literal invocation (ag_1_served.py --what post) | C0 PASS with CodeSha256 and LastModified moved off the printed pre values; FWD-32, FWD-33, FWD-34 each YES on the deployed function; THE DEPLOYED FUNCTION SERVES THE FRIDAY FEED: YES; exit=0 |  | OPEN |
| L5 | verify | AC2, the TO's literal invocation (ag_1_served.py --what text) -- GRADED because the GO states ag-2 rides | C0 PASS; C1, C2, C3 PASS on the deployed function; THE DEPLOYED FUNCTION SERVES EVERY REASON IN PLAIN WORDS: YES; exit=0 |  | OPEN |

## Log

- 20261001T075908Z OPENED by 0.7.0_AE_CloudOps~A with 5 leg(s)
