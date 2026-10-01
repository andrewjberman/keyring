# Deploy Completion Record
**Date opened:** 2026-10-01T11:38:54.534966+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261001T151406Z
**Deploy:** Inflection holdings gold rebuilt over its whole history on the declared close basis with gap links (CTO batch 63 item 3c, batch 80 items 2-3); producer and sources.json at de3d423dce (merge 1361c00b4f); emission 1.2; nothing serves this gold
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 12.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R1 | activation | s3://opal-data-inflection/irpt/inflection/gold/holdings_performance_{daily,manifest}/ date=2020-04-27..2026-09-25 | the producer run from the private worktree at de3d423dce with --source orion --upload over every trading day of the range: days landed and days not computed printed per run with their reasons; every landed partition overwrites the 2026-09-29 build (bucket versioned, prior versions kept); no delete | the producer at de3d423dce run from the private worktree with --source orion --upload over 2020-04-27..2026-09-30. First write 11:40:25Z (2026-09-24); last 15:05:47Z. Drivers, stated: the first (13 half-year chunks) was stopped by the harness at its two-hour limit and then failed six attempts at 2021-01-04..2021-06-30 on S3 body-read timeouts; a second driver for the same chunk overlapped it for about five minutes (same pin, same bytes) and was stopped; a monthly driver finished 2021-05-17..2021-06-30 and 2020, 11 of 11 months on the first attempt. Days re-run after the admissions: 2026-08-04..08-07 and 2026-09-25..09-30. Not computed, by name: 2026-05-11 and 2026-08-10 (no partition holds the close under the declared basis) and 2026-06-30 (date=2026-07-01 absent). Every landed partition overwrote the 2026-09-29 build in a versioned bucket; nothing was deleted. | CLOSED 20261001T151405Z |
| V1 | verify | the rebuilt table read back | listing: partitions written today vs the trading days of the range; a sample partition reads 20 columns at schema 1.2; the linked rows (span_trading_days 2) on 2026-05-12, 2026-07-01, 2026-08-06, 2026-08-11 present; every partition still carrying the 2026-09-29 build is NAMED (the gap days) with its disposition, none deleted | listing read 15:13:09Z: 1,616 daily partitions = the 1,616 trading days 2020-04-27..2026-09-30; 1,613 written today, 0 on a non-trading day. Samples read back at 20 columns, schema 1.2: 2020-04-27 (888 rows, all NON-POSITIVE-BASE, span 1), 2023-06-15 (880 rows, 537 OK), 2026-09-30 (966 rows, 792 OK). Linked rows of span 2: 2026-05-12 (from 2026-05-08), 2026-07-01 (from 2026-06-29), 2026-08-11 (from 2026-08-07). 2026-08-06 is an ordinary row (span 1, from 2026-08-05) since its silver partition was admitted at 12:33Z. Hand reproduction of one account, 6 of 6 rows equal to 1e-12, accepted by the CTO (msg 103769). STILL THE 2026-09-29 BUILD, named: date=2026-05-11, date=2026-06-30, date=2026-08-10 -- nine objects with their version ids in the delete packet; disposition ruled by CTO batch 92: they end as NO partition, the delete is Andrew's act, and the serving packet does not land while they exist (with them the candidate adapter's year to date for one account reads 0.36 percent, without them 2.40). None deleted. | CLOSED 20261001T151406Z |

## Log

- 20261001T113854Z OPENED by 2.0.0_SA_COO~P with 2 leg(s)
- 20261001T151405Z LEG R1 closed: the producer at de3d423dce run from the private worktree with --source orion --upload over 2020-04-27..2026-09-30. First
- 20261001T151406Z LEG V1 closed: listing read 15:13:09Z: 1,616 daily partitions = the 1,616 trading days 2020-04-27..2026-09-30; 1,613 written today, 0 o
- 20261001T151406Z CLOSED -- all 2 legs proven
