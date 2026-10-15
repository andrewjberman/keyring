# Deploy Completion Record
**Date opened:** 2026-10-15T06:45:25.540728+00:00
**Status:** OPEN
**Deploy:** MDPF_SECCLASS TO-SC-e102b: ship ONE file s3://opal-data-bd/code/gold/C_06.client_mix_timeseries.py (ETag f847d8d1 -> md5 f884f28d, one line sort_keys=True), then leg Q' (two C_06 singles, canonical, on unchanged inputs). Sentinel org/critical_paths/.open_deploys/secclass-e102-c06-sorted-keys-sc1-20261015.json; entry org/critical_paths/change_management/ (name printed at open). Rollback: code by VersionId jGO15I3AZTATLbGxE3_36dKm86wuggDK then safe-deploy of base bytes; data by leg P VersionIds and the VersionId read immediately before run 1.
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 15.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| V | verify | Step 0 reads: served C_06 ETag f847d8d1 VersionId jGO15I3A, runner stopped, no trigger-pending, 49F head-object, open-deploy ledgers across every worktree | read outputs in the log |  | OPEN |
| P | verify | Leg P: IsLatest VersionIds of mix_daily_summary, firm_mix_views_daily + alias, advisor mix_daily + aliases, platinum/firm/mix_summary.json, pages and key counts printed, to deliverables/E102_LEGP_20261014.json plus the live mix daily summary body | file path, sha256, key and page counts |  | OPEN |
| D | s3-prefix | s3://opal-data-bd/code/gold/C_06.client_mix_timeseries.py | safe-deploy.sh comp-pipescript deployed MATCH line, served ETag f884f28d, pre/post census of code/gold/ shows only C_06 moved |  | OPEN |
| Q | verify | Leg Q' Branch 1: runner stopped first by systemctl stop gold-layer-runner, run 1 and run 2 of BD_PLATINUM_MODE=canonical gold_dispatch.sh --single C_06; parsed-equal, sorted-bytes md5, rolling-rederive 0/0, other keys' ETags equal, run 2 ETag equal to run 1 | CommandIds, C06-ROLLING-REDERIVE lines, compare output |  | OPEN |

## Log

- 20261015T064525Z OPENED by 0.7.0_AE_CloudOps~SC1 with 4 leg(s)
