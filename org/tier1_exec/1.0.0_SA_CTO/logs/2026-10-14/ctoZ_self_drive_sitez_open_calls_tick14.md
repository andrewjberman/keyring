# self-drive sitez open calls -- ticks 13-14 (2026-10-14 08:50Z and 09:50Z), `1.0.0_SA_CTO~Z`

arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_203xZ_SELF_DRIVE_60M_SITEZ_BOX_OPEN_CALLS.md` @ce0ba39d90
state: ARMED   cadence: 60m (cron 5032b669 at :41)   ticks covered: 13 (quiet) and 14

## Measurements (09:50Z)

- inbox: 0 unread.
- open calls on sitez: 44 rows, **7 OPEN** (down from 10).

## Since tick 12

| item | ruling / act | carrier |
|---|---|---|
| Andrew-direct ~09:0xZ (relay msg 34000): "What is the hold you are referring to? There should be no hold" | R2 STAYS (10:30Z revert cancelled, COO~ZB ack 34004); R3 unheld; call 6c9f closed ruled-by andrew | @8033df9da2 |
| OPAL_BBGTML Z6 drain-end (ZB 34006) | 6 of 6 dispositioned: R2, R5, R6 COMPLETE; R3 parked on its branch (the Terminal is signed in, so it cannot be exercised); R4 cancelled. Call 763e CLOSED as met (dapi_check UP and entitled 09:25Z/09:30Z). Row Z-S18 recorded as NFRA_OPALAI's un-park first act (re-baseline e7.AC1) | @7461b39927 |
| call 2da6, the GUARD-4 merge | re-tested against Andrew's VERBATIM 10-06 aim ("accidentally overwriting ... Positioning ... ETFS view"); a deliberate, proven tripwire check is outside it. Ruled YES, change-managed under COO~ZB, outside the pull window, one real run | @d8c5d77e26 |

**Self-correction recorded:** this seat listed two items (6c9f and 2da6) as Andrew's on a hold scope taken from a
recorder's "Unchanged" section rather than his verbatim sentence. Andrew corrected it. From now on a hold-based act is
listed for Andrew only when his own quoted sentence covers it. The proposed skill fix (Step 1's citation test quotes
the verbatim) is offered to Andrew and not applied here.

## ACTS ONLY ANDREW (OR A PERSON) CAN DO -- 7 OPEN rows

| row | act |
|---|---|
| 21d9 (+21c5, 8ed7, f0d2) | the ONE MC Portal sitting: read the FWD-20 breakdown, /control-plane and /open-calls, one Bloomberg-account sign-in |
| 3b41 | sit once with Alyssa for MC Portal FWD-1's close run. NOTE: re-test its "10-08 hold" against his verbatim at the next tick |
| 232a | name one asset manager; his own work-Claude stand-in login |
| a519 | one Teams message to the Bloomberg account |

## Completion test

NOT DONE. Stop: Andrew's stand-down.

## Compiler Tools

`check_inbox`, `.tools/open-calls.py list|close|publish`, `git diff --stat HEAD...rv-bbgtml-guard4`. Gap: none.
