# MDPF_SECCLASS BD forward fix 2 -- the mapping from bd-securities to the canonical table, for the 290 tickers (PROPOSAL)

**Author:** `2.0.0_SA_COO~M`, 2026-10-02 10:1xZ. **For:** `1.0.0_SA_CTO` to rule (batch 117 item 4 (ii): "the 290 tickers have rows,
through a mapped writer from bd-securities under its own half"; tick 6, msg 104138: "four-postulate record for the mapping").
**Status: PROPOSAL -- nothing built, nothing written.** Evidence: `R8_CHECKS/R8_BD_290_CENSUS_20261002T0953Z.json` (script
`R8_CHECKS/bd_290_census.py`, @8a489289f8).

## The population, measured

The 290 distinct tickers with a "Classification not found" line in the 2026-10-02 04:00Z Black Diamond gold log (11,878 lines).
Dollars are open lots in `gold/holdings_lots/2026-09-25.parquet` (the latest weekly lots): **12,511,120.89 USD** in all. None has a
row in `etf-classifications` now (2,719 rows read 09:53Z).

| group | tickers | open USD | what bd-securities says |
|---|---|---|---|
| A. direct match | 28 | 2,477.15 | a (class, sub class) pair the canonical vocabulary already holds |
| B. bd row, pair not in the vocabulary | 191 | 12,357,189.98 | 17 pairs, below |
| C. no bd-securities row | 71 | 151,453.76 | nothing (SCGB1 "BALANCED FUND", QCSTPX "CREF STOCK R2", CART Maplebear ...) |

## Four postulates

1. **MECE over a declared domain.** Domain: the 290, printed above as A + B + C = 290 and 12,511,120.89 USD. Every ticker lands in
   exactly one disposition below; none is left without one.
2. **Same grain.** One ticker, one (asset_class, sub_asset_class) row -- the grain of `etf-classifications` and of bd-securities.
3. **Intent coherence.** One axis: what the security IS. bd-securities' labels are model output (gpt-4o-mini, confidence about
   0.6, row S7), and the census shows the label and the security disagree inside most pairs, so a PAIR is not evidence of what
   each member is.
4. **State coherence.** A written row moves the classes of every firm that holds the ticker (Holdings tab at all firms, Black
   Diamond gold, Cottonwood after its re-point); an unwritten ticker stays `unclassified` and, with fix 1, stays IN the mix. No
   disposition moves a row that already exists (the write is the conditional put).

## Proposed disposition

| disposition | pairs | tickers | open USD | ground |
|---|---|---|---|---|
| **WRITE as is** | the 28 direct matches | 28 | 2,477.15 | the scheduled path's own direct-match rule (`etf_classification_scheduled.plan_rows` with the bd-securities lookup), `classified_by: scheduled` |
| **WRITE, class kept, sub class dropped** | fixed_income / Investment Grade; fixed_income / Floating Rate | 62 | 6,826,778.38 | the class agrees with the security in every member read; the vocabulary has no such sub class, so none is written -- the CUSIP path's own precedent (`SEC_ASSET_TYPE_DIRECT_MAP`: "Investment Grade Corporate Bonds" -> fixed_income, no sub class) |
| **WRITE, sub class renamed** | equity / Emerging Markets -> equity / EM | 7 | 233,014.00 | the same category under the table's own word |
| **PER TICKER, by the seed peer method** | alternatives / Structured Notes, Hedge fund, Commodities, Gold, Volatility, Options, Oil; equity / Commodities, Real Estate, High Yield; fixed_income / REIT, Money Market | 119 | 5,250,681.05 | the label is wrong for many members (FBALX and LIPKX are allocation funds labelled Structured Notes; GDX, GOLD, OIH are stocks labelled Gold or Commodities; O and AGNC are equity REITs labelled fixed_income; WH is a hotel company labelled Real Estate; IBIT is bitcoin). Each gets a seed row with its own ground, largest dollars first, as the 19 Cottonwood rows did -- or stays unclassified |
| **NOT WRITTEN** | `needs_review` (3, 46,716.55), no bd row (71, 151,453.76) | 74 | 198,170.31 | no evidence to write from; they stay unclassified, in the mix |

Check: 28 + 62 + 7 + 119 + 74 = 290 tickers; 2,477.15 + 6,826,778.38 + 233,014.00 + 5,250,681.05 + 198,170.31 = 12,511,120.89 USD
(computed from the census JSON, not typed).

Money market (VMFXX, GOFXX, 98,979.25 USD) is in the per-ticker group on purpose: batch 93 item 1 made cash the caller's rule and
withdrew FCASH and FIGXX as seed rows; whether a money market fund is `fixed_income / Cash` in the table is that ruling's to
extend, not this mapping's.

## What the writer would be

The conditional put (`etf_classification_scheduled.write`, `attribute_not_exists(ticker)`), driven like `write_cusip_rows.py`:
an operator-named set file, a dry run first, `classified_by: scheduled`, `updated_by: mdpf-secclass-bd-mapped`, the bd-securities
name as `name`. For the "sub class dropped" and "renamed" rows the set file carries the mapped pair explicitly; nothing maps at
run time. Its own half, after this ruling.

## The ask

Rule the five dispositions above (or name a different split). On "per ticker", say whether to start with the largest dollars
(FBALX 798,030; JHQTX 410,575; XCAPX 349,413; GLDM 247,751; NICHX 211,899 ...) as one seed act.
