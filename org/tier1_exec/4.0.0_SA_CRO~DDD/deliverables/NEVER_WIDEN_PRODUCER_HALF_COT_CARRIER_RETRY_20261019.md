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

---

## AMENDMENT 1 (~16:5xZ) -- the WAIT is replaced by a CARRY-FORWARD (Andrew-direct ADDENDUM 1)

**The act:** `safe-deploy` of `cot_bronze_ingest.py` @e7d897445f to `s3://opal-data-cot/code/bronze/`.
- **Prior object (rollback):** VersionId `76XG3l.p2w7ESDsOVU_9lhni3IAloUHg` (the wait, @67df6e6db1, sha eac2d977).
- **opal-data-bd:** sha before is printed and restored the same turn if written (as before).
- **Mirror cron:** unchanged. The 07:25/08:25/08:45 runs are now redundant but idempotent; no second apply today.

**The rule:**
- On the daily pull and the retry sweep (never `--backfill`), an account whose holdings rows are ALL null Market Value
  lands with the previous landed HOLDINGS_DAILY file's rows.
- An account null on both days lands as delivered.
- The carry is recorded in the completeness sidecar (`carry`: from_date, from_version, accounts, market_value).
- The sweep reads a carried day as UNKNOWN-OR-ABSENT and re-pulls it inside its 5-bday lookback until BD's own values
  land. The carry also runs on the sweep, so the no-regress guard compares carry-for-carry.
- Cottonwood bucket only.

**Writers of what moves -- N = 1:** `cot_bronze_ingest` (bronze holdings, opal-data-cot). The land time returns to
~07:31 ET; the values of carried accounts move from null to the prior day's.

**Branches:**
- **(a) Carriers null at 07:30.** About 112 accounts carry D-1 rows. Next morning's sweep re-pull lands BD's values;
  if still null, it carries again (bounded by the 5-bday lookback).
- **(b) Carriers already valued.** No carry, the sidecar has no `carry` field, and behaviour is as before.
- **(c) Prior file unreadable, header changed, or any parse error.** Lands as pulled (fail-open). This is today's
  pre-wait behaviour.
- **(d) A closed account delivered all-null.** It carries one more value for up to 5 bdays, until the re-pull lands
  BD's own null. Exposure: a real closure is overstated for up to 5 bdays.

**Measured replay** (stored 2026-10-16 07:30 delivery, 160 all-null accounts, read-only):
- 112 carried from 10-15; total 561,160,180.77.
- BD's final 10-16 file: 561,115,503.42 (gap 44,677.35, 0.008%).
- As pulled: 549,927,742.23.
- The `Timestamps` sheet is byte-equal.

**Tests:** 7 new (`tests/test_carrier_carry.py`) pass. 7 pre-existing failures fail identically at HEAD.

**MDPF note:** MDPF writes a dated key once (silver converter skips an existing partition; A8 conditional put). A
carried value that MDPF consumed stays in MDPF's history for that date until Andrew answers question 2.

**Producer half (Amendment 1): SIGNED by 4.0.0_SA_CRO~DDD.**
