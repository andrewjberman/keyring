# Deploy Completion Record
**Date opened:** 2026-08-20T13:45:14.092455+00:00
**Status:** OPEN
**Deploy:** D8_LIVEEDIT: opal-portal-content store + API + CF behaviors 4c/4d (laptop apply leg per CTO~Z cert @05689f222d)
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | lambda artifact portal-content/opal-portal-content-api.zip to opal-313476888478-lambda-artifacts | head-object with content-sha256 metadata | head-object Size=3231 ETag=d7c182e52c960f7521eb17295b94d175 Meta content-sha256=19kvv8JBrnOsofnSdpe12P4QI+rwCkRZZ+VmU+Dn5hA= == local sha256 (upload-verified, not cp-exit-trusted) | CLOSED 20260820T134614Z |
| L2 | activation | safe-apply infra/aws/terraform/portal-content (~9 adds: table+role+policy+lambda+integration+3 routes+permission) | apply output + 0-diff re-plan | apply 11 added/0 changed/0 destroyed == staged d8.tfplan; 0-diff re-plan 'no differences' rc=0; table opal-portal-content id created, lambda opal-portal-content-api id created, 3 routes jl98s68/zofpjr5/zod4t2b on 7k3ed8px20 | CLOSED 20260820T135029Z |
| L3 | activation | safe-apply infra/aws/terraform/portal-auth (CF ordered behaviors 4c/4d /api/scoped/portal-content{,/*}) | apply output + 0-diff re-plan | apply in-place 0-add/1-change/0-destroy == staged d8auth.tfplan (behavior-list insert only: +2 adds, 0 removes, 0 non-behavior attrs); 0-diff re-plan 'No changes'; LIVE cloudfront get-distribution-config EVTSA9VEHNZVH: 26 behaviors, both /api/scoped/portal-content{,/*} present | CLOSED 20260820T140422Z |
| L4 | git | tag portal-content-v1.0.0 + push --follow-tags (vintage 4c8fe9d006+13fd07d510 already committed pre-apply) | tag name on remote |  | OPEN |
| L5 | verify | deployed-bytes hash vs source @4c8fe9d006 via source-map entry @13fd07d510 + IAM simulate battery D8-7 (one resource per call, separate positive control) | hash match + simulate outputs | deployed pkg member lambda_function.py sha256 3d51d677..bba0cf BYTE-MATCH source @4c8fe9d006 via source-map entry (mutant control differs=True); IAM simulate x4 SEPARATE invocations Put/Get/Delete/Scan all 'allowed' on exact table ARN; foreign-table negative control implicitDeny; accessanalyzer validate-policy 0 findings | CLOSED 20260820T140806Z |
| L6 | verify | D8-4 live 403 (non-employee PUT) + D8-3 persistence (internal PUT->GET) on https://www.opalinvest.dev/api/scoped/portal-content | HTTP responses | LIVE via www.opalinvest.dev through CF behaviors: D8-4 non-employee PUT AND DELETE both 403 '{error: forbidden: Opal-internal editors only}' (Lambda chokepoint body, not gateway generic -- valid RS256 token w/ iss=opal-portal-auth aud=opal-portal-api, firmId=49financial); D8-3 internal PUT 200 updated_by=token-subject, GET from SECOND identity shows override + updated_by/updated_at (Q3 visibility live), internal DELETE reset:true, residue GET count=0 | CLOSED 20260820T141525Z |

## Log

- 20260820T134514Z OPENED by 0.7.0_AE_CloudOps with 6 leg(s)
- 20260820T134614Z LEG L1 closed: head-object Size=3231 ETag=d7c182e52c960f7521eb17295b94d175 Meta content-sha256=19kvv8JBrnOsofnSdpe12P4QI+rwCkRZZ+VmU+Dn
- 20260820T135029Z LEG L2 closed: apply 11 added/0 changed/0 destroyed == staged d8.tfplan; 0-diff re-plan 'no differences' rc=0; table opal-portal-conten
- 20260820T140422Z LEG L3 closed: apply in-place 0-add/1-change/0-destroy == staged d8auth.tfplan (behavior-list insert only: +2 adds, 0 removes, 0 non-be
- 20260820T140806Z LEG L5 closed: deployed pkg member lambda_function.py sha256 3d51d677..bba0cf BYTE-MATCH source @4c8fe9d006 via source-map entry (mutan
- 20260820T141525Z LEG L6 closed: LIVE via www.opalinvest.dev through CF behaviors: D8-4 non-employee PUT AND DELETE both 403 '{error: forbidden: Opal-int
