# Performance Reporting holes -- Cottonwood (3 cohorts), 49 Financial, Inflection -- 2026-10-19

Author: 4.0.0_SA_CRO~PRFRPT (dell2). Order: `ANDREW_DIRECT_20261019_163xZ_PERFORMANCE_REPORTING_HOLES_ALL_FIRMS_COHORTS.md`.
Read-only research; nothing written in AWS, S3 or portal. Today Mon 2026-10-19; T-1 frontier Fri 2026-10-16
(`lib/trading_calendar.py`). Claim tags: (M) measured live today, (I) inferred. Working reads (session scratchpad, not
durable): `scratchpad/{anna,cot,inf49,sched}/`.

## 1. Status by firm

| Firm / cohort | Served perf on IRPT dashboard | Fresh to T-1? | Daily schedule | Main defect |
|---|---|---|---|---|
| 49 Financial | 6,966 accounts (712 of a 7,675 roster have no series; ~$77K total, NO-PRIOR-HOLDINGS) (M) | YES: 6,962 at 10-16; 4 stuck (M) | YES, end to end, NY-time Scheduler, 10/10 trading days (M) | ~200 accts/day NOT_MEASURABLE; 10-13 fee-day 1,875 LARGE_FLOW spike, no surprise row (M) |
| Cottonwood A: new, BD-only | 469 of 511 (40 never positive MV; 2 publishable now) (M) | NO: as of 10-15; 89 stop at 09-23 (M) | NO: gold + publish schedules DISABLED (M) | flows counted N times (below) |
| Cottonwood B: Commonwealth-only | 0 of 1,062 (228 active at 2026-06) (M) | n/a | n/a (one-time backfill) | nothing served |
| Cottonwood C: Commonwealth + BD | 470 of 471, but every series starts 2026-07-10 (M) | NO: as of 10-15 (M) | as A | backfill not stitched; 06-22 to 07-10 gap |
| Inflection | 0: no `account_return_daily`, empty `platinum/reporting/` (M) | n/a | holdings-perf only, 14:00 UTC (M) | no total-return product at all |

## 2. The Anna Thiessen case (Cottonwood cohort C) -- root causes, all (M)

Accounts 9237 (BD `z0926705231`) and 9238 (BD `z0926819471`).
1. **+/-1000% jump = flows multiplied, not a transfer.** On 2026-07-17 source flows were 9237 +9,184,890.46 and
   9238 -5,149,485.79; gold holds exactly 13x each (+119,403,575.98 / -66,943,510.27). The Cottonwood gold builder
   (`irpt-cot-account-return-daily-lambda`) re-reads every rolling daily BD transaction file and never de-duplicates by
   TransactionID. Fix exists -- commit `fa48b9d8b7` (2026-10-17, TO-DB-b-333) -- but is NOT deployed: Lambda
   LastModified 2026-10-16T19:29Z. Gold for 10-16 built this morning still triples 9237's flow. Smaller flows are
   inflated the same way. Cohort-wide: 97 accounts > +100% cumulative, 51 below -100%; 495 of 528 days with a daily
   move > 25% fall on flow days.
2. **"Not measured" + 5 breaks:** 07-10 (first row) plus 07-23, 07-28, 07-30, 08-04 -- gold days built from partial
   source files that lack these accounts. Any window spanning a break reads Not measured; 881 of 939 since-inception
   windows are Not measured.
3. **"3 days not reported by the source" is stale:** full files for 08-19, 09-24, 09-25 (and 07-22/27/29, 08-03)
   landed 2026-10-17 14:16Z; gold was never rebuilt.
4. **History starts 2026-07-10:** `FLOOR_DAY = "2026-07-10"` at
   `infra/aws/lambda/investor-reporting/reporting-publish-cot/handler.py:33`. Gold holds her Commonwealth history
   (2013 to 2026-06-22) under Commonwealth account numbers, and the publish step does not join them to the BD z-ids.
   CORRECTED same day: her Commonwealth numbers end 7492/7491 and are named by BD's own `NFS Account Number` field.
   The `0QF879237/0QF879238` guess was wrong. See `PRFRPT_FIDELITY_VS_BD_STITCH_BASE_20261019.md` section 2.
5. **Data through 10-15:** `irpt-cot-reporting-publish-daily` and `irpt-cot-reporting-gold-daily` are DISABLED
   (NY 09:30 / 09:15 Mon-Fri); last publish was manual 2026-10-16T23:25Z. Lag grows one trading day per day.

