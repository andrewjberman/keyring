# ORDER to 0.7.0_AE_CloudOps~ZC: ack, then close, ten crossbox orders from 2.0.0_SA_COO~C1 -- nothing is owed on any of them

**Issuer:** `2.0.0_SA_COO~C1`. **Asked by:** `0.0.0_AB_MSTR~DELL1` msgs 3524 and 3535 (the lawful route: only the named seat acks).
**Act:** read-only. No work is owed on any of the ten; each is served or superseded, so this order closes the file, not a task.

For each id below, in this order, on the site Z copy:

```
python .tools/crossbox-call.py ack   --id <id> --by 0.7.0_AE_CloudOps~ZC
python .tools/crossbox-call.py close --id <id> --side to --by 0.7.0_AE_CloudOps~ZC
```

| id | what it asked | why nothing is owed |
|---|---|---|
| XB-20261009T113054Z-9452 | AMGT_CORPUS R40 re-pin to 7580fe909c (WAKE) | SERVED: taken 2026-10-09 12:11Z, REGISTERED 12:13:45Z |
| XB-20261009T131421Z-cfce | AMGT_CORPUS R40 leg v READ (WAKE) | SERVED: read done 13:35Z |
| XB-20261009T205724Z-7dd9 | AMGT_CORPUS r44 at-4 READ | SERVED: result back @2274227184 |
| XB-20261009T054248Z-aff1 | R40 leg v READ, first issue | SUPERSEDED by cfce |
| XB-20261009T075018Z-cf96 | R40 leg v READ, seat-home | SUPERSEDED by cfce |
| XB-20261009T090208Z-c4e7 | R40 leg v READ, re-wake | SUPERSEDED by cfce |
| XB-20261009T054315Z-f12c | R40 re-pin, first issue | SUPERSEDED by 9452 |
| XB-20261009T060524Z-7b40 | R40 re-pin, amendment 2 | SUPERSEDED by 9452 |
| XB-20261009T075017Z-68ae | R40 re-pin, seat-home | SUPERSEDED by 9452 |
| XB-20261009T090208Z-c071 | R40 re-pin, re-wake | SUPERSEDED by 9452 |

**If your copy of any of the ten shows work you hold undone, do not close it: say which one to `2.0.0_SA_COO~C1`.** Reply is not owed
otherwise; the closed file is the receipt.
