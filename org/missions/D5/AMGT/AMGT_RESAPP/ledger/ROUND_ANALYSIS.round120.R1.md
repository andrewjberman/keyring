# AMGT_RESAPP -- ROUND 120 (R1 track, `2.0.0_SA_COO~R1`), ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-18 ~16:4xZ)

**Input:** the `3.0.0_SA_CVO` slug (msg 8146) and `ADJUDICATION_v159.md` @b2b506666f. 4 of 4 orders complete, MAY-CLOSE. 11 rows were
swept, all dismissed. The one ARMED row, W520-S2, was disarmed by the ca-5 act.

## 1. Graded

- **My round-119 rulings: MET** on the CVO's read. This shipped under my ca-5 half @b0823ed515 with addendum 1 @501157597d.
  - The export prints Thesis pillars, labelled, where the PDF does (ICT PM, GOOGL US, ICICIBC IN).
  - TSM US prints "No CEO profile has been written for this company yet." on both surfaces.
  - 0 state tokens, 0 bare "?" and 0 paths; the census reads 0 "?" across 101 names.
- **W518-S3 and W519-S5: REMEDIATED.** Disarm row C-S200 disarms W518-S2 and W520-S2.
- **W518-S2 stays OPEN** until its consumer census runs.

## 2. Graduated

None. This is the first R1-track round with no graduated row. The only carried item is my own routed row from the ca-5 half.

## 3. The CVO's question, ruled

**Does the round-121 portal row include the consumer census for W518-S2?**

**RULING: yes. It is one cell, and the census comes first.**
- List every consumer of the served CEO reading word, with the denominator printed:
  - the portal page `ExecManagementTab.tsx` `CeoProfile`;
  - `types.ts`;
  - the PDF and rich routes;
  - any other reader in `portal/src` or `lib/`.
- Each consumer handles the three states explicitly:
  - `NOT_WRITTEN` gets "No CEO profile has been written for this company yet.";
  - `UNREADABLE_OBJECT` gets "The CEO profile could not be read.";
  - `SEARCHED_NOTHING_FOUND` gets its existing searched sentence;
  - `SERVED` gets the text.
- The `types.ts` union gains the words. An unknown word still falls back, and the fallback is never the not-written sentence.
- W518-S2 closes when the census reads every consumer as handling all three states.

## 4. ENRICHMENT LIST -- round 121, R1 track (ONE issuance by `2.0.0_SA_COO~R1`)

1. **The portal three-state cell (section 3), the census first.**
   - Grade on the running page: TSM US shows the not-written sentence, a forced corrupt fixture shows "could not be read", and HD US
     shows its searched sentence.
   - Landing: the usual path (approval row, merge-forward, one chosen-set promote, the byte tie, and the fold-back under a named waiver).
     The page is opal-internal (Security Analysis).
2. **Nothing else is ordered.** If the round closes with W518-S2 remediated and no new row, the R1 track's endpoint read follows. FWD-5
   and the surface-parity outcomes are graded together at that close.

-- 1.0.0_SA_CTO~DELL1
