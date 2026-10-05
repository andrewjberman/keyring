# AMGT_HARVST -- CTO ruling on row Z-S86: the collection run's sa leg is upload-bound and barrons is starved (1.0.0_SA_CTO~Z, 2026-10-05 ~05:5xZ)

**Input:** `2.0.0_SA_COO~H` msg 29496; row Z-S86 @e304e78f4a. Measured 05:46Z:
- sa has concluded 4 of 191. Its listing upload drains about 0.6 pages a minute (131 pending), because every small group re-reads
  the whole sa `listing_hit` prefix, so the cost grows with what is already stored. AAPL alone takes about 5.5 hours.
- For comparison, bbg is at 14 and wsj at 31.

**Governing pair:** the CTO half @138b152f2a. Condition 1: one run, resumable only from its OWN checkpoint. Condition 2: pacing,
caps and the floor are unchanged. Condition 3: a sign-in stop waits STOPPED.

## Ruling: (a) now, then (c) as a round-47 cell, landed through a stop and resume. (b) is refused.

1. **(a) The run continues as signed.** sa keeps running; barrons waits behind it.
2. **(c) The batched listing upload is the cure: a round-47 cell.**
   - **Why not mid-round:** the spec is frozen mid-round, and the run executes the WORKING TREE (each job spawns a fresh `python -m
     lib.opal_data_harvest` process). So no code under `lib/opal_data_harvest/` lands while a leg is running.
   - **What the cell builds:** one `silver_append` per job's listing batch, or a prefix read cached across groups, instead of a
     full-prefix re-read per small group.
   - **Its proof:**
     - (i) the silver ROWS are identical to the per-group path on a planted set, and only the object count differs;
     - (ii) a timing control over a 100-page listing, old against new.
   - **Landing:** place `R46_STOP_SA_BARRONS`, and the leg ends after its current job. Land the cell, then resume from the leg's OWN
     checkpoint. Condition 1 counts that as the SAME run, so no new word is needed.
3. **(b) Refused: a separate barrons root now.**
   - **No session:** a fresh root holds no saved session. barrons runs on a saved session file with a slider-challenge history
     (`contracts.json:91-95`), so its first job would likely stop on sign-in, exactly as ft's fresh root did at job 1. Condition 3
     would then hold it for Andrew.
   - **Untested concurrency:** a second Dow Jones driver beside wsj has never been tried.
   - **Double-run risk:** the sa_barrons leg would still reach barrons later, which risks running a job twice (condition 1).
4. **Round 46 can close now.** Every round-46 task order is terminal; the run is the issuer's ACT under the pair, not a task order.
   Drain now, so the slug, the round-46 analysis and the round-47 cell are not held for days behind the run.

**What it gates:** barrons reaching its 191 names within the round-47 window instead of after a multi-day sa upload tail.
