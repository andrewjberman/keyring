# SELF-DRIVE cluster open calls -- tick 5 (2026-10-12 16:46Z, by hand on the laptop's return; the 15:41Z and 16:41Z cron fires did not arrive) -- state: ARMED

Arming record `ANDREW_DIRECT_20261012_125xZ_SELF_DRIVE_CLUSTER_OPEN_CALLS.md` @4698a8f59d. Cron 9c76a283. Ticks covered: 4 (quiet, 15:00Z,
runtime line) and 5. Last committed log: tick 3 @b6ceda926f (14:0xZ) -- this log is the hourly floor plus the deltas below.

## Measurements

- The laptop was dark ~15:35Z-16:45Z (Andrew's travel; record `ANDREW_DIRECT_20261012_142xZ_LAPTOP_DARK_4_5_HOURS_TRAVEL.md`),
  shorter than the 4-5 h he expected. On return: box/dell1 +39 over CLOUD, box/dell2 +4, box/sitez +1, CLOUD unmoved since
  15:30Z (the integrator is this box); 35 commits on the box branches since 15:35Z (dell1's HARVST/RIVALS/FIRMBKTS lanes, dell2 one).
  `0.0.0_AB_MSTR` ordered 16:46Z: drain the bus, one integrate pass, status exchange, report.
- open rows: 11 (sitez 6, dell1 1, dell2 4, laptop 0); closed 87. No new row since tick 3; fe9b closed by dell1 on the (A)
  ruling + the CRO's amendment.
- inbox at this tick: read by `check_inbox` (count in the tick output). Live on the laptop: MSTR, ~ANL, ~FBL (FB-f-19 edge leg
  APPLIED 15:12-15:15Z, ledger L6 open watching 7 regions), ~U7, COO~C, CVO~L, CRO (re-seated 14:04Z), this seat.

## Calls since the last log

- RULED by the driver: 0 new. Amended: fe9b addendum 1 (the CRO's secondary-suppression pattern, 460cfc8cae).
- DESIGN FORKS at CRO research: 0 open. GOVERNANCE FORKS: 0.
- ACTS ONLY ANDREW CAN DO: 15, unchanged (tick-1 record §B).

## Verdicts since the last log

- `3.0.0_SA_CVO~L` REFUSED the v0.27 ratified half (msg 108609, review @67b765298a): "the Dev clause's only reachable effect is to
  admit a Dev token on a non-Opal firm. That is a widening, not defence-in-depth." Executed: PRD v0.28 (5a2b425d6b) states what the
  code does, names the widening, binds its removal to cell CT-aa-5 at the next apply; "defence-in-depth" struck. No disagreement.

## Acts taken since the last log

v0.26 (dfec0d8ab6) -> v0.27 (0727ecb3b3, the premise measured false by the CT-aa-4 apply) -> v0.28 (5a2b425d6b); CT-aa-4 CTO half
signed (d56d3dc8fe); the dark-window record (04d7f457c8); relays to dell1 (D1-S9 withdrawn: the research-pull fence stays
tier-only) and to COO~C/CVO~L.

## Completion test

UNMEASURABLE (free-text scope); the loop ends on Andrew's stand-down word.

state: ARMED

## Compiler Tools

`python .tools/open-calls.py list --all --cloud`; `check_inbox`; `get_live_agents`; `git rev-list --count`; `safe-commit.sh`.
