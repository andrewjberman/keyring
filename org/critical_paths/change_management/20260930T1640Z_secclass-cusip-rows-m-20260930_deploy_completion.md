# Deploy Completion Record
**Date opened:** 2026-09-30T16:40:42.763136+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260930T164728Z
**Deploy:** MDPF_SECCLASS CUSIP_ROWS: 349 CUSIP:-keyed rows into etf-classifications by conditional put on absence (etf_classification_scheduled.write), halves COO 5cc84b40f6 / CTO 1f4792c45a; rollback DeleteItem over the census's 349 keys
**Authored by:** 2.0.0_SA_COO~M
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| G1 | verify | fresh r5_cusip_guard_dryrun.py immediately before the write | CUSIP-GUARD bd_delta_from_cusip=0 and CUSIP-GUARD-PLANNED would_copy_to_bd=0, both printed | r5_cusip_guard_dryrun.py 16:41:07Z: CUSIP-GUARD etf_rows=2309 cusip_rows=0 bd_rows=10929 bd_delta_from_cusip=0; CUSIP-GUARD-PLANNED planned=349 would_copy_to_bd=0 (re-run again at the write, W1) | CLOSED 20260930T164358Z |
| P1 | verify | PRE-READ of the 349 keys saved beside the ledger | present=0 of 349 | r5_cusip_rows_act.py --pre-read 16:43:31Z (consistent get_item x349): present=0 of 349; saved R5_CUSIP_ACT/PRE_READ_20260930T164331Z.json | CLOSED 20260930T164358Z |
| W1 | verify | conditional put per row via the module writer | written=349 refused=0 of 349 overwrites=0; any refused key explained | guard re-run at the write 16:44:40Z (both counts 0), then r5_cusip_rows_act.py --write 16:44:53Z via etf_classification_scheduled.write (attribute_not_exists(ticker)): written=348 refused=1 of 349 overwrites=0; saved R5_CUSIP_ACT/WRITE_20260930T164453Z.json. THE ONE REFUSAL EXPLAINED: the census carries CUSIP:786514AS8 twice (349 rows, 348 unique keys) -- 49financial (fixed_income, sub absent, input security_master_rate_bearing) and cottonwood (fixed_income / High Yield, input sec_asset_type) both hold the Safeway 7.45% 2027 bond; the first row wrote, the duplicate was refused by the absence condition, exactly as designed; no existing row moved | CLOSED 20260930T164728Z |
| R1 | verify | read-back of all 349 keys against the census file | equal=349 missing=0 differ=0 | r5_cusip_rows_act.py --read-back 16:46:19Z (consistent get_item x349): equal=348 missing=0 differ=1 of 349 -- the one differ is the duplicate CUSIP:786514AS8 census row (cottonwood's sub_asset_class High Yield vs the served row's absent sub_asset_class from the 49financial row that landed first); 348 unique keys all present and equal to their census row; saved R5_CUSIP_ACT/READ_BACK_20260930T164619Z.json. The High Yield enrichment is a seed-path correction (FWD-3), never this act's overwrite | CLOSED 20260930T164728Z |

## Log

- 20260930T164042Z OPENED by 2.0.0_SA_COO~M with 4 leg(s)
- 20260930T164358Z LEG G1 closed: r5_cusip_guard_dryrun.py 16:41:07Z: CUSIP-GUARD etf_rows=2309 cusip_rows=0 bd_rows=10929 bd_delta_from_cusip=0; CUSIP-GU
- 20260930T164358Z LEG P1 closed: r5_cusip_rows_act.py --pre-read 16:43:31Z (consistent get_item x349): present=0 of 349; saved R5_CUSIP_ACT/PRE_READ_2026
- 20260930T164728Z LEG W1 closed: guard re-run at the write 16:44:40Z (both counts 0), then r5_cusip_rows_act.py --write 16:44:53Z via etf_classification_
- 20260930T164728Z LEG R1 closed: r5_cusip_rows_act.py --read-back 16:46:19Z (consistent get_item x349): equal=348 missing=0 differ=1 of 349 -- the one di
- 20260930T164728Z CLOSED -- all 4 legs proven
