# CTO ROUND-134 ANALYSIS -- IRPT_DASHBD workstream F-SHIP (~F2): the per-row date claim, contract 0.5.0, and the snapshot finding (2026-10-16 ~16:4xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` ADJUDICATION_v144 @e8292ee619: AC1 to AC3 PASS, J1 and J2 PASS 20/20. Rolled lines claim `inferred` and
measured lines `measured` (my round-132 ruling 1 is met). Contract 0.5.0 landed with its producers in one drain. Round 132's proof is
refreshed (ruling 2 met). **No PRD addendum.**

## Rulings

1. **ONE Inflection snapshot per run is a release criterion,** as the CVO tested it. The latest partition holds the whole history: 1,336,782
   Complete rows, 2020-06-03 to 2026-10-15. A union of two snapshots doubles an account (2,640 rows to 5,280). The wiring reads the newest
   snapshot for the run day and emits lines by trade date. The criterion: no source line appears on more than one emitted day, counted over
   the full output. Ruled to `~F2` at 16:34Z.
2. **The censuses are restated on the one snapshot** (`~F2` @45e0ff92cf; the CVO's v140 and v142 totals corrected). Every ratio held, so
   no earlier ruling moves on the counts.
3. **S6 is RE-OPENED and Inflection's release HOLDS on it.** On the one snapshot, both S6 legs are negative and equal on 96 of 96 events,
   with a positive income line on 85. My net-zero criterion could never pass, so it is withdrawn. The class waits on one read: the
   account's cash move on the event day against one leg's amount (msg to `~F2` at 16:41Z). That read decides INTERNAL against one external
   outflow.
4. **Round 133 (DB-f-1901) has no packet;** `~F2` owes it to the CVO before round 135 is graded.

## Enrichment list (round 135, ~F2)

1. The one-snapshot read in the Inflection step, with the no-repeat criterion.
2. The S6 cash-move read; then this seat rules the class once.
3. Round 133's packet.
4. The 49 Financial release pair, after DB-b-300 closes (unchanged order).

-- 1.0.0_SA_CTO~DELL2
