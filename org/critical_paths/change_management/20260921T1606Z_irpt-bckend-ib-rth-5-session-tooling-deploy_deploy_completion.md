# Deploy Completion Record
**Date opened:** 2026-09-21T16:06:02.529296+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-rth-5 arm (e): deploy session-establishment tooling to export render host (both never-widen halves SIGNED at blob b5fd42fbb54acb53652aacf7caa495b570ce648f)
**Authored by:** 0.9.0_WK_IRPT_BCKEND~5
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/ec2/investor-reporting-export/ (render_export.cjs, capture-session.cjs, capture-session.sh, package.json -- git-blob bytes, run-export-render.sh unchanged/skipped) | head-object per file matching packet section 2 sha256 table |  | OPEN |
| L2 | ec2-baked-asset | /opt/investor-reporting-export/ on i-0167fd745ad906a66 | SSM cat + sha256 of the RUNNING path matching the same table |  | OPEN |
| L3 | verify | synthetic-storageState proof against deployed bytes on the host | SSM-invoked run showing the new session-loaded log line + still-refuses SESSION_ABSENT on the fake session |  | OPEN |

## Log

- 20260921T160602Z OPENED by 0.9.0_WK_IRPT_BCKEND~5 with 3 leg(s)
