# Self-drive dell2-box, ticks 204-205 (1.0.0_SA_CTO~DELL2)

Arming record: org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_020xZ_SELF_DRIVE_DELL2_BOX_KEEP_DRIVING_ON.md
Window: 04:57Z to 05:57Z 2026-10-21.

## Acts and rulings (IRPT_ANLREQ)
- **TO-APPLY-TICKETREAD** CLOSED 2/0/0 (IB2 msg 11897). The simulation arms held before apply. Read here after: GetItem with no projection is implicitDeny. Y2 verified (msg 11902).
- **7I DLQ message:** G2 issued the delete to IB2 (msg 11903), and Y2 was told to stand down (one deleter). Deleted by handle; 9 -> 8 (IB2 msg 11910).
- **S249 cause** (G2 msg 11904):
  - prepare() built the YCharts vendor upload on the Opal path ("holdings row has no provider receipt");
  - the comparables reader expected key/label, which the catalogue lacks.
  - Fixes AR-g-182 and AR-g-183, plus the lead token.
- **r34r** CTO half SIGNED @255386b0c1 (blob fd5b51feaa). Six members change; the registry is unmoved. Condition: avoid the 06:00-06:55Z gateway window. Run 7J follows.

## Next
r34r install (IB2) -> run 7J Multi-Comp, with packager and audit outcomes named and the PDF saved for Andrew.

## Completion test
NOT DONE. TCKT_VNEXT is complete; IRPT_ANLREQ is in flight.

## Acts only Andrew can do (cited)
- 65a1, 544d, a392: recursive deletion / destructive git (CLAUDE.md Agent Autonomy).
- a331: internal all-firm entitlement for an outside-domain user (entitlement beyond his grants).
- 3ffe: admin-user delete of 4 synthetic cottonwood objects. The bucket fence is never edited.
- FWD-13..15 DONE WHEN confirmation (Andrew confirms DONE WHEN at L2).
- Andrew's read of the 42-page Overview sample against YCharts (FWD-9).

state: ARMED

## Compiler Tools
open-calls.py list; inbox read/; aws iam simulate-principal-policy; safe-commit.sh.
