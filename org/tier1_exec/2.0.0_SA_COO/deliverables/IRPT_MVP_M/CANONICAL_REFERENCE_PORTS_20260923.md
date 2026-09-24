# IRPT canonical reference capability handoff

M, under CTO fd32cac392 and exact message182732; Y request182816.
This is a source-only handoff with four offline characterization checks, not an
installed reader or a live-source availability claim. Combined runtime integration
remains first priority. No source producer, cloud, provider, secret or push action.

## Existing sources and actual callable interfaces

The exact seven inspected paths, last-change commits and inspected-byte SHA256s
are in CANONICAL_REFERENCE_EVIDENCE_20260923.json. The denominator is those seven
source files, not every deployed service or every security in the estate.

| Surface | Existing interface / output | Capability and limitation |
|---|---|---|
| data/assets/scripts/gold/runners_49f/a07_dim_asset_classification.py at c85701ebca | classify(ticker, asset_name, ticker_map, name_map) -> (asset_class, classification_source); build emits dim_asset_classification/date=D/data.parquet and manifest | Canonical all-firm held-security classification, asset grain. Read the materialized dimension; do not invoke its build or _load_ddb in IRPT. Rows carry security_key,ticker,cusip,asset_name,held_by_firms,asset_class,classification_source plus producer provenance. Key order is ticker, then CUSIP, then normalized NAME:. Held population is not an all-security universe. |
| data/assets/scripts/gold/runners_49f/a03_dim_security.py at 0205eef992 | build_dim_security(sec, asof=...) -> dataframe,manifest; TABLE dimensions/dim_security | Schwab sec3 identity rows contain security_key,cusip,ticker_symbol,security_description,optional security_type. Key order is CUSIP, then ticker, then description hash. Scope differs from A07 and identical field names do not establish a join. Builder drops duplicate keys, keeping first with a warning; consumer must retain that limitation. No reader with the requested two-argument namespace API. |
| infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py at b0e1f33471 | ETFClassifier.get_classification(ticker) -> dict or None; get_asset_class/get_sub_asset_class etc. | Existing Yang ETF metadata table interface. get_classification returns None for BOTH no Item and SDK failure; cannot prove NOT_FOUND. Constructor creates a cloud client; not invoked here. Query lists also collapse error to empty. |
| infra/aws/lambda/v2_portal/_shared/etf_classification.py at eeec3e9d62 | ETF_CLASSIFICATIONS and ETF_SUB_ASSET_CLASS; get_asset_class(ticker,default='equity'), get_sub_asset_class(ticker,default='') | Existing static ETF vocabulary: 136 asset mappings and120 subasset mappings at this cut. Asset values alternatives,commodities,equity,fixed_income,structured; exact22 subasset values in evidence. Convenience functions contain defaults/inference, which must not become identity evidence or claimed sourced classification. |
| lib/research/identity/crosswalk.py at 282d3f769b | resolve(any_form,path=None) -> resolution/security_key/Bloomberg/exchange/share_class/provenance; load_crosswalk(path,refresh=False) | AMGT coverage identity only, not an IRPT/global security master. Explicit local path is offline; absent path reads cloud latest. Collision and miss both return UNRESOLVED (reason distinguishes ambiguity). No CUSIP-universe claim and no YCharts availability proof. Do not manufacture a research crosswalk for uploads. |
| data/black_diamond/scripts/gold/build_canonical_prices_v2.py at 64b6b9d65a | build pipeline emits silver/prices/canonical_prices.parquet: date,asset_name,ticker,price,source | Dated asset price series with transaction/Yahoo/interpolation/carry and scoped overrides. No callable dated_price(canonical_key,date). No explicit currency column or universal key/share-class proof in selected output. Has cloud client at module import; not imported/executed. |
| data/inf/scripts/gold/INF_build_canonical_prices.py at c184c85392 | resolve_prices_for_ticker(group_df); builder emits date,ticker,price,source to silver/prices/canonical_prices.parquet | Inflection ticker series with transaction/Yahoo/interpolation/carry/capped treatments and cash override. Not an immutable universal USD quote service; no currency column in selected output. Has cloud client at import; not imported/executed. |

Classification authority and identity authority must remain separate. A07's
classify() recognizes syntactically plausible short tickers with no reference row.
The existing algorithm can therefore classify an unbacked symbol without proving
it is a security. Y must not turn this into a candidate identity or provider FOUND.
The static ETF vocabulary is an existing named vocabulary, not a reason to flatten
other classification sources or map structured/commodities silently to equity.

## Exact consumer contract to install (not an existing runtime callable)

