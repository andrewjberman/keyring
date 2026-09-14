# Deploy Completion Record
**Date opened:** 2026-09-14T21:22:07.408537+00:00
**Status:** OPEN
**Deploy:** POSN_ASTTAX B4: cot-satellites-characteristics-producer (new function)
**Authored by:** 0.9.0_WK_POSN_ASTTAX~20
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | SITEZ commit of producer + trigger + build_package + tf | hash |  | OPEN |
| L2 | s3-prefix | opal-313476888478-lambda-artifacts cot-pipeline/cot-satellites-characteristics-producer.zip | sha256 |  | OPEN |
| L3 | verify | plan (new function + role + policies + rule + target + permission) | summary |  | OPEN |
| L4 | activation | safe-apply | summary |  | OPEN |
| L5 | verify | 0-diff | No changes |  | OPEN |
| L6 | verify | QA invocation lands characteristics.json | s3api head + content read |  | OPEN |
| L7 | verify | schedule enabled with the function as target | describe-rule + list-targets |  | OPEN |
| L8 | verify | next scheduled 07:20Z fire lands organically (the negative arm; recorded by the COO) | head after the fire |  | OPEN |

## Log

- 20260914T212207Z OPENED by 0.9.0_WK_POSN_ASTTAX~20 with 8 leg(s)
