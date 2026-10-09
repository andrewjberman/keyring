# Never-widen half, MDPF_SECHIST round 3 -- the ETF daily pull gains the total-return level field and the gap re-request (cell SH-t-8)

**Author:** `2.0.0_SA_COO~H1` (dell1), 2026-10-09 ~14:4xZ. **For:** `1.0.0_SA_CTO~Z` (the site-Z producer half; round-2 analysis item 4 and
AMENDMENT 2 conditions) and `1.0.0_SA_CTO~DELL1`. **Status: COO half DRAFTED, NOT SIGNED.** It is signed only after the field is confirmed:
request `MDPF_SECHIST-SHT8-TR-FIELD-CONFIRM-20261009` (@d22b6dfdb5, quote frozen @df823bf77a by `2.0.0_SA_COO~Q1`) returns a non-null
`TOT_RETURN_INDEX_GROSS_DVDS` for SALXX. No deploy happens before both halves are signed.

## The act

`integrations/bloomberg/pipeline/etf_daily_pull.py` runs at site Z FROM ITS WORKING TREE (`integrations/bloomberg/READ_HERE.md:104`). Today
the tree holds blob `73735f44d6b8e4a17c9ebf241a62b9bf4a334379` (SH-t-4 taken by the 12:00Z restore; ledger
`mdpf-sechist-sh-t4-sitez-run-record-20261009`). The act: site Z's working tree takes the file at blob
`055945a348d6ae11d8b1de65c75725324a6c6742` (SH-t-8, merged on dell1 @89fe7615bf; worker commit a154008d05), done by site Z's owner under a
change-management ledger entry the actor opens, OUTSIDE 10:30Z-12:00Z. Andrew lifted no-modify for THIS file only
(`ANDREW_DIRECT_20261008_230xZ_SITEZ_AND_DELL2_OPEN_CALLS_ANSWERED.md`); nothing else under `integrations/bloomberg/pipeline/` moves.

## What changes, read from the producer's own rules (@89fe7615bf)

1. `HISTORY_FIELDS = ["PX_LAST", "DAY_TO_DAY_TOT_RETURN_GROSS_DVDS", TOTAL_RETURN_LEVEL_FIELD]` with `TOTAL_RETURN_LEVEL_FIELD =
   "TOT_RETURN_INDEX_GROSS_DVDS"`. The production history request, the depth backfill and the gap fill all ask for it; the fund-daily
   request is unchanged. Each history row gains one column of that name.
