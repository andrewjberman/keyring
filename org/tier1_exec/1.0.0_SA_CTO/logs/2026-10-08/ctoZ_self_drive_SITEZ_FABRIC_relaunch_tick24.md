# /self-drive SITEZ fabric (relaunch) -- tick 24, 2026-10-08 ~06:50Z -- `1.0.0_SA_CTO~Z`

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_082xZ_SELF_DRIVE_60M_SITEZ_FABRIC_RELAUNCH_AFTER_REBOOT.md`
**Covers:** tick 23's log (author time 2026-10-08T01:55:10-04:00 by `git log`) to ~06:5xZ. Cadence 60m, cron `12f228ad`.
**state: ARMED**

## Measurements

- Sequence (`.tools/sequence-check.py --project`, 5 of 5 read): AMGT_CORPUS, AMGT_HARVST, AMGT_RESAPP NEEDS-SLOT=1 each;
  DSGN_AMGTV1 and ETFS_RIVALS none. No DRIFT, no WAITING. Unchanged.
- Inbox: 0 unread in the folder; `check_inbox` empty. Five messages since tick 23, all acked (31595, 31599, 31601, 31604, 31607).
- Origin CLOUD `ec8b9792e9` (ls-remote). After a fetch, site Z HEAD is **262 ahead and 667 behind** origin; tick 23's commit
  `bba263240e` is not on origin (positive control: `HEAD~300` is).
- `opal-amgt-scoped-api` live: CodeSha256 `MkM9Kf37...`, LastModified 2026-10-07T04:40:17Z. **The bb-18 redeploy has not landed.**
- Not run this tick: `directives-check`, `active-commitments`.

## Calls ruled since tick 23

| call | ruling | carrier |
|---|---|---|
| ETFS_RIVALS row Z-S75: the rk-1 merge changed a module the 11:00Z vehicle loads, unpaired (`2.0.0_SA_COO~RV` 31595) | LEAVE it; the names the vehicle uses are unchanged by the AST compare; the 11:00Z log read grades it, an ImportError is a revert the same hour. Term: before any merge to site-Z CLOUD the issuer lists the modules the vehicle's two working-tree legs load | msgs 31596, 31597 |
| AMGT_CORPUS: two ledger entries read PAST-WINDOW on dell1 (`0.0.0_AB_MSTR~Z` 31601) | both are open on purpose, each waiting on a named act; nothing re-executed; `2.0.0_SA_COO~X` sets each window to that act | msgs 31602, 31603; held @170d418cd7 (31607) |

Governance forks at the CVO: 0. Design forks at the CRO: 0.

## Received

- `2.0.0_SA_COO~H` 31599: AMGT_HARVST gold rebuild #9 DONE, verify ended 06:25Z, ledger closed 4 of 4. This seat's read-back
  (s3api): `article_security_mention/date=2026-10-08/part-20261008T055319Z.parquet` 7,696,668 B 06:12:53Z and
  `chatter_daily/date=2026-10-08/part-20261008T061255Z.parquet` 446,715 B 06:19:01Z are the newest part of each table. The row
  counts (48,358; 68,002), removed 21 of 21 by name (4 true), unexplained 0, and BNP 237 to 238 are the COO's.
- `2.0.0_SA_COO~Z` 31604: the bb-18 GO given at 06:31Z at pin `fbb643923e`; `0.7.0_AE_CloudOps~A` respawned on the order.

## Scope state (register read, 5 of 5)

All five `status: active`, `dep_stage: EXECUTING`. **COMPLETION TEST: NOT DONE -- 0 of 5 complete.** All five REACHABLE.
Waiting: AMGT_RESAPP on the bb-18 act; DSGN_AMGTV1 on that; AMGT_HARVST on the round-64 slug and the feed walk (round 65);
ETFS_RIVALS on the 11:00Z run, then tw-1's merge; AMGT_CORPUS on the 13:00Z fire and four captures (port 5174).

## Acts only Andrew can do (cited)

- The sign-in of `opal-gateway-bbg`, `/mcp` in the `0.0.3_BG_BBGTerminal` window, before the 2026-10-08 07:00 America/New_York
  send (his Microsoft login); and his word on the prepared one-session config move.
- His word to `0.0.0_AB_MSTR~Z` to push site-Z CLOUD (CLAUDE.md Portal: trunks are pushed on Andrew's word).
- His answer on a standing daily Bloomberg request of closes for the rivalfunds securities (CLAUDE.md, vendor use by his word).
- His word on force-removing drained worktrees that hold untracked scratch files (CLAUDE.md, recursive deletion).

## Compiler Tools

- `sequence-check.py` x5; `s3api list-objects-v2` and `lambda get-function-configuration` (read-backs after an act); native Read.
