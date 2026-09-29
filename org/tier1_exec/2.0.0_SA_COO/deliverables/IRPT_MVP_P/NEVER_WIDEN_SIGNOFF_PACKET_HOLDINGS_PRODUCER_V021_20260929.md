# Never-widen sign-off packet -- the scheduled 49F holdings producer on the v0.21 rules (row S205)

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Author and operator:** `2.0.0_SA_COO~P`, 2026-09-29 ~14:2xZ.
**Ledger:** `irpt-holdings-performance-producer-v021-20260929` (U1 and P1 closed; D1 open). **Row:** IRPT_BCKEND-S205
(ARMED, disarm_owner ~P) @36f0424d3a.

## 1. What was found

The r3 all-accounts census (the adapter's own code on the built r3 bytes, end 2026-09-28) found 14 accounts at
+1,362% to +1,369% in QTD, YTD, 1Y and SI. That is 0 UNEXPECTED, so no refusal would hide them.
- **Cause:** the scheduled producer `irpt-holdings-performance-lambda` (CodeSha a1ZUOSw5, deployed 03:02Z) packages
  `holdings_performance.py` at 23004aaf98, the round-1 thread version. That is before v0.20 rulings 13-17
  (f302ab14cd) and v0.21 ruling 18 (bf1683f172).
- **What it wrote:** its 11:30Z fire wrote `date=2026-09-28` with 14 OK days at +13.62 to +13.685.
- **Why nothing caught it earlier:** every other partition was re-emitted 09:05-09:25Z by DS~E's local v0.21 run. The
  Lambda was never updated.
- **Nothing served reads this gold yet.** The adapter is on the engine (qfxZ0DzB), and the 49F r3 switch is held on
  S205.

## 2. What ships

| surface | before | after |
|---|---|---|
| Lambda `irpt-holdings-performance-lambda` | `a1ZUOSw5` (S3 UoJZFUus) | `gLRGHIyi` (S3 `ifXqxmjU0kbueSnAiI54fYQu_Hj8oHaK`) |
| schedule `irpt-holdings-performance-daily`, target input | `{kind, note}` | `{kind, note, source: "schwab_08335338"}` |

- **Census vs live:** 14 -> 14 members. ONLY `holdings_performance.py` and `sources.json` differ; both are re-pinned to
  363dc1fda4, the producer DS~E built and drained under v0.20/v0.21 (er-301 amendment 1, er-401).
- **Why the schedule input changes:** from v0.20 the declaration carries three custody sources (schwab_08335338,
  orion, blackdiamond_z09), and the producer refuses to pick one. Measured on the built handler, today's source-less
  payload is REFUSED; with `source` it runs. The value is the declaration's key, not a firm token.
- **Plan:** 0/2/0, the schedule input plus the Lambda code; no IAM change. The role's read grants derive from the
  declared sources carrying `master`, and that is still schwab_08335338 alone. This root plans and applies with
  terraform v1.14.5: v1.9.8 cannot evaluate `locals.tf:37`.

## 3. Evidence on the BUILT bytes (U1)

The built handler was run with only the extracted zip on `sys.path`:
- It resolves `2026-09-28`. The schedule payload plus source, as a dry run, returns rc 0.
- Status census: rows 7,548: OK 6,654, NO-PRIOR-HOLDINGS 885, NON-POSITIVE-BASE 6, ALL-HOLDINGS-EXCLUDED 3.
- `compute_day` on the built bytes: **0 OK rows at |r| >= 1** (the live gold holds 14 today), and the maximum OK
  return is +3.74%.
- The 14 S205 accounts read 0.00%: ruling 14 treats their cusip-less 1.00 rows as cash, where the old code priced
  them by key. This is the S195 class again.

## 4. Blast radius -- both branches

- **Moves:**
  - the next and every later scheduled fire computes under v0.21, and names its source;
  - `date=2026-09-28` is rewritten by D1's one invoke. That is gold no served path reads today.
- **Unchanged:** IAM; the schedule's time and target; every other partition; every served answer.
- **If the fire fails:** the handler returns rc != 0 and nothing is written, the same failure shape as today.

## 5. Apply protocol

1. Both halves at HEAD naming this file's blob.
2. The S3 latest version equals `ifXqxmjU` at apply, written in the ledger. Fresh plan equal to P1. safe-apply with
   SAFE_APPLY_TERRAFORM=v1.14.5 (halt gate; HALT_ACK=1 only on 0 STOP items).
3. Read back: the CodeSha256 is `gLRGHIyi`, and the schedule input carries the source.
4. **ONE invoke with the schedule's exact new payload** (upload; the target day resolves to 2026-09-28): rc 0. It
   rewrites `date=2026-09-28`.
5. AFTER: re-read `date=2026-09-28`: 0 OK rows at |r| >= 1, and the 14 S205 accounts ordinary. Re-plan: No changes.
6. Then S205 disarms, and the r3 census re-runs before the r3 packet goes to the halves.

**Rollback:** S3 version UoJZFUus restored as latest; revert schedule.tf's `source` line; re-apply. The gold for
2026-09-28 re-emits under whichever producer is live.

## What the halves sign against

This file's committed blob; 363dc1fda4; the artifact `gLRGHIyi` (S3 `ifXqxmjU`); the schedule edit; section 3's
evidence; the apply protocol of section 5.
