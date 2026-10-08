# 1.0.0_SA_CTO~O -- /self-drive 30m ~O fabric, tick 1 (2026-10-08 ~21:5xZ)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_215xZ_SELF_DRIVE_30M_O_FABRIC_FOUR_PROJECTS.md`
@ba8c4598fb. Cron d7c133e4 at :07/:37 (session-only). `state: ARMED`.

## Scope (denominators printed)

| project | status | dep_stage | open TOs | sequence | COO lane |
|---|---|---|---|---|---|
| NFRA_OPLGTW | active | EXECUTING | 10 (to-check, 4 ACTIVE / 6 PENDING) | PLACED stage 5, no flag | 2.0.0_SA_COO~O LIVE |
| NFRA_OPALAI | active | EXECUTING | 3 PENDING | PLACED stage 5, LANE-DARK | 2.0.0_SA_COO~AI dark |
| NFRA_MCPORTAL | active | EXECUTING | 4 (2 ACTIVE / 2 PENDING) | UNPLACED | 2.0.0_SA_COO~MP LIVE |
| NFRA_MCPINDEX | active | EXECUTING | 2 ACTIVE (issued to 0.7.0_AE_CloudOps~MI) | PLACED stage 5, LANE-DARK | 2.0.0_SA_COO~MI dark |

Device: sitez (all four `device: site-z`). Inbox at tick: 0 unread (32029 acked). active-commitments: 1 line in 1 of 29
ledgers, none in scope. Capacity: 7 live COO lanes on this box, no cap ruled.

## Round 32 of NFRA_OPLGTW is issued with both of Andrew's asap chains

`OG-g5-1` (Tax SMA master 08403355 list-only enumerate) -> `OG-tm-1` (daily-pull add); `OG-cc-1` (13-month closure census)
-> `OG-bf-1` (marker backfill); `OG-cm-1` (grant calendar months); plus `OG-sf-1`, `OG-rf-1`, `OG-sc-1`. `OG-ga-1` (open
since 10-06) is the S41 `download_filtered` write on the one live `dim_asset` grant, on Andrew's own 10-06 word; it is not
Alyssa's scope and does not touch his "no downloads needed yet" for her.

## Calls ruled by the driver

1. NFRA_MCPORTAL C12, "streaming" read as "live on open" (3.0.0_SA_CVO~Z note 2, msg 32002). REC = RULING: the views update
   while the page is open, poll or push, age shown, no alert. Routed to 2.0.0_SA_COO~MP (msg to ~MP 21:56Z); PRD text at
   MCPORTAL's next L10 addendum (spec frozen mid-round).
2. NFRA_OPLGTW addendum, "any other principal needs his own word" (CVO~Z note 1): a gate Andrew did not set (his answer was
   (a), named Opal staff). RULING: struck at OPLGTW's next L10 addendum; no round-32 order depends on it.
3. NFRA_MCPORTAL C11 grant: ruled (a) by the NFRA_CLDGRPH owner (laptop msg 107359, relay 32029); routed to COO~MP.

Carried (unchanged): Alyssa's no-download as a CONTRACT line at OPLGTW's round-32 L10.

## Driver acts

- Seat ask to 0.0.0_AB_MSTR~Z: 2.0.0_SA_COO~AI and 2.0.0_SA_COO~MI (both LANE-DARK).
- Drive-pair ask to 2.0.0_SA_COO~O and 2.0.0_SA_COO~MP (msgs 32037, 32038): `/canonical-drive <own project> 30m` at +15m.

## Acts only Andrew can do

- The `opal-gateway-bbg` sign-in that release r29 waits on (`org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round31.md`
  section 5, R55). Alyssa's access waits on r29.

## Completion test

NOT DONE: 0 of 4 projects `status: complete`. REACHABLE 4, UNREACHABLE 0 (OPALAI and MCPINDEX are reachable once seated).

## Compiler Tools

- directives/sequence: `sequence-check.py --project` x4 (3 PLACED, 1 UNPLACED, 0 UNKNOWN); `to-check.py --all --project` x4;
  `active-commitments.py`. Worked.
- Failed: a first `send_message` to COO~MP returned Errno 13 but delivered; COO~MP holds a duplicate (628 B / 625 B).
- Gap: none new.
