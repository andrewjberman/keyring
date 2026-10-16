# IRPT_DASHBD round 124 -- workstream F-SHIP (~F2) decomposition: the FWD-5 words revision at tran_srcde grain

Issuer `2.0.0_SA_COO~F2`, 2026-10-16 ~04:5xZ. Gate key: `<round>124</round><workstream>~F2</workstream>`. Workstream label beside the round: **F-SHIP, round 124**.

**Answers:** the CTO's round-122 analysis for F-SHIP (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_F-SHIP_ROUND_122_20261016.md`, msg 9036): the words are NOT ratified (the CVO's rule-24 grade holds) and one revision is ordered. The analysis calls it "round 123"; round 123 already carried the producer ground read (`DB-f-901`, cut at `ef2e1b0ecc` before the analysis arrived, and the gate allows one issuance per round), so the revision is round 124. The cell is the same one the analysis orders.

## What was measured at the cut

- The CVO's finding stands against round 122: its domain for 49 Financial was the 15 `sb_cd` values; the firm's code space is `tran_srcde`: 157 distinct codes in 187 rows of the CRO classification table. Read by this seat: 10 of the 157 codes carry more than one distinct `rule` in the table (for example ADJ, DIV, DIVAJ, DFRAJ, DPINS, NDIV), so a one-word mapping of those needs a stated reason.
- The code `TRADE` is the table's `tran_srcde` for the `TR`/`TR` pair, description "ADJUSTING ENTRY", rule `trades`: the row the round-122 packet flagged and the CTO ordered decided on its own description.
- Cottonwood (16) and Inflection (48) carry over unchanged (no CVO finding on them); the checker holds them equal to the round-122 proposal's rows.

## Cell (ONE issuance; LOCAL, a proposal record)

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| 1. The REVISED WORDS PROPOSAL: 49 Financial at tran_srcde grain (157 rows), state coherence per word, Cottonwood and Inflection carried over, the census repeated | `DB-f-1001` | FWD-5 | LOCAL | none | R124-A |

**Decisions inside this decomposition (the issuer's, stated):** (a) the checker computes the 49 Financial denominator FROM THE CRO TABLE and the carry-over FROM the round-122 proposal, so a hand-printed denominator cannot pass; (b) the 49 Financial `tr_cd` action rows are dropped: the action is derived from the type through the one table, as the CTO ordered; (c) a code whose CRO rows disagree on `rule` is mapped to a word only with a stated reason, else `UNMAPPED`; (d) no contract is written; the CTO ratifies on a passing grade; (e) two mechanical criteria.

**Four-postulate record.** (i) Domain: the 157 distinct `tran_srcde` codes of the CRO table plus the 16 and 48 carried values; the subtraction is computed by the checker. (ii) Same grain: one source code to one Opal type word. (iii) One intent. (iv) Not moved: the CRO table, every code file, the round-120 and round-122 records, every contract and served file.

**Chain read.** M = 1, N = 1.

fanout: 1 of 1 chains, cap 8 (the CTO's CPU budget holds `~F2` at 4 per issuance), portal_ref: none, reason: one independent record cell. Worker `0.9.0_WK_IRPT_DASHBD~1001` (`DB-f-1001`).

| criterion | invocation | base reading |
|---|---|---|
| DBF124-1-AC1 | `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r124/p124_words49.py . DBF124-1-AC1` | FAIL (no record) |
| DBF124-1-AC2 | `... p124_words49.py . DBF124-1-AC2` | FAIL (no record) |
