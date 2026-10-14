# Deploy Completion Record
**Date opened:** 2026-10-14T22:09:57.593645+00:00
**Status:** OPEN
**Deploy:** OG-sa-1 (A2): runner stopped, SA profile copied from the main tree, runner re-registered with sa
**Authored by:** 0.7.0_AE_CloudOps~ZW
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 14.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| STOP | activation | runner ended on its own STOP file at a job boundary | cycle record stopped_by_operator + 0 cycle_runner processes + STOP file deleted |  | OPEN |
| COPY | activation | runner sa profile backed up on this box then replaced by a copy of the main tree sa profile | backup path + user_id cookie count >=1 in the runner profile |  | OPEN |
| READS | verify | authenticated account read 200 through the runner profile and again through the main profile | sa1_runner_read.json + sa1_main_reread.json |  | OPEN |
| REGISTER | activation | task re-registered with -Publishers bbg,wsj,barrons,sa -Windowless -RefreshOnce and Running | task read back from the scheduler |  | OPEN |
| WINDOW | verify | one sa cycle later an SA bronze object newer than the re-registration for BA BABA COST | sa1.AC2.sh restored branch PASS |  | OPEN |

## Log

- 20261014T220957Z OPENED by 0.7.0_AE_CloudOps~ZW with 5 leg(s)
