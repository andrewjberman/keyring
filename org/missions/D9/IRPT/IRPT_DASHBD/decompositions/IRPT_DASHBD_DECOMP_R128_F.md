# IRPT_DASHBD round 128 -- workstream F-SHIP (~F2) decomposition: the FWD-5 ground read with source reads, and Cottonwood's words re-cut

Issuer `2.0.0_SA_COO~F2`, 2026-10-16 ~07:0xZ. Gate key: `<round>128</round><workstream>~F2</workstream>`. Workstream label beside the round: **F-SHIP, round 128**.

**Answers:** the CTO's round-126 analysis for F-SHIP (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_F-SHIP_ROUND_126_20261016.md`, msg 9133): the `absent` claims of the ground reads are VOID wherever the live schema shows the field (a read that read no source cannot say absent); round 127 repeats the ground read with source reads, and Cottonwood's ratified words are SUSPENDED and re-cut at the (Transaction Type, Sub Type) grain with the action from the vendor's Action column. The analysis calls it "round 127"; round 127 (the transaction contract and the 49 Financial producer) was already issued before it arrived, so these cells are round 128. The same ruling also bears on this seat's own work: the round-123 ground read of 49 Financial read no source either (`s3_reads 0`), and the contract it fed (`DB-f-1301`, merged) and the producer in flight (`DB-f-1302`) carry its `absent` claims for `fee` and `source_txn_id`. They are re-measured here and the contract is amended from the result (a later cell).

## What was measured at the cut (the issuer's live source read, 2026-10-16 ~06:40Z, recorded)

The record is `deliverables/2.0.0_SA_COO~F2/R128_LIVE_SOURCE_CENSUS_3FIRMS.json`: per firm the partitions read, rows, the full column list with types, and the code values of the type columns. Counts and code values only (no account id, no amount, no description text; the Cottonwood client-name, address and account columns exist and were not read).

| firm | table | partitions read | rows | columns | code values |
|---|---|---|---|---|---|
| 49 Financial | `fact_trn` | 572 | 3,349,750 | 140 | `tran_srcde` 160, `tr_cd` 3, `sb_cd` 15 (the round-124 census) |
| Cottonwood | `fact_transactions` | 125 (2 empty) | 1,096,830 | 73 | `Transaction Type` 16, `Transaction Sub Type` 31, `Action` 87, 33 type and sub-type pairs, `External Flow` Contribution / Withdrawal / None |
| Inflection | `fact_transactions` | 154 | 218,054,352 | 36 | `transactionDescription` 47, `transTypeId` 47, `custodianName` 2, `productName` 1,675 |

What the schemas show that the code-only reads missed (names only): 49 Financial carries several fee columns, order and cashiering identifier columns and a trade date; Cottonwood carries `TransactionID`, `Units`, `Price`, `Transaction Fee`, `Settle Date`, `Trade Date`, `Symbol`, `Ticker`, `CUSIP`, `Asset Name` and `Custodian`; Inflection carries `id`, `ticker`, `noUnits`, `navPrice`, `transAmount`, `productName`, `custodianName` and `orderId`, and neither a settle date nor a fee column (agreeing with the CTO).

## Cells (ONE issuance; LOCAL; two independent chains)

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| 1. The GROUND READ WITH SOURCE READS for the three firms: each of the brief's 14 columns mapped to a live column, a computation from live columns, or ABSENT with every searched column printed | `DB-f-1401` | FWD-5 | LOCAL | none | R128-A |
| 2. COTTONWOOD'S WORDS RE-CUT: 33 type and sub-type pairs and 87 Action values, flow class per code from External Flow, state coherence, rule-24 record and census | `DB-f-1402` | FWD-5 | LOCAL | none | R128-B |

**Not in this round (stated, with the reason):** the contract amendment (0.2.0) and the producer revision that follow from cell 1 (cut once the records exist; the producer cell `DB-f-1302` of round 127 is still in flight on the 0.1.0 contract, whose schema hash does not depend on the claims); Inflection's 48th ratified id marked `not_observed` (47 live; the CTO's rule, carried into the contract amendment); the FWD-3 mount.

**Decisions inside this decomposition (the issuer's, stated):** (a) the live source read is the issuer's, as for round 124, because a worker has no AWS access; the cells work from the recorded census and the checkers hold every cited column to its column list; (b) the ground-read form gains `from_columns` and `method` so a computed field reads `inferred` with a method (the CTO's round-123 ruling) instead of being forced to `absent`; an `absent` target must print the whole searched column list; (c) the checker holds the CTO's fixed points (Inflection's settle date and fee absent; Cottonwood's settle date, symbol, units, price, custodian and trade date never absent); (d) Cottonwood's flow class is the vendor's own External Flow column applied to the pair, so no judgment is needed for a pair that is only ever Contribution or Withdrawal; (e) 49 Financial and Inflection words stay ratified.

**Four-postulate record.** (i) Domain: the brief's 14 columns and each firm's printed live column list (cell 1); the 33 pairs and 87 Action values of the live census (cell 2), compared by exact equality. (ii) Same grain: one account-transaction line; one pair; one Action value. (iii) One intent per cell. (iv) Not moved: the contract, the producer, the ratified words of the other two firms, every code file and every served file.

**Chain read.** M = 2 (A: 1401; B: 1402), N = 2, no edge.

fanout: 2 of 2 chains, cap 8 (the CTO's CPU budget holds `~F2` at 4 per issuance; worker `~1302` of round 127 is also running), portal_ref: none, reason: two independent record cells with disjoint write sets. Workers `0.9.0_WK_IRPT_DASHBD~1401` (`DB-f-1401`) and `~1402` (`DB-f-1402`).

| criterion | invocation | base reading |
|---|---|---|
| DBF128-1-AC1 | `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r128/p128_ground3.py . DBF128-1-AC1` | FAIL (no records) |
| DBF128-2-AC1 | `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r128/p128_cwwords.py . DBF128-2-AC1` | FAIL (no record) |
| DBF128-2-AC2 | `... p128_cwwords.py . DBF128-2-AC2` | FAIL (no record) |
