# Deploy Completion Record
**Date opened:** 2026-10-03T09:56:32.323144+00:00
**Status:** OPEN
**Deploy:** MDPF_SECCLASS-S18 class cell: deploy A_03 scoped liveness + backstop, C_06 watermarks to 09-30, one QA run, re-enable the fires; COO half @56d91fc1ec, CTO half batch 224 @2f1a96042d
**Authored by:** 2.0.0_SA_COO~M
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P | verify | preconditions: runner stopped, both rules DISABLED, deployed A_03 md5 6bce3508, silver max trade date 2026-10-01, deployed gold_prof.py + runner-telemetry.py propagate exit 2 (CTO batch 224 cond. 1) | reads | 10:0xZ reads: runner i-01003b035d2988dfb stopped; bd-gold-nightly-fallback DISABLED, bd-canonical-prices-daily DISABLED (describe-rule); deployed code/gold/A_03.positions_cube.py md5 6bce3508 VersionId 1MYNHoSQGh..; silver max trade date 2026-10-01 (newest file silver/transactions/2026-10-03.parquet max trade_date 2026-10-01; the six newest files read). CTO batch 224 cond. 1: deployed code/gold/gold_prof.py md5 6a9c95c3 (vf.dxvglJL..) EQUAL to data/black_diamond/scripts/gold/gold_prof.py, whose child exit flows exit_code = proc.wait() (:176) -> sys.exit(exit_code) (:242); deployed code/gold/runner-telemetry.py md5 75e86dfe (GjdfdZkSZW..) DIFFERS from .tools/runner-telemetry.py (0903aab3), so its own bytes were read: proc = subprocess.Popen(cmd) (:394), rc = proc.wait() (:403), return rc (:407), sys.exit(main()) (:411). Exit 2 propagates through both wrappers to gold_dispatch.sh run_script (_rc) -> wait_phase abort (NONFATAL_IDS = E_18 only). | CLOSED 20261003T095832Z |
| G | s3-prefix | safe-deploy A_03.positions_cube.py to opal-data-bd code/gold; prior VersionId 1MYNHoSQ.. | comp-pipescript deployed MATCH + prior VersionId | 10:00Z safe-deploy (HALT_ACK=1) rc 0 'OK: safe-deploy gate PASS -- all 1 file(s) deployed and verified'; 'VERIFY OK comp-pipescript deployed data/black_diamond/scripts/gold/A_03.positions_cube.py'. code/gold/A_03.positions_cube.py 1MYNHoSQGh.. (6bce3508, 2026-06-24) -> wTaLoeFXO4.. (4baf5de3 = CLOUD HEAD md5) 10:00:22Z; rollback = copy-object <- 1MYNHoSQGh... ALSO SHIPPED (CODE_TREES, row S16 class): code/gold/lib/_shared/ etf_classifications_dynamodb.py, etf_classification_scheduled.py, etf_classification.py re-uploaded 10:00:02-15Z with ETags 4cc11d3e, 617015f8, 4d63e303 = their 2026-10-02 14:36Z versions (byte-identical, no change). | CLOSED 20261003T100147Z |
| W | verify | C_06 watermarks to 09-30 (aESAiTiS.., qr2SMNeS..); prior kgIB3uHU.., say77ubaeS.. | before/after reads | 10:0xZ copy-object (metadata COPY), opal-data-bd, runner stopped, current version asserted before each copy: gold/meta/client_timeseries_watermark.json <- aESAiTiS5lfum6VL6IJyqyVjdoznykmg (data_as_of 2026-09-30), new Rkg85Sq9CloW2WU96rWmyR8STh.FQOHc; gold/client_timeseries/_watermark.json <- qr2SMNeSj6ijkFvcKxjHYuX7rVdvSjOq, new EnO3WQUzseLjBEWu733C8opWePqGp3wo. Readback both data_as_of 2026-09-30. Prior (rollback) versions: kgIB3uHU5__CA9dtObbYN0CrdaIbHcfz and say77ubaeSVYBNpnCCM.unZ.vXtqV4.p (data_as_of 2026-10-01, the S18 run). A_03's gate watermark not touched (code bytes are in its fingerprint). | CLOSED 20261003T100209Z |
| Q | verify | ONE ad hoc QA run bd-gold-trigger {mode: incremental}; A_03 Liveness + Step 3c lines | run log |  | OPEN |
| V | verify | acceptance: mix_summary 10-01 every class, pct 1.0, MV within 2.0 pct of 1,843,114,311.70; z0812888131 10-01 non-zero; the 335 synthetic_correction ~0 | served reads |  | OPEN |
| R | activation | re-enable bd-gold-nightly-fallback + bd-canonical-prices-daily, read back ENABLED | describe-rule |  | OPEN |
| S | verify | first scheduled fire after R, read by 3.0.0_SA_CVO (CTO batch 224 cond. 2) | CVO read |  | OPEN |

## Log

- 20261003T095632Z OPENED by 2.0.0_SA_COO~M with 7 leg(s)
- 20261003T095832Z LEG P closed: 10:0xZ reads: runner i-01003b035d2988dfb stopped; bd-gold-nightly-fallback DISABLED, bd-canonical-prices-daily DISABLED 
- 20261003T100147Z LEG G closed: 10:00Z safe-deploy (HALT_ACK=1) rc 0 'OK: safe-deploy gate PASS -- all 1 file(s) deployed and verified'; 'VERIFY OK comp
- 20261003T100209Z LEG W closed: 10:0xZ copy-object (metadata COPY), opal-data-bd, runner stopped, current version asserted before each copy: gold/meta/c
