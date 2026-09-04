# Deploy Completion Record
**Date opened:** 2026-09-04T02:21:56.923380+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260904T031015Z
**Deploy:** NFRA_OPSEC202609 TO-OP-S-14-21 deliverables 1-5: deploy opal-sentinel ARMED WATCH-ONLY -- function, both WAF subscription filters, and the daily digest FILE schedule. Deployed AFTER the TO-OP-S-22 verdict (02:05Z), which is what S1421-AC5 grades.
**Authored by:** 0.7.0_AE_CloudOps~S
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | artifact opsec/opal-sentinel.zip on opal-313476888478-lambda-artifacts | head-object ContentLength + VersionId + content-sha256 metadata | head-object opsec/opal-sentinel.zip: ContentLength 7751, VersionId g0j9S_J726oEkZfZUCyJ09ycq2nweh8f, metadata content-sha256=xaAT7vYieuJJWEwqV8SZaljjXYZHtUgNtjI5/aiVL9k=. The module reads that metadata key for source_code_hash. | CLOSED 20260904T031014Z |
| L2 | git | CLOUD commit of the function source and sentinel.tf | commit hash | commits c027eb4f6f (role), 94d15e76ac (function + sentinel.tf + this ledger), 7a4cc2c348 (the three fixture-found defects). Push state MEASURED: LOCAL -- GATE 5, push is the integrator's. | CLOSED 20260904T031014Z |
| L3 | activation | terraform apply on the opsec root -- 9 to add, 0 change, 0 destroy | apply output | Four applies, each safe-apply with the routine HALT_ACK: 9 added (function, 2 subscription filters, 3 permissions, digest rule+target, log group), then three in-place function updates carrying the defect fixes. Final: Apply complete, 0 added 1 changed 0 destroyed. One apply between them was REFUSED by the tag-authz gate failing closed on a shared-root break owned by TO-OP-S-15-19 -- nothing half-landed, reported as msg 20139. | CLOSED 20260904T031014Z |
| L4 | verify | UNSCOPED re-plan 0-diff on the opsec root | terraform plan -detailed-exitcode rc | terraform plan -detailed-exitcode UNSCOPED on the opsec root after the final apply: rc=0, 'No changes. Your infrastructure matches the configuration.' | CLOSED 20260904T031014Z |
| L5 | verify | APPLIED-plane read: reserved concurrency 1 (C-7), both subscription filters present, digest rule armed | aws lambda/logs/events output | APPLIED plane. C-7 reserved concurrency: get-function-concurrency returns ReservedConcurrentExecutions=1, corroborated by get-function's Concurrency block -- NOT from get-function-configuration, whose response shape omits the field and returns null for every function (a wrong-instrument null that reads as a failure). Subscription filters: opal-sentinel-cloudfront on aws-waf-logs-opal-cloudfront and opal-sentinel-gateway on aws-waf-logs-opal-gateway, both destined to the function ARN; 0 existed before, so these are the whole input. Digest rule opal-sentinel-daily-digest ENABLED, cron(0 6 * * ? *). Deployed CodeSha256 xaAT7vYieuJJWEwqV8SZaljjXYZHtUgNtjI5/aiVL9k= equals the BUILD INPUT hash. | CLOSED 20260904T031015Z |
| L6 | verify | S14-AC1/AC2/AC3 fixture exercise and its cleanup read back | invocation result plus a BLOCK census with its denominator | S14-AC1 end to end on a fixture AND on real traffic: parsed event -> counter increment -> ALLOW check -> WATCH row -> case file with the coverage bound, each read back. S14-AC3 BOTH ARMS: allowed 203.0.113.9/32 driven with a 5-record burst -> watch_rows 0, allowed_skipped 1, status still ALLOW; not-allowed 203.0.113.7/32 same burst -> watch_rows 1 plus a case file. PRD 7.3 step 5 append-to-open-case verified by discrimination: a second burst grew case_ids by 0 and wrote a new sample SHARD into the reused case. S14-AC2: BLOCK/BLOCKED 0 of 2 rows. CLEANUP READ BACK: fixture rows NONE, fixture case objects NONE; the 2 remaining rows and 9 case objects are REAL addresses caught by the live filters and are deliberately retained. | CLOSED 20260904T031015Z |

## Log

- 20260904T022156Z OPENED by 0.7.0_AE_CloudOps~S with 6 leg(s)
- 20260904T031014Z LEG L1 closed: head-object opsec/opal-sentinel.zip: ContentLength 7751, VersionId g0j9S_J726oEkZfZUCyJ09ycq2nweh8f, metadata content-sh
- 20260904T031014Z LEG L2 closed: commits c027eb4f6f (role), 94d15e76ac (function + sentinel.tf + this ledger), 7a4cc2c348 (the three fixture-found defect
- 20260904T031014Z LEG L3 closed: Four applies, each safe-apply with the routine HALT_ACK: 9 added (function, 2 subscription filters, 3 permissions, diges
- 20260904T031014Z LEG L4 closed: terraform plan -detailed-exitcode UNSCOPED on the opsec root after the final apply: rc=0, 'No changes. Your infrastructu
- 20260904T031015Z LEG L5 closed: APPLIED plane. C-7 reserved concurrency: get-function-concurrency returns ReservedConcurrentExecutions=1, corroborated b
- 20260904T031015Z LEG L6 closed: S14-AC1 end to end on a fixture AND on real traffic: parsed event -> counter increment -> ALLOW check -> WATCH row -> ca
- 20260904T031015Z CLOSED -- all 6 legs proven
