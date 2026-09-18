# THESIS -- where foreign filings can come from, measured

**From** `4.0.0_SA_CRO~Z`, 2026-09-18, under Andrew-direct ~16:xxZ (record
`ANDREW_DIRECT_20260918_16xxZ_EDGAR_CHECK_AND_WEB_SEARCH_EGRESS.md`): *"go, run the EDGAR check, you have egress for
web search for additional foreign channel reserach"*. **Status:** research. It builds nothing, writes nothing to the
pool, schedules nothing. For `1.0.0_SA_CTO~Z`, whose L4 question the Thesis source is.

> **CORRECTION, 2026-09-18 ~16:2xZ -- two figures in this note were wrong as first committed @`70361878b6`.**
> (1) **The denominator is 33, not 34.** The population of record is `crosswalk/v1/2026-09-15.json`,
> `denominators.MEASURED = 33`; this note's 34 was those 33 plus NVIDIA, which has model blocks but no measured
> identity (diffed today, and raised first by `1.0.0_SA_CTO~Z`, msg 23693). NVIDIA files a current 10-K and stays in
> the section 3 table, but no longer counts toward any tier: tier 1 adds 6, not 7. The tiers now read 12, 18, 24 and
> 33 of 33. (2) **`COMPANY_EXEC_OFFICERS` does not close the management gap as a field add.** The management roster
> is read from the filing by contract C-EXEC-MANAGEMENT (`lib/research/management/roster.py:1-15`), so using a
> Bloomberg roster is a change to ratified text -- an L4 question, not a pull change. Sections 1, 2 and 6 are
> corrected in place. The plan built on this note: `BRIEF_THESIS_CURRENT_TO_DESIRED_20260918.md`.

---

## 1. The answer

The Thesis pipeline cites passages from annual filings, and today reaches 12 of the 33 keyed names -- the ones
the union universe already gives an SEC filing identity. **Measured today, 24 of 33 are reachable from two free,
official sources, and the other 9 each need a jurisdiction-specific route or a purchase.**

| tier | source | names | cumulative |
|---|---|---|---|
| today | SEC EDGAR, identity already on the union universe | 12 | 12 of 33 |
| 1 | SEC EDGAR, identity taken from Bloomberg's `CENTRAL_INDEX_KEY_NUMBER` | +6 | 18 of 33 |
| 2 | ESEF / UKSEF annual financial reports on `filings.xbrl.org` | +6 | 24 of 33 |
| 3 | one route per jurisdiction, or a purchased feed | 9 | 33 of 33 |

---

## 2. Bloomberg: no filing text, but the keys to find it

Searched the Terminal API's own field dictionary (`//blp/apiflds`) and probed its services:

- **No field returns filing text.** `//blp/docsvc` and `//blp/news` refuse to open; `//blp/bqlsvc` opens but refuses
  queries on entitlement, as `integrations/bloomberg/READ_HERE.md` s.4 already records.
- **It returns the identifiers that locate every filing:** `CENTRAL_INDEX_KEY_NUMBER` (SEC CIK) for all 22
  unresolved names and for NVIDIA; `LEGAL_ENTITY_IDENTIFIER` for 13 of the final 15; `COMPANY_WEB_ADDRESS` for all 22.
- **It carries two header fields:** `CIE_DES_BULK` (long business description) and `COMPANY_EXEC_OFFICERS` are
  populated for all 22. The description is a field add; the officer list is not (see the correction above).

**Bloomberg as the filing source is a purchase, not a build.** Its company filings are not on this terminal's API
entitlement. The question for the Bloomberg rep is filings access through Data License, or the BQL entitlement,
for non-SEC issuers. Bloomberg's DL documentation found in search did not confirm a filings product either way.
Two competing products do confirm one: LSEG's Filings API and S&P Capital IQ's non-US annual reports.

**Intercepting Terminal traffic is not recommended.** Extracting documents outside the licensed API very likely
breaches the Bloomberg terminal agreement and puts the terminal itself at risk. The licensed route gets the same
data cleanly.

---

## 3. Tier 1 -- SEC, using Bloomberg's CIK (EDGAR, measured)

One submissions-index read per CIK through the estate's own `lib/research/filings/fetch.py` `http_get` (the SEC
fair-access header). Boeing, the positive control, reads its 10-K of 2026-01-30. **Every EDGAR entity name matches
Bloomberg's NAME.**

