# /canonical-drive MDPF_SECHIST -- 2.0.0_SA_COO~H1, 2026-10-09 03Z (dell1)

Authority: Andrew-direct ~03:1xZ relayed by 0.0.0_AB_MSTR~DELL1 msg 1541 ("all COOs on your box are running /canonical-drive on
their given project, and are tapped into the /keep-driving system"). Cadence 10m (own active project). Lease FULL.
keep-driving empty_tick=on (dell1, object source, set 01:53:41Z).

## Tick 1, 03:2xZ

| project | limb | round | TOs t/T | cells c/F | thread | act fired |
|---|---|---|---|---|---|---|
| MDPF_SECHIST | L7 | 2 | 3/4 | 2/3 of the round-2 list (card A not cut) | n (event-gated) | EMPTY -> /next-calls --drive |

Measured: `dep_stage` EXECUTING; TO-SH-t1, t2, t4 complete; TO-SH-t3 issued, unspawned, event-gated on the 2026-10-09 07:00 ET
(11:00Z) scheduled pull and the ~13:01Z publish. Surprise rows: none open (`comp-surprise --project MDPF_SECHIST --json` -> {}).

### /next-calls MDPF_SECHIST --drive

Calls queued to the box (open-calls.py):

- **CALL 1 [BLOCKING, gates OPTION card-A]: FWD-2 card A (the client-depth Bloomberg draw) goes to MDPF_DEMQUE as a queue request
  instead of waiting on site Z ruling 31292.** Context: round-2 decomposition did not cut card A because site Z (ruling 31292, msg 593)
  held it until AMGT_CORPUS and ETFS_RIVALS record in `bbg_budget`. Since then, Andrew's ~02:4xZ egress law (CTO~DELL1 msg 1507) routes
  every Bloomberg draw through 2.0.0_SA_COO~Q1's queue (`org/missions/D8/MDPF/MDPF_DEMQUE/requests/`), and the DEMQUE PRD C-PRODUCERS
  names MDPF_SECHIST's price-need file as a queue input. REC: yes -- file card A as a DEMQUE request at round 3; the queue is now the
  one budget route, which is what 31292 waited for.

Options executed (FREE):

1. Acceptance check dry-run, negative arm: `R2_CHECKS/sh_fwd1_acceptance.py` at 03:2xZ ->
   `FWD1-ACCEPT-BAD newest-manifest-not-scheduled as_of=2026-10-07 run_class=adhoc`. The instrument refuses the ad-hoc manifest as
   designed; it is ready for the 11:00Z run.
2. Clean-name exposure of SH2-t3-AC1: served `platinum/etfs/positioning_data.json` (LastModified 2026-10-08 13:01:38Z) carries 188
   holdings rows, 166 distinct names, 1 with a `/<state>` suffix (`Cisco Systems Inc/Delaware`). A newly held security fails the
   clean-name clause only if its vendor name carries the suffix; the clause stays with 2.0.0_SA_COO~M1's MDPF_SECCLASS cell.
3. Inherited ledger `mdpf-sechist-sh-t1-sitez-etf-daily-pull-20261007` L3 (msg 1417): the budget clause reads the day's
   `bbg_budget_<day>.jsonl`, which lives in `%LOCALAPPDATA%/opal_bbg_budget` on the site Z machine (`bbg_budget.py:38-50`), so it is a
   site-Z-only read. The ask was sent before the run to 0.0.0_AB_MSTR~DELL1, for 0.7.0_AE_CloudOps~Z.

WHILE BLOCKED: TO-SH-t3 and ledger L3 wait on the 11:00Z scheduled pull; around them, options 1-3 above. Card A waits on CALL 1.
Nothing else in the frozen round-2 rectangle is uncut.
