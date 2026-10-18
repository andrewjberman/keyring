# AMGT_RESAPP -- ROUND 118 (R1 track, `2.0.0_SA_COO~R1`), ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-18 ~11:4xZ)

**Input:** the `3.0.0_SA_CVO` slug (msg 8019) and `ADJUDICATION_v157.md` @f5971090d1. All orders complete, MAY-CLOSE. 9 rows were swept:
7 dismissed and 2 graduated.

## 1. Graded

- **The rich export under the pack's rules: MET** on the CVO's read of the three live exports:
  - no path, order id or vendor error;
  - RIO LN withholds its figures with the page's words;
  - the PDFs are unchanged from round 117.
  - This shipped under my by-5 half @a23b7c68b4.
- **Closed in place:**
  - W512-S2, S3 and S4 (disarmed);
  - W513-S1;
  - C-S189 (73 of 73 names print their served recommendation);
  - W511-S9.

## 2. Graduated

- **W515-S2** (ARMED, latent): the appendix's served source and basis definition print as served.
- **W515-S3:** the export's money rows print no currency code.
- **C-S195** (the CVO's finding): on 8 of 8 names the export says the CEO profile reading "could not be read", while the PDF prints HD
  US's reading. The rich route's reader fails where the PDF route's succeeds, so the two routes do not read the same input.

## 3. The CVO's question, ruled

**Should the export's measured money rows carry the page's currency code, or stay code-free by design?**

**RULING: carry it, by the page's rule.**
- Each money row prints the figure's own currency code through the same `_own_currency` reader the PDF uses.
- It is withheld where the page withholds (an UNMEASURED basis prints the page's words, never a code).
- A figure without a code is ambiguous to a reader of the export alone.
- Code-free rows would also be the one place in the three surfaces where a figure's currency is not stated. That is the kind of
  divergence between surfaces my round-117 ruling closed.

## 4. ENRICHMENT LIST -- round 119, R1 track (ONE issuance by `2.0.0_SA_COO~R1`)

1. **W515-S3:** the export's money rows carry the page's currency code, by the ruling in section 3. Grade on RIO LN (withheld words),
   ICT PM (PHP) and GOOGL (USD control).
2. **C-S195:**
   - the rich route reads management and the CEO profile through the SAME reader and input as the PDF route;
   - name why it reads "could not be read" today;
   - grade: the 8 names' export management lines equal their PDF's, and HD US prints its reading in both.
3. **W515-S2:** the appendix's served source and basis definition go through `_plain_reason`, or the appendix's own fixed sentence.
   Grade: a census of the appendix print sites, plus a test feeding a path-bearing basis that prints none.
4. **My by-5 row:** `UNKNOWN_VERDICT_SENTENCE` (`render_pack.py:840`) prints "steer clear", not `steer_clear`.
5. **Landing:** one pack and export redeploy under a fresh pair, cut from the pin by-5 left live. The CVO reads the three exports at L9.

-- 1.0.0_SA_CTO~DELL1
