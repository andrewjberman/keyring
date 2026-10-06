# MDPF_SECCLASS SC-e-20 census -- every class list or class-keyed branch that lacks `multi_asset`, outside the four edited Cottonwood files

By `0.9.0_WK_MDPF_SECCLASS~20`, 2026-10-06. READ ONLY: nothing below was edited; a gap becomes an amendment. Code at the worker
branch `wk-secclass-r7-20` (CLOUD HEAD `5942c2bb55` plus the SC-e-20 edit of the four Cottonwood files). The portal is a git
submodule that is not populated in the worktree, so the portal rows read the BASE checkout's portal working copy
(`C:/Users/AndrewBerman/Desktop/ajb_workspace/portal`, HEAD `481b3bcc`; the superproject pins `ec65c5d6`, so the portal rows
describe the working copy, not the pin).

Method: a Python sweep (file text, `*.py`, tests excluded) for the class vocabulary (`'fixed_income'` or `'alternatives'` as a quoted token),
plus a second sweep for `structured` / `commodities` / `unclassified` in files the first missed; then each hit read at its line and its
output keys read. "Feeds a served artifact" = the file writes (or is the only writer of) a key under `platinum/`, `gold/entities`,
`gold/views`, `gold/artifacts` or the portal's own render path. "Absent" = the list lacks `multi_asset` and holds no pass-through for it.

## DENOMINATOR

Files scanned (`*.py` for scripts, `*.ts` and `*.tsx` for the portal, tests and `node_modules` excluded):

