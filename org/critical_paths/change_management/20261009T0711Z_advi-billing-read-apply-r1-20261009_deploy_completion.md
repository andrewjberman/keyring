# Deploy Completion Record
**Date opened:** 2026-10-09T07:11:44.879402+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261009T071730Z
**Deploy:** ADVI_BILLING r1 close act 1: advi-49f-billing-read-lambda + route apply (7 creates) under CTO half @f4d29e294d; pin 7f294053f0; zip sha256 nIVJlBWb2zSupWk2p8C2tfkCyafXBxmE43HowkifxPQ=
**Authored by:** 2.0.0_SA_COO~B2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| V0 | verify | fee-quarter path for z08219260 BEFORE apply: route census + $default handler invoke | status recorded | BEFORE apply 07:1xZ: live route census of API 7k3ed8px20 = 117 routes, 0 fee-quarter routes, only $default matches the path; $default handler opal-portal-data-proxy invoked with the path as a 49financial user -> statusCode 404 {"error": "Route not found"}. P3 baseline: opal-partners-data platinum-summary z08219260 -> 200, body sha256 44df27b5df58b0a0..., stable on repeat. | CLOSED 20261009T071329Z |
| B1 | s3-prefix | opal-313476888478-lambda-artifacts advi/advi-billing-read-lambda.zip | head-object sha256 = built sha | s3://opal-313476888478-lambda-artifacts/advi/advi-billing-read-lambda.zip head-object 07:13:39Z: metadata content-sha256 nIVJlBWb2zSupWk2p8C2tfkCyafXBxmE43HowkifxPQ= = BUILD_ONLY sha (pin 7f294053f0), 100351 bytes | CLOSED 20261009T071410Z |
| A1 | activation | safe-apply infra/aws/terraform/advi/billing-read (re-plan 7/0/0) | apply 7 added + 0-diff re-plan | safe-apply of saved plan (7 to add, 0 change, 0 destroy; function_name advi-49f-billing-read-lambda = name() output): Apply complete 7 added; route id 9qas07n, integration 2eevnru; 0-diff re-plan 'No changes' exit 0; live CodeSha256 nIVJlBWb2zSupWk2p8C2tfkCyafXBxmE43HowkifxPQ= = built zip; LastUpdateStatus Successful | CLOSED 20261009T071701Z |
| P1 | verify | in-scope invoke z08219260/2026Q3 | body bytes = S3 object bytes | invoke advi-49f-billing-read-lambda (route GET .../relationship/{clientKey}/fee-quarter/{quarter}) as a 49financial user for z08219260/2026Q3 -> 200; body bytes == s3 object bytes (sha256 cda86da1fece8a23...) | CLOSED 20261009T071729Z |
| P2 | verify | other-firm invoke | refused, no S3 read | same path as a cottonwood principal -> 401 {"error": "Access denied to this firm"}; the refusal precedes the S3 read in entry.py and in the 16-test suite's no-S3-call assertion (live S3 access not traced) | CLOSED 20261009T071729Z |
| P3 | verify | opal-portal-data-proxy platinum-summary z08219260 before/after | byte-identical | opal-partners-data platinum-summary z08219260 after apply -> 200, body sha256 44df27b5df58b0a0... = before (byte-identical control) | CLOSED 20261009T071730Z |

## Log

- 20261009T071144Z OPENED by 2.0.0_SA_COO~B2 with 6 leg(s)
- 20261009T071329Z LEG V0 closed: BEFORE apply 07:1xZ: live route census of API 7k3ed8px20 = 117 routes, 0 fee-quarter routes, only $default matches the p
- 20261009T071410Z LEG B1 closed: s3://opal-313476888478-lambda-artifacts/advi/advi-billing-read-lambda.zip head-object 07:13:39Z: metadata content-sha256
- 20261009T071701Z LEG A1 closed: safe-apply of saved plan (7 to add, 0 change, 0 destroy; function_name advi-49f-billing-read-lambda = name() output): Ap
- 20261009T071729Z LEG P1 closed: invoke advi-49f-billing-read-lambda (route GET .../relationship/{clientKey}/fee-quarter/{quarter}) as a 49financial user
- 20261009T071729Z LEG P2 closed: same path as a cottonwood principal -> 401 {"error": "Access denied to this firm"}; the refusal precedes the S3 read in 
- 20261009T071730Z LEG P3 closed: opal-partners-data platinum-summary z08219260 after apply -> 200, body sha256 44df27b5df58b0a0... = before (byte-identic
- 20261009T071730Z CLOSED -- all 6 legs proven
