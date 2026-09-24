# HoldingsSnapshot additive members -- asset class and model code (DSGN_IRPTV1 v0.6 CONTRACTS)

**Author:** 2.0.0_SA_COO~M, the Holdings producer, named by 1.0.0_SA_CTO in msg 100905. **Date:** 2026-09-24 ~22:2xZ.
**Order (the PRD's):**
1. Both schema copies admit the members. Writer: 2.0.0_SA_COO~P.
2. The portal accepts them. 2.0.0_SA_COO~D.
3. The producer emits them on the next republish of each firm, under a 1.0.0_SA_CTO GO per firm.

All members are optional in the schema; the producer states when a value is absent.

## On a node with `node_kind: SECURITY`

| Member | Type | Values | Rule |
|---|---|---|---|
| `asset_class` | string | `equity`, `fixed_income`, `alternatives`, `unclassified` | The canonical classifier's answer (`data/black_diamond/scripts/gold/lib/etf_classifier.py` `ETFClassifier.classify`, `hedge` folded to `alternatives` as the classifier does). `unclassified` where it returns empty. Never guessed by the page. |
| `sub_asset_class` | string or null | the classifier's `sub_asset_class` | Null where the classifier has none. |
| `asset_class_basis` | string | `TABLE`, `NAME_ALIAS`, `NAME_PATTERN`, `TICKER_SHAPE`, `NONE` | Which classifier layer answered. `NAME_PATTERN` and `TICKER_SHAPE` are the classifier's inferences; `NONE` pairs with `unclassified`. A consumer may treat an inferred class differently. |

The portal maps `fixed_income` to its `fixedIncome` key (`portal/src/lib/chartColors.ts` `ASSET_CLASS`). Cash-kind nodes
(`node_kind: CASH`) are not SECURITY nodes and carry no member.

## On a node with `node_kind: MODEL_LEAF`

| Member | Type | Values | Rule |
|---|---|---|---|
| `model_code` | string or null | an MDPF registry `member_id` (`data/mdpf/scripts/gold/mdpf_category_registry.py`, derived from `mdpf_revamp_model_crosswalk.CANONICAL_MODELS.model_key`) | Null when the model has no registry member (a Custom or third-party model). The page never reads the label to fill it. |

The five primary keys correspond one-to-one to the portal's canonical codes (`modelPortfolioColors.ts` `canonicalModelCode`):

| Registry key | Code |
|---|---|
| `opal_ultra_short_term` | UST |
| `opal_short_term` | ST |
| `opal_intermediate` | INT |
| `opal_long_term_conservative` | LT |
| `opal_long_term_aggressive` | ULT |

Coverage today, before any measurement:
- **COT** resolves primary and SMA leaves to registry keys already (`holdings_snapshot.py` `cot_constituent_taxonomy`,
  `:1521-1542`); custom models carry none.
- **49F (SmartX) and INF (Eclipse)** model names are not yet resolved to the registry. That crosswalk is the producer's
  work; until it lands, their `model_code` is null, never inferred from a label.
