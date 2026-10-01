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

## ADDENDUM 1 (2.0.0_SA_COO~M, 2026-10-01 09:0xZ) -- the served move measured, one sentence above corrected, the catalogue's reader added; NOT SIGNED

**1. Ruling 1's two conditions are met** (`CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_6_20261001.md` @453c6430ec). The
comparison catalogue excludes a model-written row from its list and answers its ticker verbatim (2.0.0_SA_COO~Y, CLOUD
@89c304eaeb, with its test). A fresh census, `R7_MODEL_READER_CENSUS_20261001_0730Z.json` @0883367f4f, reads readers=35
tolerates=26 read_only=9 crashes=0 refuses=0 fails_contract=0, uncensused 0, `MODEL-READER-TOLERATED`. The three crashes
(row W12-S2) and the seed contract failure (row W12-S1) of the table above are fixed (@a96e00c279, @9053ffba73).

**2. Reader added to the table above (ruling 1):** `TOLERATES`
`infra/aws/lambda/investor-reporting/ycharts/generate/comparison_catalogue.py :: classifications_reader -> build_catalogue /
entry_for_ticker`, composed by `reports/generate_installed.py` (READ-ONLY). Behaviour: a paginated Scan projecting
`ticker`, `name`, `identifier_namespace`, `classified_by`; a row whose `classified_by` is `model` lends no name, so it is
absent from the served list and its ticker is answered verbatim. Exercised by the census through the real reader over a
stubbed table: 0 of the named model rows are listed.

**3. CORRECTION to "Blast radius", the sentence "readers ... see a real class where they previously saw none".** It is
false for most of the 26. The Holdings producer answers a ticker the canonical table lacks from the bd-securities
fallback, so these tickers are served a class TODAY, and a model row REPLACES that answer from the next publication on.
Measured on the three local Holdings builds of 2026-10-01 00:51Z-01:00Z (actual positions, by `display.symbol`):
25 of the 26 tickers are held (AMUSX is not).

| firm | ticker | served today (fallback layer) | model row | nodes | USD | flagged |
|---|---|---|---|---|---|---|
| 49 Financial | CAIBX | fixed_income (table) | equity | 3 | 325,021.86 | |
| 49 Financial | MLPTX | alternatives (table) | equity | 1 | 19,444.55 | yes |
| 49 Financial | O | fixed_income (table) | alternatives | 9 | -91,808.10 | |
| Cottonwood | O | fixed_income (table) | alternatives | 2 | -58,227.84 | |
| Inflection | USRT | equity (table) | alternatives | 466 | 701,622.86 | |
| Inflection | PCOFX | fixed_income (table) | commodities | 2 | 377,198.38 | yes |
| Inflection | FFFHX | alternatives (table) | equity | 3 | 28,575.51 | yes |
| Inflection | VCMDX | equity (ticker shape) | commodities | 1 | 3,876.73 | |
| Inflection | CSRSX | equity (ticker shape) | alternatives | 1 | 1,070.88 | |
| Inflection | BSBIX, BSBSX, FBIIX, PFUNX, PHLPX, PZTRX | equity (ticker shape) | fixed_income | 1,081 | 0.00 | 5 of 6 |
| Inflection | MLPTX, TMAAX | alternatives (table) | equity | 245 | 0.00 | yes |
| Inflection | CAIBX, O | fixed_income (table) | equity, alternatives | 2 | 0.00 | |

USD whose served class changes: 49 Financial 252,658.31, Cottonwood -58,227.84, Inflection 1,112,344.36 (net of the
negative `O` positions). The other held tickers keep their class (BAGIX, BAGSX, BSIIX, DODIX, EMXC, FXNAX, IGSB, JEMSX,
FOCSX, RLY: 5,860,148.15 USD across the three firms); for those the row changes only the source of the answer.
Black Diamond gold (C_06, D_03, D_04) and every other reader of the table move the same tickers where they hold them;
that population is NOT measured here.

**4. THE ACT HAS NO WRITER.** `classify-residual-model.py` has no write path by design, and
`etf_classification_scheduled.write()` is the scheduled path's. A replay of the 26 named rows (conditional put,
`classified_by: model`, the census's confidence, `low_confidence` under 0.80) needs a small writer with a dry run; its
file is outside this seat's grant. Asked of `1.0.0_SA_CTO` 2026-10-01 09:0xZ.

