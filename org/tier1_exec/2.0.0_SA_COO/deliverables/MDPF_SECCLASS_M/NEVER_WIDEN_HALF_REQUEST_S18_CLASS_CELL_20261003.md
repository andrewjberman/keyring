# Never-widen half, MDPF_SECCLASS-S18 class cell -- deploy A_03's liveness fix, reset C_06 to 09-30, one QA run, re-enable the fires (CTO batches 220, 221)

**Author:** `2.0.0_SA_COO~M`, 2026-10-03 09:4xZ. **For:** `1.0.0_SA_CTO` (batch 221: "I sign on receipt").
**Status: COO half SIGNED below; CTO half asked; NOT RUN. Deadline: before Monday 2026-10-05 04:00Z (else report by Sunday 18:00Z).**

## The change, and one departure from batch 220's text

Code on CLOUD (LOCAL): 564d5bede9, 5df4c735fa, 13d0277249 (drains 4f1c1b2b59, dafb13cfb2, 8c9cf4e905); `tests/test_a03_s18_liveness.py`
8 passed, BD gold suite 76. HEAD `A_03.positions_cube.py` md5 4baf5de3f9b5f3e45b7659059d38ca3a. Deployed
`code/gold/A_03.positions_cube.py` VersionId 1MYNHoSQGh6fgPL6dCQxEJYwN9WiOOYJ (2026-06-24, md5 6bce3508 = CLOUD before the cell).

**DEPARTURE.** Batch 220 says "A_03 confirms open accounts from the dimension". Measured, that is not deployable: the dimension
marks 10,702 of 11,071 accounts open, and treating each as live uncaps 4,095 accounts. 3,568 of them have a last trade before
09-30, some back to 2020, which would add ~3.55M account-days of phantom history; the 1,220 that have a readable timeseries last
held $223.9M (`R9_CHECKS/S18_CELL_DELTA_CENSUS_20261003.json`; row S20). The cell as built is scoped. An account carries forward
when the allocation file confirms it, or when it is OPEN in the dimension AND held a position on the REFERENCE day (the newest
cube partition strictly before the new frontier). Signing this half signs the scoping.

## The act, by leg

