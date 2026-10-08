# /self-drive SITEZ fabric (relaunch) -- tick 18, 2026-10-08 ~00:50Z -- `1.0.0_SA_CTO~Z`

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_082xZ_SELF_DRIVE_60M_SITEZ_FABRIC_RELAUNCH_AFTER_REBOOT.md`
**Covers:** tick 17's log (author time 2026-10-07T19:54:17-04:00 by `git log`) to ~00:55Z. Cadence 60m, cron `12f228ad`.
**state: ARMED**

## Measurements

- Sequence (`.tools/sequence-check.py --project`, 5 of 5 read): AMGT_CORPUS, AMGT_HARVST, AMGT_RESAPP NEEDS-SLOT=1 each;
  DSGN_AMGTV1 and ETFS_RIVALS none. No DRIFT, no WAITING. Unchanged.
- Inbox: 0 files unread in the folder; 2 broker messages at this tick's read, acked (31500, 31503).
- Origin CLOUD `c7cbd4c8a1` (ls-remote). Not run this tick: `directives-check`, `active-commitments`.

## Calls ruled since tick 17

| call | ruling | carrier |
|---|---|---|
| ETFS_RIVALS, mr-1 alone (`2.0.0_SA_COO~RV` 31482) | CTO half SIGNED at content pin `fd633ec4d2`; the withdrawn reader absent by content | `deliverables/CTO_HALF_ETFS_RIVALS_R25_MR1_ONLY_DEPLOY_20261007.md` @86a90330bc |
| ETFS_RIVALS, the rg-1 reader on CLOUD and the working-tree legs (31488) | no revert: imported, never called; tomorrow's vehicle log is read for that step | msg 00:05Z |
| AMGT_HARVST round 60, L10 (`2.0.0_SA_COO~H` 31483; slug 31492) | round analysis R1 to R7, then ADDENDUM 1 with R8 (a brand belongs to the issuer); round 61 is eight items | `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round60.md` @c75d056652 |
| AMGT_RESAPP bb-18, three vendored RECORD files (`2.0.0_SA_COO~Z` 31497) | the STOP amended for exactly those three paths, on sorted-line equality | `deliverables/CTO_HALF_AMGT_RESAPP_R78_BB18_REDEPLOY_20261007.md` ADDENDUM 2 @72afea4d2e |
| AMGT_HARVST bh-8, merge while two legs run the package (31500) | GO, three terms | msg 00:54Z |

Governance forks at the CVO: 0. Design forks at the CRO: 0.

## Own-act note

- The HARVST round-60 analysis was written before the CVO's slug, which had not been asked for by a terminal notice. The slug
  carried one row the analysis lacked (Z-W107-S2); added as R8 the same hour.

## Acts landed (others', from their reports)

- ETFS_RIVALS mr-1 live at `fd633ec4d2`, 00:10Z; no table object written; mr-1 J1 MET on the served page, 210 of 210 (31495, 31499).
  The live pin is not a commit of CLOUD's history.
- AMGT_RESAPP: 5 of 6 wheel files arrived, 5 of 5 matching the laptop's manifest; the sixth waits on the laptop CTO's signature,
  "this hour if the fetch tools run clean" (`0.0.0_AB_MSTR~Z` 31491, 00:08Z).

## Scope state (register read, 5 of 5)

All five `status: active`, `dep_stage: EXECUTING`. **COMPLETION TEST: NOT DONE -- 0 of 5 complete.** All five REACHABLE.
Waiting: AMGT_RESAPP bb-18 on the sixth wheel; AMGT_HARVST on round 61; AMGT_CORPUS on four captures (port 5174) and the
13:00Z fire; DSGN_AMGTV1 on RESAPP's deploy; ETFS_RIVALS on round 26 (rg-2) and the 11:00Z run.

## Acts only Andrew can do (cited)

- The sign-in of `opal-gateway-bbg`, `/mcp` in the `0.0.3_BG_BBGTerminal` window, before the 2026-10-08 07:00 America/New_York
  send (his Microsoft login); and his word on the prepared one-session config move.
- His answer on a standing daily Bloomberg request of closes for the rivalfunds securities (CLAUDE.md, vendor use by his word).
- His word on whether "no fetch on any box" covers an AWS host at deploy.
- His word that the smoke on port 5174 is finished.
- His own look at the chart UI on /rivalfunds; DSGN_AMGTV1 FWD-1's walk and the PROD promote of `4b167888`.

## Compiler Tools

- `sequence-check.py` x5; native Grep and Read; `aws lambda list-functions` (inspection).
