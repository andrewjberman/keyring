# /self-drive SITEZ fabric (relaunch) -- tick 20, 2026-10-08 ~02:50Z -- `1.0.0_SA_CTO~Z`

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_082xZ_SELF_DRIVE_60M_SITEZ_FABRIC_RELAUNCH_AFTER_REBOOT.md`
**Covers:** tick 19's log (author time 2026-10-07T21:57:14-04:00 by `git log`) to ~02:55Z. Cadence 60m, cron `12f228ad`.
**state: ARMED**

## Measurements

- Sequence (`.tools/sequence-check.py --project`, 5 of 5 read): AMGT_CORPUS, AMGT_HARVST, AMGT_RESAPP NEEDS-SLOT=1 each;
  DSGN_AMGTV1 and ETFS_RIVALS none. No DRIFT, no WAITING. Unchanged.
- Inbox: 0 unread (`check_inbox`: empty; folder count 0).
- Origin CLOUD `82c4790d6c` (ls-remote). Wheel files in `C:/tmp/mstrz-relay/taildrop-in`: 5 (of 6).
- Not run this tick: `directives-check`, `active-commitments`.

## Calls ruled since tick 19

| call | ruling | carrier |
|---|---|---|
| AMGT_HARVST, the 15 fallback pairs graded (`3.0.0_SA_CVO~Z` 31549) | the stored-case rule stands; the two true BP pairs are removed and NAMED as lost; no context test for two pairs | msgs 31550, 31551 |
| AMGT_HARVST R3, `CSLLY` as a second anchor (`2.0.0_SA_COO~H` 31553, row Z-W110-S4) | yes: the issuer's own listing symbol in exact case; merge at 39 of 39 and 3 of 3; a symbol anchor states its source | msgs 31554, 31555 |
| the same, the symbol's source (`3.0.0_SA_CVO~Z` 31557; 31559) | merged @1866108355; `CSLLY` is in no stored source (pool 0, registry 0, collector record 0), so its row says "evidenced by article spans only" | msg 02:32Z |
| AMGT_RESAPP bb-18, the sixth wheel | asked of the laptop through `0.0.0_AB_MSTR~Z`: which of three states it is in | msg 02:5xZ |

Governance forks at the CVO: 0. Design forks at the CRO: 0.

## Verdicts and statements received

- `3.0.0_SA_CVO~RV` 31548: rg-2 MET on the served plane; 2 keys written, no table, chart or page object; the page byte-identical.
- `3.0.0_SA_CVO~Z` 31549: of the 15 fallback pairs, 13 not about the company, 2 about BP. 31557: the 8 recovered CSL pairs, 8 of 8.
- `2.0.0_SA_COO~H` 31552: R3's second anchor keeps 0 of the 2 true BP pairs, by construction of the census.
- `0.0.3_BG_BBGTerminal` 31560, the pacer's statement for 2026-10-08: planned MDPF_SECHIST card-A draw ZERO; expected claims about
  755, 3,462 and 66,879 of 120,000.
- `2.0.0_SA_COO~X` 31545: the recreated AMGT_CORPUS pin tree verified by a dry run from it (registered 96, forecast 16).

## A change in a bar, stated

AMGT_HARVST's rebuild rule was "0 pairs lost". The next rebuild's rule allows a lost pair when it is NAMED: two true BP pairs
(sa:4473686, sa:4441205) go with the 13 false ones, because BP writes its name in lower case and that is also "basis points".
Told to Andrew at ~02:0xZ with the option to hold zero strictly.

## Acts landed (others', from their reports)

- ETFS_RIVALS rg-2 live at CLOUD `0576fb051f`, 01:41Z; 0 moved rows; the deployed code is a commit of CLOUD again (31546).
- AMGT_HARVST: bh-3 merged; round 63 issued @08cf3a7702 (bh-9 stored-case fallback, bh-10 HEI).

## Scope state (register read, 5 of 5)

All five `status: active`, `dep_stage: EXECUTING`. **COMPLETION TEST: NOT DONE -- 0 of 5 complete.** All five REACHABLE.
Waiting: AMGT_RESAPP bb-18 on the sixth wheel alone; ETFS_RIVALS on the 11:00Z run and round 27; AMGT_HARVST on round 63;
AMGT_CORPUS on the 13:00Z fire and four captures (port 5174); DSGN_AMGTV1 on RESAPP's deploy.

## Acts only Andrew can do (cited)

- The sign-in of `opal-gateway-bbg`, `/mcp` in the `0.0.3_BG_BBGTerminal` window, before the 2026-10-08 07:00 America/New_York
  send (his Microsoft login); and his word on the prepared one-session config move.
- His answer on a standing daily Bloomberg request of closes for the rivalfunds securities (CLAUDE.md, vendor use by his word).
- His word on force-removing drained worktrees that hold untracked scratch files (CLAUDE.md, recursive deletion).
- His word on whether "no fetch on any box" covers an AWS host at deploy; his word that the smoke on port 5174 is finished.

## Compiler Tools

- `sequence-check.py` x5; native Read; a directory listing of the Taildrop holding folder.
