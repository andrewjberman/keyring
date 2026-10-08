# /self-drive SITEZ fabric (relaunch) -- tick 19, 2026-10-08 ~01:50Z -- `1.0.0_SA_CTO~Z`

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_082xZ_SELF_DRIVE_60M_SITEZ_FABRIC_RELAUNCH_AFTER_REBOOT.md`
**Covers:** tick 18's log (author time 2026-10-07T20:56:37-04:00 by `git log`) to ~02:0xZ. Cadence 60m, cron `12f228ad`.
**state: ARMED**

## Measurements

- Sequence (`.tools/sequence-check.py --project`, 5 of 5 read): AMGT_CORPUS, AMGT_HARVST, AMGT_RESAPP NEEDS-SLOT=1 each;
  DSGN_AMGTV1 and ETFS_RIVALS none. No DRIFT, no WAITING. Unchanged.
- Inbox: 0 files unread in the folder; 3 broker messages at this tick's read, acked (31535, 31537, 31539).
- Origin CLOUD `81815f373a` (ls-remote). C: reads 92 GB free of 474 (`df`), up from about 39 GB at 01:0xZ.
- Not run this tick: `directives-check`, `active-commitments`.

## Calls ruled since tick 18

| call | ruling | carrier |
|---|---|---|
| ETFS_RIVALS round 26, rg-2 deploy (`2.0.0_SA_COO~RV` 31506) | CTO half SIGNED conditional on J1; the act must move no figure; C1 decides when it applies | `deliverables/CTO_HALF_ETFS_RIVALS_R26_RG2_READERS_DEPLOY_20261008.md` @e081a672d4 |
| the same, C1 (31526) | live code against pin code equal row for row MEETS C1; apply; the replay's difference from the served objects is its own row | msg 31527 |
| the disk cleanup (`0.0.0_AB_MSTR~Z` 31507) | four trees and one zip are not removed; issuers name any other tree a signed half cites | msgs 31516 to 31520 |
| AMGT_HARVST R6, `ICT_US_Equity` (`2.0.0_SA_COO~H` 31531) | stays with 0 pairs; the unresolved holding is the pool's; a row on AMGT_RESAPP's channel | msgs 31533, 31534 |
| AMGT_HARVST round 61 grade (`3.0.0_SA_CVO~Z` 31535) | the fallback matches the stored case only; HEI joins R3 | msgs 31542, 31543 |

Governance forks at the CVO: 0. Design forks at the CRO: 0.

## Verdicts received

- `3.0.0_SA_CVO~RV` 31525: rg-2 J1 MET; 0 of 6,066 and 0 of 1,406 rows move; by hand, the 10-02 and 10-05 objects fit their own
  dates (84 of 93, 126 of 136).
- `3.0.0_SA_CVO~Z` 31535: fallback sample 27 of 30, all 27 Nokia; nine forms 16 of 17.

## An error by another seat, and this seat's read of the damage

`0.0.0_AB_MSTR~Z` reports (31539) that its `/cleanup` run removed the LIVE AMGT_CORPUS pin worktree `61a724beb0ad` at ~01:4xZ and
recreated it at the same path and commit at ~01:5xZ; the tool's exclude flag matches a path exactly, not by prefix. This seat's
reads at ~01:5xZ: the tree exists, HEAD `61a724beb0ad`, 0 status lines; the untouched sibling pin tree holds one run record and
`__pycache__` beyond tracked files, no venv and no config. INFERRED from the sibling: tracked files are what the fire needs. Asked
of `2.0.0_SA_COO~X` before the 2026-10-08 13:00Z fire: `-Status` and a `refresh --dry-run` from that tree (msg 31540).
Present after the cleanup, by this seat's read: `C:/tmp/ba20-r77-14a36147bd.zip` (41,981,131 B), `og-rb22`, `og-rel24`, `rv-r8`,
branch `rv-deploy-r25mr`; port 5174 answers 200.

## Scope state (register read, 5 of 5)

All five `status: active`, `dep_stage: EXECUTING`. **COMPLETION TEST: NOT DONE -- 0 of 5 complete.** All five REACHABLE.
Waiting: AMGT_RESAPP bb-18 on the sixth wheel; ETFS_RIVALS on the rg-2 apply and the 11:00Z run; AMGT_HARVST on round 61's
remaining orders; AMGT_CORPUS on the pin tree's check and the 13:00Z fire; DSGN_AMGTV1 on RESAPP's deploy.

## Acts only Andrew can do (cited)

- The sign-in of `opal-gateway-bbg`, `/mcp` in the `0.0.3_BG_BBGTerminal` window, before the 2026-10-08 07:00 America/New_York
  send (his Microsoft login); and his word on the prepared one-session config move.
- His word on force-removing drained worktrees that hold untracked scratch files (CLAUDE.md Agent Autonomy: recursive deletion).
- His answer on a standing daily Bloomberg request of closes for the rivalfunds securities (CLAUDE.md, vendor use by his word).
- His word on whether "no fetch on any box" covers an AWS host at deploy; his word that the smoke on port 5174 is finished.

## Compiler Tools

- `sequence-check.py` x5; `aws lambda list-functions` (inspection); `git -C <tree> status`; `df`; native Read.
