# Deploy Completion Record
**Date opened:** 2026-10-02T05:02:56.692867+00:00
**Status:** OPEN
**Deploy:** irpt-ycharts-generate whole bundle at CLOUD 97eaff05ff (item 18: the catalogue reads etf-classifications once per window) and the catalogue route GET analysis/comparisons on the api root; never-widen packet, both halves
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | re-pin the irpt-ycharts-generate source-map row to the pin, build-and-upload, read the uploaded object back by version, member census against the live function | artifact sha256 and S3 version; downloaded by version, hash equal; census |  | OPEN |
| D1 | verify | ONE targeted safe-apply of the generate function after both halves | apply output; CodeSha256 equals the built hash; a re-plan of the same target reads no changes |  | OPEN |
| D2 | verify | ONE targeted safe-apply of aws_apigatewayv2_route.irpt for GET /api/scoped/investor-reporting/analysis/comparisons after both halves | apply output; get-routes shows the route on the portal API with the authorizer; a re-plan reads no changes |  | OPEN |
| V1 | verify | served read-back as svc-irpt-analysis: GET analysis/comparisons lists the model entries and named tickers; POST analysis (empty body) and the upload route answer as before | the route outputs, read for values before commit |  | OPEN |

## Log

- 20261002T050256Z OPENED by 2.0.0_SA_COO~Y with 4 leg(s)
