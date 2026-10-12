# SELF-DRIVE cluster open calls -- tick 2 (2026-10-12 13:56Z, run by hand: the :41 cron fire did not arrive) -- state: ARMED

Arming record `ANDREW_DIRECT_20261012_125xZ_SELF_DRIVE_CLUSTER_OPEN_CALLS.md` @4698a8f59d. Cron 9c76a283. Ticks covered: 2.

## Measurements

- open rows: 13 (sitez 6, dell1 2, dell2 4, laptop 1 -> 0 after this tick); closed 85. Delta since tick 1: site Z closed ffaf
  on the tick-1 ruling; the laptop closed fc10 (`--ruled-by cluster-lead`, the tick-1 record) -- the (a)-bounded re-seat is DONE
  (dell2's six seats re-launched in the MP-20261010 format, receipts 108554/108559); (b) credits stays a cited act.
- inbox: 0 unread at the tick's start (108553/108554/108557-108559/108568 read and acked between ticks).
- live seats on the laptop: MSTR, ~ANL, ~FBL, ~U7, COO~C, CVO~L, this seat. **4.0.0_SA_CRO is DARK** (stood down 11:1xZ) while
  holding the fe9b research ask -> re-seat asked of 0.0.0_AB_MSTR this tick (the skill: a dark seat is spawned the same tick).
- sequence-check unchanged from tick 1 (no flags on the placed projects the calls touch).

## Calls this tick

- RULED by the driver: 0 new (ffaf and fc10 closed on tick-1 rulings).
- DESIGN FORK at CRO research: dell1-fe9b (CRO dark; re-seat asked; ruled the tick the research lands, or on the REC (A) at
  tick 3 if no research lands by then -- a research seat that cannot be seated does not hold a call).
- GOVERNANCE FORKS at the CVO: 0.
- ACTS ONLY ANDREW CAN DO: 15 (the tick-1 list less fc10's re-seat; fc10 (b) credits stays): e7f2, 1b36, 21c5, 8ed7, f0d2, a519,
  058e, 01c5, e260, 3cb1, fbb1, W61-S1, S9112, FWD-27 keys + elevated runs, trade-submission-api delete, White Label standing.

## Verdicts since the last tick

none.

## Acts taken

fc10 closed on the laptop list (committed with this log); CRO re-seat asked; NFRA_CTLPLN round 10 analysis (32f1844a1f, FWD-28
REALIZED) between ticks.

## Completion test

UNMEASURABLE (free-text scope); the loop ends on Andrew's stand-down word.

state: ARMED

## Compiler Tools

`python .tools/open-calls.py list --all --cloud`; `python .tools/open-calls.py close --ruled-by cluster-lead`; `get_live_agents`;
`safe-commit.sh`.
