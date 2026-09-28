# /self-drive ~O fabric -- ticks 55-57 (07:47Z-08:46Z), 1.0.0_SA_CTO~O

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_O_FABRIC.md` @56050d290d
**Why written:** the hourly floor; also one routing refusal.

## What moved

- **MX-s-7 COMPLETE** @b8a7da3c17. NFRA_MCPORTAL: COO~O closed 4 ARMED rows (@8ade3a5801).
- **Z-S25 step 1 landed** @bbf8cfefa6 (DS~D). An EXACTLY-empty field maps to None; " ", "	", "n/a" and "--" still
  raise. The real 2026-08-29 bytes test fails first against HEAD (VendorDriftError "non-numeric text ''"); after the
  fix, 62 passed and 10 skipped. The 4-partition backfill is written as a gated runbook (@e30a974871) and not run.
- **MX-s-8 ISSUED** @f382d1848c: the Z-S3 and Z-S25 fixes go into the 4 silver Lambda copies (`silver.tf`), deployed in
  one never-widen act. **The CTO half is owed after PHASE A's announcement.** It will be signed against:
  - the Terraform plan's resource list (code attributes of 4 functions only);
  - each Lambda layer's pandas version: Z-S3 is DELTA = 0 on any layer below pandas 3;
  - Z-S25 as the one real served change: partitions that raised before will now be written, with NULL in the empty
    column;
  - the rollback keys (CodeSha256 per function).
- **COO~O liveness re-measured** at 08:00Z after DS~D wrote "QUEUED, not live": last commit 07:48Z, inbox 0 unread, and 2
  live claude.exe carry the serial. It is LIVE; "queued" meant the cell was not yet cut.

## Routing refusal (not a ruling)

COO~O asked this seat to rule OPLGTW row W3-S22 (the sprint view fails OPEN: `SPRINT_VIEW_ALLOWED_EMAILS` is set 0 times on
the host, `sprint_view.py:172-174` returns True on an empty roster, and the deploy's `.env` rewrite never writes the key).
- **Not this seat's to rule:** CVO~O's verdict @e470835e7c gives ~O the OPLGTW COO leg only, until a re-seat record moves
  `leads.cto` (~A) and `leads.cvo`. It was returned for `leads.cto`.
- REC given as input only: add the key to the `deploy-to-ec2.sh:196` literal, then flip to fail-closed, in one release
  under a never-widen sign-off.
- This is now a concrete, live cost of Andrew's call 1.

## Calls, verdicts

No new call. At Andrew: call 1 BLOCKING (the OPLGTW re-seat, now also carrying W3-S22), call 2 CARRIED (D9 device), and
the switchover sitting. 0 self-drive verdicts.

## Completion test

NOT DONE -- 0 of 4 projects `complete`. All REACHABLE. Open orders in scope: MX-s-4, MX-s-6, MX-s-8 (MCPINDEX); OA-t-1,
OA-t-3 (OPALAI).

state: ARMED

## Compiler Tools

git log / order-file reads; a PowerShell CIM process count for COO~O liveness.
