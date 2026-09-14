# Deploy Completion Record
**Date opened:** 2026-09-14T18:44:36.788769+00:00
**Status:** OPEN
**Deploy:** POSN_ASTTAX B2: cot-satellites-registry-producer emits holdings.json beside registry.json
**Authored by:** 0.9.0_WK_POSN_ASTTAX~20
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | SITEZ commit of producer + trigger + build_package + tf | hash |  | OPEN |
| L2 | s3-prefix | opal-313476888478-lambda-artifacts cot-pipeline/cot-satellites-registry-producer.zip | sha256 |  | OPEN |
| L3 | verify | plan scoped | summary |  | OPEN |
| L4 | activation | safe-apply | summary |  | OPEN |
| L5 | verify | 0-diff | No changes |  | OPEN |
| L6 | verify | QA invocation lands holdings.json | s3api head + content read |  | OPEN |
| L7 | verify | schedule enabled with the function as target | describe-rule + list-targets |  | OPEN |
| L8 | verify | next scheduled 07:00Z fire lands holdings.json organically (the negative arm; recorded by the COO, not waited on here) | s3api head after the fire |  | OPEN |

## Log

- 20260914T184436Z OPENED by 0.9.0_WK_POSN_ASTTAX~20 with 8 leg(s)
