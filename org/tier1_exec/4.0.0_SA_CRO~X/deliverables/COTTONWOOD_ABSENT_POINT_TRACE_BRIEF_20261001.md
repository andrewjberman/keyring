# Cottonwood's served aggregate: why the point is absent on days whose silver exists

**Author:** 4.0.0_SA_CRO~X (Chief Research Officer, lane X)
**Home:** org/tier1_exec/4.0.0_SA_CRO~X/deliverables/
**Asked by:** 1.0.0_SA_CTO, msg 103614 (RULINGS batch 69 item 4 @6291fa70e5), on `3.0.0_SA_CVO`'s finding F-A in
`org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_COTREMEDIATION_AC_GRADE_20261001.md` @7bc5eb882b. A decomposition
input of MDPF_HEALGAP.

Prepared by 4.0.0_SA_CRO~X on 2026-10-01 (read 07:56Z to 08:24Z). Read-only: object listings, the `value_date`
column of 47 gold partitions, the served series and its gold slice (firm-level only), and source at CLOUD. No run, no
vendor call, no write. Local copies were deleted after each read.

## The answer

**The figure is dropped between silver and gold, at `data/mdpf/scripts/gold/mdpf_gold_consolidator.py:2078`.** The
daily run calls the gold builder once, for today's assignment date, with no value date:

    rc = bdmp.main(["--date", adate, "--upload"])

The builder then values that partition at the freshest holdings date that exists at that moment
(`data/assets/scripts/gold/build_dim_model_portfolio.py:505`, `latest_holdings_date` at `:116-133`). One run, one
value date. A holdings date that is never "the freshest at run time" is never valued by any run, and nothing goes
back for it.

On the four dates that is exactly what happened: holdings landed late, several days at once, and the next run
valued only the newest.

| Value date | Its holdings partition landed | Gold runs that could have valued it | What they valued instead |
|---|---|---|---|
| 2026-08-20 (Thu) | 2026-08-25T17:20Z (the repair) | assignment 08-21, 08-22, 08-23, 08-24 at 13:30Z | 08-19, four times; then assignment 08-25 valued 08-24 |
| 2026-08-21 (Fri) | 2026-08-25T17:20Z | the same | the same |
| 2026-09-23 (Wed) | 2026-09-28T11:46Z | assignment 09-24, 09-25, 09-26, 09-27 at 13:30Z | 09-22, four times; then assignment 09-28 valued 09-25 |
| 2026-09-24 (Thu) | 2026-09-28T11:46Z | the same | the same |

No gold partition carries `value_date` 08-20, 08-21, 09-23 or 09-24 (0 of 47 partitions read). The later hops then
behave as written: the slice keys each gold partition at its own value date
(`data/assets/scripts/gold/build_cottonwood_mdpf_slice.py:344-447`), emits None for an axis date no partition values
(`:600-608`), and the served series classes a valueless date absent
(`data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py:2176-2192`).

Three artifacts agree on every date checked: the gold partitions' own `value_date` column, the slice's
`partition_to_value_date` report, and the served `point_class`.

## Two things the finding did not have

**A fifth date of the same class: 2026-08-18.** Its holdings partition landed 2026-08-20T11:46Z together with
08-19's; the 08-20 run valued 08-19 and no run ever valued 08-18. The served point on 08-18 is absent. The finding's
window began 08-20.

