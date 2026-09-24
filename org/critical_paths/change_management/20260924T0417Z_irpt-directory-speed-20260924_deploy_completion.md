# Deploy Completion Record
**Date opened:** 2026-09-24T04:17:52.528749+00:00
**Status:** OPEN
**Deploy:** IRPT directory listing speed: memory 512->1769, keep-warm schedule, code package at CRO pin 5886d0b9bd (CTO GO 100162/100169)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | safe-apply of the saved directory-root plan 31060b25 (3 add / 1 change / 0 destroy) | apply output line |  | OPEN |
| V1 | verify | get-function-configuration CodeSha256 == 6uxqQO2S..., MemorySize 1769, layers/env unchanged; get-schedule irpt-directory-keepwarm-5min ENABLED; re-plan rc 0 | readback lines |  | OPEN |
| R1 | verify | record-terraform-deploy.sh irpt-directory-search with the ledger commit and the code sha | recorder commit |  | OPEN |
| M1 | verify | CloudWatch Duration p50/p90 of irpt-directory-search over the first hour beside the 15:19-03:19Z baseline; one warm-fire log line; one timed Global list load | measurement receipt |  | OPEN |

## Log

- 20260924T041752Z OPENED by 2.0.0_SA_COO~P with 4 leg(s)
