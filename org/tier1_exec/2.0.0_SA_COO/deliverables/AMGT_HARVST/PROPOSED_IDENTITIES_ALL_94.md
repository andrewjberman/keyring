# Proposed identity for ALL 94 AM-research folders

Andrew's direction, this terminal: *reasonable proof, it does not have to be perfect; keep the ones not
100%% confirmed by supporting documentation in a list for later guidance, and do not let them hold up
matches for the rest.* This is that table. **PROPOSAL ONLY -- nothing is written to the universe or the
crosswalk.**

## Where the 94 land

| tier | n | meaning |
|---|---|---|
| `RESOLVED` | **33** | already resolved by the pipeline |
| `A-DOC` | **17** | A -- document-confirmed (the folder's own workbook names the ticker) |
| `B-SEC` | **26** | B -- folder-name ticker confirmed against the SEC ticker-to-CIK table |
| `C-ADR` | **13** | C -- ADR/US line already resolved elsewhere in the universe |
| `D-BEST` | **5** | D -- best effort, NOT document-confirmed (the later-guidance list) |
| | **94** | |

**89 of 94 carry a proposal backed by a document, a cik or an existing universe line. 5 more are
best-effort and sit on the later-guidance list. 0 have no proposal.**

## D -- the later-guidance list (5)

Strong but not confirmed by supporting documentation in the folder itself. Usable now, flagged for review.

| folder | proposed | evidence |
|---|---|---|
| Air Liquide AI FP | `AIQUF` | name match 1.00 to SEC 'L AIR LIQUIDE SA /FI' cik 1161167 -- NOT document-confirmed |
| Coca Cola Femsa | `KOF` | name match 1.00 to SEC 'COCA COLA FEMSA SAB DE CV' cik 910631 -- NOT document-confirmed |
| Manila MER PER | `--` | Manila = EDGAR 'MANILA ELECTRIC CO' cik 61975 -- EDGAR registrant confirmed this session (submissions API); no US ticker, no 20-F |
| Sumitomo Mitsui Financial Group 8316 JP | `SMFG` | name match 1.00 to SEC 'SUMITOMO MITSUI FINANCIAL GROUP, INC.' cik 1022837 -- NOT document-confirmed |
| Tokyo Electron 8035 JP | `--` | Tokyo = EDGAR 'Tokyo Electron LTD' cik 1443276 -- EDGAR registrant confirmed this session (submissions API); F-6 ADR facility, no 20-F |

## Every folder, by tier

### already resolved by the pipeline (33)

| folder | key / ticker | evidence |
|---|---|---|
| ASML NA | `ASML_NA_Equity` | already carries a security_key in universe/v1/2026-09-16.json |
| Alibaba BABA | `BABA_US_Equity` | already carries a security_key in universe/v1/2026-09-16.json |
| BB Seguridade BBSE3 BZ | `BBSE3_BZ_Equity` | already carries a security_key in universe/v1/2026-09-16.json |
| BP PLC | `BP/_LN_Equity` | already carries a security_key in universe/v1/2026-09-16.json |
| Boeing BA | `BA_US_Equity` | already carries a security_key in universe/v1/2026-09-16.json |
| Costco COST | `COST_US_Equity` | already carries a security_key in universe/v1/2026-09-16.json |
| Enel SpA ENEL IM | `ENEL_IM_Equity` | already carries a security_key in universe/v1/2026-09-16.json |
| HSBC HSBA LN | `HSBA_LN_Equity` | already carries a security_key in universe/v1/2026-09-16.json |
| Haliburton HAL | `HAL_US_Equity` | already carries a security_key in universe/v1/2026-09-16.json |
| Hermes RMS | `RMS_FP_Equity` | already carries a security_key in universe/v1/2026-09-16.json |
| Home Depot HD | `HD_US_Equity` | already carries a security_key in universe/v1/2026-09-16.json |
| Hon Hai 2317 TT | `2317_TT_Equity` | already carries a security_key in universe/v1/2026-09-16.json |
| ICICI Bank ICICIBC IN | `ICICIBC_IN_Equity` | already carries a security_key in universe/v1/2026-09-16.json |
| Imperial Brands IMB LN | `IMB_LN_Equity` | already carries a security_key in universe/v1/2026-09-16.json |
| Intuit INTU | `INTU_US_Equity` | already carries a security_key in universe/v1/2026-09-16.json |
| KDDI | `9433_JP_Equity` | already carries a security_key in universe/v1/2026-09-16.json |
| Kimberly Clark KMB | `KMB_US_Equity` | already carries a security_key in universe/v1/2026-09-16.json |
| Koninklijke KPN NA | `KPN_NA_Equity` | already carries a security_key in universe/v1/2026-09-16.json |
| Lenovo 992 HK | `992_HK_Equity` | already carries a security_key in universe/v1/2026-09-16.json |
| National Grid NG LN | `NG/_LN_Equity` | already carries a security_key in universe/v1/2026-09-16.json |
| Novartis NOVN SW | `NOVN_SW_Equity` | already carries a security_key in universe/v1/2026-09-16.json |
| Nubank NU | `NU_US_Equity` | already carries a security_key in universe/v1/2026-09-16.json |
| Petrobras PETR3 BZ | `PBR_US_Equity` | already carries a security_key in universe/v1/2026-09-16.json |
| RWE AG RWE GY | `RWE_GR_Equity` | already carries a security_key in universe/v1/2026-09-16.json |
| Reckitt Benckiser RKT LN | `RKT_LN_Equity` | already carries a security_key in universe/v1/2026-09-16.json |
| Roche ROG SW | `ROG_SW_Equity` | already carries a security_key in universe/v1/2026-09-16.json |
| SAP GY | `SAP_GY_Equity` | already carries a security_key in universe/v1/2026-09-16.json |
| SSE plc SSE LN | `SSE_LN_Equity` | already carries a security_key in universe/v1/2026-09-16.json |
| Singapore Telecom ST SP | `ST_SP_Equity` | already carries a security_key in universe/v1/2026-09-16.json |
| Unilever ULVR LN | `ULVR_LN_Equity` | already carries a security_key in universe/v1/2026-09-16.json |
| Valero Energy VLO | `VLO_US_Equity` | already carries a security_key in universe/v1/2026-09-16.json |
| Walmart de Mexico WALMEX MM | `WALMEX*_MM_Equity` | already carries a security_key in universe/v1/2026-09-16.json |
| Zurich Insurance ZURN SW | `ZURN_SW_Equity` | already carries a security_key in universe/v1/2026-09-16.json |

### A -- document-confirmed (the folder's own workbook names the ticker) (17)

| folder | key / ticker | evidence |
|---|---|---|
| America Movil AXMB MM | `AMXB MM` | workbook America Movil 2025 07 11.xlsx names Ticker 'AMXB MM' |
| AstraZeneca AZN | `AZN-GB` | workbook AZN FactSet Based ONE PAGER 2026 06 22_v names Ticker 'AZN-GB' |
| Canadian National Railway CNR | `CNR-CA` | workbook CNR CA FactSet Based ONE PAGER 2026 06 3 names Ticker 'CNR-CA' |
| Clorox CLX | `CLX_US_Equity` | workbook CLX FactSet Based ONE PAGER 2026 06 12_v names Ticker 'CLX-US' |
| Copa CPA | `CPA_US_Equity` | workbook COPA FactSet Based ONE PAGER 2027 07 07_ names Ticker 'CPA-US' |
| JD.com 9618 HK | `9618-HK` | workbook JD. com FactSet Based ONE PAGER TEMPLATE names Ticker '9618-HK' |
| Michelin ML FP | `ML-FR` | workbook Michelin FactSet Based ONE PAGER TEMPLAT names Ticker 'ML-FR' |
| Mitsubishi UFJ Financial Group 8306 JP | `8306-JP` | workbook MUFG FactSet Based ONE PAGER TEMPLATE 20 names Ticker '8306-JP' |
| Nestle NESN SW | `NESN-CH` | workbook Nestle FactSet Based ONE PAGER TEMPLATE  names Ticker 'NESN-CH' |
| Nokia FH | `NOKIA-FI` | workbook Nokia FactSet Based ONE PAGER TEMPLATE 2 names Ticker 'NOKIA-FI' |
| Orange ORA FP | `ORA-FR` | workbook Orange FactSet Based ONE PAGER TEMPLATE  names Ticker 'ORA-FR' |
| Sanofi SAN FP | `SAN-FR` | workbook Sanofi SAN FactSet Based ONE PAGER TEMPL names Ticker 'SAN-FR' |
| Schlumberger SLB | `SLB_US_Equity` | workbook SLB One Pager 2025 07 14_v1 WW.xlsx names Ticker 'SLB' |
| Shopify SHOP CA | `SHOP_US_Equity` | workbook SHOP CA FactSet Based ONE PAGER 2026 07  names Ticker 'SHOP-US' |
| Telefonica Brazil VIVT3 BZ | `VIVT3 BZ` | workbook Telefonica Brazil 2026 01 13_v1.xlsx names Ticker 'VIVT3 BZ' |
| Tokyo Marine 8766 JP | `8766-JP` | workbook Tokyo Marine FactSet Based ONE PAGER TEM names Ticker '8766-JP' |
| Uber Technologies UBER US | `UBER_US_Equity` | workbook UBER-Adam.xlsx names Ticker 'UBER' |

### B -- folder-name ticker confirmed against the SEC ticker-to-CIK table (26)

| folder | key / ticker | evidence |
|---|---|---|
| Adobe ADBE US | `ADBE_US_Equity` | folder ticker 'ADBE' = SEC 'ADOBE INC.' cik 796343 |
| Alphabet GOOGL US | `GOOGL_US_Equity` | folder ticker 'GOOGL' = SEC 'Alphabet Inc.' cik 1652044 |
| Cadence CDNS US | `CDNS_US_Equity` | folder ticker 'CDNS' = SEC 'CADENCE DESIGN SYSTEMS INC' cik 813672 |
| Celsius CELH | `CELH_US_Equity` | folder ticker 'CELH' = SEC 'Celsius Holdings, Inc.' cik 1341766 |
| Eli Lilly LLY US | `LLY_US_Equity` | folder ticker 'LLY' = SEC 'ELI LILLY & Co' cik 59478 |
| Global Payments GPN | `GPN_US_Equity` | folder ticker 'GPN' = SEC 'GLOBAL PAYMENTS INC' cik 1123360 |
| HEICO Corporation HEI US | `HEI_US_Equity` | folder ticker 'HEI' = SEC 'HEICO CORP' cik 46619 |
| Idexx IDXX | `IDXX_US_Equity` | folder ticker 'IDXX' = SEC 'IDEXX LABORATORIES INC /DE' cik 874716 |
| Intuitive Surgical ISRG US | `ISRG_US_Equity` | folder ticker 'ISRG' = SEC 'INTUITIVE SURGICAL INC' cik 1035267 |
| MSCI Inc MSCI US | `MSCI_US_Equity` | folder ticker 'MSCI' = SEC 'MSCI Inc.' cik 1408198 |
| Mastercard MA | `MA_US_Equity` | folder ticker 'MA' = SEC 'Mastercard Inc' cik 1141391 |
| MercadoLibre MELI US | `MELI_US_Equity` | folder ticker 'MELI' = SEC 'MERCADOLIBRE INC' cik 1099590 |
| Monster MNST | `MNST_US_Equity` | folder ticker 'MNST' = SEC 'Monster Beverage Corp' cik 865752 |
| Netflix NFLX | `NFLX_US_Equity` | folder ticker 'NFLX' = SEC 'NETFLIX INC' cik 1065280 |
| Nike NKE US | `NKE_US_Equity` | folder ticker 'NKE' = SEC 'NIKE, Inc.' cik 320187 |
| Quanta Services PWR | `PWR_US_Equity` | folder ticker 'PWR' = SEC 'QUANTA SERVICES, INC.' cik 1050915 |
| Rio Tinto RIO LN | `RIO_US_Equity` | folder ticker 'RIO' = SEC 'RIO TINTO PLC' cik 863064 |
| ServiceNow NOW US | `NOW_US_Equity` | folder ticker 'NOW' = SEC 'ServiceNow, Inc.' cik 1373715 |
| Spotify SPOT US | `SPOT_US_Equity` | folder ticker 'SPOT' = SEC 'Spotify Technology S.A.' cik 1639920 |
| Synopsys SNPS US | `SNPS_US_Equity` | folder ticker 'SNPS' = SEC 'SYNOPSYS INC' cik 883241 |
| Taiwan Semiconductor Manufacturing TSM US | `TSM_US_Equity` | folder ticker 'TSM' = SEC 'TAIWAN SEMICONDUCTOR MANUFACTURING CO LTD' cik 1046179 |
| Total Energies TTE FP | `TTE_US_Equity` | folder ticker 'TTE' = SEC 'TotalEnergies SE' cik 879764 |
| UnitedHealth Group UNH US | `UNH_US_Equity` | folder ticker 'UNH' = SEC 'UNITEDHEALTH GROUP INC' cik 731766 |
| Visa V | `V_US_Equity` | folder ticker 'V' = SEC 'VISA INC.' cik 1403161 |
| Workday WDAY US | `WDAY_US_Equity` | folder ticker 'WDAY' = SEC 'Workday, Inc.' cik 1327811 |
| Zoetis ZTS US | `ZTS_US_Equity` | folder ticker 'ZTS' = SEC 'Zoetis Inc.' cik 1555280 |

### C -- ADR/US line already resolved elsewhere in the universe (13)

| folder | key / ticker | evidence |
|---|---|---|
| AMD Advanced Micro Devices | `AMD_US_Equity` | ADR/US line already resolved in the universe as AMD_US_Equity ('Advanced Micro Devices Inc') |
| BNP Paribas BNP FP | `BNPQY_US_Equity` | ADR/US line already resolved in the universe as BNPQY_US_Equity ('BNP Paribas SA') |
| British American Tobacco | `BTI_US_Equity` | ADR/US line already resolved in the universe as BTI_US_Equity ('British American Tobacco PLC') |
| Bunzl BNZL GB | `BZLFY_US_Equity` | ADR/US line already resolved in the universe as BZLFY_US_Equity ('Bunzl PLC') |
| China Construction Bank | `CICHY_US_Equity` | ADR/US line already resolved in the universe as CICHY_US_Equity ('China Construction Bank Corp') |
| GSK LN | `GSK_US_Equity` | ADR/US line already resolved in the universe as GSK_US_Equity ('GSK PLC') |
| Grupo Aeroportuario del Centro OMAB MM | `OMAB_US_Equity` | ADR/US line already resolved in the universe as OMAB_US_Equity ('Grupo Aeroportuario del Centro') |
| Iberdrola IBE SM | `IBDRY_US_Equity` | ADR/US line already resolved in the universe as IBDRY_US_Equity ('Iberdrola SA') |
| International Container Terminals | `ICT_US_Equity` | ADR/US line already resolved in the universe as ICT_US_Equity ('International Container Termin') |
| Intesa Sanpaolo ISP IM | `ISNPY_US_Equity` | ADR/US line already resolved in the universe as ISNPY_US_Equity ('Intesa Sanpaolo SpA') |
| QXO | `QXO_US_Equity` | ADR/US line already resolved in the universe as QXO_US_Equity ('QXO Inc') |
| UBS | `UBS_US_Equity` | ADR/US line already resolved in the universe as UBS_US_Equity ('UBS Group AG') |
| Universal Music Group UMG NL | `UNVGY_US_Equity` | ADR/US line already resolved in the universe as UNVGY_US_Equity ('Universal Music Group NV') |

---
Measured 2026-09-24 18:48Z by `2.0.0_SA_COO~Y` over the LIVE research directory.
Arms: the folder's own FactSet workbook; the ingested SEC ticker-to-CIK table (date=2026-09-22);
the universe's own holdings side; and EDGAR for the two the others could not reach.
NOTE: a proposed `<ROOT>_US_Equity` key is the US-line convention. A non-US local line keeps its own
ticker form and its exchange-code translation is the crosswalk's call, not typed here.
