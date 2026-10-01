# NEVER-WIDEN HALF REQUEST -- MDPF_SECCLASS FWD-7/FWD-4 model-path first write (SC-e-10)

**Requesting seat:** `0.9.0_WK_MDPF_SECCLASS~8` (worker of `2.0.0_SA_COO~M`), task order `MDPF_SECCLASS.TO-SC-e10`.
**For:** the CTO+COO never-widen sign-off on the FIRST real write of `etf-classifications` rows under the `model`
path (PRD `org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md`, C-WRITER, C-SERVED; contract 0.3.0's new
`classified_by = model`, `classification_confidence`, `low_confidence` fields). This build itself performs NO such
write (WORLD-risk build bound: a real Kimi K3 run was authorised, a table write was not); every number below is
measured from the real, live census, `R4_MODEL_CLASSIFY_CENSUS_20260930.json` (generated 2026-09-30, real
DynamoDB + Kimi K3 reads, `table_rows_at_build` 2309, `overwrites` 0 by construction -- this runner never imports
or calls anything with PutItem/UpdateItem authority).

## The act

For each RESIDUAL entry (E8's `R2_UNRESOLVED_REVIEW_20260930.json`, every entry with no `proposed_class`, 357 at
this build) that (a) carries a ticker (a keyed candidate) AND (b) the model resolved to a non-null `asset_class`,
write ONE row to `etf-classifications` via a conditional put, `ConditionExpression=attribute_not_exists(ticker)`,
setting `classified_by = "model"`, `classification_confidence = <the model's own confidence>`,
`low_confidence = (confidence < 0.80)`, plus `asset_class`/`sub_asset_class` and `name`. Exactly like `scheduled`
and `constituents`, this write lands ONLY where no row exists -- an existing ticker is never touched, and this
act never re-derives the plan at write time; it replays the reviewed candidate list below verbatim.

**Measured scope (`R4_MODEL_CLASSIFY_CENSUS_20260930.json`, this build, real Kimi K3 calls against a real prompt
carrying ONLY name+ticker):**

