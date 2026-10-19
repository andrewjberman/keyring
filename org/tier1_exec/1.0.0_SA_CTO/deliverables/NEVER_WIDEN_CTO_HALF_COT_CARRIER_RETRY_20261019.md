# NEVER-WIDEN -- CTO HALF + APPLY GATE: Cottonwood carrier-value retry (`1.0.0_SA_CTO~DELL1`, 2026-10-19 ~15:1xZ)

**Binds the producer half** `org/tier1_exec/4.0.0_SA_CRO~DDD/deliverables/NEVER_WIDEN_PRODUCER_HALF_COT_CARRIER_RETRY_20261019.md`
@e02d5ee3a9, sha256 `9ab3c414053c94e2be15b2e1e766da0001fd69311d311b0ff1c0201308a75664` (re-hashed by me). Any edit to it voids this
half.

**Authority:** Andrew-direct `ANDREW_DIRECT_20261019_144xZ_COT_CARRIER_RETRY_FIX_NOW.md` @5dcfce1cd7 ("We need that fix now").
`4.0.0_SA_CRO~DDD` builds it on that word.

## What I read at signing (the producer's own rule, `cot_bronze_ingest.py` @67df6e6db1)

- **The wait** is `_wait_for_carrier_values` (cap 100, spacing 420 s, 6 attempts).
  - It keeps the delivery with the fewest all-null accounts.
  - A failed re-pull keeps the best delivery so far.
  - `_holdings_all_null_accounts` fails OPEN to 0 on any parse ambiguity, so an unreadable delivery never waits.
- **Gate (line 915):** `table == "holdings" and _CARRIER_WAIT_ACTIVE and BD_S3_BUCKET == "opal-data-cot"`. 49F, whose bucket is
  opal-data-bd, never waits.
- **The retry sweep cannot wait.** The `--backfill-snapshot-net` / `--backfill-holdings-net` branch returns at line ~1369, before
  `_CARRIER_WAIT_ACTIVE = not args.backfill` (line 1390), and a `--backfill` run sets it False.
- **Writers, N = 2**, as the half prints them: the bronze holdings land, via `cot_bronze_ingest` on the 07:30 ET run, and the monolith
  mirror (`opal-assets-ingest-mirror`, firm cot), which gets 2 more runs a day and is idempotent.

## Blast radius

- **One code object:** `s3://opal-data-cot/code/bronze/cot_bronze_ingest.py`.
- **One schedule field:** `aws_scheduler_schedule.mirror_cot_et` cron, changed from `cron(45 7 * * ? *)` to
  `cron(25,45 7-8 * * ? *)` America/New_York, with plan 0/1/0.
- The Cottonwood holdings land time moves from ~07:31 to at most ~08:15 ET on a carrier-null morning.
- Nothing is rewritten. opal-data-bd is not touched.

## Both branches, and the rollback

The half covers all four cases, and I accept them as written:
- (a) the carriers post within the wait;
- (b) the wait is exhausted, so the best delivery lands, which is today's behaviour about 45 minutes later;
- (c) a re-pull fails, and the best delivery is kept;
- (d) the timeout budget holds.

The rollback is:
- copy-object VersionId `n0hfQiQf...` back onto the code key;
- the cron back to `cron(45 7 * * ? *)`, by plan and `safe-apply`.

## Conditions of this signature (APPLY GATE)

1. **The deployed object's bytes are read back** after `safe-deploy`, and their sha256 must equal the file at 67df6e6db1.
2. **opal-data-bd's code object** has its sha256 printed before and after. If safe-deploy wrote it, it is restored by copy-object the
   same turn, and the after-sha must equal the before-sha.
3. **The mirror plan is targeted and reads exactly 0/1/0**, the cron only. Any other diff in the plan is a STOP.
4. **A NEVER-2 ledger entry** is opened at the start, and its close is COMMITTED at the end with both read-backs in it.
5. **The 2026-10-20 07:30 ET read is reported to me and Andrew.** It covers the WAIT or carrier-check line, the 08:25 mirror copy, and
   Cottonwood 10-19 at the 13:30Z fire with carriers.

## VERDICT: SIGNED (CTO). The apply gate is OPEN under conditions 1 to 5.

-- 1.0.0_SA_CTO~DELL1
