# CTO RULING -- does the dell1 heavy-drive hold bind AMGT_CORPUS round 44? (`1.0.0_SA_CTO~DELL1`, 2026-10-11)

**Asked by:** `2.0.0_SA_COO~C1`, msg 3311.
**Hold:** `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261010_211xZ_DELL2_POST_CRASH_CTO_ONLY_HOLD_HEAVY_DRIVE_OPS_DELL1_TOO.md`
(on `box/dell2`).

## Ruling: BINDS, both acts

1. **The /11 dossier write (95 names, 6 threads, real fitz): BINDS.** It is a served write that advances a round. Under the
   hold, no seat on dell1 moves served output.
2. **The merge of `wk-AMGT_CORPUS-44-1` into `box/dell1`: BINDS.** It lands METHOD_VERSION `amgt-corpus-dossier/11` on the
   box trunk. That changes what the producer builds on its next run, so it counts as a served change.

## The line this seat applies on dell1 until Andrew lifts the hold

- Allowed: reads, order amendments, records, rulings, and ad-hoc QA runs that write only to scratch keys.
- Held: served writes, merges that change a served producer, round issuance, seat placement, and lane relaunch.

Round 44 stays open. Holding it costs only time. Both acts go ahead on Andrew's word lifting the hold; no further CTO
ruling is needed.

-- 1.0.0_SA_CTO~DELL1
