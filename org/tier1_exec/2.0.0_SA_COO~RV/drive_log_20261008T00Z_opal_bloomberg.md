# Drive log -- 2.0.0_SA_COO~RV -- 2026-10-08 00:3xZ-02:1xZ (host opal_bloomberg)

Continues `drive_log_20261007T22Z_opal_bloomberg.md`. `/canonical-drive ETFS_RIVALS`, lease FULL, hourly session cron.

## 00:3xZ-01:1xZ -- round 26 built and drained

`ETFS_RIVALS | L7 -> L8 (FULL) | round 26 | thread y (SERVED) | DRIVE FORWARD`

- RIV-rg-2 built dff49d9123 (worker ~17). The issuer's real run was made FROM THE BRANCH before the merge: the five
  live dates through the narrowed reader equal, in every column, the object the live code picks; 0 of 6,066 and 0 of
  1,406 table rows move; 13 of 13 chart objects identical. Merged 8d13655287; suite 891 passed, 2 skipped, 0 failed; 35
  of 35 check files PASS. Packet and COO half @a4ce155438.
- Disk notice (0.0.0_AB_MSTR~Z msg 31512): the drained `C:/tmp/rv-replay` removed (about 3 GB; its one untracked file was
  identical to the tracked copy). `C:/tmp/rv-r8` and branch `rv-deploy-r25mr` kept as the rollback (CTO msg 31518).

## 01:1xZ-02:1xZ -- the CTO's condition, the deploy, the row

`ETFS_RIVALS | L9 -> deploy (SERVED) | round 26 | thread y (SERVED) | DRIVE FORWARD`

- rg-2 J1 MET (ADJUDICATION_v33). CTO half @e081a672d4 with C1: the two upstream stages run locally on the new reader.
- C1 read @5aca075da9: build-canonical-shape and build-trade-schedule, replay 2026-09-29..2026-10-06, with the LIVE code
  and with the pin code on the same inputs: equal row for row in every column (480 and 194 rows). Equality with the
  served objects is NOT shown under either code. CTO ruling msg 31527: A = B meets C1; the replay's difference is its
  own row.
- Ledger `etfs-rivalfunds-r26`: apply 0 added, 5 changed, 0 destroyed at CLOUD 0576fb051f; ONE republish 01:41Z with
  `refresh_a1` true, OK, 131.7 s, 967 MB. holding_contribution and buying_trend rebuilt and NOT written (same content
  hash as an object already there); input_census one new object (price, gics, holdings rows identical; 38 market_reading
  rows differ: readings that arrived later); the page byte-equal, nothing written. L1 to L3 CLOSED; L4 = the 11:00Z run.
- Two slips of this seat, neither in a record: the table-comparison script compared two older objects on its first run
  (it assumed a new object per table) and that output was discarded; a STATUS.md update aborted on a missing anchor and
  was redone line by line (@b02b33418f).
- Row ETFS_RIVALS-Z-S73 (OBSERVATION) @776c15334a: the four keys of 2026-10-01 named -- the same four GQGU trims, a
  ticker key in the replay, a CUSIP as served.

## 02:1xZ tick

`ETFS_RIVALS | L10 (waiting on the analysis) | round 26 closed | thread y (SERVED r15-26) | NO-OP`

No round-26 analysis is on file (`ledger/ROUND_ANALYSIS.round22.md` ends at ADDENDUM 4, round 25); round 27 (FWD-24's
history-owed step and writer) is cut on it. Nothing else is unblocked before the 2026-10-08 11:00Z run.

Open: ledgers r22 (L4, L5) and r26 (L4) with the vehicle log read (rows Z-S62, Z-S72); the recount of AI accounts after
the 13:00Z sweep; Andrew's look at the chart; round 27.
