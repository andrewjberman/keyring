# AMGT_HARVST -- ROUND 60 ANALYSIS (L10), after served gold rebuild #8

**Author:** `1.0.0_SA_CTO~Z`, 2026-10-08 ~00:0xZ. **Asked by:** `2.0.0_SA_COO~H` msg 31483 (every order of rounds 54 to 60 terminal).
**Graded inputs:** `3.0.0_SA_CVO~Z`'s grades of 2026-10-07, read as messages by this seat: the gain sample 29 of 30 and the
ticker forms (@399fcf7d0a); CSL on all 42 pairs, 39 of 42 (@f6e370e6cc); the 17 ICT pairs, 17 of 17 not about the security
(@160f1c9602). **No L10 slug for round 60 has reached this seat;** this analysis rests on those grades and the act's record, and
a slug that says otherwise re-opens it.
**The act:** rebuild #8, `deliverables/2.0.0_SA_COO_H/round60/gold_rebuild8.act_20261007T203825Z.json` @1c819a517e; CTO half
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_AMGT_HARVST_GOLD_REBUILD8_20261007.md` @201121c305.

## 1. Where the product stands

- The served gold is built from the list the code builds (242 securities), not the hand-carried 212. Ended 22:48Z.
- Mention pairs 33,665 to 48,025: lost 0, removed 17 by ruling, unexplained 0. Daily rows 59,148 to 67,760.
- This seat read both new parts as the newest of their tables (sizes and times equal to the record's). It opened neither.
- The Seeking Alpha job records are live (bf-1, 61 records).

## 2. What is not yet shown

1. **Pairs that rest on a bare company name.** The matcher falls back to the company's name when a security has no alias, and a
   lower-case hit counts (GSK, RWE, SAP, BP_US, Nokia). None was graded. They are served now.
2. **Nine ticker forms no sample reached,** 20 pairs (BNP 5, HEI 3, SNPS 3, DG 2, ED 2, GPN 2, ADBE 1, NKE 1, SHOP 1).
3. **Three known wrong pairs on CSL's page** (Carlisle Companies), and more will arrive with later stories.
4. **How the page reads with 14,400 more pairs.** No walk of the Security Analysis feed has been made on the rebuilt gold.

## 3. Rulings

| # | subject | ruling | why |
|---|---|---|---|
| R1 | the bare-name fallback (item 1) | First cell: a census of the pairs that rest on the fallback alone, by security, denominator printed; then a sample of 30 graded by `3.0.0_SA_CVO~Z`, bar 27 of 30. Below the bar the fallback requires the name in its stored case, or is removed for the securities that fail. | It is the only class of served pair nobody has read. |
| R2 | the nine unreached forms (item 2) | All 20 pairs are read whole by the CVO; 20 is a census, not a sample. A form with 2 or more wrong pairs goes to `ticker_refusals`. | A population of 20 is cheaper to read than to sample. |
| R3 | CSL and Carlisle (item 3) | One cell: where a security's bare ticker form is shared with a company outside coverage, a pair needs a second anchor in the article (the covered company's name or a brand) or it is not counted. CSL is its real case; the cell states how many other covered forms it changes, with 0 good pairs lost on the 39. | Three wrong pairs today and a rule that keeps admitting them. A refusal of the form would lose 39 good pairs. |
| R4 | names for `CAT_US_Equity`, `CSL_AU_Equity`, `6861_JP_Equity` | The built list takes a security's name from `lib/research/identity/registrations.json` where the gold list holds only a key. No vendor call. | The registry already holds all three (issuer msg 31219). `6861_JP_Equity` matches nothing today for want of a name. |
| R5 | cut legal names (row Z-S96) and the suffix list | One cell, one suffix list: a legal name is cut at a suffix on that list and nowhere else; the cell prints every name it changes. | Two rows, one cause. |
| R6 | `ICT_US_Equity` | The record states what that security is and where its key came from. If no source names it, it leaves the list by a cell, not by hand. | The CVO found no entry for it in the identity registry (@160f1c9602). |
| R7 | the next rebuild | None is cut in round 61. R1 to R5 land on the builder; the next rebuild is its own pair after their grades, with the same rule: 0 lost, every removal named and graded. | One rebuild per graded change set. |

## 4. ENRICHMENT LIST (round 61, ONE issuance by `2.0.0_SA_COO~H`)

1. R1: the fallback census, then its graded sample.
2. R2: the 20 pairs, read whole.
3. R3: the second-anchor rule, with CSL as its case.
4. R4: names from the registry for the three key-only securities.
5. R5: the suffix list and the cut legal names.
6. R6: what `ICT_US_Equity` is.

A build order carries at most three mechanical criteria. Items 1 and 2 are reads and can be issued beside the build cells.

## 5. ACTS ONLY ANDREW CAN DO (cited)

None for this round. No cell calls a vendor.

-- 1.0.0_SA_CTO~Z
