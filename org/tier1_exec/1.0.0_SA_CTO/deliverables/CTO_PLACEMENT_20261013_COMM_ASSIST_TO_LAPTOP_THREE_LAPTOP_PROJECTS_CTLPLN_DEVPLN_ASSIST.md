# CTO placement ruling (L3) -- COMM_ASSIST moves from site Z to the laptop; the laptop runs three projects: NFRA_CTLPLN, NFRA_DEVPLN, COMM_ASSIST

From `1.0.0_SA_CTO` (laptop), 2026-10-13 ~14:5xZ.

## Andrew's words, VERBATIM

At the `4.0.0_SA_CRO` terminal ~14:4xZ (record
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261013_144xZ_MUSE_DECISIONS_AND_COMM_ASSIST_TO_LAPTOP.md` @356f0973f4):
"is COMM_ASSIST being handled on this box? I think it should be if it is not already. I want this box handling CTLPLN, DEVPLN, and
ASSIST, because I need to be overseeing them directly."

At the `1.0.0_SA_CTO` terminal ~14:4xZ: "we are going to need to /endpoint docs/briefs/nfra-devpln-per-box-portal-dev-approval-brief-20261013.md,
as this will be an additional project That run on the laptop box. The laptop should run the following three projects CTLPLN DEVPLN
and ASSIST. If there needs to be adjustments to any terraforms that cross over with sitez (e.g. in the case of ASSIST) we will cross
that bridge when we get to it on an ad hoc basis)"

## Ruling

1. **COMM_ASSIST placement SITEZ -> LAPTOP**, between rounds, in the tree row `org/missions/D9/COMM/COMM_ASSIST/project.json`
   (placement, fabric, placement_ruling, coo_lane, phase) and the derived index row. The 2026-10-09 ruling that sent it to site Z
   is superseded by his word above and retained in the row. D9 is a LAPTOP directive, so no directive placement changes.
2. **Handover from site Z**: `1.0.0_SA_CTO~Z` and `2.0.0_SA_COO~ZZ` finish nothing new on it; the open COMM_ASSIST acts on the
   site Z open-calls list (288f the channel @mention, 058e the colleague mail) stay Andrew's acts and are re-filed to the laptop
   list by this seat when site Z closes its rows on this record; the round-15 cells in flight drain where they are (spine scope
   clause: work in flight completes under its own spec), and the next round is issued from the laptop. `0.0.0_AB_MSTR` relays.
3. **Terraform that crosses site Z** (LDO-001's root `infra/aws/terraform/transcripts` is shared with NFRA_TRNSPT on dell2 and the
   gateway routes are NFRA_OPLGTW's on site Z): taken ad hoc on his word; each such apply is a targeted apply under a pair naming
   its overlap, as COMM_ASSIST's PRD S02 already says. The gateway stays site Z's.
4. **The muse midstream brief's L2 addendum** (`docs/briefs/comm-assist-through-muse-midstream-brief-20261013.md`) is this seat's
   now, not `1.0.0_SA_CTO~Z`'s; his four answers are all (a) with an efficacy outcome owed (the text fallback retires on a measured
   read of muse's efficacy, never a guess). Cross-box parts stand as ruled @2f0ed70e40.
5. **Seating -- three laptop COOs, his standing limit**: `2.0.0_SA_COO~C` (NFRA_CTLPLN, live); one lane for COMM_ASSIST now
   (`0.0.0_AB_MSTR` seats it); one lane for NFRA_DEVPLN after he confirms its DONE WHEN lines (@a9280cac15). The laptop's lent
   CloudOps lanes `~FBL`/`~ANL` stand down on the Dell read-backs (ruling @1161dc05fc) and are not counted here.
6. **NFRA_DEVPLN's endpoint is already emitted** at `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_DEVPLN_ENDPOINT_FORWARD_20261013.md`
   (@a9280cac15) and the project is registered under D0 on the laptop; his five rec approvals of ~14:3xZ are folded in.

## Acts

- `0.0.0_AB_MSTR`: relay this record to `1.0.0_SA_CTO~Z` / `2.0.0_SA_COO~ZZ` (handover) and seat the COMM_ASSIST laptop COO lane.
- `1.0.0_SA_CTO` (this seat): the COMM_ASSIST PRD addendum for muse (L2) next; NFRA_DEVPLN L4 on his DONE WHEN confirmation.
- Andrew: confirm or re-word the seven NFRA_DEVPLN DONE WHEN lines.
