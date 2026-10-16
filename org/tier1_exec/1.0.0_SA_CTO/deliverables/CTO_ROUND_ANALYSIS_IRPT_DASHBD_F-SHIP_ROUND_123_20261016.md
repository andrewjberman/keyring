# CTO ROUND-123 ANALYSIS -- IRPT_DASHBD workstream F-SHIP (~F2): DB-f-901, the producer ground read (2026-10-16 ~04:5xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` ADJUDICATION_v127 @0cee932fa9 (msg 9062): MAY-CLOSE, DBF123-1-AC1 PASS. The denominator is printed:
14 targets, 7 absent, every target with a claim.
**No PRD addendum.**

1. **A filled value is never labelled `absent` (row W901-S2).** `custodian`, `flow_class` and `coverage` are computed by the producer, yet
   labelled `absent` because the claim set has no `derived` value. RULED: no new claim value. The doctrine's set
   (measured / inferred / held / absent) stays closed, and adding one is a rule-24 proposal nobody needs.
   - A field the producer computes from measured inputs carries `inferred`, with a `method` naming the derivation (for example
     "from the source entry's custodian").
   - `absent` is reserved for a value that is not there.
   - Owner `~F2`, in the transaction contract when it is written.
2. **Round 124's denominator (the 49 Financial `tran_srcde` mapping) is the UNION of two sources,** refining my round-122 analysis:
   - the CRO table (`SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811.json`, 157 codes);
   - every `tran_srcde` value 49 Financial's own silver transactions carry, read live with the read's date and row count printed.
   - Each source's count is printed, and so is their difference both ways. A code in the silver but missing from the table gets its own
     row, decided on its description. A table code never seen in the silver keeps its row, marked `not_observed`.
   - The 2026-08-11 table alone would miss any code added since.

-- 1.0.0_SA_CTO~DELL2
