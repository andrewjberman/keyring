# Leg V, 49financial -- the served 2026-10-06 14:15Z fire (acceptance of CTO batches 266 and 281's leg V)

**Author:** `2.0.0_SA_COO~M`, 2026-10-06 ~14:3xZ. **Claim:** measured (served platinum, all 188 of 188 parts streamed, 8 shards, the deployed reader's own bytes).
Result file: `MULTI_ASSET_LEG_V_49financial_20261005.json` (overwritten by the merge; the 2026-10-05 pre-fire read is in git @b218075200).

## Result

- **Manifest:** `current/manifest.json` LastModified 2026-10-06T14:20:48Z; revision `94ad27048e21...`; business date 2026-10-05.
- **Packet nodes by class:** `multi_asset` 35, `unclassified` 0 (the pre-fire read, revision f8bf8dcb53cd, read multi_asset 25 and unclassified 9).
- **S27:** key 808516306 (symbol SCGB1) reads `multi_asset` on 9 of 9 nodes ($175,356.90), as the local dry build predicted.
- **Totals:** `reconciled=True`; the packet's multi_asset amount is $2,515,601.18.
- **Reader:** deployed `irpt-holdings`, valid against the contract schema, reconciled, admits `multi_asset`, class totals carry it.

## Named swaps (CTO batch 282 duty)

49financial, from the FWD-10 first fire (row S28): BG (1 account) `Developed` -> `Consumer Staples`, TABLE; NBIS (1) none -> `Information Technology`,
TABLE (no label lost). BKD is held at inflection, and cottonwood's BG (2 accounts) is held there: those two firms' builds were NOT read in this leg.

## Caveat

- `reader_pin_t=False`: the deployed `irpt-holdings` code is `SRANzIGz...`, last modified 2026-10-06T01:44:23Z, not pin T (`RmruvCeo...`, read 2026-10-05).
  Someone redeployed it after the earlier reads. Not established here: what changed or who. The new bytes pass the three reader checks above.
- The paired pre/post account-total comparison was not repeated (`--no-pre`); the evidence for "totals unchanged" is the reconcile flag and the
  2026-10-04 served-effect read (153,291 of 153,291 nodes equal).
