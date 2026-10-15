# NEVER-WIDEN CO-SIGN -- COO HALF. Round 107, A4's history window: step 0 (30 days) to step 1 (90 days), a SITE-Z-REACHING one-integer change

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-15 ~22:5xZ. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND107_A4_WINDOW_STEP1_CTO_HALF.md`, signed BEFORE the act. Authority: CTO msgs 6265 and 6279
(steps 30 -> 90 -> 365 days, one completed good day per step, hold on the first vendor warning; 365 waits for the CTO's read of a measured 90-day);
Andrew-direct 2026-10-15 ~21:2xZ, "We should increase limits on all our pull surfaces" (record `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261015_21xxZ_RAISE_PULL_LIMITS_FLOOR_IS_NOT_A_CAP.md`).
Model: round 84's `II1_SITEZ` pair. Code half already landed at step 0: `AMGT-bn-5`, merge `077b203366`, which moves nothing.

## THE ACT

ONE commit on `box/dell1` that changes ONE integer in `integrations/bloomberg/research/price_axis_window.json`: `"step": 0` to `"step": 1`. It reaches CLOUD at the
integrator's next run and site Z's working tree at its next box-sync; the next run of the task's price leg after that sync pulls 90 days instead of 30.
**Preconditions, both read before the act:** (1) the DAY-0 READ: a completed price-leg fire at step 0 under the merged code shows the budget-ledger line (mode
`amgt-price-axis`, rows about 2,100), the same 30-day products as the day before, its daily series persisted, its exit code unchanged and no vendor warning;
(2) the act's commit lands on a trading day BEFORE that day's A4 fire, never after it (see the write-once note below).

## BLAST RADIUS -- what the act MAY move, and nothing else

1. **The Bloomberg draw of one fire:** `PX_LAST` daily for every covered name (94 on 2026-10-14), through the same `blp_client` path in the same chunks of 20: about 2,126
   returned observations a day today, about 6,400 at 90 days (measured on the stored 2026-10-14 series, 22.6 observations a name). No new field, security or channel.
2. **The stored history:** that day's daily object (name unchanged, `daily_30d.json`) carries 90 days of rows instead of 30. `load_history` merges per ticker by date with
   the LATER object winning, so rows inside the 90 days are refreshed with the vendor's current values (restatements, split adjustments). Nothing is deleted.
3. **The served 90- and 365-day TRENDING and BREAKOUT generations** built that day from the merged history: their values may move for a name whose stored price a restatement changes.
   The 30-day products are byte-identical by construction (test W5, the difference control, and the mutation control, in `test_price_axis_window.py`).
NO schema, table, grant, Lambda, schedule or task change.

## WRITER CENSUS -- who WRITES the moved properties (N = 2, both read)

- `integrations/bloomberg/research/price_axis_pull.py`: the only writer of the daily object and of the 30-day ranking rows; run as the PRICE LEG of the one scheduled task `OPAL_BBGTML_daily_pull` on site Z (`integrations/bloomberg/pipeline/scheduled_daily_pull.cmd` line 359; the task runs several legs and logs each).
- `integrations/bloomberg/research/price_history_pull.py`: the one-time year puller, hand-run, not scheduled; it landed `date=2026-10-02/year_pull.json` (95 names, 26,081 observations) once. It is unchanged by this act and is not run.

## EXPECTED OUTCOME -- both branches

- **No restatement in the 90 days for any name:** the refreshed rows are byte-equal to the stored ones; only the draw is larger; the 90/365 generations read the same.
- **A restatement exists:** the refreshed rows differ from the stored ones for those names, and the 90/365 generations move for them. This is the purpose of the widening.

## PER-KEY ROLLBACK

Set `step` back to 0 (one commit, the same path, the same sync); effect at the next fire. Rows already refreshed STAY (they are the vendor's current values). The daily object is
WRITE-ONCE per `as_of`: a second fire of the same `as_of` that carries a DIFFERENT series is REFUSED by `persist_series` (logged, never fatal; the 30-day leg's writes and exit codes are untouched),
so the act's commit must precede that day's fire, and a rollback commit after a day's fire takes effect the NEXT trading day.

## COUPLING NAMED, NOT DECIDED HERE

A4's spend is now recorded on the production budget ledger (mode `amgt-price-axis`). The history drawer (`MDPF_DEMQUE`) leaves room from what production uses, and the CTO's history-ceiling ramp (msg 6250, steps 11,716, 23,432, 29,290 cells a day) is Q1's. Step 1 adds about 4,250 observations a day to production. The CTO's half orders this against the ramp.

## STOP RULE

The first vendor warning, or a day an A4 leg misses its pull, sets `step` back to 0 and brings the finding to the CTO; no step is retried without a new read.

## NOT COVERED

Step 2 (365 days, the CTO's read of a measured 90-day); the schedule of `OPAL_BBGTML_daily_pull` and every other leg it runs; any DEMQUE ceiling or step; the year puller.

-- 2.0.0_SA_COO~R1
