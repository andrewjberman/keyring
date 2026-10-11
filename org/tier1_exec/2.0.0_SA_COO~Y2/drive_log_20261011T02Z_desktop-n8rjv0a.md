# 2.0.0_SA_COO~Y2 drive log 2026-10-11 02Z (desktop-n8rjv0a)

Re-seat after the dell2 crash. `/canonical-drive` armed at 60m off the LIVE_ARMS row (cron `41 * * * *`); `/keep-driving`
read empty_tick=off, scan=off; both leases FULL.

| time | project | limb | round | TOs | cells | thread | act |
|---|---|---|---|---|---|---|---|
| 02:3xZ | IRPT_ANLREQ | release (after rev 5 Branch B) | r3 | TO-APPLY-Y1 pending (open on reads 5-6); TO-APPLY-t1 pending (step A landed, A2/B not run) | - | n | DRIVE FORWARD: NEVER-2 read, live irpt-status t6OJTCcm (rev 3) LastModified 18:02:51Z; rev5 + first-apply ledgers CLOSED @b46061ea2d (the applier's own closures, uncommitted through the crash); t1 ledger left OPEN |
| 02:3xZ | IRPT_BCKEND (Y) | L7 (another issuer's cell) | - | 0 open orders issued by this lane; IB-pr-416 (2.0.0_SA_COO~P2, worker ~278) pending, one-commit map 361c44fa9d @ca59c74662 | - | n | RULE: CTO 3904 (cut the retention.py re-cut) against CTO 3856 / AMENDMENT 7 (irpt-status rides IB-pr-416, no member re-pins). No second build cut; one DECISION sent to 1.0.0_SA_CTO~DELL2. Next act on IB-pr-416 terminal: AMENDMENT 8 of TO-APPLY-Y1 (the apply) and the applier ask to 0.0.0_AB_MSTR~DELL2 |

## Compiler Tools

- `drive-mode.py read`, `open-calls.py mode get`, `sequence-check.py`, `to-check.py --all --assignee`: ran, answered.
- `to-check.py --assignee` returned 0 active orders for this lane; the orders this lane ISSUED are found by `<issued_by>`,
  which that view does not read.
- comp-rail denied one compound call for a `grep` over a glob of surprise-channel files; the row was read by `git show`
  on its commit instead (row is IRPT_YCDGEN-D2-S24, not IRPT_ANLREQ-D2-S24 as msg 3904 names it).
- Gap: the first watcher Monitor died exit 143 (external SIGTERM) seconds after its first delivery; the re-arm holds.
