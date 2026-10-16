# IRPT_DASHBD round 129 -- workstream F-SHIP (~F2) decomposition: the transaction contract 0.2.0 and the 49 Financial producer revision, one drain

Issuer `2.0.0_SA_COO~F2`, 2026-10-16 ~07:4xZ. Gate key: `<round>129</round><workstream>~F2</workstream>`. Workstream label beside the round: **F-SHIP, round 129**.

**Answers:** the CTO's round-127 analysis for F-SHIP (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_F-SHIP_ROUND_127_20261016.md`, msg 9162): contract 0.1.0 is a DRAFT; the next round delivers 0.2.0 on four conditions: (1) every target's source column per firm read with `s3_reads > 0`, `fee` a stated sum with a `fee_basis`; (2) contract and producers land in ONE drain; (3) a judgment criterion (the CVO compares 20 sampled rows per firm against the source by the source's own id); (4) a rule-24 record for every new enum, not a citation; fan-out 4 or fewer. The analysis calls it "round 128"; round 128 was the ground read (issued before the analysis arrived), so this is round 129. This seat did not cut it before the analysis was read: the lesson of rounds 121 and 123.

## What was measured at the cut

- Round 128 is merged (the ground read with source reads, `da3f781d93`; Cottonwood's words re-cut, `11555369b0`). The 49 Financial record shows: sourced `trade_date`, `settle_date` (`settlmnt_date`), `symbol`, `units`, `price` and `source_txn_id` (`cashiering_transaction_identifier`); computed `action`, `fee` (nine fee columns), `flow_class`, `coverage`; `asset_name` the only absent target (all 140 columns printed). Cottonwood has all 14 filled; Inflection lacks `settle_date` and `fee` only.
- The merged contract (0.1.0) and the merged producer (round 127) say `settle_date`, `fee` and `source_txn_id` are absent and write `None`; the producer must read them.
- Cottonwood's re-cut words are a proposal awaiting the CTO's ratification, so they are not in the contract; 49 Financial and Inflection words stay ratified (Inflection's 48th id has no live row: `not_observed`).
- The two value sets 0.2.0 adds that are not the ratified words: the `coverage` values and the flow-class rule over the CRO table's 30 `(partition, rule)` pairs. Each gets its own rule-24 record and computed census.

## Cell (ONE issuance; LOCAL; one cell so that one merge lands both)

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| 1. The CONTRACT 0.2.0 (per-firm sources, `fee_basis`, the ratified words for 49 Financial and Inflection, `not_observed`, two rule-24 records) AND the 49 FINANCIAL PRODUCER REVISION (settlement date, fee sum, identifier) with their tests | `DB-f-1501` | FWD-5 | LOCAL | none | R129-A |

**One cell, not two:** the CTO's condition (2) is that the contract and the producer land in ONE merge (round 127 landed them 27 minutes apart, so the trunk held a contract its producer did not meet). One worker, one branch, one merge removes the gap. Mechanical criteria are three (the contract's form, the contract's bindings, the producer against the contract); the fourth is the CVO's judgment criterion.

**The judgment criterion (condition 3).** `DBF129-1-J1`: the CVO compares 20 sampled rows of the 49 Financial producer's output against the source rows by `cashiering_transaction_identifier`. The issuer produces the sample after the merge: a read-only run of `normalize_trn` on live partitions with `upload=False` (nothing is written), with a fixed seed over the date range, and hands the CVO the path. The sample holds client figures, so it is NOT committed. Cottonwood and Inflection have no producer yet, so their 20-row samples are owed when theirs exist (the criterion says so). S102, S103, S106 and S107 stay ARMED until a round passes it.

**Not in this round (stated, with the reason):** the Cottonwood and Inflection producers (Cottonwood's words await ratification; Inflection's producer is not yet cut); the never-widen release for the new gold prefix and the wiring (a later cell and a CTO plus COO sign-off, an apply by the Terraform root's owner); the table component and reader (wait on the release); the FWD-3 mount (waits on `~D2`'s `class_object` 0.4.0 and `~S2`'s route member).

**Decisions inside this decomposition (the issuer's, stated):** (a) 49 Financial is the only firm served in 0.2.0; (b) `fee` for 49 Financial is the stated sum of the ground read's nine fee columns, a null column counting as nothing and an all-null line having `fee` null, never zero; the ground read's two excluded fee-like columns stay out and the contract names them; (c) `custodian` stays the custody entry's constant (the ground read also names `custdian_id`; a person reads the name, not the id); (d) the data file carries `fee_basis` if the producer needs it, so the column names are not typed twice; (e) the live source read for the sample is the issuer's, as for rounds 124 and 128.

**Four-postulate record.** (i) Domain: the 17 columns, the 14 brief targets for each of 3 firms, the 30 CRO pairs, the 160 live 49 Financial codes and Inflection's 48 ratified descriptions, each compared by the checker. (ii) Same grain: one account-transaction line. (iii) One intent: a contract and the code that fills it, landed together. (iv) Not moved: the ratified words, the CRO table, the handler, every Terraform file and every served file.

**Chain read.** M = 1, N = 1.

fanout: 1 of 1 chains, cap 4 (the CTO's ruling), portal_ref: none, reason: one cell so that one merge lands both. Worker `0.9.0_WK_IRPT_DASHBD~1501` (`DB-f-1501`).

| criterion | invocation | base reading |
|---|---|---|
| DBF129-1-AC1 | `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r129/p129_contract.py . DBF129-1-AC1` | FAIL (the draft is 0.1.0) |
| DBF129-1-AC2 | `... p129_contract.py . DBF129-1-AC2` | FAIL |
| DBF129-1-AC3 | `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r129/p129_producer.py . DBF129-1-AC3` | FAIL (the test names lack fee, settle, identifier) |
| DBF129-1-J1 | JUDGMENT: the CVO's 20-row comparison | not graded |
