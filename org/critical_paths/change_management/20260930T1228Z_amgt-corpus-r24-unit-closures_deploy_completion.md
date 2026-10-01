# Deploy Completion Record
**Date opened:** 2026-09-30T12:28:11.736090+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260930T141652Z
**Deploy:** AMGT_CORPUS round 24 CRPS-z-1 served act: map rebuild + 28-block re-derive + 27 dossiers (pair COO ab84e2b6df / CTO 4acf8806ce)
**Authored by:** 2.0.0_SA_COO~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| a | activation | PYTHONPATH=<root> build_unit_map.py --population crosswalk on the committed map | 84 entries, 10 fields, 0 shared, 0 top-level, 0 added | 12:29:48Z PYTHONPATH=<root> build_unit_map.py --population crosswalk at a974d07eb1 rc 0 (crosswalk 2026-09-29.json, 237 keyed); diff vs pre-image: entries_changed 84 fields_touched 10 (BEST_BPS BEST_DIV_YLD BEST_DPS BEST_SALES BS_CASH_NEAR_CASH_ITEM BS_TOTAL_LIABILITIES CURR_ENTP_VAL EQY_DPS IS_DIV_PER_SHR SALES_REV_TURN) shared_changed 0 securities_added 0 top_level_changed 0 lf_only True = the stated line | CLOSED 20260930T123213Z |
| b | git | field_map.json commit | commit hash | field_map.json committed 6caac02338 (working copy == HEAD after commit) | CLOSED 20260930T123830Z |
| c | activation | model_block_pull derive --no-sa-fallback over the 28 (3 per call) | 28 new stamps; per-block unit+sign counts = m2 BLOCK lines; 0 value/case moves; 0 measured-to-other; 0 sign contradicts value; filled_by_sa 0 | 12:39-12:40Z derive --no-sa-fallback over the 28 in 10 calls (<=3 each) at a974d07eb1+map 6caac02338, rc 0 x10, 28 stamps; c_verify vs recorded predecessors: blocks_matching 28/28, unit_changes 565 = expected 565, sign_changes 115 = expected 115, value 0, case 0, other 0, measured_to_other 0, sign_contradicts_value 0, filled_by_sa 0, held_off 9; the derive vintage stamp moved on 10083 figures + cases.base.px_last.vintage on 26 blocks (a derive timestamp, not content; first verify run counted it as other/case, diagnosed field-by-field, excluded and counted) (evidence/r24_leg_c_verify{,2}.txt) | CLOSED 20260930T124425Z |
| d | activation | dossier write_one over the 27 | 27 puts; inputs_equal_now True; other_moves 0 outside model_rows | 12:44-13:39Z write_one over the 27 (6861 JP has no dossier): first writer (python -, PID 21416) outlived its 30-min harness kill and overlapped the 13:27Z continuation (4 wrote, 3 unchanged, 0 errors) -- idempotent never-overwrite puts; S3 read: exactly one new object per name 27/27, 0 other names written, changed document keys fields.model_rows + inputs + content_sha256 only, inputs_equal_now 27/27 (evidence/r24_leg_d_{structure,inputs}.txt, r24_leg_d2.txt) | CLOSED 20260930T141652Z |
| v | verify | z1 census remaining + served /thesis read on 8306 JP (current deployed build) | remaining 49; served route shows the new stamp's label | served census (z1_check over the 98 non-excluded blocks): not-measured 602 -> 49 = pair; CTO condition 3 served read 13:33Z: deployed opal-amgt-scoped-api CodeSha256 nKWCfQRQ3/lL6cJxgYG3dZr0tcVdOBheeMMNaoWQE+w= (LastModified 11:43:22Z, ab-6 build) /thesis 8306_JP_Equity status 200: 36/36 moved figures show the new label (e.g. SALES_REV_TURN/BS_CASH_NEAR_CASH_ITEM/BS_TOTAL_LIABILITIES MILLIONS), 0 show the predecessor's UNRESOLVED (evidence/r24_leg_v_served_read.txt) | CLOSED 20260930T141652Z |

## Log

- 20260930T122811Z OPENED by 2.0.0_SA_COO~X with 5 leg(s)
- 20260930T123213Z LEG a closed: 12:29:48Z PYTHONPATH=<root> build_unit_map.py --population crosswalk at a974d07eb1 rc 0 (crosswalk 2026-09-29.json, 237 
- 20260930T123830Z LEG b closed: field_map.json committed 6caac02338 (working copy == HEAD after commit)
- 20260930T124425Z LEG c closed: 12:39-12:40Z derive --no-sa-fallback over the 28 in 10 calls (<=3 each) at a974d07eb1+map 6caac02338, rc 0 x10, 28 stamp
- 20260930T141652Z LEG d closed: 12:44-13:39Z write_one over the 27 (6861 JP has no dossier): first writer (python -, PID 21416) outlived its 30-min harn
- 20260930T141652Z LEG v closed: served census (z1_check over the 98 non-excluded blocks): not-measured 602 -> 49 = pair; CTO condition 3 served read 13:
- 20260930T141652Z CLOSED -- all 5 legs proven
