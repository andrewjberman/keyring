# ETF Classifier tags vs the classification table vs served Holdings -- measured (CTO 101502, Andrew-direct ~21:2xZ)

2.0.0_SA_COO~M, 2026-09-26 ~21:4xZ. Andrew, verbatim, via the CTO: "securities which were already listed/tagged in the
ETF CLassifier table should retain the same classification. For example, VXX is tagged to "Structured" and GLD or
PHYS are tagged to "Commodities". The classification table shows both as "Alternatives", which is incorrect." Record:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_212xZ_ETF_CLASSIFIER_TAGS_TAKE_PRECEDENCE.md`.

## The two tables (read-only scans, 2026-09-26 ~21:3xZ)

- **ETF Classifier = DynamoDB `etf-classifications`:** 285 tickers (HASH `ticker`). `asset_class`: equity 211,
  fixed_income 61, commodities 7, structured 5, alternatives 1. It also carries `sub_asset_class` and `sector` (VXX:
  structured / Hedge / Volatility; GLD: commodities / Metals / Gold).
- **Classification table = DynamoDB `bd-securities`:** the table Holdings (`holdings_snapshot.classify_security`), COT
  and BD C_06, and a07 read through the ETFClassifier loader.
- **PHYS is NOT in `etf-classifications`.** In bd-securities it is `alternatives` ("Physical gold trust", gpt-4o-mini,
  2026-04-09). If Andrew means PHYS is Commodities, it has to be added to the ETF Classifier, or ruled by name.

## Why the categories collapse (both causes hold)

1. **Taxonomy.** The Holdings and COT asset_class list is `equity | fixed_income | alternatives | cash | other`
   (Holdings ASSET_CLASS_VALUES and the v1 contract; C_06 MIX_ASSET_CLASSES). `structured` and `commodities` are not
   members, so they cannot be served as they are. bd-securities stored them as `alternatives` (and the loader maps
   `hedge` to `alternatives`, etf_classifier.py).
2. **Which table is read.** No served producer reads `etf-classifications`; it is the Positioning family's table. So
   even an in-list tag (for example fixed_income) loses to whatever bd-securities says.

## Tag vs the classification table (285 ETF-tagged tickers)

| ETF tag -> bd-securities | Tickers |
|---|---|
| equity -> equity | 198 |
| fixed_income -> fixed_income | 58 |
| equity -> ABSENT | 13 |
| **commodities -> alternatives** | 6 |
| **structured -> alternatives** | 4 |
| fixed_income -> ABSENT | 2 |
| **fixed_income -> equity** | 1 |
| **alternatives -> equity** | 1 |
| **structured -> equity** | 1 |
| **commodities -> equity** | 1 |

## Served delta, per firm (served 2026-09-22 revisions, SECURITY nodes whose ticker is ETF-tagged)

| Firm | ETF tag -> served class | Nodes | $ | Tickers |
|---|---|---|---|---|
| 49F | structured -> alternatives | 6,448 | 20,987,194 | QBER, VXX |
| 49F | structured -> equity | 11 | 265,977 | JEPI |
| 49F | commodities -> alternatives | 16 | 241,817 | GLD, IAU, SLV, USO |
| 49F | fixed_income -> equity | 1 | 14,969 | CASH |
| 49F | alternatives -> equity | 2 | 2,558 | VNQ |
| 49F | commodities -> equity | 4 | 952 | PDBC |
| INF | structured -> alternatives | 510 | 1,749,317 | UVXY, VXX |
| INF | commodities -> alternatives | 7 | 0 | GLD, SLV |
| INF | alternatives -> equity | 3 | 0 | VNQ |
| COT | commodities -> alternatives | 575 | 9,492,047 | GLD |
| COT | fixed_income -> equity | 624 | 2,868,029 | CASH, FXFXX |
| COT | structured -> alternatives | 381 | 2,089,681 | VXX |
| COT | structured -> equity | 15 | 1,219,918 | JEPI |

Nodes already equal to their tag: 49F 109,139; INF 12,428; COT 8,332. The per-firm JSON is
`ETF_CLASSIFIER_TAGS_VS_SERVED_20260926.json` beside this file.

## Two parts, one decision

- **Part A -- tags already in the list** (fixed_income, alternatives, equity). The tag wins by a precedence rule in
  the Holdings classifier: read `etf-classifications` first. Served delta: 49F CASH $14,969 and VNQ $2,558; INF VNQ $0;
  COT CASH/FXFXX $2,868,029. This is a producer change and can ride the R4 enable half.
- **Part B -- `structured` and `commodities`** (49F about $21.5M, INF $1.75M, COT about $12.8M). They cannot be
  served until the Holdings contract either (a) admits `structured` and `commodities` as asset_class values (portal
  mapping by ~D, and COT C_06 MIX if COT mix should show them too), or (b) carries the ETF tag in a separate member
  beside the 5-value class. That is a contract and taxonomy decision (the `other` precedent), and it is the ONE
  decision asked of the CTO before the half.