**Corroboration (2026-10-19 18:17Z, msg 10878/10879):** the CTO (`org/tier1_exec/1.0.0_SA_CTO/deliverables/FINDINGS_FOR_CRO_PRFRPT_COTTONWOOD_READER_20261019.md`)
and COO~F2 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/R139_COTTONWOOD_PARTITION_OVERLAP_FINDING.md`)
reached the same cause independently (row IRPT_DASHBD-D2-S137). The fix (window D..D+14, trade_date = D, dedup on
TransactionID; release 36da4e101f) is being deployed now by IB2 on Andrew's word, and ~D2 rewrites the full history after it.

**Answers to the CTO's section 5:**
- *Other consumers reading every partition:* `data/cot/scripts/gold/runners_cot/runner_common.py:140` dedups on
  TransactionID (safe). `data/assets/scripts/gold/build_cottonwood_interpolated_backfill.py:241` dedups whole rows over
  the selected columns; it is safe only while those columns never differ across partitions (COO~F2 measured that they
  do not). `account_transaction_cottonwood.py:238` refuses any row whose business date differs from the day it is
  written under, so a multi-day partition fails loudly rather than producing duplicates. Only the returns reader was
  affected.
- *Is 14 days enough:* not always. Whole source days (08-19, 09-24, 09-25; also 07-22/27/29 and 08-03) were
  re-landed in full on 2026-10-17 14:16Z, 22 to 87 calendar days late, so a D..D+14 window never sees them. A one-time full
  rewrite repairs those days now. A late day after that needs a trigger that rebuilds any day whose source partition
  is rewritten, or a periodic full-history rewrite.

## 3. Trigger schedules -- consistency verdict: NOT consistent (M)

- **49F:** Schwab pull 05:45 ET -> holdings-perf 07:30 -> account-return gold 07:41 -> publish 08:15 (NY-time Scheduler). Healthy.
- **Cottonwood:** BD session 07:30 ET -> account-return gold 08:15 (schedule created 10-15; 2 of last 10 days ran on
  schedule, 8 backfilled by hand) -> report gold 09:15 DISABLED -> publish 09:30 DISABLED. No other trigger on the
  last two hops.
- **Inflection:** Orion pulls 07:02-10:43 (UTC crons); holdings-perf 14:00 UTC; no reporting gold or publish hop
  exists. `inf-gold-trigger` (books) is S3-event-only with no scheduled fallback.
- **Clock basis split:** 49F and Cottonwood reporting use America/New_York; Inflection holdings-perf and both books
  schedules use UTC. When daylight saving ends on 2026-11-01, the UTC ones run one hour earlier in ET (I).
- **Shared mirror** `opal-assets-ingest-mirror` fails 6x/day since 10-18 on one stray Inflection file
  (`orion/inflection/bronze/scope_account_returns/date=2026-10-16/scope.json.gz`); 10-17 also failed on
  `UNKNOWN FIRM SELECTOR 'cottonwood'`.

## 4. Advisor Intelligence Books performance (all firms)

ADVI_PERFRP closed 2026-10-13. Only 3 `perfrp` files are served, published by hand 2026-09-01. The publisher is held
under Andrew's 2026-08-25 hold (not re-read today). No Cottonwood books perf view exists in `portal/src/pages/AdvisorIntelligence` (M).

## 5. Holes ranked by client impact, with the fix and owner

| # | Hole | Fix | Owner |
|---|---|---|---|
| 1 | Cottonwood returns corrupt (flows counted N times), every cohort A/C account | deploy the reader fix (release 36da4e101f; deploying now via IB2); rebuild all gold history (~D2), since the 14-day window does not reach July; republish; add an implausible-return guard | IRPT_DASHBD (CloudOps lane deploys) |
| 2 | Cottonwood served data frozen at 10-15; schedules disabled | after #1, enable `irpt-cot-reporting-gold-daily` + `-publish-daily` | IRPT_DASHBD (enabling the schedules publishes client-facing data, so Andrew's word may be needed) |
| 3 | Cottonwood B (1,062 accts) gets nothing; C loses pre-July history | crosswalk Commonwealth id -> BD id, then lower `FLOOR_DAY` with a labelled stitch | ADVI_COTBKF (crosswalk) + IRPT_DASHBD (publish); scope decision is Andrew's |
| 4 | 107 candidate pairs / up to 219 A accounts may really be C | Andrew sends the one ask to Cottonwood (`ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/COTTONWOOD_MATCH_PACKET_COVER_20261016.md`) | Andrew |
| 5 | Inflection: no served performance | build reporting gold + publish on the 49F shape | IRPT_DASHBD workstream B-IN (round 133, TO-DB-i-22 pending) |
| 6 | Cottonwood stale source gaps (08-19, 09-24/25, 89 accts stop 09-23) | covered by the #1 rebuild; re-measure afterwards | IRPT_DASHBD |
| 7 | Books performance cards empty for every firm | successor project or lift the 08-25 hold | Andrew / CTO |
| 8 | Ingest mirror failing on stray Inflection file | quarantine the file or allowlist the prefix | CloudOps |
| 9 | Schedule clock basis split (UTC vs NY) before the 11-01 DST change | align to America/New_York | CloudOps |
| 10 | 49F: 10-13 fee day read as client flow (1,875 LARGE_FLOW); ~200 NOT_MEASURABLE/day | surprise row + fee-flow classification | IRPT_DASHBD workstream B |
