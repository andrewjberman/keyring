# Never-widen sign-off packet -- two coerced Inflection positions files admitted to silver by ONE named path (2026-08-06, 2026-09-29)

Author `2.0.0_SA_COO~P`, 2026-10-01 ~12:1xZ. Ordered by `1.0.0_SA_CTO` rulings batch 63 item 5 and batch 81 items 1-5 ("the
admission is its own packet with both never-widen halves ... names the one path by which a coerced file is admitted and that
nothing else takes it"). Halves owed: `1.0.0_SA_CTO` and `2.0.0_SA_COO~P` (signed below). Rows IRPT_BCKEND-S216, S245.

## 1. The act, exactly

TWO S3 puts of TWO new keys in `opal-data-assets`, by `IRPT_MVP_P/admit_coerced_positions.py --admit <date> --write`:

| key (absent today) | from | rows x columns |
|---|---|---|
| `orion/inflection/silver/fact_positions/date=2026-08-06/data.parquet` | `s3://opal-data-inf/bronze/positions/2026-08-06.parquet` (1,231,196 bytes, written 2026-08-06 13:40Z) | 35,262 x 64 |
| `orion/inflection/silver/fact_positions/date=2026-09-29/data.parquet` | `s3://opal-data-inf/bronze/positions/2026-09-29.parquet` (1,282,552 bytes, written 2026-09-29 11:25Z) | 36,109 x 64 |

Nothing is overwritten and nothing is deleted. No Lambda, schedule or converter code changes: the converter and the mirror still
refuse a bronze parquet. No vendor call.

## 2. The one path, and that nothing else takes it

`admit_coerced_positions.py` (committed with this packet): its `ADMITTED` table holds exactly these two dates, each with its
ruling; `--admit` refuses any other date (run: 2026-07-01 is refused by name), refuses a date whose silver partition exists, and
refuses a date whose raw file exists. It reads the coerced file with pyarrow, re-serialises the rows as the JSON lines the raw file
would have carried, and passes them through the CONVERTER'S OWN code imported from the repo: `mirror_conversion._orion_tables`
(declared 59-column schema, drift gate, exact dedup, provenance) and `stream_parquet.stream_to_parquet` (atomic, read-back
verified). The partition's `_source_file` is the coerced file's own name, `<date>.parquet`: that is its provenance, and it is how
the one earlier admission in this monolith reads (`fact_assets/date=2026-08-06`, written 2026-08-14, `_source_file`
`2026-08-06.parquet`).

## 3. Measured (reads only)

**Each date's own controls** (`coerced_positions_equality.py`; coerced vs raw, rows matched on `id`, all 59 declared columns):

| date | controls | result |
|---|---|---|
| 2026-09-29 | 2026-09-26, 2026-09-27, 2026-09-30 | equal on 59 of 59 columns: 36,103, 36,103 and 36,110 rows; id sets identical | 
| 2026-08-06 | 2026-08-04, 2026-08-05, 2026-08-07 | equal on 59 of 59 columns: 35,219, 35,262 and 35,262 rows; id sets identical |
| 2026-07-01 (NOT admitted) | 2026-06-29, 2026-06-30, 2026-07-02 | 2 of 3: 2026-07-02 differs on 4 columns in 9 of 33,618 rows (`isRebalance` and `modelName` 7 rows, `productType` and `productSubType` 2). Batch 81 item 3: it stays a gap and is linked across |

Denominator: 2,344 dates carry both forms; 7 carry only the coerced one (2026-07-01, 07-03, 07-04, 07-05, 08-06, 09-28, 09-29).

**The path is exact** (`admit_coerced_positions.py --control`): for five dates whose raw file exists, the table this path builds
from the COERCED file was compared with the silver partition the converter built from the RAW file -- all 64 columns, every row,
matched on `id`. 2026-08-04, 08-05, 08-07, 09-26, 09-27: schema equal, row counts equal, 0 columns differ except `_source_file`
(5 of 5). 2026-09-30 is not a control here: its silver partition is not mirrored yet.

**Which close each file holds** (Schwab own-date anchor, securities whose close moved): 2026-08-06.parquet 150 of 150 at the
2026-08-05 close; 2026-09-29.parquet 149 of 149 at the 2026-09-28 close. Both PRIOR_TRADING_DAY, as their declared segments say.

## 4. Blast radius: TWO readers of this table

| reader | 2026-08-06 | 2026-09-29 |
|---|---|---|
| the holdings producer (`sources.json` `orion`; nothing serves its gold yet) | the close of 2026-08-05 exists again: 08-05 and 08-06 compute as ordinary days (today 08-05 is absent and 08-06 is one linked row of span 2) | the close of 2026-09-28 exists: with today's mirror fire landing 09-30, the days 09-28 and 09-29 compute as ordinary days |
| `inf-etf-ownership-daily` (cron 15:00Z; reads every existing partition; catches up dates within 10 days that have no output) | none: `opal-data-etfs/daily/inflection/2026-08-06.json` exists (written 2026-08-08) and the date is outside the window | **at its next run it writes `opal-data-etfs/daily/inflection/2026-09-29.json`**: one more September daily slice for Inflection, holding the 2026-09-28 settled book. Today the series ends at 2026-09-27 |

The second reader is another project's served series (ETFS). The slice it would write is a true day of holdings by section 3's
measurement, and without it September's Inflection series has no slice for 09-28 or 09-29. It is still a move of that series, so it
is named here for the half that signs. If the ETFS side should not move today, the alternative is: admit 2026-08-06 now and
2026-09-29 on or after 2026-10-10, when it is outside the catch-up window (the holdings producer links 09-29 across the gap until
then). This seat's recommendation is to admit both now.

Also a consequence, not a write of this act: the converter's daily sweep compares the bronze it sees with the silver that landed
and already reads `FAIL` every day on one alien key (the earlier `fact_assets/date=2026-08-06`; row W99-S4). It will name two more.
The verdict stops nothing. Teaching the sweep an admitted class is a converter change with its own packet.

Writers of each new key: 1 (this path). The converter cannot write them (no raw file exists for either date).

## 5. Rollback, per key

Removing a key this act created is an S3 delete and needs Andrew's word. Without a delete: for the holdings producer, declaring
the partition date `NO_SINGLE_CLOSE` in `sources.json` makes it unread (data, one commit), and the affected gold days are re-run.
For the ETF slice: once `daily/inflection/2026-09-29.json` is written, removing it is the ETFS owner's act and also a delete.
That asymmetry is why section 4 offers the later date for 09-29.

## 6. Conditions

1. `--admit` dry run first for each date (done: 35,262 x 64 and 36,109 x 64 rows, 0 duplicates removed, nothing written).
2. Each write is read back by the writer; then listed: the key, its size, and `_source_file` read from the landed partition.
3. The landed partition for each date is graded against the anchor again (section 3's third read, on the landed bytes).
4. The holdings gold days the two dates change are re-run under the rebuild's ledger
   (`irpt-holdings-gold-inflection-rebuild-20261001`): 2026-08-05 and 08-06, and 2026-09-28 and 09-29 once 09-30 is mirrored.
5. The first `inf-etf-ownership-daily` run after the 09-29 write is read from its log and its output listed; what it wrote is
   reported the same hour.

## COO half -- 2.0.0_SA_COO~P

SIGNED, 2026-10-01 ~12:1xZ, on this packet's bytes at the commit that carries it. Write set: two literal keys, both absent today.

## CTO half

(owed: `1.0.0_SA_CTO`, bound to this packet's pre-signature blob)
