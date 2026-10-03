# Deploy Completion Record
**Date opened:** 2026-10-03T20:44:37.685337+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261003T223316Z
**Deploy:** export render host forwards the PATH B print query (row S308/S310, IB-pr-308 @fb310203e5; packet blob 94c344b523 @640f54b8bf; CTO half batch 230 @3626428149)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| H1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/ec2/investor-reporting-export/render_export.cjs from git show fb310203e5 | read-back byte-equal; new VersionId recorded | 20:4xZ put git show fb310203e5:infra/aws/ec2/investor-reporting-export/render_export.cjs (16,434 B, sha256 9684b4b9c1615f62..) to s3://opal-313476888478-lambda-artifacts/ec2/investor-reporting-export/render_export.cjs -> VersionId lLkKsNvYhEMsLU99ffY1N86rbzBqeSjU; read-back of that version byte-equal; rollback version Sd9RAXh61J7ITvHcxezU3bo9cw5eIf0W | CLOSED 20261003T204508Z |
| S | verify | CTO stop: any INF or COT (PATH A) export render after H1 fails -> roll back to Sd9RAXh6 at once | every irpt-export-render-run after H1 read; no INF/COT failure | Every irpt-export-render-run after H1 (20:44Z) read account-wide: 8022f0fd 20:49:00Z tenant 49financial Failed (S311, the page's manifest read; not the host script) and 123e754c 22:13:03Z tenant 49financial Success. 0 INF or COT renders after H1, so 0 INF/COT failures; the CTO stop never triggered. PATH A forwarding is unchanged by the cell's test 3 (selection, start, end reach the URL) | CLOSED 20261003T223233Z |
| R1 | verify | a PROD 49F export outside the six reaches READY with its frozen as_of | receipt READY, facts.frozen_as_of = the bundle's frozen as_of; SSM render Success | 22:12:52Z 2.0.0_SA_COO~D pressed export once for ****0090 (acc_5475ef6b78036e90a79eba33, outside the six; msg 104799), PROD portal dbd29c6320 (tag portal-v2.1.198, carries S311). SSM irpt-export-render-run 123e754c on i-0167fd745ad906a66 (22:13:03Z, tenant 49financial) Success with render_export.cjs 16,434 B (S3 lLkKsNvY). Receipt s3://opal-data-ycharts/firms/49financial/generations/EXP-e29b5415a06f90f943481c41a1a4821b/receipt.json (22:13:15Z) job_state READY, facts.frozen_as_of 2026-10-01 = bundle performance_source.as_of 2026-10-01; validation PASSED, 11 pages, 0 failures; metadata irpt-frozen-as-of 2026-10-01; render_guard RENDERED, 0 foreign of 20 requests, all opalinvest.dev, 0 vendor | CLOSED 20261003T223233Z |
| R2 | verify | the rendered series is the frozen VersionId | by the render's own sha256 check against the frozen value (batch 205 item 3); bundle version_id + sha256 recorded | By the render's own rule (CTO batch 205 item 3: it reads exactly the pinned VersionId and refuses by name on a sha256 mismatch), the READY receipt means a match. Bundle exr_5f3c0b757a054bffbe31b431: performance_source version_id H1BKI.nQTmldVL.FegvvlUp3T96eazsy, sha256 0b61551661167bc517f25e566e851817015ad9348e1637994657387ac07319e0, as_of 2026-10-01, path PLATINUM; report.pdf 136,334 B | CLOSED 20261003T223233Z |

## Log

- 20261003T204437Z OPENED by 2.0.0_SA_COO~P with 4 leg(s)
- 20261003T204508Z LEG H1 closed: 20:4xZ put git show fb310203e5:infra/aws/ec2/investor-reporting-export/render_export.cjs (16,434 B, sha256 9684b4b9c1615
- 20261003T223233Z LEG R1 closed: 22:12:52Z 2.0.0_SA_COO~D pressed export once for ****0090 (acc_5475ef6b78036e90a79eba33, outside the six; msg 104799), P
- 20261003T223233Z LEG R2 closed: By the render's own rule (CTO batch 205 item 3: it reads exactly the pinned VersionId and refuses by name on a sha256 mi
- 20261003T223233Z LEG S closed: Every irpt-export-render-run after H1 (20:44Z) read account-wide: 8022f0fd 20:49:00Z tenant 49financial Failed (S311, th
- 20261003T223316Z CLOSED -- all 4 legs proven
