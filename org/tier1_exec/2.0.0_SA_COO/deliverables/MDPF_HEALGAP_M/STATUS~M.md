# MDPF_HEALGAP cell 1 -- the Cottonwood gold catch-up step -- STATUS (2.0.0_SA_COO~M)

Overwritten each tick. Register: `org/projects/MDPF_HEALGAP.json` (no tree home, by ruling). Authority:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md` batch 72 items 1-7 and batch 75
items 5-7. Trace: `org/tier1_exec/4.0.0_SA_CRO~X/deliverables/COTTONWOOD_ABSENT_POINT_TRACE_BRIEF_20261001.md`.

## Lease

NOT ARMED. `drive-mode.py arm MDPF_HEALGAP --surface data/mdpf/scripts/gold/mdpf_gold_consolidator.py` was REFUSED at
09:06Z: the live FAST lease MDPF_TAXSMA (seat `4.0.0_SA_CRO`) holds all of `data/mdpf`. Ruled (batch 75 items 5-6): the
catch-up is a NEW module built in this seat's worktree; `4.0.0_SA_CRO` re-arms MDPF_TAXSMA on its claimed files; the
consolidator's one call line is added by that seat at its next merge.

## Pins

- Module `data/mdpf/scripts/gold/mdpf_gold_catchup.py` and test `data/mdpf/tests/test_mdpf_gold_catchup.py`: on branch
  `coo-m-r30` (see the commit that carries this file). Code only. Nothing is deployed, nothing is written.

## What is built

- `plan()`: for each holdings date on the axis that no gold partition values, the build `--date <next trading day>
  --value-date <that date>`. Skips, each with its reason: no assignment partition for the next trading day (the seven
  days stay absent); a rewrite that would restate or drop an older date (no EARLIER partition values it); the newest
  date, which its own daily run values.
- `run()`: plans from live state through the slice's own readers and calls the existing builder. A failed build is
  recorded and does not raise. With `upload=False` every build is the builder's dry run.
- Test, 13 passed: the September replay (control: two dates dropped; with the step: none, built on the landing day),
  the August replay (three dates), the seven no-assignment days, the restate guard, a day with nothing to do
  (zero builder calls), and a failed build.

## One fact the half must carry

The gold partition key is the ASSIGNMENT date. Valuing holdings date V rewrites partition `date=<next trading day>`,
which today carries an older value date. Five existing partitions are rewritten (expected: 08-19, 08-21, 08-24, 09-24,
09-25). The older date stays served by the same partition as before, because the slice keeps the EARLIEST assignment
per value date and the guard requires that earlier partition to exist. Rollback is the prior object version per key.

## Next, in order

1. Read the ad-hoc QA run (live plan plus the builder's dry run per date; no write): the five figures for the half.
2. Count the readers of `gold/dim_model_portfolio` partitions by key (the slice reads by value date; the pair reads
   today's partition), so the half names who sees a rewritten partition.
3. The never-widen half: the five keys, their before and after value dates, the five figures, both outcomes on a day
   with nothing to catch up, the rollback per key. COO half, then the CTO's.
4. Hand-off to `4.0.0_SA_CRO` (file, not message): the one call line in `run_cottonwood_family` after the daily
   build and before the slice, and the module's entry in the MDPF gold Lambda's package list (the package is flat).
5. After both halves and the hookup: ledger entry, the apply, one trace per date to the served point.

## Parked

| Question | Owner | Un-parks when |
|---|---|---|
| The seven days with no assignment partition stay absent (ruling item 4) | Andrew (a Rebalancer re-pull is a vendor call) | his per-use word |
| MDPF_TAXSMA's lease surface is the whole directory | `4.0.0_SA_CRO` | it re-arms on its claimed files (batch 75 item 6) |
