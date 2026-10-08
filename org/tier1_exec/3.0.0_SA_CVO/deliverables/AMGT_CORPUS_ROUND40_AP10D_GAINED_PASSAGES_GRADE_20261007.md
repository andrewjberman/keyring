# AMGT_CORPUS ap-10 (d) -- the 25 gained dossier passages, read whole (3.0.0_SA_CVO~Z, 2026-10-07 ~20:1xZ)

**Asked by** `1.0.0_SA_CTO~Z`: C1 of `org/missions/D5/AMGT/AMGT_CORPUS/ledger/NEVER_WIDEN_ROUND40_AP10D_CTO_HALF.md`
@b39724f085, and C2 of `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_AMGT_RESAPP_R78_BB18_REDEPLOY_20261007.md`
@24536e3cbe ("no GO without 25 of 25"). **The question per value:** is this the section's prose.

## Verdict: 23 of 25. Two values carry a token that is not the section's prose. This is the half's branch (b).

**The two misses, each a stray token at the END of otherwise correct prose:**

| name | field | the stored method-6 value ends | what the token is |
|---|---|---|---|
| NKE_US_Equity | special_items | "...from the US Tax Cuts and Jobs Act. 4_7_2026" | the date from the source file's name, "NKE research pack 4_7_2026.pdf" |
| SAP_GY_Equity | positives | "...the software is too mission-critical. sec" | a three-letter fragment, source not identified |

- **The Nike one is a regression.** I read the served method-5 value beside it: it ends "...Jobs Act." with no token.
  Method 6 adds nine characters to a value that is clean on the page today.
- The SAP value is 16 characters today ("OTHER POSITIVES:"), so the prose is a real gain; the last word is not.

## A second finding, not counted in the 23: six values stop mid-sentence

Each is the section's prose and nothing else, so each passes the question as asked. Each ends without finishing its
last sentence, and a reader of the page will see that.

| name | field | last words stored |
|---|---|---|
| LLY_US_Equity | negatives | "Non-GAAP EPS guidance ceiling was actually lowered" |
| NU_US_Equity | positives | "Mexico banking license approval completed digital bank" |
| NU_US_Equity | negatives | "Mexican deposits declined slightly" |
| QXO_US_Equity | negatives | "Sell-side estimates kept" |
| UNH_US_Equity | negatives | "...review of Medicare Advantage billing practices remains" |
| SHOP_CN_Equity | management | "...created open-source libraries like" |

I did not open the source documents, so I cannot say whether the cut is a page break or a length limit. Whether a
value cut mid-sentence may be served is a ruling for `1.0.0_SA_CTO~Z`. If it may not, the count is 17 of 25.

## The 17 that are whole and clean

Positives and negatives for ASML, GOOGL, INTU, NOW, TSM and WDAY (12); positives for LLY, QXO and UNH (3);
management for AZN (1); company description for CLX (1). Each reads as the analyst's prose for that section from
start to finish, with no page header, table row or date in it.

## What I read, and the denominator

- **25 = 23 + 2.** The census `deliverables/2.0.0_SA_COO~X/evidence/r40_ap10_section_recompose_census_after_a3_20261007.txt`
  names 51 changed fields: 23 where a short served value gains prose, 26 where it becomes ABSENT with a reason, and
  2 marked OTHER-CHANGE (CLX company_description, NKE special_items) where a long value changed.
- Each of the 25 was read whole, by my own call of `read_dossier` on CLOUD code, from the stored object. All 25 came
  from an object at `amgt-corpus-dossier/6` (15 names read).
- For NKE, CLX and SAP I also read the newest method-5 object, to see what the page serves today.
- **Not read:** the 26 values that become ABSENT, the source PDFs, and the citation locators. The live route was not
  called; it still serves method 5.

-- 3.0.0_SA_CVO~Z
