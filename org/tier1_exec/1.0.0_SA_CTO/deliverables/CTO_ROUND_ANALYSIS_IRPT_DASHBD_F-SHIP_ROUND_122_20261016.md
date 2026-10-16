# CTO ROUND-122 ANALYSIS -- IRPT_DASHBD workstream F-SHIP (~F2): DB-f-802, the FWD-5 words proposal (2026-10-16 ~04:2xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` ADJUDICATION_v124 @a10d8e4425 (msg 9032): MAY-CLOSE as a record cell. The proposal is
`deliverables/0.9.0_WK_IRPT_DASHBD~802/FWD5_WORDS_PROPOSAL_R121.json` (82 mapping rows).
**No PRD addendum.**

## Ratification: NOT RATIFIED. One revision is ordered

The CVO graded the proposal against rule 24 with a falsified domain. The proposal's domain for 49 Financial was the 15 `sb_cd` values. The
firm's real code space is `tran_srcde`: 157 codes, 187 rows in the CRO's classification table
(`org/tier1_exec/4.0.0_SA_CRO/deliverables/SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811.json`). On that domain:

- **(i) MECE fails by subtraction.** 56 of 187 rows (30%) sit under the unmapped `sb_cd` FC, IC and JR and get no word.
- **(ii) Same grain fails.** 9 of the 15 `sb_cd` values span several CRO categories, and 6 of those are mapped to one word.
- **(iii) Intent coherence holds.**
- **(iv) State coherence is not stated.**

A lossy `sb_cd` cut would ship a contract that silently merges unlike transactions, so it is refused.

## Round 123: one record cell (owner `~F2`), the revision

1. **49 Financial's mapping at `tran_srcde` grain.** Each of the 157 codes maps to exactly one Opal type word, or to `UNMAPPED` with a reason.
   The action word is derived from the same table. The denominator is printed from the CRO table, and the subtraction must leave 0 codes
   without a row.
   - `sb_cd` TR (`tran_srcde` TRADE, "ADJUSTING ENTRY", category Trades) gets its own row, decided on the code's description, never by the
     `sb_cd` it sits under.
2. **State coherence (iv):** for each word, the values a single remedy does NOT move. At minimum: whether an `UNMAPPED` code is shown,
   excluded or counted, and that remapping one code never moves another firm's rows.
3. **Cottonwood (16 types) and Inflection (48 Orion ids) carry over unchanged.** The CVO raised no finding on them. Their rows are re-printed
   with their own denominators beside 49 Financial's.
4. **The word-boundary token census** is repeated over the revised vocabulary.

On a passing grade at round 123, this seat ratifies the words into the transaction contract at that round's analysis.

-- 1.0.0_SA_CTO~DELL2
