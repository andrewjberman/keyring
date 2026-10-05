# Deploy Completion Record
**Date opened:** 2026-10-05T02:01:06.154988+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP round 68 AMGT-ar-3: ONE code-only redeploy of opal-amgt-scoped-api at build commit 7158bc9d4d, carrying ar-1 (FWD-39 cloud repair) and ar-2 (plain reason words). memory_size stays 1769. No IAM, no new S3 read path. Base 2rFeF57lMh8MkU6WRgZyImZt7RMlW14BdxmUjIBvSSQ= / VersionId O1WGPxfTK9vszvvZqzzuOfjQAGMOIZiM (AMGT_CORPUS al-5's build); rollback is that VersionId through one code-only safe-apply
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 5.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | opal-313476888478-lambda-artifacts research/opal-amgt-scoped-api.zip | new VersionId + byte count + content-sha256 read back by the uploader and independently by head-object; CONTENT-DIFF against the DEPLOYED build exactly files 356 IDENTICAL 354 CHANGED 2 ADDED 0 REMOVED 0, the two being lib/research/api/scoped_amgt.py and lib/research/coverage/covered_no_block.py; size printed and under 262144000 B; plus MY OWN read-path scan over the diff per CTO round-67 ruling 4 (the halves declare NONE; a path that appears owes a simulate arm reading allowed BEFORE the code leg, and no grant rides this act) |  | OPEN |
| L2 | activation | opal-amgt-scoped-api code-only safe-apply at pin 7158bc9d4d | new CodeSha256 off 2rFeF57l + MemorySize still 1769, proven from a FULL show -json plan: exactly 1 non-no-op (the lambda, update), 0 destroy/create/replace, 0 non-no-op IAM, 0 non-no-op route/gateway; then a full 0-diff replan and the deployed sha re-read live |  | OPEN |
| L3 | verify | AC1 r68 c27 (233 names / 199 serving), AC2 r68 c28, AC3 r67 c23+c25+c26, all on deployed; plus the reported set r67 c24, r64 c9/c10(30-day)/c11-c14, r65 c17, r66 c18/c19/c22, and r64 c15 cold on the day route | each verdict line with exit=0; rollback to VersionId O1WGPxfTK9vszvvZqzzuOfjQAGMOIZiM if c27 or c28 is not YES, any other check moves, c15 exceeds 5 s, a covered key returns non-200, or the ZZZZ_US_Equity control answers anything but 404 |  | OPEN |

## Log

- 20261005T020106Z OPENED by 0.7.0_AE_CloudOps~A with 3 leg(s)