| | count |
|---|---|
| Residual entries (the census's own denominator) | 357 |
| Keyed (carries a ticker) | 41 |
| CUSIP-only (a 9-character CUSIP-shaped identifier, no ticker) | 8 |
| Name-only (neither a ticker nor a CUSIP shape) | 308 |
| `would_write` (the census's own definition: a keyed result whose ticker has NO live row today) | 41 |
| Of the 41 keyed: model resolved a non-null `asset_class` -- **the real candidate row set this act writes** | 26 |
| Of the 41 keyed: model returned `asset_class = null` (7 transport `KIMI_TIMEOUT` refusals, 8 self-declared "no reliable signal" refusals, e.g. a bare ticker `ARTS`/`UCON` or a fund name that IS the ticker) -- **NOT part of this act; no row to write for these 15 until re-run or otherwise resolved** | 15 |
| Of the 26 candidate rows: `low_confidence = true` (confidence < 0.80) -- **the flagged count**, written exactly like any other model row per Andrew's standing word (no human review, no withheld write) | 11 |
| Of the 26 candidate rows: `low_confidence = false` | 15 |
| Candidate rows by `asset_class` | fixed_income 13, equity 7, alternatives 4, commodities 2 |
| Overwrites (structural: this act's conditional-put never touches an existing row) | 0 |

Full candidate list (ticker, asset_class, confidence, flagged): BAGIX fixed_income 0.85 -, USRT alternatives 0.85 -,
FBIIX fixed_income 0.72 FLAGGED, RLY alternatives 0.42 FLAGGED, BSIIX fixed_income 0.85 -, DODIX fixed_income 0.90 -,
FXNAX fixed_income 0.95 -, BAGSX fixed_income 0.88 -, PZTRX fixed_income 0.55 FLAGGED, JEMSX equity 0.80 -, MLPTX
equity 0.60 FLAGGED, FFFHX equity 0.72 FLAGGED, BSBSX fixed_income 0.78 FLAGGED, PHLPX fixed_income 0.60 FLAGGED,
EMXC equity 0.95 -, PFUNX fixed_income 0.82 -, FOCSX equity 0.70 FLAGGED, BSBIX fixed_income 0.75 FLAGGED, TMAAX
equity 0.60 FLAGGED, AMUSX fixed_income 0.82 -, CAIBX equity 0.85 -, O alternatives 0.80 -, PCOFX commodities 0.65
FLAGGED, IGSB fixed_income 0.92 -, CSRSX alternatives 0.80 -, VCMDX commodities 0.85 -. The exact same 26 rows,
byte-identical, are `R4_MODEL_CLASSIFY_CENSUS_20260930.json`'s `results[]` filtered to `key` set and `asset_class`
not null -- this half names no candidate the census does not also carry.

## Blast radius

- **The rows.** Exactly the 26 tickers named above. Zero existing rows are touched: `overwrites: 0` in the census,
  structurally -- this runner (`classify-residual-model.py`) never imports `etf_classification_scheduled.write()`
  or issues any PutItem/UpdateItem itself; there is no `--write` flag. The 15 null-class keyed tickers (FSRNX,
  UCON, PHNNX, ZVZZT, PFONX, BTMSX, ARTS, CAIFX, CSIBX, FDKVX, BIICX, TRRBX, SGIIX, FSKGX, FPURX) are NOT in scope
  of this act -- writing a row with no resolved `asset_class` is not a row this table's own schema supports
  (`asset_class` is not nullable on a written row), so they stay unresolved until a re-run, a different input, or
  a human correction resolves them; they are named here for completeness, not as candidates.
- **Every reader of `classified_by`.**
  - `label-legacy-classified-by.py`'s `plan_unlabelled()` (`infra/aws/lambda/v2_portal/yang_pipeline/label-legacy-classified-by.py:74-77`,
    `attribute_not_exists(classified_by)`-guarded scan): a model row already carries `classified_by`, so this
    reader correctly EXCLUDES it from the legacy-label population the same way it already excludes seed/scheduled/
    constituents rows -- zero code change needed there, confirmed by the field's own presence check, not by name.
  - `etf_classifications_dynamodb.ETFClassifier.find_by_asset_class`/`find_by_sub_asset_class`
    (`infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py:116-158`): measured, per the prior
    backfill half (`NEVER_WIDEN_HALF_REQUEST_SECCLASS_BACKFILL_20260929.md`), at ZERO functional call sites across
    all three copies of this client -- unchanged by this act; the 26 new rows grow the result set any FUTURE
    caller would see, from that point on.
  - `seed-etf-classifications.py` (`infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py:122`)
    writes `classified_by = "seed"` UNCONDITIONALLY on every ticker in its own module list -- it does not read the
    existing value before writing, so a seed row always wins over a model row exactly as it already does over
    scheduled/constituents/legacy (contract 0.3.0 `classified_by.precedence`). None of these 26 tickers is in the
    seed module's list today (`ETF_CLASSIFICATIONS`/`ETF_SUB_ASSET_CLASS` in `etf_classification.py`) -- confirmed
    by their presence as UNRESOLVED in E8's round-2 review in the first place (a seed-source ticker is never
    reviewed as residual; see `etf_classification_scheduled.plan_rows`'s own `seed_pending` exclusion).
  - `etf_classification_scheduled.py`'s own writers (`plan_rows`/`write`) never read `classified_by`; they read
    `existing_tickers()` (ticker presence only), so they are unaffected structurally, and a scheduled write is
    itself conditional on ticker-absence, so it could never re-touch one of these 26 rows once written.
  - No FWD-2/Positioning surface reads `classified_by` itself (it is provenance metadata, not a served class
    value) -- readers of `asset_class`/`sub_asset_class` on these 26 tickers see a real class where they
    previously saw none (FWD-2's own unclassified-by-name bar), the same "both branches" shape as the FWD-7
    backfill half.
- **`classification_confidence` / `low_confidence` readers.** Zero today (new fields, contract 0.3.0, this
  commit) -- a repo-wide word-boundary census of both tokens outside this cell's own new files (`etf_classification_model.py`,
  `classify-residual-model.py`, `test_model_classifier.py`, the contract) reads zero hits in
  `infra/aws/lambda/v2_portal`, `data/**/*.py` and `portal/src` (contract `rule24_record.token_census`). No reader
  changes behavior from these two fields existing on a row.
- **The 15 unresolved-by-the-model tickers and the 308 name-only + 8 CUSIP-only residual entries.** Named here,
  never written, and HELD FOR THE ROUND ANALYSIS: the name-only and CUSIP-only entries have no key in this order
  (no ticker to conditional-put on) -- E9's `CUSIP:<9>`-prefixed key is the eventual home for the 8 CUSIP-shaped
  ones, still unwired as a live writer at this build; the 308 name-only entries have no path to a table row at
  all under this table's own ticker-keyed schema, and stay exactly where E8 left them (unresolved, by name, with a
  reason) unless a future cell finds them a different identifier.
- **IAM (DESIRED, NOT APPLIED).** This act needs the SAME PutItem-on-`etf-classifications` grant the FWD-7
  backfill already requires for its own principal (whichever principal runs `classify-residual-model.py` on a
  schedule); no NEW IAM surface beyond that is implied by the model path specifically.

## Rollback per key

Delete exactly the 26 rows with `classified_by = "model"` AND `ticker` in the candidate list above, one
`DeleteItem` per ticker, never a table-wide delete or scan-and-filter -- the key list is
`R4_MODEL_CLASSIFY_CENSUS_20260930.json`'s `results[]` filtered to `key` set and `asset_class` not null, the exact
26-row set this half names. No pre-existing row is ever touched by the write (structural, per the conditional-put
guard and the `overwrites: 0` census field), so no existing row ever needs restoring as part of this rollback.

## Known gaps, not widened here

- The 15 keyed-but-null tickers (7 `KIMI_TIMEOUT`, 8 self-declared low-signal refusals) are not retried within
  this order; a re-run (same runner, `--limit`-free, against just the residual tickers still unresolved) is a
  cheap follow-up for a later cell, not this act.
- `instrument_kind` and `industry` are not attempted by this model path (out of the standing word's scope: name
  and ticker only) -- absent on every model row, same as on every scheduled row (FWD-8's own known gap, carried
  forward, not reopened here).
- The 308 name-only and 8 CUSIP-only residual entries are outside this act's write surface entirely (no ticker
  key) and are carried to the round-4 analysis as the population FWD-7/FWD-4's next cell, if any, would need a
  different identifier strategy to resolve.

