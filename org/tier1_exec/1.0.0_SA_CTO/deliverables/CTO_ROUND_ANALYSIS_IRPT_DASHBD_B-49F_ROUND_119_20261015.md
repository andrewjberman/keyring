# CTO ROUND-119 ANALYSIS -- IRPT_DASHBD workstream B-49F (~D2) -- the contract repair first, the Cottonwood key, and which price moved on 04-21 (2026-10-15 ~05:4xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `3.0.0_SA_CVO~IRPT`'s L10 slug for round 118 (msg 8094,
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/adjudications/ADJUDICATION_v82.md` @229f883be6): 6 of 6 live criteria PASS, MAY-CLOSE.
Also the issuer's packet `deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND118_B_DRAIN_END_20261015.md`. **No PRD addendum.** Issuer: `~D2`,
ONE issuance.

## 1. What round 118 established

- **Hop 1 exists LOCAL for 49 Financial.** `filled_report_values` writes rows at the firm's `address()` gold and round-trips the contract's
  document. The QA run covers 25 households and 29,294 rows, and the ending value ties for both probed households. The cloud prefix lists 0
  objects (control 570), so nothing is written yet.
- **2026-04-21 is VALUE-led:** 941 of 943 disagreed rows (1,009 of 1,022 over six dates) are an account value that moved while the holdings
  price return did not.
- **Cottonwood cannot yet form a household report:**
  - its household key is the Black Diamond account key;
  - its `account_return_daily` history is keyed by the Commonwealth custodian number, with 12 accounts at 06-22;
  - its gold `account_dim` is unwritten.
  The reader refused correctly.
- **The struck criterion DB118-3-AC3 is DEFERRED, NOT MET** (the CVO ran it: FAIL). The issuer may amend its own criteria. The amendment
  names its limb, and the outcome stays unmet in the record.

## 2. Rulings

1. **The contract repair goes FIRST:** contract 0.5.4. The `act.*` and `hold.net_gain_*` members print the same value-summary folds that
   DB-b-202 ruled. No table is scheduled or cloud-written until 0.5.4 lands. Today 527 rows are absent for a reason the contract created, not
   the data. **D2-S56 is its ARMED carrier, owner `~D2`,** until the module and the contract move together.
2. **Yes to the issuer's (a):** the Cottonwood input to `account_return_daily` from Black Diamond values and flows, keyed by the Black
   Diamond account key, by the one method (B-CW round-117 ruling 3, ask 8040).
3. **Yes to (b), a READ:** does the Black Diamond silver hold a map from the Commonwealth custodian number to the Black Diamond account key?
   - If yes, the history before 2026-06-23 joins through it, with the map's table and coverage recorded.
   - If no, Cottonwood's account history before 06-23 is reported `SOURCE_BREAK` at the seam, in words. It is not stitched by guesswork.
4. **The 04-21 next read: which holdings price moved,** or failed to. For the VALUE rows, name the securities whose price return on that day
   is flat or absent while the position value moved, and the price source of each. Counts by source and by security class; no client value.
   No repair this round.
5. **Cottonwood QA becomes a criterion again** in the round where (a), the gold `account_dim` and either branch of (b) have landed.
   `account_dim`'s pair is unsigned today: `~C2` cuts it with the B-CW apply. Until then it is carried as deferred-not-met.
6. **The `~F2` debt (reading `avs` `by_row`) gets a carrier:** `~D2` files ONE row with owner `2.0.0_SA_COO~F2`, naming the contract member
   and the reader line.
7. **Round numbers collide across workstreams** (114, 115, 118). The fix is a label, not a renumbering:
   - every order, packet, slug and analysis names its workstream (`B-49F`, `B-IN`, `B-CW`, `F-SHIP`) beside the round number;
   - `round-close-check` is always run with `--workstream`;
   - a number is never reused within one workstream.
   This seat's analyses already carry the tag.

## 3. The next round's cells (ONE issuance by `~D2`; each at most three mechanical criteria)

1. Contract 0.5.4 and the module, together (ruling 1).
2. The Cottonwood Black Diamond input to `account_return_daily`, keyed by the Black Diamond account key (ruling 2).
3. The Commonwealth-to-Black-Diamond key-map READ (ruling 3).
4. The 04-21 price READ (ruling 4).

The schedule and first cloud write of `filled_report_values` go to `0.7.0_AE_CloudOps~DB2` after cell 1 lands. `~P2`'s deploy legs wait on
that write.

-- 1.0.0_SA_CTO~DELL2
