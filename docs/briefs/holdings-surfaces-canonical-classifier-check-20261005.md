# CHECK -- do the holdings tables use ONLY the canonical ETFClassifier table?

- **Author:** `4.0.0_SA_CRO` (base), 2026-10-05 ~21:0xZ (5:0x PM Eastern). Read-only; nothing was changed.
- **Order:** Andrew-direct 2026-10-05 ~20:4xZ, verbatim in
  `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261005_204xZ_HOLDINGS_SURFACES_ONLY_CANONICAL_ETFCLASSIFIER_TABLE.md`.
- **The canonical table:** DynamoDB `etf-classifications` (3,493 rows today), read through its one client
  `infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py` (class `ETFClassifier`).
- **Claim marks:** MEASURED = read today from the served object or the file line named. NOT TRACED = found, not
  followed to a page. rivalfunds is out of scope on Andrew's word.

---

## 1. Answer

**No. Three of the five holdings tables checked take a label from somewhere other than the canonical table.**

| # | Surface | Canonical only? | What else labels it |
|---|---|---|---|
| 1 | Investor Reporting, Holdings tab | **No** | a second table (`bd-securities`) plus three guess layers behind it |
| 2 | Positioning page, ETFs mode | **No** | Bloomberg's sector field, set in the ETF gold producer; only the NAME comes from the canonical table |
| 3 | Positioning page, Models mode | **Backend yes; page no** | a hardcoded 37-ticker list in the portal overrides or fills the sub-asset label |
| 4 | Positioning page, Satellites mode | Backend yes | nothing found in the backend; whether its rows also pass the portal list of row 3 was not separated today |
| 5 | Attribution page, holdings table | **Backend not read today; page no** | its own second copy of the hardcoded list |

---

## 2. Evidence per surface

### 2.1 Investor Reporting, Holdings tab -- NOT canonical-only (the largest finding)

**The process (MEASURED, file lines):** `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py:938-972`
(`classify_security`). The canonical table answers first. A security it does not hold falls to
`bd_securities_fallback.py`, which reads the older `bd-securities` table and then guesses in three more layers:
a name-alias match, a name pattern (for example the word "TREASURY" or a coupon rate in the name means fixed income),
and a ticker-shape rule (any ticker of 1 to 5 letters is called equity). The module header declares this as a
temporary exception owned by `2.0.0_SA_COO~M`, on CTO ruling 103169, until the canonical table's coverage completes
(project MDPF_SECCLASS).

**The served page cannot tell the two tables apart:** a canonical hit and a `bd-securities` hit are both served as
basis `TABLE` (`holdings_snapshot.py:837-845`). Which table answered is kept only in the producer's own run census.

**What is served today (MEASURED on the live snapshots for business date 2026-10-02; "canonical" = the security's
symbol has a row in `etf-classifications`):**

| Firm | Distinct securities | Labelled from the canonical table | Share of holdings value from the canonical table | Not canonical, by layer (distinct securities) |
|---|---|---|---|---|
| Cottonwood | 1,259 | 735 | 77.3 percent | name alias 311; `bd-securities` row 177; unlabelled 28; ticker shape 5; name pattern 3 |
| 49 Financial | 1,832 | 1,336 | 97.3 percent | ticker shape 359; `bd-securities` row 63; name alias 53; unlabelled 20; name pattern 1 |
| Inflection | 1,601 | 827 | 98.6 percent | ticker shape 370; `bd-securities` row 213; name alias 149; name pattern 38; unlabelled 4 |

Read: by value the canonical table already carries most of 49 Financial and Inflection. **Cottonwood is the gap:
22.7 percent of its holdings value is labelled by something other than the canonical table**, 9.5 percent of it by
name alias and 8.6 percent with no label at all.

**A second, smaller non-canonical step on the same tab:** the portal component
`portal/src/components/holdings/HoldingsBreakdownTable.tsx:109-126` (`getSubAssetClass`), called from
`portal/src/pages/InvestorReporting/tabs/holdings/SecurityList.tsx:273`. When the served sub-asset label is missing
or not one the page recognises, it substitutes a label from a hardcoded list (section 2.3).

### 2.2 Positioning page, ETFs mode -- NOT canonical for class and sub-asset class

