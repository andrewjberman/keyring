# Serving Inflection's Performance from its holdings gold -- what the packet needs, what is measured, what blocks it (PREP, not a packet)

Author `2.0.0_SA_COO~P`, 2026-10-01 15:3xZ. Batch 63 item 3(e) and item 7; batch 80 items 4 and 7; batch 92 item 4. Nothing here is
built, uploaded or applied. This file exists so the packet can be written the hour its blockers clear, by this seat or the next.

## The parts, and where each stands

| # | part | state | measured |
|---|---|---|---|
| 1 | The gold itself | DONE: rebuilt at emission 1.2, 1,613 of 1,616 partitions; ledger closed @3cc5b831aa | three hand reproductions accepted (CTO 103769); row S254 |
| 2 | The three stale gap-day partitions | **BLOCKED on Andrew's word** (an S3 delete); packet prepared @3cc5b831aa | pre-condition check prints FAIL, 9 objects (15:14Z) |
| 3 | Adapter members `installed.py`, `holdings_gold.py` at 89b5a85abe | candidate assembled locally (`asm5`), NOT built or uploaded; source-map re-pin uncommitted in the worktree | all 41 closure members of `runtime.py` equal CLOUD; interface gate 0 findings from `runtime.py` and `served.py`; the candidate's own reader serves account 226 year to date as OPAL_HOLDINGS with three `linked_days` absences |
| 4 | The adapter role's read on the Inflection gold | declared in the worktree's `performance/retained.tf` (two statements, mirroring 49 Financial's), uncommitted | live simulate 13:2xZ: `s3:GetObject` and `s3:ListBucket` on the Inflection gold are `implicitDeny`; the same two on 49 Financial's are `allowed` (positive control) |
| 5 | The producer function for Inflection and its schedule | declared by IB-er-501, never applied; **the root does not plan** (row S258) and the schedule fires before its partition lands (row S257) | 1 of 224 functions and 1 of 26 schedules match holdings-performance, both 49 Financial's |
| 6 | The producer artifact | ONE zip serves both functions (`lambda.tf`: the Inflection module reuses the 49 Financial artifact key) | so building the 1.2 pair moves 49 Financial's daily partitions to emission 1.2 in the same act: 20 columns, `span_trading_days` 1, same code path for the return (a dry run of 2026-09-25 at the close-basis commit, before the span column was added, printed the same row count and census as the unchanged producer; the 1.2 build itself is NOT yet compared row for row on a 49 Financial day) |
| 7 | PRD ruling 23 (the gap rule) | the CTO's addendum, with the serving move (batch 80 item 7) | -- |
| 8 | The contract the report validates against | not yet read for this move | `PerformanceReport.schema.json` admits OPAL_HOLDINGS today (49 Financial is served); whether the two new absence facts need a contract line is unread |

## What the packet will have to say that is not obvious

- **Two pullers of one artifact.** The producer zip is pulled by the 49 Financial function (live) and the Inflection function (to
  be created). The packet names both, states 49 Financial's after-state (emission 1.2, one added column, declaration 1.2 with
  `link_across_gaps` false and one OWN_DATE segment), and pins or moves each deliberately.
- **The schedule's time.** Under the measured basis the day the handler targets (the trading day before the fire) has its close in
  the partition dated the fire's own morning, which lands at 13:05Z to 13:08Z. The declared 07:30 America/New_York fire is before
  that. The entry belongs after the mirror's fire; after its second fire (17:05Z, declared @2e00498347, unreleased) if a late raw
  is to be caught the same day. With `link_across_gaps` a too-early fire does not fail loudly: it finds the day absent and the next
  day's fire links across a close that exists by then.
- **The windows that the adapter rules.** `holdings_gold._period_for` admits year to date, quarter to date, one year and since
  inception. A month to date request refuses `HoldingsWindowNotRuled` (seen in the 49 Financial after-read). Unchanged by this move.
- **A fresh Inflection request PERSISTS a report.** The service-level harness used for packet 3 stubs authorization and refuses the
  vendor transport; for this move a fresh request would be SERVED and retained. The read-only instrument is the candidate's own
  `holdings_gold.calculate` (no persistence), as run for account 226; a persisted report is made only by a real, authorized request.
- **Three linked rows remain in the year** (2026-05-12, 2026-07-01, 2026-08-11), disclosed as PARTIAL absences. 2026-07-01's is
  there because its coerced file was not admitted (row S250).

## Blockers, each with its owner

1. Andrew's word on the nine-object delete (the CTO lists it; batch 92 item 6 reopens the disposition if none comes).
2. The holdings-performance root's two files, `locals.tf` (the one-expression fix, row S258) and `schedule.tf` (the re-timing, row
   S257): outside this lane's lease and under an open IRPT_DASHBD order's `<paths>`. Asked of the CTO.
3. The PRD addendum carrying ruling 23 (`1.0.0_SA_CTO`).

## Uncommitted in the private worktree, held for the packet

`infra/aws/lambda/ci/lambda-source-map.json` (adapter rows `installed.py` and `holdings_gold.py` re-pinned to 89b5a85abe) and
`infra/aws/terraform/investor-reporting/performance/retained.tf` (the two read statements). Committing either puts a pending plan on
a live root, so they land with the packet, not before.
