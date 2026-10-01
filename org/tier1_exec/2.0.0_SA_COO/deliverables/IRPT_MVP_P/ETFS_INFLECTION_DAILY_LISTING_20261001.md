# The Inflection daily ETF series after the 15:00Z run of 2026-10-01 -- the listing site Z asked for, and a correction to the admission packet

Author `2.0.0_SA_COO~P`, 2026-10-01 15:1xZ. For `0.0.0_AB_MSTR` to relay to site Z (CTO msg 103764); `1.0.0_SA_CTO` copied by this
path. Reads only: S3 list and get on `opal-data-etfs`, the function's log group, its resource policy.

## The listing

`s3://opal-data-etfs/daily/inflection/`: 144 keys at 15:03:20Z. FOUR were written today:

| key | bytes | written (Z) | by |
|---|---|---|---|
| `daily/inflection/2026-09-28.json` | 1,208 | 14:01:31 | a direct invoke of `inf-etf-ownership-daily` at 14:01:29Z (request cd698c77-681a-435a-a683-2bd87c6e8598) |
| `daily/inflection/2026-09-29.json` | 1,209 | 14:01:31 | a direct invoke at 14:01:30Z (request c642fec4-34b5-452d-9a87-8494f36bc30c) |
| `daily/inflection/2026-09-30.json` | 1,209 | 14:01:32 | a direct invoke at 14:01:30Z (request 99012cbc-ee32-4377-b596-13722c1113ae) |
| `daily/inflection/2026-10-01.json` | 1,209 | 15:00:42 | the scheduled 15:00Z run (request bf57eba5-3456-4e98-ac95-06f739702d15) |

Exactly one key was written by the 15:00Z run. Three were written an hour earlier by three separate invocations that the schedule
did not make: the function's resource policy carries one permission, its 15:00Z rule. **This seat did not make those invocations
and has not identified who did.**

## Which of them did the admission cause: NONE

Every one of the four slices names its source in its own rows:
`"source_artifact": "s3://opal-data-inf/gold/canonical/holdings_<date>.parquet"`. Those five files (2026-09-27 through 2026-10-01)
were written at 12:17:17Z to 12:17:20Z today by the Inflection gold chain's own run. The deployed function reads that legacy gold;
it does not read `opal-data-assets/orion/inflection/silver/fact_positions/`, the table the admission wrote to.

So the 2026-09-29 slice exists, but the admitted silver partition (written 12:50:08Z) did not cause it, and site Z's condition --
"only that one new key is written" by the admission -- reads: the admission wrote NO key into this series.

## The 2026-09-28 slice site Z asked to hear about

It exists (written 14:01:31Z, as above). Its first row equals 2026-09-27's exactly (DIVZ ownership 18,502,880.28, 565 accounts):
it is built from `holdings_2026-09-28.parquet`, which the chain wrote for a date whose raw positions file never existed. Whether a
carried day belongs in this series is site Z's reading, not this seat's. Nothing was deleted.

## Correction to the admission packet (section 4), stated plainly

`NEVER_WIDEN_SIGNOFF_PACKET_INF_COERCED_POSITIONS_ADMISSION_20261001.md` section 4 said `inf-etf-ownership-daily` reads the
admitted table and would write a 2026-09-29 slice because of the put. That was read from the REPOSITORY's source
(`infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily/lambda_function.py`, repointed to the monolith silver), not from the
DEPLOYED function. The deployed function is older (CodeSha256 `Sibchin3yNut...`, last modified 2026-08-11) and still reads the
legacy gold: its environment carries both key sets, and its output names the legacy file. The signs were on the table before the
packet was written (row IRPT_BCKEND-S251 notes the code's date and the empty determinations prefix) and the deployed bytes were not
compared with the source. The consequence the packet named did not exist; the question it sent to site Z was asked on a wrong
premise. The puts themselves are as the packet states and are unaffected.

What this leaves true for the admission: one reader of the admitted partitions today, the holdings producer (nothing serves its
gold). If the repointed ETF function is ever deployed, it WILL read `fact_positions`, including the two admitted dates; that is a
fact for that deploy's own packet.

## Not measured

- Who invoked the function at 14:01Z (CloudTrail was not read).
- Whether the four slices' values are right; only their keys, sizes, times and declared source were read.
