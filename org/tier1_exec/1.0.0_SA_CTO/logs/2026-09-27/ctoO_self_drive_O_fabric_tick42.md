# /self-drive ~O fabric -- ticks 41-42 (01:05Z-01:20Z), 1.0.0_SA_CTO~O

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_O_FABRIC.md` @56050d290d
**Why written:** a driver act (the runbook update) on a gate flip (OA-g-3 drained).

## What moved

- **W2-S4 CLOSED at the tool:** `0.7.0_AE_CloudOps~I` applied this seat's patch under its lane @765093b0e3. The defect
  behind NFRA_OPALAI-Z-W2-S4 is fixed in `infra/aws/ec2/safe-ec2-deploy.sh`.
- **OA-g-3 drained** @da3a2cafbe (`2.0.0_SA_COO~O`; worker proof @1bc93fcd6b, AC1 and AC2 PASS). Alyssa Keith's portal-only
  grant is ACTIVE: operations `[query]`, 10 portal channels, zero Schwab masters, written through the operator command.
- **MX-s-4** ledger CLOSED 6/6 @18379da757, with `0.7.0_AE_CloudOps~I`'s row on the BD SSM documents (`exit 1` before
  `shutdown -h +2` strands the runner in 5 of 6; one idle instance at filing). That row is owned by AE~I and COO~O, not
  this seat.

## Driver act

`ANDREW_SWITCHOVER_RUNBOOK.md`: the step-6 precondition now reads UNBLOCKED, citing OA-g-2 @20bf1189bd and OA-g-3
@da3a2cafbe. All four parts (A, B, C, D) can run in one sitting.

## Inbox, calls, verdicts

0 unread. No new call. At Andrew, unchanged: call 1 BLOCKING (re-seat OPLGTW's CTO and CVO legs to ~O); call 2 CARRIED
(D9 device, REC (a) no). The switchover sitting itself is Andrew's act, now fully unblocked. 0 verdicts.

## Completion test

NOT DONE -- 0 of 4 projects `complete` (NFRA_OPALAI, NFRA_MCPORTAL, NFRA_MCPINDEX, NFRA_OPLGTW). All REACHABLE.

state: ARMED

## Compiler Tools

git reads only.
