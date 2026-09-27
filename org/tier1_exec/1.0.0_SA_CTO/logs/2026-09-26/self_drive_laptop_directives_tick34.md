# SELF-DRIVE laptop directives -- ticks 33-34 (2026-09-27 ~04:47Z and ~05:18Z)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_LAPTOP_DIRECTIVES_IRPT.md`
@`ce6aa15a17`. **Covers:** the ticks since the ticks 31-32 log (@`7b6d2b6d65`, ~04:19Z). **State: ARMED.**

## Scope

9 laptop directives of 15 live. IRPT first: IRPT_BCKEND and DSGN_IRPTV1, both active / EXECUTING. Unread at the tick: 0.

## Milestones (read, not this seat's acts)

- **COT's first signed-in Performance journey is DONE** (Andrew's call 3; ~P @`ffe4269b12`):
  - ONE claim, 22f0a988 (04:31:30Z), with 2 BD requests under it;
  - RPT-b683f188 PARTIAL, -1.18% on the face;
  - disarmed to `approved_performance_plan = null` at 04:34:55Z (0/1/1, no session grant), as the CTO half
    @`cd91ef7c0e` named.
- Both of Andrew's one-use calls are now spent: INF (call 2, @7f64b166) and COT (call 3, @22f0a988).
- **Window 8 closed** (@`f293962a58`): the principal was deleted at 04:46:35Z, after every job was terminal (the
  101673 rule).
- **~Y's WAF-refresh fix** (the bounded (c)) was proved offline @`141a45d087`: window 8's live shape goes from ATTENTION
  to READY with one recapture. ~P ships it.
- **~D:** TO-IV-e-52 (the UIR-29/27 cell) complete, and wk-29 drained @`ebbd3aa18b`.
- **~P deploy `irpt-cot-actual-window-20260927`** (@`765f498ad4`): an adapter code-only change (`bd_selected.py`,
  actual_start = the first series point). With the plan null, the adapter cannot call BD, so DELTA=0 on every
  reachable surface and no half is owed. Named for ~P's record: the retained RPT-b683f188 keeps its computed
  actual_start until a new use recomputes it.

## Acts (1.0.0_SA_CTO lane)

- The inbox watcher re-armed on each expiry.
- No new ruling since the ticks 31-32 log.

## Open calls in scope

None.

## Completion test

NOT DONE: 0 of 2 IRPT projects complete. D10 is UNMEASURABLE (no members).

## Waiting on other seats

| seat | owes |
|---|---|
| ~P | the WAF-refresh resident swap; the next Analysis packet (K5: up to 6 status GETs + ONE host recapture) |
| ~M | Monday 09-28: R1, then the COT cash-line act with S155 alone |
| ~D | the round-8 items (the exception label); the round 7 push to origin DEV |
| 3.0.0_SA_CVO | round 7 L9 grades; the round-5 slug |

## Compiler Tools

`git log -1 --format=%B` on the ledger commits; `git show --stat` on 05778597eb.

state: ARMED
