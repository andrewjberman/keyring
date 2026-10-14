# Deploy Completion Record
**Date opened:** 2026-10-14T06:18:12.936103+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261014T113034Z
**Deploy:** MDPF_SECCLASS TO-SC-e97b leg Q (amendments 2-4): ad-hoc QA run of C_06 ALONE on unchanged inputs, canonical mode, on the production runner. No code key moves. Boot wrapper stopped by systemctl first (option A), then BD_PLATINUM_MODE=canonical gold_dispatch.sh --single C_06 from S3. Opened as its own entry because deploy_ledger.py cannot add a leg to the HELD entry secclass-e97-c06-d04-rolling-rederive-sc1-20261012. Rollback: any C_06-written key whose ETag differs after the run goes back to its BEFORE VersionId.
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| B | verify | STEP 0 and BEFORE: runner stopped and trigger-pending absent before the start; accounts_dimension_latest.parquet ETag and VersionId recorded; after the stop command: no gold process, no trigger-pending; BEFORE key lists (canonical clients and views, mix_daily_summary, firm mix_summary, firm_mix_views and firm_mix_views_daily; legacy client_timeseries and the watermark) to E97_LEGQ_BEFORE_20261014.json with pages and key counts | runner state reads, accounts-dimension version, gate outputs, BEFORE file with counts | stop CommandId 703c7787-46de-40f5-b49c-fd7fff3f1e8c at 11:14:07Z STOP-RC=0 ACTIVE=failed NO-GOLD-PROCESS; gold/trigger-pending.json 404; accounts_dimension_latest ETag 8738357c8aa372e36bbe1a65040c533a VersionId DL3BWqn7cTrEnDsYqLjVjLWnRvriVhi1 (04:03:46Z); BEFORE2 deliverables/E97_LEGQ_BEFORE2_20261014.json 29565 keys 11:17:03Z (supersedes 06:21Z BEFORE: runner relaunched 09:46:43Z by advi-49f-gold-dispatch; mix_daily_summary ETag and both watermarks rewritten 06:24:16Z) | CLOSED 20261014T111945Z |
| R | activation | THE RUN: first SSM command sudo systemctl stop gold-layer-runner (its output printed), second SSM command BD_PLATINUM_MODE=canonical bash /tmp/gold_dispatch.sh --single C_06 with the script pulled from S3; both CommandIds printed | CommandIds, stop output, single's rc and its C06-ROLLING-REDERIVE line from the single log | CommandIds 703c7787 (stop, STOP-RC=0, 11:14:07Z) + fd6ae905 (single, 11:19:07-11:22:45Z, Success rc 0); log s3://opal-data-bd/gold/logs/single_C_06_20261014_111907.log: C06-ROLLING-REDERIVE relationships_read=3795 relationships_rewritten=0 keys_written=0; run 1 (previous instance, 28f0c841, 06:21:49Z) same line | CLOSED 20261014T113025Z |
| A | verify | AFTER lists to E97_LEGQ_AFTER_20261014.json and the DELTA verdict (same key set, every ETag equal), keys with a new VersionId and equal ETag reported, accounts-dimension version after, S_00 state and proof A_00 and A_02 never ran | AFTER file, compare output, S_00 and A_00/A_02 telemetry state | order key set 15544 vs 15544, none added/removed, ETAG_DIFFERS=1 (mix_daily_summary, key-order only, parsed JSON identical) restored to 0hTbccF5... at 11:27:24Z new VersionId sB5iD9.LuxAWSYF77RFYvWY4uCbVSA1. ETag afd575 equal to BEFORE; post-restore DELTA=0, 3 new-version-equal-ETag; accounts_dimension unchanged DL3BWqn7...; S_00/A_00/A_02 telemetry newest 09:49-09:50Z, none after 11:13Z; E97_LEGQ_DELTA_ORDER_KEYSET_20261014.txt | CLOSED 20261014T113025Z |

## Log

- 20261014T061812Z OPENED by 0.7.0_AE_CloudOps~SC1 with 3 leg(s)
- 20261014T111945Z LEG B closed: stop CommandId 703c7787-46de-40f5-b49c-fd7fff3f1e8c at 11:14:07Z STOP-RC=0 ACTIVE=failed NO-GOLD-PROCESS; gold/trigger-p
- 20261014T113025Z LEG R closed: CommandIds 703c7787 (stop, STOP-RC=0, 11:14:07Z) + fd6ae905 (single, 11:19:07-11:22:45Z, Success rc 0); log s3://opal-da
- 20261014T113025Z LEG A closed: order key set 15544 vs 15544, none added/removed, ETAG_DIFFERS=1 (mix_daily_summary, key-order only, parsed JSON identic
- 20261014T113034Z CLOSED -- all 3 legs proven
