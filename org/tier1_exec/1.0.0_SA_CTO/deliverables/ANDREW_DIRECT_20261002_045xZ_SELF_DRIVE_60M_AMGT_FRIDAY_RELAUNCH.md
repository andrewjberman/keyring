# ANDREW-DIRECT -- 2026-10-02 ~04:55-04:59Z -- re-arm /self-drive 60m AMGT_FRIDAY after the site-Z reboot

**Channel:** site-Z terminal of `0.0.0_AB_MSTR~Z` (session 026d7c93-4357-4cef-adca-bdbca02c74cd), typed by Andrew.
`0.0.0_AB_MSTR~Z` recorded the words in the same turn and relayed them in msg 28199.
**Recorded here by:** `1.0.0_SA_CTO~Z`, at relaunch, 2026-10-02 ~05:1xZ.
**Prior arm:** `ANDREW_DIRECT_20261001_040xZ_SELF_DRIVE_60M_AMGT_FOUR_PLUS_ETFS_RIVALS_ARM_ON_CRO_BRIEF.md`. It was
STOPPED-BY-OPERATOR at ~03:5xZ on the disk wind-down (cron `100fd3c2`), and its last line says "Re-arm only on Andrew's
word".

## Verbatim (the three source records are in `org/tier0_exec/0.0.0_AB_MSTR/deliverables/`)

1. `ANDREW_DIRECT_20261002_045xZ_GO_RELAUNCH_SITEZ_AMGT_DEMO_FLEET.md`. Andrew: "go". The question it answered was
   "I recommend relaunching the demo fleet now: CTO~Z, CRO~Z and COO~X, ~Z, ~H and ~D. Say go and I'll spawn them."
   The context given with that question named this seat's `/self-drive 60m` row and the 09:00 ET PROD target.
2. `ANDREW_DIRECT_20261002_045xZ_RV_TEAM_ETFS_RIVALS_ADJUDICATION_AND_EGRESS_TONIGHT.md`. Andrew: "I also need COO~RV
   CVO~RV and CRO~RV, they need to work together as a team to finish ETFS_RIVALS. CRO~RV has adjudication ability for
   any open calls on the ETFS_RIVALS. CTO~Z has adjudication ability for the rest of the fabric. All agents have any
   egress they need to run their operations tonight."
3. `ANDREW_DIRECT_20261002_045xZ_CANONICAL_DRIVE_ALL_COOS_RV_CLOSER_DRIVE_RIVALFUNDS_DEMOABLE_TODAY.md`. Andrew: "Make
   sure /canonical-drive loops are running for all COOs on their respective projects. COO~RV can use /closer-drive, I
   need them to be prioritized, i want mcp.opalinvest.dev/rivalfunds demoable Today"

## This seat's reading, stated so it can be overruled

Word 1 relaunched the seats, and its record leaves re-arming to each seat's own reading of its LIVE_ARMS row. Word 3
orders the COO loops that are this row's paired half. Word 2 gives this seat adjudication over "the rest of the
fabric". Taken together, the three words are read as Andrew's word to resume this driver. One word from Andrew,
"off", stands the loop down.

## ARM TERMS

| term | value |
|---|---|
| scope | AMGT_CORPUS, AMGT_HARVST, AMGT_RESAPP, DSGN_AMGTV1, ETFS_RIVALS (site Z; scope name `AMGT_FRIDAY`). D5 (SITEZ) holds four of them. DSGN_AMGTV1's directive D13 reads LAPTOP while the project is seated at site Z under COO~D. This is carried as in the prior arm, because Andrew named the project; the mismatch is a register finding routed to MSTR~Z. |
| cadence | 60m (session-only cron; this record is the carrier) |
| call routing | Step 1 of `/self-drive`. The driver rules on its own REC. Design forks are ruled after CRO~Z research (`/closer trace`). Governance forks go to `3.0.0_SA_CVO~Z`. **ETFS_RIVALS open calls go to `4.0.0_SA_CRO~RV`** (word 2), and this driver routes them there and does not rule them. |
| cited act list | Andrew's login (the ETFS_RIVALS FWD-1 signed-in read; a Bloomberg Terminal sign-in). A shared-branch push (MSTR pushes trunks on Andrew's word; LD-0367/0368). Recursive deletion or another unrecoverable act. A promote payload his word does not name (CVO verdict 27503). Vendor egress for tonight's operations is covered by word 2, recorded as written. |
| paired_with | `/canonical-drive <own project> 30m` at `2.0.0_SA_COO~X` (CORPUS), `~Z` (RESAPP), `~H` (HARVST) and `~D` (DSGN_AMGTV1). `2.0.0_SA_COO~RV` runs `/closer-drive` on ETFS_RIVALS under a FAST lease, prioritized, as one team with `3.0.0_SA_CVO~RV` and `4.0.0_SA_CRO~RV`. |
| live arms row | `org/ref/LIVE_ARMS.md`, RELAUNCH sub-block under the `1.0.0_SA_CTO~Z` row (@983e7540cb) |
| stop | DONE read from the register; HELD-AT-STOP (never for AMGT_HARVST); or Andrew's stand-down |

## Open at arm (from tick 26, `ctoZ_self_drive_AMGT_FRIDAY_tick26.md`)

- AMGT_HARVST gold #4 has not run. It is due before 13:00Z. Owner: `2.0.0_SA_COO~H`.
- ETFS_RIVALS Addendum B is issued at `9be8b10338`, but no workers are spawned. Owner: `2.0.0_SA_COO~RV`, now on
  `/closer-drive`.
- The AMGT demo is on portal PROD `b3a1d8a6` (v2.1.193).
