# 2.0.0_SA_COO~C1 -- handoff, ADVI_COTBKF waiting state (written 2026-10-16 ~10:05Z, dell1)

Resume from this file, the ledger and branch `box/dell1` only. Nothing is uncommitted; no worker or worktree is live; origin and local read the same head (a28c3c33be) at writing.

## State (all measured this session)

- **Project:** `ADVI_COTBKF`, `dep_stage` EXECUTING, lease FULL. Rounds 96 to 103 are closed by the CTO (`ledger/ROUND_ANALYSIS.round96-98.md`, `.round99.md` to `.round103.md`). The CTO's last word (msg 6640): no round 104 now.
- **Outcomes:** 5 of 9 REALIZED (FWD-1, 3, 5, 6, 8). FWD-2, FWD-4 and FWD-7 wait on Andrew landing the CRM archive in the store (and, for FWD-7, naming who can read the restricted places). FWD-9 waits on his sending the match packet. No contact with Cottonwood.
- **FWD-3 as graded:** REALIZED on ACCEPT's terms (0 blanks lack a reason); beside it the stated facts: 93.7% of days blank, 98.3% of those UNPRICED (15,973,399 holding-days over 4,371 securities); UNGRADABLE months 78,622, at most 72,184 of them gradable after a full UNPRICED fill (`deliverables/0.9.0_WK_ADVI_COTBKF~193/MONTH_PARTITION_RECORD.json`).
- **Served tables:** the relabelled FWD-3 tables, applied in round 98 (apply commit a593268704), VersionIds `lNzQMjfx6uX2zdFdWKsDANboShtDUz2N` (daily_returns), `ObKZXku7Am.QGjO.oSAsIScy8IcJxN5a` (account_day_value), `nkTE.F82uFSboXr9PEamIENCwFL9cwcC` (month_grades). `deliverables/2.0.0_SA_COO~C1/cu1_ac3_served_unchanged_check.py` reads them unchanged; rollback VersionIds are in the COO half.
- **Bloomberg history:** nothing in the store reaches before 2025-08-28; the CUSIP-keyed store covers 0 and the ticker-keyed stores 1,960 of 15,973,399 unpriced holding-days (row D1-S19). The CTO routed the 4,371-security history pull to `2.0.0_SA_COO~Q1`'s queue, priced first.

## What I owe, and when

1. **When Q1's queue reports covered holding-days that move the fill rate:** cut the rebuild under a never-widen pair (CTO's word, msg 6640). The pair's template is `ledger/NEVER_WIDEN_R97_FWD3_LABELS_COO_HALF.md` and its CTO half; the order template is `task-orders/ADVI_COTBKF.TO-CB-ct-1.fwd3-labels-apply.md`; the regrade command and pins are in `deliverables/0.9.0_WK_ADVI_COTBKF~129/RETURN_CHANGE.md` and the round-97 order `TO-CB-cs-1`. The private sweeps config is at `C:/Users/Test/.opal/commonwealth_sweeps.json` (sha256 `b1d93408f64a996b2a9659bbed9ca0863fbf0d0db348e1397e1a7e184910a89d`, never committed). The dell2 run data is at `.scratch/advi_cotbkf/` (20,563 files, 4,478,568,892 bytes; off git).
2. **Otherwise:** dispatch nothing. Tick with `python .tools/unblock.py tick --serial 2.0.0_SA_COO~C1 --project ADVI_COTBKF --result work --owed-call <id>` (a dated wait on a live owner is not an empty tick); do not count it.
3. **If Andrew acts** (CRM archive landed, or the packet sent): the CTO's next analysis cuts the cells; FWD-4 will need a CRM silver builder, which does not exist in `data/assets/scripts/silver/` (only `cotbkf_crm_match_job.py`).

## Rule 34 (CLAUDE.md, Andrew-direct 2026-10-16 ~15:4xZ, CTO msg 6814)

CloudOps is seated one lane per macro per box, never one per task. The next CloudOps order for ADVI_COTBKF (the apply of a rebuild under a pair) goes to the ADVI lane `0.7.0_AE_CloudOps~<MACRO><n>` that `0.0.0_AB_MSTR` names, shared with ADVI_FIRMBKTS, not to a fresh lane. `0.7.0_AE_CloudOps~CB1` closes as idle; do not address new orders to it. Ask MSTR~DELL1 for the lane name when the rebuild is cut.

## Lessons to carry (all happened, all recorded)

- A check script and its order must define the same thing: two of mine disagreed (rows D1-S17, the round-103 partition script). Run every issuer script against a matching and an altered record before the cut.
- An order's `<paths>` must name its own file, or the worker cannot flip it (D1-S16).
- The investigation channel holds CRLF lines: append with `open(path, 'ab')`; never read and rewrite it.
- A proof instance's `output_evidence` must equal its `expect` pattern exactly, and an artifact row for a file an earlier commit carried is pinned to that commit's FULL hash.
- A worker's instance lives in its lane's deliverables folder; correcting it needs `GIT_COMMIT_AUTHOR_OVERRIDE` (audited; used twice, say so in the message).
- The comp rail denies `find`, blind recursive grep and a pipe after a census; use native Grep and Glob.

## Loop and watcher

Cron `b6082e41` (`11,41 * * * *`, `/canonical-drive ADVI_COTBKF once`) dies with the session; re-arm only per Andrew's relayed word (MSTR msg 6412, record `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261016_024xZ_KEEP_DRIVING_ON_30M_SELF_DRIVE_CANONICAL_DRIVE.md`) after `CronList`. The inbox watcher expires every 30 minutes and is re-armed on the expiry notice.

## Compiler Tools

- Written from the ledger, the round analyses, the drive logs and the broker mail of this session; checked with `git status` and `git log` only; no tool was run to produce this note beyond reading origin and local heads.
