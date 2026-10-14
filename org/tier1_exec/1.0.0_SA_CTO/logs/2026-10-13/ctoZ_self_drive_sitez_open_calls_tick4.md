# self-drive sitez open calls -- ticks 3-4 (2026-10-13 22:50Z and 23:50Z), `1.0.0_SA_CTO~Z`

arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_203xZ_SELF_DRIVE_60M_SITEZ_BOX_OPEN_CALLS.md` @ce0ba39d90
state: ARMED   cadence: 60m (cron :41)   ticks covered: 3 (quiet, line carried from `org/mcp/drive_ticks/`) and 4

## Measurements (23:50Z)

- inbox: 0 unread.
- open calls on sitez: 43 rows, 10 OPEN, all `act`.
- sequence-check: no DRIFT and no OUT-OF-SEQUENCE.

## Calls ruled since tick 2

| call | ruling | carrier |
|---|---|---|
| MX-r-11 CTO half (MI 33810) | SIGNED: catalog + discover release `ad2acc0a93` on live 64b3e54658 (2 files; blobs equal the drained bytes) | @98ce8d9ff1 |
| OG-ap-15 per-family drains (O 33817) | schwab SIGNED; etf SIGNED on E1 (its 17 drift lines are the ruled Z-S25/Z-S3 fixes); blackdiamond refused as built; route (a) drain-only RULED | @39efe27671 |
| OG-ap-15 drain-only re-ask (O 33825) | blackdiamond, orion, eclipse SIGNED: one file each vs base b0af6527a3, 0 stray lines, 0 address lines | @29c257aa4e |
| 232a, name an asset manager (ruled a FACT, not an Andrew-only act) | asked dell1 first: NONE ON RECORD (33821). Andrew's work Claude runs FWD-21's first live read as a stand-in, graded PARTIAL; the research-only arm waits for a named asset manager (dell1's tick-4 REC, concurred, 33822) | msg to COO~O |
| MX-r-11 v2 fix-forward (MI 33832) | SIGNED: 1 file, +5/-5; the two `definition:` values now point at the decorators of def opal_discover / def opal_describe; rollback is v1, never 64b3e54658 | @62e8f7d19f |

Delivered: MCPINDEX v1 is serving on the gateway (FWD-20 67 of 67, FWD-21 3 of 3, per COO~MI).

## ACTS ONLY ANDREW (OR A PERSON) CAN DO -- 10 OPEN rows, each cited

| row | act | citation |
|---|---|---|
| 6c9f | yes or no: lift the 10-06 no-modify hold for R2/R3 (R2 is reverted at 10:30Z with no answer) | a hold he set by name |
| 3b41 (new) | lift the 10-08 hold and sit once with Alyssa for MC Portal FWD-1's close run (r29's `opal_asker_query` is now live) | a hold he set by name; a sitting with a named user |
| 21d9 (+21c5, 8ed7, f0d2) | the ONE MC Portal sitting | a human read and a login |
| 232a | name one asset manager by work email (dell1 has none on record); his own work-Claude login for the stand-in read | his knowledge of his staff; a login |
| 763e | Terminal sign-in before 07:00 ET (may be met: DAPI UP at 21:14Z per row Z-S16) | a login |
| a519 | one Teams message to the Opal Bloomberg account | a person's send |
| 2da6 | the TO-GUARD-4 merge | the 10-06 hold, lifted for GUARD-3 only |

## Completion test

NOT DONE. Stop: Andrew's stand-down.

## Compiler Tools

`check_inbox`, `.tools/open-calls.py list`, `.tools/sequence-check.py`, `comp-find` (AMGT asset-manager census: 4 hits in 63
files, none naming a person), `git diff --stat` and `git merge-base`/`rev-parse` on each signed cut, the `comm -23` stray-line
check on orion's drain-only package (0 stray). Gap: none.
