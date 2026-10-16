# IRPT_DASHBD round 137 -- workstream F-SHIP (~F2) decomposition: the 49 Financial transaction apply, the Cottonwood host read, the Inflection pair's reads, and round 135's packet

Issuer `2.0.0_SA_COO~F2`, 2026-10-16 ~22:5xZ. Gate key of the one cell: `<round>137</round><workstream>F2APPLY</workstream>`. Workstream label beside the round: **F-SHIP, round 137**.

**Answers:** the CTO's round-136 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_F-SHIP_ROUND_136_20261016.md` @7d7bb3a642, msg 9966): round 136 CLOSES on the CVO's ADJUDICATION_v146 (J1 and J2 PASS 20 of 20; one snapshot per run 646 of 646; S6 INTERNAL, 96 plus 96); no PRD addendum. The enrichment list, with the state of each item at the cut:
1. **The 49 Financial transaction apply by `0.7.0_AE_CloudOps~IB2`** (receipt, the first scheduled fire's read, the margin check after Act 3): **cell `DB-f-2204`**, the order issued under round 136 (`418869a62b`) and RE-TAGGED to round 137 here, because the CTO set the apply as round 137's first act and closed round 136 with the order still pending. It stood at a STOP before the apply on a wording defect of the issuer's: the plan puts the new resource second in the policy's Resource list, and the order and checker had said "last" (a list in IAM is a set). AMENDED (the order and `p136_apply.py`, 12 selftest arms): the gate reads the SET; nothing applied.
2. **The Cottonwood host: the read-only sizing read now** (the CTO's message 9962; cells wait on XA-20261016T224156Z-3c21): the issuer's read, recorded in `R137_COTTONWOOD_SIZING_READ.md`. No cell is cut.
3. **The Inflection pair's reads:** the S6 "N of 96" print (done in round 136: 96 of 96), the live read of whether the runner's flat sync of `code/gold` copies the `.zip` beside the launcher, and the bundle pin re-cut at release (never carried). The pair itself follows the 49 Financial pair's applied result and the Cottonwood pair.
4. **Round 135's L8 packet to the CVO:** written and sent (`L8_PACKET_R135_F.md` @a822b5a00e).

## Cell (ONE order; WORLD)

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| The apply of the signed pair (packet sha256 `b67bd4ad57f2`): bundle, ONE `safe-apply` (plan 0/2/0, the policy change read as a SET), a transaction-only dry run, the 720 s time trigger, the first one-day write, a 25-day range | `DB-f-2204` | FWD-5 | WORLD | `DB-f-2201`, `DB-f-2202`, `DB-f-2203` (merged); both halves SIGNED | R137-A |

Three mechanical criteria (the checker `checks/r136/p136_apply.py` is the one the order carries; its fresh-read path was exercised against the world): `DBF136-4-AC1` (the record's head), `DBF136-4-AC2` (fresh live reads), `DBF136-4-AC3` (the events and the new prefix's counts). The criterion ids keep their round-136 names because the order carries them already. **Decisions (the issuer's):** (a) the order is a modification of an existing file, re-tagged, not a new order; (b) the first scheduled fire after the apply is READ by the issuer (the ledger's leg L7) and is the acceptance of the scheduled path, a stated wait on the CTO's own condition 6, not an unproven outcome of the cell; (c) the Cottonwood and Inflection cells are NOT cut this round (their dependencies are stated above). fanout: 1 of 1 chains, cap 4.

**Four-postulate record.** (i) Domain: one function, one role policy, one new gold prefix, 26 day partitions at most. (ii) Same grain: a day partition per trading day. (iii) One intent: the table is written, nothing else, and nothing reads it. (iv) Not moved: the five other gold tables, the filled report, the published series, every read and list grant, the schedule.

| criterion | invocation | base reading |
|---|---|---|
| DBF136-4-AC1 | `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r136/p136_apply.py . DBF136-4-AC1` | FAIL (no record) |
| DBF136-4-AC2 | `python -I .../checks/r136/p136_apply.py . DBF136-4-AC2` | FAIL (no record) |
| DBF136-4-AC3 | `python -I .../checks/r136/p136_apply.py . DBF136-4-AC3` | FAIL (no record) |
