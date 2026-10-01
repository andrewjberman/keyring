# Deploy Completion Record
**Date opened:** 2026-10-01T11:01:29.412035+00:00
**Status:** OPEN
**Deploy:** MDPF_SECCLASS item 9: 13 new model rows in etf-classifications by write-model-rows.py --write over MODEL_ROWS_WRITE_SET_20261001.txt (set a: AMUSX BAGIX BAGSX BSIIX DODIX EMXC FXNAX IGSB JEMSX; set b: USRT CSRSX VCMDX PFUNX); conditional put only, no overwrite, no delete; halves COO @eae4fbeb14 + CTO SIGNED FOR 13 ROWS @000b55fc4b (CAIBX excluded); rollback is a seed row per ticker. Black Diamond gold, restated for SIX held tickers (CTO half item 5): BAGIX, BSIIX, DODIX, EMXC, IGSB, USRT, 57 open lots, 518,062.80 USD, move from other to a class on C_06 / D_03 / D_04 at the next gold run (the seven-ticker figure 976,963.75 USD included CAIBX, 42 lots, 458,900.95 USD)
**Authored by:** 2.0.0_SA_COO~M
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 30.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P | verify | the two stops read immediately before the write: census prints MODEL-READER-TOLERATED; writer dry run reads named=13 plan=13 already_present=0 refused=0 | census line + dry-run line, UTC-stamped | Read immediately before the write: reader census 11:01Z prints readers=36 tolerates=27 read_only=9 crashes=0 refuses=0 fails_contract=0 and MODEL-READER-TOLERATED (record R7_MODEL_READER_CENSUS_20261001_1100Z.json; the 10:55Z run had WITHHELD the verdict on UNCENSUSED write-model-rows.py, fixed by exercising the writer as a reader @c16bba2af4). Writer dry run 11:04:58Z: MODEL-ROWS named=13 plan=13 already_present=0 refused=0 (census candidates=26, table rows=2658). Writer and shared-put blobs equal CLOUD's. | CLOSED 20261001T110814Z |
| W | verify | the write and its readback: 13 rows classified_by model each with both model fields; table count 2,671; second dry run plan=0 already_present=13 | writer output + scan | write-model-rows.py --tickers-file MODEL_ROWS_WRITE_SET_20261001.txt --write, 11:05Z: WRITTEN 13 of 13: AMUSX BAGIX BAGSX BSIIX DODIX EMXC FXNAX IGSB JEMSX USRT CSRSX VCMDX PFUNX, rc 0. Readback 11:07Z (consistent scan): table rows 2,671 (2,658 before); classified_by scheduled 2,281, legacy 238, seed 139, model 13; all 13 model rows carry classification_confidence and low_confidence false, updated_by mdpf-secclass-model, no name attribute, class and sub class as planned. Second dry run: named=13 plan=0 already_present=13 refused=0. No item was overwritten or deleted. | CLOSED 20261001T110814Z |
| H | verify | next irpt-holdings-snapshot publication serves the moves of addendum 2 on one selection per firm | page or served-slice read | Served-slice read of the three firms' publications written 2026-10-01 14:18Z-14:21Z (business date 2026-09-30), every security node, all with class basis TABLE. Inflection, set (b) class moves served: USRT 411 nodes 660,867.45 USD and CSRSX 1 node 1,054.79 USD alternatives / Real Estate; VCMDX 1 node 3,887.47 USD commodities / Commodities; PFUNX 139 nodes 0.00 USD fixed_income / International. Set (a) sub class moves served: Inflection BAGIX, BSIIX, DODIX, FXNAX, AMUSX, BAGSX Intermediate and EMXC, JEMSX EM (947,407.72 USD with a value); Cottonwood FXNAX Intermediate, IGSB Short Duration, EMXC EM (4,676,307.39 USD); 49 Financial BAGIX, DODIX Intermediate, IGSB Short Duration, JEMSX EM (28,993.14 USD). CAIBX, excluded from the act, is unchanged at fixed_income / Investment Grade (49 Financial 323,820.02 USD). Node counts and dollars differ from the half's table because that table was the 2026-09-28 business date. Page: one Cottonwood selection walked 14:45Z-14:57Z, 469 of 469 served aggregates equal the page fold. | CLOSED 20261001T151826Z |
| G | verify | next scheduled Black Diamond gold fire reads the six held tickers with class_source etf-classifications | log or served artifact read |  | OPEN |

## Log

- 20261001T110129Z OPENED by 2.0.0_SA_COO~M with 4 leg(s)
- 20261001T110814Z LEG P closed: Read immediately before the write: reader census 11:01Z prints readers=36 tolerates=27 read_only=9 crashes=0 refuses=0 f
- 20261001T110814Z LEG W closed: write-model-rows.py --tickers-file MODEL_ROWS_WRITE_SET_20261001.txt --write, 11:05Z: WRITTEN 13 of 13: AMUSX BAGIX BAGS
- 20261001T151826Z LEG H closed: Served-slice read of the three firms' publications written 2026-10-01 14:18Z-14:21Z (business date 2026-09-30), every se
- 20261001T154800Z CORRECTION to leg H's proof by 2.0.0_SA_COO~M: its last-but-one sentence gave the business date as the reason Inflection's node counts and dollars are below the half's table (USRT 411 nodes against 466). That reason was not measured. Measured since (row IRPT_BCKEND-S259): today's Inflection publication lists no position rows for 91 of 884 accounts (49.98 million USD) under the producer's split-account rule, so the tickers' rows on those accounts are absent, not reclassified. Every USRT, CSRSX, VCMDX and PFUNX row that IS served reads the model row's class; the leg's verdict stands on that.
