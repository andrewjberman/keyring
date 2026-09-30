# Andrew-direct 2026-09-29 ~17:4xZ-17:5xZ -- one canonical per-security table feeds ALL holdings

**Recorded by:** 2.0.0_SA_COO~D (Andrew's words received in its session, verbatim below).

## The words

> "GLD and PHYS are both commodities not alternatives. That is represented properly in whatever table feeds
> Positioning, and it should be the same in the case of the Holdings tab on Investor Reporting; should feed in from
> that same table, and if we need to add an entry for PHYS there, then so be it, that is the proper order. With that
> said, VXX is also in that table displayed as Alternative, even though we use "Structured" as asset class for that and
> "Hedge" for Sub Asset Class, in the canonical table. THis is why I say that this should be pointed at the canonical
> table. That same table also has all the individual securities [...]. We do need a clever way to break out the
> individual groups from the ETF classes, so that is an open-ended question, maybe it restarts and we place single
> stocks after the last ETF-class asset, that might be the best approach there."

> "Not just "matching" the Positioning table, I think the table that feeds positioning should feed ALL HOLDINGS. Which
> means that is our canonical table for all holdings info, so that is where we feed in a row per security, including
> asset class, sub asset, and so on"

> "Better to use that table as a shared source for this kind of thing so we dont have duplicated tables and rules laying
> around. thats why i call it "Canonical""

## What the canonical table is (measured 2026-09-29 by a read-only trace)

- **DynamoDB `etf-classifications`** (us-east-1), hash key `ticker`; columns `asset_class`, `sub_asset_class`, `sector`,
  `name`, `management_style`; GSIs `asset-class-index`, `sub-asset-class-index`. Client
  `infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py:52-72`; seeded by
  `infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py` from `_shared/etf_classification.py`.
- It feeds Positioning's Models (`yang-generate-positioning/lambda_function.py:25-31, 53-74`) and Satellites
  (`data/assets/scripts/gold/build_satellites_registry.py:127, 133, 335-353`). Positioning's ETFs mode does NOT
  read it (`data/etfs/scripts/gold/etf_positioning_gold.py:986-1021`, Bloomberg GICS fields).
- Live rows: GLD = commodities / Metals (sector Gold); VXX = structured / Hedge. **PHYS: no row** (live get-item).

## Why Investor Reporting differs

- `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py:828-873` classifies through
  `data/black_diamond/scripts/gold/lib/etf_classifier.py`, which scans DynamoDB **`bd-securities`** -- a fork seeded
  from `etf-classifications` (`seed_bd_securities.py:21-22`) that has drifted: GLD, PHYS = alternatives / Gold,
  VXX = alternatives / Volatility; the classifier also folds `hedge` into `alternatives` (`etf_classifier.py:99,108`).
- Portal: `portal/src/pages/InvestorReporting/tabs/holdings/SecurityList.tsx:149` calls
  `getSubAssetClass(ticker, undefined)`, discarding the served sub-asset, so GLD/PHYS/VXX fall to 'Other'.

## The duplicates Andrew's directive retires (each assigns asset class or sub-asset to tickers)

`bd-securities` and its readers: `data/black_diamond/scripts/gold/lib/etf_classifier.py`, `data/cot/scripts/gold/lib/etf_classifier.py`,
`data/assets/scripts/gold/runners_49f/a07_dim_asset_classification.py:58,220`, `data/black_diamond/scripts/silver/build_bd_assets_dim.py:154`,
`data/black_diamond/scripts/gold/D_03.composition_artifacts.py:116`, `data/black_diamond/scripts/classification/seed_canonical_securities.py`
(writes both tables; VXX = equity/Volatility). Lambda copies: `partners/lambdas/opal-partners-data/etf_classification.py:230,235`
(VXX = equity, GLD = other) and `etf_classifier.py:9`; `yang-generate-etf-returns/etf_classification.py:115`;
`yang-generate-holdings-attribution/etf_classifications_dynamodb.py` (second client copy);
`01_market_overview/.../market-overview-tiered-generator/lambda_function.py:67`; `yang-generate-positioning/lambda_function.py:324`
(alias map). Other: `lib/research/identity/positioning_chain.py:163`. Front end: `portal/src/pages/Positioning/constants/etf-categories.ts:11-66`
(UVXY = Equity/Volatility), `portal/src/components/holdings/HoldingsBreakdownTable.tsx:69,129`. Deliberately separate:
`data/canonical/schwab/gold/build_gold_firm_composition.py:7` (Schwab as security master).

## Open design question (Andrew's)

How single stocks break out from the ETF classes in a holdings table; his lean: the ordering restarts and single stocks
are placed after the last ETF-class asset.
