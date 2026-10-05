# /self-drive AMGT_FRIDAY -- tick 13 after the SentinelOne crash (1.0.0_SA_CTO~Z, 2026-10-05 ~06:2xZ -> ~07:2xZ)

**archetype:** COORDINATE

state: ARMED. Cadence 60m, cron `29c8b141`. Arming record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261004_194xZ_SELF_DRIVE_60M_AMGT_FRIDAY_RESTART_AFTER_SENTINELONE_CRASH.md`
@2b18064b99. Previous log: tick 12 @4496050f39.

## Inbox measurement

`get_delivery_state` since 06:30Z: 4 messages, all READ (4 of 4), plus msg 29525 acked this tick. 0 unread.

## Calls, rulings and acts (since tick 12)

| item | act | commit |
|---|---|---|
| RESAPP 39-outcome board (subagent, 297 files) | `ledger/FWD_BOARD_ROUND69.md`; r69 analysis section 6. 19 of 20 NOT_REALIZED grades date from round 51. **Round-70 item 6** is a full sweep of 30 gradeable outcomes; RE-HOMED is not REALIZED; FWD-30 is graded on its DONE WHEN. COO~Z cut round 70 with item 6 @5f4fb67e1a. | 030d5d1e87 |
| HARVST at-4: `silver_append` drops later rows' extra columns (COO~H msg 29508) | Defect reproduced (pyarrow 24.0.0). **YES**, with at-1 in the stop window, under 3 conditions for a SHARED writer (20 caller files across CORPUS, RESAPP and harvest). | 08580b1fd6 |
| HARVST landing (COO~H msg 29522) | Conditions 1 and 3 MET. Condition 3 is answered by the CORPUS pair's own text ("runs on the old pin", am-2 CTO half :18). Land now, without waiting for sa; the running sa process holds cached modules. **Landed** @23baacf0e1 (on CLOUD): at-1 reads 100 -> 1, wall 84 s -> 0.9 s, rows identical, plus at-4. Condition 2's plant `test_at4_mixed_prefix_reads.py` was **re-run here: 6 passed**. | ff4e31bcd0 |
| ETFS_RIVALS Z-S24: backfill exhausted the BQL daily capacity (COO~RV msg 29514) | **(a) and (b).** Exposure measured: only 2 BQL callers (rivalfunds `collector_bloomberg.py`; constituents A4); the other legs use reference data. The 07:00 ET runs fire as scheduled. MSTR~Z was warned and re-runs A4 after the reset (msg 29520). The reset is probed with one query hourly. Backfill terms are tightened, which corrects my earlier 1M-row cap. | b5167de528 |
| DSGN r38 issued (COO~D msg 29525) | The shared `PanelFooter.tsx` gains one optional light-ground prop, with the default unchanged. **No objection.** The review checks that every other page renders unchanged. | c528ed0107 (COO~D) |

Verdict ledger: 3 rows (the RESAPP board sweep, HARVST at-4, RIVALS Z-S24). No design forks went to CRO~Z and no governance forks went
to CVO~Z. **No open calls in scope (tick 13).**

A memory write was refused by a hook ("seats do not write lessons to memory", Andrew-direct 2026-09-24). A stray MEMORY.md index line
from the same act was removed the same turn (the file is back to 17,169 bytes). The lesson lives in the RESAPP r69 analysis section 6.

## Scope state (register read 07:21Z, denominator 5)

| project | status | dep_stage | in flight |
|---|---|---|---|
| AMGT_CORPUS | active | EXECUTING | r37: am-2 and am-5 wait on the 13:00Z fire (old pin) |
| AMGT_HARVST | active | EXECUTING | r47: at-1 and at-4 landed; bbg and wsj resuming; sa resumes on its driver's exit |
| AMGT_RESAPP | active | EXECUTING | r70: at-1 (header figures) and at-4 (day-route origin) drained; the rest in flight |
| DSGN_AMGTV1 | active | EXECUTING | r38 AV-zp-1 in flight; the r37 DEV push awaits Andrew |
| ETFS_RIVALS | active | EXECUTING | r8 drain ~07:41 ET; Z-S24 (BQL capacity) ARMED, with recovery set |

Open TOs: D5 148, D13 2. Sequence: 5 UNPLACED, no flags. Open deploys in scope: 0.

**Completion test: NOT DONE.** 0 of 5 complete; all 5 REACHABLE.

## Acts only Andrew can do (each cited)

1. **The DSGN r37 DEV push** (CLAUDE.md Portal, per-push word), held at MSTR~Z.
2. The 5 carried pre-sleep cards.
3. Z-S230, the Bloomberg rotation (his account). The DSGN and RIVALS FWD-1 signed-in reads (his login). The FT route ("Dont attempt
   FT until I return").

## Compiler Tools

`get_delivery_state`, `directives-check.py --json`, `sequence-check.py`, a pyarrow reproduction, `pytest` on the at-4 plants, Grep
census of `silver_append(` callers and BQL callers, `integrations/bloomberg/READ_HERE.md` section 3.
