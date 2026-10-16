# Never-widen half (COO), MDPF_SECHIST -- Andrew-direct da0c: the Positioning pull's backfill cap, A2 `BACKFILL_CAP` 50 to 62

**Author:** `2.0.0_SA_COO~H1` (dell1), 2026-10-15 ~23:5xZ. **For:** `1.0.0_SA_CTO~DELL1` (the CTO half, which CTO msg 6323 says is one line). **Status: COO half SIGNED for the act below**, a direct act off the pair (minted order, no decomposition cell).
Basis: Andrew-direct da0c, record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_233xZ_DA0C_POSITIONING_PULL_SLIGHT_INCREASE.md` ("Positioning ETF pull can have slight increase"); CTO msgs 6322, 6323 (the knob, A5 has none); routed by `2.0.0_SA_COO~Q1` msg 6324. The 2026-09-30 hold stands for everything else: fields, securities, schedule, code path, and the shared `data/etfs/scripts/rivalfunds/bbg_budget.json`.

## integrations/bloomberg/pipeline/etf_daily_pull.py -- line 62, BACKFILL_CAP 50 to 62

**The act.** ONE line: `BACKFILL_CAP = 50` becomes `BACKFILL_CAP = 62` (+24%, inside the CTO's one step of at most +25%). No other byte of any file moves (the commit's diff is 1 insertion, 1 deletion, one path). A worker makes the commit on `box/dell1`; box-sync carries it to `CLOUD` and to site Z's working tree, where the daily 07:00 ET pull reads it.

**What reads the constant (counted from the code, `comp-find` denominator 18 hits / 100,234 files; first-party source hits 2):**
- `history_backfill_plan(..., cap=BACKFILL_CAP)`, the default bound at definition: called at L513 (the read-only `HISTORY-PLAN` entry, writes nothing) and at L713 (the run, no `cap` argument). N = 1 rule; plan order is sorted ticker, and the overflow is returned as `capped` for the next run.
- `data/mdpf/scripts/demque/reserve_estimate.py` L256 reads the literal from source into a note string only (a reader, no write).
- Tests: `test_etf_daily_pull_history_plan.py` passes `cap=50` explicitly, so none moves.

## Writers counted

The property is "which names a run asks the vendor for history". Writers: N = 1, the run block of `etf_daily_pull.py` (L700 on), which writes `bbg/<as_of>/history_topup.*` and the manifest fields `history_backfill`, `history_backfill_capped`, `history_backfill_exhausted`, `history_backfill_budget`. One rule read: `history_backfill_plan` (L246-276). The block is isolated from the production pull: any failure there is a WARN and a manifest field, never the leg's exit code (L690-691).

## Both branches (read from the plan's own rule, not predicted from the input)

- **needing_count <= 50:** `needing[:62]` equals `needing[:50]`; the run is byte-identical to today's. **Measured now:** the 2026-10-14 scheduled manifest planned 1 name (`2602335D`), `history_backfill_capped` `[]`, `history_backfill_exhausted` `{PFDE, PFOE}` (excluded from needing by rule); universe 172. The cap is NOT binding: **the 62 changes nothing until more than 50 names need depth.**
- **50 < needing_count <= 62:** the extra names are asked this run instead of next; at most 12 more names, each at most about 267 ticker-weekdays (a full-year window: the 10-14 run's `estimate` 276 is `2602335D`'s backfill plus the gap fill's 9): <= 3,204 ticker-weekdays a run.
- **needing_count > 62:** 62 planned, the rest `capped` to the next run, as it is today at 50.
- **The ledger arm (every branch):** the run prices its estimate against the one Bloomberg ledger before any request. `limit` = `daily_ceiling_rows` 150,000 - `production_reserve_rows` 30,000 = 120,000; the 10-14 run read `spent_before` 0, recorded 9, remainder 119,991. If `spent + estimate > limit` the block raises and **nothing is fetched** (L740-743). The worst branch above is about 2.7% of the limit (3,204 of 120,000).

## Blast radius

From the first scheduled run after site Z carries the commit: `bbg/<as_of>/history_topup.{csv,parquet}` and `run_manifest.json` (additive rows and fields), the ledger's daily draw (bounded as above), and the depth gold reads from the bronze history (a name that gains a year of history gains its served 1Y window; additive). Not touched: the production pull, fields, securities, schedule, `bbg_budget.json`, any IAM, any served key's schema. A5 has no knob and does not move.

## Rollback

A new commit on `box/sitez` restoring `BACKFILL_CAP = 50` (never a rebase), before the next 07:00 ET run. Rows a run already landed stay (additive bronze, per-day keys that are never rewritten; no S3 delete). **One state outlives a rollback:** a newly planned name that returns zero rows older than its earliest stored date joins `history_backfill_exhausted` and stops being requested; that is the plan's rule and a true fact about the name, so it is not undone.

## Timing, and the shared file

Takes effect on the first scheduled 07:00 ET pull after site Z carries the commit. Per CTO msg 6304 and `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/2.0.0_SA_COO~Q1/LIMIT_STEP_DAYS.md`: no other limit step on the same day (A4's earliest is the first trading day after Sat 2026-10-17); `2.0.0_SA_COO~Q1`'s ramp starts no earlier than Sat 2026-10-24. This seat reads that file at the landing, takes a day no row holds, and appends its row with the commit. Target: Tue 2026-10-20.

## Acceptance (the first scheduled run on it, read by this seat)

- Manifest `run_class` scheduled, `objects_failed` `[]`, the pull's exit 0.
- `history_backfill_budget` present with `spent_before + estimate <= 120000`; `len(history_backfill) <= 62`; `history_backfill_capped` equals `needing_count - 62` names or `[]`.
- Nothing in the manifest or served page differs in schema from the prior day's.
