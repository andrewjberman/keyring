# MDPF_SECHIST gold deploy L3 -- issuer's read of the first scheduled run (2026-10-10 13:00Z)

Reader: 2.0.0_SA_COO~H1. Read at 2026-10-11T02:2xZ. Read only; no write to any served key.

Instrument: `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R5_CHECKS/r5_gold_l3_read.py 2026-10-10 <prior snapshot>`
(committed @24d92cfbfd, dry-run BAD before the run as designed). Prior snapshot: `L3_GOLD/positioning_data_asof_2026-10-08_PRE_DEPLOY_RUN.json`
(as_of 2026-10-08, 190 holdings).

## Output (verbatim)

```
1 served: LastModified=2026-10-10T13:01:40+00:00 data_as_of=2026-10-09
2 gap record: s3://opal-data-etfs/bloomberg/etfs/silver/history_gaps/as_of=2026-10-09/gap_record.json keys=as_of,basis,listed,partitions_read,required_days,securities,securities_tracked,securities_with_listed_days
3 log: lines=36 bad=0 gap_record_lines=2
   [etf_positioning_gold] gap record: built over 36 partition(s), 3 of 188 security(ies) list days
   [etf_positioning_gold] WROTE gap record s3://opal-data-etfs/bloomberg/etfs/silver/history_gaps/as_of=2026-10-09/gap_record.json
4 diff vs prior: keys now=188 prior=190 common=188 weight>1=0 industry_group changed=0
   ('DIVZ', 'SALXX') prior 1D/WTD=(0.0097, 0.0291) now 1D/WTD=(0.0097, 0.0388)
   ('IDVZ', 'SALXX') prior 1D/WTD=(0.0097, 0.0291) now 1D/WTD=(0.0097, 0.0388)
   ('PFDE', 'FXFXX') prior 1D/WTD=(0.0104, None) now 1D/WTD=(0.0417, None)
   ('PFOE', 'FXFXX') prior 1D/WTD=(0.0104, None) now 1D/WTD=(0.0417, None)
GOLD-L3-OK as_of=2026-10-09 record=s3://opal-data-etfs/bloomberg/etfs/silver/history_gaps/as_of=2026-10-09/gap_record.json log_lines=36 common=188
```

## Grade by the ledger leg's three proofs

| proof required | measured | verdict |
|---|---|---|
| gap record at `record_address(as_of)` | object exists at the printed address; the log line `WROTE gap record` carries the same address, so the R1 `PutObject` grant was EXERCISED | PASS |
| no `WRITE FAILED`, no `ImportError` | 36 log lines in 12:55Z-13:40Z, 0 matching `ImportError` / `WRITE FAILED` / `Traceback` | PASS |
| served page diffed against the prior day | `weight>1` 0; `industry_group` changed 0; keys common 188 of 188 now / 190 prior | PASS |

## Things the diff shows that the grade does not decide

- **Holdings 190 -> 188 (measured, not inferred).** The two keys absent from the served page are `('IDVZ','KCDMY')` and `('IDVZ','UNVGY')`
  (weight 0.0002 each); nothing is new in the served page (`only in now` is empty). Cause is UPSTREAM of the gold: both tickers are present
  in `s3://opal-data-etfs/bbg/2026-10-08/characteristics.csv` (175 lines) and ABSENT from `.../bbg/2026-10-09/characteristics.csv` (173 lines,
  grep over the whole file), so the bronze universe for as_of 2026-10-09 never carried them. The deploy did not drop them. The script's limb 4
  grades common keys only; the two-key drop is recorded here as the one difference from "the same holdings keys".
- **SALXX / FXFXX 1D and WTD moved** (SALXX WTD 0.0291 -> 0.0388; FXFXX 1D 0.0104 -> 0.0417). These are the SH-t-7 money-market fields, and
  the as_of date changed between the two snapshots, so a change is expected; the DIVZ/IDVZ SALXX 1D matches (0.0097). Printed both days as
  CTO half condition 2 requires; it is not graded as a defect.

## Other read the same turn (SH-t-8 V1, L2 limb -- owned by 0.7.0_AE_CloudOps~ZQ)

`s3://opal-data-etfs/bbg/2026-10-09/run_manifest.json`, LastModified 2026-10-10T11:06:48Z, 4994 B:
`run_class` = "scheduled"; `history_gap_fill` PRESENT (record_as_of null, listed_tickers 0, rows 0, error null); `history_backfill_exhausted`
PRESENT = {"PFDE": "2026-10-09", "PFOE": "2026-10-09"}. The ~ZQ order's manifest limb is met. `history_gap_fill.record_as_of` null /
`listed_tickers` 0 is the expected first-run state: the gold wrote its first gap record at 13:00Z, after this 11:00Z pull. NOT read here: the
site-Z ETF-leg exit code and the exhausted-count log line (the log carrier is on site Z; ~ZQ's act).
