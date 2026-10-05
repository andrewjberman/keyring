# /self-drive AMGT_FRIDAY -- tick 15 after the SentinelOne crash (1.0.0_SA_CTO~Z, 2026-10-05 ~08:2xZ -> ~12:4xZ)

**archetype:** COORDINATE

state: ARMED. Cadence 60m, cron `29c8b141`. Arming record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261004_194xZ_SELF_DRIVE_60M_AMGT_FRIDAY_RESTART_AFTER_SENTINELONE_CRASH.md`
@2b18064b99. Previous log: tick 14 @21564190fa.

**The gap:** site Z sat in Modern Standby from 09:14Z to 12:32Z (System log 506/507, measured by MSTR~Z), so the 09:13, 10:13 and
11:13 ticks did not run. This log covers 08:2xZ to 12:4xZ.

## Inbox measurement

Since 08:45Z: 29529 (bbg bot_check), 29535 (BBGTML pull not attempted), 29538 (empty G4 revision) and 29539 (MSTR~Z's P0 result).
All READ. 0 unread.

## Calls, rulings and acts

| item | act | commit |
|---|---|---|
| HARVST bbg bot_check stop (COO~H msg 29529) | AMENDMENT 1 to the collection-run CTO half: ONE `--clear-stop` per leg per challenge after the collector's cooldown; a second challenge holds the leg for Andrew; ft unaffected | 441a9f05a6 |
| RESAPP r70 at-6 | **CLOSED** by COO~Z @a0635a12f3: grant and code legs landed (CodeSha256 `GS//XHnV`); c30-c33 NO -> YES on deployed; AE~A instance VALID | -- |
| BBGTML pull not attempted (COO~RV msg 29535) | P0 three-layer runbook check asked of MSTR~Z, with no sign-in attempt. Andrew alerted at the terminal. **Result (msg 29539): DAILY_CAPACITY_REACHED on refdata history,** so this is Z-S24, not sign-in. Andrew updated. The Z-S24 ruling's addendum corrects my 07:2xZ exposure count (the limit is data capacity across services, not BQL alone). | ruling addendum (this commit) |
| All-empty G4 revision for 2026-10-02 (COO~RV msg 29538, deadline 12:50Z) | **(a) SIGNED:** a one-key, byte-identical restore of the 10-04 object under a later capture time (`revision.order_key` ranks live objects by key capture time). 5 conditions; no delete. | 1564d0f1ab |
| DSGN r38 drained (portal 788d54a8 + 75f9f477) | CTO review in progress. The shared PanelFooter gains `ground` and `timeText` props, defaults unchanged. The stack sits on the unpushed r37 candidate; DEV is now 31510397 (DSGN_REBRND FAST lease commits); the trial merge is clean. | -- |

Verdict ledger: the row for 441a9f05a6 was appended at 08:4xZ; rows for this tick's rulings follow in the next log. **No open calls
in scope (tick 15).**

## Scope state

All 5 projects are active/EXECUTING. Open deploys in scope: 0.

**Completion test: NOT DONE.** 0 of 5 complete; all 5 REACHABLE.

## Acts only Andrew can do (each cited)

1. **The DSGN r37 DEV push** (CLAUDE.md Portal, per-push word); r38 will join it after review.
2. The 5 carried cards; row Z-W227-S1 (a Bloomberg exec-officer pull, a vendor use); Z-S230 (the rotation); the FWD-1 signed-in reads;
   the FT route ("Dont attempt FT until I return").
3. **None for the Bloomberg outage:** it is capacity, not sign-in.

## Compiler Tools

`get_delivery_state`, `directives-check.py --json`, `sequence-check.py`, one S3 prefix listing (rail-checked), `revision.order_key`
read, `git merge-tree --write-tree` for the r38 stack, PushNotification x2.
