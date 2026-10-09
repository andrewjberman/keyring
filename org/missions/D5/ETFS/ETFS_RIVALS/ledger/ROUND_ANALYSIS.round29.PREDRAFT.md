# ETFS_RIVALS round 28 -> 29 -- the CTO's L10 answer, PRE-DRAFT (NOT ISSUED)

**Author:** `1.0.0_SA_CTO~DELL1`, 2026-10-09 ~05:1xZ, on UB-20261009T045707Z-003b (the CRO's optional act). **Status: DRAFT.** It is
issued only after the round-28 L10 slug arrives. The slug's grades choose the branches, never this draft. **Base:**
`ledger/ROUND_ANALYSIS.round22.md` ADDENDUM 7 (round 28 closes on three acts: aw-1 deploy, tc-1 merge, switch-on). Ruling
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_RIVALS_D1S2_QUEUE_STATE_READER_20261009.md` @c5fb809173. Laptop XA-20261009T033809Z-8c1a
(standing tier-3 request; condition 1: the vehicle reads the request's state before each draw).

## Branch reads (two independent J1s)

| J1 | read at | MET -> | NOT MET -> |
|---|---|---|---|
| tw-1 J1: the leg is reached and unchanged with the switch unset (AMENDMENT 1's tells) | 2026-10-09 11:00Z scheduled vehicle run, transcribed by `~ZV` (XB-897f) | the tc-1 merge proceeds under its pair | one round-29 cell on the failing tell. If the cause is a Terminal sign-in or session failure, it is no cell: re-read at Monday 2026-10-12's 11:00Z run, preceded by a pre-flight |
| aw-1 J1 (R31): the first 13:00Z sweep after the round-28 Lambda deploy | 2026-10-09 13:00Z sweep | aw-1 graded MET | one round-29 cell on the failing read, at most three criteria |

## Round-29 enrichment list (one issuance by `2.0.0_SA_COO~V1`)

1. **ALWAYS: the queue-state READER cell** (row D1-S2). Before each draw, the history-owed leg in
   `data/etfs/scripts/rivalfunds/enrichment_bloomberg.py` reads the standing request's `state`.
   - Anything but `active` draws ZERO rows and logs one line naming the state.
   - A state that cannot be read draws zero and logs that it cannot read the state. It never draws on a failed read.
   - Criteria (three): `active` draws as today, `paused` draws 0 rows (the negative arm), and an unreadable state draws 0 rows.
   - **Precondition:** MDPF_DEMQUE's addendum names the state's address as `lib/opal_naming.py address()` output (Rule 30). That is
     DEMQUE's next round, with XA condition 3. The cell is cut against that address, never a typed one. If the addendum has not landed
     at issuance, the cell waits and the rest of the list goes ahead.
   - **Deploy:** the vehicle runs this file, so the change is a site-Z producer change, under `1.0.0_SA_CTO~Z`'s never-widen half. It
     is not under Andrew's no-modify order, which covers `integrations/bloomberg/pipeline/`, the vehicle scripts and the sign-in; this
     file sits in `data/etfs/scripts/rivalfunds/`. The apply follows Andrew-direct ~03:5xZ: dell1 for cloud acts, `~ZV` for
     site-bound ones.
2. **Then act 3, the switch-on, and act 4's plant key**, under the one pair the fold names (@79c8d84e65 section 1). They are no cell.
   They wait for item 1 deployed and read once with the request `active`. The standing request is entered by `2.0.0_SA_COO~Q1` before
   the first draw.
3. **Any J1 NOT MET cell** from the branch table.

**FWD-24** stays NOT REALIZED until the switch-on runs and the planted security is read whole within 3 runs.

## Unchanged

The 20,000-row per-run cap (R24). The queue's reserve rule (a run stops at the reserve and resumes next day). R32 (`round` carries
the task-order round).
