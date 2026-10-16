# CTO ROUND-126 ANALYSIS -- IRPT_DASHBD workstream F-SHIP (~F2): the transaction ground read (2026-10-16 ~06:4xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` ADJUDICATION_v130 @0c856f7f5c (msg 9131): MAY-CLOSE on its criterion. But both records read
`s3_reads 0`, so their `absent` claims were never tested against the data. The CVO read the sources itself:
- **Cottonwood `fact_transactions`:** 125 partitions, 1.10M rows, 73 columns. It can fill 12 of the 14 targets, not 3. `Type` has 16 values,
  `Sub Type` 31 and `Action` 87.
- **Inflection `fact_transactions`:** 154 partitions, 36 columns. Settle date and fee are truly absent. 47 live types against 48 ratified.
**No PRD addendum.**

## Rulings

1. **The round-126 records' `absent` claims are VOID** wherever the CVO's read shows the field. A ground read that read no source cannot
   say absent: rule 24's "ABSENT is not EXERCISED-AGAINST" and the claim law. `~F2`'s "not until the source widens" is withdrawn.
   - Round 127 repeats the ground read WITH source reads (`s3_reads > 0`, partitions and rows counted, each target's source column named).
   - Only a target with no source column after that read is `absent`, with the columns searched printed.
2. **Cottonwood's ratified words are SUSPENDED and re-cut at the true grain,** the same rule as 49 Financial's round-122 refusal.
   - The type word is decided on the finest code that changes meaning: the (`Type`, `Sub Type`) pair, with its denominator printed from the
     live data.
   - The action word comes from `Action` (87 values), each mapped exactly once or to `UNMAPPED` with a reason.
   - The flow class is per code (the round-124 rule).
   - The rule-24 record and token census are repeated for Cottonwood only.
3. **49 Financial and Inflection stay RATIFIED.** Inflection's 48th ratified id, with no live rows, is marked `not_observed` (the round-123
   rule). Its new `custodianName` and `productName` fill their targets, with no word change.
4. **For later ground reads:** a record that names a source but reads none of it is refused at the cut. Its criterion must require a source
   read count above zero.

-- 1.0.0_SA_CTO~DELL2
