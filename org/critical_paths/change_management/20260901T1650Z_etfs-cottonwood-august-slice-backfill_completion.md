# ETFS cottonwood August daily-slice BACKFILL -- opened and closed in-session

**Actor:** `4.0.0_SA_CRO` · **Date:** 2026-09-01 ~16:4x-16:5xZ · **Class:** data repair (additive), not a deploy
**Authorization:** Andrew-direct, verbatim: *"We shouldnt have coverage gaps, you have egress to go and fill
those out"* -> then, narrowing the source: *"you should be able to handle this from opal-data-assets"* ->
then, scoping the acceptance: *"there should not be any missing dates when we present"*.

## What was wrong

`opal-data-etfs/daily/cottonwood/` was missing 5 of August's 21 NYSE trading days:
**2026-08-04, 08-18, 08-20, 08-21, 08-31.**

**NO EGRESS WAS REQUIRED and none was performed.** The upstream partitions already existed in
`opal-data-assets/blackdiamond/cottonwood/silver/fact_holdings/date={D}/data.parquet` for all five dates.
The gap was a producer that did not fire, not absent data.

## The premise that had to be checked FIRST, and was

`cot-etf-ownership-daily/lambda_function.py:137-141` carries a deliberate ZERO-vs-MISSING contract: a day
whose holdings are present but **entirely unpriced** writes **NO slice** and is excluded from the average --
distinct from a held-zero. **A backfill over such a day would have FABRICATED data**, and the absence would
have been correct by design.

MEASURED before invoking anything, reading each upstream parquet directly:

| date | rows | priced positions | ETF total |
|---|---|---|---|
| 2026-08-04 | 16,953 | 10,958 | 51,233,635 |
| 2026-08-18 | 18,051 | 11,553 | 52,311,873 |
| 2026-08-20 | 18,088 | 11,472 | 52,853,165 |
| 2026-08-21 | 18,102 | 11,835 | 52,999,503 |
| 2026-08-31 | 18,633 | 11,929 | 53,546,052 |
| *control 08-19 (slice existed)* | 18,051 | 11,457 | 52,974,277 |

All five PRICED. The skip contract does not explain them -> backfill is valid.
**Control 08-19 recomputed to DIVZ 18,814,714 against the existing slice's 18,814,714.24 -- so the method
reproduces the producer exactly.**

## The act

`aws lambda invoke --function-name cot-etf-ownership-daily --payload '{"date":"YYYY-MM-DD"}'` x5 -- the
producer's OWN documented backfill path (`lambda_function.py:45`, `_partition_key_for` LOUD-fails on an
absent date). No new code, no hand-written JSON, no schema divergence. All five returned
`StatusCode=200 / status=ok`.

**Predicted-before-observed:** the five totals were computed independently BEFORE invocation and match the
producer's written values to the cent (51,233,634.54 / 52,311,873.43 / 52,853,164.81 / 52,999,503.08 /
53,546,051.78).

## Verification -- read from S3, NOT from the lambda return value

`49financial 43/43 · cottonwood 43/43 · inflection 43/43` trading days across July+August. COMPLETE.

## Scope boundary -- what was deliberately NOT done

⛔ **The served monthly reports under `opal-data-etfs/platinum/reports/` were NOT re-rendered.** A re-render
overwrites served output AND re-sends the month-end SES email. Both months were instead rebuilt LOCALLY via
`render_month_end.py --out ... --pdf` with **`--s3-out` omitted**, into Andrew's Desktop pack only. Zero S3
writes under `platinum/`, zero email.

**CONSEQUENCE, STATED SO IT IS NOT DISCOVERED LATER: the served reports are now BEHIND the Desktop pack.**
`platinum/reports/2026-07/` and `2026-08/` still carry the gap-bearing renders. Refreshing them is a
separate act requiring the served-output sign-off and accepting the email re-send. **Surfaced to Andrew, not
self-authorized.**

## Residual, NOT chased (surprise channel)

Why the cottonwood producer missed five runs is **UNDIAGNOSED**. The backfill repairs the data; it does not
explain the misfire, and nothing here prevents a sixth. Owner for the root cause: the cot-pipeline lane.

## Numbers moved (previously published -> complete data)

| month | partner | was | now | delta |
|---|---|---|---|---|
| 2026-07 | cottonwood | 31,186,887.06 | 31,242,755.15 | +55,868.09 |
| 2026-07 | inflection | 46,695,709.41 | 47,137,193.79 | +441,484.38 |
| 2026-08 | cottonwood | 52,488,748.61 | 52,492,649.45 | +3,900.84 |
| 2026-07 | **49financial** | 527,715,910.53 | 527,715,910.53 | **0.00 (control)** |
| 2026-08 | **49financial** | 547,008,390.28 | 547,008,390.28 | **0.00 (control)** |
| 2026-08 | **inflection** | 52,383,045.42 | 52,383,045.42 | **0.00 (control)** |

The three zero rows are the check that the rebuild moved only what it should.
July's revision (+497,352) was reached twice by independent routes and agreed.

**STATUS: CLOSED.** Opened and closed in-session per NEVER#2.
