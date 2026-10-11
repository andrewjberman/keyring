# ANDREW-DIRECT -- 2026-10-11 ~02:1xZ -- /self-drive 60m over EVERY dell2 project, re-armed after the hold lift

**Seat:** `1.0.0_SA_CTO~DELL2`. **Channel:** relayed, not heard at this terminal. Andrew spoke at the laptop
`1.0.0_SA_CTO` terminal; the words reached this seat as `0.0.0_AB_MSTR~DELL2` msg 3873 (bus 3279a489, laptop CTO msg
108173) and msg 3872 (bus cb13f851). Both source records were read here by `git show` at `cbcfdc0c1c`.

## His words, VERBATIM as recorded

Lift (record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261011_0xxxZ_LIFT_DELL1_DELL2_HOLD_ON_60M_PACING_KEEP_DRIVING_OFF.md`):

> lift the hold on dell1 and dell2, make sure my specifications are met on loop timing and /keep-driving OFF

Pacing (record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261010_23xxZ_SLOWER_PACING_LOOPS_60M_KEEP_DRIVING_OFF.md`):

> yeah we need slower pacing, i think canonical drive and self drive loops can be on 60m interval and /keep-driving OFF
> for now, no need to be so aggressive. This is to avoid the usage limit and try to scale productivity correctly.

> in govern loop too

The hold these lift: `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261010_211xZ_DELL2_POST_CRASH_CTO_ONLY_HOLD_HEAVY_DRIVE_OPS_DELL1_TOO.md`
@352fbe6093.

## What is re-armed

The scope and terms of `ANDREW_DIRECT_20261009_034xZ_SELF_DRIVE_30M_EVERY_DELL2_PROJECT_AND_DISCRETION_ON_THREE_ACTS.md`
@35fabf20c8 (his "run a /self-drive loop on 30m interval covering every single project on this fabric"), whose newest
log, `logs/2026-10-09/ctoDELL2_self_drive_dell2_every_project_tick27.md`, reads `state: ARMED`. The crash ended the
session cron; no stop was appended to that record. Only the cadence changes.

## ARM TERMS

| Term | Value |
|---|---|
| Scope | EVERY project placed on dell2, measured from `org/missions/D*/*/*/project.json` with `placement: DELL2` (50 scanned, 11 match; 10 `active`, 1 `closed` = IRPT_CUSTDY): ADVI_BILLING, ADVI_COTBKF, DSGN_IRPTV1, IRPT_ANLREQ, IRPT_BCKEND, IRPT_CUSTDY, IRPT_DASHBD, IRPT_YCDGEN, NFRA_OPSWKF, NFRA_TRNSPT, TCKT_VNEXT |
| Cadence | 60m (was 30m) |
| /keep-driving | OFF. Read at arm: `scan=off empty_tick=off` for dell2 |
| Call routing | /self-drive Step 1 (the driver rules; design forks to CRO; governance forks to `3.0.0_SA_CVO`) |
| Cited act list | only acts no seat can perform |
| paired_with | solo. Each COO runs `/canonical-drive` on its own project at 60m, armed by that seat |
| STOP-CONDITION | all in-scope projects `status: complete` (Step 4), HELD-AT-STOP, or Andrew's stand-down |

## Not decided here

- Which COO lanes are seated: the eight `claude.exe` processes (`~B2 ~C2 ~D2 ~G2 ~O2 ~P2 ~T2 ~V2`) launched 2026-10-10
  21:15Z have not registered. Seating is `0.0.0_AB_MSTR~DELL2`'s.
- dell2 is the model-policy control arm (lift record); this record changes no model.

-- 1.0.0_SA_CTO~DELL2
