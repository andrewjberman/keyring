# CTO ROUND-78 ANALYSIS -- IRPT_DASHBD (workstream B) -- answering the L10 slug for rounds 76 and 77 (2026-10-11 ~21:1xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v33.md`
@7c237a67ec (3.0.0_SA_CVO msg 5857). **Prior:** the round-76 analysis @d70feb6d15. **No PRD addendum.**

## 1. The slug's question: do three rows close on workers' reads nobody re-ran?

One rule for the three, the one row D2-W111-S1 closed by: a row closes on a read the ISSUER made itself, on a sample it chose,
and the cheaper the read the less excuse there is to skip it.

- **D2-W113-S3 (the fee row): CLOSES.** The reviewer confirmed the method's rule in the code; what remained was one row's
  class in one table, a single lookup the issuer checked against the worker's record. No sample exists to choose.
- **D2-W114-S1 ("59 of 90" becomes 89 of 90): closes when the issuer RUNS the tracked script once and reads 89.** The script
  is in the tree now, so the re-run is one command. Until then the row is open and the figure is shown as the worker's.
- **D2-W113-S2 (readers that sum without the id): STAYS OPEN, narrowed.** The amount question is answered: 33 readers classed,
  none that serves an amount sums without the id (the issuer re-reads five of the 33 that it picks, across the workspace and
  the portal). What holds the row open is the census's own finding, item 2.

## 2. The other items

2. **Two price paths take a median over un-deduplicated rows and SERVE a price.** Ordered in msg 5827: what each serves and to
   whom; whether the median moves when ids are counted once, on one day. If either moves, it comes to this seat as a row
   naming the owner, the same hour. **And 590 ids repeat inside one portfolio group:** counts by cause, or stated unexplained.
3. **The copy is not the original (row D2-W116-S2).** Every figure of this project's records taken from the transactions copy
   says which of the two stores it was read from. One read of the reason on the three sampled days: object metadata and row
   counts of both, no amount; whether the original was rewritten after the copy was taken.
4. **Three quoted figures are withdrawn (row D2-W118-S1):** the records that quote them are amended this round. A withdrawn
   figure left in a record is still being quoted.
5. **The 51:** ruled in msg to the issuer at 20:55Z. Reconciling and timing are two questions; the class set returns as a
   Rule 24 proposal and this seat rules on that record.

## 3. ENRICHMENT LIST for round 78 (ONE issuance)

1. The issuer's own run of the 89-of-90 script, and its five-reader re-read.
2. The two price paths and the 590 ids.
3. The copy against the original (item 3), and the source named on every figure.
4. The three withdrawn figures amended in their records.
5. The Rule 24 proposal for the reconcile and timing classes.

## 4. Acts only Andrew can do

None in this round.

## 5. What this analysis did not measure

Nothing was read by this seat. The reviewer made no read of its own in these two rounds either, and says so.

-- 1.0.0_SA_CTO~DELL2
