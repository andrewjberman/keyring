# Deploy Completion Record
**Date opened:** 2026-09-30T16:49:26.520929+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260930T182520Z
**Deploy:** AMGT_CORPUS round 25 CRPS-aa-2 served act: map rebuild (aa-3) + 22-block re-derive (aa-1 label rule) + 21 dossiers (pair COO 5466e66bee / CTO 21f7a96cf6)
**Authored by:** 2.0.0_SA_COO~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| a | activation | PYTHONPATH=<root> build_unit_map.py --population crosswalk on the committed map | 6 fields changed (the named 6), 0 shared, 0 top-level, 0 added | PYTHONPATH=<root> build_unit_map.py --population crosswalk rc 0 at 3d5235be21; diff vs pre-image: entries_changed 6 fields_touched 6 (BEST_EPS BEST_PE_RATIO BOOK_VAL_PER_SH BS_TOTAL_LIABILITIES CURR_ENTP_VAL REVENUE_PER_SH) shared_changed 0 securities_added [] top_level_changed 0 lf_only True = the stated line | CLOSED 20260930T165332Z |
| b | git | field_map.json commit | commit hash | field_map.json committed d66497aec3 (working copy == HEAD after commit) | CLOSED 20260930T165407Z |
| c | activation | model_block_pull derive --no-sa-fallback over the 22 (3 per call) | 22 stamps; per-block unit/sign/currency = m3 lines; 0 value/case/measured-to-other; label moves header only; 0 sign contradicts; filled_by_sa 0 | derive --no-sa-fallback over the 22 in 8 calls (<=3 each) at map d66497aec3, rc 0 x8, 22 stamps, 0 ERROR; c25_verify vs recorded predecessors: blocks_matching 22/22, unit 38/38, sign 38/38, currency 53/53, value 0, case 0, other 0, measured_to_other 0, label_moves_outside_header 0, sign_contradicts_value 0, filled_by_sa 0; derive vintage stamp on 7753 figures counted separately (evidence/r25_leg_c_verify.txt) | CLOSED 20260930T165838Z |
| d | activation | dossier write_one over the 21 (named script, python -u) | 21 puts; exactly one new per name; changed keys model_rows/inputs/content_sha256; inputs_equal_now 21/21 | 17:01-18:0xZ d25.py write (named script, python -u; PID 49000 by CreationDate): 21 wrote, 0 unchanged, 0 errors; S3 structure since 17:01:05Z: exactly one new object 21/21, 0 other names, changed keys fields.model_rows + inputs + content_sha256 only; inputs_equal_now 21/21 (evidence/r25_leg_d{,_structure,_inputs}.txt) | CLOSED 20260930T182520Z |
| v | verify | aa3_check measured_before 11 + served /thesis TSM (CUR_MKT_CAP USD, NET_DEBT no currency) + BA_US CUR_MKT_CAP label unchanged | as stated | aa3_check over the 98 keys: measured_before 11 (49 -> 11); served read 17:04Z: deployed opal-amgt-scoped-api CodeSha256 /QP4upEVzTjnHV2bAeIXIud0k0DgjDDGrlMgtm0uo7o= (15:22:01Z) /thesis TSM_US_Equity CUR_MKT_CAP 2339877750964.95 USD quote (CRNCY), NET_DEBT currency None (UNMEASURED:); negative arm BA_US_Equity CUR_MKT_CAP USD reporting = its recorded predecessor label (evidence/r25_leg_v_{census,served_read}.txt, r25_ba_before.txt) | CLOSED 20260930T182520Z |

## Log

- 20260930T164926Z OPENED by 2.0.0_SA_COO~X with 5 leg(s)
- 20260930T165332Z LEG a closed: PYTHONPATH=<root> build_unit_map.py --population crosswalk rc 0 at 3d5235be21; diff vs pre-image: entries_changed 6 fiel
- 20260930T165407Z LEG b closed: field_map.json committed d66497aec3 (working copy == HEAD after commit)
- 20260930T165838Z LEG c closed: derive --no-sa-fallback over the 22 in 8 calls (<=3 each) at map d66497aec3, rc 0 x8, 22 stamps, 0 ERROR; c25_verify vs 
- 20260930T182520Z LEG d closed: 17:01-18:0xZ d25.py write (named script, python -u; PID 49000 by CreationDate): 21 wrote, 0 unchanged, 0 errors; S3 stru
- 20260930T182520Z LEG v closed: aa3_check over the 98 keys: measured_before 11 (49 -> 11); served read 17:04Z: deployed opal-amgt-scoped-api CodeSha256 
- 20260930T182520Z CLOSED -- all 5 legs proven
