# Reader census for the ETF tag admission (`structured`, `commodities`) -- 2026-09-26

A read-only audit by a general-purpose subagent of 2.0.0_SA_COO~M. It answers the CTO's 101511 condition: census EVERY
reader of asset_class and show each handles the new values. The source is the 69 paths of the R5 census
(`CLASSIFIER_WIDENING_REQUEST_ROWS_AND_READERS_20260924.json`), plus readers added since, plus the portal rendering.

Prefixes: `bd/` = `data/black_diamond/scripts/`, `cot/` = `data/cot/scripts/gold/`, `v2/` = `infra/aws/lambda/v2_portal/`.
(ETF-C) marks a reader of `etf-classifications`, which already holds these values, so its verdict is what happens today.

## Part 1: the 69 paths

| Path | Verdict | Evidence | Served? |
|---|---|---|---|
| `bd/gold/lib/etf_classifier.py` | PASS_THROUGH (only `hedge` remapped) | :98-99, :107-108 | via callers |
| `cot/lib/etf_classifier.py` | PASS_THROUGH | :92-93, :101-102 | via callers |
| `data/assets/scripts/gold/runners_49f/a07_dim_asset_classification.py` | PASS_THROUGH into dim_asset_classification and alias_key_expansion | :230-239, :374, :526/:541; `_CLS_RANK` :336 falls back to 9 (tie-break only) | yes (gold dims read by d06, d08, perfrp) |
| `bd/classification/seed_bd_securities.py` | PASS_THROUGH: copies etf-classifications into bd-securities | :62-82; put_item replaces the whole item | writes the table |
| `data/inf/scripts/classification/classify_assets.py` | PASS_THROUGH (lookup); LLM writer gate drops new values | :144-153, :231; gate :67/:328 | no |
| `v2/_shared/etf_classifications_dynamodb.py` (ETF-C) and 2 identical copies | PASS_THROUGH; `classify_holdings` :177-190 would KeyError but has no caller | :94 | via callers |
| `v2/partners/lambdas/opal-partners-data/etf_classifier.py` | PASS_THROUGH | :80-81, :89-90 | via lambda |
| `v2/yang_pipeline/positioning/yang-generate-holdings-attribution/lambda_function.py` (ETF-C) | PASS_THROUGH: raw `structured` beside `Equity`/`Fixed Income`; the subtotal lookup misses | :585, :594-597, :627, :643-647 | yes (holdings_attribution_data.json) |
| `data/assets/scripts/gold/build_satellites_registry.py` (ETF-C) | PASS_THROUGH | :350-353, :479 | yes (satellites) |
| `lib/research/identity/positioning_chain.py` (ETF-C) | PASS_THROUGH | :276-277 into :405 | UNDETERMINED |
| `bd/gold/C_06.client_mix_timeseries.py` | ALLOWLIST_DROP from the mix; the pct_sum check still passes, so the mix sums below 1 | MIX :179, loop :507-508, :500 | yes |
| `cot/C_06.client_mix_timeseries.py` | ALLOWLIST_DROP | :173, :477 | yes |
| `bd/gold/D_03.composition_artifacts.py` | ALLOWLIST_DROP from mix[]; still counted in the total and global top holdings, not counted as unclassified | :101-107, :339, :387, :397 | yes |
| `cot/D_03.composition_artifacts.py` | ALLOWLIST_DROP | :102-109, :391 | yes |
| `bd/gold/D_04.client_portal_summary.py` | ALLOWLIST_DROP in the firm composition (keyed on C_06's classes) | :457-464 (account mix :1283 and positions :2835 are dynamic) | yes |
| `cot/D_04.client_portal_summary.py` | ALLOWLIST_DROP | :561-568 (dynamic :1381) | yes |
| `bd/gold/E_25.aua_decomposition_audit.py` | ALLOWLIST_DROP (reads 3 keys) | :144-147 | audit |
| `bd/gold/B_01b.classify_new_securities.py` | ALLOWLIST_DROP (writer gate; the prompt steers VIX and commodities to alternatives) | :43, :314-316, :45-51 | writes the table |
| `cot/B_01b.classify_new_securities.py` | ALLOWLIST_DROP (writer gate) | :48, :331-333 | writes the table |
| `bd/classification/classify_bd_securities.py` | ALLOWLIST_DROP (writer gate) | :22, :194-196 | writes the table |
| `infra/aws/lambda/semantic-news-layer3-curation/lambda_function.py` | ALLOWLIST_DROP (equity and fixed_income only, as for alternatives today) | :76, :87 | yes (news) |
| `bd/silver/build_bd_assets_dim.py` | DEFAULT_BUCKET: unmapped, so the BD coarse class is kept (alternatives or other) | :57-62, :144-148, :65-72, :166 | UNDETERMINED |
| `v2/yang_pipeline/seed-etf-constituents.py` | DEFAULT_BUCKET `unknown` | :133-138, :189 | writes etf-classifications |
| `portal/src/pages/InvestorReporting/tabs/holdings/assetClass.ts` | DEFAULT_BUCKET `Unclassified`; colours for Structured and Commodities already exist but have no mapping | :22-23, :33-40, :45 | yes |
| `v2/partners/lambdas/opal-partners-data/lambda_function.py` | EXPLICIT_HANDLING (dynamic group-by, title-case) | :1270-1277, :1303 | yes |
| `v2/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py` (ETF-C) | EXPLICIT_HANDLING | :296-305, :324-342, :800-804 | yes |
| `portal/src/pages/Positioning/shared/satelliteAdapter.ts` | EXPLICIT_HANDLING | :109-117, :395-410 | yes |
| `bd/classification/seed_canonical_securities.py` | EXPLICIT_HANDLING on its etf-classifications read, but writes bd-securities unconditionally | :267-285, :349-356; write :314-337 | writes the table |

The other 39 are NOT_A_CLASS_READER: the census script, build_satellites_characteristics (name and management_style
only), chain_49f_entrypoint, backfill_name_aliases, resolve_tickers, the bd and cot copies of B_01, E_18,
build_canonical_prices_v2, gold_dispatch.sh and s3_layout, build_gold_firm_composition (Schwab dim),
etf_positioning_publisher (name only), INF_D_03 and INF_D_07a (Orion), build scripts and source maps, the two SmartX
silver.py, a deploy.sh, 10 Terraform files, and satelliteSet.ts (a type declaration).

**Counts:** NOT_A_CLASS_READER 39, PASS_THROUGH 13, ALLOWLIST_DROP 11, DEFAULT_BUCKET 3, EXPLICIT_HANDLING 4, RAISES 0
(total 69).

## Part 2: readers not in the 69

| Path | Verdict | Evidence | Served? |
|---|---|---|---|
| `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` | RAISES | ASSET_CLASS_VALUES :748, refuses :800-801 | yes (IR Holdings) |
| both `HoldingsSnapshot.schema.json` (`_contracts/`, `holdings/contracts/`) | closed enum; a validator refuses | :523-531, :578-586 | contract |
| `portal/src/pages/InvestorReporting/contracts/adapt.ts` | DEFAULT_BUCKET `unclassified` | :983-993, :1005 | yes |
| `data/assets/scripts/gold/runners_49f/d06_firm_mix_summary.py` | RAISES (SystemExit outside CLASS_ORDER) | :46-47, :96-98 | yes (platinum firm mix) |
| `data/cot/scripts/gold/runners_cot/d08_cot_mix_summary.py` | RAISES | :51-54 | yes |
| bd and cot `lib/mix_views.py` | ALLOWLIST_DROP; the gap lands in `unclassified` | :19, :84-99 | yes |
| IR portal SecurityList :101/:157, HoldingsTreemap :152/:160/:310, DrillTree :261/:494 | DEFAULT_BUCKET `Unclassified` via assetClassOf | as listed | yes |
| portal `contracts/index.ts` :797, `contracts/wire/HoldingsSnapshot.ts` :104 | closed type unions (compile time) | as listed | n/a |
| `runners_49f/perfrp_emit_core.py` | EXPLICIT_HANDLING (dynamic); the portal PerfrpAllocation.tsx :48-54 shows the raw token | :688-690, :710-712 | yes |
| `infra/aws/lambda/exec-summary-generator/platinum_reader.py` | PASS_THROUGH into LLM context | :191 | indirect |
| `v2/yang_pipeline/seed-etf-classifications.py` | EXPLICIT_HANDLING (refuses conflicts) | :72-95, :230-247 | writes etf-classifications |

## Part 3: portal rendering of an unknown class

- **IR Holdings:** adapt.ts :1005 folds it to `unclassified`, and assetClass.ts :45 renders a grey "Unclassified". The
  page never receives one today because the producer raises first.
- **Advisor Intelligence composition:** `normalizeMixTo4Class` (composition.ts :32, :43, :90-93) keeps the listed
  classes only and skips others (:108), then re-percents over the kept classes (:119, :125). The other slices inflate
  with no visible gap. The partner `ordered` lists (e.g. 49financial/layout.ts :89, cottonwood/layout.ts :125) are
  fixed keys.

## Must change before the new values are written

1. **Crashes:** holdings_snapshot :748/:800 and both schema enums; d06 :96-98; d08 :51-54.
2. **Silent drops in served output:** both C_06; both mix_views; both D_03; both D_04; portal composition.ts
   :32/:108 and the Advisor Intelligence fixed-key lists; E_25 (audit only).
3. **Wrong class:** build_bd_assets_dim :57-62; portal adapt.ts :1005 and assetClass.ts :33-40.
4. **Writers that would undo it:** re-running seed_canonical_securities (:314-337) resets VXX/UVXY/PDBC to equity and
   QBER to fixed_income; seed_bd_securities (:82) overwrites whole items. The LLM writer gates refuse the new classes
   for new securities only.

**Side finding, checked by ~M:** E_18 :206 writes stub rows with `asset_class: 'unknown'`, which would crash the same
three producers. A bd-securities scan at ~22:1xZ found 0 values outside {equity, fixed_income, alternatives, cash}
(10,877 items), so none exist today.
