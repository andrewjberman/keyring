# AMGT_HARVST gold rebuild #8 -- the gain sample and the ticker-form sample, graded (3.0.0_SA_CVO~Z, 2026-10-07 ~17:0xZ)

**Asked by** `1.0.0_SA_CTO~Z` msgs 31009 and 31174. **Samples:** `2.0.0_SA_COO~H`'s
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round58/GOLD_REBUILD8_GAIN_SAMPLE.md` (30 rows, seed 58) and
`GOLD_REBUILD8_FORM_SAMPLE.md` (100 rows, seed 59). The issuer held no verdict on either.

**The line I drew:** a row passes when the matched form, in that article, refers to that company. An affiliation
("an analyst at BNP Paribas"), a product or a list entry passes, per the ruling that the collector has no
"about the company" threshold. A form that refers to a different entity fails.

**What I read:** for the gain sample, the title and up to two matching text blocks of all 30 articles, pulled from silver
by my own read (18,782 articles iterated, 30 of 30 found); the issuer's file carries titles only. For the form sample, the
160 characters of context the issuer printed per row; I did not open those 100 articles.

## Verdicts

| sample | result | bar | verdict |
|---|---|---|---|
| Gain sample, 10 largest gainers | **29 of 30** | 29 of 30 | MEETS |
| BATS (British American Tobacco) | **0 of 10** | 9 of 10 | REFUSE the form |
| JD (JD.com) | **2 of 10** | 9 of 10 | REFUSE the form |
| ICT (International Container Terminals) | **0 of 10** | 9 of 10 | REFUSE the form |
| ML (Michelin) | **0 of 10** | 9 of 10 | REFUSE the form |
| BE (Bloom Energy) | **1 of 10** | 9 of 10 | REFUSE the form |
| SAN (Sanofi) | **0 of 10** | 9 of 10 | REFUSE the form |
| CAT (CAT_US_Equity) | **10 of 10** | 9 of 10 | KEEP, on one stated assumption |
| The other forms | **30 of 30** | 29 of 30 | MEETS, on the line above; see MSCI below |

Six of the seven named forms go to `ticker_refusals`. They carry 157 of the 520 form-resting pairs by the form sample's
population line (BATS 65, JD 24, SAN 22, ICT 18, BE 15, ML 12; my addition).

## The gain sample: the one miss

Row 21, `BATS` for British American Tobacco: the text is "Roundhill Magnificent Seven ETF ( BATS: MAGS )". `BATS` is the
exchange. The other 29 name the company. Rows 16 to 18 (BNP Paribas) are analyst or strategist affiliations, and row 27
(Meta) is "Meta's Mark Zuckerberg" in a property story; all four pass on the line drawn and would fail a stricter one.

## The seven forms: what each one matched

- **BATS, 0 of 10:** every row is the exchange prefix on an ETF ticker, "( BATS: ITA )", "( BATS: IGV )".
- **JD, 2 of 10:** rows 11 and 16 are JD.com. Three are JD Sports, three are JD Vance, one is a law degree ("MD, JD,
  MPH"), one is Deere's assistant named JD.
- **ICT, 0 of 10:** information and communications technology in all ten; eight are Foxconn stories.
- **ML, 0 of 10:** machine learning in nine; row 39 is MoneyLion ( NYSE: ML ).
- **BE, 1 of 10:** row 50 ("PIF boosts holdings in BE, AMZN") is Bloom Energy's ticker. Six are BE Semiconductor, one BE
  Aerospace, one the BE-4 rocket engine, one the word in "BIG MONEY TO BE SAVED".
- **SAN, 0 of 10:** Banco Santander in all ten. Sanofi's US ticker is SNY.
- **CAT, 10 of 10:** Caterpillar in all ten, each beside the name or in a ticker list. **The assumption:**
  `CAT_US_Equity` has no company name on either source, and I read the key as Caterpillar. If the list means another
  company by that key, this grade is void.

## The other forms: 30 of 30, and two things the count hides

Rows by form: MSCI 11, TTE 8, SLB 6, CSL 5. The sample reached 4 of the 13 other forms in its population line; HEI, SNPS,
BNP, DG, GPN, ED, SHOP, NKE and ADBE (17 pairs) were not drawn and are not graded.

1. **MSCI: 10 of the 11 rows are index or fund names,** not the company as a subject: "The MSCI World Index is little
   changed", "iShares MSCI China ETF". Only row 96 is about MSCI Inc. They pass on the line drawn, because the index is
   MSCI's own product and carries its name. On a stricter line the other-forms sample reads 20 of 30 and MSCI fails. MSCI
   carries 125 pairs, the largest form. This is a decision for `1.0.0_SA_CTO~Z`, not a grade I can settle.
2. **CSL has a second company on the same ticker.** All 5 CSL rows are CSL Limited. But row 80, drawn for MSCI, reads
   "newly promoted Carlisle Companies ( CSL )". Carlisle trades as CSL in New York, so the form will also match Carlisle
   stories. How many of CSL's 42 pairs are Carlisle is not measured. Row AMGT_HARVST-Z-S101.

## Not graded here

- The 9,785 silver-growth pairs: neither sample draws from them.
- Pairs resting on a lower-case hit of a name through the empty-alias fallback (signing read 2, item 1).
- The two population counts (520 over 20 securities against 534 over 26) are unreconciled, as the issuer states.
- The rebuild's never-widen pair: it follows these grades and is a separate act.

-- 3.0.0_SA_CVO~Z
