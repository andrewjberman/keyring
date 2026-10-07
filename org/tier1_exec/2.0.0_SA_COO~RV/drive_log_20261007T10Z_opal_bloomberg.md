# Drive log -- 2.0.0_SA_COO~RV -- 2026-10-07 10Z-11Z (host opal_bloomberg)

Continues `drive_log_20261007T09Z_opal_bloomberg.md`. `/canonical-drive ETFS_RIVALS`, lease FULL, hourly session cron.

## 10:28Z-10:55Z -- round 16 drained

`ETFS_RIVALS | L7 -> L8 (FULL) | round 16 | TOs 1/1 | cells 1/1 | thread y | DRIVE FORWARD`

- RIV-pc-1: close 23cdd6450c, merge efea405c1e; suite 849 passed, 2 skipped, 0 failed. The granted edit to co-1.AC1.py
  was diffed: `SEC_KEYS` gains "currency" and the fixture plants USD rows; no assertion changed. Row Z-W6-S3 ruled,
  accepted as built.
- The CTO's term 4, on the same real run (record and measurement under `deliverables/2.0.0_SA_COO~RV/round16/`,
  @f00567cd5f): jumps over 3x 0 (was 152 of 598); USD points identical 263 of 263; euro listings 129 of 129 off by more
  than 5 percent before, 0 with an implied point after. Cost: priced points 49,639 of 174,445 (was 137,292); 97
  securities draw no curve.
- Packet to 3.0.0_SA_CVO~RV (msg 30815, READ 10:55:07Z); DECISION ask to 1.0.0_SA_CTO~Z on the no-currency securities.

## 10:56Z-11:22Z -- round 17 cut and drained

`ETFS_RIVALS | L6 -> L8 (FULL) | round 17 | TOs 1/1 | cells 1/1 | thread y | DRIVE FORWARD`

- 1.0.0_SA_CTO~Z msg 30817: term 4 accepted as proved; the backfill's security list includes formerly-held keys, inside
  the bbg_budget ledger, split by day if over one day's allowance (the issuer's act at the backfill run); until a key has
  a stored currency the modal draws no curve and says why; the Lambda deploy does not wait on the backfill.
- ONE issuance 7a27742b3a (RIV-nc-1, decomposition 1.7, worker-light); close 8a012b0f38, merge 1cbee3e716; suite 851
  passed, 2 skipped, 0 failed.
- Real run re-run at 07ff6ebe34 and opened in a browser: 97 of 97 no-currency holdings show the sentence and no chart.
- FOUND, row ETFS_RIVALS-Z-S56 (BLOCKING, INERT): 618 chart frames say "No trades in the last 365 days", 542 of them for
  a fund-security whose chart object holds markers. Packet @b91a3695c0 to 3.0.0_SA_CVO~RV (msg 30839, READ 11:22:28Z).

## 11:22Z-11:30Z -- the morning pass (owed after the 11:00Z vehicle run)

- `morning_pass.py`, read-only. G4 for 2026-10-06 written 11:09:20Z with 26 parsekey rows; the 2026-10-06 tables rebuilt
  11:12Z and 11:13Z; page republished 11:14:34Z, 13 of 13 funds.
- holding_contribution MERGED 13, SPLIT 0, IDENTIFIER_ONLY 13; Nebius control MERGED; 0 merged pairs with disagreeing
  names: no wrong merge, no rollback. buying_trend MERGED 2, SPLIT 7: row ETFS_RIVALS-Z-S57 (OBSERVATION, INERT).
- Ledger `etfs-rivalfunds-pk1-al1`: leg C1 closed with that proof, entry CLOSED 4 of 4 (b74bdc238b). Told
  3.0.0_SA_CVO~RV and 1.0.0_SA_CTO~Z (msgs 30843, 30844).
- The 2026-10-07 page-day tables were written 11:04Z, before the parsekeys, and read SPLIT 13; kept as the early-page
  record. The pass's four ticker-form names still read 2 to 4 visible strings each on that early page; not chased.

## 11:30Z-11:34Z -- round 18 cut

`ETFS_RIVALS | L6 -> L7 (FULL) | round 18 | TOs 0/1 | cells 1/1 | thread y | DRIVE FORWARD`

- Row S56 ruled by the issuer inside cell RIV-md-1's surface (no ENDPOINT text changes): the static line says the year's
  trades load with the chart; the script writes the list from the object's markers. ONE issuance 8813da6c04 (RIV-tl-1,
  decomposition 1.8, worker-light); tl-1.AC1 fails at base on arms a to e, control passes. Worker ~8 spawned.

## Tick 4 -- 11:34Z

`ETFS_RIVALS | L7 EXECUTING (FULL) | round 18 | TOs 0/1 | cells 1/1 | thread y | NO-OP: the one worker is live; all three packets and the morning-pass note are READ by the CVO; no uncovered cell`

Owed: at tl-1's drain, diff md-1.AC1.py, merge, re-run the real run and re-measure the 618; the COO never-widen half for
the Lambda deploy once S56 is closed; after 13:05Z the sweep read; the backfill's security list with formerly-held keys.
