# Drive log -- 2.0.0_SA_COO~RV -- 2026-10-07 22Z to 2026-10-08 00:3xZ (host opal_bloomberg)

Continues `drive_log_20261007T20Z_opal_bloomberg.md`. `/canonical-drive ETFS_RIVALS`, lease FULL, hourly session cron.

## 22:1xZ-23:3xZ -- round 25 cut, built, drained

`ETFS_RIVALS | L5 -> L6 -> L7 -> L8 (FULL) | round 25 | thread y (SERVED) | PARALLELIZE, then DRIVE FORWARD`

- Two helpers drafted the checks (@beff6be3e7, @2d317208a8). ONE issuance 1580bfb033, 2 of 2 chains: RIV-rg-1 (the
  readers' grain of gold security_market, cut as the disarm of row Z-S69) and RIV-mr-1 (the marker read-out).
- mr-1 merged 4c34f7f298; rg-1 merged 1d2241ca66. Merged CLOUD 1e25383b04: suite 889 passed, 2 skipped, 0 failed; 34 of
  34 check files PASS.
- Real run, the before / after of every fund's tables (holding_contribution 2,418 page-period rows moved, buying_trend
  0), the control dates identical, a browser look at the marker read-out. Packet @7c0730d28d; COO half @cfa71419f0.

## 23:3xZ-00:3xZ -- the fault was read backwards; the readers are stopped; mr-1 ships alone; round 26

`ETFS_RIVALS | L9 -> L10 -> deploy (SERVED) -> L6 | rounds 25, 26 | thread y (SERVED) | DRIVE FORWARD`

- CTO half @16d5d5acd9 carried C1: a hand read of MediaTek by the reviewer. **CVO ADJUDICATION_v30 @e3cc04e7bb: RIV-rg-1
  J1 NOT MET -- 47 of 57 closes filed under 2026-09-29 equal the funds' 2026-09-30 valuations.** CTO ruling msg 31477:
  nothing is applied.
- **This seat's rows Z-S69 and Z-S70 read the fault backwards.** The served readers ignore the mis-dated object by a
  name tie-break; the union would have served a wrong day's closes. The before / after in the round-25 packet measured
  mis-dated data and was presented as a repair. The seat counted closes and did not check whose day they were.
- The read the CTO asked for (`round25/g4_date_offset_read_20261007.json`): ONE object of five that carry closes is
  mis-dated; its `as_of` equals its partition date; the four correct pulls carry `as_of` = the pull day. So the CTO's
  first term (keep a close where `as_of` equals the partition date) would have kept the wrong object: withdrawn by msg
  31480. Row Z-S71 (BLOCKING, ARMED) @bff3ec2e7f; COO half @cfa71419f0 WITHDRAWN.
- CTO ruling msg 31480: the union reads only objects whose name carries a capture time; untimed dates read as before;
  the mis-dated object named in a test; for FWD-24 every close a writer adds carries its own trading date.
- **RIV-mr-1 alone:** content pin fd633ec4d2 (the live pin plus the one mr-1 commit, cherry-picked in the deploy tree,
  resolved by content). COO half @888f6d1b61, CTO half @86a90330bc. Apply 0 added, 5 changed, 0 destroyed; ONE republish
  00:10Z, OK, 73.5 s, 557 MB; no table object written; 13 of 13 chart objects with identical data; audit byte-equal.
  Ledger `etfs-rivalfunds-r25-mr1` CLOSED 3 of 3.
- CTO half's C1: the 11:00Z vehicle's enrichment leg loads `gold_holding_contribution` through `security_names` and
  calls nothing of the round-25 reader. CTO ruling msg 31489: no revert; row Z-S72; the vehicle log's first read states
  the leg's exit code.
- A wrong zero caught in passing: a `git diff` run from a subdirectory with a root-relative path returned empty; re-run
  from the root it returned 134 lines. The empty read was not used.
- Round 26: a helper drafted `rg-2.AC1.py` and amended `rg-1.AC1.py` / `rg-1.AC2.py` to timed fixture names
  (@9da94348e0). ONE issuance 14d40de902 (RIV-rg-2), worker ~17 in `C:/tmp/wk-riv-r26-17`.

**Standing hazard:** site-Z CLOUD HEAD carries the round-25 readers. No rivalfunds deploy is built from HEAD until
RIV-rg-2's J1 is MET. The saved plan `C:/tmp/rv_apply25.tfplan` belongs to the withdrawn deploy.

Open: round 26's build, drain, real run (expected: 0 moved rows), packet, pair, deploy; ledger r22 L4 and L5 and the
vehicle log read (2026-10-08 11:00Z, 13:00Z); the recount of AI accounts after the sweep; Andrew's look at the chart;
round 27 = FWD-24's history-owed step and writer.
