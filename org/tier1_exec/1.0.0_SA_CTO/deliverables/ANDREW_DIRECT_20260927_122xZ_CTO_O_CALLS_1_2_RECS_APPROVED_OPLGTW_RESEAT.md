# ANDREW-DIRECT 2026-09-27 ~12:2xZ at the 1.0.0_SA_CTO~O terminal -- "recs approved"

**Verbatim:** "recs approved"

**What it answers:** the two cards of this seat's `/open-calls` at ~12:20Z (re-carded ~12:05Z after `2.0.0_SA_COO~O` measured the
laptop agentbus queue unconsumed, 5 held and 0 in flight, file 20260927T120052Z):

1. **CALL 1 (BLOCKING): re-seat NFRA_OPLGTW's CTO and CVO legs from the laptop to ~O -- REC yes. APPROVED.**
   This is the "Andrew's word, since ~A is not live" that `3.0.0_SA_CVO~O`'s verdict names as the un-park condition
   (`org/tier1_exec/3.0.0_SA_CVO/deliverables/cvoO_GOVERNANCE_VERDICT_SELF_DRIVE_O_D9_PROJECTS_20260926.md` @e470835e7c,
   lines 36-45: "a re-seat record for OPLGTW's CTO and CVO legs, in the same shape as @23bbeff325. It must carry a
   release from ~A's side, or Andrew's word, since ~A is not live to give one. It also updates `leads` in the same
   commit"; placement and fabric "go with the CTO's re-seat record"). The card's REC also carried the W3-S22 path:
   add `SPRINT_VIEW_ALLOWED_EMAILS` to the `deploy-to-ec2.sh:196` literal, then flip `sprint_view.py:172-174` fail-closed,
   in one release under a never-widen sign-off.
2. **CALL 2 (CARRIED): D9 as a whole moves to site Z -- REC (a) no. APPROVED: (a), D9 does not move;** the per-project
   placement fields carry placement.

## Acts, this seat

- The re-seat record: `org/missions/D9/NFRA/NFRA_OPLGTW/project.json` -- `leads.cto` 1.0.0_SA_CTO~A -> 1.0.0_SA_CTO~O,
  `leads.cvo` 3.0.0_SA_CVO -> 3.0.0_SA_CVO~O, `leads.coo` 2.0.0_SA_COO -> 2.0.0_SA_COO~O (the lane already running it),
  and `placement` LAPTOP -> SITEZ, `fabric` laptop -> site-z. It is committed with this record.
- Broadcast to `2.0.0_SA_COO~O` and `3.0.0_SA_CVO~O` (whose OPLGTW parks lift on this record), and to the laptop's
  `1.0.0_SA_CTO~A` and `0.0.0_AB_MSTR` by agentbus as notice; their queue is unconsumed, so it is notice, not a gate.
- W3-S22 is then ruled from this seat as OPLGTW's CTO, per the card's REC.
