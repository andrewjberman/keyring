# IRPT_DASHBD round 122 -- workstream F-SHIP (~F2) decomposition: the FWD-5 words proposal

Issuer `2.0.0_SA_COO~F2`, 2026-10-16 ~03:2xZ. Gate key: `<round>122</round><workstream>~F2</workstream>`. Workstream label beside the round: **F-SHIP, round 122**.

**Answers:** the CTO's round-120 analysis for F-SHIP (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_F-SHIP_ROUND_120_20261016.md`, msg 8917), ruling 1: `~F2` PROPOSES Opal's action and type words and the CTO ratifies; a rule-24 record, a word-boundary census and a per-firm mapping table in which every source value maps to exactly one Opal word or to `UNMAPPED` with a reason; a firm with no action field gets its action derived from the type through the same table. Round 121 (the class-series reader, `DB-f-801`, merged) was cut before this analysis was read; the gate allows one issuance per round, so the words cell is this round's.

## What was measured at the cut

- The denominator is the round-120 record `deliverables/0.9.0_WK_IRPT_DASHBD~701/RD_FWD5_FIELDS_R120.json`: 49 Financial 3 action + 15 type values, Cottonwood 0 + 16, Inflection 0 + 48 (82 in all), and 7 flow classes in the backend brief. No file defines Opal's words for them.
- The meanings of the 49 Financial codes live in the CRO classification table; Cottonwood's in `TYPE_CLASS`; Inflection's in the Orion cashflow taxonomy (each entry carries a bucket). The worker reads those, and any value for which the repository gives no meaning is `UNMAPPED` with that reason, never a guess.

## Cell (ONE issuance; LOCAL, a proposal record)

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| 1. The FWD-5 WORDS PROPOSAL: Opal's closed type words (each carrying its action and flow class), a mapping row for each of the 82 source values, and the rule-24 record with a word-boundary census; for the CTO to ratify | `DB-f-802` | FWD-5 | LOCAL | none | R122-A |

**Not in this round (stated, with the reason):** the `AssetClassSection` mount (FWD-3). The CTO's ruling 3 makes it wait on `~D2`'s committed 0.4.0 shape, read at the cut; `IRPT_DASHBD_SERIES_CONTRACT.json` is at 0.2.0 with no `class_object` section at this commit, so there is nothing to read the reader against. It is cut when that file lands (it stacks on the merged reader, `DB-f-801`).

**Decisions inside this decomposition (the issuer's, stated):** (a) a PROPOSAL only: nothing is written to `org/standards/` and no contract is created, the CTO ratifies into the contract at the round-122 analysis; (b) the checker computes the subtraction from the round-120 record itself, so a source value with no row, a row with no source value, a duplicate or an undefined word fails; (c) the worker's worktree carries the folders it reads (`--sparse-add`), the round-119 lesson; (d) two mechanical criteria.

**Four-postulate record.** (i) Domain: one proposal record over a printed 82-value denominator. (ii) Same grain: one transaction line's type and action. (iii) One intent. (iv) Not moved: every contract, producer, code table and served file.

**Chain read.** M = 1, N = 1.

fanout: 1 of 1 chains, cap 8 (the CTO's CPU budget holds `~F2` at 4 per issuance), portal_ref: none, reason: one independent record cell. Worker `0.9.0_WK_IRPT_DASHBD~802` (`DB-f-802`).

| criterion | invocation | base reading |
|---|---|---|
| DBF122-1-AC1 | `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r122/p122_words.py . DBF122-1-AC1` | FAIL (no record) |
| DBF122-1-AC2 | `... p122_words.py . DBF122-1-AC2` | FAIL (no record) |
