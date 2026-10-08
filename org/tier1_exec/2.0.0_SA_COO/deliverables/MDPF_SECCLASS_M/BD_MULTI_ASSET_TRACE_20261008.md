# BD multi_asset trace -- SC-e-75 / row MDPF_SECCLASS-D1-S9

Traced by `0.9.0_WK_MDPF_SECCLASS~65` on 2026-10-08 ~18:5xZ, worktree branch `wk-secclass-r14-65`, base `82cbab0909`. Read-only: S3 get/list and repo reads.
The trace-correctness judgment is 3.0.0_SA_CVO's (L9); this record states what was read, not a verdict.

## Result in one paragraph

The `multi_asset` literal does NOT enter in `D_04.client_portal_summary.py`. D_04 copies `concentration` verbatim from the C_06
envelope `gold/entities/clients/{rel_id}.json` (`D_04:1192` read, `D_04:1208` write). In the C_06 envelope the `multi_asset` items sit on
**three history dates only (2026-10-03, 10-04, 10-05)**. They were classified verbatim from the `etf-classifications` table by
`C_06.classify_series` (`C_06:228`, `C_06:239`) on the C_06 runs of those dates, while the table still held `multi_asset` rows (written by
the R9 act 2026-10-03; remapped to equity / fixed_income by commit `0d9457b639`, 2026-10-07 03:10 -0400 = 07:10Z). C_06's incremental
merge then froze those dated entries: `C_06:731-740` reads the existing envelope and only overwrites dates in the new partitions
(`existing_conc[ds] = ...`), so a date already on the envelope is never reclassified. Every run since re-serves the frozen entries;
D_04 re-wrote the 36 `concentration.json` files on 2026-10-08 00:50-05:51Z carrying them forward. Dates 10-06 onward read the six-class
values.

The fix is therefore outside this order's grant (`C_06` code is not a change; the INPUT OBJECTS `gold/entities/clients/{rel_id}.json`
hold the stale classes). Steps 2-4 were not executed; see surprise row `MDPF_SECCLASS-D1-W65-S1`.

## Deployed-vs-repo, by content (sha256 of `s3://opal-data-bd/code/gold/<file>` against `git show HEAD:<repo path>`)

Denominator: 9 files read, 9 IDENTICAL, 0 differ, 0 absent from S3.

| file | repo path | bytes (deployed = repo) | sha256[:12] |
|---|---|---|---|
| D_04.client_portal_summary.py | data/black_diamond/scripts/gold/ | 161921 | 039779c147e1 |
| C_06.client_mix_timeseries.py | data/black_diamond/scripts/gold/ | 42619 | dad81a5f8fbf |
| lib/etf_classifier.py | data/black_diamond/scripts/gold/ | 16901 | cfc32f80a0bc |
| lib/s3_layout.py | data/black_diamond/scripts/gold/ | 17811 | 5e5063e8eb22 |
| lib/config.py | data/black_diamond/scripts/gold/ | 467 | ffcb7716d3f5 |
| lib/exclusions.py | data/black_diamond/scripts/gold/ | 8550 | 54044b1944eb |
| lib/floored_percentiles.py | data/black_diamond/scripts/gold/ | 5226 | baee4e294afe |
| lib/mix_views.py | data/black_diamond/scripts/gold/ | 4905 | be7eec161266 |
| lib/_shared/etf_classifications_dynamodb.py | infra/aws/lambda/v2_portal/_shared/ | 14746 | 92b64d97d69b |

