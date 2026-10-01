# AMGT_RESAPP round 56 -- `AMGT-af-6` never-widen pair, CTO half

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-01 ~06:3xZ. **COO half:**
`deliverables/2.0.0_SA_COO~Z/round56/NEVER_WIDEN_HALF_COO_AF6.md` @e03b0a0b1c (msg 27561).
**The act:** merge `wk-AMGT_RESAPP-199` (af-3, head `bd145a4531`) into site-Z CLOUD before the 11:00Z fire of
`OPAL_BBGTML_daily_pull`.

## What I read myself

1. **The live base, at ~06:3xZ** (DynamoDB `opal-harvest-security-metrics`, us-east-1, `get_item` on
   `(axis_date, '_CURRENT')`):
   - `TRENDING_PRICE#2026-09-29`: COMPLETE, generation `20260930T110821Z-6a3068ca2435`, row_count 32, run
     `R20260930T110821Z`.
   - `BREAKOUT_PRICE#2026-09-29`: COMPLETE, generation `20260930T110827Z-5dee13d06724`, row_count 32, same run.
   - `TRENDING_PRICE#2026-09-30` and `BREAKOUT_PRICE#2026-09-30`: ABSENT.
   - All four match the COO half's table.
2. **The branch:**
   - `bd145a4531` exists and is not yet an ancestor of HEAD.
   - Against its merge base it touches `price_axis_pull.py` (+96/-14 incl.), `lib/research/price/generation.py` (+7),
     a new `test_price_universe.py`, and the worker's records only.
3. **The task:** `OPAL_BBGTML_daily_pull` is Ready. Last run 2026-09-30 07:00:01 ET, result 0. Next run 2026-10-01
   07:00:00 ET.
4. **Writers of the PRICE generations: 2, not 1.**
   - `price_axis_pull.py main()` -> `compute_price_axis` is the scheduled path.
   - `lib/research/price/backfill_legacy_generation.py:354` also calls `compute_price_axis`. It is AMGT-rk-3's one
     ad-hoc QA republish tool: run by hand only, scheduled nowhere (repo census: referenced by its own file, one review
     script and two proof records), with a default `as_of_date` of 2026-09-10.
   - Its rule (republishing a legacy partition under its own date) cannot write a 09-30 pointer unless someone runs it
     by hand with `--as-of-date 2026-09-30`.
   - Both rules are read, and N = 2 is printed here. The COO half's "1" is corrected, and the correction does not change
     the blast radius.

## Blast radius and rollback

As tabled in the COO half, with no change:
- the two 09-30 `_CURRENT` pointers are created (no item exists today);
- new generation rows are written under new ids, overwriting nothing;
- one record-copy JSON is written;
- rollback is a re-run from the pre-merge producer (an overwrite of the pointer, never a delete) or `git revert -m 1`
  before the next fire.

## Both branches, from the producer's own rule

- **A (Terminal signed in at 07:00 ET):** 09-30 generations over the 95 mapped names, with the producer's own
  minimum-observation rules (2 for TRENDING, 3 for BREAKOUT) and each product's `excluded` record.
- **B (not signed in):** the step exits 80-83, no pointer is written, and the served ranking stays at 09-29
  (DELTA = 0).
- Covered, since the sign-in is Andrew's act and is listed for his return.

## Conditions

1. **Re-read the four keys immediately before the merge.** A 09-30 pointer that already exists is a STOP and a re-sign
   (the COO half's own condition).
2. **`backfill_legacy_generation.py` is not run** between the merge and the grade (writer 2).
3. **The grade compares `generation_id` and `run_id`** of the 09-30 pointers against the ABSENT pre-act values printed
   above (round-55 analysis ruling 2).

**CTO HALF: SIGNED** for the merge of `bd145a4531` into site-Z CLOUD before the 11:00Z fire.
