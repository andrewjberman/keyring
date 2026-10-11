# MDPF_CANON round 3: the bronze moves to the builder's address; the grant was already live -- 0.7.0_AE_CloudOps~DELL1

**Date:** 2026-10-11 (UTC; ~04:50Z - 05:10Z)
**Task Order:** ADHOC.canon-r3-bronze-intake (risk WORLD)
**Status:** COMPLETE
**archetype:** DEPLOY
**Branch:** box/dell1

## Objective

Close `ADHOC.canon-r3-bronze-intake` (MDPF_CANON CN-c-2 + CN-c-3): the Orion model-composition bronze moves from
`s3://opal-data-mdpf/mdpf/bronze/orion_model_composition/` to the builder's address
`s3://opal-data-assets/mdpf/inflection/bronze/orion_model_composition/date=<D>/`, with the runner grant, the history
copy, three file deploys, one on-demand Stage-0 pull and one local feeder read. The previous session of this seat
opened the ledger at 04:39Z and was lost; this session measured every leg's state before acting.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| r3_checks.py | writer / reader / homes / libs | PASS | 3/3, 3/3, 3/3, 5/5 arms (C1) |
| deploy_ledger.py | close-leg x7, close, check | PASS | ledger CLOSED, sentinel removed |
| comp-rail | three denials (recursive grep, find, a `grep -rn`) | WARN | each denial ran nothing; native Grep and `ls` answered |

**What worked:** measuring each leg before acting found two of the order's premises already false (grant live, no history).
**What failed:** a Python `subprocess` call to the bash `.tools/aws` shim died WinError 193; the background wrapper
reported exit 0 because the shell's last command was `tail`. The log, not the exit, showed it. Nothing had been copied.
**Gap found:** `aws s3api list-objects-v2 --query length(Contents)` returns per-PAGE counts (1000 + 30), the CLAUDE.md
22a trap; counted client-side instead.

## Work Completed

1. **Step a, schedule.** Runner `i-02448edb624a7a7cf` stopped. Scheduler crons: feeder backstop 12:52Z, floor 13:30Z,
   accrual 13:40Z, publisher 13:50Z; the accelerator is event-driven off the INF sentinel. Nearest start >= 7h away.
2. **L1 grant (C2).** Targeted plan = No changes. Live `mdpf-runner-scoped` already carries
   `OrionModelCompositionBronzeRW` and `OrionModelCompositionBronzeListScoped`. CloudTrail: `PutRolePolicy`
   04:41:01Z by `cloudops-dell1-agent-user`, two minutes after the ledger opened: applied by the prior session
   (inferred), no proof left. Recorded as such; the 0/1/0 plan could not be reproduced.
3. **L2 history (C3).** Source 1030 objects before and after (same key set); new prefix 1030 = 103 `date=`
   partitions, 927 `model_*.json` + 103 `_meta/pull_complete.json`; 0 missing, 0 extra, 0 size mismatches.
4. **L3-L5 files (C4).** `bronze_homes.json` (prior absent), writer (prior ETag 0f2ba775..), feeder (prior ETag
   2024adcc..), each read back byte-equal to the repo; prior versions recorded in the ledger for rollback.
5. **L6 pull (C5).** SSM `f1b89351-3669-479a-868a-598939f07e92`, exit 0, `date=2026-10-11/` holds nine models plus
   the sentinel. Runner left RUNNING (stopping EC2 is a confirm-class act; the next dispatch stops it itself).
6. **L7 feeder (C6).** `--date 2026-10-09`, no `--upload`. Default eclipse date 2026-10-10 differed in two outputs
   (input vintage). With `--eclipse-date 2026-10-09`: 750 rows, DELTA=0 on all data-bearing columns; only
   `_ingested_at` differs. Nothing written to S3.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Fetched exactly two files onto the runner, not the dispatch's `s3 sync --delete` | the order says deploy exactly the files; the sync would also move the ~20-commit-behind scripts |
| Compared at `--eclipse-date 2026-10-09` | the live feed's `as_of_date`; the default differed by input vintage, not by bronze |
| Left the runner running | stopping EC2 needs a human confirmation per CLAUDE.md |

## Open Items

- Row `MDPF_CANON-D1-S12` filed; `MDPF_CANON-D1-W9-S7` is `2.0.0_SA_COO~D1`'s to disposition.
- Old bronze prefix is NOT deleted (DEC-8: an S3 delete needs a human's confirmation).
- Runner `i-02448edb624a7a7cf` running until the 12:52Z dispatch ends or Andrew confirms a stop.
