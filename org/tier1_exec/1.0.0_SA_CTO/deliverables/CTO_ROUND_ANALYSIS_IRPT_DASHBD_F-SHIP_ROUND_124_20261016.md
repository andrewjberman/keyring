# CTO ROUND-124 ANALYSIS -- IRPT_DASHBD workstream F-SHIP (~F2): the FWD-5 words at tran_srcde grain -- RATIFIED (2026-10-16 ~05:4xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` ADJUDICATION_v128 @886dbf99a3 (msg 9096): MAY-CLOSE, DBF124-1-AC1/AC2 PASS. The CVO recounted 49 Financial's
live silver: 572 partitions (2024-07-08 to 2026-10-14), 3,349,750 rows, 160 distinct `tran_srcde`. 3 codes are silver-only (EXWT, RDPC,
SQDAJ) and none is table-only; the union of 160 matches.
**No PRD addendum.**

## Rule 24, as graded

- **(i) MECE holds:** each of the 160 codes maps exactly once, 16 to `UNMAPPED` with a reason.
- **(ii) Grain holds.**
- **(iii) Intent coherence fails on two words:** `Tax withheld` (EXTERNAL-OUT and INTERNAL) and `Journal`.
- **(iv) State coherence** is stated for 22 of 22.

## Ruling on (iii): flow class is a property of the CODE, not of the word (row W1001-S2)

The type word and the flow class are two axes with two intents: the word is what a person reads, and the flow class is what the return
engine treats as money crossing the account boundary. Forcing one flow class onto a word mixes the axes, and splitting the word would mix
them the other way. So:

- **Each `tran_srcde` row carries its own `flow_class`,** from the CRO classification table (IRAWH and MCE: EXTERNAL-OUT). For the 3
  silver-only codes, the class is decided on each code's description by `~F2`, as it decided their words.
- **`Tax withheld` stays ONE word.** Withholding that leaves the account (a distribution's withholding) is EXTERNAL-OUT. Withholding inside
  the account (a foreign tax on a dividend) is INTERNAL. The code decides which, never the word.
- **`Journal` stays one word, on the same rule:** a journal between two accounts of the firm is classed per code, as the table says.
- The word's (iii) record is restated: one intent, "what the line is called". The flow-class axis is graded separately: one intent, "does
  money cross the account boundary", one value per code.

## Ratification

**The FWD-5 words are RATIFIED** at `tran_srcde` grain for 49 Financial (160 codes, 16 `UNMAPPED`), and as proposed for Cottonwood (16 types)
and Inflection (48 Orion ids), with the per-code flow class above.

- `UNMAPPED` lines are shown as "Other" with their count, never hidden. Their codes stay in the record.
- `~F2` writes the transaction contract and its per-firm producer (row S103) on these words. A new code in the silver that is not in the
  mapping reads `UNMAPPED` with reason `CODE_NOT_IN_MAPPING` until a row is added: it is counted, never dropped.

-- 1.0.0_SA_CTO~DELL2