Served object `platinum/etfs/positioning_data.json`, built by `data/etfs/scripts/gold/etf_positioning_publisher.py`.
`asset_class` and `sub_asset_class` are passed through from the ETF gold tables (`:416-417`); the gold producer
`data/etfs/scripts/gold/etf_positioning_gold.py:1219-1249` sets them from Bloomberg's cash flag and GICS sector name.
Only the display NAME is read from the canonical table (`etf_positioning_publisher.py:241-255`). This was a
deliberate design (the sector axis is Bloomberg's GICS), and it is still not the canonical table.

### 2.3 Positioning page, Models mode -- backend canonical, page not

- **Backend (MEASURED):** the `yang-generate-positioning` Lambda reads asset class, sub-asset class, management style
  and name from the canonical table only (`lambda_function.py:25-76`, `:415-431`, `:1662`). Its inline copies were
  deleted on 2026-08-18. One inline list remains: `ETF_GEOGRAPHY_MAPPING` (`:95`), because the canonical table has no
  geography field.
- **Page (MEASURED):** `portal/src/pages/Positioning/tabs/HoldingsTab.tsx:575` and `:634` pass every holding through
  `getSubAssetClass`, which falls back to `portal/src/pages/Positioning/constants/etf-categories.ts`: a hardcoded
  list of 37 tickers with an asset class and a segment each. A served label the page does not recognise is replaced
  by this list's label.

### 2.4 Positioning page, Satellites mode -- backend canonical

`data/assets/scripts/gold/build_satellites_registry.py:312-351` and `build_satellites_characteristics.py:302-322`
read the canonical table through its one client and nothing else. A ticker with no row is served as null, not
guessed (`portal/src/pages/Positioning/shared/satelliteAdapter.ts:137`).

### 2.5 Attribution page -- its own copy of the hardcoded list

`portal/src/pages/Attribution/constants/etf-categories.ts` (119 lines) is a second copy of the list in 2.3, with its
own `getSubAssetClass` in `constants/holdings-shared.tsx:142`, used by `tabs/SelectionTab.tsx:141`. The backend that
feeds this table was not read today.

---

## 3. Other classification paths found, NOT TRACED to a page

Each of these labels securities without going through the canonical table alone. Which screen, if any, shows their
output was not followed today.

| Path | What it is |
|---|---|
| `data/assets/scripts/gold/runners_49f/a07_dim_asset_classification.py:108-252` | 49 Financial's own classifier: name patterns and the ticker-shape rule, reading `bd-securities` |
| `infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/etf_classifier.py` | a separate classifier file inside the partners data Lambda |
| `data/inf/scripts/classification/classify_assets.py`, `data/inf/scripts/gold/INF_D_03.composition_artifacts.py` | Inflection's own classification scripts |
| `data/canonical/schwab/gold/build_gold_firm_composition.py` | references the older securities table |
| `portal/src/lib/tickerRegistry.ts` (322 lines) | a hardcoded ticker-to-name-and-class registry in the portal, used by the market-performance summary |

**Already canonical (MEASURED):** the Black Diamond and Cottonwood gold libraries
(`data/black_diamond/scripts/gold/lib/etf_classifier.py`, `data/cot/scripts/gold/lib/etf_classifier.py`) read the
canonical table only, one ticker lookup, no guess. One addition: for a position with a BLANK ticker, the Black
Diamond library works out WHICH security it is from Black Diamond's own name and CUSIP records, then reads that
security's canonical row (`:207-230`). The class still comes from the canonical table; the identity step is a
process beside it.

---

## 4. What making it canonical-only would take (for the decision, not a design)

1. **Holdings tab:** remove the fallback. Before that, the canonical table needs rows for the securities the
   fallback labels today: about 496 for Cottonwood, 476 for 49 Financial and 770 for Inflection (distinct
   securities not in the table, less those already unlabelled; the three sets overlap and were not de-duplicated).
   Without those rows, removal turns them into "unclassified" on the page. This is the held MDPF_SECCLASS migration.
2. **Portal lists:** delete both `etf-categories.ts` files and the fallback branch of `getSubAssetClass`; a missing
   served label then shows as "Other" instead of a portal guess.
3. **ETFs mode:** a ruling is needed. The canonical table would have to carry a sector for every ETF constituent, or
   Bloomberg's sector stays as a declared second source for that one mode.
4. **Section 3:** trace each path to its screen first.

## 5. Limits

- "Canonical" in the section 2.1 table is tested by symbol membership in the table today, not by the producer's own
  record of which table answered; a security whose row was added after the 2026-10-02 snapshot counts as canonical
  here.
- Securities with a blank symbol are counted under the layer that labelled them.
- Client-portal pages, the advisor pages and exports were not walked; section 3 is a code read, not a page read.
- No page was rendered; this is a source and served-data check.
