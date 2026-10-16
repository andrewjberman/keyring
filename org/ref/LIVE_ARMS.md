# LIVE ARMS AND HOLDS -- the register

The only source of truth for live scoped loop arms and holds (org/XXX.md Step 1b-F points here). State, not law: it
lives outside the law lock because it changes as arms start and stop (Andrew-direct 2026-09-24 ~17:3xZ, record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260924_173xZ_XXX_MD_GUIDANCE_ONLY_NO_TEMPORAL_ITEMS.md`).
`1.0.0_SA_CTO` lands and strikes rows, naming the chooser and the record. A seat never writes its own row. On DONE the
lane deletes its cron and the row is struck; a struck row's record stays in git. A row absent here arms nothing.

## PACING -- governs every row below (Andrew-direct 2026-10-16 ~02:4xZ; before it, 2026-10-10 ~23:3xZ)

Every live CTO `/self-drive` (its box's open calls) and COO `/canonical-drive` (its assigned project) arm runs at **30m**,
whatever cadence its row names, and so does every re-arm. Andrew-direct ~02:4xZ 2026-10-16 at the laptop MSTR terminal,
VERBATIM: "ON, all CTO COO agents should now be on 30m loops for /self-drive {Each CTO adjudicates their box activities}
/canonical-drive {the project the COO is assigned}, respectively". Record
`org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261016_024xZ_KEEP_DRIVING_ON_30M_SELF_DRIVE_CANONICAL_DRIVE.md`
@def0cd29c2 (relayed by 0.0.0_AB_MSTR msg 109564). The cloud switch was re-set ON at 2026-10-16T02:42:55Z and read back
scan=on empty_tick=on. `/govern` was not named and stays at **60m**. Class DIRECTED, chooser Andrew; landed by 1.0.0_SA_CTO.
Superseded cadence, kept for history: every live `/canonical-drive`, `/self-drive` and `/govern` arm at 60m. `/keep-driving` is **ON** on all four boxes since 2026-10-13 20:34:07Z (cloud switch set by
0.0.0_AB_MSTR, read back scan=on empty_tick=on, no overrides) on Andrew-direct ~20:3xZ at the MSTR terminal, VERBATIM: "ON, 60m
loops for /self-drive, /canonical-drive, /govern for the relevant agents. CTOs on each box should have /self-drive loop on their
entire box, i.e. any open-calls that appears on that box they need to adjudicate." (relayed by 0.0.0_AB_MSTR msg 108887;
landed by 1.0.0_SA_CTO). Before that, OFF from 2026-10-10 23:33:52Z (set by 1.0.0_SA_CTO, read back scan=off empty_tick=off). VERBATIM: "yeah we need slower pacing, i think canonical drive and self drive loops can be on 60m
interval and /keep-driving OFF for now, no need to be so aggressive. This is to avoid the usage limit and try to scale
productivity correctly." then "in govern loop too". Record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261010_23xxZ_SLOWER_PACING_LOOPS_60M_KEEP_DRIVING_OFF.md`.
Class DIRECTED, chooser Andrew; landed by 1.0.0_SA_CTO. `/govern` fires on each box's first slot only: laptop `:00`, `~Z`
`:06`, `~DELL1` `:12`, `~DELL2` `:18`.

**30m from 2026-10-16 ~02:4xZ for `/self-drive` and `/canonical-drive`** (`/govern` is not named and stays 60m). Andrew-direct,
relayed by `0.0.0_AB_MSTR~DELL2` msg 8926, VERBATIM: "ON, all CTO COO agents should now be on 30m loops for /self-drive {Each CTO
adjudicates their box activities} /canonical-drive {the project the COO is assigned}, respectively". Record
`org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261016_024xZ_KEEP_DRIVING_ON_30M_SELF_DRIVE_CANONICAL_DRIVE.md` @def0cd29c2
(origin/box/laptop). Class DIRECTED, chooser Andrew. This line supersedes the 60m above for those two loops on every box. The dell2 rows are
landed by 1.0.0_SA_CTO~DELL2; each other box's CTO lands its own.

## Holds

