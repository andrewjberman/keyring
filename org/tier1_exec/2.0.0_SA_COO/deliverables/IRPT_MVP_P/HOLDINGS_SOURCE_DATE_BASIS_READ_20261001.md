# Which close a holdings partition dated D holds, per source -- the read CTO rulings batch 63 items 2-3 ordered (row IRPT_BCKEND-S245)

Author `2.0.0_SA_COO~P`, 2026-10-01. First form 07:2xZ-07:4xZ (@bc19cd3e16: the seam); this form ~10:4xZ adds the whole-history
and every-day reads, which changed the answer for Inflection after its seam. Read-only throughout: S3 reads of `opal-data-assets`
silver, no vendor call, no write. Instruments, all in this folder:

| instrument | what it can see | what it cannot |
|---|---|---|
| `partition_close_consecutive.py` | every consecutive pair in a short range | which close a weekday partition holds (two weekdays differ on either basis) |
| `partition_close_history_sweep.py` | every weekend and holiday pair of a whole history (701 pairs) | Tuesday to Friday partitions |
| `partition_close_anchor.py` | the days it is given, against the Schwab own-date close | days it is not given |
| `partition_close_anchor_sweep.py` | EVERY trading-day partition in a range, against the Schwab anchor | any day before the anchor's first partition (2024-07-09) |

The first three were not enough: thirteen sampled anchor days and the seam read all agreed, and the week of 2026-07-13 was on a
different basis. A basis is called MEASURED below only where every trading-day partition in the span was graded.

## Answer

| source (declaration key) | a partition dated D holds | claim | evidence |
|---|---|---|---|
| `schwab_08335338` (49 Financial) | D's OWN close | inferred (33 of 559 partitions read) | the price's own last-update date equals the partition date on 99.89 to 99.93 percent of rows on each of 26 partitions 2025-03-11..2026-09-16, and on at least 99.908 percent on each of the 113 anchor partitions the every-day sweep read (2026-04-16..2026-09-25); business-day partitions only |
| `blackdiamond_z09` (Cottonwood) | D's OWN close, with a lagged minority | inferred (10 of 81 partitions read) | of the securities whose anchor close moved: 326 of 351 to 540 of 543 own-date on each of 10 days 2026-06-10..2026-09-25; 0 to 22 per day at the prior close; 2 to 25 neither. The lagged minority is not explained |
| `orion` (Inflection) | see the segments below | measured 2024-07-11..2026-09-25 (555 trading-day partitions graded); inferred before 2024-07-11 and after 2026-09-25 | below |

## Inflection, every trading-day partition 2024-07-11..2026-09-25 (`partition_close_anchor_sweep.py`)

Before the seam: all 444 trading-day partitions from 2024-07-11 through 2026-04-17 read OWN_DATE, each at 99 percent or more of
its discriminating securities; no absent partition, no partly carried one. (The anchor's own freshness -- rows whose price
last-update date equals the partition date -- is at least 93.88 percent on every one of the 446 anchor partitions read.) The
table below is the 111 days from 2026-04-20.

A partition reads one basis when at least 95 percent of its discriminating securities (those whose Schwab close moved that day,
137 to 168 per day) carry that close. Census: OWN_DATE 14, PRIOR_TRADING_DAY 92, NO_SINGLE_CLOSE 3, ABSENT 2.

| partition dates | reads | detail |
|---|---|---|
| 2026-04-20 .. 2026-05-04 (11 days) | OWN_DATE | 152 of 152 at 2026-05-04 |
| 2026-05-05 .. 2026-05-11 (5) | PRIOR_TRADING_DAY | the SEAM is the partition dated 2026-05-05: 149 of 149 at the prior close; it repeats 2026-05-04 on 9,350 of 9,350 priced keys |
| 2026-05-12 | NO_SINGLE_CLOSE | 36 of 148 at the prior close, 110 at the close two trading days back: a partly carried pull |
| 2026-05-13 .. 2026-06-30 (33) | PRIOR_TRADING_DAY | 140 of 145 on the weakest day |
| 2026-07-01 | ABSENT | no partition (2026-07-03, 07-04, 07-05 are absent too and are not trading days) |
| 2026-07-02 .. 2026-07-10 (6) | PRIOR_TRADING_DAY | all securities, every day |
| 2026-07-13 .. 2026-07-15 (3) | OWN_DATE | 156 of 156, 156 of 156, 156 of 159: three pulls made after their own day's close |
| 2026-07-16 | NO_SINGLE_CLOSE | 39 of 156 at the prior close, 117 two back |
| 2026-07-17 .. 2026-08-05 (14) | PRIOR_TRADING_DAY | all securities, every day |
| 2026-08-06 | ABSENT | no partition |
| 2026-08-07 .. 2026-08-10 (2) | PRIOR_TRADING_DAY | all securities |
| 2026-08-11 | NO_SINGLE_CLOSE | 123 of 137 at the prior close (89.8 percent, under the line), 12 two back, 2 own-date |
| 2026-08-12 .. 2026-09-25 (32) | PRIOR_TRADING_DAY | 127 of 128 on the weakest day |

