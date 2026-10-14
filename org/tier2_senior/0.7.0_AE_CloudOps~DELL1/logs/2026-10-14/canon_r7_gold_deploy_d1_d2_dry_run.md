# MDPF_CANON round 7: one named gold script, the package with the registry row, one dry run -- 0.7.0_AE_CloudOps~DELL1

**Date:** 2026-10-14 (UTC; ~16:02Z - 16:3xZ)
**Task Order:** ADHOC.canon-r7-gold-deploy (risk WORLD)
**Status:** COMPLETE
**archetype:** DEPLOY
**Branch:** box/dell1

## Objective

Deploy CN-h-1 and CN-l-1 as one change: the single script `dim_mdpf_aum_metrics.py` to `code/scripts/gold/`, the
`mdpf-gold-lambda` package at pin `9592daf75c` with `MDPF_GOLD_COMMIT` set to the full built SHA in the same apply, and one
`qa_local` dry run. The aggregate library is not copied; the emitter is not touched.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| r6_cn_h_1.py / r7_cn_l_1.py | seams / unit (C1) | PASS | 6 of 6 and 8 of 8 arms |
| mdpf-code-equality.py | whole tree before and after; --files | PASS | 44/33 -> 45/32; one name changed (the D1 name) |
| safe-deploy.sh | the one named file | PASS | gate PASS, VERIFY OK |
| build_package.py / safe-apply.sh | --pin 9592daf75c; planfile apply | PASS | plan 0/1/0, only code + MDPF_GOLD_COMMIT |
| own byte and plan graders | built zip vs git show pin; terraform show -json | PASS | after one fix (below) |
| AWS-RunShellScript (read-only) | ls, test -d, ps on the runner | PASS | `/opt/mdpf/lib` ABSENT (leg 2g) |
| comp-rail | one denial (an AWS list I did not need, tacked onto a read) | WARN | ran nothing; dropped the line |

**What worked:** the before print equalled the pair's measured baseline in every field the pair names (D1 key ETag and
VersionId, function hash, package object, Scheduler input), so the order began from a verified premise, not an assumed one.
**What failed:** my plan grader skipped any attribute whose `after_unknown` entry was an all-false container, so a change
inside one of those attributes could have read as no change. In this plan it hid `environment`, which the env-key diff showed
did change. Corrected to compare every attribute by value; both this plan and the round-30 plan re-graded, with the same
conclusions (round 30: only `source_code_hash` by value across all 46 attributes of the five movers).
**Gap found:** none new. The stated DIFFER of the aggregate library persists by ruling.

## Work Completed

1. **GO and preconditions** (msg 5644 acked READ; both pair halves signed): 2a-2f re-measured; 2g read through SSM.
2. **Ledger** `mdpf-canon-r7-gold-deploy-dell1-20261014` opened 16:06Z with 5 legs; L1 closed with the before print.
3. **D1** 16:08Z: `safe-deploy` of the one file; NAMED EQUAL; prior VersionId recorded.
4. **D2** 16:10Z-16:14Z: built from the pin; checks of the built zip; upload; the `.tf` edit (`50a4da9a95`); targeted plan 0/1/0
   graded; applied through `safe-apply`; read back; re-plan clean.
5. **D4** 16:15Z-16:17Z: one invoke, 200, green, errors empty, 16 of 16; 16 served objects, control key, stores and emitter
   unchanged; two new workbook snapshot objects, as the pair expects.
6. **L5**: after print 45/32; the D1 name EQUAL; the aggregate library still DIFFER, by ruling. Ledger CLOSED.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Started at 16:02Z, not waiting for the night | the order's window runs to 12:44Z tomorrow; today's fire had written its manifest; nothing was running |
| Did not open the publisher order's ledger | it waits for the issuer's GO naming the pin |

## Open Items

- The first-fire acceptance is the issuer's read on the 2026-10-15 13:30Z fire.
- `ADHOC.canon-r7-publisher-deploy` is staged behind this order and waits for `2.0.0_SA_COO~D1`'s GO message.
- Scratch under `C:/tmp/r7-gold/` (built zip, plans, invoke response) is local and not committed.
