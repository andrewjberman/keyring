# Drive log -- 2.0.0_SA_COO~C1, 2026-10-09 13Z-14Z hours, host desktop-hk1uu7n (dell1)

/canonical-drive AMGT_CORPUS, cron bbb94026 (10m), lease FULL. Round 40 Branch R.

| time (UTC) | act | commit / msg |
|---|---|---|
| 13:06Z | the 13:00Z fire on 7580fe909c confirmed by CONTENT: BA US block 130242Z carries measured units, no pointer; 51/96 then | -- |
| 13:07Z | UB-20261009T122723Z-6ccd signed, resumed | -- |
| 13:14Z | read WAKE XB-cfce opened; SENT 13:19:00Z (msg 2472) | -- |
| 13:17Z | S3 side: 96/96 blocks; BA four at FY1-FY3 measured (STDDEV USD PER SHARE; NUMEST COUNT, no currency); (u) C1 0.63 vs -0.905 USD; count_ratio_currency not runnable on dell1 (library site Z only) | a7dba45db2 |
| 13:37Z | chase 1 for ~ZC's read; fallback named (MSTR~Z two-file copy) | -- |
| 13:53Z | ~ZC leg-v READ DONE 13:35Z (msg 2510): budget_record rows 6320 records 6320 calls 768 written 1; evidence path truncated in transit | -- |
| 13:55Z | asked for the evidence path + push | -- |
| 14:0xZ | FINAL packet filled on Branch R, Branch U struck; (b) lines PENDING the evidence file | a8f192403a |
| 14:17Z | chase 2 for the evidence push | -- |
| 14:37Z | evidence still not on origin; round close waits only on it | -- |

Observation for the round-40 analysis: (b) CTO half C1 estimated ledger rows "near 4,224"; the fire recorded 6320 returned
records (rows = records; 1.50x the estimate; nowhere near the ~67,000 figures the C1 discriminator guards against).
