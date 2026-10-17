# Deploy Completion Record
**Date opened:** 2026-10-17T08:33:32.774570+00:00
**Status:** OPEN
**Deploy:** MDPF_SECCLASS TO-SC-e111b: ship TWO files s3://opal-data-bd/code/gold/E_18.detect_new_securities.py (ETag a7820a20 VersionId wb5QYkh7QEfrvMEscg.EgAui0MeBaNwB -> md5 f5c03ee6) and gold_dispatch.sh (ETag 882a910b VersionId .bNYVetB5sGV8bZki7EgXBfChCH_uPyE -> md5 165933f6), then leg Q E_18 single on the runner. Sentinel org/critical_paths/.open_deploys/secclass-e111b-e18-repoint-ship-dell1-20261017.json; entry org/critical_paths/change_management/ (name printed at open). Rollback: both files by the base VersionIds then safe-deploy of base bytes.
**Authored by:** 0.7.0_AE_CloudOps~DELL1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 13.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| V | verify | Step 0 reads: served ETags, md5 of repo files, runner stopped, no trigger-pending, open ledgers across worktrees | read outputs in the log |  | OPEN |
| P | verify | Leg P: code/gold IsLatest census and etf-classifications state to deliverables E111_LEGP_* | file paths, key and page counts |  | OPEN |
| D1 | s3-prefix | s3://opal-data-bd/code/gold/E_18.detect_new_securities.py | safe-deploy comp-pipescript deployed MATCH line, served ETag f5c03ee6 |  | OPEN |
| D2 | s3-prefix | s3://opal-data-bd/code/gold/gold_dispatch.sh | safe-deploy comp-pipescript deployed MATCH line, served ETag 165933f6 |  | OPEN |
| C | verify | e108_shipped_check.py reads E108-SHIPPED ok=True; pre/post code/gold census shows only the two moved | check line, census diff |  | OPEN |
| Q | verify | Leg Q Branch 1: runner service stopped first, BD_PLATINUM_MODE=canonical gold_dispatch.sh --single E_18 no --upload; exit 0, no ERROR, 9 held-out unresolved, etf-classifications unchanged | CommandIds, lines, table diff |  | OPEN |
| G | git | ledger, deliverables and logs committed | commit hash with push state |  | OPEN |

## Log

- 20261017T083332Z OPENED by 0.7.0_AE_CloudOps~DELL1 with 7 leg(s)
