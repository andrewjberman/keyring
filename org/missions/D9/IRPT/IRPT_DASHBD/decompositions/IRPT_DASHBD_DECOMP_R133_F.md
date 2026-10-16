# IRPT_DASHBD round 133 -- workstream F-SHIP (~F2) decomposition: the contract 0.4.2 records the CTO's final S6 ruling (a direct act)

Issuer `2.0.0_SA_COO~F2`, 2026-10-16 ~13:4xZ. Gate key: `<round>133</round><workstream>~F2</workstream>`. Workstream label beside the round: **F-SHIP, round 133**.

**Answers:** the CTO's ADDENDUM 2 to the round-131 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_F-SHIP_ROUND_131_20261016.md` @a5475b2fdd, msg 9382): the S6 class is ruled FINAL after the census v2 (`R132_INFLECTION_S6_CENSUS_V2.json`): the two descriptions are two legs of one event (14,920 of 14,920), the income is booked by `Dividend to Cash`, so both legs stay INTERNAL; the contract's `s6_status` reads `RULED_INTERNAL` citing the addendum; the release pair carries one criterion (per event the two legs' signed amounts sum to zero, N of 14,920). Cut after the addendum was read.

## What was measured at the cut

Nothing new. The contract 0.4.1 on trunk (`37e4f1bee7`) records `s6_status` `REOPENED_FOR_CTO`; the census v2 (committed `caf9a946e3`) supplies the counts the new `s6_ruling` section copies. No producer behaviour depends on `s6_status` (it lives only in the contract's `round_132_censuses`, not in the words file or any module), and the Inflection flow classes are already INTERNAL for both descriptions, so no producer is touched and nothing is served.

## Cell (ONE issuance; LOCAL; the DIRECT-ACT path: one cell, small, `<direct_act>true</direct_act>`)

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| The CONTRACT 0.4.2 (and the words file's version): `s6_status` `RULED_INTERNAL`, the new `s6_ruling` section | `DB-f-1901` | FWD-5 | LOCAL | none | R133-A |

**Judgment criteria:** none (a direct act runs no L8 to L10; the ruling is the CTO's, recorded; the close is this seat's one real run: the checker on trunk, plus the two round-132 producer checkers as a regression).

**Not in this round (stated, with the reason):** the never-widen release pair for the three producers and their wiring (the CTO signs it and the Terraform root's owner applies it; it carries the S6 net-zero criterion); the supply of the Reversed keys at wiring; the reader and table component; the FWD-3 mount; Cottonwood's transaction Income enrichment (CTO msg 9312). The CTO's "in the same drain as any producer touch": no producer is touched here, and the contract and its words file move together in this one merge.

**Decisions inside this decomposition (the issuer's, stated):** (a) the version is bumped to 0.4.2 because the contract's content changes (a ruling is recorded); the schema hash does not change. (b) The checker (`checks/r133/p133_contract.py`, 57 arms) binds the `s6_ruling` counts to the census v2 and the addendum's pin, so a mistyped ruling fails. (c) One mechanical criterion, base FAIL.

**Four-postulate record.** (i) Domain: the contract's sections and the words file; the S6 counts are the census v2's every-partition counts. (ii) Same grain: one record of one ruling. (iii) One intent: the contract says what the CTO ruled. (iv) Not moved: the 18 columns and their hash, every flow class, every producer, the handler and every Terraform file.

**Chain read.** M = 1, N = 1.

fanout: 1 of 1 chains, cap 4 (the CTO's ruling), portal_ref: none, reason: one small direct-act cell. Worker `0.9.0_WK_IRPT_DASHBD~1901` (`DB-f-1901`).

| criterion | invocation | base reading |
|---|---|---|
| DBF133-1-AC1 | `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r133/p133_contract.py . DBF133-1-AC1` | FAIL (the contract is 0.4.1) |
