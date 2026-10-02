# MDPF_SECCLASS -- `multi_asset` (CTO batch 164): the reader census and the readers packet's scope

By `2.0.0_SA_COO~M`, 2026-10-02 12:5xZ. Batch 164: readers first, as one packet; rows after PROD readers.

## The census

`R8_CHECKS/r8_multi_asset_reader_census.py` runs the round-6 reader census (`R6_CHECKS/r6_model_reader_census.py`: every reader of
`etf-classifications` through its real function on an in-memory table double, no AWS call) with nine `multi_asset` rows (AOR, VSMGX,
VTHRX, VTIVX, VWELX, ABALX, AAETX, MDLOX, KAGIX; Target Date, Fixed Mix, Flexible; `classified_by: seed`). Result
(`R8_CHECKS/R8_MULTI_ASSET_READER_CENSUS_20261002.json`): **36 readers -- 17 tolerate, 8 read-only, 2 crash, 9 fail a contract.**

| verdict | reader | real for `multi_asset`? |
|---|---|---|
| CRASHES | `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` (`classify_security`) | **REAL** -- `REFUSED: the canonical table returned 'multi_asset', outside the admitted asset_class enum` (`ASSET_CLASS_VALUES`, :847) |
| FAILS-CONTRACT | `portal/src/pages/AdvisorIntelligence/_shared/lib/composition.ts` | **REAL** -- `multi_asset` outside the portal's `CANONICAL_CLASSES` (read at the workspace's portal pin) |
| FAILS-CONTRACT x3 | the shared client and its two Lambda copies | harness only -- "model attributes lost" (a model-row check; these rows are seed) |
| FAILS-CONTRACT | positioning Lambda | harness only -- "management style default" (the model-row expectation) |
| FAILS-CONTRACT | `build_satellites_characteristics.py` | harness only -- the model-row identity check |
| FAILS-CONTRACT | `label-legacy-classified-by.py`, `seed-etf-constituents.py` | harness only -- "model label / model row changed" |
| CRASHES | `write-model-rows.py` | harness only -- `KeyError: 'classification_confidence'` in the census's own model-writer exercise |
| FAILS-CONTRACT | `comparison_catalogue.py` | harness only -- the CTO round-6 model-name rule; seed rows are offered by design |
| UNCENSUSED | `data/cot/scripts/gold/lib/etf_classifier.py` | a reader added after the census was cut (Cottonwood's ruled rule, serve-held); to add to READERS |

Also enumerating classes, outside the table census: `docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json` and its
producer copy `infra/aws/lambda/investor-reporting/holdings/contracts/HoldingsSnapshot.schema.json` -- `asset_class` enums at
`nodes[]`, `security_aggregates[]`, `class_totals[]` (equity, fixed_income, alternatives, structured, commodities, cash, other,
unclassified). The classification contract (`org/standards/MDPF_SECCLASS_CONTRACT.json`) carries no asset_class enum.

## The readers packet (one packet, batch 164), by owner

| change | files | owner |
|---|---|---|
| Holdings producer admits `multi_asset` | `holdings_snapshot.py` `ASSET_CLASS_VALUES`; both `HoldingsSnapshot.schema.json` copies (three enums each); the producer's tests | `2.0.0_SA_COO~M` (IRPT_BCKEND ~M) |
| Investor Reporting Holdings tab renders it | the IR portal page's class label and colour maps | `2.0.0_SA_COO~D` (DSGN_IRPTV1 lease) |
| Advisor Intelligence readers render it | `composition.ts` `CANONICAL_CLASSES` and the batch-99 reader set (on DEV at eb90f2ad), `chartColors.ts` | `2.0.0_SA_COO~M` (readers), `2.0.0_SA_COO~D` (colour) |
| the census covers Cottonwood's classifier | `r6_model_reader_census.py` READERS | `2.0.0_SA_COO~M` |
| Black Diamond's and Cottonwood's mix lists (nine classes) | `MIX_ASSET_CLASSES` x2 + comp-constants | after the re-land and re-point land (batch 164: not riding the signed halves) |

The served move of the packet itself: none (no row carries `multi_asset` until the rows act, which follows PROD readers).
