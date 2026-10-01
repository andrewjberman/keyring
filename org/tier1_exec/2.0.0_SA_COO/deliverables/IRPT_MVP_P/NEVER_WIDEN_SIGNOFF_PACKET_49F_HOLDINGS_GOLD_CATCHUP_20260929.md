# Never-widen sign-off packet -- ONE catch-up fire of the 49 Financial holdings producer for trading day 2026-09-29

Author `2.0.0_SA_COO~P`, 2026-10-01 ~06:5xZ. Ledger `irpt-holdings-gold-49f-catchup-20260929` (OPEN, two legs). Ordered by
`ROUND_ANALYSIS.sweep5.md` @a50d8207bc section 2 item 3 ("one fire for 2026-09-29 through the producer's own path ... both halves
naming that one key and that manual state") and CTO rulings batch 63 queue item 3. Halves owed: `1.0.0_SA_CTO` and
`2.0.0_SA_COO~P` (signed below). No CRO half: no page text changes.

## 1. The act, exactly

ONE `lambda invoke` of `irpt-holdings-performance-lambda` (CodeSha256 `gLRGHIyi6u6NEibnWwOlf80hq1tH8GlXVWRhmf81xwE=`, unchanged since
2026-09-29T14:42:51Z; no code moves) with the event `{"date": "2026-09-29", "source": "schwab_08335338"}`. The producer accepts an
as-of date: `handler.py` `_target_day` returns `event['date']` when the caller names one.

Write set, three literal keys in `opal-data-49financial` (addresses from `lib/opal_naming.address()`), none of which exists today
(`list-objects-v2` on both prefixes for `date=2026-09-29`: 0 objects, read 06:51Z and again after the dry run):

- `irpt/49financial/gold/holdings_performance_daily/date=2026-09-29/data.parquet`
- `irpt/49financial/gold/holdings_performance_manifest/date=2026-09-29/data.parquet`
- `irpt/49financial/gold/holdings_performance_manifest/date=2026-09-29/manifest.json`

## 2. Why the day is missing, measured

- The newest served partition is `date=2026-09-28` (written 2026-09-29T14:45:04Z). `date=2026-09-29` is absent in both tables.
- The Schwab silver for 2026-09-29 exists in both tables the producer reads (`dim_position` and `dim_balance`
  `date=2026-09-29/data.parquet`, LastModified 2026-09-30T21:46:40Z): it landed twelve hours after the feed's usual hour and ten
  hours after the 09-30 scheduled fire, which refused ABSENT. The cause of the late landing stays with `TO-IB-pr-274` (parked).
- The schedule computes one day per fire, `prev_trading_day(expected_last_trading_day(now))`, and never revisits a missed day. The
  2026-10-01 11:30Z fire computes 2026-09-30, a different key. Without this act 2026-09-29 stays absent.

## 3. Both branches, read from the producer's own rule (`holdings_performance.py` `compute_day`, `emit_day`, `main`)

| branch | what the producer does | what is written |
|---|---|---|
| A: the day-t and t-1 partitions it needs are present | computes every account, writes the daily parquet, then the manifest parquet, then `manifest.json`, returns rc 0 | the three keys of section 1 |
| B: a needed partition is absent | `compute_day` returns `ABSENT: ...`, the day is skipped, rc 1 (the Lambda reports `ok: false`) | nothing |

Which branch, MEASURED and not predicted: the same event with `"dry_run": true` ran at 06:53:34Z (rc 0, 8.4 s, nothing written):
`rows=7559 prior_holdings=6349 computable=6346 not_computable=3 complete=True`, census `OK 6663, NO-PRIOR-HOLDINGS 887,
NON-POSITIVE-BASE 6, ALL-HOLDINGS-EXCLUDED 3`. It sits beside the three newest served partitions (2026-09-24, 09-25, 09-28: rows 7,534,
7,540, 7,548; OK 6,639, 6,650, 6,654; NO-PRIOR-HOLDINGS 887, 881, 885; NON-POSITIVE-BASE 6, 6, 6; ALL-HOLDINGS-EXCLUDED 2, 3, 3). So
the wet run takes branch A with those counts; a different count is a stop (condition 2).

The three writes are sequential, not atomic: a failure after the first leaves a daily partition without its manifest. The readback
of condition 2 names that state and the remedy is the same invoke again (the writes are idempotent overwrites of the same keys).

## 4. Writers of the named keys, and the manual state

Three trigger paths, ONE rule (`holdings_performance.py main`): the 07:30 America/New_York schedule (source `schwab_08335338`; never
targets a past day), this manual event with `date`, and the producer's command line run by a DS seat with `--upload` (the path that
wrote `date=2026-09-21..25` on 2026-09-29T09:25Z). The manual path is the `--date` override this packet covers: it runs the scheduled
producer off its own clock, for the one date named, once. No other date is fired under this packet.

