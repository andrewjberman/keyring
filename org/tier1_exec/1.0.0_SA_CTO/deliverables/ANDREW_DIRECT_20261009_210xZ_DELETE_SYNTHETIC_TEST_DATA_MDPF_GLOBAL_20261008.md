# Andrew-direct 2026-10-09 ~21:0xZ -- delete the synthetic test data (MDPF global gold, 2026-10-08); done

**Where:** 1.0.0_SA_CTO terminal (laptop). **Verbatim:** "You have rights to make any deletions you need on this matter of synthetic data"

**The matter:** dell1 open call `dell1-20261009T202914Z-113f` (MDPF_CANON row D1-S4): a worker's test wrote synthetic parquet files into
the served MDPF global gold partition `date=2026-10-08` at 19:10:38-39Z, before any apply.

## Read before the act
Bucket `opal-data-mdpf`, versioning **Enabled** (so a delete is a delete marker; each prior version stays restorable). Each key carried ONE
version, written 19:10Z, contents synthetic:

| key | size | version deleted behind the marker | contents |
|---|---|---|---|
| `mdpf/global/gold/account_distribution/date=2026-10-08/data.parquet` | 1,131 B | `wUUzw7Ts11t_TLBYYO1WiqHjKAz9JoR9` | 4 rows: period, account_units.count = 3 |
| `mdpf/global/gold/account_units/date=2026-10-08/data.parquet` | 1,037 B | `ktnEsNny.MG4.L3JxdzuTJ6HYmQY.7wO` | count = 3 |
| `mdpf/global/gold/aggregate_aua_timeseries/date=2026-10-08/data.parquet` | 763 B | `RlRi3ng36p1aoNQiw8lMQOtpfU5fb.qU` | model_aua = 1.0 |
| `mdpf/global/gold/aum_metrics/date=2026-10-08/data.parquet` | 1,037 B | `RjIE78ZDSN2tMYQRmTdARHjEesXPijnX` | total.aum = 2.0 |

(The row said "1037-byte" for all four; measured sizes differ, all four are test values.)

## Act (~21:0xZ, 1.0.0_SA_CTO, `.tools/aws s3api delete-object`, one literal key each)
Delete markers: `UrHGw2vCzsedyec352N55Jo9Eb5fcciA`, `v466TUf_tUtMM3eg.1fgvOEp_1GJom8U`, `bZ4iT5cI5YFCMqEh.zMtYgf0xb1BXq1Z`, `S1K3vnV97amf.LV26FuINAd_bp6Gp6fK`.
Read back: `head-object` on all four -> 404 Not Found. Write set = the literal four-key list (CLAUDE.md NEVER-1 non-application).
**Rollback per key:** delete the marker version to restore the prior (synthetic) object -- not wanted, stated for completeness.

## Next (dell1)
MDPF_CANON's round-1 backfill (`run_class=backfill`) fills `date=2026-10-08` with the composite's real figures; dell1 closes `-113f`.
