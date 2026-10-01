# DRAFT never-widen packet -- Inflection's Performance served from its holdings gold (IB-pr-221; batch 63 items 3e and 7)

Author `2.0.0_SA_COO~P`, 2026-10-01 ~16:0xZ. **A DRAFT: no half is asked on it.** It becomes the packet when its one open
pre-condition passes (the nine-object delete, Andrew's act) and the two artifacts are built, at which point the hashes in section 1
are filled and both halves are asked on the bytes. Everything else below is measured today. Rulings: batch 63 items 3-4 and 7,
batch 80 items 2-7, batch 92 item 4, batch 95 items 3-5; PRD v0.23 ruling 23 (@4177fc7c46).

## 0. Pre-conditions (each read at the hour of the act)

| # | pre-condition | today |
|---|---|---|
| a | `stale_gap_days_precondition.py` prints PASS: no partition under 2026-05-11, 2026-06-30, 2026-08-10 | FAIL, 9 objects (15:14Z); the delete is Andrew's (packet @3cc5b831aa) |
| b | PRD ruling 23 ratified | DONE, v0.23 |
| c | the holdings-performance root plans with 0 errors | DONE @2d74e53d39: `7 to add, 0 to change, 0 to destroy` (15:49Z) |
| d | the gold is the rebuilt one | DONE: 1,613 of 1,616 partitions written 2026-10-01 at emission 1.2; ledger closed @3cc5b831aa |

## 1. The acts, in order, under ONE ledger entry

| leg | act | resource | before | after |
|---|---|---|---|---|
| P1 | build and upload the producer artifact | `investor-reporting/irpt-holdings-performance-lambda.zip` | `gLRGHIyi...` (producer and `sources.json` at 363dc1fda4) | (hash at build) producer and `sources.json` at de3d423dce; 2 members change |
| P2 | targeted apply, 49 Financial's producer function | `module.irpt_holdings_performance.aws_lambda_function.this` | code `gLRGHIyi...` | the P1 artifact |
| P3 | apply, Inflection's producer function, roles, policies, schedule | the 7 resources of IB-er-501 | absent | created; schedule `cron(0 14 ? * MON-FRI *)` UTC, input `source: orion` |
| G1 | targeted apply, the adapter role's policy | `aws_iam_role_policy.performance_retained` | 49 Financial's gold readable; Inflection's `implicitDeny` | two statements added: list and get on `irpt/inflection/gold/holdings_performance_daily/` |
| F1 | build, upload, targeted apply, the adapter | `module.irpt_performance_adapter.aws_lambda_function.this` | `cdbFZDJA...` | (hash at build) `installed.py` and `holdings_gold.py` at 89b5a85abe; 2 of 70 members change |
| V1 | after-reads | sections 6 and 7 | | |

Order: the producer first, so the daily job exists before anything is served from its table; the grant before the adapter, so the
adapter never meets a table it cannot read. Each apply goes through `safe-apply`, targeted.

## 2. TWO pullers of the producer artifact (batch 95 item 5)

The one zip is pulled by `irpt-holdings-performance-lambda` (49 Financial, live, daily at 07:30 New York) and by
`irpt-inf-holdings-performance-lambda` (to be created). P2 and P3 move both in the same window; neither is left on the old zip.

49 Financial's after-state, measured before the act (`f49_rowcompare`, no write, 15:3xZ): the producer at de3d423dce computed
2026-09-25 and 2026-09-29 and each was compared with the SERVED partition on every account -- 7,540 of 7,540 and 7,559 of 7,559
accounts, 18 shared columns, the only column that differs is `schema_version` (1.1 -> 1.2), and the only added column is
`span_trading_days`, 1 on every row. The return, the basket and every count are unchanged. Its declaration is one OWN_DATE segment
and `link_across_gaps` false, so a day it cannot compute stays absent as today (batch 80 item 6). Its schedule is not moved.

The adapter reads only five named columns and tolerates the added one (the 49 Financial reader's `_NEEDED_COLUMNS` check).

## 3. What changes for whoever asks

| who asks | before | after |
|---|---|---|
| Inflection, a ruled window (year to date, quarter to date, one year, since inception), one permitted account | refused, `OBJECT_NOT_COVERED` (uncomposed) | SERVED, provider `OPAL_HOLDINGS`: the chain of the account's OK rows; a linked row is chained and named in a PARTIAL absence; a window edge inside linked days is named. **The first Performance figure this product serves for Inflection.** A fresh request retains a report |
| Inflection, the exact request of the one retained ORION report | refused, `OBJECT_NOT_COVERED` | refused, `OBJECT_NOT_COVERED` (a retained vendor figure never reopens; packet 3) |
| Inflection, any other window | refused, `OBJECT_NOT_COVERED` | refused, `UNSUPPORTED_OPERATION` (`HoldingsWindowNotRuled` in `entry.py`'s map), as 49 Financial's is today |
| 49 Financial | served from its gold | unchanged; its daily partitions carry one more column from the next fire |
| Cottonwood | refused, `OBJECT_NOT_COVERED` | unchanged |

Measured on the candidate (read-only, `holdings_gold.calculate` through the candidate's own `installed._holdings_sources`; no
persistence, no served function touched): account 226, 2026-01-01..2026-09-30, SERVED, 187 partitions read, three `linked_days`
absences (05-12, 07-01, 08-11). Its value equals an independent chain of the gold rows. With the three stale rows present that
chain reads 0.003633; over the rebuild's rows alone 0.024031 -- which is why pre-condition (a) exists.

## 4. Members and closure (on the locally assembled candidate; repeated on the uploaded zips at build)

- Adapter: 70 members, 2 change. `runtime.py`'s import closure: 41 bundled members, 0 differ from CLOUD (the first time since
  packet 1: `installed.py` and `holdings_gold.py` were the last two behind). Interface gate: 0 findings from `runtime.py` and from
  `served.py`. Tests at 89b5a85abe: performance suite 237 passed.
- Producer: 14 files, 2 change (`holdings_performance.py`, `sources.json`). Tests at de3d423dce: 60 passed. `handler.py` is
  unchanged: fired at 14:00 UTC on trading day T it targets T-1, whose close is in the partition dated T (landed 13:05Z to 13:08Z).

## 5. Rollback, per key

- P1/P2: `s3api copy-object` of the prior artifact version over the key, then the same targeted apply. The 49 Financial partitions
  written meanwhile at emission 1.2 are valid under both producers' readers and need no rollback.
- P3: destroy of the 7 created resources is a deletion and needs Andrew's word; without it, the schedule's `state` set DISABLED
  by a targeted apply stops the job, and the rows it wrote are the rebuild's own code path.
- G1: revert the two statements, targeted apply.
- F1: `s3api copy-object` of the adapter's prior version (`wjneBb9_...`, CodeSha256 `cdbFZDJA...`) and the targeted apply:
  Inflection answers `OBJECT_NOT_COVERED` again. A report retained for Inflection in between stays retained and reopenable only by
  a composed adapter; it is named in the ledger if one exists.

## 6. Conditions

1. Pre-conditions (a) to (d) read at the hour; (a) printed with its control line.
2. Each plan is exactly the leg's resources; the producer's census shows 2 members changed, the adapter's 2 of 70.
3. One 49 Financial day computed dry by the DEPLOYED producer function (`dry_run: true`) before and after P2: same rows and census.
4. The Inflection function invoked ONCE with `{"source": "orion", "date": <the newest computable day>, "dry_run": true}`: its
   census equals the rebuild's for that day. Then its first scheduled fire is read from its own log the next trading day.
5. After G1: simulate the adapter role on the Inflection gold, get and list, each `allowed`; the Cottonwood bucket still denied
   (negative control).
6. After F1: the two probe invokes (empty headers; trusted headers with a non-existent user) equal before and after; the
   candidate read of section 3 re-run on the DEPLOYED bytes; ten minutes of log with zero error-class lines.
7. The first real Inflection request is read from the log and from the retained report: provider, the absences, and the value
   against an independent chain. Until one arrives the served path is exercised only up to the enforcer, and the packet says so.
8. Row S257 disarms on condition 4's scheduled fire; row S258 is disarmed by pre-condition (c).

## 7. Not measured, and said

- A real, authorized Inflection request end to end (no scripted human identity exists; a persisted report is made only by one).
- The Performance tab's rendering of a served Inflection figure and of the two new absence facts (`2.0.0_SA_COO~D`'s page).
- Inflection's gold before 2024-07-11 rests on weekend pairs only (the first segment is `inferred`); a since-inception window
  reaches into it.
- 2026-07-01's linked row would become an ordinary row if its coerced file were ever admitted (row S250); it is not.
