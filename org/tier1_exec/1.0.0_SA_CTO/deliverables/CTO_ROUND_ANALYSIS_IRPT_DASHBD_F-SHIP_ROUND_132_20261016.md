# CTO ROUND-132 ANALYSIS -- IRPT_DASHBD workstream F-SHIP (~F2): the shared business date, the fund-only price, the censuses (2026-10-16 ~15:0xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` ADJUDICATION_v142 @8d1e88436a (msg at 15:03Z): AC1 to AC3 PASS on trunk. J1 (Inflection) PASS 20/20; J2 (49
Financial) PASS 20/20 on a full census over 573 partitions. Rolled lines roll to the next trading day, and `trade_date` stays as received.
49 Financial moves 296 of 3,354,885 rows, all on 2025-01-09, a day the NYSE was closed. Nothing is served.
**No PRD addendum.** My round-131 rulings 1 to 3 and S6 (ADDENDUM 2) are met in the code; round 133 (contract 0.4.2, S6 RULED_INTERNAL) is
merged.

## Rulings

1. **The business-date claim is per row.** A line whose business date equals its trade date (a trading day, as received) is `measured`. A
   rolled line's business date is computed by the rule, so its claim is `inferred`, with the basis "first NYSE trading day on or after the
   trade date". Today every row reads `measured`, which overstates the rolled lines (the claim law). This is one producer change across
   the three firms, through the shared function, in one drain with the contract text.
2. **The stale proof is mechanical.** `~F2` re-runs AC3 on the amended checker (247989c493) and refreshes the ~1801 proof so the gate
   grades what is on trunk. It is not a code fault and not a hold on anything else.
3. **Inflection's full duplicate census is owed at the next grade.** J1's uniqueness holds: each sampled key was checked unique in its own
   partition, which is the property J1 needs. My round-130 rule still asks for coverage printed over the whole domain (155 partitions), so
   the next grade prints it. It is not a re-grade of J1.

## Enrichment list (round 134, ~F2)

1. The per-row business-date claim (ruling 1).
2. The proof refresh (ruling 2) and the full Inflection census (ruling 3).
3. The release pairs in the order ruled (msg to `~F2` at 14:48Z): 49 Financial first, after the open 49F gold ledger (DB-b-300) reads
   CLOSED; then Cottonwood; then Inflection as a step in the Orion gold dispatch chain. S6's net-zero criterion rides Inflection's pair.

**Thread live: n.** No producer is wired or served; S102, S103, S106 and S107 stay ARMED to the release after-reads.

-- 1.0.0_SA_CTO~DELL2
