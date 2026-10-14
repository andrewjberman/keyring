# self-drive sitez open calls -- ticks 15-16 (2026-10-14 10:50Z and 11:50Z), `1.0.0_SA_CTO~Z`

arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_203xZ_SELF_DRIVE_60M_SITEZ_BOX_OPEN_CALLS.md` @ce0ba39d90
state: ARMED   cadence: 60m (cron 5032b669 at :41)   ticks covered: 15 (quiet) and 16 (quiet) -- the hourly floor log

## Measurements (11:50Z)

- inbox: 0 unread at both ticks.
- open calls on sitez: 45 rows, 8 OPEN, all `act`.
- Since tick 14: the Alyssa row 3b41 was re-tested against Andrew's verbatim. The 10-08 "hold" was an approved REC
  "until r29 is live", and that condition is met, so nothing is left to lift. Corrected row def4 was added. 3b41's
  close was REFUSED as CROSS-BOX (it needs xadj), and def4 is also CROSS-BOX, so both stay open and one sitting closes
  both. Commit @7dc729445b.

## ACTS ONLY ANDREW (OR A PERSON) CAN DO -- 8 rows, 4 distinct acts

| act | rows | citation |
|---|---|---|
| the ONE MC Portal sitting (FWD-20 read, /control-plane, /open-calls, one Bloomberg-account sign-in) | 21d9, 21c5, 8ed7, f0d2 | a human read and a login (MP-z-6, MP close runs) |
| the Alyssa sitting (FWD-1 close run: narrow, she asks, widen, she asks) | def4, 3b41 | his dashboard change plus a named user's own questions |
| name one asset manager by work email; his own work-Claude stand-in login | 232a | his knowledge of his staff; a login |
| one Teams message to the Opal Bloomberg account | a519 | a person's send |

## Completion test

NOT DONE. Stop: Andrew's stand-down.

## Compiler Tools

`check_inbox`, `.tools/open-calls.py list|close|add|publish`. Gap: `close` refuses a CROSS-BOX row without an xadj, while
`add` admits a CROSS-BOX replacement row, so a correction that cannot close its original leaves a duplicate.
