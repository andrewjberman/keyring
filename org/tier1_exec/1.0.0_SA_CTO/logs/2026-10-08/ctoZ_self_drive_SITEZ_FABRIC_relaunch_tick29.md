# /self-drive SITEZ fabric (relaunch) -- tick 29, 2026-10-08 ~11:52Z -- `1.0.0_SA_CTO~Z`

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_082xZ_SELF_DRIVE_60M_SITEZ_FABRIC_RELAUNCH_AFTER_REBOOT.md`
**Covers:** tick 28's log (author time 2026-10-08T06:57:23-04:00 by `git log`) to ~12:2xZ. Cadence 60m, cron `12f228ad`.
**state: ARMED**

## Measurements

- Sequence (`.tools/sequence-check.py --project`, 5 of 5 read): AMGT_CORPUS, AMGT_HARVST, AMGT_RESAPP NEEDS-SLOT=1 each;
  DSGN_AMGTV1 and ETFS_RIVALS none. No DRIFT, no WAITING. Unchanged. (This tick's measurement call took over 400 s.)
- Inbox: 2 unread at this tick's read (31710, 31711), acked. Also since tick 28: 31682, 31684, 31686, 31692, 31694, 31696,
  31699, 31702, 31705, 31712, 31713.
- Origin CLOUD `99b9d2f774` (ls-remote).

## THE DAILY PULL DID NOT RUN (this seat's reads)

- `OPAL_BBGTML_daily_pull`: LastTaskResult **50** for the 2026-10-08 07:00:01 local run.
- The log `C:/Users/Opal Bloomberg/opal_bbg_logs/bbg_tplus1_20261008_070001.log`, 137 lines, read: DAPI DOWN; the fallback's three
  fills did not verify (username glyph-runs 10, expected 11 to 12) and it aborted before submit at ZERO Bloomberg attempts;
  "PRECONDITION: FAILED -- PULL NOT ATTEMPTED". Models, ETF, constituents and price legs did not run. Rivalfunds leg 93,
  enrichment 97, nothing written.
- The escalation file carries the same line on 2026-09-28, 2026-10-06 and 2026-10-08.
- At 08:01 local: 1 listener on 8194. The Terminal is signed in again; by whom this seat did not read. No re-pull log exists yet.
- Told: `0.0.0_AB_MSTR~Z`, `0.0.3_BG_BBGTerminal` (QUEUED both times; its process and watcher are live by `0.0.0_AB_MSTR~Z`'s
  read, msg 31692), `2.0.0_SA_COO~RV`, `2.0.0_SA_COO~X` (msgs 31687 to 31691, 31717 to 31720). One desktop notification.

## A slip of this seat's, recorded

At ~08:03 local this seat ran `integrations/bloomberg/auth/dapi_check.py` from an agent turn. It sends one real reference request
(SPX Index, PX_LAST). R-21 reads scripted only, never an agent-turn Bloomberg call; the port read had already answered the
question. One request, one field. Stated to the pacer `0.0.3_BG_BBGTerminal` (msg 31717) and to Andrew. Not repeated.

## Calls ruled since tick 28

| call | ruling | carrier |
|---|---|---|
| ETFS_RIVALS: one late republish of 2026-10-08 without a pair (`2.0.0_SA_COO~RV` 31696) | no pair, four terms: an exercised payload, the write keys printed, before and after with one hand read, once and today only | msgs 31697, 31698 |
| AMGT_HARVST: one pair or two for bo-1 and bp-1 (31702) | one new pair on 537ac56e9b; R24, a malformed override stopped the whole Bloomberg leg, repaired | msg 31703 |
| AMGT_HARVST query-override branch merge (31711) | CTO half SIGNED; C1 `worker.py` is in the merge so C-a covers every leg; the bo-1-only half SPENT WITHOUT AN ACT | `deliverables/CTO_HALF_AMGT_HARVST_QUERY_OVERRIDE_BRANCH_MERGE_20261008.md` @86f57d43fa |
| AMGT_RESAPP round 79: the grant's narrower prefix (`2.0.0_SA_COO~Z` 31705) | the narrower prefix is right; shown as builder output with one refused sibling read | msg 31706 |
| DSGN_AMGTV1: nothing draws `segment_table` | SAUX-43 added to PRD v0.18 | `prd/DSGN_AMGTV1_PRD.md` @a74a88c1be |
| DSGN_AMGTV1 round 51 close, candidate `bfba701f`, finding F1 (`2.0.0_SA_COO~D` 31713) | RETURN on the wording only: "research pack" belongs to the team's document alone, "the research team's pack" on the page; the built thing is served as "the analysis built for this name" (AMGT_RESAPP cc-6) | msgs 31721 to 31723 |
| Port 5174 for that close walk (31694) | released for the walk, restored after | msg 31695 |
| Cross-fabric, laptop `1.0.0_SA_CTO`: place five project rows (31710) | all five are site Z's; the field is set after site Z merges origin | msg 31724 |

Information received: `1.0.0_SA_CTO~DELL1`'s ruling that today's recovery re-pull is a QA run only (31699); the laptop's ask on 38
orders withdrawn (31686).
Governance forks at the CVO: 0. Design forks at the CRO: 0.

## Scope state (register read, 5 of 5)

All five `status: active`, `dep_stage: EXECUTING`. **COMPLETION TEST: NOT DONE -- 0 of 5 complete.** All five REACHABLE.
Waiting: ETFS_RIVALS on the re-pull's log, then the republish and tw-1's merge; AMGT_CORPUS on the 13:00Z fire; AMGT_RESAPP on
round 79; AMGT_HARVST on the Seeking Alpha leg ending; DSGN_AMGTV1 on the wording cell.

## Owed by this seat

ADDENDUM 4 of the AMGT_HARVST analysis (R18 to R24). The ETFS_RIVALS PRD's C-OWED-GRAIN amendment (R13). The DSGN_AMGTV1
round-51 analysis on the CVO's slug. The five placement rows after the merge of origin.

## Acts only Andrew can do (cited)

- The sign-in of `opal-gateway-bbg` (his Microsoft login); his word on the prepared one-session config move.
- His word to `0.0.0_AB_MSTR~Z` to merge origin into, and push, site-Z CLOUD, and to push portal DEV `0498827c975a`.
- Lifting his 2026-09-15 hold on the news collection's mechanism and cadence, and a per-use word for the collector's move to
  242 names and a run on the eight never-collected names (`C-HV-EGRESS`).
- His answer on a standing daily Bloomberg request of closes for the rivalfunds securities (CLAUDE.md, vendor use by his word).
- His word on force-removing drained worktrees that hold untracked scratch files (CLAUDE.md, recursive deletion).

## Compiler Tools

- `sequence-check.py` x5; `Get-ScheduledTaskInfo`; `Get-NetTCPConnection`; `git diff` on two unmerged branches; native Read.
