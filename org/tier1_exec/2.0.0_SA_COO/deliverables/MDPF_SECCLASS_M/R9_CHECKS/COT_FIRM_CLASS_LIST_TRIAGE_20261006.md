# MDPF_SECCLASS SC-e-20 amendment 1 -- triage of the 22 served class lists that lack `multi_asset`, by measured loss TODAY

By `0.9.0_WK_MDPF_SECCLASS~20`, 2026-10-06 (reads 16:2x-17:0xZ). READ ONLY: S3 and DynamoDB were read, nothing was written, no list outside the
granted files was edited. Claim state of every dollar below: `measured` (read from the named served key or computed by the named in-process read),
unless the line says `inferred`. Served keys are as served at read time; the `LastModified` stamps are UTC (boto3).

Subjects: the 22 rows of `COT_FIRM_CLASS_LIST_CENSUS_20261006.md` that lack `multi_asset` AND feed a served artifact (census Counts, "Of the 28
lacking, feeding a served artifact: 22"). The census rows carry no numbers, so they are numbered T01-T22 here in the census's own row order
(Black Diamond, Inflection, 49F runners, Cottonwood tree, portal); the six lacking-but-not-served rows (BD `B_01b`, `E_16`, `E_25`; Inflection
`classify_assets`; 49F `d06:235`; portal `types.ts`) are not triaged.

| id | list (census row) | firm / bucket |
|---|---|---|
| T01 | `data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py:182` | 49 Financial / `opal-data-bd` |
| T02 | `data/black_diamond/scripts/gold/lib/mix_views.py:25` | 49 Financial / `opal-data-bd` |
| T03 | `data/black_diamond/scripts/gold/D_03.composition_artifacts.py:101-111` | 49 Financial / `opal-data-bd` |
| T04 | `data/black_diamond/scripts/gold/D_02.advisor_client_detail.py:2289` | 49 Financial / `opal-data-bd` |
| T05 | `data/black_diamond/scripts/gold/D_00b.portal_timeseries.py:90-96, :690, :704` | 49 Financial / `opal-data-bd` |
| T06 | `data/black_diamond/scripts/gold/D_00.portal_aggregates.py:113-115, :216-223` | 49 Financial / `opal-data-bd` |
| T07 | `data/inf/scripts/gold/INF_D_02d.firm_mix_summary.py:76-80` | Inflection / `opal-data-inf` |
| T08 | `data/inf/scripts/gold/INF_D_03.composition_artifacts.py:120-126` | Inflection / `opal-data-inf` |
| T09 | `data/inf/scripts/gold/INF_D_04b.client_publishers.py:81` | Inflection / `opal-data-inf` |
| T10 | `data/inf/scripts/gold/INF_D_06.client_timeseries.py:92-96` | Inflection / `opal-data-inf` |
| T11 | `data/inf/scripts/gold/INF_D_07a.firm_concentrations.py:192-202` | Inflection / `opal-data-inf` |
| T12 | `data/assets/scripts/gold/runners_49f/d06_firm_mix_summary.py:46-47` | 49 Financial runner (local mirror) |
| T13 | `data/assets/scripts/gold/runners_49f/d09_firm_timeseries_overview.py:162-165` | 49 Financial runner (local mirror) |
| T14 | `data/assets/scripts/gold/runners_49f/a07_dim_asset_classification.py:336` | 49 Financial runner (local mirror) |
| T15 | `data/cot/scripts/gold/runners_cot/d08_cot_mix_summary.py:48-57` | Cottonwood / `opal-data-cot` |
| T16 | `data/cot/scripts/gold/D_03.composition_artifacts.py:102-111` (+ the new label, this commit) | Cottonwood / `opal-data-cot` |
| T17 | `data/cot/scripts/gold/D_00b.portal_timeseries.py:91-96, :642-645` | Cottonwood / `opal-data-cot` |
| T18 | `data/cot/scripts/gold/D_00.portal_aggregates.py:111-113, :219-221` | Cottonwood / `opal-data-cot` |
| T19 | `data/cot/scripts/gold/D_02.advisor_client_detail.py:2310` | Cottonwood / `opal-data-cot` |
| T20 | `portal/src/pages/AdvisorIntelligence/_shared/perfrp/PerfrpAllocation.tsx:43-46` | portal (all firms) |
| T21 | `portal/src/pages/AdvisorIntelligence/_partners/inflection/InflectionInsightsPanel.tsx:1022-1025` | portal (Inflection) |
| T22 | `portal/src/api/endpoints/advisor-intelligence.ts:842-850, :1201-1210` | portal (Inflection adapter) |

## HELD `multi_asset` DOLLARS (the yardstick)

From `MULTI_ASSET_LEG_V_<firm>_20261005.json` (served platinum holdings, reconciled to custody) and the in-process reads below:

| firm | leg V held `multi_asset` | leg V date | this triage's own read of the class on the served-artifact basis |
|---|---|---|---|
| Cottonwood | $159,905.56 (5 nodes, 2 keys) | 2026-10-02 | $266,651.67 = SGIIX (CUSIP 32008F606) in `gold/canonical/holdings/2026-10-05.parquet`, ghost-excluded, classed by `D_03.classify_series` (class total beside it: all 8 classes sum to the 2026-10-05 canonical AUA $546,489,758.16) |
| Inflection | $40,560.31 (20 nodes, 7 keys) | 2026-10-02 | not re-read: the Inflection chain never reads the canonical table class (T07-T11) |
| 49 Financial | $2,515,601.18 (35 nodes, 9 keys; 2026-10-06 post-fire read) | 2026-10-05 | $5,524,740.01 raw / $5,438,537.07 scaled to canonical AUA $1,994,163,246.13 = 22 CUSIP/ticker rows classed `multi_asset` over `gold/timeseries/holdings_lots/2026-10-02.parquet` (ghost + AP gates as D_03 applies), classed by BD `D_03.classify_series` |

The 49F leg-V figure and this read differ in date (10-05 vs the 10-02 holdings_lots the served BD gold last read) and in key set (9 keys vs 22 rows);
neither is wrong, they are different populations. The verdicts below use the served artifact's own as-of date.

---

## T01 -- BD `C_06.client_mix_timeseries.py:182` `MIX_ASSET_CLASSES` (eight classes)

- Served artifacts (read from the code, `lib/s3_layout.py`): `s3://opal-data-bd/gold/entities/clients/<id>.json` (client mix points), `gold/views/mix_daily_summary.json` (firm and advisor daily).
- READ: `mix_daily_summary.json` LastModified 2026-10-04 05:27:06Z; 10-02 firm point: eight classes sum $1,994,163,061.52 vs `total` $1,994,163,246.13 (gap $184.61, not `multi_asset`). All client files: max LastModified 2026-10-04 05:27:05Z. The 77 relationships whose 2026-10-02 holdings_lots rows carry one of the 22 `multi_asset` CUSIP/ticker keys: 77 of 77 client mix files carry a 2026-10-02 point and 77 of 77 sum to 0.999999 (none off by more than 0.001).
- Reading: this C_06 run (10-04 05:27Z) predates the table's `multi_asset` rows reaching 49F's classification (BD `D_03` at 2026-10-06 05:25Z already classes them `multi_asset`, T03), so the held dollars sit in the served `unclassified` line (INFERRED from the timing: served `unclassified` $150,433,677.99 vs D_03's raw `unclassified` about $146.03M plus `multi_asset` $5,524,740; the run's classifier state was not read). The served mix therefore sums to 1 and loses none today.
- NEXT-RUN EXPOSURE (not today's loss): the 77 clients publish mixes that omit `multi_asset` the first time C_06 runs against the current table, and C_06's sum guard over the aggregate would pass (the SC-e-20 defect, unedited for BD).

VERDICT: HOLDS-NONE

## T02 -- BD `lib/mix_views.py:25` `MIX_ASSET_CLASSES` (period views)

- Served artifacts: `s3://opal-data-bd/gold/artifacts/firm_mix_views.json`, `gold/entities/advisors/<id>/mix.json` and `mix_timeseries.json` (written by `D_03._publish_mix_views`).
- READ: `firm_mix_views.json` LastModified 2026-10-06 05:27:58Z, as of 2026-10-02: monthly point class values sum $1,994,163,246.13 = `total_aua` $1,994,163,246.13, pct sum 1.0 (the daily summary it reads is the 10-04 one of T01). 213 advisor directories: 59 carry `mix_timeseries.json`, all 59 in the `views` shape, all 59 last-point pct sums equal 1 within 0.001 (56 written 2026-10-06, class set equal to the eight).
- Reading: the views carry no `multi_asset` line because their input (T01) carries none; no dollars are lost on the served points. Same next-run exposure as T01: once `mix_daily_summary` carries `multi_asset`, this list drops it.

VERDICT: HOLDS-NONE

## T03 -- BD `D_03.composition_artifacts.py:101-111` `_ASSET_CLASS_LABELS` (loop `for asset_class in _ASSET_CLASS_LABELS`)

- Served artifacts: `s3://opal-data-bd/gold/views/firm_composition.json`; `gold/entities/advisors/<id>/composition.json`; `gold/entities/clients/<id>_composition.json`.
- READ: `firm_composition.json` LastModified 2026-10-06 05:25:50Z, data_as_of 2026-10-02: `total_market_value` $1,994,163,246.13; the seven mix classes sum to $1,988,724,709.05; the difference is $5,438,537.08.
- The held `multi_asset` dollars on the same basis (BD `D_03` steps 1-2 re-run in process over `gold/timeseries/holdings_lots/2026-10-02.parquet`: 512,456 lots after the ghost and AP gates; class `multi_asset` = $5,524,740.01 raw; scaled by canonical AUA / lot total = $5,438,537.07). Left side (custody total, served) $1,994,163,246.13 - right side (sum of the served classes) $1,988,724,709.05 = $5,438,537.08 against the held $5,438,537.07: the missing dollars ARE the `multi_asset` holdings, to $0.01.
- Client compositions: the 77 relationships holding a `multi_asset` key: 77 of 77 `<id>_composition.json` read; 52 of 77 have `total_market_value` more than $1 above the sum of their class lines; the 52 gaps sum to $5,469,154.53 (largest: `z08320620`, short $1,121,776.75; the other 25 show no gap above $1).

VERDICT: DROPS-TODAY

## T04 -- BD `D_02.advisor_client_detail.py:2289` `mix_fields` (equity, fixed_income, structured_notes, cash, other)

- Served artifact it writes: `s3://opal-data-bd/gold/entities/advisors/<id>/mix_timeseries.json` (data shape, `build_advisor_mix_timeseries`).
- READ: 213 advisor directories listed; 59 carry `mix_timeseries.json`; 0 of 59 are in D_02's `data` shape, 59 of 59 are in the `views` shape that `D_03._publish_mix_views` writes to the same key (T02). The D_02 list is not the writer of any served byte today.
- Reading: the artifact the list would write is overwritten by, or never replaces, the D_03 views; no held `multi_asset` value passes through this list into a served key.

VERDICT: HOLDS-NONE

## T05 -- BD `D_00b.portal_timeseries.py:90-96, :690, :704` `ASSET_CLASS_LABELS` + name-pattern `_classify_asset`

- Served artifact: `aua_mix` block of `s3://opal-data-bd/gold/artifacts/timeseries_chart.json` and `platinum/firm/timeseries_chart.json` (LastModified 2026-10-06 05:32:01Z and 05:56:13Z).
- READ: latest `aua_mix` period 2026-10: the six segments sum $2,037,980,919.10. The 2026-10-02 holdings_lots snapshot's open lots sum $2,037,980,919.10 (513,784 rows read, `asset_name`, `market_value`, `is_open`). Left side $2,037,980,919.10 = right side $2,037,980,919.10: no dollars are lost. The list classes by NAME pattern with a catch-all `other`, never by the table class, so held `multi_asset` funds are counted inside Equities / Fixed Income / Other (a labelling question, not a loss).

VERDICT: HOLDS-NONE

## T06 -- BD `D_00.portal_aggregates.py:113-115, :216-223` `ASSET_CLASS_LABELS` / `_classify_asset`

- Served artifact: none through these names. The Grep tool over `D_00.portal_aggregates.py` returns the definitions only (lines 98, 113, 216): `_classify_asset` and `ASSET_CLASS_LABELS` have no call site in the file, and no other file calls `_classify_asset(` from D_00 (other `D_00.portal_aggregates` mentions in `data/` are comments and source citations). The comment "used by build_snapshots via _classify_asset" names a function that no longer calls it.
- Reading: the list is not exercised, so it loses nothing in any artifact.

VERDICT: HOLDS-NONE

## T07 -- Inflection `INF_D_02d.firm_mix_summary.py:76-80` `_CLASS_BUCKETS` (equity, fixed_income, cash, alternatives)

- Served artifact: `s3://opal-data-inf/platinum/firm/mix_summary.json` (LastModified 2026-10-06 12:51:27Z) and `gold/artifacts/firm_mix_views.json` (12:51:23Z).
- READ: `mix_summary.json` `classification_method` `orion_native_v1`; its four classes sum to the composition's $208,044,040.13 (equity $134,418,694.54 + fixed_income $57,582,402.33 + cash $10,281,261.26 + alternatives $5,761,682.00); `firm_mix_views.json` last quarterly point values sum $208,044,040.13 = `total_aua` $208,044,040.13.
- Reading: the chain classes by Orion `product_category` / Morningstar category (INF_D_03 docstring), never by the canonical table class, so a table `multi_asset` never reaches the list; the held $40,560.31 sits inside the four served buckets and nothing is lost.

VERDICT: HOLDS-NONE

## T08 -- Inflection `INF_D_03.composition_artifacts.py:120-126` `_ASSET_CLASS_LABELS`

- Served artifacts: `s3://opal-data-inf/platinum/firm/firm_composition.json`, `platinum/advisors/<id>/composition.json`.
- READ: firm: `total_market_value` $208,044,040.13 = sum of four mix classes $208,044,040.13, `unclassified` count 0 / $0.00. Advisors: 5 of 5 compositions read sum to their totals (205,146.38; 29,816,578.11; 12,827,209.29; 24,710,168.09; 140,690,084.64; every difference $0.00); the sixth directory (`unknown`) has no composition file.
- Reading: classification is Orion-native (`_bucket_from_orion`), so the table class is never an input; no gap.

VERDICT: HOLDS-NONE

## T09 -- Inflection `INF_D_04b.client_publishers.py:81` `_ASSET_CLASS_ORDER`

- Served artifact: `s3://opal-data-inf/platinum/clients/<household_id>/composition.json` (written 2026-10-06 12:51Z).
- READ: all 315 composition files: 315 of 315 have mix pct summing to 1 within 0.001; class keys seen across the 315: alternatives, cash, equity, fixed_income only.
- Reading: Orion-native bucket map (`_bucket_from_orion`); no table class enters, none dropped.

VERDICT: HOLDS-NONE

## T10 -- Inflection `INF_D_06.client_timeseries.py:92-96` `CLASS_*` constants

- Served artifact: `s3://opal-data-inf/platinum/clients/<household_id>/timeseries.json` (`mix_periods`, written 2026-10-06 12:52Z).
- READ: all 317 household files: every non-zero period has `equity_pct + fixed_income_pct + cash_pct + alt_pct` = 100 within 0.1; 0 periods off, 0 files affected. The code sends every ticker the Orion map does not place to `alternatives` (`get_class` default `CLASS_ALTERNATIVES`), so the four buckets always close.
- Reading: no class outside the four can be produced; no loss.

VERDICT: HOLDS-NONE

## T11 -- Inflection `INF_D_07a.firm_concentrations.py:192-202` `_classify_asset_class` (Orion product category, residue `other`)

- Served artifact: `s3://opal-data-inf/platinum/firm/firm_concentrations.json` (LastModified 2026-10-06 12:52:58Z, data_as_of 2026-10-05).
- READ: 20 securities, `asset_class` values `equity` and `fixed_income` only; diagnostics `classifier_unmatch_rate` 0.0, `other_rate` 0.0. The artifact is a top-25 security drill-down, not a mix: it states no class sum for a `multi_asset` to break, and an unplaced class would land in `other`, not vanish.
- Reading: no held `multi_asset` is lost. SEPARATE FINDING (surprise row W20-S4): `total_firm_aua` $389,707,543.56 is 1.873 times the same-day `firm_composition.json` total $208,044,040.13, and IEFA reads $40,941,476.76 here vs $21,495,407.99 there; the gap ($181,663,503.43) is not the held `multi_asset` ($40,560.31).

VERDICT: HOLDS-NONE

## T12 -- 49F runner `d06_firm_mix_summary.py:46-47` `CLASS_ORDER` (equity, fixed_income, alternatives, unclassified)

- Served artifact it would write: family `platinum/firm/mix_summary` through `ShapeFrozenPublisher`, from a FROZEN LOCAL mirror of the 2026-08-07 graded partition set (module docstring: "S3 deliberately NOT read").
- READ: the served `s3://opal-data-bd/platinum/firm/mix_summary.json` (LastModified 2026-10-06 05:46:40Z) has eight class keys (equity ... other, including commodities, structured, cash), which this runner never emits (it emits four); its mix sums $1,994,163,061.52 = its embedded composition total $1,994,163,061.52, pct sum 1.0. The runner is not the writer of the served key; it reads an 08-07 mirror that predates every `multi_asset` row.
- Reading: no served byte comes through this list; the served key it shares is the BD gold's (T01/T02 lineage).

VERDICT: HOLDS-NONE

## T13 -- 49F runner `d09_firm_timeseries_overview.py:162-165` zero-filled mix rows

- Served artifact it would write: `platinum/firm/timeseries_overview.json` mix block (the NMNC/NMEC zero-filled rows), same frozen local mirror.
- READ: served `s3://opal-data-bd/platinum/firm/timeseries_overview.json` (LastModified 2026-10-06 05:56:02Z): its `mix` rows carry eight classes (the runner's rows carry four); not the runner's bytes. The runner's rows are zero-filled by construction (`total_aua 0.0`), so they hold no dollar to lose.
- Reading: not exercised against a held `multi_asset`.

VERDICT: HOLDS-NONE

## T14 -- 49F runner `a07_dim_asset_classification.py:336` `_CLS_RANK` (alternatives, cash, fixed_income, equity)

- Served artifact it writes: the A_07 `dim_asset_classification` parquet and `alias_key_expansion` parquet under `--output-root` (a local directory; `to_parquet` at :462-465 and :572-575). I could NOT read this artifact: no `dim_asset_classification` prefix exists at the roots of `opal-data-bd`, `opal-data-cot` or `opal-data-inf` under `dimensions/`, `gold/dimensions/`, `gold/canonical/` or the bucket root (listed, CommonPrefixes).
- Code read in its place: `_CLS_RANK` only orders alias-variant hits when STEP A (the representative's own class) did not classify; `_CLS_RANK.get(vac, 9)` gives a class outside the map rank 9, still chosen if it is the only hit (`ac = hits[0][2]`), and a STEP-A class is copied verbatim (`"asset_class": ac if ac else "UNCLASSIFIED-LOUD"`). A `multi_asset` class is therefore passed through, never dropped. An artifact I can read that shows the same: the served 49F artifacts T01-T03 are written by the BD gold, not from this dim, and lose none through this list.
- Reading: nothing is lost by this list on the code read plus the readable served 49F keys.

VERDICT: HOLDS-NONE

## T15 -- Cottonwood runner `runners_cot/d08_cot_mix_summary.py:48-57` `known` set (any other class raises `CLASS-DOMAIN FAIL`)

- Served artifact it would write: `s3://opal-data-cot/platinum/firm/mix_summary.json`.
- READ: the served key (LastModified 2026-10-06 11:38:31Z, data_as_of 2026-10-05) has eight class keys (equity, fixed_income, alternatives, commodities, structured, cash, unclassified, other) in `mix`; d08 emits only equity / fixed_income / alternatives and folds the rest (its docstring). The served bytes are the gold D_04 shape, not d08's.
- Reading: d08 is not the live writer; against a `multi_asset` position it raises (`SystemExit`) and writes no file, so it cannot publish a mix that omits the dollars. Nothing is lost through it today.

VERDICT: HOLDS-NONE

## T16 -- Cottonwood `D_03.composition_artifacts.py:102-111` `_ASSET_CLASS_LABELS` (loop at :387)

- Served artifacts: `s3://opal-data-cot/gold/views/firm_composition.json`; `gold/entities/clients/<id>_composition.json`. (No advisor composition exists: `gold/entities/advisors/` holds only `cottonwood_capital_advisors/book.json` and `timeseries.json`; see W20-S1.)
- READ (firm): LastModified 2026-10-06 11:38:14Z, data_as_of 2026-10-05: `total_market_value` $546,489,758.16; the seven served classes sum $546,223,106.49; the difference is $266,651.67. Held `multi_asset` on the same basis (D_03 steps 1-2 in process, 20,944 canonical rows, 4 ghost accounts excluded): $266,651.67, all SGIIX / CUSIP 32008F606; canonical AUA scale factor 1.0. Left $546,489,758.16 - right $546,223,106.49 = $266,651.67 = the held `multi_asset`, to the cent.
- READ (the four clients of the cell): `<id>_composition.json` total vs sum of classes: z09305621 $261,942.26 vs $236,079.28, short $25,862.98; z09305679 $2,556,929.28 vs $2,447,609.47, short $109,319.81; z09305703 $958,976.00 vs $933,415.95, short $25,560.05; z09305578 $1,146,795.30 vs $1,281,553.45, net -$134,758.15 (this one is the SGIIX drop of $49,876.03 less $184,634.18 of an unrelated effect: negative-value rows of -$214,526.15 sit in the total and a class with a non-positive total is skipped by `if class_mv <= 0`; the SGIIX drop in it is measured as $49,876.03 from the holdings). Each SGIIX amount equals the holdings figure to the cent.
- The label is added to the file in this commit (`'multi_asset': 'Multi-Asset'`), so the NEXT run carries the line; the served bytes above are the deployed code's and still lose it.

VERDICT: DROPS-TODAY

## T17 -- Cottonwood `D_00b.portal_timeseries.py:91-96, :642-645` `ASSET_CLASS_LABELS` + name-pattern classifier

- Served artifact it would write: the `aua_mix` block of `s3://opal-data-cot/gold/artifacts/timeseries_chart.json` (and the platinum copy).
- READ: `gold/timeseries/holdings_lots/` has 0 objects in `opal-data-cot` (the code's `HOLDINGS_LOTS_PREFIX`, `lib/s3_layout.py:49`; the legacy `gold/holdings_lots/` also 0), so `_build_aua_mix` returns `[]` ("no holdings_lots snapshots -- aua_mix skipped") and `if aua_mix_data:` omits the key. The served `timeseries_chart.json` (LastModified 2026-10-06 11:36:53Z) has no `aua_mix` key (keys: generated_at, data_as_of, firm_id, date_range, metadata, aua, nna, adv, geo, ofc, nna_ofc, growth_decomposition, nna_geo, nna_adv, geo_drill, nna_geo_drill, cla); `platinum/firm/timeseries_chart.json` has no key containing `mix`.
- Reading: the list is not exercised for Cottonwood; and by name pattern it would not read the table class anyway.

VERDICT: HOLDS-NONE

## T18 -- Cottonwood `D_00.portal_aggregates.py:111-113, :219-221` `ASSET_CLASS_LABELS` / `_classify_asset`

- Served artifact: none through these names. Grep over the file: definitions only (lines 96, 111, 214), no call site; no import of it elsewhere in `data/` (T06's search covers this file too).
- Reading: not exercised.

VERDICT: HOLDS-NONE

## T19 -- Cottonwood `D_02.advisor_client_detail.py:2310` `mix_fields`

- Served artifact it writes: `s3://opal-data-cot/gold/entities/advisors/<id>/mix_timeseries.json` (`advisor_mix_timeseries_key`; the legacy twin is `gold/advisors/<id>/mix_timeseries.json`, written by `D_03._publish_mix_views` only).
- READ: the full listing under `gold/entities/advisors/` is 2 objects (`cottonwood_capital_advisors/book.json`, `timeseries.json`); no `mix_timeseries.json`, `mix.json` or `composition.json` exists for any Cottonwood advisor. D_02's writer produces no served byte for this firm today (the advisor lookup `rel_architect_lookup.parquet` is also absent, W20-S1).
- Reading: nothing is served through this list for Cottonwood.

VERDICT: HOLDS-NONE

## T20 -- portal `PerfrpAllocation.tsx:43-46` `CLASS_LABELS` (four)

- Served artifact: a render path over `platinum/advi/<firm>/perfrp_allocation_<level>.json` (`advisor-intelligence.ts:1915`, `perfrpLeafBase`). READ: 0 objects whose key contains `perfrp_allocation` under `platinum/` in `opal-data-bd`, `opal-data-cot` and `opal-data-inf` (paginated, all pages); the file's own comment says no perfrp key is served today (the fetch 404s and the card renders its shell).
- Code read: `classLabel()` returns the producer's own token for a class not in the map, and rows are never dropped ("Absence is the one outcome this card may not produce"), plus a closure control that shows a total off 100%. Portal read from the base working copy (HEAD `481b3bcc`; the worktree's portal submodule is empty).
- Reading: not served today, and when served it passes an unknown class through.

VERDICT: HOLDS-NONE

## T21 -- portal `InflectionInsightsPanel.tsx:1022-1025` basket-filter legend (Equity, Fixed Income, Alternatives, Cash)

- Served artifact: a static legend beside the treemap; the treemap's data source was not traced here, the nearest served Inflection key is `platinum/firm/firm_concentrations.json` (T11). The legend is text only: no dollar is written or summed.
- READ: Inflection's `firm_concentrations.json` securities carry `equity` and `fixed_income` only (T11) and Inflection's chain emits only the four legend classes (T07-T10), so no `multi_asset` tile exists for the legend to omit.
- Reading: no value is lost; the legend is cosmetic.

VERDICT: HOLDS-NONE

## T22 -- portal `src/api/endpoints/advisor-intelligence.ts:842-850, :1201-1210` `FirmMixPeriodPoint` built from `*_pct` fields (four classes)

- Served artifacts it reads: the Inflection advisor book's `headline.historical_quarters` (per-class buckets set to zero by design, comment :833-838; that source key was not read here) and the Inflection household `platinum/clients/<id>/timeseries.json` `mix_periods`.
- READ: the household `mix_periods` it maps: 317 of 317 files, 0 periods off 100 (T10); the four `*_pct` fields close, so the four-class map drops nothing. `historical_quarters` carries `total_aua` only (no class value exists to lose; the zero buckets are a stated follow-on, not a `multi_asset` loss).
- Reading: the adapter serves only Inflection, whose artifacts carry no fifth class; no held value is lost.

VERDICT: HOLDS-NONE

---

## SUMMARY

- Subjects triaged: 22 (T01-T22). Verdict DROPS-TODAY: 2 (T03 BD `D_03` $5,438,537.08; T16 Cottonwood `D_03` $266,651.67). Verdict HOLDS-NONE: 20.
- Exposure the HOLDS-NONE count hides (not today's loss, flagged for the issuer): T01 and T02 (BD `C_06`, `lib/mix_views`) publish the 77 holders' mixes without `multi_asset` on the first C_06 run against the current table; the served 10-04 run predates it. The same two lists were edited for Cottonwood only.
- Not read: the BD C_06 run's classifier state at 2026-10-04 05:27Z (timing inference only); any artifact for T14 (local output root); the portal pin `ec65c5d6` (the base working copy `481b3bcc` was read).