**The other seven absent days are the same hop with a different trigger.** The finding reads `fact_model_assignment`
as having no partition on eight trading days from 2026-08-31 to 09-10 (not re-read here). The builder reads the
assignment for its own date
(`build_dim_model_portfolio.py:503`), so on those days there was no gold run at all: gold partitions jump from
date=2026-08-30 to date=2026-09-11. The value dates those runs would have carried (08-31, 09-01 to 09-04, 09-08,
09-09) were therefore never valued either. So all 12 absent trading days since 08-17 (the finding's 11 plus 08-18)
are lost at this one hop: gold is built once per assignment date and nothing revisits a value date.

There is also a second lapse worth a line: the holdings for 09-23, 09-24 and 09-25 all landed on 09-28. That is a
three-day feed delay inside the repaired table, after the project's repair, and no record names it.

## Start-to-finish walk

### 1. Black Diamond exports -> silver `fact_holdings` and `fact_model_assignment` -- WORKS, late

Both silver tables hold a partition for each of the five dates. The holdings partitions for those dates landed 1 to
4 days after their usual next-morning time (table above); the assignment partitions landed on their own day at
06:00Z.

### 2. Silver -> gold `dim_model_portfolio` -- MISMATCHED (the dropping hop)

What exists: `build_dim_model_portfolio.py`, called once a day from `mdpf_gold_consolidator.py:2078`; partitions are
keyed by assignment date and carry a `value_date` column; the builder accepts an explicit `--value-date` (`:494`).

The exact mismatch: the table's key is the assignment date, and the series it feeds is read by value date. The daily
call supplies only the first. When holdings are on time the two differ by one trading day and every value date gets
exactly one partition. When holdings are late, several assignment dates collapse onto one stale value date (08-19
has five partitions, 09-22 has five) and the dates in between get none. The consolidator's own comment at
`:2048-2052` records an earlier instance of the same shape (holdings for 08-04 and 08-05 both landing on 08-06).

Close: a catch-up step that, after the daily run, lists holdings dates on the axis that no gold partition values
and builds each one with its explicit `--value-date`, paired with the assignment of the next trading day. For the
seven dates with no assignment partition the pairing is a decision, not a default. Proof: the slice's
`dates_absent` reads 0 for every trading day whose holdings exist.

### 3. Gold -> the Cottonwood slice -- WORKS

`build_cottonwood_mdpf_slice.py` reads every gold partition, re-keys it at its own value date, keeps the earliest
assignment where several share one, and emits None where none exists. It reports the collisions; it cannot invent a
date nobody built.

### 4. Slice -> the served series -- WORKS

The served file reads `as_of_last` 2026-09-29, 34 measured points, and absent on the 12 dates. It serves what the
slice holds.

## Recommended completion sequence (PROPOSAL -- the CTO rules)

1. **The remedy cell for MDPF_HEALGAP.** One catch-up pass over the five dates whose holdings and assignment both
   exist: 08-18, 08-20, 08-21, 09-23, 09-24. It rewrites served history, so it is a never-widen act naming those
   five keys, their before values (absent) and the rollback (the prior object versions).
2. **The standing step** (hop 2's Close), so a late holdings landing no longer drops a date.
3. **The seven assignment-gap dates**: a ruling on which assignment values them, or a declared gap.
4. **The frontier read**: the CVO's own note stands -- a read that checks the class of the last point, not only its
   date, would have shown each of these on its day.

MDPF_HEALGAP's recorded root cause is "nothing re-runs after the heal". This is that sentence one layer up: nothing
re-values after a late landing.

## Acceptance

For each of the five dates: the holdings partition, a gold partition whose `value_date` equals it, the slice's
covered set, and the served point reading measured -- one trace per date, with 49 Financial and Inflection
byte-unchanged.

## Evidence anchors and limits

Source at CLOUD HEAD at 08:2xZ; objects read 07:56Z to 08:22Z. Machine-readable evidence:
`org/tier1_exec/4.0.0_SA_CRO~X/deliverables/cottonwood_absent_trace_20261001/EVIDENCE.json`.

Limits. The daily run was not executed and its logs were not read: the "13:30Z run valued X" statements are read
from each gold partition's own `value_date` and write time. The deployed consolidator's bytes were not compared to
CLOUD; the line numbers are CLOUD source. Why the holdings landed late on 09-28 was not traced. The pairing proposed
in hop 2's Close (value date D with the next trading day's assignment) is the pattern the on-time partitions show,
not a ruled convention.

- `data/mdpf/scripts/gold/mdpf_gold_consolidator.py:1992`, `:2048-2052`, `:2078`
- `data/assets/scripts/gold/build_dim_model_portfolio.py:116-133`, `:494`, `:503`, `:505`
- `data/assets/scripts/gold/build_cottonwood_mdpf_slice.py:344-447`, `:600-608`, `:618`
- `data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py:1980`, `:2176-2192`
- `org/projects/MDPF_HEALGAP.json` (root_cause)

## Andrew-direct request -- verbatim record

Channel: Andrew at the `1.0.0_SA_CTO` terminal, 2026-10-01 about 04:23Z, recorded in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_042xZ_SELF_DRIVE_60M_LAPTOP_FABRIC_FINAL_SAY_CLOSER_DRIVE_IRPT_FIRST.md`;
this surface reached this seat as msg 103614.

> Our goal is to close out pretty much everything left open on the laptop fabric.
