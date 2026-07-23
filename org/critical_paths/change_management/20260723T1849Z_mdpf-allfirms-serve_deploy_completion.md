# MDPF all-firms serve -- deploy completion ledger
OPENED: 2026-07-23T18:49Z by 0.4.0_DS_ClientPlatform
AUTHORITY: CTO serve-fire 184804Z on COO clean counter-sign 184724Z + DE render evidence @5ae6762da
(never-widen co-sign satisfied: CTO+COO). Andrew tonight-completion order standing.
PATTERN: per key, staged-md5 assert (gate-cited prefixes matched) -> put -> fresh-GET
byte-compare -> ListObjectsV2 key+size -> served ETag cited.

SERVED (opal-data-portal-v2), all 6/6 byte-identical:
1. json/mdpf/49financial/aggregate-aua-timeseries.json  171,643B ETag d68f2f4bb3337738817c55a5a9ad8fed
2. json/mdpf/inflection/aggregate-aua-timeseries.json   136,236B ETag 904df9f29cd469725ed593e00704aaf9
3. json/mdpf/aggregate-aua-timeseries.json              242,414B ETag 8b6de1d5b506f6504426078c30e53edc
   (GLOBAL: measured frontier 2026-07-22 = $1,951,676,164.42, cottonwood=measured)
4. json/portfolios/aum-metrics.json                       7,234B ETag 4580938e4aab3e978807eeb8d487dc94
5. json/mdpf/global/account-distribution.json             7,220B ETag 0a2978d46352932d3f53c52161cedfb4
6. json/mdpf/cottonwood/aggregate-aua-timeseries.json    66,999B ETag 55f3c6fed26852de218748263a671a28
   (band w/ measured 07-21/22 tail; supersedes the 1203Z serve per V6 measured-beats-interpolated)

CLOSED: 2026-07-23T18:52Z -- publish complete, report to CTO+COO+DE+DT sent same turn.
Downstream: DE live-render check -> DT DEV cfb0afb7 -> PROD promote -> COO confirms live to Andrew.