2. Gap re-request: the pull reads the newest gap record (`etf_history_gap_record.record_address`, lookback 10 days) and requests each
   listed day per ticker as weekday-contiguous windows, after the depth backfill, cut to `limit - used - estimate` of the `bbg_budget`
   plan (C-BUDGET) and deferred to the next run when short. The manifest gains `history_gap_fill {requested, deferred, estimate, rows}`.
   **Today no gap record exists** (no caller writes one -- round 4's first item), so branch (b) below is what runs.

## Both branches

- (a) A gap record exists: extra history cells = the listed days kept under the budget; rows land in `history_topup`; days over the
  budget are deferred, never forced; a read failure of the record is a WARN plus a manifest field and the pull carries on.
- (b) No gap record (today): `history_gap_fill.requested = 0`; the only change is the third field on each history row.
- Field rejected by the Terminal (the risk the confirmation read removes): `blp_client.historical_data` with
  `on_response_error="ignore"` returns rows without the column; the pull does not fail; FWD-9's money-market windows stay blank.

## Writers counted

`s3://opal-data-etfs/bbg/<asof>/history_topup.{csv,parquet}` and `run_manifest.json`: N = 1 rule (the leg's `main()`). Gold reads
`history_topup.parquet` whole (`etf_positioning_gold.py:764`, `_read_parquet`); a new column is ignored by today's gold, which selects
`PX_LAST` / `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS` by name. The money-market rule that reads the new column is SH-t-7 (gold, AWS Lambda
`etf-positioning-producer`), a SEPARATE later deploy, ordered AFTER this one so SALXX / FXFXX never read blank in between.

## Draw (the MDPF_DEMQUE quote, owed before the first run)

Per run: + one history cell per history row (the 2026-10-09 run: 687 top-up rows + 514 backfill rows = about 1,201 extra cells), plus any
gap re-request rows (0 today). Ledgered through `bbg_budget` as today.

## Blast radius

Keys the act may touch, from the first run after it: `bbg/<asof>/history_topup.{csv,parquet}` (one more column; more rows only when a gap
record exists) and `bbg/<asof>/run_manifest.json` (one new field). No served value moves until SH-t-7's gold deploy reads the column.
No historical partition is rewritten.

## Rollback (opal-data-etfs has no versioning)

- code: site Z restores `etf_daily_pull.py` to blob `73735f44d6` in its working tree;
- `history_topup` for each run since: drop the `TOT_RETURN_INDEX_GROSS_DVDS` column and any rows whose date lies outside that run's
  production window and was requested by the gap fill (manifest `history_gap_fill`);
- `run_manifest.json`: remove `history_gap_fill`;
- the `bbg_budget` ledger keeps its lines (rows were drawn).

## Acceptance (the first scheduled run after the take)

Manifest `run_class` scheduled, exit 0; `history_topup` carries a non-null `TOT_RETURN_INDEX_GROSS_DVDS` for SALXX on the as-of;
`history_gap_fill` present.

## COO half -- NOT YET SIGNED

Signed by `2.0.0_SA_COO~H1` when the confirmation read returns a value. Already read: SH3-t8-AC1 `PULL-TESTS-OK passed=2/2` and the whole test
file 11 of 11 at the drain (@89fe7615bf).

## HELD (2.0.0_SA_COO~H1, 2026-10-09 ~15:2xZ) -- the field read came back EMPTY

The confirmation read (`MDPF_SECHIST-SHT8-TR-FIELD-CONFIRM-20261009`) returned an EMPTY `TOT_RETURN_INDEX_GROSS_DVDS` for SALXX on
2026-10-08, with no vendor error (0.0.0_AB_MSTR~DELL1 msg 2644). This half is NOT signed. Deploying SH-t-8 as merged would add about
1,200 history cells a run for an empty column, and SH-t-7's money-market rule would then read SALXX / FXFXX blank. FWD-9's route is
asked of the CTO: another level field (confirmed by one more queued cell first), or route 2b (re-request held-null days; amends ratified
C-MMF, needs Andrew's word). The gap re-request half of SH-t-8 has no gap record to read until round 4's producer exists, so nothing is
lost by holding the whole take.

## UPDATE (~15:2xZ) -- the field is valid; history read pending; the CTO's condition

- Q1 msg 2649: a reference read returned `TOT_RETURN_INDEX_GROSS_DVDS` = 1.000389 for SALXX (negative control `FUND_TOTAL_RETURN_1D`
  INVALID_FIELD). The mnemonic is right; only the single-day HISTORY for 2026-10-08 was empty.
- Next: request `MDPF_SECHIST-SHT8-TR-FIELD-HISTORY-20261009` (@e98d4837ad): SALXX + FXFXX, 2026-09-28..2026-10-07, 16 cells.
- CTO condition (msg 2653): if settled days carry values but the same-day read stays empty, every run's newest money-market day lands
  empty, and SH-t-7 would blank SALXX/FXFXX daily. The pair must state whether the newest day is empty; if it is, the gap-record
  PRODUCER (round 4's first item) lands before or with this deploy, so the re-request fills the day.
- Fallbacks if the history read is empty (Q1 msg 2654, CRO msg 2655): `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS` re-read late (FXFXX has 25
  stored Bloomberg days, MDPF_DEMQUE DQ-t-21); `TOT_RETURN_INDEX_NET_DVDS` after one reference read; a 7-day-yield field found by a
  Terminal FLDS lookup, never a guessed name.

## SUPERSEDED IN PART by PRD v0.3 (2.0.0_SA_COO~H1, 2026-10-09 ~16:3xZ) -- the take carries round 5's repair, not the level field

- The history read (16 of 16 values exactly 1) ruled route 2a out; PRD v0.3 C-MMF (CTO @847e1e265e, CVO sign @cc57bafcdb) takes route 2b.
  The blob `055945a348` above is NOT the take. The take is the file after round 5's repair cell SH-t-19 (staged @ffd76f8b9d): `HISTORY_FIELDS`
  back to `["PX_LAST", "DAY_TO_DAY_TOT_RETURN_GROSS_DVDS"]`, gap re-request kept. The blob is re-read at that drain and written here.
- Sections "What changes" item 1, branch "Field rejected", Draw (about 1,200 extra cells) and Rollback's column drop fall away: no new
  column. Draw = gap re-request rows only, quoted through MDPF_DEMQUE before the first run.
- Order (CTO msg 2778): the gap-record producer (SH-t-15, gold) must write a record for the re-request to read; until gold is deployed,
  branch (b) runs (requested = 0). Pull first, gold second still holds: the pull change alone moves no served value.
- Acceptance becomes: manifest scheduled, exit 0, `history_gap_fill` present; FWD-9 is graded on gold's served page (CTO msg 2791).

## THE TAKE, re-read at SH-t-19's drain (2.0.0_SA_COO~H1, 2026-10-09 ~16:5xZ) -- COO half SIGNED

- **The act:** site Z's working tree takes `integrations/bloomberg/pipeline/etf_daily_pull.py` at blob
  `627deda306287d4de3dc7b3ac29e6e2abef44018` (box/dell1 @522aa18dc2, SH-t-19 drained), replacing `73735f44d6` (SH-t-4). Done by site Z's
  owner under a change-management ledger entry it opens, OUTSIDE 10:30Z-12:00Z. Nothing else under `integrations/bloomberg/pipeline/` moves.
- **What changes vs 73735f44d6, read from the producer's own rules @522aa18dc2:** (1) the SH-t-8 gap re-request (unchanged from the
  sections above; `HISTORY_FIELDS` stays the two fields it has today -- no new column); (2) the SH-t-19 depth bound: tickers listed in the
  previous manifest's `history_backfill_exhausted` are not planned; this run writes the updated list into its manifest.
- **Writers counted:** `bbg/<asof>/history_topup.{csv,parquet}` and `run_manifest.json`: N = 1 rule (`main()`). New manifest fields:
  `history_gap_fill`, `history_backfill_exhausted`.
- **Both branches:** (a) a gap record exists (only after gold is deployed with SH-t-15): listed days re-requested under the budget, rows
  land in `history_topup`, overflow deferred; (b) no gap record (until gold): `history_gap_fill.requested = 0`. Depth: a ticker with zero
  backfill rows and a stored date is skipped from the next run on; every other ticker plans exactly as today.
- **Draw:** at most today's draw (the depth bound only removes zero-row requests); gap rows 0 until gold is deployed, then quoted through
  MDPF_DEMQUE before the first run that carries them.
- **Blast radius:** the two keys above, from the first run after the take. No served value moves (gold reads history columns by name).
  No historical partition rewritten.
- **Rollback:** site Z restores blob `73735f44d6`; remove `history_gap_fill` / `history_backfill_exhausted` from manifests written since;
  drop gap-fill rows outside each run's production window; `bbg_budget` lines stay.
- **Acceptance (first scheduled run after the take):** manifest `run_class` scheduled, exit 0, both new fields present.
- **Read at the drain:** SH5-t19-AC1 `MMFR-TESTS-OK 3/3`, AC2 `PULLR-TESTS-OK 2/2`, AC3 `GOLD-SUITES-OK files=3`; `test_etf_daily_pull_history_plan.py`
  12/12 (issuer re-run @522aa18dc2, FORCE_COLOR=3 shell). Row `MDPF_SECHIST-D1-S1` (depth bound never expires) ruled INERT for this take.

**COO half: SIGNED by 2.0.0_SA_COO~H1, 2026-10-09 ~16:5xZ, at blob 627deda306.** Owed: the CTO half (`1.0.0_SA_CTO~DELL1`; site-Z producer
half `1.0.0_SA_CTO~Z`), then a site-Z task order via 0.0.0_AB_MSTR~DELL1. Gold follows the take (its own pair).

## RE-SIGNED at blob 75342a6958 (2.0.0_SA_COO~H1, 2026-10-09 ~17:0xZ) -- CTO condition 1 built

- The take is now blob `75342a695857a86e3a4f0c651d5febc6d66b98db` (box/dell1 @09b6a7d580: TO-SH-t19 AMENDMENT 1 drained). The only delta
  from `627deda306`: `history_backfill_exhausted` is a mapping ticker -> entry as-of date (an old-list entry reads null), and every run
  logs `history backfill exhausted: <ticker> since <date>` per entry plus `history backfill exhausted count: <n>` (CTO half condition 1,
  msg 2848). Same writer, same keys, same blast radius and rollback as above.
- Read at the drain (FORCE_COLOR=3): AC1 `MMFR-TESTS-OK 3/3`, AC2 `PULLR-TESTS-OK 3/3` (incl. `test_exhausted_list_printed_with_entry_date`),
  pull test file 13/13, gold suites 3/3.
- Acceptance adds: the run log carries the count line.

**COO half: RE-SIGNED by 2.0.0_SA_COO~H1 at blob 75342a6958.** The CTO half (msg 2848) named this condition; site Z's producer half
(`1.0.0_SA_CTO~Z`) is asked at this blob.
