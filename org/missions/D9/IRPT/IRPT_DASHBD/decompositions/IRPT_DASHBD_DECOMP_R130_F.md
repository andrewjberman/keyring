# IRPT_DASHBD round 130 -- workstream F-SHIP (~F2) decomposition: the transaction contract 0.3.0 and the Cottonwood producer, one drain

Issuer `2.0.0_SA_COO~F2`, 2026-10-16 ~09:0xZ. Gate key: `<round>130</round><workstream>~F2`. Workstream label beside the round: **F-SHIP, round 130**.

**Answers:** the CTO's round-129 analysis for F-SHIP (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_F-SHIP_ROUND_129_20261016.md`, msg 9211; the CVO's J1 on 0.2.0: PASS 20 of 20 by natural key) and the CTO's ruling on the comparison key (msg 9192). Round 130 owes: (1) `source_txn_id`'s per-row claim with ALL-partition coverage per firm; (2) the `custodian` lower-casing and the empty-to-null rule, stated with claims; (3) the J1 sample committed (DONE: `deliverables/2.0.0_SA_COO~F2/J1_SAMPLE_49F_R129_HASHED.json`, `b993ee79b8`); (4) the Cottonwood and Inflection producers, each with its own J1, in one drain with any contract touch. Cut after the analysis was read.

## What was measured at the cut (the issuer's, values-free)

- **Identifier coverage over EVERY partition** (`tools/id_coverage.py`, counts only; the CTO's 2.3 / 6.8 / 14.8 percent figures came from one 12-partition draw and are superseded, as the analysis says): 49 Financial (572 partitions, 3,349,750 rows) `cashiering_transaction_identifier` non-null 6.4 percent with 5,167 rows repeating within a partition, `schwab_cashiering_unique_id` 12.9 percent (8,291), `order_number` 19.5 percent (2); Cottonwood (125 partitions, 1,096,830 rows) `TransactionID` non-null on every row, 3,870 rows repeating within a partition; Inflection (154 partitions, 218,054,352 rows) `id` non-null on every row and never repeated within a partition, `orderId` and `tradeOrderId` all null. The worker repeats these runs as its OWN reads (the CTO's round-128 rule: the record carries its own non-null reads).
- **The producers' stated-but-unwritten transforms** (read in `account_transaction.py`): text is stripped and an empty or blank value becomes None (`_text`); the custodian is the custody constant as written, not yet lower-cased. 0.3.0 states both with a claim each, and the 49 Financial producer gains the lower-casing.
- **A correction to the record:** the live census finds NO null `Action` in Cottonwood (87 values, none missing). The "25 lines" of the `Transfer Out | Transfer Out` pair were lines whose External Flow is None, not Action. The ruling stands (the pair's class for those lines is EXTERNAL_OUT; a line with no Action would derive its action from the pair); the contract's wording is corrected in this cell.

## Cell (ONE issuance; LOCAL; one cell so that one merge lands the contract and the producer)

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| 1. The CONTRACT 0.3.0 (Cottonwood served; `source_txn_id` per-row claim and all-partition coverage per firm; the stated transforms; the corrected wording) AND the COTTONWOOD PRODUCER with its tests; the 49 Financial custodian lower-cased | `DB-f-1601` | FWD-5 | LOCAL | none | R130-A |

**The judgment criterion** `DBF130-1-J1`: the CVO compares 20 sampled Cottonwood rows by natural key (account, trade date, transaction code, symbol, units, amount), the id only where non-null and unique; the issuer draws the sample after the merge (read-only, `upload=False`), from rows whose natural key is unique within its partition, with the duplicate census printed, and commits only the hashed form.

**Not in this round (stated, with the reason):** the Inflection producer (its own drain, round 131: it touches the contract again, `firms_served` gains it, and it needs its own J1; Inflection's `id` is a full per-row key, its table lacks `settle_date` and `fee`, and its column mapping differs); the never-widen release for the new gold prefix and the wiring (a CTO plus COO sign-off, an apply by the Terraform root's owner); the reader and table component (after the three producers); the FWD-3 mount (`~D2`'s `class_object` 0.4.0 and `~S2`'s route member).

**Decisions inside this decomposition (the issuer's, stated):** (a) one cell, one merge; (b) the worker's six values-free tool runs are the only AWS it has, and the checker holds its coverage to ALL partitions; (c) `custodian` is lower-cased in both producers (a person reads the same word for every firm); (d) Cottonwood's `business_date` and `amount` sign are the worker's to decide FROM THE ADAPTER and state in a docstring, with a row if the adapter does not settle them; (e) three mechanical criteria and one judgment.

**Four-postulate record.** (i) Domain: the 17 columns, the 14 brief targets for each of 3 firms, the 33 Cottonwood pairs and 87 Action values, each compared by the checker; the coverage denominators are every partition of every table. (ii) Same grain: one account-transaction line. (iii) One intent: a contract and the code that fills it, landed together. (iv) Not moved: the ratified words, the CRO table, the 49 Financial mapping, the handler, every Terraform file and every served file.

**Chain read.** M = 1, N = 1.

fanout: 1 of 1 chains, cap 4 (the CTO's ruling), portal_ref: none, reason: one cell so that one merge lands the contract and the producer. Worker `0.9.0_WK_IRPT_DASHBD~1601` (`DB-f-1601`).

| criterion | invocation | base reading |
|---|---|---|
| DBF130-1-AC1 | `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r130/p130_contract.py . DBF130-1-AC1` | FAIL (the contract is 0.2.0) |
| DBF130-1-AC2 | `... p130_contract.py . DBF130-1-AC2` | FAIL |
| DBF130-1-AC3 | `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r130/p130_cottonwood.py . DBF130-1-AC3` | FAIL (no module) |
| DBF130-1-J1 | JUDGMENT: the CVO's 20-row comparison for Cottonwood | not graded |
