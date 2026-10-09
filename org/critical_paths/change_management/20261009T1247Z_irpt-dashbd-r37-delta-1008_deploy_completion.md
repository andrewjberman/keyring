# Deploy Completion Record
**Date opened:** 2026-10-09T12:47:22.905946+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD DB-b-88: R37 DELTA -- realized key gains realized_gain; re-pin account_activity_lots.py (0a41f929a3) and 2026-10-08 lots backfill on irpt-49f-reporting-gold-lambda -- signed against R37 packet sha256 848dd8640688c28cb62ffab109c4d55ea4e5348bc5286400a824d8e1405fd40b; delta packet sha256 e4231140c59ecee6183cbab525193e612882a4d2c43150863a17f103d6e37ae6; targeted plan 0/1/0
**Authored by:** 0.9.0_WK_IRPT_DASHBD~63
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | source-map re-pin + artifact upload + targeted plan | Plan: 0 to add, 1 to change, 0 to destroy |  | OPEN |
| D1 | activation | safe-apply of the saved plan, infra/aws/terraform/investor-reporting/reporting-gold | Apply complete, 1 changed |  | OPEN |
| V1 | verify | readback CodeSha256 = source map deployed_code_sha256 | get-function-configuration CodeSha256 |  | OPEN |
| B1 | verify | ONE backfill 2026-10-08 (lots rows, no LOTS_SKIPPED, returns byte-equal) | request id + REPORT line + returns sha256 before/after |  | OPEN |

## Log

- 20261009T124722Z OPENED by 0.9.0_WK_IRPT_DASHBD~63 with 4 leg(s)
