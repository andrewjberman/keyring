# Deploy Completion Record
**Date opened:** 2026-09-23T22:26:22.904458+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260923T230810Z
**Deploy:** Holdings exact Lambda-depth schema repair
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | activation | Replacement canonical artifact upload | Exact member/code hash and VersionId | Replacement artifact s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-holdings.zip VersionId nWRHWWilAp0fu9f7swCfvS1zXHEaTfXC, zip SHA256 97f190ac5704bd63153f24666401a8a102ed35dc1a1c07be0afcbfdb71540c35, content-sha256 metadata l/GQrFcEvWMVPyRmZAGooQLtNdwaHAe+Cvy/23FUDDU=; 33 members, only snapshot.py/BUILD_MANIFEST differ from e7XAGneq1 (CTO d8e9d68378 independent download); HOLDINGS_SCHEMA_APPLY_20260923.json | CLOSED 20260923T230510Z |
| A1 | activation | Reviewed one-function saved plan | Canonical apply receipt | Saved plan 30f1d202bf7a50fa063e7d96eee2e6ae5ed7465c23471cf1d670230f780d5f02 applied via safe-apply from irpt-smoke-p-backend-20260923 at 23:00:52Z: 0 added 1 changed 0 destroyed, only module.irpt_holdings.aws_lambda_function.this; pre-apply live CodeSha vLP7cZN61JWOOmiCGmCjnOM43296i8qDt1hL1ZE8yUs= matched plan before (no drift); halt/naming/tagauthz/tombstone gates recorded in schema-apply-2.log; HOLDINGS_SCHEMA_APPLY_20260923.json | CLOSED 20260923T230510Z |
| V1 | verify | Actual code/config and no-diff | Runtime layout schema proof and M authenticated handoff | Actual irpt-holdings readback 23:00:52Z: CodeSha256 l/GQrFcEvWMVPyRmZAGooQLtNdwaHAe+Cvy/23FUDDU=, Active/Successful, python3.12, irpt-common:5, role/env unchanged, remote state serial 12; post-plan -detailed-exitcode rc=0 No changes; runtime layout schema proof CTO c6835d130c (replacement passes /var/task depth in the pinned Lambda image); exact-function recorder 7a356ba08e (last_deployed_commit c6dd07832f, deploy_ledger ab3bdd897e); M authenticated handoff sent as msg 99787 to 2.0.0_SA_COO~M, CTO copy 99786; HOLDINGS_SCHEMA_APPLY_20260923.json | CLOSED 20260923T230810Z |

## Log

- 20260923T222622Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260923T230510Z LEG P1 closed: Replacement artifact s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-holdings.zip VersionId nWRHWWilAp0f
- 20260923T230510Z LEG A1 closed: Saved plan 30f1d202bf7a50fa063e7d96eee2e6ae5ed7465c23471cf1d670230f780d5f02 applied via safe-apply from irpt-smoke-p-bac
- 20260923T230810Z LEG V1 closed: Actual irpt-holdings readback 23:00:52Z: CodeSha256 l/GQrFcEvWMVPyRmZAGooQLtNdwaHAe+Cvy/23FUDDU=, Active/Successful, pyt
- 20260923T230810Z CLOSED -- all 3 legs proven
