# Which close a holdings partition dated D holds, per source -- the read CTO rulings batch 63 item 3(a) ordered (row IRPT_BCKEND-S245)

Author `2.0.0_SA_COO~P`, 2026-10-01 07:2xZ-07:4xZ. Read-only: S3 reads of `opal-data-assets` silver, no vendor call, no write.
Instruments, both in this folder: `partition_close_consecutive.py` (does a partition repeat the one before it) and
`partition_close_anchor.py` (a partition's prices against the Schwab own-date closes).

## Answer

| source (declaration key) | a partition dated D holds | effective | evidence |
|---|---|---|---|
| `schwab_08335338` (49 Financial) | D's OWN close | all history read | the price's own last-update date equals the partition date on 106,748 of 106,835 rows at 2026-09-25 (and on 86,418 to 106,748 rows of each of the seven anchor days read); partitions exist for business days only, landing D+1 about 09:46Z |
| `blackdiamond_z09` (Cottonwood) | D's OWN close | 2026-09-24 and 2026-09-25 read | against the Schwab anchor, of the securities whose close moved that day: 540 of 543 and 524 of 547 equal the own-date close; 1 and 19 equal the prior day's; 2 and 4 equal neither |
| `orion` (Inflection) | D's OWN close through 2026-05-04; the PRIOR TRADING DAY's close from 2026-05-05 | the seam day is **2026-05-05** | below |

## Inflection: the seam is 2026-05-05, by two instruments that share no method

**Instrument 1, consecutive partitions** (keys `accountId, productId`, positive `currentPrice` in both; "unchanged" = the same price):

| pair | unchanged | reading |
|---|---|---|
| Thu 04-30 -> Fri 05-01 | 2,488 of 9,364 (26.6%) | Friday holds a new close |
| Fri 05-01 -> Sat 05-02 | 9,373 of 9,373 (100%) | Saturday repeats Friday: own-date basis |
| Sat 05-02 -> Sun 05-03 | 9,373 of 9,373 (100%) | |
| Sun 05-03 -> Mon 05-04 | 860 of 9,311 (9.2%) | Monday holds Monday's close: still own-date |
| **Mon 05-04 -> Tue 05-05** | **9,350 of 9,350 (100%)** | **Tuesday REPEATS Monday: the first partition holding the prior day's close** |
| Tue 05-05 -> Wed 05-06 | 999 of 9,345 (10.7%) | Wednesday holds Tuesday's close |
| Fri 05-08 -> Sat 05-09 | 1,243 of 9,386 (13.2%) | Saturday is the first to hold Friday's close |
| Sat 05-09 -> Sun 05-10, Sun 05-10 -> Mon 05-11 | 100%, 100% | Monday repeats: prior-day basis |

The same shape holds in 2026-09: Fri 09-18 -> Sat 09-19 8.1%, Sat -> Sun 100%, Sun -> Mon 09-21 100%; Fri 09-25 -> Sat 09-26 7.0%.

**Instrument 2, the Schwab anchor** (securities joined by ticker whose Schwab close moved that day):

| Inflection partition | discriminating securities | equal to the own-date close | equal to the prior-day close |
|---|---|---|---|
| 2026-05-04 | 152 | 152 | 0 |
| 2026-05-05 | 149 | 0 | 149 |
| 2026-05-06 | 148 | 0 | 148 |
| 2026-09-24 | 136 | 0 | 136 |
| 2026-09-25 | 148 | 0 | 148 |

So Monday 2026-05-04's close sits in TWO partitions (05-04 on the old basis, 05-05 on the new one) and no trading day's close is
missing at the seam.

## What follows for the producer (batch 63 item 2), stated as data and not yet built

For trading day t the producer needs the partition holding t's close and the one holding the prior trading day's close. One rule
gives both, per source: **the close of trading day x is in the partition dated x when x is before the source's effective-from
date, and in the partition dated `next_trading_day(x)` from it on.** An own-date source has no effective-from date and always reads
partition x (today's rule, correct for Schwab and Black Diamond).

For Inflection, effective-from is the PARTITION date 2026-05-05:

| trading day t | t's close is in partition | the prior day's close is in partition |
|---|---|---|
| t <= 2026-05-04 | t | prev(t) |
| t = 2026-05-05 | 2026-05-06 | 2026-05-04 (own basis; 2026-05-05 holds the same prices, 9,350 of 9,350) |
| t >= 2026-05-06 | next(t) | t |

A consequence for freshness: on the new basis the newest computable day is the trading day BEFORE the newest partition, and a day's
row can be computed only once the next trading day's partition has landed.

## Not measured

- Black Diamond before 2026-09-24 (two days read; its history starts 2026-06-09). The 19 prior-day matches on 2026-09-25 are not
  explained (3.5 percent of the discriminating set).
- Mon 2026-05-11 -> Tue 2026-05-12 reads 5,656 of 9,387 unchanged (60.3%), where about 10% is the usual weekday figure; not explained.
- Why the basis changed on 2026-05-05 (the daily pull's start is the likely cause; the pull was not read here).
- Weekend pairs for Schwab and Black Diamond do not exist (business-day partitions only), which is why the anchor was used.
