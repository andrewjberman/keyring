# Deploy Completion Record
**Date opened:** 2026-10-18T00:51:12.890476+00:00
**Status:** OPEN
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
| L3 | verify | the next page build reads the published objects (holding_contribution implied days fall as act 2 measured) | the next publish's price_source counts |  | OPEN |

## Log

- 20261018T005112Z OPENED by 2.0.0_SA_COO~RV with 3 leg(s)
- 20261018T012008Z LEG L1 closed: readers at site Z, true python exit 0 (unpiped), reproduced on a second run: 'VERDICT: no new dramatic_move candidate on
- 20261018T012008Z LEG L2 closed: publish at site Z: dry run exit 0 'objects in layer 256 | new 256 | present-and-equal 0 | present-and-different 0', 256 
