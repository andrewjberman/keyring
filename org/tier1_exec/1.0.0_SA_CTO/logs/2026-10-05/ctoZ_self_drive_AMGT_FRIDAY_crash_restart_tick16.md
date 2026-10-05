# /self-drive AMGT_FRIDAY -- tick 16 (1.0.0_SA_CTO~Z, 2026-10-05 ~12:4xZ -> ~13:2xZ)

**archetype:** COORDINATE

state: ARMED. Cadence 60m, cron `29c8b141`. Arming record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261004_194xZ_SELF_DRIVE_60M_AMGT_FRIDAY_RESTART_AFTER_SENTINELONE_CRASH.md`
@2b18064b99. Previous log: tick 15 @1aa51f0074.

## Inbox measurement

Since 12:45Z: 29547, 29552, 29554 and 29559, all READ. 0 unread.

## Andrew's words (relayed by MSTR~Z, each recorded there)

| word | record | this seat's act |
|---|---|---|
| "For IDVZ and PFOE, we should not touch anything being done on the Positioning pipeline. It should be done purely additively where we do one ad hoc targeted backfill in the rivalfunds shape for IDVZ and PFOE, then we add the two funds to the daily incremental pull with the rest of the rivalfunds." | @33ff3bdac0 | Agreed with COO~RV's reading (D12 as built). Added a condition to the Step B pair: prove the import is SERVED where a live home_producer object exists (`order_key` ranks live over import). |
| "3.) Yes, recommendation approved." (the DSGN r37+r38 DEV push, after the CardFooter fix) | 121b7b016e | Round-39 list @222ecd916c with the fix first; then this seat confirms and sends MSTR~Z the hash |

## Acts (since tick 15)

| item | act | commit |
|---|---|---|
| G4 2026-10-02 restore | COO~RV wrote 1 key, sha256-equal to 10-04 (msg 29547); **re-verified here**: 3 keys, new 46,943 B | 1564d0f1ab (CTO half) |
| DSGN r38 review | APPROVED pending the CardFooter:95 fallback fix (FWD-11). Shared PanelFooter defaults unchanged. | 2e225582da |
| DSGN r38 closed (COO~D @96ebc7a629) | The candidate lacks the fix; it is cut as round 39. Round-39 list sent. | 222ecd916c |
| ETFS_RIVALS round 8 | **Drained** by COO~RV (rp-1, lg-1, gc-1, hc-1, bt-1, su-1, an-1, rw-1, rn-1, fc-1). The CVO slug, then this seat's round-8 analysis, are next. | c79332ad2c (COO~RV) |

Verdict ledger: 2 rows (the G4 restore; IDVZ/PFOE). **No open calls in scope (tick 16).**

## Scope state (register read 13:18Z, denominator 5)

All 5 projects are active/EXECUTING. Open TOs: D5 136, D13 1. Sequence: 5 UNPLACED, no flags. Open deploys in scope: 0.

**Completion test: NOT DONE.** 0 of 5 complete; all 5 REACHABLE.

## Acts only Andrew can do (each cited)

1. Row Z-W227-S1: a Bloomberg exec-officer pull (a vendor use no word of his names).
2. Z-S230, the Bloomberg rotation (his account).
3. The FWD-1 signed-in reads (his login).
4. The FT route ("Dont attempt FT until I return").
5. The remaining carried cards: the DEV standing permission (moot now that this push is approved), the seat relaunch, the PROD
   promote, HARVST FWD-7 guidance.

## Compiler Tools

`get_delivery_state`, `directives-check.py --json`, `sequence-check.py`, an S3 prefix listing (rail-checked), `git show` reads of the
portal candidates.
