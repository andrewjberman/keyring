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

## ADDENDUM 1 -- S6 ruled on the cash-move read (2026-10-16 ~16:4xZ)

`~F2`'s read (`R135_INFLECTION_S6_CASH_MOVE.json`, 96 events, one snapshot, within 1 cent): custodial cash fell by about one leg's amount
(X) on 75 events, about 0 on 18, other on 3, and about 2X on 0. Money left the account once per event, not twice.

**RULED (supersedes round-131 ADDENDUM 2 and its row D2-S120):**
1. **"Dividend Paid from Cash" is an EXTERNAL outflow:** the dividend paid out of the account to the client. Its flow class carries the
   basis "measured cash move", which overrides the source taxonomy's Internal bucket for this description. The claim is `inferred`.
2. **"Income Paid" is INTERNAL:** the same payout booked a second time on the income side, with zero effect, so it is never counted.
3. **The income line ("Dividend to Cash" and the like) stays INCOME.** Read together: income in, then paid out. TWR counts the income as
   return and the payout as an external flow, so a dividend paid out does not read as a loss.
4. **Release criterion:** per event, exactly one leg is EXTERNAL and one INTERNAL, on 96 of 96. The cash-move agreement is printed as 75 of
   96. The 21 others (18 at about 0, 3 other) are read again with a cash move one trading day either side. If fewer than 90 of 96 agree on
   that wider read, the release stops and comes back here.
5. **One drain:** the contract's mapping rows for the two descriptions, the producer and any mirror land together. The contract's
   `s6_status` reads RULED_EXTERNAL_PAYOUT and cites this addendum.
