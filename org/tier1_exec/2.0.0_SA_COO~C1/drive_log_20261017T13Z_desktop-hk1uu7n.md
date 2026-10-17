# Drive log -- 2.0.0_SA_COO~C1, ADVI_COTBKF, 2026-10-17 12Z to 14Z (written ~13:58Z, desktop-hk1uu7n)

One row per substantive tick: project | limb | round | TOs t/T | cells c/F | thread | act fired. Counts and ids only; no account, name or dollar value.

| tick | project | limb | round | TOs | cells | thread | act fired |
|---|---|---|---|---|---|---|---|
| ~12:34Z | ADVI_COTBKF | L9 read | 106 | 1/1 | 1/1 | n | session start on dell1; CRO~DDD msg 7501 (10/16 carriers re-pulled behind the guard 12:11Z, ADVI gold chain 12:14Z) read; `dc1_fire_read.py fire`: silver_partitions=47 newest=2026-10-16, dim_rebuilt=True (99OZcIE1), attr_filled 1004 of 1005, added_filled 62/62, changed_agree 72/72; `snapshot` taken; sent to CRO~DDD |
| ~13:52Z | ADVI_COTBKF | L9 read | 106 | 1/1 | 1/1 | n | CRO~DDD msg 7549 (13:30Z fire served Cottonwood 10/16, no further cot gold build until the 7-day half is signed); `dc1_apply_check.py doc` and `state` read: default_version=5, added is account_attributes, nongating, after holdings; partitions=47, existing partition unchanged; `fire` unchanged; `compare` prints changed_portfolio_group=0 dropped_between_builds=0 |
| ~14:25Z | ADVI_COTBKF | L9 read | 106 | 1/1 | 1/1 | n | CRO~DDD msgs 7571, 7580: 14 stray bronze account_attributes keys (07-15..07-31 weekdays, 08-12) verified in the bucket, one version each, landed 14:06-14:09Z; silver still 47 partitions, dimension 99OZcIE1 unchanged; CTO msg 7588 RULED never merge, quarantine by CRO~DDD before ~11:30Z 10-18 (record `MDPF_CANON/ledger/CTO_RULING_QUARANTINE_14_STRAY_ACCOUNT_ATTRIBUTES_20261017.md` @d398734b87), no S3 delete |

**Measured limit on C-1.** The baseline snapshot (QyyWrPzI) holds 1 multi-book account; the latest (99OZcIE1) holds 122; the two share 1. So `compare` graded 1 of the 122. C-1 (determinism of `portfolio_group` between two consecutive builds on the full 122) is NOT yet measured: it needs a second build on the 47-partition set. The round is not closed on this read.

**Owed.** After the 10-18 silver run: proof read (silver/account_attributes still 47 partitions, none dated in the 14, merge log names them quarantined); C-1 snapshot held until that read is clean (CTO 7588). Then a `snapshot` after the next gold build that follows the 12:17Z one, then `compare`; the round-106 close (`.tools/round-close-check.py --round 106`) after that. Andrew: the CRM console upload; the ADVI_COTBOOKS DONE WHEN lines. Push state: this seat's commits since @8816c4fe6c are LOCAL; origin not re-measured.
