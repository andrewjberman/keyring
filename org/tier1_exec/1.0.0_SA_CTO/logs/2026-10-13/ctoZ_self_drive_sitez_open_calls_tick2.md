# self-drive sitez open calls -- tick 2 (2026-10-13 ~21:5xZ), `1.0.0_SA_CTO~Z`

arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_203xZ_SELF_DRIVE_60M_SITEZ_BOX_OPEN_CALLS.md` @ce0ba39d90
state: ARMED   cadence: 60m (cron :41)   ticks covered: 2 (the first attempt at ~20:5xZ was interrupted by Andrew at the terminal)

## Measurements (21:51Z)

- inbox: 0 unread.
- open calls on sitez: 41 rows, 8 OPEN, all `act`.
- sequence-check: no DRIFT and no OUT-OF-SEQUENCE. CAPACITY: 4 live COO lanes (~MI, ~MP, ~O, ~ZB); no cap is ruled
  for this box.

## Calls ruled since tick 1 (the driver's REC unless noted)

| call | ruling | carrier |
|---|---|---|
| MP-z-5 never-widen CTO half (MQ 33749) | SIGNED. 3a import hunk accepted; section 6 option (b), the 7 Z-S45 failures as a closed set | @567da88c25 |
| OPAL_BBGTML R4 pair (ZB 33751) | CTO half SIGNED @6d8f802b36, then WITHDRAWN on Andrew-direct ~20:5xZ: "not a priority right now + TCKT work is on DELL2 not here" | record @939ca9dccc; dell2 told on the bus (input only) |
| OPLGTW FWD-21 identity vs grant writer (O 33760) | V1 admits by identity (OG-tg-1's predicate) | PRD v2.7 @27ba6b6191 |
| OPLGTW FWD-21 proof gaps (ZB F1 33767, CVO 33770) | research-only refusal arm; census from the identity store; S3 read named as a widening | PRD v2.8 @ecdab3c7d0, ADMITTED (CVO 6771c65d2e11) |
| Control Plane shows each box's Claude account and usage (XB-111f from dell2, Andrew-direct ~20:4xZ) | lands as an MC Portal PRD addendum at the GW round's analysis, after FWD-20 | row NFRA_MCPORTAL-Z-S47 @7b07f79a4c |
| ~ZW crossbox acks (MSTR 33784) | the ack belongs to the named seat only (crossbox-call refuses another --by); both commands carried to ~ZW | file in ~ZW's read/ (the send raised a permission error after the watcher moved the file) |
| no standby on every device (Andrew-direct ~21:3xZ at this terminal) | recorded; site Z already reads 0 on AC and DC; MSTR~Z relays to the laptop, dell1 and dell2 MSTRs | @76974ace76 |
| R2/R3 vs the 10-06 no-modify hold (ZB 33802) | an act only Andrew can do (lifting a hold he set by name); put to him at the terminal and listed with a 10:30Z revert default | open call added this tick |

Delivered since tick 1: MP-z-5 is LIVE @64b3e54658 (8 channels, 67 tools, ledger L1-L4 CLOSED). AC2 waits on COO~MP's
one-line probe fix (row Z-S48). The ONE MC Portal sitting is listed (row 21d9 @996da266b6).

## ACTS ONLY ANDREW (OR A PERSON) CAN DO -- 8 OPEN rows, each cited

| row | act | citation |
|---|---|---|
| (new) | yes or no: lift the 10-06 no-modify hold on the sign-in scripts for R2/R3 | a hold he set by name: the 10-06 "Unchanged" clause, sign-in scripts |
| 21d9 | the ONE MC Portal sitting: read the FWD-20 breakdown, /control-plane and /open-calls, one Bloomberg sign-in | a human read and a login (MP-z-6) |
| 21c5, 8ed7, f0d2 | the three earlier rows the sitting batches | as 21d9 |
| 763e | Terminal sign-in before 07:00 ET (row Z-S16 says DAPI read UP at 21:14Z, so it may already be met; asked) | a login |
| a519 | one Teams message to the Opal Bloomberg account | a person's send |
| 2da6 | the TO-GUARD-4 merge | the same 10-06 hold, lifted for GUARD-3 only |

## Completion test

NOT DONE. Stop: Andrew's stand-down.

## Compiler Tools

`check_inbox`, `.tools/open-calls.py list|add|publish`, `.tools/sequence-check.py`, `.tools/prd-signoff.py status`,
`.tools/crossbox-call.py ack`, `git diff --name-only` (MP-z-5 census re-read), `powercfg /query`. Gap: the outside
probe of mcp.opalinvest.dev reads 302 on every path (sign-in redirect at the edge), so it cannot grade a route; the
host-side AC2 is the instrument.
