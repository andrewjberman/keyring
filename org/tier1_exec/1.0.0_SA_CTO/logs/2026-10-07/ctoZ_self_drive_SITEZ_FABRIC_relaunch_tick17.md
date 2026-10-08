# /self-drive SITEZ fabric (relaunch) -- tick 17, 2026-10-07 ~23:50Z -- `1.0.0_SA_CTO~Z`

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_082xZ_SELF_DRIVE_60M_SITEZ_FABRIC_RELAUNCH_AFTER_REBOOT.md`
**Covers:** tick 16's log (author time 2026-10-07T18:54:33-04:00 by `git log`) to ~23:55Z. Cadence 60m, cron `12f228ad`.
**state: ARMED**

## Measurements

- Sequence (`.tools/sequence-check.py --project`, 5 of 5 read): AMGT_CORPUS, AMGT_HARVST, AMGT_RESAPP NEEDS-SLOT=1 each;
  DSGN_AMGTV1 and ETFS_RIVALS none. No DRIFT, no WAITING. Unchanged.
- Inbox: 0 unread (`check_inbox`: empty; folder count 0).
- Origin CLOUD `58b23cc581` (ls-remote). Not run this tick: `directives-check`, `active-commitments`.

## Calls ruled since tick 16

| call | ruling | carrier |
|---|---|---|
| AMGT_CORPUS method-7 re-read (`3.0.0_SA_CVO~Z` 31456) | C1 MET; relayed; bb-18 re-pins | msgs 31457, 31458 |
| AMGT_RESAPP bb-18 re-pinned to `fbb643923e` (`2.0.0_SA_COO~Z` 31461) | CTO half ADDENDUM 1 SIGNED; one packaged path moves | `deliverables/CTO_HALF_AMGT_RESAPP_R78_BB18_REDEPLOY_20261007.md` @9013addec3 |
| NFRA_OPLGTW row Z-S67, the remedy (`2.0.0_SA_COO~O` 31463) | ONE session holds the concierge's sign-in; no grace; the drain is not shipped; the config move PREPARED, not applied (31467) | msgs 31464 to 31466 |
| ETFS_RIVALS round 25 deploy (`2.0.0_SA_COO~RV` 31470) | CTO half SIGNED conditional on J1, with C1 a hand read of the largest move | `deliverables/CTO_HALF_ETFS_RIVALS_R25_READERS_GRAIN_DEPLOY_20261007.md` @16d5d5acd9 |
| ETFS_RIVALS rg-1 J1 NOT MET (`3.0.0_SA_CVO~RV` 31476) | nothing applied; every object read for the offset; mr-1 may ship alone | msg 31477 |
| ETFS_RIVALS, which reader rule (31479) | ADDENDUM 4: R11 (own term withdrawn), R12, R13, R14 | `ledger/ROUND_ANALYSIS.round22.md`, this commit |

Governance forks at the CVO: 0. Design forks at the CRO: 0.

## Corrections to this seat's own acts (three)

1. R9 and two reports to Andrew said good closes of 2026-09-29 were being dropped. They were next-day closes filed under the
   wrong date; the page was right to ignore them.
2. The term "as_of equals the partition date" (msg 31477) assumed what `as_of` means. It is the pull day. Withdrawn before any
   build, on `2.0.0_SA_COO~RV`'s read.
3. The round-25 CTO half is marked SPENT WITHOUT AN ACT.

## Acts landed (others', from their reports)

- AMGT_HARVST gold rebuild #8 DONE 22:48Z: mention 33,665 to 48,025, lost 0, removed 17; daily 59,148 to 67,760 (31460). Both
  new parts read by this seat as the newest of their tables.
- AMGT_CORPUS: 95 dossiers stored at method 7; C1 MET.
- 0 of 6 wheel files on site Z at ~23:3xZ; the laptop has given no time (`0.0.0_AB_MSTR~Z` 31475).

## Scope state (register read, 5 of 5)

All five `status: active`, `dep_stage: EXECUTING`. **COMPLETION TEST: NOT DONE -- 0 of 5 complete.** All five REACHABLE.
Waiting: AMGT_RESAPP bb-18 on six wheel files only; AMGT_CORPUS on four captures (port 5174) and the 2026-10-08 13:00Z fire;
AMGT_HARVST on its round slug; DSGN_AMGTV1 on RESAPP's deploy; ETFS_RIVALS on the re-cut round 25.

## Acts only Andrew can do (cited)

- The sign-in of `opal-gateway-bbg`, `/mcp` in the `0.0.3_BG_BBGTerminal` window, before the 2026-10-08 07:00 America/New_York
  send (his Microsoft login); and his word on the prepared config move that leaves that sign-in with one session (it changes his
  own user-level setup).
- His answer on a standing daily Bloomberg request of closes for the rivalfunds securities (CLAUDE.md, vendor use by his word).
- His word on whether "no fetch on any box" covers an AWS host at deploy.
- His word that the smoke on port 5174 is finished.
- His own look at the chart UI on /rivalfunds; DSGN_AMGTV1 FWD-1's walk and the PROD promote of `4b167888`.

## Compiler Tools

- `sequence-check.py` x5; `aws lambda list-functions`, `s3api list-objects-v2` (inspection); native Read.
