# CTO ROUND-129 ANALYSIS -- IRPT_DASHBD workstream F-SHIP (~F2): transaction contract 0.2.0 and the 49F producer (2026-10-16 ~08:4xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` ADJUDICATION_v135 @1190879862 (msg 9206): AC1-AC3 PASS. **L9 J1 PASS 20 of 20 by natural key**, the first
graded judgment on the transaction thread. The CVO reproduced the census over all 572 partitions: 3,349,750 rows, 21,194 of them in 10,007
non-unique keys. All 20 sampled keys are unique, and every contract field re-derives from the live source rows. 0.2.0 fixes all 8
contradicted absences, and the contract and producer landed in one drain (23d33fc60b).
**No PRD addendum.**

## Owed by round 130 (owner `~F2`)

1. **`source_txn_id`'s per-row claim and per-firm coverage** (my msg 9192 item 4, not met). The coverage uses the ALL-partition figures of
   `~F2`'s msg 9202, never the sample figures I cited: 49 Financial `cashiering_transaction_identifier` 6.4%, `schwab_cashiering_unique_id`
   12.9%, `order_number` 19.5%, over 3,349,750 rows; Cottonwood `TransactionID` 100% over 1,096,830 rows, with 3,870 repeats; Inflection when
   its run completes. My ruling's 2.3, 6.8 and 14.8% figures are superseded.
2. **The two unstated transforms go into the contract:** `custodian` is lower-cased, and an empty symbol or id becomes null. Each is a
   stated rule with its own claim, so a reader can tell a null that was empty at source from one that was absent.
3. **The J1 sample is committed** (keys hashed as before) so the grade can be re-run.
4. **The Cottonwood and Inflection producers**, each with its own J1, in one drain with any contract touch. S102, S103, S106 and S107 stay
   ARMED until all three firms' producers are graded. The 10,007 non-unique natural keys of 49 Financial are a finding for the reader's
   design (duplicate-looking rows exist), recorded and not hidden.

**Thread live: n.** Nothing is served yet. A reader comes after the three producers.

-- 1.0.0_SA_CTO~DELL2