| leg | what |
|---|---|
| P | precondition reads: runner i-01003b035d2988dfb stopped; `bd-gold-nightly-fallback` and `bd-canonical-prices-daily` DISABLED; deployed A_03 md5 6bce3508; **silver max trade date = 2026-10-01** (a later trade date makes the reference day the S18 run's 10-01 partition, which lacks the 335: STOP and return here) |
| G | safe-deploy `data/black_diamond/scripts/gold/A_03.positions_cube.py` to opal-data-bd `code/gold/`; prior VersionId recorded; `comp-pipescript deployed` MATCH |
| W | C_06 watermarks to 09-30 by copy-object (metadata COPY): `gold/meta/client_timeseries_watermark.json` <- aESAiTiS5l.. and `gold/client_timeseries/_watermark.json` <- qr2SMNeSj6.. (both data_as_of 2026-09-30, 2026-10-02 15:53:08Z); read back. A_03's own gate watermark is NOT touched: its fingerprint carries the code bytes, so the deploy alone forces a rebuild. |
| Q | ONE ad hoc QA run, `bd-gold-trigger {mode: incremental}`; run log read |
| V | acceptance reads (Branch A below) |
| R | re-enable both rules, read back ENABLED (closes leg R of `secclass-s18-restore-0930-m-20261003` too) |

## Writers, counted

Property 1, which accounts a cube partition holds. Its writers are five rules, all in A_03; each was read.
1. The end-date cap (`_compute_account_end_dates` over `liveness_set`). CHANGED.
2. The phantom filter (allocation AUA >= $100 plus RPS-mapped). Unchanged; it applies only when the allocation file for the
   max trade date exists, and there is none for 10-01.
3. The matured-bond filter (asset level, by partition year). Unchanged.
4. Realized-sell and synthetic-buy injection (Step 2a). Unchanged.
5. The backstop (Step 3c). NEW; it removes nothing and refuses.

Property 2, the served as_of. Its writers are C_06 (its watermark and the mix timeseries) and D_04 (platinum). N = 7 rules,
three scripts, one chain.

## Expected outcome, both branches (the producer's rule over today's inputs, read-only)

Census at 09:0xZ: `R9_CHECKS/S18_SCOPED_CENSUS_20261003.json` and `s18_scoped_census.py`; limit: no transaction_id de-dup.
- Inputs: max trade date 10-01; no allocation file for 10-01 (weekly; latest 09-25); dimension open 10,702.
- Reference day 09-30, with 6,836 accounts held. Carry set (dimension-open AND held): 6,710.

**Branch A, frontier whole (the census's reading).**
- The rule uncaps 502 accounts against the old rule, 0 of them with a last trade before 09-30. Partitions up to 09-30 rebuild
  with the served cube's account set: history DELTA = 0 by the rule.
- 10-01 delta for the 335: 332 reappear on 10-01 holding their 09-30 units. Their 09-30 value is $78,634,159.20 for the 335,
  less the 3 below. The other 3 traded out on 10-01: z0818919951, z0821124151 and z0822808251, daily-feed accounts selling
  residual units (0.39 stable value, 160.45 money market, 0.02 government cash). That is about $161, inferred from units. The
  backstop excludes them as traded.
- C_06 recomputes 10-01 from its 09-30 watermark, and D_04 serves as_of 10-01.

ACCEPTANCE (leg V):
1. The A_03 log reads 'Liveness: reference day 2026-09-30 ... 6,710 carry forward' and 'frontier whole'.
2. `platinum/firm/mix_summary.json` reads data_as_of 2026-10-01: every class, pct sum 1.0, market value within 2.0 pct of
   09-30's $1,843,114,311.70. The S18 run served $1,764,886,987.32; the expected total is about $1.843B, moved by one day's prices.
3. z0812888131's served timeseries carries 10-01 non-zero, near 09-30's 27,904.62.
4. The 335's 10-01 synthetic_correction sums to about 0 (the S18 run: -$78,504,236.80).

**Branch B, refusal (DELIVERY-INCOMPLETE, or LIVENESS-UNREADABLE if the dimension or the 09-30 partition cannot be read).**
- A_03 writes NO partition, does not advance its gate watermark, and exits 2.
- The chain aborts, so C_06 and D_04 do not run. Read in code:
  - `gold_dispatch.sh` aborts on a non-zero A_03 on both paths: parallel `wait_phase` (:489-517) and serial `set -e`
    (:427-429). `NONFATAL_IDS` is "E_18" only (:165).
  - Both wrappers return the child's exit code: `gold_prof.py:176,242` and `.tools/runner-telemetry.py:403-411`. The deployed
    `code/gold/runner-telemetry.py` (2026-06-05) is not diffed against the local copy.
- The served state stays as_of 09-30 (the restore). The S18 run's 10-01 partition stays in the cube, unread.
- The act stops: rules stay DISABLED, and the absent-account list from the log comes back here, by Sunday 18:00Z at the latest.

## Write set, per key, and rollback

- G: `code/gold/A_03.positions_cube.py`. Rollback: copy-object <- 1MYNHoSQ...
- W: the two C_06 watermark keys. Rollback: copy-object <- their pre-act versions kgIB3uHU5_.. and say77ubaeS.. (data_as_of 10-01).
- Q (Branch A only): the whole chain's served keys, the same classes as the restore set (platinum/**, gold/views/**,
  gold/artifacts/**, gold/firm_*.json), about 23.6k keys at as_of 10-01; plus the gold intermediates, which are not served.
  Rollback: the restore tool again (`R9_CHECKS/s18_restore_set.py` over the QA window, then `s18_restore.py --write`), back to
  today's restored 09-30 versions; the rules stay DISABLED.
- R: two rules re-enabled. Rollback: disable.
- Nothing deleted.

## COO half -- SIGNED (2.0.0_SA_COO~M, 2026-10-03 09:4xZ)

Signed on:
- the scoping departure above;
- the write set and the per-key rollback;
- writers counted at seven rules in three scripts;
- both branches, read from A_03's rule over today's inputs.

NOT read at signing:
- the run itself (leg Q);
- whether a 10-02 trade date lands before the fire (leg P stops it);
- which other consumers key on `account_is_open` alone (row S20).

Not covered by this cell: a cube partition left behind by a platinum-only restore is a trap for any later reference day. Today's
leg P guards it; the general case is named here, not solved.
