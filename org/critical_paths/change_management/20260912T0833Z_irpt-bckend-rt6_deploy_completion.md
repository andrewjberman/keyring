# Deploy Completion Record
**Date opened:** 2026-09-12T08:33:41.578962+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-rt-6: the DRIVEN PRODUCTION FIRE of irpt-directory-refresh for business date 2026-09-11 (three firms)
**Authored by:** 0.9.0_WK_IRPT_BCKEND~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | invoke the deployed irpt-directory-refresh with business_date 2026-09-11 | StatusCode 200 and the three per-firm envelopes |  | OPEN |
| L2 | s3-prefix | the three firm buckets investor-reporting/directory/_refresh/2026-09-11/manifest.json | head-object on each, with the denominator |  | OPEN |
| L3 | verify | each manifest reads build_dispatch SSM with a real command id, and each command id resolves through ssm get-command-invocation | the three command ids and their statuses |  | OPEN |

## Log

- 20260912T083341Z OPENED by 0.9.0_WK_IRPT_BCKEND~2 with 3 leg(s)
