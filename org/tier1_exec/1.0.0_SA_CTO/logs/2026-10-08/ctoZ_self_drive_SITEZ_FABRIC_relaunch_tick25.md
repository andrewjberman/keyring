# /self-drive SITEZ fabric (relaunch) -- tick 25, 2026-10-08 ~07:50Z -- `1.0.0_SA_CTO~Z`

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_082xZ_SELF_DRIVE_60M_SITEZ_FABRIC_RELAUNCH_AFTER_REBOOT.md`
**Covers:** tick 24's log (author time 2026-10-08T02:55:41-04:00 by `git log`) to ~07:5xZ. Cadence 60m, cron `12f228ad`.
**state: ARMED**

## Measurements

- Sequence (`.tools/sequence-check.py --project`, 5 of 5 read): AMGT_CORPUS, AMGT_HARVST, AMGT_RESAPP NEEDS-SLOT=1 each;
  DSGN_AMGTV1 and ETFS_RIVALS none. No DRIFT, no WAITING. Unchanged.
- Inbox: 0 unread in the folder; `check_inbox` empty. Six messages since tick 24, all acked (31609, 31611, 31612, 31615, 31618, 31619).
- Origin CLOUD `f7e80ffdf2` (ls-remote).
- **`opal-amgt-scoped-api` live, this seat's read at 07:50Z: CodeSha256 `+s6R0/rcpQ6l...`, LastModified 2026-10-08T07:19:32Z.**
  It was `MkM9Kf37...` at 06:50Z. The bb-18 redeploy has landed.
- Not run this tick: `directives-check`, `active-commitments`.

## The bb-18 act, from its ledger entry `org/critical_paths/.open_deploys/amgt-resapp-r78-bb18.json` (read whole; 5 of 6 legs closed)

The entry is `0.7.0_AE_CloudOps~A`'s; only the live hash above is this seat's own read.
- L1 build at the pin `fbb643923e`, detached; the pip log shows 0 index requests, both steps resolved from the six local wheels
  (the half's C3). L2: 147 of 147 vendored files equal the deployed zip; CHANGED 22, ADDED 8, REMOVED 0; the three RECORD files
  sorted-line-equal 3 of 3 (ADDENDUM 2). L3 upload. L4: one plan, one in-place update of the function's code, memory 1769
  unchanged; a 0-diff re-plan. L5: the freshness snapshot rewritten by the new code, 302 rows, same key.
- **L6 is OPEN:** AC1 to AC3 on the deployed function. Not yet run by this seat: the 2009-date read on the staleness call.

## Calls ruled since tick 24

| call | ruling | carrier |
|---|---|---|
| AMGT_HARVST rounds 64 and 65, L10 (`2.0.0_SA_COO~H` 31609, `3.0.0_SA_CVO~Z` 31612) | ADDENDUM 3: R14 row Z-S103 is a collection gap read first, from held data and the collector's logs, no publisher called; R15 row Z-S102, the exact-case form does not pair alone in an all-capitalised headline; round 66 | `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round60.md` @f7ad546af4; msgs 31613, 31614 |
| Cross-fabric (rule 32), laptop `1.0.0_SA_CTO` via `0.0.0_AB_MSTR~Z` 31615: can NFRA_OPLGTW serve a mailbox read by sender domain | YES; a widening, one round with a pair and a restart; after site Z merges origin and after the 07:00 America/New_York send. Accepted by the laptop (31619) | msg 31617 |

Open from that second call, this seat's: the laptop names the mailbox as the signed-in user's, and `mail_route.py` runs under a
fixed ingest identity. Which mailbox that identity reads is unread; it is read before the round is issued.

Governance forks at the CVO: 0. Design forks at the CRO: 0.

## Scope state (register read, 5 of 5)

All five `status: active`, `dep_stage: EXECUTING`. **COMPLETION TEST: NOT DONE -- 0 of 5 complete.** All five REACHABLE.
Waiting: AMGT_RESAPP on L6 and the round-78 slug; DSGN_AMGTV1 on that; AMGT_HARVST on round 66's issuance; ETFS_RIVALS on the
11:00Z run, then tw-1's merge; AMGT_CORPUS on the 13:00Z fire, its live-route read now unblocked, and four captures.

## Acts only Andrew can do (cited)

- The sign-in of `opal-gateway-bbg`, `/mcp` in the `0.0.3_BG_BBGTerminal` window, before the 2026-10-08 07:00 America/New_York
  send (his Microsoft login); and his word on the prepared one-session config move.
- His word to `0.0.0_AB_MSTR~Z` to push site-Z CLOUD (trunks are pushed on Andrew's word).
- His answer on a standing daily Bloomberg request of closes for the rivalfunds securities (CLAUDE.md, vendor use by his word).
- His word on force-removing drained worktrees that hold untracked scratch files (CLAUDE.md, recursive deletion).

## Compiler Tools

- `sequence-check.py` x5; `lambda get-function-configuration` (a read-back after an act); native Read and Grep.