- `2.0.0_SA_COO` (base): D2 off until Andrew lifts it.
- DSGN_REBRND: **CLOSED** by Andrew-direct ~20:1xZ 2026-10-06 at the `1.0.0_SA_CTO` terminal ("Yeah REBRND should be closed definitively."; record
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261006_201xZ_DSGN_REBRND_CLOSED_AND_RDP_DIRECTIONS.md`); no seat works it. Before that,
  `2.0.0_SA_COO~D`: STOPPED and HELD by Andrew-direct ~14:35Z 2026-10-06 at the `2.0.0_SA_COO~D` terminal, VERBATIM:
  "Stop work on REBRND", then "Any work on DSGN_REBRND from this point forward is on hold and not to be merged to the main branch
  unless I explicitly ask for it." Record: `org/missions/D13/DSGN/DSGN_REBRND/STATUS.md` "Open at Andrew" (@2ddf3afa91). Its light
  /market page is "kept off the main branch without explicit approval" (`org/tier1_exec/3.0.0_SA_CVO/deliverables/ANDREW_DIRECT_20261006_1414Z_LIGHT_MARKET_EXPERIMENT_OFF_MAIN_BRANCH.md`).
  DSGN_IRPTV1 is not stopped. Lifted only by his explicit word. Landed by 1.0.0_SA_CTO.

## Arms

- **Every COO lane seated on a non-terminal project, on every box: `/canonical-drive 60m` over its own project**, DIRECTED,
  chooser Andrew. Andrew-direct ~20:3xZ 2026-10-13 at the MSTR terminal, VERBATIM: "ON, 60m loops for /self-drive,
  /canonical-drive, /govern for the relevant agents" (relayed by 0.0.0_AB_MSTR msg 108887). Then at the `1.0.0_SA_CTO` terminal
  ~20:4xZ: "we need COO~C added to the live arms group, as well as any other active COO on the various boxes, so they can run
  canonical-drive properly". Lanes named at landing are measured from the project registers on CLOUD (28 active of 52) and the
  dell2 packet's seat list:
  - laptop: `2.0.0_SA_COO~C` (NFRA_CTLPLN), `~DV` (NFRA_DEVPLN), `~CA` (COMM_ASSIST);
  - dell1: `~B1` (ADVI_FIRMBKTS), `~K1` (ADVI_BDPRCE), `~R1` (AMGT_RESAPP), `~W1` (AMGT_HARVST), `~V1` (ETFS_RIVALS),
    `~D1` (MDPF_CANON), `~Q1` (MDPF_DEMQUE), `~M1` (MDPF_SECCLASS), `~G1` (MDPF_HEALGAP), `~S1` (MDPF_STRATID), `~H1` (MDPF_SECHIST);
  - dell2: `~Y2` (IRPT_ANLREQ), `~G2` (IRPT_YCDGEN), `~P2` (IRPT_BCKEND), `~D2` (IRPT_DASHBD), `~C2` (ADVI_COTBKF), `~T2`
    (NFRA_TRNSPT), `~V2` (TCKT_VNEXT);
  - site Z: `~O` (NFRA_OPLGTW), `~MP` (NFRA_MCPORTAL), `~MI` (NFRA_MCPINDEX).

  A COO lane seated later on an active project is covered by this row as written. A project the pivot PARKED (the
  direction packets, @4e963d4a12) or a CLOSED one does not drive: its lane stops at its drain. A lane may drive only its own
  project (Tier-2 seating). Stop: his stand-down. Landed by 1.0.0_SA_CTO.
- **Each box's CTO: `/self-drive 60m` over EVERY open call on its own box** (`python .tools/open-calls.py list` for that box;
  rule, escalate or hold each, per `/open-calls`), DIRECTED, chooser Andrew, Andrew-direct ~20:3xZ 2026-10-13 (PACING above).
  Lanes: `1.0.0_SA_CTO` (laptop, inside its cluster loop below), `1.0.0_SA_CTO~DELL1`, `1.0.0_SA_CTO~DELL2`, `1.0.0_SA_CTO~Z`.
  Each lane arms in its own session; `0.0.0_AB_MSTR` relays the word to the other boxes. Stop: his stand-down. Landed by
  1.0.0_SA_CTO.
- `1.0.0_SA_CTO` (laptop) **CLUSTER LEAD: `/loop 60m` over every box's open calls**, DIRECTED. Andrew at the laptop
  `1.0.0_SA_CTO` terminal ~03:2xZ 2026-10-11, VERBATIM: "I am also deputizing you as the leader of the entire cluster. What
  that means is that you should run a /loop to check the various /open-calls across the various boxes json uploads, and you
  adjudicate them. This loop should run every 60m." Body: `python .tools/open-calls.py list --all --cloud`, then a ruling
  per open row, relayed through `0.0.0_AB_MSTR`; rows Andrew reserved stay his. Record
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261011_032xZ_CTO_LEADS_CLUSTER_OPEN_CALLS_LOOP_60M.md`.
  Stop: his stand-down. Landed by 1.0.0_SA_CTO. RE-ARMED 2026-10-13 ~20:4xZ in the post-reboot session at 60m (keep-driving ON). The laptop `/self-drive` row below is NOT re-armed since the 2026-10-10 restart.
- `1.0.0_SA_CTO` `/self-drive 30m laptop directives` at `17,47 * * * *` (cron `a5054ca6`; 30m on Andrew ~06:0xZ 2026-10-09, "that should be much faster clip, like 30m"), DIRECTED: re-armed after the 2026-10-08 laptop reboot on
  Andrew's "1.) Yes." (~18:3xZ, last addendum of
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_153xZ_TWO_PRIORITIES_GITOPS_AND_PROCESS_GC.md`), terms of
  `ANDREW_DIRECT_20261007_071xZ_SELF_DRIVE_60M_LAPTOP_FABRIC_AS_CLUSTER_CONTROL_PLANE.md`; GitOps, GC and graph coherence
  ranked first each tick. Stop: as that record. Landed by 1.0.0_SA_CTO.
- `2.0.0_SA_COO~R` `/canonical-drive 30m COMM_ASSIST`, session cron `36340e72`, DIRECTED: Andrew ~03:5xZ 2026-10-09, VERBATIM "I see, yes
  run it on a 30m basis" (record `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261009_035xZ_COO_R_CANONICAL_DRIVE_30M_COMM_ASSIST.md`).
  Stop: the project closes, or his word. Landed by 1.0.0_SA_CTO on msg 107702. **STOPPED ~06:1xZ 2026-10-09:** Andrew took the seat
  offline ("I took COO~R offline because there wasnt really anything happening on that thread"); cron `36340e72` died with the session.

- Every fabric manager (`0.0.0_AB_MSTR`, `~Z`, `~DELL1`, `~DELL2`) `/govern 30m` at instantiation, DIRECTED. Andrew at the laptop
  `1.0.0_SA_CTO` terminal ~17:4xZ 2026-10-08, VERBATIM: "MSTR agents should have /govern on a 30m loop at instantiation." Record
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_174xZ_MSTR_GOVERN_30M_LOOP_AT_INSTANTIATION.md`. Supersedes
  the 60m interval in the `~DELL1` and `~DELL2` rows below. Stop: his stand-down. Landed by 1.0.0_SA_CTO.
  Minutes of the hour, DIRECTED (Andrew ~18:0xZ, verbatim in section 9 of
  `org/tier1_exec/4.0.0_SA_CRO~A/deliverables/PER_BOX_BRANCH_DESIGN_20261008.md`): laptop `0,30`, `~Z` `6,36`, `~DELL1` `12,42`,
  `~DELL2` `18,48`.

- `0.0.0_AB_MSTR~DELL1` `/govern 60m` DIRECTED (Andrew at the dell1 terminal ~07:08Z 2026-10-07, as relayed by `0.0.0_AB_MSTR` msg 106029 from bus
  4db364bf, VERBATIM as relayed: "Time to get to work, run /git-pull ajb_workspace, afterwards check sequence.yaml and directives.yaml and get
  to work on the projects assigned to you."; the `/govern 60m` arm is that fabric manager's own report of his act). Lanes it awarded:
  `2.0.0_SA_COO~M1` (MDPF_SECCLASS), `2.0.0_SA_COO~H1` (MDPF_SECHIST). He named no stop: his stand-down. Landed by 1.0.0_SA_CTO.
- DELL2, all rows from one record written by `0.0.0_AB_MSTR~DELL2`: `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261007_071xZ_DELL2_SEATING_CTO_SELF_DRIVE_COO_CANONICAL_DRIVE_MSTR_ARMS.md`
  @aed4552f74 (on origin CLOUD bd7cd8fb0a by `0.0.0_AB_MSTR` msg 106054). Landed by 1.0.0_SA_CTO; chooser Andrew except where said.
  - `0.0.0_AB_MSTR~DELL2` `/govern 60m` DIRECTED. His words at the dell1 terminal ~07:10Z, relayed on bus 900b6ce0, VERBATIM: "Also tell DELL2 to
    run the same /govern loop that you are running, with verbatim text and same 60m interval." Stop: his stand-down.
  - `0.0.0_AB_MSTR~DELL2` fast-forward `/git-pull` every 15m, and the Taildrop receive monitor: DIRECTED (was AUTHORITY-UNVERIFIED). The record's
    section 1 quotes the handoff he pasted as that session's first message: "Taildrop monitor is a standing arm at launch on this box." Both
    are session Monitors. Stop: his stand-down.
  - `1.0.0_SA_CTO~DELL2` `/self-drive 30m` over EVERY dell2 project (11: ADVI_BILLING, ADVI_COTBKF, DSGN_IRPTV1, IRPT_ANLREQ, IRPT_BCKEND,
    IRPT_CUSTDY until its close, IRPT_DASHBD, IRPT_YCDGEN, NFRA_OPSWKF, NFRA_TRNSPT, TCKT_VNEXT), DIRECTED. VERBATIM (2026-10-09 ~03:4xZ): "run a
    /self-drive loop on 30m interval covering every single project on this fabric". Arming record
    `ANDREW_DIRECT_20261009_034xZ_SELF_DRIVE_30M_EVERY_DELL2_PROJECT_AND_DISCRETION_ON_THREE_ACTS.md` @35fabf20c8; it supersedes the 10-07 60m and
    10-08 30m seven-project records. Stop: all in-scope projects complete, HELD-AT-STOP, or his stand-down.
  - `/canonical-drive <own project>`, CHOSEN: each seat accepts Andrew's recommendation, VERBATIM: "I also recommend that when you bring on the
    COOs, they should have /canonical-drive on their respective projects." He named no interval and no stop; "recommend" is his word and
    this row does not convert it into an order. Seven seats: `2.0.0_SA_COO~K2` IRPT_CUSTDY (STRUCK 2026-10-09 ~04:4xZ: IRPT_CUSTDY merged into IRPT_DASHBD, CTO ruling @ca5f74553d, handover @185805a565); `2.0.0_SA_COO~C2` ADVI_COTBKF;
    `2.0.0_SA_COO~P2`, `2.0.0_SA_COO~Y2`, `2.0.0_SA_COO~M2` IRPT_BCKEND (workstreams P, Y, M); `2.0.0_SA_COO~G2` IRPT_YCDGEN;
    `2.0.0_SA_COO~D2` IRPT_DASHBD. Cadence is each seat's to state in its own first tick; stop when its project reads complete, at
    HELD-AT-STOP, or on his stand-down.
  - RELAUNCH 2026-10-11 after the dell2 crash and hold lift (record
    `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261011_0xxxZ_LIFT_DELL1_DELL2_HOLD_ON_60M_PACING_KEEP_DRIVING_OFF.md` @cbcfdc0c1c).
    THESE TERMS ARE CURRENT. Landed by 1.0.0_SA_CTO~DELL2.
    - `1.0.0_SA_CTO~DELL2` `/self-drive 60m` over every dell2 project, DIRECTED, chooser Andrew. Arming record
      `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261011_021xZ_SELF_DRIVE_60M_EVERY_DELL2_PROJECT_REARM_AFTER_HOLD_LIFT.md`
      @86d65d0c3e. It carries the 10-09 row's scope and stop at the 60m cadence.
    - `/canonical-drive <own project>` 60m, CHOSEN (the recommendation above; the cadence is his 2026-10-10 pacing word). Six seats, named
      by 1.0.0_SA_CTO~DELL2 msg 3875 and seated by `0.0.0_AB_MSTR~DELL2` msg 3877: `2.0.0_SA_COO~C2` ADVI_COTBKF, `2.0.0_SA_COO~D2`
      IRPT_DASHBD, `2.0.0_SA_COO~G2` IRPT_YCDGEN, `2.0.0_SA_COO~P2` IRPT_BCKEND, `2.0.0_SA_COO~T2` NFRA_TRNSPT, `2.0.0_SA_COO~V2` TCKT_VNEXT.
      `~M2` was not relaunched. Stop: the seat's project reads complete, HELD-AT-STOP, or his stand-down.
      STRUCK 2026-10-14 ~17:4xZ for `~V2` only, by 1.0.0_SA_CTO~DELL2 on `~V2` msg 7786: TCKT_VNEXT folded into IRPT_ANLREQ (round-17
      analysis @0a18c286a5) and `~Y2` issues every ticket cell. `~V2` deletes its 60m cron and is re-seated by `~Y2` naming it in an order.
      RE-SEATED 2026-10-14 ~18:5xZ by 1.0.0_SA_CTO~DELL2: `2.0.0_SA_COO~V2` `/canonical-drive` 60m over TCKT_VNEXT FWD-10 (Trade Request)
      and FWD-11 (Meeting Request), due 2026-10-24. Class: CHOSEN by this seat on Andrew-direct ~18:3xZ (call 2 DECLINED: "DELL2 has the
      capacity to manage it"; record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261014_183xZ_FIVE_CALLS_ANSWERED_AND_BD_ASOF_CITATION.md`),
      cadence per his 2026-10-10 pacing word. Stop: FWD-10 and FWD-11 read REALIZED, HELD-AT-STOP, or his stand-down.
      STRUCK 2026-10-14 ~18:5xZ for `2.0.0_SA_COO~C2` (ADVI_COTBKF) by 1.0.0_SA_CTO~DELL2: the project moves to dell1 now
      (Andrew-direct ~18:5xZ, "devote DELL1 wholly to ADVI/MDPF work", record
      `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261014_185xZ_DELL1_WHOLLY_ADVI_MDPF_AMGT.md`); its loop is dell1's to seat.
      ADDED 2026-10-15 ~01:1xZ by 1.0.0_SA_CTO~DELL2: IRPT_DASHBD splits into four workstreams at round 114, DIRECTED on Andrew's "Go on"
      (`org/tier1_exec/4.0.0_SA_CRO/deliverables/IRPT_DASHBD_PARALLELIZATION_ASSESSMENT_20261014.md` ADDENDUM 1; ruling
      `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md`). `/canonical-drive`
      60m each, scoped to its workstream: `2.0.0_SA_COO~D2` B-49F+contract (continues), `2.0.0_SA_COO~C2` B-CW Cottonwood (re-tasked on
      dell2), `2.0.0_SA_COO~I2` B-IN Inflection (new), `2.0.0_SA_COO~F2` F-SHIP (new). Stop: the workstream's outcomes REALIZED,
      HELD-AT-STOP, or his stand-down.
    - `2.0.0_SA_COO~Y2` `/canonical-drive` 60m over IRPT_BCKEND workstream Y, and IRPT_ANLREQ as its interim driver (CVO verdict msg 1889),
      CHOSEN. Seating asked of `0.0.0_AB_MSTR~DELL2` by 1.0.0_SA_CTO~DELL2 at ~02:27Z on `2.0.0_SA_COO~G2` msg 3899 (IRPT_YCDGEN FWD-1 waits on
      a workstream-Y re-cut). Same stop.
    - `2.0.0_SA_COO~D2` `/canonical-drive` 60m over DSGN_IRPTV1 as a SECOND project beside IRPT_DASHBD, CHOSEN, lease FULL (no FAST
      lease: none is armed without Andrew's word). Ruled by 1.0.0_SA_CTO~DELL2 ~05:1xZ in
      `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_DSGN_IRPTV1_FROM_WATERMARK_20261002_20261011.md` section 2; no new seat.
      Stop: DSGN_IRPTV1 reads complete, HELD-AT-STOP, or his stand-down.
    - `2.0.0_SA_COO~G2` also holds IRPT_ANLREQ WORKSTREAM G (the resident release 4: AR-g-21 to AR-g-23), under its existing
      `/canonical-drive` 60m loop, CHOSEN. Ruled by 1.0.0_SA_CTO~DELL2 ~06:1xZ on `2.0.0_SA_COO~G2` msg 4247: the lane issued that
      workstream before the crash, and its write surface is disjoint from `2.0.0_SA_COO~Y2`'s. No new seat. Same stop.
    - **DELL2 COO SET AT 30m, ADDED 2026-10-16 ~02:4xZ by 1.0.0_SA_CTO~DELL2** on the 30m word above. Each seat runs `/canonical-drive 30m`
      over the scope the parallelization ruling gives it
      (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_PARALLELIZE_WORKSTREAM_ASSIGNMENTS_20261015.md` @1a39b02d2e, on
      Andrew's "lets do that", record `ANDREW_DIRECT_20261015_231xZ_PARALLELIZE_IRPT_SUITE_GO.md`). This row supersedes the 60m cadence
      of every dell2 COO row above; their scopes stand where this row does not restate them. Eleven seats:
      - `2.0.0_SA_COO~Y2`: IRPT_ANLREQ (FWD-1 thread, interim driver);
      - `2.0.0_SA_COO~G2`: IRPT_ANLREQ workstream G (engine, brand, releases);
      - `2.0.0_SA_COO~T2`: IRPT_ANLREQ workstream TX (FWD-4/5);
      - `2.0.0_SA_COO~V2`: TCKT_VNEXT (FWD-10/11);
      - `2.0.0_SA_COO~P2`: IRPT_BCKEND holdings;
      - `2.0.0_SA_COO~N2`: IRPT_BCKEND Inflection feeds;
      - `2.0.0_SA_COO~S2`: IRPT_BCKEND export, routes and serve path;
      - `2.0.0_SA_COO~D2`: IRPT_DASHBD B-49F plus the contract (and DSGN_IRPTV1, as above);
      - `2.0.0_SA_COO~C2`: IRPT_DASHBD B-CW Cottonwood;
      - `2.0.0_SA_COO~I2`: IRPT_DASHBD B-IN Inflection;
      - `2.0.0_SA_COO~F2`: IRPT_DASHBD F-SHIP.
      `1.0.0_SA_CTO~DELL2` `/self-drive 30m` over the dell2 box (arming record
      `ANDREW_DIRECT_20261015_020xZ_SELF_DRIVE_DELL2_BOX_KEEP_DRIVING_ON.md`, cadence change @9bfb404220). Stop: the scope's outcomes
      REALIZED, HELD-AT-STOP, or his stand-down.
    - Not seated: `2.0.0_SA_COO~B2` ADVI_BILLING and `2.0.0_SA_COO~O2` NFRA_OPSWKF (both WAITING in `sequence-check` on Andrew's inputs).
  - No row: the Microsoft Defender CPU sampling Monitor (record section 5). He asked that seat to "keep an eye"; it is a watch, not a loop.


- `2.0.0_SA_COO~C` on NFRA_CTLPLN ONLY (Andrew-direct ~06:1xZ 2026-10-07 at the `1.0.0_SA_CTO` terminal, VERBATIM: "bring COO~C on for
  this purpose. COO~C should only be focused on this work, not cottonwood backfill project."). Record
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_061xZ_PROCEED_NFRA_CTLPLN_COO_C_ON_IT_ONLY_NOT_COTBKF.md`. He named no
  loop and no cadence: event-driven, NO cron. Landed by 1.0.0_SA_CTO.

- RELAUNCH 2026-09-28 (Andrew-direct ~17:3xZ, record
  `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20260928_173xZ_RELAUNCH_CTO_COO_DYPM_CANONICAL_DRIVE_D_CLOSER_CRO_UIWALK.md`;
  placement `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_PLACEMENT_20260928_174xZ_RELAUNCH_CANONICAL_DRIVE_PMY_CLOSER_D.md`).
  Class DIRECTED, chooser Andrew; landed by 1.0.0_SA_CTO. The comp-tool rail stays on.
  - `2.0.0_SA_COO~D` `/canonical-drive 10m` over DSGN_IRPTV1; the FAST lease (`org/mcp/drive-mode.log`, surface
    `portal/src/pages/InvestorReporting`) routes each tick to `/closer-drive`. Stop: Andrew's stand-down; a lapse to
    FULL keeps the loop on the canonical body.
  - `2.0.0_SA_COO~P`, `~M`, `~Y` `/canonical-drive 10m`, each over its own IRPT_BCKEND workstream (the contract's
    writer table is the split), leases FULL. First act is the closer hand-back freeze (placement act 3); the loop
    skips the row until the CTO removes `closer_contract` (act 5). Stop: IRPT_BCKEND `status: closed`, or Andrew's
    stand-down.
  - `4.0.0_SA_CRO` `/ui-walk` runs plus Andrew's transcripts, ad hoc, NO cron; findings to 1.0.0_SA_CTO and
    2.0.0_SA_COO~D.
- `1.0.0_SA_CTO~Z` `/self-drive 30m` over every open call on site Z, DIRECTED, chooser Andrew (~02:4xZ 2026-10-16, relayed by
  `0.0.0_AB_MSTR~Z` msg 34667, VERBATIM: "ON, all CTO COO agents should now be on 30m loops for /self-drive {Each CTO adjudicates
  their box activities} /canonical-drive {the project the COO is assigned}, respectively"). Arming record
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_30M_SITEZ_BOX_OPEN_CALLS.md`. Stop: his
  stand-down. Landed by 1.0.0_SA_CTO~Z. The same word takes the site Z COO row below to 30m.
- `2.0.0_SA_COO~O` (NFRA_OPLGTW), `~MI` and `~MI2` (NFRA_MCPINDEX), `~MP` (NFRA_MCPORTAL): `/canonical-drive <own project>` (60m, now 30m per the row above),
  DIRECTED, chooser Andrew. ~02:0xZ 2026-10-16 at the `1.0.0_SA_CTO~Z` terminal, VERBATIM: "time to get back on the mission, we need
  the MCPINDEX OPLGTW MCPORTAL COO teams backonline and moving". Record
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_020xZ_MCPINDEX_OPLGTW_MCPORTAL_COO_TEAMS_BACK_ONLINE.md`. Seated by
  `0.0.0_AB_MSTR~Z`. Stop: the project closes, HELD-AT-STOP, or his stand-down. Landed by 1.0.0_SA_CTO~Z.
- ~~`1.0.0_SA_CTO~O` `/self-drive 30m`~~ STRUCK 2026-10-09 ~07:4xZ by `1.0.0_SA_CTO~Z`: Andrew-direct "we don't need CTO~O
  anymore, you just lead the fabric here" (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_074xZ_CTO_O_RETIRED_CTO_Z_LEADS_SITEZ_FABRIC.md`).
  The COO half below is not touched by that word. Original row: `1.0.0_SA_CTO~O` `/self-drive 30m` over NFRA_OPLGTW, NFRA_OPALAI, NFRA_MCPORTAL, NFRA_MCPINDEX, paired with
  `2.0.0_SA_COO~O` / `~MI` / `~MP` / `~AI` `/canonical-drive <own project> 30m` (+15m). Class DIRECTED, chooser Andrew
  (his `/self-drive` invocation, 2026-09-28 ~22:2xZ); landed by 1.0.0_SA_CTO~O. Record
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_222xZ_SELF_DRIVE_O_FABRIC_FOUR_PROJECTS.md`. Stop:
  all four `status: complete`, HELD-AT-STOP, or Andrew's stand-down.
- `1.0.0_SA_CTO~Z` `/self-drive 60m` over the site-Z NFRA projects whose CTO is this seat: NFRA_SPRINTWIN, NFRA_IAMROLES202609,
  NFRA_OPSEC202609, NFRA_REPORT, NFRA_MCPMSP, NFRA_MCPORTAL, NFRA_OPALAI, NFRA_MCPINDEX (not NFRA_OPLGTW: `1.0.0_SA_CTO~O`).
  Class DIRECTED, chooser Andrew: ~04:3xZ 2026-10-09 at the `1.0.0_SA_CTO~Z` terminal, VERBATIM in part: "Do you have self-drive
  running? ... that should entirely be covered between the CTO self-drive and the MSTR govern loops." Arming record
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_043xZ_SELF_DRIVE_60M_SITEZ_NFRA_AND_PUSHES_NEED_NO_ANDREW.md`.
  Stop: DONE read from the register for all eight, HELD-AT-STOP, or his stand-down. Landed by 1.0.0_SA_CTO~Z.
  **STRUCK 2026-10-09 ~06:1xZ by `1.0.0_SA_CTO~Z`, STOPPED-BY-OPERATOR:** "No im winding down this fabric, take a /log on current
  status". Cron deleted. A successor does not re-arm this row.
- `1.0.0_SA_CTO~Z` `/self-drive 30m` over every non-terminal project placed on site Z (re-read each tick; 9 at arm, NFRA_OPLGTW
  included). Class DIRECTED, chooser Andrew: ~07:3xZ 2026-10-09 at the laptop MSTR terminal, VERBATIM in part: "cto needs to be
  running /self-drive on 30m interval covering all projects on sitez box" (relay msg 32505). Arming record
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_074xZ_SELF_DRIVE_30M_EVERY_SITEZ_PROJECT.md`. Paired with
  every site-Z COO lane's `/canonical-drive <own project>` on the same word. Stop: all in-scope projects `status: complete`,
  HELD-AT-STOP, or his stand-down. Landed by 1.0.0_SA_CTO~Z.
- `1.0.0_SA_CTO~Z` `/self-drive 60m` over AMGT_CORPUS, AMGT_HARVST, AMGT_RESAPP, DSGN_AMGTV1, ETFS_RIVALS (the
  Friday demo: PROD by 09:00 ET 2026-10-02). The driver adjudicates every open call; CRO~Z runs `/closer trace` on
  request. Paired with `2.0.0_SA_COO~X` / `~Z` / `~H` / `~D` running `/canonical-drive <own project> 30m`; `~RV`
  unchanged. Class DIRECTED, chooser Andrew (2026-10-01 ~04:0xZ, armed on the CRO~Z brief 04:14Z); landed by
  1.0.0_SA_CTO~Z. Record
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_040xZ_SELF_DRIVE_60M_AMGT_FOUR_PLUS_ETFS_RIVALS_ARM_ON_CRO_BRIEF.md`;
  placement `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_PLACEMENT_20261001_043xZ_AMGT_FRIDAY_DEMO_RESTRUCTURE.md`.
  Stop: DONE read from the register, HELD-AT-STOP (never for AMGT_HARVST), or Andrew's stand-down.
  - RELAUNCH 2026-10-02: the ~04:0xZ disk wind-down stopped this loop (cron `100fd3c2` deleted). Andrew re-armed it with
    "go" at ~04:55Z. That word answered a relaunch question whose context named this row. Two more words followed at
    ~04:57Z and ~04:59Z. Re-arm record:
    `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261002_045xZ_SELF_DRIVE_60M_AMGT_FRIDAY_RELAUNCH.md`.
    Source records are in `org/tier0_exec/0.0.0_AB_MSTR/deliverables/`:
    `ANDREW_DIRECT_20261002_045xZ_GO_RELAUNCH_SITEZ_AMGT_DEMO_FLEET.md`,
    `ANDREW_DIRECT_20261002_045xZ_RV_TEAM_ETFS_RIVALS_ADJUDICATION_AND_EGRESS_TONIGHT.md` and
    `ANDREW_DIRECT_20261002_045xZ_CANONICAL_DRIVE_ALL_COOS_RV_CLOSER_DRIVE_RIVALFUNDS_DEMOABLE_TODAY.md`. Relay: MSTR~Z
    msg 28199. Class DIRECTED, chooser Andrew; landed by 1.0.0_SA_CTO~Z. These terms replace the terms above where
    they differ:
    - ETFS_RIVALS open calls are adjudicated by `4.0.0_SA_CRO~RV`, not by this driver. Verbatim: "CRO~RV has
      adjudication ability for any open calls on the ETFS_RIVALS. CTO~Z has adjudication ability for the rest of the
      fabric."
    - `2.0.0_SA_COO~RV` drives ETFS_RIVALS on `/closer-drive` under a FAST lease (`/drive-mode`), prioritized, as one
      team with `3.0.0_SA_CVO~RV` and `4.0.0_SA_CRO~RV`. Goal, verbatim: "i want mcp.opalinvest.dev/rivalfunds demoable
      Today". Stop: ETFS_RIVALS DONE in the register, or Andrew's stand-down. This replaces "`~RV` unchanged".
      - **~14:1xZ addendum (Andrew-direct at the `4.0.0_SA_CRO~RV` terminal, record
        `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261002_141xZ_RIVALFUNDS_UI_WALK_BRIEF_TO_CTO_COO_RV_CANONICAL_DRIVE.md`),
        VERBATIM:** "I also want COO~RV to dramaticaly uptick its efforts, so I suggest /canonical-drive with max
        parallelization on subagents."
        - The FAST lease ENDED at 14:40:14Z, ended by `2.0.0_SA_COO~RV` (`org/mcp/drive-mode.log` END line; `drive-mode.py
          status` reads 0 live leases at 15:01Z), not at its 17:08:53Z expiry. From then, `2.0.0_SA_COO~RV` drives
          ETFS_RIVALS on `/canonical-drive` FULL, with fan-out at the cap the decomposition's chains allow (spine L6
          `fanout:`).
        - "Suggest" is relayed as written; this row does not convert it into an order.
        - Its work list is round 6 plus the 33-item walk register, PRD v0.12 @afc2bed44f.
        - Stop: ETFS_RIVALS DONE, or Andrew's stand-down. Landed by 1.0.0_SA_CTO~Z.
    - `2.0.0_SA_COO~X` / `~Z` / `~H` / `~D` each arm `/canonical-drive <own project> 30m`, on "Make sure
      /canonical-drive loops are running for all COOs on their respective projects".
    - Egress, verbatim: "All agents have any egress they need to run their operations tonight." It is recorded as
      written. This row does not decide how "tonight" or "the rest of the fabric" bound.
  - RELAUNCH 2026-10-04 after the SentinelOne crash (shutdown 18:58:20Z). Andrew answered "Restart the AMGT drive
    loops?" with "2.) Yes" at ~19:4xZ, record
    `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261004_194xZ_RELAUNCH_COO_O_CVO_O_RESTART_AMGT_DRIVE_LOOPS.md`
    @3166fec43e. Re-arm record:
    `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261004_194xZ_SELF_DRIVE_60M_AMGT_FRIDAY_RESTART_AFTER_SENTINELONE_CRASH.md`.
    Class DIRECTED, chooser Andrew; landed by 1.0.0_SA_CTO~Z. The terms above carry unchanged. Each paired seat re-arms
    its own loop (MSTR~Z relays). `2.0.0_SA_COO~RV` stays on `/canonical-drive` FULL.
  - RELAUNCH 2026-10-07 after the site-Z reboot. THESE TERMS ARE CURRENT and replace the terms above where they differ.
    Andrew-direct ~08:2xZ at the `0.0.0_AB_MSTR~Z` terminal, VERBATIM: "CTO should have a self-drive loop on the fabric
    as a whole running  on the hourly basis. Research needs should go to CRO as needed for additional clarity. all COOs
    should have /canonical-drive running on their respective projects." Source record
    `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261007_082xZ_SITEZ_RELAUNCH_CTO_Z_AMGT_FABRIC_RV_SELF_DRIVE_HOURLY_CANONICAL_DRIVE.md`
    @8bd783d51f; relay MSTR~Z msg 30718. Arming record
    `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_082xZ_SELF_DRIVE_60M_SITEZ_FABRIC_RELAUNCH_AFTER_REBOOT.md`
    @d97558efe8. Class DIRECTED, chooser Andrew; landed by 1.0.0_SA_CTO~Z.
    - `1.0.0_SA_CTO~Z` `/self-drive 60m`. The selector is spelled as the same five projects; the row does not decide
      whether "the fabric as a whole" is wider (the arming record names the wider spelling).
    - `2.0.0_SA_COO~X` / `~H` / `~Z` / `~D` / `~RV` `/canonical-drive <own project>`. He named no cadence; each COO arms
      its own loop.
    - `3.0.0_SA_CVO~RV` is the ETFS_RIVALS validator; `3.0.0_SA_CVO~Z` and `4.0.0_SA_CRO~Z` are general fabric
      resources. `4.0.0_SA_CRO~RV` was not relaunched, so the driver rules ETFS_RIVALS calls until he says otherwise.
    - The "Friday demo" goal text is not in his word of today and is not carried.
    - Stop: DONE read from the register, HELD-AT-STOP (never for AMGT_HARVST), or Andrew's stand-down.
    - **STRUCK 2026-10-09 ~02:0xZ by `1.0.0_SA_CTO~Z`, STOPPED-BY-OPERATOR.** Andrew moved all five projects to DELL1 (records
      `ANDREW_DIRECT_20261008_225xZ_AMGT_DSGN_RIVALS_TO_DELL1_AFTER_ROUND_CLOSE_AND_BBG_CENSUS.md` @b7361ceb2a and
      `ANDREW_DIRECT_20261009_014xZ_RESAPP_BBG_ASKS_VIA_BACKFILL_QUEUE_NO_UNBLOCK_NEEDED.md` @0953984a75: "those agents are on DELL1
      now, thats where they can work"). The cron is deleted. The site-Z COO rows above are void for the five projects, whose seats
      are dell1's. A successor does not re-arm this row.
- DELL1 (Andrew-direct ~07:15Z 2026-10-07 at the `0.0.0_AB_MSTR~DELL1` terminal, relayed as msg 1, VERBATIM: "Bring CTO online
  with instructions to run /self-drive on the underlying COOs projects with a 60m interval. Furthermore, the COOs should be running
  /canonical-drive on their projects."). Record
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_0715Z_SELF_DRIVE_60M_MDPF_SECCLASS_MDPF_SECHIST_DELL1.md`.
  Class DIRECTED, chooser Andrew; landed by 1.0.0_SA_CTO~DELL1. Stop: both projects `status: complete`, HELD-AT-STOP, or his stand-down.
  - `1.0.0_SA_CTO~DELL1` `/self-drive 60m` over MDPF_SECCLASS, MDPF_SECHIST, MDPF_HEALGAP. Paused 2026-10-07 ~22:3xZ on his word;
    RE-ARMED 2026-10-08 ~17:5xZ on Andrew-direct at the dell1 CTO terminal, VERBATIM: "Yes rec approved, please proced" (the card named
    all three projects), record @2a728669cf.
  - EXTENSION (MDPF_HEALGAP, paired with `2.0.0_SA_COO~G1` `/canonical-drive 60m`): first landed 2026-10-07 ~08:4xZ as
    AUTHORITY-UNVERIFIED; re-classed DIRECTED on the 2026-10-08 ~17:5xZ word above. Cadence 10m -> 60m on Andrew-direct ~18:5xZ
    2026-10-08 at the `2.0.0_SA_COO~G1` terminal, VERBATIM: "Ok lets slow that down to 60 min" (class DIRECTED, chooser Andrew; G1
    msg 1057, cron ae79a828 at :07).
  - `2.0.0_SA_COO~M1` `/canonical-drive MDPF_SECCLASS` and `2.0.0_SA_COO~H1` `/canonical-drive MDPF_SECHIST`. He named no cadence,
    so each uses the skill's 10m DIRECTED own-project default.
  - The `/govern` arms of the two fabric managers are the two DIRECTED rows at the top of this section.
  - Re-classes the AUTHORITY-UNVERIFIED row that 1.0.0_SA_CTO landed @e37552ef87, which is folded into this row.
  - `3.0.0_SA_CVO` (base, dell1) runs these seats' surprise channels ad hoc, with NO cron.
- `2.0.0_SA_COO~A` `/drive` NFRA_CLDGRPH to CLOSED:
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260910_171xZ_CLDGRPH_HOLDS_OFF_WRAP_IT_UP.md`.
- `2.0.0_SA_COO~X` `/drive` NFRA_C3MATERIALIZE:
  `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260828_050xZ_COOX_DRIVE_LOOP_NFRA_C3MATERIALIZE.md`.
- `1.0.0_SA_CTO` `/self-drive 60m laptop directives` DIRECTED (Andrew-direct 2026-10-07 ~07:1xZ, typed at this seat as the invocation, VERBATIM:
  "[60m] <Run the laptop fabric as the control plane of the cluster. Manage and adjudicate requests as needed.>"). Record
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_071xZ_SELF_DRIVE_60M_LAPTOP_FABRIC_AS_CLUSTER_CONTROL_PLANE.md`. Chooser Andrew;
  landed by 1.0.0_SA_CTO. Solo: no COO loop is armed by it. Stop: DONE read from the register, HELD-AT-STOP, or his stand-down.
- `1.0.0_SA_CTO` `/self-drive MDPF_TAXSMA,NFRA_OPLGTW,LGIC_NAMING,LGIC_ENFORCE,LGIC_CANON` -- PAUSED by the managed
  wind-down, resume authority:
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260915_193xZ_COO_GOALS_AND_CTO_SELF_DRIVE_ADJUDICATES.md`.
- `1.0.0_SA_CTO` fallback adjudicator for LGIC_LGCTFM's `ANDREW_CARD.md` when Andrew is unavailable (one artifact,
  nothing wider): `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260917_23xxZ_CTO_ADJUDICATES_LGCTFM_ANDREW_CARD_IF_ANDREW_UNAVAILABLE.md`.
- SITE-Z only: `3.0.0_SA_CVO~Z` SYSPARITY cron (`org/tier0/ledger/LD-0318.md`, LD-0319); `4.0.0_SA_CRO~W` harvest remediation loop
  (`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260915_HARVEST_REMEDIATION_LOOP_W.md`; the collection
  mechanism and cadence RESERVED to Andrew).

## Struck

- `1.0.0_SA_CTO` `/self-drive 60m laptop directives` (record `ANDREW_DIRECT_20261002_050xZ_SELF_DRIVE_60M_LAPTOP_DIRECTIVES_ADJUDICATE_ALL_KEEP_COOS_FLOWING.md`):
  struck 2026-10-07 by 1.0.0_SA_CTO. Chooser Andrew: his 2026-10-07 ~07:1xZ invocation re-arms the same scope with new terms (the row above). A
  successor does not re-arm the 2026-10-02 row.

- `2.0.0_SA_COO~C` `/canonical-drive ADVI_COTBKF` (record `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261006_201xZ_ADVI_COTBKF_CANONICAL_DRIVE.md`
  @45b266dcdb): struck 2026-10-07 by 1.0.0_SA_CTO. Chooser Andrew: "COO~C should only be focused on this work, not cottonwood backfill
  project." (record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_061xZ_PROCEED_NFRA_CTLPLN_COO_C_ON_IT_ONLY_NOT_COTBKF.md`).
  He named no successor seat for ADVI_COTBKF; nothing here decides one. A successor does not re-arm this row.

- `2.0.0_SA_COO~C` `/closer-drive` over NFRA_CTLPLN (record `ANDREW_DIRECT_20261006_144xZ_SEAT_COO_C_NFRA_CTLPLN_CLOSER_DRIVE.md`):
  struck 2026-10-06 by 1.0.0_SA_CTO on its own stop condition, "round 1 graded by the CVO": FWD-5, FWD-2, FWD-8 and FWD-7 all PASS
  (3.0.0_SA_CVO @ec24439bc0, @4e6b82af13, @a69d29a7b0). FAST lease ended (FULL). Round 2 needs dell1; a successor does not re-arm
  this row.

- `1.0.0_SA_CTO` `/self-drive 60m laptop directives` (record `ANDREW_DIRECT_20261001_042xZ_SELF_DRIVE_60M_LAPTOP_FABRIC_FINAL_SAY_CLOSER_DRIVE_IRPT_FIRST.md`):
  struck 2026-10-02 by 1.0.0_SA_CTO. Chooser Andrew: his 2026-10-02 ~05:0xZ word re-arms the same scope at 60m with new terms (the row
  above). A successor does not re-arm the 2026-10-01 row.

- `1.0.0_SA_CTO` `/self-drive 30m laptop directives` (record `ANDREW_DIRECT_20260928_230xZ_SELF_DRIVE_LAPTOP_FABRIC.md`):
  struck 2026-10-01 by 1.0.0_SA_CTO. Chooser Andrew: his 2026-10-01 ~04:2xZ word re-arms the same scope at 60m with new
  terms (the row above). A successor does not re-arm the 30m row.

- SITE-Z `1.0.0_SA_CTO~Z` `/self-drive 30m` "AMGT fabric ops" (record
  `ANDREW_DIRECT_20260929_183xZ_SELF_DRIVE_AMGT_FABRIC_OPS.md`). Struck 2026-10-01 by `1.0.0_SA_CTO~Z`: the 09-30 wind-down
  for the reboot cancelled its crons, and Andrew's 2026-10-01 ~04:0xZ `/self-drive 60m` row above supersedes it.
- SITE-Z `1.0.0_SA_CTO~Z` `/self-drive 30m` AMGT + DSGN_AMGTV1 with its COO pairs (record
  `ANDREW_DIRECT_20260928_220xZ_SELF_DRIVE_AMGT_AND_DSGN_AMGTV1.md`). Struck 2026-09-29 by `1.0.0_SA_CTO~Z`. The 11:34 ET
  crash ended the arm and it was never re-armed. Andrew's post-crash word of ~18:3xZ is the new AMGT arm above. A
  successor does not re-arm the struck row.

- SITE-Z `1.0.0_SA_CTO~Z` `/self-drive AMGT_RESAPP & POSN_ASTTAX` 30m, `2.0.0_SA_COO~Z` `/drive` POSN_ASTTAX 10m and
  `2.0.0_SA_COO~ZZZ` `/drive` AMGT_RESAPP 10m (record
  `ANDREW_DIRECT_20260911_222xZ_COO_DRIVE_10M_CANONICAL_FLOW_STAGE_CHECK_AND_REBRAND.md`): struck 2026-09-28 by
  `1.0.0_SA_CTO~Z`. POSN_ASTTAX is CLOSED; the site-Z reboot relaunched every seat with zero crons (record
  `ANDREW_DIRECT_20260928_195xZ_SITEZ_AMGT_ONE_COO_PER_PROJECT_SEATING.md`); Andrew's `/self-drive` of ~22:0xZ is the
  new AMGT arm above. A successor does not re-arm the struck row.

- The ~O fabric's three 2026-09-26 rows -- `1.0.0_SA_CTO~O` `/self-drive 30m`, `2.0.0_SA_COO~O` `/canonical-drive 30m`
  COO MODE over all four ~O projects, `3.0.0_SA_CVO~O` `/canonical-drive 30m` CVO MODE (arming record
  `ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_O_FABRIC.md`): struck 2026-09-28 by `1.0.0_SA_CTO~O`. The chooser is Andrew:
  "kill the crons in this session not needed anymore" (stop @33f5ce4752), then the relaunch word of 2026-09-28 ~19:5xZ
  relayed by `0.0.0_AB_MSTR~Z` -- one COO per project, ZERO crons at launch, loops operator-initiated
  (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_195xZ_O_FABRIC_ONLINE_ONE_COO_PER_PROJECT.md`). The
  single COO~O over four projects is split by that record; a successor does not re-arm these rows.

- BLAST MODE (2026-09-24 ~17:4xZ, `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260924_174xZ_BLAST_MODE_P_M_Y_D_ONLINE_FAST_CLOSER.md`)
  and the three DIRECTED `/loop 20m` goal rows of ~P, ~M and ~Y (goal records `ANDREW_DIRECT_20260923_224xZ_COO_P_*`,
  `ANDREW_DIRECT_20260923_224xZ_COO_M_*`, `ANDREW_DIRECT_20260923_230xZ_COO_Y_*` in `org/tier1_exec/2.0.0_SA_COO/deliverables/`):
  struck 2026-09-28 by 1.0.0_SA_CTO. Chooser Andrew: the relaunch word routes ~P/~M/~Y to `/canonical-drive` (the
  stand-down of the goal loops, return brief A3). The goal records stay the done-criteria; a successor does not
  re-arm these rows.

- `2.0.0_SA_COO~O` `/canonical-drive NFRA_OPLGTW` 30m DIRECTED (relay 97709; on DONE the slot was to go to `~T`
  MDPF_TAXSMA then `~M` NFRA_MCPINDEX): struck 2026-09-24 by `1.0.0_SA_CTO~O`. The chooser is Andrew: his
  2026-09-22 ~18:2xZ word to that seat, "Finish your work and research on the OPLGTW project and do not go further
  with it", is carried in `2.0.0_SA_COO~O`'s session-close commit @5799432c1c. The lane `~O` is re-seated for
  NFRA_OPALAI on the ~O fabric (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260924_185xZ_CTO_O_NEW_PROJECT_O_FABRIC.md`),
  and a successor does not re-arm this row. The `~T` and `~M` hand-on clauses are NOT carried: nothing here
  decides them.
- IRPT POST-SLUG HOLD on the old `~B`/`~F` canonical progression (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260922_1517ET_IRPT_HOLD_AFTER_CVO_SLUGS.md`):
  lifted for IRPT_BCKEND and IRPT_FNTEND closed SUPERSEDED, Andrew-direct 2026-09-24 ~16:4xZ
  (`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260924_164xZ_IRPT_RETURN_FIVE_CALLS_ANSWERED.md`). The P/M/Y
  seats still read `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/{AUTHORITY,CONTRACT}.md` first.
- N1 push hold (`org/tier0/ledger/LD-0613.md` Progress 11): lifted by Andrew-direct ~17:5xZ "Push it"
  (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260924_175xZ_PUSH_N1_APPROVED.md`).
