# The canonical classification table's coverage of served COT and BD holdings (Andrew-direct 12:4xZ, CTO 102302/102310)

2.0.0_SA_COO~M, 2026-09-28 ~12:5xZ.
- Andrew, verbatim, via the CTO: "The only classification table that matters is whatever ETFClassifier is connected
  to, the DDB table and associated infra that feeds into the 'Positioning' POSN page." / "THat is the canonical
  table."
- That table is DynamoDB `etf-classifications` (record @871b7458ec).
- Script `etf_classifications_coverage_census.py` produced `ETF_CLASSIFICATIONS_COVERAGE_20260928.json` (both beside
  this file). Everything is read-only.

## 1. Firm-tagged attributes: none

`etf-classifications` has 285 items. Its attributes are:
- ticker 285, name 285, asset_class 285, sub_asset_class 285, last_updated 285, updated_by 285;
- management_style 283, sector 115.
**0 values name a firm** (a scan of every attribute for 49financial/49f/inflection/cottonwood). The classifier's read
projects `ticker, asset_class, sub_asset_class` only (CTO 102310). Unlike bd-securities, whose 222 rows carry
firm_origin "inflection" (CRO 102305), it has nothing to exclude.

## 2. Coverage of served holdings (canonical/holdings 2026-09-25, positive market value)

| Firm | Served $ | Tickers | In etf-classifications | $ covered | In bd-securities (comparison) | $ with no ticker |
|---|---|---|---|---|---|---|
| COT (opal-data-cot) | $564.0M | 847 | 179 | **39.7%** | 817 (77.8%) | $105.3M |
| BD (opal-data-bd) | $1,955.2M | 1,449 | 228 | **68.1%** | 1,383 (73.7%) | $510.6M |

- **The gap: 668 COT tickers and 1,221 BD tickers are absent from the canonical table.**
- The largest by dollars:
  - COT: FCASH $20.3M (money market); SHYD $12.9M; MFEIX $10.5M; MEAR $10.4M; SHM $10.3M; SUB $10.3M; EVSM $10.3M;
    PEIYX $10.2M; PHYS $8.6M (Andrew named it Commodities); FSPGX $6.6M.
  - BD: KYCCF $3.6M, DFAC $3.0M, WMT $2.7M, PCOFX $2.6M, VMGMX $2.5M, VTSAX $2.5M, VFIAX $2.3M, VIGAX $2.2M, META $1.7M,
    ROAD $1.7M.
- The table is ETF-scoped. Single stocks and most mutual funds and money-market funds are absent.
- The rows with no ticker (manual assets, CASH lines and the like) cannot be covered by any ticker table; they stay
  with the name rules.
- **Where the two tables disagree on a covered ticker:** COT 7 and BD 10, listed in the JSON.

## 3. What re-pointing does and does not do

Re-pointing the COT gold classifier (`data/cot/scripts/gold/lib/etf_classifier.py:42-47`) to `etf-classifications`:
- classifies 39.7% of COT's served dollars from the canonical table;
- leaves the other 60.3% on the name rules and the ticker-shape heuristic, which is exactly how ALL of COT is served
  today (S173).
The served move is therefore limited to the covered ETFs until the fill lands. The fill goes through POSN via MSTR
(CTO 102310).

## 4. The Holdings producer

The Holdings producer (`holdings_snapshot.classify_security`) reads **bd-securities** through the same ETFClassifier
class, and its host can read that table. Under Andrew's word the canonical source is etf-classifications for Holdings
too. That is the same re-point, with the same gap.