## Reader census (SC-e-15)

Task order `MDPF_SECCLASS.TO-SC-e15`, worker `0.9.0_WK_MDPF_SECCLASS~12`, 2026-09-30. Check: `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R6_CHECKS/r6_model_reader_census.py`; record: `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R6_MODEL_READER_CENSUS_20260930.json`. Every reader of `etf-classifications` is exercised through its real function on the 260 classified results of `R4_MODEL_CLASSIFY_CENSUS_20260930.json` built as `classified_by = "model"` rows (130 flagged `low_confidence`, `classification_confidence` a Decimal as boto3 returns it, classes alternatives 14, commodities 14, equity 155, fixed_income 73, structured 4); only the table is stubbed, nothing is written. Search denominators at build: `comp-find` (corpus=all) `etf-classifications` 5962 hits over 46462 files, `classified_by` 4908 over 46466, `etf_classifications_dynamodb` 440 over 46467; the check's own tracked-tree census and its completeness guard (a tracked code file naming the table that is in neither READERS nor NOT_READERS prints `UNCENSUSED`) are in the JSON `denominator` and `search` keys.

The check's lines, verbatim:

```
Classification not found for ticker: NOSUCHTKR
READER TOLERATES       infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py :: ETFClassifier.get_*/find_by_* (the one client)
READER TOLERATES       infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/etf_classifications_dynamodb.py :: ETFClassifier.get_*/find_by_* (Lambda copy, yang-generate-positioning)
READER TOLERATES       infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-holdings-attribution/etf_classifications_dynamodb.py :: ETFClassifier.get_*/find_by_* (Lambda copy, yang-generate-holdings-attribution)
READER CRASHES         infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py :: ETFClassifier.classify_holdings (static, no call site)
READER CRASHES         infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/etf_classifications_dynamodb.py :: ETFClassifier.classify_holdings (static, no call site; Lambda copy)
READER CRASHES         infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-holdings-attribution/etf_classifications_dynamodb.py :: ETFClassifier.classify_holdings (static, no call site; Lambda copy)
READER TOLERATES       infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py :: resolve_display_name/classify_etf/calculate_allocations/calculate_segment_breakdown
READER TOLERATES       infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-holdings-attribution/lambda_function.py :: resolve_display_name/extract_holdings_for_portfolio
READER TOLERATES       data/etfs/scripts/gold/etf_positioning_publisher.py :: _display_name
READER TOLERATES       data/assets/scripts/gold/build_satellites_registry.py :: load_classifier/classify
READER TOLERATES       data/assets/scripts/gold/build_satellites_characteristics.py :: load_identity
READER TOLERATES       data/black_diamond/scripts/gold/lib/etf_classifier.py :: ETFClassifier.classify/get_sub_asset_class (BD library)
READER TOLERATES       data/black_diamond/scripts/silver/build_bd_assets_dim.py :: apply_blend (BD assets dim)
READER TOLERATES       data/black_diamond/scripts/gold/D_04.client_portal_summary.py :: _classify_with_canonical
READER READ-ONLY       data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py :: BD library consumer (classify/get_sub_asset_class)
READER READ-ONLY       data/black_diamond/scripts/gold/D_03.composition_artifacts.py :: BD library consumer (classify/get_sub_asset_class)
READER TOLERATES       data/assets/scripts/gold/investor_reporting/holdings_snapshot.py :: annotate_classification/classify_security -> HoldingsSnapshot contract
READER TOLERATES       infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py :: TableVocabulary.from_live_table/existing_tickers/plan_rows
READER READ-ONLY       data/black_diamond/scripts/gold/E_18.detect_new_securities.py :: E_18 scheduled caller (BD)
READER READ-ONLY       data/cot/scripts/gold/E_18.detect_new_securities.py :: E_18 scheduled caller (COT)
READER TOLERATES       infra/aws/lambda/v2_portal/yang_pipeline/label-legacy-classified-by.py :: scan_all/plan_unlabelled/label_row_if_unlabelled
READER TOLERATES       infra/aws/lambda/v2_portal/yang_pipeline/set-instrument-kind.py :: scan_all/plan_absent_kind/set_kind_if_absent
READER FAILS-CONTRACT  infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py :: read_existing/merge_item (seed correction of a model row)
READER TOLERATES       infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-constituents.py :: main (--dry-run, --kind-only)/put_row_if_unclassified
READER TOLERATES       data/black_diamond/scripts/classification/seed_canonical_securities.py :: _yang_conflicts
READER TOLERATES       data/black_diamond/scripts/classification/seed_bd_securities.py :: seed (one-time copy into bd-securities)
READER TOLERATES       infra/aws/lambda/v2_portal/yang_pipeline/classify-residual-model.py :: table_rows_at_build/existing_tickers
READER TOLERATES       lib/research/api/scoped_amgt.py :: _join_classification/_classification_for_ticker
READER TOLERATES       lib/research/identity/positioning_chain.py :: read_etf_classifications/resolve_one
READER TOLERATES       infra/aws/lambda/investor-reporting/ycharts/generate/comparison_catalogue.py :: build_catalogue (injected port, unwired)
READER READ-ONLY       infra/aws/lambda/investor-reporting/ycharts/generate/entry.py :: read_comparison_catalogue (delegates to build_catalogue)
READER READ-ONLY       portal/src/pages/AdvisorIntelligence/_shared/lib/composition.ts :: CANONICAL_CLASSES / normalizeMixTo4Class (portal asset-class mapping)
READER READ-ONLY       portal/src/pages/InvestorReporting/contracts/wire/HoldingsSnapshot.ts :: asset_class wire type
READER READ-ONLY       org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md :: IRPT_DASHBD C-CLASSES consumer (PRD only, no code yet)
MODEL-READER-CENSUS readers=34 tolerates=22 read_only=8 crashes=3 refuses=0 fails_contract=1
```