Reserve M semantic adapter home `_scope/security_reference.py` under
infra/aws/lambda/investor-reporting, plus focused `_scope/tests/test_security_reference.py`.
These paths are NOT created by this handoff and require the ordinary path-owner
check when implementation is paired. Existing canonical source producers retain
their owners. P owns transport/package/resource installation; Y owns resolver.

```python
identity(identifier: str, namespace: str) -> IdentityResult
dated_price(canonical_key: dict, date: str) -> PriceResult
taxonomy() -> TaxonomyResult
```

All ports are server-installed, never browser-selected. identity namespace is
explicit TICKER or CUSIP; raw names are not identifiers. Canonical key is the
source-qualified pair {source_namespace, value}, never a naked security_key
shared across incompatible dimensions. No suffix guessing, provider mapping,
name-hash minting, alias creation or automatic substitution in this adapter.

Common result keys: state, reason_code, provenance. State is AVAILABLE, ABSENT,
AMBIGUOUS or UNAVAILABLE. ABSENT means a complete successful read of the named,
bounded source at the named revision found no exact row; it NEVER means the
security does not exist or YCharts returned NOT_FOUND. Unknown/unread/failed/
partial source is UNAVAILABLE. Ambiguous exact matches retain all candidate IDs
without choosing one. Provenance includes canonical source path/namespace,
immutable artifact reference/version/hash, source as_of/schema and lookup scope.
Missing immutable evidence is explicit UNAVAILABLE, not a fabricated revision.

IdentityResult additionally has candidates[], each carrying source-qualified
canonical_key, original identifier fields, name/type where present, classification
values plus their original classification_source and provenance. One matching
row can be AVAILABLE identity evidence only within that source's population;
classification-only rows must be labelled classification evidence. A nonempty
classifier guess cannot synthesize an identity. No result field claims YCharts
FOUND; Y's separate deterministic provider receipt remains required.

PriceResult additionally has canonical_key, price (decimal string or null),
currency (USD or null), as_of (ISO date or null), price_basis and provenance.
AVAILABLE requires exact-date, finite positive Decimal, explicit USD evidence,
exact identity/share-class match and immutable source revision. No float-based
revaluation, nearest-date fill, interpolated/carry/capped value promotion, cash
price invention or auto-FX. Existing raw producer columns alone are insufficient
for these conditions: report UNAVAILABLE/CURRENCY_OR_IDENTITY_BASIS_UNAVAILABLE.
Date miss in a complete compatible source is ABSENT/PRICE_DATE_ABSENT. Conflicting
eligible same-key/date rows are AMBIGUOUS. Y surfaces SHARES_PRICE_UNAVAILABLE;
Dollars/weight template paths need no invented price to proceed.

TaxonomyResult additionally carries source-qualified asset_classes/sub_asset_classes
and exact source revision. Consume maintained literal vocabulary or materialized
source values; preserve separate vocabularies where they differ. Missing
classification metadata remains missing; no default-equity or inferred duration,
credit, region, exchange or capitalization. Existing source has no complete closed
region/credit/duration/cap taxonomy established by this inspection.

## Offline evidence

Four checks execute only the unchanged A07 classify/normalize_name AST bodies
and regex constants with synthetic local maps (no imports/clients/producers):

- ZZZZQ with no reference rows -> equity, regex-name: not identity evidence.
- Numeric unknown with no rows -> empty class, unclassified.
- Explicit fixture hedge row -> alternatives, dynamodb-ticker: preserve existing semantics.
- Synthetic MONEY MARKET name -> fixed_income, regex-name: classification only.

All four pass. AST literal reads retain the static ETF vocabulary count and exact
values; no API query or deployed data receipt is implied. Producer output column
and key-order findings are source inspection, not fresh artifact validation.

## Installation dependency and requested next artifact

No inspected installed IRPT port yet meets the identity/dated_price contract.
P must name the concrete existing materialized source reader, exact payload/schema,
immutable artifact receipt, permitted lookup population and runtime installer.
For Shares it must also supply the designated explicit currency, unit/share-class
and price-treatment evidence source. Without those, the truthful installed port
can only report UNAVAILABLE; this is a capability gap, not an Opal access refusal.
M can then bind the owned pure reader against those actual payloads with focused
offline controls. This avoids writing a generic new crosswalk/price database or
claiming a callback stub is installed capability. CTO decides any genuine source
or taxonomy conflict; no independent CVO wait. Signed custody policy is unchanged.

Y may continue the admitted template/resolver implementation using these explicit
absence states and fixtures while P supplies the concrete source installer.
Existing Y1385/P375/M485 paired source verdict583d2da remains bounded PASS and its
runtime/package/live proof remains separate. Push state LOCAL; no push/deploy.