| name | latest SEC annual report |
|---|---|
| National Grid | 20-F, 2026-06-03 |
| Novartis | 20-F, 2026-02-04 |
| BP | 20-F, 2026-03-06 |
| HSBC | 20-F, 2026-02-26 |
| ICICI Bank | 20-F, 2026-07-20 |
| Unilever | 20-F, 2026-03-12 |
| NVIDIA (outside the keyed 33) | 10-K, 2026-02-25 |

Fifteen others have a CIK but no current annual report: Enel's last 20-F is 2007, Imperial's 2007, KPN's 2008; the
rest file only ADR paperwork (F-6), ownership forms or old 12g3-2(b) supplements. **A CIK proves an SEC record,
never an annual report** -- which is why the check was needed.

**What it takes:** write Bloomberg's CIK and the expected form onto each name's `filing_identity` on the union
universe. The existing fetch, analyze and draft path then runs unchanged.

---

## 4. Tier 2 -- ESEF and UKSEF, one free repository (measured)

`filings.xbrl.org`, run by XBRL International, holds the Inline XBRL annual financial reports that EU and UK issuers
file with their national storage mechanisms, and serves them through a JSON:API. Queried by Bloomberg's LEI:

| name | domicile | reports held | newest |
|---|---|---|---|
| Enel | IT | 8 | period 2024-12-31 -- the FY2025 report is not there yet |
| Imperial Brands | GB | 3 | period 2025-09-30 |
| KPN | NL | 5 | period 2025-12-31 |
| Reckitt | GB | 5 | period 2025-12-31 |
| Hermes | FR | 6 | added 2026-03-24 |
| SSE | GB | 5 | period 2026-03-31 |

**Caveats that belong in the L4:** the repository is best-effort, not the official store, so Enel's FY2025 gap is
exactly the risk; the official UK store is the FCA's National Storage Mechanism, which serves the same files. And
the pipeline's section cutter is built for 10-K and 20-F item headings, so an ESEF annual report needs a second
cutter for a management report that has no "Item 1A".

---

## 5. Tier 3 -- the last nine

| name | domicile | official channel | note |
|---|---|---|---|
| KDDI | JP | EDINET API v2 (FSA) | free with an API key; annual securities report in Japanese |
| BB Seguridade | BR | CVM open-data portal | structured statements daily; document downloads alongside |
| Lenovo | HK | HKEXnews | annual reports since 1999; no official API |
| Hon Hai | TW | MOPS (TWSE) | English annual report is a summary translation |
| SingTel | SG | SGXNet announcements | no official API |
| Walmex | MX | BMV issuer pages / company site | BMV annual report in Spanish; XBRL copy is sold |
| RWE | DE | not on `filings.xbrl.org` (404) | Unternehmensregister, or the company site |
| Roche, Zurich | CH | no ESEF regime | company sites only |

Each is its own adapter, and several are in the local language. Tier 3 is where a purchased global filings feed
earns its cost, if one is bought.

---

## 6. For the CTO's L4

1. Tier 1 is an identity fix, not a new source. It lifts Thesis from 12 to 18 of 33 and needs no vendor spend.
2. Tier 2 is one new adapter plus a second section cutter, both over free official data, and lifts it to 24.
3. Tier 3 is a buy-or-build decision for Andrew: nine adapters, or one feed.
4. Independent of all three: `CIE_DES_BULK` on the existing Bloomberg pull serves the description line (12 of 33
   today) for the names Thesis cannot reach. Management (12 of 33) follows filing coverage, because its roster is
   read from the filing; a Bloomberg roster would be a contract change, not a field add.

**Sources:** EDGAR submissions API (`data.sec.gov`); [filings.xbrl.org about](https://filings.xbrl.org/docs/about);
[FCA National Storage Mechanism](https://www.fca.org.uk/markets/primary-markets/regulatory-disclosures/national-storage-mechanism);
[EDINET API v2 specification](https://disclosure2dl.edinet-fsa.go.jp/guide/static/disclosure/download/ESE140206.pdf);
[CVM open data, DFP](https://dados.cvm.gov.br/dataset/cia_aberta-doc-dfp);
[HKEXnews title search](https://www1.hkexnews.hk/search/titlesearch.xhtml);
[TWSE MOPS](https://emops.twse.com.tw/server-java/t58query);
[SGX company announcements](https://www.sgx.com/securities/company-announcements);
[BMV Walmex periodic information](https://www.bmv.com.mx/es/emisoras/informacionfinanciera/WALMEX-5214-CGEN_CAPIT);
[LSEG Filings API](https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/filings-API);
[Bloomberg Data License](https://professional.bloomberg.com/products/data/data-license/).