D_04's deployed VersionId (latest) `Mu1tZXWFwKEKDLBkmRcfhBq04GXNoAVh`, LastModified 2026-10-02T14:37:30Z. Running bytes are not older than the repo
for any file read. (The shared client's cache `etf_classifications_dynamodb.py:58` is per-process memory only; no persisted copy of a class.)

## The input objects, read for one hit client (z08119861)

- `s3://opal-data-bd/platinum/clients/z08119861/concentration.json` (generated 2026-10-08T05:51:33Z, data_as_of 2026-10-06): 1294 dated
  entries; holdings by class equity 9920, fixed_income 1957, alternatives 1057, unclassified 3, **multi_asset 3**.
- `s3://opal-data-bd/gold/entities/clients/z08119861.json` (C_06 envelope; VersionId `pUkdGIUqCg0Y_I8tkmOHelaTlNn5U.ar`, LastModified
  2026-10-08T05:24:01Z, generated_at 05:22:51Z): the same 3 `multi_asset` holdings are already there, as
  `{"asset_name":"KENSINGTON DYNAMIC ALLOCATION INST","ticker":"KAGIX","asset_class":"multi_asset","asset_class_canonical":"multi_asset","sub_asset_class_canonical":"Flexible","class_source":"etf-classifications"}`
  on dates 2026-10-03, 10-04, 10-05. So the value is present one hop BEFORE D_04.
- KAGIX across dates in the 36 hit files: 09-30, 10-01, 10-02 `unclassified`; 10-03..10-05 `multi_asset`; (10-06 not in the top-10 of that client).
  ABALX: equity 09-30..10-02, multi_asset 10-03..10-05, equity 10-06. AMECX / CAIBX: unclassified 09-30..10-02, multi_asset 10-03..10-05,
  fixed_income 10-06. SCGB1: unclassified, then multi_asset 10-03..10-05, equity 10-06. The flip to the six-class value on 10-06 is the
  first date classified after the 10-07 07:10Z remap.

## Census of all hit keys (S3 get, all 36 opal-data-bd keys read; the 2 other hit keys are in opal-data-cot and out of scope)

- 36 of 36 `platinum/clients/*/concentration.json` read; 141 `multi_asset` holdings in total.
- By date: 2026-10-03 = 47, 2026-10-04 = 47, 2026-10-05 = 47. Latest hit date 2026-10-05. Zero hits on any date >= 2026-10-06.
- By ticker: ABALX 12, AMECX 9, CAIBX 9, SCGB1 5, KAGIX 3, FBALX 3, FKIQX 3, MDLOX 3, AAETX 3, CFIHX 3, no ticker 88. The four named tickers and the 88
  match the cell's measurement exactly. All 141 carry `class_source` `etf-classifications`.
- The 88 items with no ticker carry `class_source` `etf-classifications`, i.e. they resolved through the blank-ticker identity chain
  (`lib/etf_classifier.py classify_with_identity`) to a row that said `multi_asset` at the time.
- Mix (`mix` in the envelope) is not affected: its keys are the fixed set equity / fixed_income / alternatives / commodities / structured /
  cash / unclassified / other; only `concentration` carries the per-holding class.
- The 2 cot hits (`opal-data-cot platinum/clients/z09305621|z09305679/concentration.json`, last modified 2026-10-08T11:36:56Z, 1 hit each)
  are COT's twin (SC-e-67); not traced here.

## First entry point, named

1. Origin of the literal: the `etf-classifications` rows written `multi_asset` by the R9 act (row-set
   `R9_CHECKS/MULTI_ASSET_ROW_SET_20261003.tsv`, e.g. line 27 `WRITE KAGIX ... absent -> multi_asset`), read at run time by
   `C_06.client_mix_timeseries.py:228` (`classifier.classify`) and `:239` (`asset_classes.append(canonical_class)`), emitted at `:575-577`.
2. Persistence: `C_06.client_mix_timeseries.py:731-740` (incremental merge keeps every already-written date's entry).
3. Passthrough: `D_04.client_portal_summary.py:1192` (`conc_list = data.get('concentration', [])`) and `:1208` (written to
   `platinum/clients/{rid}/concentration.json`).

The same literal can also be re-served by D_04's other two concentration paths (`D_04:490`, `:632`, `:1085`, which read `cls.get('asset_class')`
from the same classifier output at run time), but the census reads zero hits on a date >= 2026-10-06, so those do not carry it today.

## What would remove it (stated, not done: outside the grant)

The 36 C_06 envelopes need their 10-03..10-05 holdings reclassified through the current table (a C_06 FULL build, which reclassifies every
date, or a targeted rewrite of those dated entries), after which the next D_04 fire rewrites `concentration.json`. Either is a write to
served `gold/entities/clients/` objects and `platinum/clients/` and needs the never-widen sign-off pair; it is the issuer's re-point.