One line per reader (verdict, path, function -- evidence; the full evidence is the JSON `readers[].evidence`):

- `TOLERATES` `infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py` :: ETFClassifier.get_*/find_by_* (the one client) -- 260 model rows through get_classification/get_asset_class/get_sub_asset_class/get_management_style/get_sector verbatim (Decimal confidence and bool flag intact); find_by_asset_class over 5 classes returned all ...
- `TOLERATES` `infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/etf_classifications_dynamodb.py` :: ETFClassifier.get_*/find_by_* (Lambda copy, yang-generate-positioning) -- 260 model rows through get_classification/get_asset_class/get_sub_asset_class/get_management_style/get_sector verbatim (Decimal confidence and bool flag intact); find_by_asset_class over 5 classes returned all ...
- `TOLERATES` `infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-holdings-attribution/etf_classifications_dynamodb.py` :: ETFClassifier.get_*/find_by_* (Lambda copy, yang-generate-holdings-attribution) -- 260 model rows through get_classification/get_asset_class/get_sub_asset_class/get_management_style/get_sector verbatim (Decimal confidence and bool flag intact); find_by_asset_class over 5 classes returned all ...
- `CRASHES` `infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py` :: ETFClassifier.classify_holdings (static, no call site) -- KeyError('alternatives') on model row MDLX009 (asset_class=alternatives): result[asset_class] += weight over a dict seeded with fixed_income/equity/hedge/unknown only. PRE-EXISTING, not caused by the model ...
- `CRASHES` `infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/etf_classifications_dynamodb.py` :: ETFClassifier.classify_holdings (static, no call site; Lambda copy) -- KeyError('alternatives') on model row MDLX009 (asset_class=alternatives): result[asset_class] += weight over a dict seeded with fixed_income/equity/hedge/unknown only. PRE-EXISTING, not caused by the model ...
- `CRASHES` `infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-holdings-attribution/etf_classifications_dynamodb.py` :: ETFClassifier.classify_holdings (static, no call site; Lambda copy) -- KeyError('alternatives') on model row MDLX009 (asset_class=alternatives): result[asset_class] += weight over a dict seeded with fixed_income/equity/hedge/unknown only. PRE-EXISTING, not caused by the model ...
- `TOLERATES` `infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py` :: resolve_display_name/classify_etf/calculate_allocations/calculate_segment_breakdown -- 260 model rows through resolve_display_name/classify_etf/classify_management_style; calculate_allocations over all 5 classes summed to 100.0 with every class present; calculate_segment_breakdown ok; served ...
- `TOLERATES` `infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-holdings-attribution/lambda_function.py` :: resolve_display_name/extract_holdings_for_portfolio -- 260 model rows through resolve_display_name; extract_holdings_for_portfolio over a synthetic attribution sheet of 60 model tickers kept 60 of 60 holdings (none dropped), classes ['Equity', 'Fixed Income', ...
- `TOLERATES` `data/etfs/scripts/gold/etf_positioning_publisher.py` :: _display_name -- 260 model rows through _display_name (registry name wins, classifier cached per ticker)
- `TOLERATES` `data/assets/scripts/gold/build_satellites_registry.py` :: load_classifier/classify -- 260 model rows through load_classifier()+classify() -> (asset_class, sub_asset_class) strings, json-safe
- `TOLERATES` `data/assets/scripts/gold/build_satellites_characteristics.py` :: load_identity -- load_identity over 260 model tickers -> name served, management_style None (absent, not guessed), missing=0, json-safe
- `TOLERATES` `data/black_diamond/scripts/gold/lib/etf_classifier.py` :: ETFClassifier.classify/get_sub_asset_class (BD library) -- 260 model rows through classify()/get_sub_asset_class() verbatim; a miss still reads unknown
- `TOLERATES` `data/black_diamond/scripts/silver/build_bd_assets_dim.py` :: apply_blend (BD assets dim) -- apply_blend over 260 model-row assets (all coarse BD super class) kept every row, canonical columns ['asset_class_canonical', 'sub_asset_class_canonical']
- `TOLERATES` `data/black_diamond/scripts/gold/D_04.client_portal_summary.py` :: _classify_with_canonical -- _classify_with_canonical over 260 model rows -> (class, class, sub, 'etf-classifications'), json-safe
- `READ-ONLY` `data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py` :: BD library consumer (classify/get_sub_asset_class) -- READ-ONLY (runs only inside a live pipeline run). Consumes only the two strings the BD library returns (exercised above). Deciding line(s): `canonical_class = classifier.classify(ticker, name)` | ...
- `READ-ONLY` `data/black_diamond/scripts/gold/D_03.composition_artifacts.py` :: BD library consumer (classify/get_sub_asset_class) -- READ-ONLY (runs only inside a live pipeline run). Consumes only the two strings the BD library returns (exercised above). Deciding line(s): `canonical_class = classifier.classify(ticker, asset_name)` | ...
- `TOLERATES` `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` :: annotate_classification/classify_security -> HoldingsSnapshot contract -- annotate_classification over 260 SECURITY nodes from model rows (classify_security -> canonical row -> asset_class/sub_asset_class, basis TABLE, by_class_source {'etf-classifications': 260}); every served node ...
- `TOLERATES` `infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py` :: TableVocabulary.from_live_table/existing_tickers/plan_rows -- TableVocabulary.from_live_table saw all 5 model classes (paginated projected scan of 263 rows); existing_tickers held all 260 model tickers; plan_rows over 261 held securities planned only the 1 new one(s) and ...
- `READ-ONLY` `data/black_diamond/scripts/gold/E_18.detect_new_securities.py` :: E_18 scheduled caller (BD) -- READ-ONLY (runs only inside a live pipeline run). Calls only TableVocabulary.from_live_table, existing_tickers and plan_rows, exercised in etf_classification_scheduled.py in this order. Deciding line(s): ...
- `READ-ONLY` `data/cot/scripts/gold/E_18.detect_new_securities.py` :: E_18 scheduled caller (COT) -- READ-ONLY (runs only inside a live pipeline run). Calls only TableVocabulary.from_live_table, existing_tickers and plan_rows, exercised in etf_classification_scheduled.py in this order. Deciding line(s): ...
- `TOLERATES` `infra/aws/lambda/v2_portal/yang_pipeline/label-legacy-classified-by.py` :: scan_all/plan_unlabelled/label_row_if_unlabelled -- scan_all paginated 263 rows; plan_unlabelled excluded all 260 model rows (classified_by present) and kept only the unlabelled control; label_row_if_unlabelled on a model row raises RowAlreadyLabelled ...
- `TOLERATES` `infra/aws/lambda/v2_portal/yang_pipeline/set-instrument-kind.py` :: scan_all/plan_absent_kind/set_kind_if_absent -- scan_all+plan_absent_kind offered all 260 model rows (no instrument_kind yet); set_kind_if_absent set instrument_kind on one and touched no other attribute (classified_by/confidence/low_confidence unchanged); ...
- `FAILS-CONTRACT` `infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py` :: read_existing/merge_item (seed correction of a model row) -- no crash and no refusal (read_existing paged 263 rows; the 260 model tickers overlap the seed source by 0, so today's population is unaffected), BUT the seed CORRECTION path carries model attributes onto a ...
- `TOLERATES` `infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-constituents.py` :: main (--dry-run, --kind-only)/put_row_if_unclassified -- paginated scan of 263 rows read; --dry-run plan KEEPs the model ticker (preserve-existing) and plans CREATE for the new one; --kind-only dry-run ok; put_row_if_unclassified on a model row raises RowProtected ...
- `TOLERATES` `data/black_diamond/scripts/classification/seed_canonical_securities.py` :: _yang_conflicts -- _yang_conflicts over 80 model rows read the row via get_item and returned 177 field conflict(s) (table wins, PRESERVED; designed guard), no crash; an absent ticker is still a clean first mint
- `TOLERATES` `data/black_diamond/scripts/classification/seed_bd_securities.py` :: seed (one-time copy into bd-securities) -- one-time seed scanned 263 rows and copied all 260 model rows into bd-securities without error. NOTE (recorded, not graded): the copy overwrites classified_by ('model' -> 'seed_from_yang'), stamps ...
- `TOLERATES` `infra/aws/lambda/v2_portal/yang_pipeline/classify-residual-model.py` :: table_rows_at_build/existing_tickers -- table_rows_at_build counted 263 (Select=COUNT, paginated) and existing_tickers returned all 260 model tickers: the runner's own census sees a model row as a live row, so it is never re-planned
- `TOLERATES` `lib/research/api/scoped_amgt.py` :: _join_classification/_classification_for_ticker -- _join_classification over 260 model tickers (GetItem by bare ticker) -> name SERVED, classification {asset_class, sub_asset_class, sector} from the row, json.dumps strictly (only three named fields leave the ...
- `TOLERATES` `lib/research/identity/positioning_chain.py` :: read_etf_classifications/resolve_one -- read_etf_classifications (client scan + TypeDeserializer, paginated) returned 263 rows incl. all 260 model rows; resolve_one carried classifier_asset_class/sub/name, json.dumps strictly
- `TOLERATES` `infra/aws/lambda/investor-reporting/ycharts/generate/comparison_catalogue.py` :: build_catalogue (injected port, unwired) -- build_catalogue with the injected port returning 260 model rows -> 264 entries, all model tickers named (name_source etf_classifications), validates against ComparisonCatalogue.schema.json (closed), entry keys ...
- `READ-ONLY` `infra/aws/lambda/investor-reporting/ycharts/generate/entry.py` :: read_comparison_catalogue (delegates to build_catalogue) -- READ-ONLY (runs only inside a live pipeline run). Delegates to comparison_catalogue.build_catalogue (exercised above); no classifications port is installed on ENTRY. Deciding line(s): `return ...
- `READ-ONLY` `portal/src/pages/AdvisorIntelligence/_shared/lib/composition.ts` :: CANONICAL_CLASSES / normalizeMixTo4Class (portal asset-class mapping) -- READ-ONLY (TypeScript). Deciding line composition.ts:38: `export const CANONICAL_CLASSES = ['equity', 'fixed_income', 'alternatives', 'structured', 'commodities'] as const`; normalizeMixTo4Class keeps an item ...
- `READ-ONLY` `portal/src/pages/InvestorReporting/contracts/wire/HoldingsSnapshot.ts` :: asset_class wire type -- READ-ONLY (TypeScript). Deciding line HoldingsSnapshot.ts:104 `readonly asset_class?: 'equity' | 'fixed_income' | 'alternatives' | 'structured' | 'commodities' | 'cash' | 'other' | 'unclassified'`: the model's ...
- `READ-ONLY` `org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md` :: IRPT_DASHBD C-CLASSES consumer (PRD only, no code yet) -- READ-ONLY (no consumer code exists in the tree). Deciding line IRPT_DASHBD_PRD.md C-CLASSES row: 'Each holding maps through `etf-classifications` (DynamoDB, key `ticker`): fixed_income, equity, commodities, ...

**Result at this build: `MODEL-READER-TOLERATED` was NOT printed.** `crashes=3` is the static `ETFClassifier.classify_holdings` (three byte-identical copies, zero call sites, raises `KeyError` on alternatives/commodities/structured and already does on live rows of those classes: surprise row `MDPF_SECCLASS-W12-S2`); `fails_contract=1` is `seed-etf-classifications.py`, whose seed-correction path carries `classification_confidence`/`low_confidence` onto a `classified_by = seed` row against contract 0.3.0 (surprise row `MDPF_SECCLASS-W12-S1`). Every reader on the served path (the Holdings producer against `HoldingsSnapshot.schema.json`, the Positioning Lambdas, the BD library and its consumers, the satellites and ETF publishers, the research readers, the scheduled writer's absence test) TOLERATES the row.

**The MODEL_ROWS act is REFUSED unless a fresh census immediately before it prints `MODEL-READER-TOLERATED`.**

