# Deploy Completion Record
**Date opened:** 2026-10-14T06:18:12.936103+00:00
**Status:** OPEN
**Deploy:** MDPF_SECCLASS TO-SC-e97b leg Q (amendments 2-4): ad-hoc QA run of C_06 ALONE on unchanged inputs, canonical mode, on the production runner. No code key moves. Boot wrapper stopped by systemctl first (option A), then BD_PLATINUM_MODE=canonical gold_dispatch.sh --single C_06 from S3. Opened as its own entry because deploy_ledger.py cannot add a leg to the HELD entry secclass-e97-c06-d04-rolling-rederive-sc1-20261012. Rollback: any C_06-written key whose ETag differs after the run goes back to its BEFORE VersionId.
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| B | verify | STEP 0 and BEFORE: runner stopped and trigger-pending absent before the start; accounts_dimension_latest.parquet ETag and VersionId recorded; after the stop command: no gold process, no trigger-pending; BEFORE key lists (canonical clients and views, mix_daily_summary, firm mix_summary, firm_mix_views and firm_mix_views_daily; legacy client_timeseries and the watermark) to E97_LEGQ_BEFORE_20261014.json with pages and key counts | runner state reads, accounts-dimension version, gate outputs, BEFORE file with counts |  | OPEN |
| R | activation | THE RUN: first SSM command sudo systemctl stop gold-layer-runner (its output printed), second SSM command BD_PLATINUM_MODE=canonical bash /tmp/gold_dispatch.sh --single C_06 with the script pulled from S3; both CommandIds printed | CommandIds, stop output, single's rc and its C06-ROLLING-REDERIVE line from the single log |  | OPEN |
| A | verify | AFTER lists to E97_LEGQ_AFTER_20261014.json and the DELTA verdict (same key set, every ETag equal), keys with a new VersionId and equal ETag reported, accounts-dimension version after, S_00 state and proof A_00 and A_02 never ran | AFTER file, compare output, S_00 and A_00/A_02 telemetry state |  | OPEN |

## Log

- 20261014T061812Z OPENED by 0.7.0_AE_CloudOps~SC1 with 3 leg(s)
