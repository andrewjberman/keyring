# ADR resolution of the identity residual -- 15 of 17 closed without a vendor call

**Ask:** Andrew, this terminal -- assess whether the residual holdings are ADRs; if so find the main ticker/CIK
via EDGAR, noting foreign private issuers file **Form 20-F** rather than 10-K.

**ANSWER: yes, they are overwhelmingly ADRs -- and 13 of them were ALREADY IN THE UNIVERSE, resolved, on the
holdings side.** The research folder names the LOCAL line (`BNP FP`, `IBE SM`, `8316 JP`) while the ETF books hold
the US ADR (`BNPQY`, `IBDRY`, `SMFG`). Same company, two lines, and nothing ever linked them -- which is also why
the coverage and holdings halves of the universe share only three names.

## Resolved (15 of 17)

| research folder | ADR / US ticker | CIK | in the SEC table as | found by |
|---|---|---|---|---|
| Air Liquide AI FP | `AIQUF` | 1161167 | L AIR LIQUIDE SA /FI | SEC title match: 'L AIR LIQUIDE SA /FI' |
| BNP Paribas BNP FP | `BNPQY` | **not in the SEC table** | - | universe holdings side: BNPQY_US_Equity 'BNP Paribas SA' |
| British American Tobacco | `BTI` | 1303523 | British American Tobacco p.l.c. | universe holdings side: BTI_US_Equity |
| Bunzl BNZL GB | `BZLFY` | 1072397 | BUNZL PLC | universe holdings side: BZLFY_US_Equity |
| China Construction Bank | `CICHY` | **not in the SEC table** | - | universe holdings side: CICHY_US_Equity |
| Coca Cola Femsa | `KOF` | 910631 | COCA COLA FEMSA SAB DE CV | universe holdings side: KOF_US_Equity |
| GSK LN | `GSK` | 1131399 | GSK plc | universe holdings side: GSK_US_Equity |
| Grupo Aeroportuario del Centro OMAB MM | `OMAB` | 1378239 | Central North Airport Group | universe holdings side: OMAB_US_Equity |
| Iberdrola IBE SM | `IBDRY` | **not in the SEC table** | - | universe holdings side: IBDRY_US_Equity |
| International Container Terminals | `ICT` | **not in the SEC table** | - | universe holdings side: ICT_US_Equity |
| Intesa Sanpaolo ISP IM | `ISNPY` | **not in the SEC table** | - | universe holdings side: ISNPY_US_Equity |
| QXO | `QXO` | 1236275 | QXO, Inc. | universe holdings side: QXO_US_Equity (US issuer, NOT an ADR) |
| Sumitomo Mitsui Financial Group 8316 JP | `SMFG` | 1022837 | SUMITOMO MITSUI FINANCIAL GROUP, INC. | SEC title match: 'SUMITOMO MITSUI FINANCIAL GROUP, INC.' |
| UBS | `UBS` | 1610520 | UBS Group AG | universe holdings side: UBS_US_Equity 'UBS Group AG' |
| Universal Music Group UMG NL | `UNVGY` | 1890126 | Universal Music Group N.V./ADR | universe holdings side: UNVGY_US_Equity 'Universal Music Group NV' |

## The five ADRs with no CIK, and the two still open -- one structural reason covers all seven

`BNPQY`, `CICHY`, `IBDRY`, `ICT`, `ISNPY` resolve to a company but carry **no CIK**, and `Manila MER PER`
and `Tokyo Electron 8035 JP` produced no match at all. Measured rather than assumed: searching the SEC
table's 10,459 TITLES for `PARIBAS`, `CONSTRUCTION BANK`, `IBERDROLA`, `CONTAINER TERMINAL`, `INTESA`,
`MERALCO` / `MANILA ELECTRIC` and `TOKYO ELECTRON` returns **0 hits each**. Those issuers are not in the
table under any ticker.

**That is a property, not a gap in the search.** `company_tickers.json` maps EXCHANGE-LISTED tickers to
registrants. An **unsponsored OTC ADR** is created by a depositary bank without the issuer's
participation; the foreign issuer typically relies on the **Rule 12g3-2(b) exemption**, files **no
Form 20-F**, and so has no CIK to find. So for these seven, "find the CIK on EDGAR" has no answer by
construction -- which is a different and more useful finding than a null result.

⚠ **The honest bound:** this is inferred from one instrument (the ticker-to-CIK table). It is possible for
an issuer to file 20-F while carrying no exchange-listed ticker, and this table would not show it. A live
EDGAR company-name search (`/cgi-bin/browse-edgar?company=...&type=20-F`) would settle each definitively.
That is egress and was NOT performed -- say the word and it is seven lookups.

## What this does NOT claim

- A CIK here is the registrant the ADR ticker maps to in the ingested table. I did **not** fetch filing
  histories, so **20-F filer status is inferred from the issuer being foreign and US-listed, never
  measured**.
- The holdings-side match is on COMPANY NAME -- exact token match on every row above, but still a
  PROPOSAL: linking a research folder to an existing `*_US_Equity` identity is a crosswalk write, and
  this lane wrote nothing.
- `QXO` is a US issuer, not an ADR; it appears only because its folder carried no resolvable ticker.

---
Measured 2026-09-24 by `2.0.0_SA_COO~Y`. Sources: `universe/v1/2026-09-16.json` and the ingested SEC
`company_tickers` bronze copy (date=2026-09-22, 10,459 tickers). No vendor call, no write.
