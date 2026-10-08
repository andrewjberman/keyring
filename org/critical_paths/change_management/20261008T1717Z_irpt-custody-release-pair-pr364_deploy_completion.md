# Deploy Completion Record
**Date opened:** 2026-10-08T17:17:31.456495+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261008T173754Z
**Deploy:** IRPT_BCKEND TO-IB-pr-364: irpt-export-render at pin 1e0cdaf90c then custody-report-read route; rollback S3 version ZBwAzArTtDSpCIYL8CwhqqmIooS4mVPx (opal-313476888478-lambda-artifacts/investor-reporting/irpt-export-render.zip)
**Authored by:** 0.9.0_WK_IRPT_BCKEND~172
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| route | activation | aws_apigatewayv2_route custody-report-read api 7k3ed8px20 | TF apply of the one route + 0-diff targeted replan + route listed live | TF apply 1 added 0 destroyed; api root re-plan No changes; route GET /api/scoped/investor-reporting/custody-report/{reportId} listed on api 7k3ed8px20; unauthenticated GET refused 401 | CLOSED 20261008T173740Z |
| irpt-export-render | tf-lambda | module.irpt_export_render.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | TF apply 1 changed 0 destroyed; live CodeSha256 03p2eIEKU9iSIOe5GYDbkbisapqAjULUyAPA/Wcxrfc= equals built sha256 (S3 version FHKz88vjxHfi5uqADSw5GlQq8IULm615); export root re-plan No changes; release-census changed_members=0 | CLOSED 20261008T173740Z |

## Log

- 20261008T171731Z OPENED by 0.9.0_WK_IRPT_BCKEND~172 with 2 leg(s)
- 20261008T173740Z LEG irpt-export-render closed: TF apply 1 changed 0 destroyed; live CodeSha256 03p2eIEKU9iSIOe5GYDbkbisapqAjULUyAPA/Wcxrfc= equals built sha256 (S3 ver
- 20261008T173740Z LEG route closed: TF apply 1 added 0 destroyed; api root re-plan No changes; route GET /api/scoped/investor-reporting/custody-report/{repo
- 20261008T173754Z CLOSED -- all 2 legs proven
