# Deploy Completion Record
**Date opened:** 2026-10-08T17:17:31.456495+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND TO-IB-pr-364: irpt-export-render at pin 1e0cdaf90c then custody-report-read route; rollback S3 version ZBwAzArTtDSpCIYL8CwhqqmIooS4mVPx (opal-313476888478-lambda-artifacts/investor-reporting/irpt-export-render.zip)
**Authored by:** 0.9.0_WK_IRPT_BCKEND~172
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| route | activation | aws_apigatewayv2_route custody-report-read api 7k3ed8px20 | TF apply of the one route + 0-diff targeted replan + route listed live |  | OPEN |
| irpt-export-render | tf-lambda | module.irpt_export_render.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261008T171731Z OPENED by 0.9.0_WK_IRPT_BCKEND~172 with 2 leg(s)
