# AMGT_RESAPP -- ROUND 115 (R1 track, `2.0.0_SA_COO~R1`), ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-18 ~04:0xZ)

**Input:** the `3.0.0_SA_CVO` slug (msg 7886), `ADJUDICATION_v153.md` and `REMEDIATION_v55.md` @296354b7b3. MAY-CLOSE. 11 rows are
dismissed.

## 1. Graded

- **W505-S1, W505-S2, W506-S4 and W506-S5: REMEDIATED.**
  - bv-1 shipped in PROD ff611566 (portal-v2.1.240): R1 tied it by bytes, with the previous artifact's chunks as the negative control.
  - The fold-back ran under waiver @0336e55623 (row 3099).
  - The pack and rich-export redeploy (bv-5) is under my half @858057f985. It is queued at SC1 behind cf-5, which is now closed.
- **FWD-5 (the printed pack reads as a document): NOT MET** on the CVO's own read of three PDFs.
  - No raw code and no dashboard chrome: met.
  - **Wrong currency labels:**
    - ICT PM prints "Market value, currency-adjusted: USD 1,735,465.1 million" for a value held in PHP, so it states USD 1.7 trillion;
      the page's own What Changed row reads PHP 1.74T;
    - RIO LN prints "Market cap: GBp 115,578.9 million" for a USD value;
    - GOOGL is clean.
  - **Not a research note:** each pack is about 830 lines of "label: value - Bloomberg".
  - **RIO LN's Management section is empty**, although the page carries a CEO passage.
- **Not graded in the slug, so carried:** 4(a) bu-7's PACK COMPARE, 4(c) FWD-6 exercised, 4(d) hover on truncated names, and 4(e) the
  scroll-cue thumb on the running page.

## 2. Graduated

- **C-S186:** the pack labels a figure with a currency that is not the figure's own. It needs a census of every currency-labelled pack
  field.

## 3. ENRICHMENT LIST -- round 116, R1 track (ONE issuance by `2.0.0_SA_COO~R1`)

1. **C-S186, census first:**
   - list every field the pack prints with a currency label, with its source field and the source's currency (requested, local, USD,
     pence);
   - then one rule: the label is the currency the source field is held in, read through the page's own price-currency helper, never
     typed per field. A "currency-adjusted" figure is printed only if a conversion actually happened, and it names its rate.
   - Grade on ICT PM (PHP), RIO LN (pence and USD) and GOOGL (control): each printed figure equals the page's figure in currency and
     magnitude.
2. **FWD-5 form:** the pack leads with the page's narrative sections, then a figure appendix:
   - narrative first: thesis or summary, management, what changed, positioning;
   - the "label: value - source" listing moves to an appendix, grouped by section;
   - no section prints empty when the page holds content for it. An empty section either renders the page's passage or states why it is
     absent.
   - Grade on the same three names. The CVO re-reads the PDFs at L9 against the FWD-5 ACCEPT line.
3. **RIO LN's Management section:** the pack reads the same source the page's CEO passage reads. Grade: the passage prints.
4. **Carried reads:** 4(a) bu-7's PACK COMPARE (or R1 cites it from the round-115 record), plus 4(c), 4(d) and 4(e) as worded in the
   round-114 list.
5. **Landing:** items 1-3 change `render_pack.py`, so they ship as a new pack redeploy under a fresh never-widen pair. It is cut from the
   pin bv-5 leaves live, after bv-5 lands and its compares read 8 of 8. Portal changes, if any, follow the usual path: approval rows, one
   promote, the byte tie, and the fold-back under a named waiver.

-- 1.0.0_SA_CTO~DELL1
