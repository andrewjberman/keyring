# TCKT_MTADTA round 1 -- CTO rulings on rows D1-S4 (ListBucket) and D1-S5 (the collector as an invoker) (`1.0.0_SA_CTO~DELL1`, 2026-10-16 ~07:4xZ)

**Asked by:** `2.0.0_SA_COO~S1`, msg 6584. Drain-end packet:
`deliverables/2.0.0_SA_COO~S1/L8_DRAIN_END_PACKET_R1_20261016.md` (round 1 MAY-CLOSE, 5 of 5 merged @4d34045b07). Both rows are
open in `surprise-channel/investigations/INVESTIGATION_v1.md`, and both are owned by this seat.

## D1-S4: RULED option (ii). `s3:ListBucket` stays out of the bucket policy's Deny

- **The defect:** with ListBucket denied to every principal but the access role, the applying identity cannot refresh the bucket. Every later
  plan of the root fails, including the plan that would fix the policy. That is a lock-out only the root user could undo.
- **What a listing reveals, measured from the PRD's builder output (C-HOMES):** keys are `m365-metadata/trino/<tier>/<table>/date=<day>/<file>`.
  A listing shows table names, dates and object sizes. It shows no person, no address, no file name and no content.
- **What stays denied to everyone but the role:** every object data action (Get, Put, Delete and their variants). The KMS key policy admits
  the role alone, so an object copied out is still unreadable.
- **Conditions:**
  - (1) No key segment may ever carry a person, an address or an M365 file name. The partitions stay date-only. The door enforces this, and a
    builder change that adds a segment needs this seat's word.
  - (2) The FWD-8 statement names the listing plainly: who can list, and what a list shows.
  - (3) The release-act-1 apply order is unchanged: one apply, with the patch to `collector.tf` beside it.
- **Rejected:** option (i) (a two-stage apply) still locks out every later plan. Option (iii) (a named apply principal) contradicts Andrew's
  "only" and would need his word for no gain over (ii).

## D1-S5: RULED. The collector's execution role is the door's one named non-member invoker, write-only

- Andrew's 06:2xZ word: "only iam globgrph group can access, if you want to access you have to go through the reader/writer lambda". The
  collector does go through the door. It cannot be a group member, because a role is not a user.
- **Contract, as a PRD addendum at the round-1 analysis:**
  - the door's invokers are the group's members and the collector's execution role, named by its builder name;
  - the door's resource policy admits exactly those two;
  - the door gives the collector's identity `put` only, never a read.
- The FWD-8 statement lists the collector role among the paths. That is a residual, not a widening of who reads.

-- 1.0.0_SA_CTO~DELL1
