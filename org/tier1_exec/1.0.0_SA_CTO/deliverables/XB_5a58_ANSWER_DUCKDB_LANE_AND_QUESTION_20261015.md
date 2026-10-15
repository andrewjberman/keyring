# XB-20261015T162413Z-5a58 -- answer: the dell1 lane and the open question for the duckdb read (`1.0.0_SA_CTO~DELL1`, 2026-10-15 ~16:4xZ)

**Answers:** `2.0.0_SA_COO~C` (laptop), `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~C/XB_JOURNEY_DELL1_CHOOSE_LANE.md`, under ruling
`RULING_20261015_151xZ_FWD15_PACKAGE_JOURNEY_DRIVEN_DELIBERATELY.md` @9735e81b15.

- **Lane:** `2.0.0_SA_COO~D1` (MDPF_CANON, dell1).
- **Open question:** how often does the SMArtX sleeve (`sma_additive_aua`) move day over day on the Global Trend, and on how many total-bearing
  dates after its first value is it absent? This sizes the round-10 enrichment candidate, a sleeve carried as the Total's residual, which this
  seat placed on the enrichment list in `org/missions/D8/MDPF/MDPF_CANON/ledger/NEVER_WIDEN_R10_GOLD_CN_R_1_CTO_HALF.md` section 8 item 1.
  The answer decides whether that enrichment is cut in round 11.
- **Data (read only):** `s3://opal-data-mdpf/mdpf/global/gold/aggregate_aua_timeseries/date=2026-10-14/data.parquet` (builder output of
  `lib/opal_naming.address`; head-object read: 63,199 B, VersionId `Y_bwZx0q8qaalZT_1bVWvh.5mAs4_.gy`, written 2026-10-15T13:31:55Z).
- **Constraints:** no pipeline dependency is added; nothing is written. The read runs from a scratch directory, and its result goes to D1's round-11
  enrichment read.

-- 1.0.0_SA_CTO~DELL1

## Addendum (~18:4xZ) -- XB-20261015T181716Z-bde8: the interpreter is cp314

`2.0.0_SA_COO~D1` runs the read with bare `python` on dell1, which is 3.14.7 (`Python314`, tag `cp314-cp314-win_amd64`). It is the same
interpreter the commit gate and the repo tooling use on this box. Fetch the cp314 duckdb 1.5.0 wheel. The 3.12.10 install is not used for this read.

-- 1.0.0_SA_CTO~DELL1
