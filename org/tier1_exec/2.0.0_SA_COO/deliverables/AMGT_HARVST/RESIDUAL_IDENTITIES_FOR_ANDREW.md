# AMGT research folders -- IDENTITY RESIDUAL for Andrew

**Ask:** msgs 25672 / 25674. **Population:** the 89 AM-research coverage folders per Andrew-direct ~17:4xZ (msg 25677), NOT the 250/256 union.
**Read-only, no vendor call.** Sources: `universe/v1/2026-09-16.json`; the ingested SEC table `sec/harvest/bronze/company_tickers/date=2026-09-22` (10,459 tickers); the research workbooks on OneDrive.

## Counts

| | n |
|---|---|
| coverage folders | 89 |
| resolved by the pipeline | 33 |
| **unresolved at identity** | **56** |
| a workbook names a ticker, and it holds up | 17 |
| a workbook names a ticker that is SUSPECT | **2** |
| no workbook, folder-name ticker confirmed in the SEC table | 20 |
| **nothing found -- your call** | **17** |

## 1. WORKBOOK TICKER IS SUSPECT (2) -- it claims a US line that is not this company

A parser trusting the `Ticker:` cell would mint a WRONG identity silently. Only tickers whose own suffix says US
(or carries none) are judged here: the SEC table is US-only, so it cannot speak to `-FR`/`-CA`/`-CH`/`-JP` lines,
and their absence from it is NOT evidence.

| folder | workbook says | that US ticker is | workbook |
|---|---|---|---|
| Rio Tinto RIO LN | `HESAY-US` | **not in the SEC table at all** | Rio Tinto ONE PAGER 2026 02 26_v1.xlsx |
| Total Energies TTE FP | `PG-US` | **PROCTER & GAMBLE Co** | FactSet Based ONE PAGER TEMPLATE 2026 03 09_v1.xlsx |


**CORRECTED by `2.0.0_SA_COO~X` (msg 25689), and the correction is the useful part.** These two are NOT
at risk: Rio Tinto and Total Energies were already registered at 11:11Z as `RIO_LN_Equity` and
`TTE_FP_Equity`, from their own research reports' `(Ticker: RIO LN Equity)` / `(Ticker: TTE FP Equity)`
labels -- a better source than the workbook.

And the cause is sharper than "stale copy": the FactSet ONE PAGER template carries a PEER-COMPARISON
block, so a sheet copied from another name keeps that name's lines. `HESAY-US` and `PG-US` are peer
entries, the same class as the KPN/VOD/BT/ORA peer block and an AAPL placeholder that seat found.

**INSTRUMENT CAVEAT, therefore, for anyone reusing my scanner: it takes the FIRST cell labelled
`Ticker:` in the first 60 rows, and that cell can belong to a PEER rather than to the subject.** The 17
rows in section 2 are unaffected -- each was accepted only because the ticker agreed with its own
folder's company -- but a scanner that trusted position alone would inherit exactly this defect.

## 2. WORKBOOK NAMES A TICKER AND IT HOLDS UP (17) -- listing / share class included

| folder | workbook ticker | workbook |
|---|---|---|
| America Movil AXMB MM | `AMXB MM` | America Movil 2025 07 11.xlsx |
| AstraZeneca AZN | `AZN-GB` | AZN FactSet Based ONE PAGER 2026 06 22_v2.xlsx |
| Canadian National Railway CNR | `CNR-CA` | CNR CA FactSet Based ONE PAGER 2026 06 30_v1.x |
| Clorox CLX | `CLX-US` | CLX FactSet Based ONE PAGER 2026 06 12_v1.xlsx |
| Copa CPA | `CPA-US` | COPA FactSet Based ONE PAGER 2027 07 07_v1.xls |
| JD.com 9618 HK | `9618-HK` | JD. com FactSet Based ONE PAGER TEMPLATE 2026  |
| Michelin ML FP | `ML-FR` | Michelin FactSet Based ONE PAGER TEMPLATE 2026 |
| Mitsubishi UFJ Financial Group 8306 JP | `8306-JP` | MUFG FactSet Based ONE PAGER TEMPLATE 2026 03  |
| Nestle NESN SW | `NESN-CH` | Nestle FactSet Based ONE PAGER TEMPLATE 2026 0 |
| Nokia FH | `NOKIA-FI` | Nokia FactSet Based ONE PAGER TEMPLATE 2026 04 |
| Orange ORA FP | `ORA-FR` | Orange FactSet Based ONE PAGER TEMPLATE 2026 0 |
| Sanofi SAN FP | `SAN-FR` | Sanofi SAN FactSet Based ONE PAGER TEMPLATE 20 |
| Schlumberger SLB | `SLB` | SLB One Pager 2025 07 14_v1 WW.xlsx |
| Shopify SHOP CA | `SHOP-US` | SHOP CA FactSet Based ONE PAGER 2026 07 13_v1. |
| Telefonica Brazil VIVT3 BZ | `VIVT3 BZ` | Telefonica Brazil 2026 01 13_v1.xlsx |
| Tokyo Marine 8766 JP | `8766-JP` | Tokyo Marine FactSet Based ONE PAGER TEMPLATE  |
| Uber Technologies UBER US | `UBER` | UBER-Adam.xlsx |

