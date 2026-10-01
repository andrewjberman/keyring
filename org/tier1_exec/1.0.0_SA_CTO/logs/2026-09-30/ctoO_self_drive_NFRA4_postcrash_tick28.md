# /self-drive NFRA four -- ticks 26-28, hourly floor (1.0.0_SA_CTO~O, site Z, 2026-09-30 08:2xZ-09:2xZ)

- **state:** ARMED
- **Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260929_182xZ_SELF_DRIVE_O_NFRA_FOUR_PROJECTS_POSTCRASH.md` @680afc11fd
- **Cron:** 625c63e4
- **Previous log:** tick 25 @be216e1f39 (08:02Z author time).

## Carried tick lines (drive_ticks)

- tick 26 08:20Z: inbox 0; 19 of 187 open. MCPINDEX round 5 was written by 2.0.0_SA_COO~MI (7 new orders, not yet
  committed). MX-r-6 carries the NEVER-2 ledger and the CTO/COO never-widen halves, per B1. 0 calls.
- tick 27 08:51Z: inbox 0; 19 of 187 open. MCPINDEX round 5 was ISSUED @b2ead0491d and drained @2cae2db258. 0 calls.
- tick 28 09:20Z: this log.

## Measured (09:20Z)

- **Inbox:** 0 unread.
- **Open TOs:** 19 of 187, read from the last `<status>` tag (case-insensitive).
  - NFRA_OPLGTW 4 of 54.
  - NFRA_OPALAI 4 of 35.
  - NFRA_MCPORTAL 2 of 18.
  - NFRA_MCPINDEX 9 of 80: MX-a-8, q-3, r-6, r-7, s-14, s-15, t-10, t-12, t-13.
- **MX-a-8** (the Black Diamond analysis) was drained by 2.0.0_SA_COO~MI @2f81e5aa77. Its last tag still reads
  `pending`, so the issuer's close is not yet written.
- **Completion:** 0 of 4.
  - 1 REACHABLE: MCPINDEX, with round 5 executing.
  - 3 UNREACHABLE: the acts per the tick-11 log.
- **NFRA_MCPMSP (outside the scope):** round 1 is executing. MS-t-1, t-2 and t-5 are complete, and MS-w-1 is drained.
  2.0.0_SA_COO~MS filed row Z-S3, the `terraform get` step for the opal-gateway module (@d861bc3903).

## Calls

No open calls in the four projects (ticks 26-28).

## Acts only Andrew can do (each cited)

- **B3:** his R20 acknowledgement for the served key under `platinum/etfs/`. CLAUDE.md rule 30: "a deliberate departure
  is an R20 register entry Andrew acknowledges". It gates MX-t-10 only.
- **MX-t-12 / MX-t-11:** lifting his NOT YET on platinum/advi, a hold he set by name.
- **Unchanged:**
  - G-ACCT step 5 (his login or spend);
  - MCPORTAL G-2ND and G-CLOSE;
  - OPLGTW G-D and Part D;
  - NFRA_MCPMSP G-USER, G-IT-INF, G-ADVISOR, G-FIRM and G-KEY.
- G-C is external, at Opal IT.

## Compiler Tools

- Last-tag `<status>` census over `org/missions/D*/NFRA/<CODE>/task-orders/*.md`, with the per-project denominator
  printed.
- `git log --since` over `org/missions/D9/NFRA` and `org/missions/D6/NFRA` for movement.
