# IRPT_DASHBD round 126 -- workstream F-SHIP (~F2) decomposition: the FWD-5 producer ground read for Cottonwood and Inflection

Issuer `2.0.0_SA_COO~F2`, 2026-10-16 ~05:3xZ. Gate key: `<round>126</round><workstream>~F2</workstream>`. Workstream label beside the round: **F-SHIP, round 126**.

**Answers:** the empty-tick sequence (`/next-calls IRPT_DASHBD --drive`), which found one FREE option around the FWD-5 block: round 123 read the 49 Financial ground only; the transaction contract and the per-firm producers (CTO round-119 analysis ruling 3: "from the custody transaction silver per firm") need the same measurement for the other two firms, on which the CTO's live read found the class prefixes empty and the first served account is a 49 Financial one (round-121 analysis).

## What was measured at the cut

- The round-120 record lists the columns the code reads: Cottonwood 5 (`AccountID`, `Trade Date`, `External Flow`, `Transaction Type`, `Market Value`), Inflection 11 (`id`, `accountId`, `clientId`, `householdId`, `transTypeId`, `transDate`, `transAmount`, `noUnits`, `navPrice`, `ticker`, `transactionDescription`), against the brief's 14. Most of the brief's columns therefore have no source column in the code a worker can read; the contract needs those absences stated, not invented.
- Round 123's open decision (CTO round-123 analysis ruling 1): a field the producer computes carries `inferred` with a method, never `absent`. This cell asks the worker to say in `words` which targets are computed, so the contract can carry them correctly.

## Cell (ONE issuance; LOCAL, a read)

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| 1. The FWD-5 PRODUCER GROUND READ for Cottonwood and Inflection: per firm, per brief column the source or ABSENT; the pattern producer; the source; the builder address and registry row; the emit path | `DB-f-1201` | FWD-5 | LOCAL | none | R126-A |

**Not in this round (stated, with the reason):** the contract and producers (wait on the ratified words and these reads); the FWD-3 mount (waits on `~D2`'s `class_object` 0.4.0 and `~S2`'s route member).

**Decisions inside this decomposition (the issuer's, stated):** (a) two records of one form in one cell, one criterion (the checker runs both); (b) the one local call of the naming builder per firm is allowed (no AWS); (c) the worker adds no registry row; (d) no compound criterion: one checker, one pass line.

**Four-postulate record.** (i) Domain: the brief's 14 columns, a printed list, checked by exact equality in order, for each of two firms. (ii) Same grain: one account-transaction line. (iii) One intent: where each column comes from. (iv) Not moved: the contract, the producers, the registry, every served file.

**Chain read.** M = 1, N = 1.

fanout: 1 of 1 chains, cap 8 (the CTO's CPU budget holds `~F2` at 4 per issuance; workers `~1001` and `~1101` are also running), portal_ref: none, reason: one independent read cell. Worker `0.9.0_WK_IRPT_DASHBD~1201` (`DB-f-1201`).

| criterion | invocation | base reading |
|---|---|---|
| DBF126-1-AC1 | `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r126/p126_ground2.py . DBF126-1-AC1` | FAIL (no records) |
