# Never-widen half request, MDPF_SECCLASS -- release of SC-e-71: the 12 seed-source names reach the table through ONE re-seed (15 rows)

**Author:** `2.0.0_SA_COO~M1`, 2026-10-09 ~03:4xZ. **For:** `1.0.0_SA_CTO~DELL1`, second half. **Status: COO half SIGNED; CTO half SIGNED (a) @d6c99a32d5; condition 1 MET (below); act HELD on XA-20261009T034916Z-ccd1.**
**Cell:** `SC-e-71` (`decompositions/MDPF_SECCLASS_DECOMP_R12.md`). The build is on the held line `q/dell1/secclass-r12-held-e71/r1` @2f063454e3
(proof VALID). Its release was held on limit item 5, which is lifted (Andrew-direct 2026-10-08 ~13:2xZ; routes-host policy measured absent ~02:0xZ).

## What the release has to move, measured

The 12 names live in `infra/aws/lambda/v2_portal/_shared/etf_classification.py` `ETF_NAME_OVERRIDES`. Readers of that dict, by census
(`comp-find 'ETF_NAME_OVERRIDES'`, 205 hits / 65,467 files, SURFACED read in full):
- `_shared.get_display_name()` has **no caller** (`comp-find 'get_display_name|get_etf_name'`: 9 hits; the only other caller,
  `bd_gold_common.get_display_name(row)`, is a different function). So the shipped copies at `opal-data-bd` / `opal-data-cot`
  `code/gold/lib/_shared/etf_classification.py` (both ETag 3a033c04 = box/dell1 md5 today) serve no name. **They are NOT shipped by this
  act.** A later deploy that names them would move bytes with DELTA=0 on any served name.
- `opal-partners-data` and `yang-generate-etf-returns` carry their own copies of the dict, which e71 does not edit. Out of scope.
- **`seed-etf-classifications.py` (writer 1 of `name`, N = 8 per the V2 half)** writes `name = ETF_NAME_OVERRIDES.get(ticker)` for
  `seed` rows. **This is the only path to a served name.** The V2 clean-name writer refuses all 12 by design ("a seed row always wins").
  Dry run over a 12-row WRITE set `CLEAN_NAME_ROW_SET_E71_SEED_SOURCE_20261009.tsv`: `refused_stale=12 puts=0`.

## The act (issuer-designed; applied by a CloudOps seat per 1.0.0_SA_CTO~DELL1 msg 1445)

1. Merge the held line onto box/dell1. It merges clean: `git merge --no-commit` over box/dell1 @HEAD ~03:3xZ, 4 files, 0 conflicts.
2. Run `python infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py --region us-east-1 --accept-module-truth` from that
   merged tree.

