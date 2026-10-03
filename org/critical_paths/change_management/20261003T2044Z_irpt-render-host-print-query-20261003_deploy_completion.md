# Deploy Completion Record
**Date opened:** 2026-10-03T20:44:37.685337+00:00
**Status:** OPEN
**Deploy:** export render host forwards the PATH B print query (row S308/S310, IB-pr-308 @fb310203e5; packet blob 94c344b523 @640f54b8bf; CTO half batch 230 @3626428149)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| H1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/ec2/investor-reporting-export/render_export.cjs from git show fb310203e5 | read-back byte-equal; new VersionId recorded | 20:4xZ put git show fb310203e5:infra/aws/ec2/investor-reporting-export/render_export.cjs (16,434 B, sha256 9684b4b9c1615f62..) to s3://opal-313476888478-lambda-artifacts/ec2/investor-reporting-export/render_export.cjs -> VersionId lLkKsNvYhEMsLU99ffY1N86rbzBqeSjU; read-back of that version byte-equal; rollback version Sd9RAXh61J7ITvHcxezU3bo9cw5eIf0W | CLOSED 20261003T204508Z |
| S | verify | CTO stop: any INF or COT (PATH A) export render after H1 fails -> roll back to Sd9RAXh6 at once | every irpt-export-render-run after H1 read; no INF/COT failure |  | OPEN |
| R1 | verify | a PROD 49F export outside the six reaches READY with its frozen as_of | receipt READY, facts.frozen_as_of = the bundle's frozen as_of; SSM render Success |  | OPEN |
| R2 | verify | the rendered series is the frozen VersionId | by the render's own sha256 check against the frozen value (batch 205 item 3); bundle version_id + sha256 recorded |  | OPEN |

## Log

- 20261003T204437Z OPENED by 2.0.0_SA_COO~P with 4 leg(s)
- 20261003T204508Z LEG H1 closed: 20:4xZ put git show fb310203e5:infra/aws/ec2/investor-reporting-export/render_export.cjs (16,434 B, sha256 9684b4b9c1615
