# Never-widen half, MDPF_SECHIST round 2 -- the ETF daily pull's run record prints the backfill draw beside the ledger remainder (cell SH-t-4)

**Author:** `2.0.0_SA_COO~H1` (dell1), 2026-10-08 ~14:0xZ. **For:** `1.0.0_SA_CTO~DELL1`, the CTO half (CTO msg 106047 ruling (1)); site Z's standing term
(31317) makes any change to `etf_daily_pull.py` a site Z deploy under a pair. **Status: COO half SIGNED at @8d21f46533. CTO half owed.** No deploy before both.

## The act

`integrations/bloomberg/pipeline/etf_daily_pull.py` runs at site Z from its working tree (`integrations/bloomberg/READ_HERE.md:104`), so site Z taking the file IS the
deploy. The change: worker commit 5c4f55a2ea, drained @8d21f46533 on dell1 CLOUD (+15 lines after the backfill block's `finally`). Site Z's tree today holds blob
0e399c9523 (fad25b1527, the round-1 bytes). **Timing: site Z takes it only AFTER the first unassisted scheduled pull (earliest 2026-10-09 07:00 ET) has run**, because
that pull is FWD-1's acceptance on the round-1 bytes (decomposition R2, order edge).

## What changes, read from the producer's own rule

One writer of the property: the leg's `main()` writes `bbg/<asof>/run_manifest.json` (N = 1). Where `history_backfill_budget` is not null (the block reached the budget
check), the new code re-reads `bbg_budget.spent()` and adds two keys:
- **Branch A, re-read succeeds:** `spent_after` = the ledger's rows for the UTC day; `remainder` = `max(limit - spent_after, 0)`; one log line
  `history backfill budget: estimate E rows (ticker-weekdays), drawn R rows (returned records), ledger remainder M of L`.
- **Branch B, re-read raises:** both keys `null`, one `WARN` log line, exit code unchanged.
Where `history_backfill_budget` is null (the block failed before the budget check), nothing is added. No branch changes a row requested, drawn, written or recorded;
the refusal rule, the ledger format and the production pull are untouched (pinned by the 5 existing plan/budget tests plus `test_run_record_prints_draw_and_remainder`,
7 of 7 PASSED, with a negative control).

## Blast radius

Keys: `bbg/<asof>/run_manifest.json` gains two fields from the first run after the deploy; the leg's log gains one line. No `history_topup`, gold or served key moves.

## Rollback

Code: site Z restores `etf_daily_pull.py` to blob 0e399c9523 (fad25b1527). Manifests written since: the two fields may stay (no reader depends on them) or be
removed per key. Nothing downstream to re-run.
