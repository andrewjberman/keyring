# Deploy Completion Record
**Date opened:** 2026-09-21T16:06:02.529296+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260921T161523Z
**Deploy:** IRPT_BCKEND IB-rth-5 arm (e): deploy session-establishment tooling to export render host (both never-widen halves SIGNED at blob b5fd42fbb54acb53652aacf7caa495b570ce648f)
**Authored by:** 0.9.0_WK_IRPT_BCKEND~5
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/ec2/investor-reporting-export/ (render_export.cjs, capture-session.cjs, capture-session.sh, package.json -- git-blob bytes, run-export-render.sh unchanged/skipped) | head-object per file matching packet section 2 sha256 table | head-object+get-object on all 5 keys under s3://opal-313476888478-lambda-artifacts/ec2/investor-reporting-export/ this session: sizes 12929/5544/1724/1109/1330 bytes; sha256(fetched bytes) render_export.cjs=fe2af007f3.. capture-session.cjs=edf76b2dc1.. capture-session.sh=21555558be.. package.json=2016e7b88a.. run-export-render.sh=e52661229c.. -- ALL 5 match packet section 2's COMMITTED-FILE-SHA256 table exactly (git-blob bytes, extracted via 'git show HEAD:<path>', never a raw disk copy). | CLOSED 20260921T161428Z |
| L2 | ec2-baked-asset | /opt/investor-reporting-export/ on i-0167fd745ad906a66 | SSM cat + sha256 of the RUNNING path matching the same table | ssm:5ab3ab4f-3268-4a9f-bd91-4d1ae8f7334e -- SSM AWS-RunShellScript sha256sum of the RUNNING path /opt/investor-reporting-export/ on i-0167fd745ad906a66 (this session, after the render document's own S3 sync ran): render_export.cjs=fe2af007f3.. capture-session.cjs=edf76b2dc1.. capture-session.sh=21555558be.. package.json=2016e7b88a.. run-export-render.sh=e52661229c.. -- ALL 5 match packet section 2's table exactly; this is the stronger read-back (proves the INSTANCE ROLE actually fetched the bytes), not just an S3-side head-object. | CLOSED 20260921T161449Z |
| L3 | verify | synthetic-storageState proof against deployed bytes on the host | SSM-invoked run showing the new session-loaded log line + still-refuses SESSION_ABSENT on the fake session | ssm:91bcd165-9ca0-4fda-9d9f-5b3bbc234482 -- synthetic storageState.json (352 bytes, clearly-fake cookie IB_RTH5_ARM_E_SYNTHETIC_FAKE_SESSION_DO_NOT_TRUST, written via ssm:e54f5123-3028-477e-893d-8fd70acc2852) present at /opt/investor-reporting-export/session/storageState.json BEFORE the render send. irpt-export-render-run invoked against the DEPLOYED bytes (this same send synced them from S3) with the replayed GENRT8PROOF/rt8-render ExportBundle. StandardOutputContent shows the NEW, distinguishing log line -- 'OK: session state loaded from /opt/investor-reporting-export/session/storageState.json (1 cookies, 0 origins) -- attempting session reuse' -- never printed by the pre-cell script, then STILL refuses: StandardErrorContent 'BLOCKED: SESSION_ABSENT -- the print route answered with a sign-in screen. This script never signs in; an authenticated session for the host is an OPERATOR ACT.' Status=Failed, ExecutionElapsedTime=PT4.28S. No PDF was written (outcome:REFUSED in the printed GUARD line). Vendor-separation guard: 11 of 11 requests to opalinvest.dev, 0 foreign, 0 vendor. NEVER claims a real session was established -- the fake session correctly failed to authenticate. | CLOSED 20260921T161510Z |

## Log

- 20260921T160602Z OPENED by 0.9.0_WK_IRPT_BCKEND~5 with 3 leg(s)
- 20260921T161428Z LEG L1 closed: head-object+get-object on all 5 keys under s3://opal-313476888478-lambda-artifacts/ec2/investor-reporting-export/ this s
- 20260921T161449Z LEG L2 closed: ssm:5ab3ab4f-3268-4a9f-bd91-4d1ae8f7334e -- SSM AWS-RunShellScript sha256sum of the RUNNING path /opt/investor-reporting
- 20260921T161510Z LEG L3 closed: ssm:91bcd165-9ca0-4fda-9d9f-5b3bbc234482 -- synthetic storageState.json (352 bytes, clearly-fake cookie IB_RTH5_ARM_E_SY
- 20260921T161523Z CLOSED -- all 3 legs proven
