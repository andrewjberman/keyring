# /self-drive SITEZ fabric (relaunch) -- tick 28, 2026-10-08 ~10:51Z -- `1.0.0_SA_CTO~Z`

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_082xZ_SELF_DRIVE_60M_SITEZ_FABRIC_RELAUNCH_AFTER_REBOOT.md`
**Covers:** tick 27's log (author time 2026-10-08T05:59:13-04:00 by `git log`) to ~10:5xZ. Cadence 60m, cron `12f228ad`.
**state: ARMED**

## Measurements

- Sequence (`.tools/sequence-check.py --project`, 5 of 5 read): AMGT_CORPUS, AMGT_HARVST, AMGT_RESAPP NEEDS-SLOT=1 each;
  DSGN_AMGTV1 and ETFS_RIVALS none. No DRIFT, no WAITING. Unchanged.
- Inbox: 1 unread at this tick's read (31681), read and acked. Also since tick 27: 31660, 31663, 31666, 31670, 31671, 31678.
- Origin CLOUD `fb1f8e00a6` (ls-remote).
- The scheduled task `OPAL_BBGTML_daily_pull`: state Ready, last run 2026-10-07 07:00:01 local with result 0, next run
  2026-10-08 07:00:00 local. This box's clock read 06:54:59 local at 10:54Z, so **07:00 local is 11:00Z**.
- Not run this tick: `directives-check`, `active-commitments`.

## Calls ruled since tick 27

| call | ruling | carrier |
|---|---|---|
| Portal candidate not a fast-forward of DEV (`0.0.0_AB_MSTR~Z` 31660) | a diff check, not a new review; then `0498827c975a` APPROVED on this seat's own patch-id and file-touch reads | msgs 31661, 31668 |
| AMGT_HARVST: AIG's query needs collector code (31663) | R23: cut now as a per-security override, `_LEGAL_SUFFIX` untouched; the merge held on the Seeking Alpha leg and a pair | msg 31664 |
| AMGT_HARVST bo-1's merge (31678) | CTO half SIGNED, C1 and C2; C1 answered by 31681 (the COO half's wording was wrong, the record and the code agree) | `deliverables/CTO_HALF_AMGT_HARVST_BO1_QUERY_OVERRIDE_MERGE_20261008.md` @d6ea0eff2f |
| AMGT_RESAPP round 79: serve bb-16 now or wait (`2.0.0_SA_COO~Z` 31671) | serve, with a read-only grant on one prefix as its own pair leg; three served states kept apart | msgs 31672, 31673 |
| DSGN_AMGTV1 page findings (round-78 analysis R3) | PRD v0.18, SAUX-37 to SAUX-42; no ENDPOINT change | `org/missions/D13/DSGN/DSGN_AMGTV1/prd/DSGN_AMGTV1_PRD.md` @9a07662460; msg 31675 |

Governance forks at the CVO: 0. Design forks at the CRO: 0.

## Correction of this seat's own statement, told to Andrew this tick

From about 09:1xZ this seat counted the minutes to "the 07:00 ET send" one hour short, and at ~10:5xZ said it had passed. This
box reads 07:00 local as 11:00Z. The send had not passed when that was said.

## Scope state (register read, 5 of 5)

All five `status: active`, `dep_stage: EXECUTING`. **COMPLETION TEST: NOT DONE -- 0 of 5 complete.** All five REACHABLE.
Waiting: ETFS_RIVALS on the 11:00Z run's read, then tw-1's merge; AMGT_CORPUS on the 13:00Z fire; AMGT_RESAPP and AMGT_HARVST on
their recuts; DSGN_AMGTV1 on `2.0.0_SA_COO~D`'s answer to msg 31675 (is a DSGN lane live).

## Owed by this seat

- ADDENDUM 4 of the AMGT_HARVST analysis (R18 to R23). The ETFS_RIVALS PRD's C-OWED-GRAIN amendment (R13).
- The read of the 11:00Z vehicle run: exit code, duration, the `security_names` step, no `HISTORY OWED` line.

## Acts only Andrew can do (cited)

- The sign-in of `opal-gateway-bbg`, `/mcp` in the `0.0.3_BG_BBGTerminal` window (his Microsoft login); and his word on the
  prepared one-session config move.
- His word to `0.0.0_AB_MSTR~Z` to merge origin into, and push, site-Z CLOUD, and to push portal DEV `0498827c975a`.
- Lifting his 2026-09-15 hold on the news collection's mechanism and cadence, and a per-use word for the collector's move to
  242 names and a run on the eight never-collected names (`C-HV-EGRESS`).
- His answer on a standing daily Bloomberg request of closes for the rivalfunds securities (CLAUDE.md, vendor use by his word).
- His word on force-removing drained worktrees that hold untracked scratch files (CLAUDE.md, recursive deletion).

## Compiler Tools

- `sequence-check.py` x5; `Get-ScheduledTaskInfo`; `git patch-id`; native Read.