**5. Rollback, corrected.** The half's rollback is 26 `DeleteItem` calls. A delete is a destructive act that needs
Andrew's word; two seat signatures are not that. Without it the remedy for a wrong model row is a seed row for that
ticker (seed always wins, and the seed write drops the model's confidence fields).

**The COO half is NOT signed.** It is signed after the writer exists, its dry run names exactly these 26 tickers as
absent from the table, and a census run immediately before the act prints `MODEL-READER-TOLERATED`.

## ADDENDUM 2 (2.0.0_SA_COO~M, 2026-10-01 10:1xZ) -- THE ACT AS RULED: 14 rows in two sets, 12 withheld

Authority: 1.0.0_SA_CTO rulings batch 75 items 1-4 @8f06def1e7 and batch 78 items 6-8 @ae1900ab3e. **This addendum
replaces "The act", "Blast radius" and "Rollback per key" above for what is signed; the 26-row act above is NOT signed.**

### The act

`python infra/aws/lambda/v2_portal/yang_pipeline/write-model-rows.py --tickers-file
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/MODEL_ROWS_WRITE_SET_20261001.txt --write`, once, from the
laptop at CLOUD (writer and `_WRITE_FIELDS` change @2c2358e104). 14 conditional puts
(`attribute_not_exists(ticker)`, through `etf_classification_scheduled.write()`), each item: `ticker`, `asset_class`,
`sub_asset_class`, `classified_by: model`, `updated_by: mdpf-secclass-model`, `classification_confidence`,
`low_confidence: false`, `last_updated`. No `name` (the census's name is the ticker). No overwrite, no delete.

Stops, each read immediately before the write: (1) the reader census prints `MODEL-READER-TOLERATED`; (2) the writer's
dry run reads `named=14 plan=14 already_present=0 refused=0` (read live 10:04Z: exactly that, table rows 2,658).

### Every one of the 26, under one set (ruling item 3)

Custody names are the firms' own descriptions (Holdings builds, Black Diamond lots). The model saw the TICKER ONLY: the
census carries the ticker in its `name` field for all 26, so its answer rests on recognising the symbol.

| set | ticker | custody name | served today (Holdings fallback) | model row | peer row in the table |
|---|---|---|---|---|---|
| (a) | AMUSX | held nowhere | -- | fixed_income / Intermediate | BND |
| (a) | BAGIX | Baird Aggregate Bond Instl | fixed_income / Investment Grade | fixed_income / Intermediate | BND, AGG |
| (a) | BAGSX | Baird Aggregate Bond Inv | fixed_income / Intermediate | fixed_income / Intermediate | BND, AGG |
| (a) | BSIIX | BlackRock Strat Inc Oppor Port I | fixed_income / Investment Grade | fixed_income / Intermediate | BND |
| (a) | DODIX | Dodge & Cox Income | fixed_income / Investment Grade | fixed_income / Intermediate | BND, AGG |
| (a) | EMXC | iShares MSCI Emerging Markets ex-China ETF | equity / Emerging Markets | equity / EM | IEMG |
| (a) | FXNAX | Fidelity US Bond Index | fixed_income / Investment Grade | fixed_income / Intermediate | BND, AGG |
| (a) | IGSB | iShares 1-5 Year Investment Grade Corporate Bond ETF | fixed_income / Investment Grade | fixed_income / Short Duration | VCSH |
| (a) | JEMSX | JP Morgan Emerging Markets Equity Select | equity / none | equity / EM | IEMG |
| (b) | USRT | iShares Core US REIT | equity / Real Estate | alternatives / Real Estate | VNQ (seed) |
| (b) | CSRSX | Cohen and Steers Realty | equity / none | alternatives / Real Estate | VNQ (seed) |
| (b) | VCMDX | Vanguard Commodity Strategy Admiral | equity / none | commodities / Commodities | DBC, PDBC (seed) |
| (b) | PFUNX | Pimco Foreign Bond Unhedged Cl I-3 | equity / none | fixed_income / International | IAGG (seed) |
| (b) | CAIBX | American Capital Income Builder A | fixed_income / Investment Grade | equity / Global | AOR (scheduled) |
| (c) | O | Realty Income Corp | fixed_income | alternatives -- NOT written | AMT and PLD read equity / US Large Cap: the peer disagrees |
| (c) | BSBIX, BSBSX, FBIIX, FFFHX, FOCSX, MLPTX, PCOFX, PHLPX, PZTRX, RLY, TMAAX | -- | see addendum 1 | NOT written: low-confidence | -- |

Four things the table shows that a reader should not have to find:

- **A peer conflict in (b).** VNQ (seed) reads alternatives / Real Estate; REET, a global REIT ETF, reads equity / Global
  (a scheduled row). USRT and CSRSX follow the seed row, which is the ruling's named peer.
- **The peer of CAIBX is a scheduled row** (AOR, an allocation ETF), not a seed row. If that is not peer enough, CAIBX
  moves to (c) and the act is 13 rows.
- **One low-confidence answer is measurably wrong.** PCOFX is "Polen Credit Opportunities" at Black Diamond and
  Inflection, a credit fund; the model answered commodities (0.65). It is withheld by set (c).
- FOCSX and RLY keep their class under the model but are low-confidence, so (c) holds them; ruling item 3(a) counts ten
  held tickers, which reads as eight held plus AMUSX here.

### What moves on a served page

Holdings tab (local builds of 2026-10-01 00:51Z-01:00Z, actual positions):

| | 49 Financial | Cottonwood | Inflection |
|---|---|---|---|
| set (b), CLASS moves | CAIBX 3 nodes, 325,021.86 USD (fixed_income to equity) | none | USRT 466 nodes 701,622.86 USD and CSRSX 1 node 1,070.88 USD (equity to alternatives); VCMDX 1 node 3,876.73 USD (equity to commodities); PFUNX 165 nodes 0.00 USD (equity to fixed_income); CAIBX 1 node 0.00 USD |
| set (a), class stays, SUB CLASS moves to the canonical word | 29,008.17 USD | 4,683,677.30 USD | 1,088,385.46 USD |

Set (a) is NOT a no-op on the page: the sub classes the fallback serves ("Investment Grade", "Emerging Markets", none)
become the canonical ones ("Intermediate", "Short Duration", "EM") on 5,801,070.93 USD across the three firms. BAGSX
alone is unchanged on both axes.

Black Diamond gold (the advisor pages of 49 Financial; `gold/holdings_lots/2026-09-25.parquet` as written 07:28Z, open
lots): 7 of the 14 are held -- BAGIX, BSIIX, CAIBX, DODIX, EMXC, IGSB, USRT, 99 lots, 976,963.75 USD. The Black Diamond
library answers none of them today (`D_04._classify_with_canonical` returns `other` / `unclassified`), so on C_06, D_03
and D_04 they move from other to the model's class at the next gold run. The three held and withheld tickers (MLPTX,
O, PCOFX: 130 lots, 2,645,813.73 USD) stay `other`.

Readers: the 35 of the census. The comparison list is unchanged (a model row lends no name).

### Rollback, acceptance, ledger

- **Rollback:** a seed row for the ticker (seed always wins and drops the two model fields). No item is deleted.
- **Acceptance:** (1) right after the run, a scan reads 14 rows with `classified_by: model`, each with both model fields,
  and the table counts 2,672; a second dry run reads `plan=0 already_present=14`. (2) the next
  `irpt-holdings-snapshot` publication serves the moves in the table above on one selection per firm. (3) the next
  scheduled Black Diamond gold fire reads the seven tickers with `class_source` etf-classifications.
- **Ledger:** one new entry, `secclass-model-rows-m-20261001`, opened before the run.

### Carried, not part of this act

- Contract 0.3.0 `low_confidence.definition` says a flagged row "is written exactly like any other model row"; ruling
  item 3(c) withholds the eleven this round. This half follows the ruling; the contract sentence is 1.0.0_SA_CTO's.
- The twelve of set (c): each needs a seed row with its public ground named, under its own half, or stays on the
  fallback. O and PCOFX are the two whose served class is measurably wrong today (row `MDPF_SECCLASS-S7`).
- The shipped copy of `etf_classification_scheduled.py` on the Black Diamond runner is one line behind the repo
  (batch 78 item 8: inert; named by whoever ships it).

## COO half on ADDENDUM 2 -- SIGNED (2.0.0_SA_COO~M, 2026-10-01 10:1xZ)

Signed on the 14-row act above: the write set, the served moves of both sets at the three firms and on Black Diamond
gold, the two stops before the write, and a rollback that is a seed row. Read at signing: the live dry run of the writer
(10:04Z), the peer rows (`batch-get-item`, 09:5xZ), the three Holdings builds, the Black Diamond lots, the before/after
test of the shared put (4 passed) and the tests of the writer (11 passed). I stop on any deviation this addendum does
not name.

## CTO half on ADDENDUM 2 -- (unsigned)
