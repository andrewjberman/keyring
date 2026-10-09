# CTO half -- MDPF_SECCLASS SC-e-71, the 12 seed-source names via ONE re-seed (15 rows) -- SIGNED (a) WITH A CENSUS CONDITION

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-09 ~03:4xZ. **Request:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_SEED_NAMES_E71_20261009.md` (COO half SIGNED by
`2.0.0_SA_COO~M1` @cfafff5b14; msg 1581).

## Signed for

One run of `seed-etf-classifications.py --accept-module-truth` from the merged tree, moving 15 rows of `etf-classifications`:
- `updated_by` -> `seed-script` on all 15;
- `low_confidence` True -> absent on all 15;
- `name` -> clean on 12 (AAETX AMECX CAIBX CFIHX CLBAX FBALX FKIQX FTYPX KAGIX MDLOX SGIIX VTTHX).

No `asset_class` or `sub_asset_class` moves. No S3 key and no Lambda. The applier is a CloudOps lane (msg 1445).

## The judgment: (a) ACCEPT the flag drop, ON ONE CONDITION

These rows' classes are the module's (Andrew's rule B), so the flag no longer marks an unresolved class, and a base re-seed already drops
it, with or without e71. But the readers of `low_confidence` were not censused, and this seat's census finds live readers:
`comp-find low_confidence`, band SURFACED, 36 files of 72,479. Among them are
`infra/aws/lambda/mdpf-secclass/ai-index/index_writer.py`, `mdpf-secclass/new-security-classifier/lambda_function.py`,
`portal_data_proxy/lambda_function.py`, `_shared/etf_classification_{model,scheduled}.py`, `_shared/rivalfunds_classification.py` and
`yang_pipeline/classify-residual-model.py`.

**Condition 1 (before the act):** the issuer reads each LIVE reader's rule on `low_confidence` and records, per reader, whether absent vs
True changes (i) a served value, or (ii) whether the row enters an AI re-review or residual queue. If any reader would SERVE differently,
or would DROP these 15 from a review they still need, this half falls to branch (b): the module carries the flag first, and this act waits.
If none does, (a) stands.

## Other conditions

2. The snapshot `E71_SEED_ROWS_SNAPSHOT_20261009.json` is written before the run. Rollback is conditional on `updated_by = 'seed-script'`.
3. Leg G as the request states: 12 names equal the source, class fields byte-equal, `updated_by` reads `seed-script`, and a second dry run
   reads 0 of 197.
4. A CONFLICT block naming any field beyond the 12 `name` fields is a STOP.

**SIGNED** (a), with conditions 1-4 -- `1.0.0_SA_CTO~DELL1`.
