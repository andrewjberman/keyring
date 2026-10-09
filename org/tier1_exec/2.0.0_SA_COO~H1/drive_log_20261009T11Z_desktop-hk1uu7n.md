# /canonical-drive MDPF_SECHIST -- 2.0.0_SA_COO~H1, 2026-10-09 11Z (dell1)

## 11:14Z -- the 2026-10-09 07:00 ET scheduled pull ran; manifest read (S3 half of ledger leg L3)

`s3://opal-data-etfs/bbg/2026-10-08/run_manifest.json`, LastModified 2026-10-09 11:07:27Z, read at 11:14Z:
- `run_class` **scheduled**; `as_of` 2026-10-08; `generated_utc` 2026-10-09T11:07:23Z; universe 174.
- `history_backfill_error` **null**; `objects_failed` **[]** (7 written); `history_backfill_capped` [].
- `history_backfill`: 5 planned securities -- **HTHIY 257 rows**, **TOELF 257 rows** (2025-10-01..2026-10-08: the two newly held
  securities, one year deep per C-DEPTH), and PFDE 0, PFOE 0, 2602335D 0 (the same three zero-row keys as the 10-08 QA run).
- `history_backfill_budget` {estimate 931, limit 120000, spent_before 0, **recorded 514**} = 257 + 257. `recorded` non-null means
  `bbg_budget.record("backfill", ...)` returned true (`etf_daily_pull.py:606-609`): the day's ledger line was written --
  claim **inferred** (the producer's own return), not measured.

Ledger `mdpf-sechist-sh-t1-sitez-etf-daily-pull-20261007` L3 needs: manifest names the planned securities (YES), error null (YES),
leg exit 0 (manifest written with 0 failures; the exit code itself is site-Z-only), a backfill line in the day's ledger file
(inferred YES). NOT closed yet: the measured exit code and ledger line come from TO-READ-R2-L3 (0.7.0_AE_CloudOps~Z, window
11:45Z-13:30Z). If that read does not land by 13:30Z, L3 closes on the manifest with the ledger line marked inferred.

FWD-1 (TO-SH-t3): HTHIY and TOELF are the newly held securities the acceptance read grades on Positioning after the ~13:01Z
publish (the check requires the served file to post-date the manifest). Worker ~4 spawns then.