| scope | files scanned | files carrying class vocabulary | of those, mentioning `multi_asset` |
|---|---|---|---|
| `data/black_diamond/scripts/gold` (49 Financial's chain) | 90 | 10 | 0 |
| `data/inf/scripts` (Inflection) | 123 | 6 | 0 |
| `data/assets/scripts/gold/runners_49f` | 73 | 3 | 0 |
| `data/assets/scripts/gold/runners_cot` | 0 (the directory does not exist; the Cottonwood runners live in `data/cot/scripts/gold/runners_cot`) | - | - |
| `data/cot/scripts/gold` (added: the Cottonwood tree beside the edited files, incl. `runners_cot` 25 files) | 84 | 9 | 4 (the edited B_01b, C_06, D_04 and lib/mix_views) |
| `portal/src/pages/AdvisorIntelligence` | 64 | 11 | 9 |

DENOMINATOR total: 90 + 123 + 73 + 84 + 64 = 434 files scanned across the five existing scopes.

## Rows

Columns: file and line | the list or branch | `multi_asset` absent | feeds a served artifact (what it writes).

### Black Diamond gold (49 Financial's chain)

| file:line | list or branch | multi_asset absent | feeds a served artifact |
|---|---|---|---|
| `data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py:182` | `MIX_ASSET_CLASSES` = equity, fixed_income, alternatives, commodities, structured, cash, unclassified, other | YES | YES: `gold/entities/clients/<id>.json` and `MIX_DAILY_SUMMARY` (:321, :372); its sum guard still runs over the aggregate (the SC-e-20 defect, unedited here) |
| `data/black_diamond/scripts/gold/lib/mix_views.py:25` | `MIX_ASSET_CLASSES` (same eight) | YES | YES: period views for clients, advisors and firm |
| `data/black_diamond/scripts/gold/D_03.composition_artifacts.py:101-111` | `_ASSET_CLASS_LABELS` loop at :373 `for asset_class in _ASSET_CLASS_LABELS` | YES (a class not in the map is never iterated, so it leaves the composition) | YES: firm, advisor and client composition keys, `FIRM_MIX_VIEWS`, advisor mix keys (:503-585) |
| `data/black_diamond/scripts/gold/D_02.advisor_client_detail.py:2289` | `mix_fields = ['equity','fixed_income','structured_notes','cash','other']` | YES (also lacks alternatives, commodities, structured, unclassified) | YES: `gold/entities/advisors/<id>/mix_timeseries.json` (:2342) |
| `data/black_diamond/scripts/gold/D_00b.portal_timeseries.py:90-96, :690, :704` | `ASSET_CLASS_LABELS` (equities, fixed_income, real_estate, alternatives, cash, other); name-pattern classifier :642-645 | YES | YES: `aua_mix` segments (:704, :1219); classes by NAME pattern, never by the table |
| `data/black_diamond/scripts/gold/D_00.portal_aggregates.py:113-115, :216-223` | `ASSET_CLASS_LABELS`; `_classify_asset` name-pattern branch | YES | YES (writes a portal aggregates parquet, :210; its reader not traced) |
| `data/black_diamond/scripts/gold/B_01b.classify_new_securities.py:44` | `VALID_ASSET_CLASSES` = equity, fixed_income, alternatives | YES | NO directly: validates the model's answer before it is written to the securities table (never offered `multi_asset`, by design) |
| `data/black_diamond/scripts/gold/E_16.unit_math_audit.py:163-175` | `classify_asset_type` name heuristic | YES | NO: an audit read |
| `data/black_diamond/scripts/gold/E_25.aua_decomposition_audit.py:146-160` | per-class pct from `mix_daily_summary` (equity, fixed_income, alternatives) | YES | NO: writes `gold/manifests/` audit (:426) |
| `data/black_diamond/scripts/gold/D_04.client_portal_summary.py:146-175` | `_classify_with_canonical` returns the table class verbatim, residue `unclassified` | NO (pass-through; no list) | YES, and not a gap |
| `data/black_diamond/scripts/gold/lib/etf_classifier.py:136, :216` | `CASH_USD` and cash rule return `fixed_income`; `classify` returns the table class verbatim | NO (pass-through) | not a list |

### Inflection gold

| file:line | list or branch | multi_asset absent | feeds a served artifact |
|---|---|---|---|
| `data/inf/scripts/gold/INF_D_02d.firm_mix_summary.py:76-80, :200-208, :394-402` | `_CLASS_BUCKETS` = equity, fixed_income, cash, alternatives; points built over the same four | YES | YES: `platinum/firm/mix_summary.json` (:66) |
| `data/inf/scripts/gold/INF_D_03.composition_artifacts.py:120-126, :183-194, :718-726` | `_ASSET_CLASS_LABELS` (five); `_bucket_from_orion` by Orion product category; views over four | YES | YES: platinum composition and `gold/artifacts/firm_mix_views.json` |
| `data/inf/scripts/gold/INF_D_04b.client_publishers.py:81, :138-148` | `_ASSET_CLASS_ORDER` = equity, fixed_income, alternatives, cash; Orion product-category branch | YES | YES: platinum client summaries |
| `data/inf/scripts/gold/INF_D_06.client_timeseries.py:92-96` | `CLASS_*` constants (four) | YES | YES: platinum client timeseries |
| `data/inf/scripts/gold/INF_D_07a.firm_concentrations.py:192-202` | Orion product-category branch; everything else `other` | YES | YES: `platinum/firm/firm_concentrations.json` (:105) |
| `data/inf/scripts/classification/classify_assets.py:67` | `VALID_ASSET_CLASSES` = equity, fixed_income, alternatives, cash | YES | NO directly: validates the model answer written to the securities table |

### 49F runners (`data/assets/scripts/gold/runners_49f`)

| file:line | list or branch | multi_asset absent | feeds a served artifact |
|---|---|---|---|
| `data/assets/scripts/gold/runners_49f/d06_firm_mix_summary.py:46-47` | `CLASS_ORDER` = equity, fixed_income, alternatives, unclassified | YES | YES: `platinum/firm/mix_summary` (ShapeFrozenPublisher, :41); behaviour for a class outside the list not traced |
| `data/assets/scripts/gold/runners_49f/d06_firm_mix_summary.py:235` | five-way comparison recompute (equity, fixed_income, alternatives, cash, other) | YES | NO: comparison only |
| `data/assets/scripts/gold/runners_49f/d09_firm_timeseries_overview.py:162-165` | zero-filled mix rows (equity, fixed_income, alternatives, unclassified) | YES | YES: the timeseries overview's `mix` block (the NMNC/NMEC zero rows) |
| `data/assets/scripts/gold/runners_49f/a07_dim_asset_classification.py:336` | `_CLS_RANK` = alternatives, cash, fixed_income, equity (source-tie ranking) | YES | YES: the A_07 dim parquet every 49F emitter reads; a table class outside the rank was not traced |

### Cottonwood runners and the Cottonwood tree beside the four edited files (outside the named scope, found on the way)

| file:line | list or branch | multi_asset absent | feeds a served artifact |
|---|---|---|---|
| `data/cot/scripts/gold/runners_cot/d08_cot_mix_summary.py:48-57` | `known = {equity, fixed_income, alternatives, UNCLASSIFIED-LOUD}`; any other class raises `CLASS-DOMAIN FAIL` | YES (a `multi_asset` position would abort the runner) | YES: `platinum/firm/mix_summary.json` (runner form) |
| `data/cot/scripts/gold/D_03.composition_artifacts.py:102-111` | `_ASSET_CLASS_LABELS` loop at :387 `for asset_class in _ASSET_CLASS_LABELS` | YES (a `multi_asset` holding row is never iterated, so it leaves the served composition) | YES: Cottonwood firm, advisor and client composition |
| `data/cot/scripts/gold/D_00b.portal_timeseries.py:91-96, :642-645` | `ASSET_CLASS_LABELS`; name-pattern classifier | YES | YES: Cottonwood `aua_mix` segments |
| `data/cot/scripts/gold/D_00.portal_aggregates.py:111-113, :219-221` | `ASSET_CLASS_LABELS`; name-pattern classifier | YES | YES (portal aggregates parquet) |
| `data/cot/scripts/gold/D_02.advisor_client_detail.py:2310` | `mix_fields = ['equity','fixed_income','structured_notes','cash','other']` | YES | YES: Cottonwood advisor `mix_timeseries.json` |

### Portal Advisor Intelligence pages (`portal/src/pages/AdvisorIntelligence`, base working copy @481b3bcc)

| file:line | list or branch | multi_asset absent | feeds a served artifact |
|---|---|---|---|
| `portal/src/pages/AdvisorIntelligence/_shared/types.ts:1561, :1566-1568, :1607-1610` | `MixAssetClass` union (equity, fixed_income, alternatives, cash); `MixTimeseriesPoint` and `FirmMixPeriodPoint` fields | YES (compile-time type only; `FirmMixPeriodPoint` readers go through `Object.entries`, so the value is read) | NO: a type, no render |
| `portal/src/pages/AdvisorIntelligence/_shared/perfrp/PerfrpAllocation.tsx:43-46` | `CLASS_LABELS` (four) | YES, harmless: an unknown class falls back to the producer's own token (the file says so, :36-41) | YES: renders the allocation card, label unprettified |
| `portal/src/pages/AdvisorIntelligence/_partners/inflection/InflectionInsightsPanel.tsx:1022-1025` | basket-filter legend: Equity, Fixed Income, Alternatives, Cash only | YES | YES: a legend (the tiles beside it are drawn by data) |
| `portal/src/api/endpoints/advisor-intelligence.ts:842-850, :1201-1210` (outside `pages/`, the file the readers call) | builds `FirmMixPeriodPoint` from `*_pct` fields: equity, fixed_income, alternatives, cash only | YES | YES: the Books-tab `mix_periods` for sources that deliver `*_pct` fields (Inflection / headline path) |
| `portal/src/pages/AdvisorIntelligence/_shared/lib/composition.ts:42, :57` | `CANONICAL_CLASSES` and `CANONICAL_CLASSES_WITH_CASH` | NO (carry `multi_asset`) | YES; `normalizeMixTo4Class` (:100-135) now keeps it |
| `portal/src/pages/AdvisorIntelligence/_partners/cottonwood/layout.ts:129` | `assetClasses.ordered` | NO (carries `multi_asset`, `unclassified`, `other`) | YES |
| `portal/src/pages/AdvisorIntelligence/_partners/49financial/layout.ts:91`, `_partners/inflection/layout.ts:128`, `_partners/demo/layout.ts:77`, `_shared/types/TenantLayoutConfig.ts:369` | `assetClasses.ordered` | NO (carry `multi_asset`; 49F and Inflection and demo omit `unclassified` and `other`, which is a separate question) | YES |
| `portal/src/pages/AdvisorIntelligence/_shared/components/PartnerAnalytics.tsx:75-89`, `:625-645` | label map; `firmMixChartData` maps every served key | NO | YES |
| `portal/src/pages/AdvisorIntelligence/_shared/components/AdvisorAnalytics.tsx:664-670` | Mix chart class list | NO | YES |
| `portal/src/pages/AdvisorIntelligence/_shared/panels/ConsolidatedOverviewPanel.tsx:391` | legend list | NO | YES |

## Counts

Counted from the printed rows (one row = one list, branch or file-line group; a row naming several layout files is one row):

- Rows found: 36 (Black Diamond 11, Inflection 6, 49F 4, Cottonwood tree 5, portal 10).
- Lacking `multi_asset`: 28 (Black Diamond 9, Inflection 6, 49F 4, Cottonwood tree 5, portal 4: `types.ts`, `PerfrpAllocation.tsx`,
  `InflectionInsightsPanel.tsx`, `advisor-intelligence.ts`). The other 8 rows carry it or pass the table's class through.
- Of the 28 lacking, feeding a served artifact: 22 (Black Diamond 6: `C_06`, `mix_views`, `D_03`, `D_02`, `D_00b`, `D_00`; Inflection 5; 49F 3:
  `d06:46`, `d09`, `a07`; Cottonwood tree 5; portal 3: `PerfrpAllocation`, `InflectionInsightsPanel`, `advisor-intelligence.ts`).
  Not served: Black Diamond `B_01b`, `E_16`, `E_25`; Inflection `classify_assets`; 49F `d06:235`; portal `types.ts`.
- Cottonwood rows that change what a Cottonwood advisor sees for a client or firm that holds a `multi_asset` position:
  `data/cot/scripts/gold/D_03.composition_artifacts.py:387` (drops the class from the served composition) and
  `data/cot/scripts/gold/runners_cot/d08_cot_mix_summary.py:51` (raises on it). Neither was in the named scope; both are reported as found.
- The acceptance one-liner counts the substring `| ` followed by a backtick, which also matches inside cells; it prints a larger number than 36.
  The row count is the one above.

Rows the sweep could not settle: whether `D_00` and `D_00b` run for Cottonwood at all (they are in the Cottonwood tree; the scheduler was not read); the
reader of the BD `D_00` parquet; how `d06` and `a07` behave for a table class outside their lists (their list was read, their handling was not traced).
