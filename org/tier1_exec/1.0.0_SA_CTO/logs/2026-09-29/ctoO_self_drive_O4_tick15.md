# /self-drive ticks 14-15 -- ~O fabric, four projects (1.0.0_SA_CTO~O)

**archetype:** COORDINATE

- Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_222xZ_SELF_DRIVE_O_FABRIC_FOUR_PROJECTS.md`
  @7612f001c4. Cron `0eef1ea2` (confirmed live by CronList at ~04:5xZ, on Andrew's question).
- Ticks covered: 14 (04:44Z, runtime line) and 15 (05:13Z). **state: ARMED**

## Scope at tick 15

| project | status | dep_stage | open TOs | reachability |
|---|---|---|---|---|
| NFRA_OPLGTW | active | EXECUTING | 7 / 53 | REACHABLE |
| NFRA_OPALAI | active | EXECUTING | 5 / 35 | REACHABLE |
| NFRA_MCPORTAL | active | EXECUTING | 2 / 18 | REACHABLE |
| NFRA_MCPINDEX | active | EXECUTING | 9 / 73 | REACHABLE (round 4 issued) |

23 of 179 open. The rise from 14 is MCPINDEX's round-4 issuance of 9 orders. Inbox: 0 unread. Sequence flags: none.

## Acts since tick 13

1. **NFRA_MCPINDEX round-3 L10 analysis** @f354170b42, sent to COO~MI.
   - Grades: 0 REALIZED; FWD-1 and FWD-2 NOT_REALIZED; 7 DEFERRED; FWD-3 HELD on the OPLGTW Schwab switch-on.
   - Rulings: Z-C-S28 (next_tool names the purpose-built tool); Z-C-S29 (keep the certification vintage and add a
     measured served_written_at); Z-W8-S3 ARMED, disarmed this round by DISABLING the 4 proven-dead BD schedules.
   - G5 rides OPLGTW's G-C identity. The round-4 list has 7 items, with r5.J1.
2. **Z-S15, the halt gate refusing two-letter lanes, ruled this seat's and fixed** @64a3ef4b4e: `halt-gate-check.sh`
   now admits 1-3 uppercase letters. Exercised: ~MI, ~O and ~ZZZ give rc=0; ~ABCD, ~mi and ~M1 give rc=1.
3. **The RESERVED catalog-widening calls went to Andrew.** On his "Go with your recs" (~04:5xZ, record @dc75ddbe32):
   - platinum/etfs is YES, and 3b is released;
   - platinum/advi is NOT YET, and 3c is held until W4b's certification closes.
   The word was relayed to COO~MI.

## Verdicts from CVO~O

0 pitched (no governance fork).

## At Andrew (acts only; 0 open calls)

G-ACCT steps 5-6; MCPORTAL G-2ND and G-CLOSE; Alyssa's Q1-Q3 post; the BD rotation (later).

## Completion test

NOT DONE: 0 of 4 complete. REACHABLE 4, UNREACHABLE 0.

## Compiler Tools

- `sequence-check.py --project` x4: flags none.
- The order-file census: 23 of 179 open.
- `bash -n` plus a direct `halt_gate_validate_serial` exercise (3 positive, 3 negative).
- `CronList`: 1 job, `0eef1ea2`.
- The gap: `send_message` twice returned `id=None` and one ack returned "broker call FAILED". The broker plane
  degraded briefly, while file delivery held.
