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

### Corrections, 03:3xZ

- CALL 1 was HELD for Andrew by 1.0.0_SA_CTO~DELL1 (msg 1566): card A is his named hold ("I will handle that with sitez",
  this seat's own record `org/tier1_exec/2.0.0_SA_COO/deliverables/cooH1_ANDREW_DIRECT_20261008_175xZ_SECHIST_SH_T4_RELAND_YES_SITEZ_CARD_A_HIS.md`
  point 3). This seat's miss: the record was its own and the call was queued without reading it. The queue rule changes the route, not who releases card A.
  SH-t-5 stays uncut until his release or his yes to "file it as a MDPF_DEMQUE tier-2 request, quoted first".
- Option 3's carrier was wrong: site Z ruling 32271 (msg 1561) requires a task order, not a manager relay. READ order
  `MDPF_SECHIST.TO-READ-R2-L3.pull-exit-and-budget-line-sitez` to 0.7.0_AE_CloudOps~Z committed @3033ceac2a (gate OK).

## Ticks 03:34Z, 03:44Z, 03:54Z

Empty x3 (no change; gated on the 11:00Z pull and Andrew's card-A word). 03:54Z read THIRD-EMPTY-TICK: unblock case
UB-20261009T035455Z-cbf8 opened to 4.0.0_SA_CRO~DELL1.

### Site-Z read: lane collision and the S3 fallback (03:5xZ)

Site Z CTO msg 32344 (relayed 0.0.0_AB_MSTR~DELL1 msg 1608): 0.7.0_AE_CloudOps~Z keeps NFRA_OPLGTW, so this seat's READ order
@3033ceac2a collides with rule 27 (one project per Tier-2 lane); a re-ruling is open with 1.0.0_SA_CTO~Z and Andrew is asked
whether "Do not seat site-Z CloudOps agents for dell1's deploys" covers site-bound acts. The order stays as written until then.

Fallback if no site-Z read lands: ledger L3's budget clause ("a backfill line in the day's bbg_budget ledger file") is
readable from S3 as an INFERRED value. `etf_daily_pull.py:606-609` sets `history_backfill_budget.recorded` to the row count
only when `bbg_budget.record("backfill", ...)` returned true (the ledger line was written), else None; a refused backfill
records nothing. So in `s3://opal-data-etfs/bbg/<asof>/run_manifest.json`, `run_class=scheduled`, `history_backfill_error`
null, `objects_failed` empty and `history_backfill_budget.recorded` non-null together read L3, with the ledger line marked
`inferred` (the producer's own record() return), never `measured`. Shape confirmed on the 2026-10-07 ad-hoc manifest:
recorded 2929, estimate 3448, limit 120000, spent_before 0, 15 planned securities. A direct site-Z ledger read, when one
lands, upgrades it to `measured`.
