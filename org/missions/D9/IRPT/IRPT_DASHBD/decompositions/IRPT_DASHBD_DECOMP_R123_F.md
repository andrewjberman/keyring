# IRPT_DASHBD round 123 -- workstream F-SHIP (~F2) decomposition: the FWD-5 producer ground read (49 Financial)

Issuer `2.0.0_SA_COO~F2`, 2026-10-16 ~04:1xZ. Gate key: `<round>123</round><workstream>~F2</workstream>`. Workstream label beside the round: **F-SHIP, round 123**.

**Answers:** the empty-tick sequence (`/next-calls IRPT_DASHBD --drive`), which found one FREE option around the FWD-5 block, and the CTO's rulings that `~F2` writes the transaction contract and its producer (round-119 analysis ruling 3) and that the first served account is a 49 Financial one (round-121 analysis, msg 8991). The CTO's ratification of the round-122 words is pending; this cell does not depend on it.

## What was measured at the cut

- The ratification fixes only the enum (the words for `action` and `txn_type`). The contract's SHAPE (grain, partition, columns, the per-firm fence) and the producer's SOURCE MAPPING do not depend on it.
- The brief names 14 columns for `account_transaction` (line 78 of the reporting-dashboard backend brief). The round-120 record lists the 14 columns the 49 Financial code reads for a transaction; the brief's list has columns that list does not obviously supply (a settle date, a fee, a source transaction id, an asset name). Which are ABSENT is a fact the contract needs before it is written: an absent column becomes a stated absence in the contract, not an invented value.
- `account_transaction` would be the third gold table the reporting-gold function emits beside `account_return_daily` and `account_class_daily`; the address must come from the naming builder, and a refusal is a missing registry row (CLAUDE.md rule 30).

## Cell (ONE issuance; LOCAL, a read)

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| 1. The FWD-5 PRODUCER GROUND READ for 49 Financial: per brief column the silver source or ABSENT; the pattern producer; the silver source; the builder address and registry row; the emit path's touch-points | `DB-f-901` | FWD-5 | LOCAL | none | R123-A |

**Not in this round (stated, with the reason):** the FWD-3 mount (`DB-f-803`) waits on `~D2`'s `class_object` 0.4.0 and `~S2`'s route member (round-121 analysis); the transaction contract and producer wait on this read and on the ratified words.

**Decisions inside this decomposition (the issuer's, stated):** (a) 49 Financial only, as the CTO ruled the first served account; Cottonwood and Inflection get the same read after it; (b) the one local call of the naming builder is allowed (no AWS); (c) the worker adds no registry row (a refusal is reported); (d) one mechanical criterion.

**Four-postulate record.** (i) Domain: the brief's 14 columns, a printed list, checked by exact equality in order. (ii) Same grain: one account-transaction line. (iii) One intent: where each column comes from. (iv) Not moved: the contract, the producer, the registry, every served file.

**Chain read.** M = 1, N = 1.

fanout: 1 of 1 chains, cap 8 (the CTO's CPU budget holds `~F2` at 4 per issuance), portal_ref: none, reason: one independent read cell. Worker `0.9.0_WK_IRPT_DASHBD~901` (`DB-f-901`).

| criterion | invocation | base reading |
|---|---|---|
| DBF123-1-AC1 | `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r123/p123_ground.py . DBF123-1-AC1` | FAIL (no record) |