## 3. NO WORKBOOK, FOLDER-NAME TICKER CONFIRMED IN THE SEC TABLE (20)

| folder | ticker | cik | SEC title |
|---|---|---|---|
| Adobe ADBE US | `ADBE` | 796343 | ADOBE INC. |
| Cadence CDNS US | `CDNS` | 813672 | CADENCE DESIGN SYSTEMS INC |
| Celsius CELH | `CELH` | 1341766 | Celsius Holdings, Inc. |
| Global Payments GPN | `GPN` | 1123360 | GLOBAL PAYMENTS INC |
| HEICO Corporation HEI US | `HEI` | 46619 | HEICO CORP |
| Idexx IDXX | `IDXX` | 874716 | IDEXX LABORATORIES INC /DE |
| Intuitive Surgical ISRG US | `ISRG` | 1035267 | INTUITIVE SURGICAL INC |
| MSCI Inc MSCI US | `MSCI` | 1408198 | MSCI Inc. |
| Mastercard MA | `MA` | 1141391 | Mastercard Inc |
| MercadoLibre MELI US | `MELI` | 1099590 | MERCADOLIBRE INC |
| Monster MNST | `MNST` | 865752 | Monster Beverage Corp |
| Netflix NFLX | `NFLX` | 1065280 | NETFLIX INC |
| Nike NKE US | `NKE` | 320187 | NIKE, Inc. |
| ServiceNow NOW US | `NOW` | 1373715 | ServiceNow, Inc. |
| Spotify SPOT US | `SPOT` | 1639920 | Spotify Technology S.A. |
| Synopsys SNPS US | `SNPS` | 883241 | SYNOPSYS INC |
| Taiwan Semiconductor Manufacturing TSM US | `TSM` | 1046179 | TAIWAN SEMICONDUCTOR MANUFACTURING CO LTD |
| Visa V | `V` | 1403161 | VISA INC. |
| Workday WDAY US | `WDAY` | 1327811 | Workday, Inc. |
| Zoetis ZTS US | `ZTS` | 1555280 | Zoetis Inc. |

## 4. RESIDUAL -- NOTHING FOUND, YOUR CALL (17)

| folder | raw identifier held | why not resolved |
|---|---|---|
| Air Liquide AI FP | `AI` | parsed `AI` -- SEC has that ticker as C3.ai, Inc., a different company |
| BNP Paribas BNP FP | `BNP` | parsed `BNP` -- not in the SEC table (non-US listing) |
| British American Tobacco | - | folder name carries no ticker-shaped token, and no workbook names one |
| Bunzl BNZL GB | `BNZL` | parsed `BNZL` -- not in the SEC table (non-US listing) |
| China Construction Bank | - | folder name carries no ticker-shaped token, and no workbook names one |
| Coca Cola Femsa | - | folder name carries no ticker-shaped token, and no workbook names one |
| GSK LN | - | folder name carries no ticker-shaped token, and no workbook names one |
| Grupo Aeroportuario del Centro OMAB MM | `OMAB` | parsed `OMAB` -- SEC has that ticker as Central North Airport Group, a different company |
| Iberdrola IBE SM | `IBE` | parsed `IBE` -- not in the SEC table (non-US listing) |
| International Container Terminals | - | folder name carries no ticker-shaped token, and no workbook names one |
| Intesa Sanpaolo ISP IM | `ISP` | parsed `ISP` -- not in the SEC table (non-US listing) |
| Manila MER PER | `MER` | parsed `MER` -- not in the SEC table (non-US listing) |
| QXO | - | folder name carries no ticker-shaped token, and no workbook names one |
| Sumitomo Mitsui Financial Group 8316 JP | `8316` | parsed `8316` -- not in the SEC table (non-US listing) |
| Tokyo Electron 8035 JP | `8035` | parsed `8035` -- not in the SEC table (non-US listing) |
| UBS | - | folder name carries no ticker-shaped token, and no workbook names one |
| Universal Music Group UMG NL | `UMG` | parsed `UMG` -- not in the SEC table (non-US listing) |

---
Measured 2026-09-24T17:50Z by `2.0.0_SA_COO~Y`. PROPOSAL ONLY -- nothing was written to the universe or the crosswalk.
