# Never-widen PRODUCER half, 4.0.0_SA_CRO~DDD -- Cottonwood carrier-value retry (the durable morning fix)

**Author:** 4.0.0_SA_CRO~DDD, 2026-10-19 ~15:1xZ. **For:** 1.0.0_SA_CTO~DELL1 (CTO half + apply gate).
**Authority:** Andrew-direct `ANDREW_DIRECT_20261019_144xZ_COT_CARRIER_RETRY_FIX_NOW.md` @5dcfce1cd7 ("We need that fix now").
**Deadline:** the 2026-10-20 07:30 ET bronze pull (as-of 10-19) is the first new-day exposure.

## The problem, measured

BD posts the insurance carrier-feed values after the 07:30 ET pull, so that pull lands ~96 supervised accounts at $0
(8.86M on 10/15; FWD-10 findings ADDENDUM 2). The signal is accounts whose holdings rows are ALL null Market Value. Over
11 deliveries, 10-09 .. 10-16:
- carrier-null deliveries: **136-160**;
- valued deliveries: **36-56**.

## The act

1. **Ingest** (`data/cot/scripts/bronze/cot_bronze_ingest.py` @86e3cac7d9 + @67df6e6db1).
   - Rule (d): on the MAIN daily Cottonwood pull, a holdings delivery with more than 100 all-null accounts is re-pulled
     every 420 s, up to 6 times. The delivery with the FEWEST all-null accounts lands; the last re-pull ends ~08:15 ET.
   - Never on the retry sweep (`--backfill-holdings-net`, a separate process, flag False) or a `--backfill` window.
   - Never on 49F (`BD_S3_BUCKET == "opal-data-cot"` gate).
   - Offline check on stored versions: 144 and 160 -> WAIT; 48, 56, 56, 48 -> land.
   - Deploy: `safe-deploy` to `s3://opal-data-cot/code/bronze/`. The prior object VersionId is `n0hfQiQfsIAAGVEqCKcTGXSjMyIbEhWA`
     (sha 5486514d.. = @de2e85035d). The second target opal-data-bd must NOT be written; if safe-deploy writes it, it is
     restored by copy-object the same turn, as CTO 7262.
2. **Mirror schedule** (`infra/aws/terraform/opal-assets/mirror.tf`, `aws_scheduler_schedule.mirror_cot_et`).
   - Cron changes `cron(45 7 * * ? *)` -> `cron(25,45 7-8 * * ? *)` America/New_York, i.e. 07:25, 07:45, 08:25, 08:45 ET.
   - Targeted plan: **0 to add, 1 to change, 0 to destroy**.
   - The 08:25 run carries a wait-delayed holdings land into the monolith before the MDPF 13:30Z floor (12:25Z EDT /
     13:25Z EST). 07:45 still serves the 08:15 ET IRPT readers (irpt-cot-account-return / -holdings-performance,
     measured reading the monolith Cottonwood silver).
   - The handler is idempotent (skip-if-landed) and reserved_concurrency=1, so the extra runs copy nothing new on a
     normal day.
   - Why not a second schedule: the naming gate (LGIC_ENFORCE DEC-6) refuses a hand-kept name for a new resource.
   - Why not moving 07:45: it would starve the 08:15 IRPT readers.

## Writers of what moves -- N = 2

1. **Cottonwood bronze holdings** (`forwardfill_v2/holdings/HOLDINGS_DAILY_<asof>.xlsx`).
   - Written by `cot_bronze_ingest` on the 07:30 ET `opal-cot-bronze-run`. Its land moves from ~07:31 to ≤ ~08:15 ET on a
     carrier-null morning.
   - Downstream follows the existing sentinel chain: silver, then the ADVI gold.
2. **The monolith mirror** (`opal-assets-ingest-mirror`, firm cot): two more runs a day.

## Branches

- **(a) Carriers post within the wait.** Holdings lands valued (~36-56 all-null). ADVI and MDPF serve the supervised
  total including carriers on the new day.
- **(b) Carriers do not post by ~08:15 ET.** The best delivery lands with a "WAIT EXHAUSTED" line, the same as today's
  behaviour, ~45 min later. The no-regress guard (c) admits any later fuller re-land.
- **(c) A wait re-pull fails** (BD error). The best delivery so far is kept, and the run continues.
- **(d) Timeout risk.** The SSM step timeout is 7200 s. The wait adds ≤ 6 × (420 s + pull time), about 50 min, inside the
  budget alongside the doc's own sentinel retry.

## Rollback

- **Ingest:** copy-object VersionId `n0hfQiQf..` onto `code/bronze/cot_bronze_ingest.py`.
- **Mirror:** cron back to `cron(45 7 * * ? *)`, then plan and safe-apply the same target.
- No data rollback is needed; nothing is rewritten by this act.

## Verification

At the 2026-10-20 07:30 ET pull, the bronze-run log shows either a WAIT line and a valued land, or "carrier check: <=100".
The 08:25 mirror copies the land, and the 13:30Z fire writes Cottonwood 10-19 with carriers. Read and reported to the CTO
and Andrew.

## Producer half: SIGNED by 4.0.0_SA_CRO~DDD. Awaiting the CTO half and apply gate.
