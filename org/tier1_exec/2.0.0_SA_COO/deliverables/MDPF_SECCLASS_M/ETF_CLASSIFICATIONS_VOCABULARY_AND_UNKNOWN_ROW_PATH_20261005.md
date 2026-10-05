# etf-classifications: its vocabulary, and how an unknown security gets a row (answer to 1.0.0_SA_CTO msg 105363)

**Author:** `2.0.0_SA_COO~M`, 2026-10-05 ~20:5xZ. **Claim:** measured (consistent full scan of the live table, 3,493 rows; module
headers read). No sector vocabulary beyond what is listed here is carried.

## 1. The vocabulary the table carries

- **asset_class (6 values, every row):** equity 2,746; fixed_income 671; multi_asset 33; structured 20; commodities 12;
  alternatives 11. `cash` and `other` are named in code comments but no row holds them.
- **sub_asset_class (3,256 of 3,493 rows; the table's one per-class sub-vocabulary):**
  - equity: US Large Cap 905, US Small Cap 474, Developed 395, International 238, EM 100, US Mid Cap 92, Global 67, then the
    ten GICS sector names: Financials 122, Consumer Staples 44, Communication Services 42, Consumer Discretionary 40,
    Industrials 63, Information Technology 59, Health Care 29, Materials 24, Utilities 22, Energy 16; 14 rows empty.
  - fixed_income: Municipal 231, Intermediate 58, Short Duration 40, High Yield 40, Ultra Short Duration 20, International 15,
    Structured Credit 13, Long Duration 8, TIPS 6, Cash 17; 223 empty.
  - multi_asset: Flexible 13, Fixed Mix 12, Target Date 8. structured: Hedge 17, Options Income 3.
    commodities: Metals 6, Commodities 4, Oil 2. alternatives: Real Estate 10, International Real Estate 1.
- **The GICS sector vocabulary IS the equity sub-class vocabulary** (the ten names above; Real Estate sits under alternatives).
  There is no separate GICS-sector field.
- **`sector` attribute (179 rows, all `classified_by seed`, ETF-constituent seed):** 36 distinct labels of a different grain
  (US Growth, Investment Grade, Government, Ultra Short, Gold, Japan, China, Technology, and so on), mixed style, region and
  category. It is not the GICS vocabulary. Its readers were not censused here (`get_sector` returns it), so whether anything depends on it is unread.
- **`industry` (1 row, WMT):** Bloomberg GICS industry-group text. **`instrument_kind`** (988 rows): `fund` or `single_security`.
  **`management_style`** (435): active 58, passive 105, unknown 272.
- **Row keys:** bare ticker (2,442), `CUSIP:<9>` (425, `identifier_namespace CUSIP`), `BBG:<ticker>:<exch>` (626,
  `identifier_namespace BLOOMBERG`, with `listing_country`, `security_bloomberg`).
- **Provenance fields:** `classified_by` scheduled 3,045; legacy 238; seed 197; model 13. `low_confidence` 14 rows;
  `classification_confidence` 13 rows (the model rows).

## 2. How an unknown security gets a row, through the table's own classifier

The path is `infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py` (plan, then `write()`); `ETFClassifier`
(`etf_classifications_dynamodb.py`) only reads (`get_classification`, `get_asset_class`, `get_sector`, `classify_holdings`).

1. **Plan.** For a ticker the table LACKS, in order, first direct hit wins; a value is used only if it is already a member of the
   table's own vocabulary (`TableVocabulary`, read from the seed and the live table), never through a fold:
   (i) the bd-securities row, read as input only; (ii) Bloomberg GICS sector, only where it equals an existing equity
   sub-class; (iii) the Schwab security master's own class and sub-class.
2. **No guess.** A ticker with no direct match gets no row and is listed UNRESOLVED by name. No outside model is called in this
   path.
3. **Write.** One conditional put (`attribute_not_exists(ticker)`): an existing row is never replaced. `classified_by scheduled`.
4. **The one model-shaped precedent:** 13 rows `classified_by model`, `updated_by mdpf-secclass-model`, carrying
   `classification_confidence` (0.88 on the sample read) and `low_confidence`, written by `write-model-rows.py` from a reviewed set.
   So a model verdict fits the row shape today only as `classified_by model` plus those two fields, landed from a reviewed set file.
5. **Producers in service:** the FWD-10 Lambda `mdpf-secclass-new-security-lambda` (daily, MON-FRI 10:00 ET; a NEW US ticker is
   written only with a resolved sub-class, batch 263 condition 2), the CUSIP rows writer, and the per-firm detectors.

## 3. What this does not say

- Whether an AI classifier verdict may write a row without a reviewed set is not decided by this record; today none does.
- The `sector` attribute's grain is described, not ruled on.