**Dry run, both arms, the same table read (11,361 rows, 197 module tickers):**
- **Base (box/dell1, no e71):** `rows to write: 15 of 197`, 0 CONFLICT. **A re-seed today already rewrites 15 rows** (row S46's class).
- **With e71 merged:** the same 15 rows, plus a CONFLICT block naming exactly the 12 `name` fields. The run is BLOCKED without
  `--accept-module-truth` ("NOTHING WAS WRITTEN").

**The per-field delta of that run, every field, 15 rows** (`merge_item` against a consistent `get_item` of each, timestamps excluded):

| rows | field | table today -> after |
|---|---|---|
| 15 (all) | `updated_by` | `mdpf-secclass-remap-b` -> `seed-script` |
| 15 (all) | `low_confidence` | `True` -> **absent** |
| 12 | `name` | all-caps -> clean_name() (AAETX AMECX CAIBX CFIHX CLBAX FBALX FKIQX FTYPX KAGIX MDLOX SGIIX VTTHX) |
| 3 | (no `name` change) | LIPKX, VSMGX, VTIVX: only the two fields above |

**No `asset_class` and no `sub_asset_class` moves on any row.** The 15 rows are the remap-b rows the seed module carries.

## The judgment the signers must make

The remap-b act (ledger `secclass-multi-asset-remap-b-m-20261007`) set `low_confidence=True` on these 15 rows. Any re-seed removes the flag,
because the seed module does not carry it. That holds with or without e71: the base arm writes the same 15. Two branches:
- **(a) Accept:** the seed rows are module-curated, so the flag goes. The 12 names land clean. Every later re-seed is then a no-op on these rows.
- **(b) Keep the flag:** the module (or `merge_item`) must carry `low_confidence` for these 15 first. That is a new code cell, and this act waits for it.

COO recommendation: **(a)**. These rows' classes are the module's, ruled by Andrew's rule B, so the flag no longer marks an unresolved class.
Readers of `low_confidence` were not censused for this request. The CTO half should name whether that census is a condition.

## Rollback per key

`E71_SEED_ROWS_SNAPSHOT_20261009.json`: a consistent read of the 15 rows at ~03:4xZ, each item whole. To roll back, put each snapshot
item back with condition `updated_by = 'seed-script'`, so a row moved since is refused, not overwritten. Numbers in the snapshot are JSON
floats; none of the 15 rows' changed fields is numeric.

## Acceptance (leg G)

A consistent read of the 15 rows shows:
- the 12 names equal the e71 source;
- `asset_class` and `sub_asset_class` byte-equal to the snapshot;
- `updated_by` reads `seed-script`.

A second `--dry-run` reads `rows to write: 0 of 197`. The served names appear at the next consumer read of the table.

## COO half -- SIGNED

`2.0.0_SA_COO~M1`, 2026-10-09 ~03:4xZ.
- **Writers of `name` on this table: N = 8**, counted in the V2 half. Writer 1 (this script) is the only one that writes a `seed` row's name. Writers 3-7 are put-on-absence.
- **Both branches** of the seed run's own rule were read at signing: BLOCKED without the flag, written with it.
- **The blast radius is the 15 rows in the delta table above.** Nothing else is written: no S3 key and no Lambda.

## CTO half -- SIGNED (a) with conditions 1-4

Recorded by the issuer: `1.0.0_SA_CTO~DELL1`, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_SECCLASS_SC_E71_SEED_NAMES_20261009.md`
@d6c99a32d5 (msg 1585). The act is held until laptop cross-adjudication XA-20261009T034916Z-ccd1 reads RULED (msg 1586).

## CTO condition 1 -- the reader census of `low_confidence`: MET, branch (a) stands

`2.0.0_SA_COO~M1`, 2026-10-09 ~03:5xZ. The census is `comp-find 'low_confidence' --corpus default --band SURFACED --files --all`: 32 files of
65,557 scanned. Of those, 11 are product code. The other 21 are records, issuer check scripts and audit logs, which serve nothing. Each of the
11 rules was read at the line:

| reader | rule on `low_confidence` | (i) serves differently? | (ii) drops the 15 from a review? |
|---|---|---|---|
| `mdpf-secclass/ai-index/index_writer.py` | `build_listing` keeps only `classified_by == model` rows (:102-103) | no: the 15 are `seed` | no |
| `yang_pipeline/classify-residual-model.py` | plans held keys and puts with `attribute_not_exists(ticker)`; it sets the flag on new model rows and never selects on it | no | no: a present key is never re-planned |
| `yang_pipeline/write-model-rows.py` | refuses a model CANDIDATE under threshold (:112); writes `False` on its own rows | no | no: it reads candidates, not table rows |
| `_shared/etf_classification_model.py` | produces the flag from the model's confidence | no | no |
| `_shared/etf_classification_scheduled.py` | carries the field in `_WRITE_FIELDS` (:139); does not branch on it | no | no |
| `_shared/rivalfunds_classification.py` | sets the flag on a planned row with no sub-class (:181) | no | no |
| `mdpf-secclass/new-security-classifier/lambda_function.py` | plans through rivalfunds; skips every present key | no | no |
| `keyword_intelligence_generator/lambda_function.py`, `portal_data_proxy/lambda_function.py`, `portal/src/api/endpoints/sentiment.ts` | a different field: the `sentiment_pattern` VALUE `'low_confidence'` | n/a | n/a |
| `yang_pipeline/seed-etf-classifications.py` | the writer of this act | n/a | n/a |

No reader serves a value from an existing row's `low_confidence`, and no queue selects on it. Absent and True are equivalent for every live reader
of these 15 seed rows.
