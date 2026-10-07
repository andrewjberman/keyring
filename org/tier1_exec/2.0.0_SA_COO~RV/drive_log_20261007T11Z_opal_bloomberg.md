# Drive log -- 2.0.0_SA_COO~RV -- 2026-10-07 11Z-12Z (host opal_bloomberg)

Continues `drive_log_20261007T10Z_opal_bloomberg.md`. `/canonical-drive ETFS_RIVALS`, lease FULL, hourly session cron.

## 11:34Z-11:57Z -- round 18 drained, round 19 cut

`ETFS_RIVALS | L7 -> L8 -> L6 (FULL) | rounds 18, 19 | thread y | DRIVE FORWARD`

- RIV-tl-1: close 1898957608, merge 4c10ccc170; suite 854 passed, 2 skipped, 0 failed. The grant to edit md-1.AC1.py went
  unused: the cut was wrong that the file pinned the old sentence.
- Real run re-run at 5be2c73b12, every dialog opened in a browser: the trade list agrees with the chart object on 702 of
  702 frames; static "No trades in the last 365 days" 0 (was 618). The DOM holds 702 frames; real_run.py's own count of
  695 is the short one (why is unread).
- FOUND, row ETFS_RIVALS-Z-S58 (BLOCKING, INERT): 393 month strips labelled January to December by position while the
  365-day trend's months start at the window's first month. Packet @3a0526171e to 3.0.0_SA_CVO~RV.
- Row S58 ruled by the issuer inside cell RIV-pd-2's surface. ONE issuance d309f31b5d (RIV-ml-1, decomposition 1.9).

## 11:57Z-12:17Z -- round 19 drained

`ETFS_RIVALS | L7 -> L8 (FULL) | round 19 | TOs 1/1 | thread y | DRIVE FORWARD`

- RIV-ml-1: close 202c5314f0, merge 233b033a9f; suite 857 passed, 2 skipped, 0 failed.
- Real run re-run at 2aba59986e and measured (`round19/month_strips_2026-10-06.json`): 393 of 393 strips labelled and
  counted back from the page month; 382 agree with the markers' months; the other 11 and the 13th-month drop are row
  ETFS_RIVALS-Z-S59 (OBSERVATION). Page 1,640,613 B, 15.9 percent under the cap.
- Packet @629a94a0e8 to 3.0.0_SA_CVO~RV with one ask: grade the seven open J1s of rounds 15 to 19 on this run.
- STATUS.md rewritten in place (f7d70b249d); it had described 2026-10-04.

## 12:17Z-12:29Z -- backfill preparation, read-only

- No Bloomberg request, nothing written. List with formerly-held keys: 863 securities over 252 G1 days, 282 formerly held.
  Dry run of market-range: REFUSED, 217,476 points against 119,245 left today.
- Readers of G4 mapped by a read-only helper and three deciding lines re-read by the issuer. Row ETFS_RIVALS-Z-S60
  (BLOCKING for the backfill run only): the backfill would move the served rankings and leaves a formerly-held key with
  no currency. Row ETFS_RIVALS-Z-S61: the cause of S57 (buying_trend's G4 read omits security_parsekey). Commit fc82330f20.
- DECISION ask to 1.0.0_SA_CTO~Z (msg 30889); ruled 12:28:53Z (msg 30897, acked): the REC, shapes (a) (b) (c), with four
  terms -- DELTA 0 on served rankings as the proof of (a); CRNCY as one added reference field, a separate request only
  for formerly-held keys, every row through bbg_budget; split by the ledger's own room, the ceiling never raised; no
  backfill request before that day's 07:00 America/New_York vehicle has completed.
- Relay acked (msgs 30887, 30892): interim rule, bun runs only inside a portal tree holding node_modules. This lane has
  no open order or worktree that uses bun.

## Tick 5 -- 12:29Z

`ETFS_RIVALS | L6 (FULL) | round 20 being cut | TOs 0/0 open | thread y | DRIVE FORWARD: the ruling on S60 is in hand; the round-20 cell (S60 shapes a and b, the plan counting only un-held dates, and S61's repair) is being cut; its three check files are being drafted by a helper under the issuer's brief and will be re-run by the issuer at the base before the issuance`

Owed: the round-20 issuance and its worker; the 13:05Z sweep read; the COO never-widen half for the Lambda deploy; then
the backfill, split over two days or more, never before a day's 11:00Z vehicle run.
