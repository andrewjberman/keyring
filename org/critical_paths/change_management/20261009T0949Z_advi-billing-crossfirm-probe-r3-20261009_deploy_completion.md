# Deploy Completion Record
**Date opened:** 2026-10-09T09:49:55.431218+00:00
**Status:** OPEN
**Deploy:** ADVI_BILLING TO-AB-r-2: ONE read-only GET probe exercising the cross-firm arm -- an other-firm (inflection) firmRole-admin token with complete claims against 49 Financial household z08219260
**Authored by:** 0.7.0_AE_CloudOps~AB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | cloudfront GET other-firm admin token -> /api/scoped/partners/books/relationship/z08219260/fee-quarter/2026Q3 | integer status 401/403 plus refused_by classified from the edge and Lambda source, recorded in AB_R2_CROSSFIRM_PROBE.json | cross-firm probe: firmId inflection, role user, firmRole admin, complete claims, ONE GET through opalinvest.dev -> HTTP 401 body head {error: Access denied to this firm}. The edge ADMITTED (firmRole admin short-circuits .004c at index.mjs:468-470); the read Lambda refused on the firm at infra/aws/lambda/advi/billing-read/entry.py:135-136, not 130-131: computeAllowedFirms builds inflection for these claims (portal-authorizer index.mjs:293-322), is_authorized(inflection, inflection) exercised True against the real function, and ADVI_BILLING_FIRM on the deployed advi-49f-billing-read-lambda reads 49financial. AB_R2_CROSSFIRM_PROBE.json probe; record commit a3715edef2 | CLOSED 20261009T095440Z |

## Log

- 20261009T094955Z OPENED by 0.7.0_AE_CloudOps~AB2 with 1 leg(s)
- 20261009T095440Z LEG L1 closed: cross-firm probe: firmId inflection, role user, firmRole admin, complete claims, ONE GET through opalinvest.dev -> HTTP 
