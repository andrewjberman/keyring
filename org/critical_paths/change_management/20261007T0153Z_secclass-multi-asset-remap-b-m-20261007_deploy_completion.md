# Deploy Completion Record
**Date opened:** 2026-10-07T01:53:50.095679+00:00
**Status:** HELD-SOVEREIGN-GATED -- gate: sovereign / Andrew limit item 5: TO-SC-e67 (COT D_04 no multi_asset) held line q/dell1/secclass-r12-held-e67/r1 @a5ce0efab3; row MDPF_SECCLASS-S60. Measured 2026-10-09 00:1xZ by 2.0.0_SA_COO~M1: opal-data-cot listed=1153 hit_keys=2 post_switch=2 (z09305621, z09305679 concentration.json @2026-10-08T11:36Z), record MDPF_SECCLASS_M/SERVED_MULTI_ASSET_SPLIT_COT_20261009T00Z.json. Table rows (leg S) and IRPT holdings (leg H) are correct; no rollback. BD half reads at the 2026-10-08 23:00Z fire with secclass-e75 leg G. (held since 2026-10-09T00:09:51.088023+00:00)
**Deploy:** MDPF_SECCLASS: the 33 multi_asset etf-classifications rows remapped into the six classes by Andrew's rule B (no multi-asset class); conditional compare-and-set updates with a pre-state snapshot; halves COO + CTO
**Authored by:** 2.0.0_SA_COO~M
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S | verify | 33 rows written; consistent readback of each (class, sub-class, updated_by); a table scan reads zero multi_asset rows | readback and scan | 2026-10-07 ~07:15Z remap_multi_asset_rows_b.py --write: WROTE 33 of 33, condition failures 0; snapshot MULTI_ASSET_REMAP_B_ROLLBACK_20261007T0715Z.json (33 rows). Readback (consistent get per row): ALREADY 33, MOVE 0, REFUSED 0. Full consistent scan of etf-classifications: 3507 rows (3507 before), 0 multi_asset (CTO condition 2), 33 rows updated_by mdpf-secclass-remap-b = equity 25 + fixed_income 8, 5 with sub-class, 28 low_confidence | CLOSED 20261007T071015Z |
| H | verify | the next IRPT holdings build per firm (cottonwood, inflection, 49financial) reads the remapped nodes as equity or fixed_income, none as multi_asset | served platinum reads | 2026-10-08 ~18:05Z, 2.0.0_SA_COO~M1: e62e56_post_fire_read.py read over the served irpt holdings publications business_date 2026-10-07 for all three firms: 49financial rev 61537f666d00, inflection rev efe113f13183, cottonwood rev 8982ba981eb8 -- multi_asset check True and six_class check True on each (0 multi_asset nodes, 0 classes outside the six). Record MDPF_SECCLASS_M/LEG_H_SERVED_HOLDINGS_READ_20261008T1805Z.json. | CLOSED 20261008T180919Z |
| G | verify | the next Cottonwood and Black Diamond gold runs read: the four Cottonwood clients sum to 1, both firms' firm_composition gaps close | served reads |  | OPEN |

## Log

- 20261007T015350Z OPENED by 2.0.0_SA_COO~M with 3 leg(s)
- 20261007T071015Z LEG S closed: 2026-10-07 ~07:15Z remap_multi_asset_rows_b.py --write: WROTE 33 of 33, condition failures 0; snapshot MULTI_ASSET_REMAP
- 20261008T180919Z LEG H closed: 2026-10-08 ~18:05Z, 2.0.0_SA_COO~M1: e62e56_post_fire_read.py read over the served irpt holdings publications business_d
- 20261009T000951Z HELD-SOVEREIGN-GATED gate=sovereign/Andrew limit item 5: TO-SC-e67 (COT D_04 no multi_asset) held line q/dell1/seccl