## 5. Blast radius

Readers of the holdings gold for 49 Financial: `irpt-performance-adapter` (the 49 Financial performance report since the r3 switch;
101 fresh serves read it between 2026-09-29T16:40Z and 2026-10-01T06:47Z) and the IRPT_DASHBD adapter's guard (not served). After the
write, a report whose window reaches 2026-09-29 reads that day's 6,663 OK returns; before it the day is absent. NOT measured: what the
served report shows today for a window that crosses the absent day; the after-read of condition 3 reads the adapter's log instead.

## 6. Rollback

The three keys do not exist today, so undoing the act is removing three objects. The bucket has versioning Enabled (read 06:55Z),
so a removal writes delete markers and loses no bytes; it is still an S3 delete, which this seat does not perform without Andrew's
confirmation. Containment that needs no delete: a wrong partition is corrected by re-firing the same event after the cause is fixed
(the keys are overwritten).

## 7. Conditions

1. One invoke, the event of section 1, nothing else. `FunctionError` absent and `{"date": "2026-09-29", "rc": 0, "ok": true}`.
2. Readback: the three keys listed with size and LastModified; the daily parquet's row count is 7,559 and its status census equals
   the dry run's; its schema equals `date=2026-09-28`'s; `manifest.json` reads `complete: true`. Any difference stops and is reported.
3. After-read: the adapter's log for the hour after the write shows no new `HoldingsGoldRefused` outcome that names 2026-09-29.
4. The ledger closes on 2 and 3, never on the invoke.

## COO half -- 2.0.0_SA_COO~P

SIGNED, 2026-10-01 ~06:5xZ, on this packet's bytes at the commit that carries it. The write set is three literal keys; both branches
are read from the producer's rule and the taken branch is measured by the dry run.

## CTO half -- 1.0.0_SA_CTO

SIGNED, 2026-10-01 07:0xZ, bound to this packet's pre-signature blob `654fa59653` (@5b8b8cf4fc). Signed on the write set of three
literal keys, both branches of section 3, the manual-date state of section 4 and the containment of section 6.

**Measured by this seat at signing (07:08Z):**

- The two target prefixes for `date=2026-09-29` hold 0 objects each; the positive control `date=2026-09-28` holds 1 (daily) and 2
  (manifest), which is the three-key shape the act writes.
- The silver the producer reads for 2026-09-29 is present in both tables: `dim_position` and `dim_balance`
  `date=2026-09-29/data.parquet`, LastModified 2026-09-30T21:46:40Z.
- The function's live `CodeSha256` is `gLRGHIyi6u6NEibnWwOlf80hq1tH8GlXVWRhmf81xwE=`, last modified 2026-09-29T14:42:51Z, as stated.
- The date input was read by this seat earlier (`handler.py:52-59`, sweep-5 analysis section 2 item 3). NOT re-run here: the dry
  run. Its counts are taken from the packet.

**Conditions, in addition to section 7's four (each a stop):**

5. **No S3 delete under this half.** Section 6 is accepted as written: a wrong partition is corrected by re-firing after the cause
   is fixed; removing the three keys needs Andrew's confirmation and is not asked here.
6. **The fire runs before or after the 2026-10-01 11:30Z scheduled fire, never while it runs.** The two write different keys, but one
   producer process per window keeps the readback of condition 2 unambiguous. The UTC time of the invoke goes in the ledger.
7. Condition 2's row count and census are compared with the dry run's numbers in section 3 (7,559 rows; OK 6,663); a difference
   stops the ledger open and comes back here before any re-fire.
8. This half covers the ONE date named. A second missed day is a second packet.
