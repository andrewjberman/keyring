# Deploy Completion Record
**Date opened:** 2026-10-09T08:55:54.127969+00:00
**Status:** OPEN
**Deploy:** ADVI_BILLING TO-AB-e-1: five read-only GET probes of the edge book check (.004c relationship) for household z08219260, with five synthetic 10-minute RS256 tokens minted in-session
**Authored by:** 0.7.0_AE_CloudOps~AB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | cloudfront GET in_book -> /api/scoped/partners/books/relationship/z08219260/fee-quarter/2026Q3 | integer HTTP status recorded in AB_E1_PROBES.json | in_book: advisorId chase_bertrand, map lists z08219260 -> HTTP 200 through CloudFront; AB_E1_PROBES.json probes[0] | CLOSED 20261009T090725Z |
| L2 | verify | cloudfront GET out_of_book -> same route, mapped advisor without z08219260 | integer HTTP status recorded in AB_E1_PROBES.json | out_of_book: advisorId abby_horton, mapped with a non-empty book that lacks z08219260 -> HTTP 403, body head Advisor scoping: not authorized for this resource (edge .004c, index.mjs:529-543); probes[1] | CLOSED 20261009T090744Z |
| L3 | verify | cloudfront GET firm_admin -> same route, firmRole=admin bypass | integer HTTP status recorded in AB_E1_PROBES.json | firm_admin: firmRole admin, no advisorId -> HTTP 200; the admin short-circuit at index.mjs:468-470 admits before any ownership-map read; probes[2] | CLOSED 20261009T090803Z |
| L4 | verify | cloudfront GET other_firm -> same route, firmId=mockadv | integer HTTP status recorded in AB_E1_PROBES.json |  | OPEN |
| L5 | verify | execute-api GET execute_api_bypass -> 7k3ed8px20.execute-api.us-east-1.amazonaws.com, CloudFront bypass | integer HTTP status recorded in AB_E1_PROBES.json |  | OPEN |

## Log

- 20261009T085554Z OPENED by 0.7.0_AE_CloudOps~AB2 with 5 leg(s)
- 20261009T090725Z LEG L1 closed: in_book: advisorId chase_bertrand, map lists z08219260 -> HTTP 200 through CloudFront; AB_E1_PROBES.json probes[0]
- 20261009T090744Z LEG L2 closed: out_of_book: advisorId abby_horton, mapped with a non-empty book that lacks z08219260 -> HTTP 403, body head Advisor sco
- 20261009T090803Z LEG L3 closed: firm_admin: firmRole admin, no advisorId -> HTTP 200; the admin short-circuit at index.mjs:468-470 admits before any own
