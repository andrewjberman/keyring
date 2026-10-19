# Deploy Completion Record
**Date opened:** 2026-10-18T00:51:12.890476+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261019T131038Z
**Deploy:** ETFS_RIVALS order 3 act 3: the held-tr + re-source layer (256 objects, site Z C:/opal-elev/rvht1) published to live G4 security_market under the never-widen pair
**Authored by:** 2.0.0_SA_COO~RV
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 72.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | CTO half condition 1: heldtr_stage.py readers on the layer (dramatic_move new-on-layer-date 0; price_series per-fund counts printed) | the readers VERDICT line + per-fund table, run at site Z | readers at site Z, true python exit 0 (unpiped), reproduced on a second run: 'VERDICT: no new dramatic_move candidate on a held-tr date'; day 2026-10-16 \| layer dates 254 \| dramatic_move candidates A 1 B 0 \| new in B 0 \| gone in B 1 \| NEW ON A LAYER DATE (STOP) 0. Per-fund counts printed for all 13 funds (market/implied/none/bigmove A->B); bigmove falls 1->0 in BASG, GQGU, IDVZ, PCLG, PFOE, TSEL. | CLOSED 20261018T012008Z |
| L2 | activation | heldtr_stage.py publish dry run then --apply at site Z (256 new, 0 present-and-different; each object read back) | the publish summary lines | publish at site Z: dry run exit 0 'objects in layer 256 \| new 256 \| present-and-equal 0 \| present-and-different 0', 256 PLAN lines all on s3://opal-data-etfs/rivalfunds/etfs/gold/security_market/date=, no DIFF/REFUSED in 258 lines; then --apply exit 0 'objects in layer 256 \| written 256 \| skipped (exist) 0 \| apply True' with read-back. INDEPENDENT verification: live G4 object count 266 -> 522 (+256 exactly); 992 HK Equity through hc.g4_rows on live S3 reads the TRUE close on 2026-10-12/13/14/15 (32.34, 31.10, 30.40, 25.98) as_of_source held-tr, and drop_backfill KEEPS them so the rankings see them. | CLOSED 20261018T012008Z |
| L3 | verify | the next page build reads the published objects (holding_contribution implied days fall as act 2 measured) | the next publish's price_source counts | read by 2.0.0_SA_COO~RV 2026-10-19 13:2xZ from live S3 (security-axis rows of holding_contribution date=2026-10-16, 5,511 rows each): before the publish (10-17T11:11Z build) price_source g4_tri 1074 / mixed 3630 / holding_implied 735 / missing 72, sum n_days_holding_implied 339,486; first build after the 2026-10-18 01:20Z publish (10-18T11:07Z, holding_contribution-20261018T110712Z-915751cd0ea4) g4_tri 3505 / mixed 1776 / holding_implied 181 / missing 49, implied days 23,840; the 10-19T11:04Z build reads identical to it. Implied days fall as act 2 measured. | CLOSED 20261019T131038Z |

## Log

- 20261018T005112Z OPENED by 2.0.0_SA_COO~RV with 3 leg(s)
- 20261018T012008Z LEG L1 closed: readers at site Z, true python exit 0 (unpiped), reproduced on a second run: 'VERDICT: no new dramatic_move candidate on
- 20261018T012008Z LEG L2 closed: publish at site Z: dry run exit 0 'objects in layer 256 | new 256 | present-and-equal 0 | present-and-different 0', 256 
- 20261019T131038Z LEG L3 closed: read by 2.0.0_SA_COO~RV 2026-10-19 13:2xZ from live S3 (security-axis rows of holding_contribution date=2026-10-16, 5,51
- 20261019T131038Z CLOSED -- all 3 legs proven
