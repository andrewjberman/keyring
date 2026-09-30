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
