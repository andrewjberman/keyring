# Deploy Completion Record
**Date opened:** 2026-09-15T03:43:51.686945+00:00
**Status:** OPEN
**Deploy:** POSN_ASTTAX B6: characteristics.json gains the tickers block; rule to cron(30 12 * * ? *); driven run
**Authored by:** 0.9.0_WK_POSN_ASTTAX~24
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | SITEZ commit of producer + build_package + tf | hash |  | OPEN |
| L2 | s3-prefix | opal-313476888478-lambda-artifacts cot-pipeline/cot-satellites-characteristics-producer.zip | VersionId + content-sha256 read back |  | OPEN |
| L3 | verify | targeted plan | 0 add / 3 change / 0 destroy |  | OPEN |
| L4 | activation | safe-apply | summary + HALTGT |  | OPEN |
| L5 | verify | unscoped 0-diff | No changes |  | OPEN |
| L6 | verify | driven invoke with explicit bbg_as_of lands the tickers block | VersionId moved + block read back |  | OPEN |
| L7 | verify | rule cron(30 12 * * ? *) ENABLED with the function as target | describe-rule + list-targets |  | OPEN |
| L8 | verify | first scheduled 12:30Z fire lands organically (the negative arm; recorded by the COO, not waited on here) | s3api head after the fire |  | OPEN |
| L9 | git | deploy recorded: source map + CHANGELOG entry by hand | git show --stat |  | OPEN |

## Log

- 20260915T034351Z OPENED by 0.9.0_WK_POSN_ASTTAX~24 with 9 leg(s)