Weekend and holiday pairs over the WHOLE history (`partition_close_history_sweep.py`; 2,343 partitions from 2020-04-24, 701
discriminating pairs): OWN_DATE 650, PRIOR_TRADING_DAY 39, NO-PRICES 10 (through 2020-05-26 fewer than three keys carry a price),
ABSENT 2. Runs: own-date on 648 of 648 pairs from 2020-06-06 through 2026-05-04; prior-day on every pair from 2026-05-09 except
Monday 2026-07-13 (own-date, the week above). One pair in 2020-06-01 reads prior-day on a single priced key and means nothing.

## What the declaration costs: closes that are in no partition

Under the segments above, for the 111 graded days:

| close of | why it is in no partition | trading days not computable |
|---|---|---|
| 2026-05-11 | the partition that would hold it (05-12) holds no single close | 05-11, 05-12 |
| 2026-06-30 | the partition that would hold it (07-01) is absent | 06-30, 07-01 |
| 2026-08-05 | the partition that would hold it (08-06) is absent | 08-05, 08-06 |
| 2026-08-10 | the partition that would hold it (08-11) holds no single close | 08-10, 08-11 |

Eight trading days of 111. Friday 2026-07-10's close is read from the weekend partitions and the 07-13 week's closes from their own
partitions, so that week loses nothing. Dry run of the changed producer on 2026-05-01..2026-05-13 (real silver, no write): seven
days computed, 2026-05-11 and 2026-05-12 ABSENT by name.

**A method question this raises, not answered here.** A day the producer cannot compute has no gold partition, and the adapter
chains the days that exist: a period that spans such a day silently leaves that day's return out (the adapter reads the partitions
inside the window and links the OK rows; it does not check that every trading day is present). For 49 Financial that was the
2026-09-29 gap, closed by a catch-up. For Inflection it would be eight days in five months. The alternatives are a ruling: leave the
days absent and make the adapter refuse or mark a window that spans one; or let the producer link across the gap (a multi-day
return dated on the first computable day, `prior_business_date` naming the close it started from). Nothing here builds either.

## Rule-24 record for the declaration's new field (`sources.json` 1.2, `partition_close[].holds` and `.basis`)

- **(i) MECE over a declared domain.** Domain: a partition dated D of a declared source, as read by the holdings producer.
  `OWN_DATE` (D holds D's close) | `PRIOR_TRADING_DAY` (D holds the close of the trading day strictly before D) | `NO_SINGLE_CLOSE`
  (anything else: the partition's rows are priced at more than one day's close). The third member is the complement of the first
  two, so the set is exhaustive by construction. Hunted by subtraction against the printed denominator: of 111 graded trading-day
  partitions, 14 + 92 + 3 are covered and 2 are ABSENT, which is not a member because an absent partition is read at run time, not
  declared. A partition holding the close of two days back for ALL its rows would be a fourth basis; none of 111 reads that way (the
  "two back" counts sit inside NO_SINGLE_CLOSE partitions), and the producer refuses an unknown value rather than guessing.
- **(ii) Same grain.** Every member is a property of one partition date. A segment is a run of partition dates with one value.
- **(iii) Intent coherence.** One question: which close. Whether the partition EXISTS is not on this axis (run time), nor is how the
  value was established (`basis`, its own field: `measured` = every trading-day partition of the segment was graded; `inferred` = a
  sample was, or none could be).
- **(iv) State coherence.** Re-pulling a NO_SINGLE_CLOSE partition from the vendor as-of its date would move it to a single-close
  member; it would not move an ABSENT partition (nothing to re-read) and it needs Andrew's vendor word. Measuring more partitions
  moves `basis` from inferred to measured and never moves `holds` by itself.
- **Token census** (comp-find, word-boundary, case-insensitive, corpus=all, 212,415 to 212,422 files scanned, 94,072 ephemeral-floor
  files not searched, 7,677 binary, 7 to 8 unreadable): `partition_close` 0 hits; `OWN_DATE` 2 hits in 1 file, the comp-tool's own
  query log; `PRIOR_TRADING_DAY` 96 hits in 50 files, none an enum member: they are the function `prior_trading_day` in
  `data/inf/scripts/silver/_orion_vendor_asof.py` (the estate's own statement of Orion's forward label) and its callers and
  records. Same meaning, different object (a function, not a declared value). `NO_SINGLE_CLOSE` 0 hits (212,530 files scanned, read before the
  commit that lands it).

## The estate already knew the mechanism, not the seam

`data/_contracts/vendor_asof_registry.yaml` (owner `0.4.0_DS_ClientPlatform`) declares the Orion positions feed
`label_offset: -1 trading day`, and `_orion_vendor_asof.py` normalizes labels by it. Neither carries an effective-from date. The
monolith silver this producer reads is own-date through 2026-05-04, so applying "-1 trading day" to its whole history would be as
wrong before the seam as the old pairing was after it. Not changed here: that registry is another seat's file.

## Not measured

- Inflection before 2024-07-11 by the every-day instrument: no anchor exists before 2024-07-09, so that span rests on the 648
  weekend and holiday pairs alone and its Tuesday-to-Friday partitions are ungraded.
- Schwab and Black Diamond beyond the partitions counted above.
- Why 2026-05-12, 2026-07-16 and 2026-08-11 were partly carried, why 07-13..07-15 were pulled after the close, and why 07-01 and
  08-06 are absent (the pull's own logs were not read).
- Whether the 95 percent line is the right one for 2026-08-11 (89.8 percent): under a 85 percent line it would read prior-day and
  the 12 lagged securities would have one day's return dated a day late instead of two days being absent.
