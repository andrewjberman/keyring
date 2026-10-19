# NEVER-WIDEN -- CTO HALF for AMENDMENT 1: the Cottonwood carrier WAIT is replaced by a CARRY-FORWARD (`1.0.0_SA_CTO~DELL1`, 2026-10-19 ~17:5xZ)

**Binds** the producer half `org/tier1_exec/4.0.0_SA_CRO~DDD/deliverables/NEVER_WIDEN_PRODUCER_HALF_COT_CARRIER_RETRY_20261019.md` as it
stands at 47e2585e9c, with Amendment 1, sha256 `5f3dfd4df020ff56bbef223552106c0f9c70593cf117b20b4cee6db44565137d` (re-hashed by me).
This supersedes my half @2a3569ab5b for the ingest object only. The mirror cron is unchanged.

**Authority:** Andrew-direct ADDENDUM 1 in `ANDREW_DIRECT_20261019_144xZ_COT_CARRIER_RETRY_FIX_NOW.md`: *"1.) Yes, the t+2 aspect for
insurance does not need to be separately labeled."* The carried value carries no page label on his word. Its claim is recorded in the
completeness sidecar (`carry`), where a consumer can read it.

## What I read at signing (`cot_bronze_ingest.py` @e7d897445f)

- **Gates (lines 953 and 1142):** `table == "holdings" and _CARRIER_CARRY_ACTIVE and BD_S3_BUCKET == "opal-data-cot"`. 49F is never
  touched.
- **`_CARRIER_CARRY_ACTIVE = not args.backfill` (line 1403):** the carry is on for the daily pull and the sweep, and off for an explicit
  `--backfill`.
- **`_carry_forward_carrier_values` fails OPEN** and lands the delivery as pulled when:
  - there is no prior file;
  - the header differs;
  - no account was valued on the prior day;
  - there is any parse error.
- **The sweep reads a carried day as not complete** (`_landed_with_carry`) and re-pulls it inside its 5-bday lookback.
- **Writers, N = 1:** `cot_bronze_ingest`, Cottonwood bronze holdings.

## Blast radius

- **One code object:** `s3://opal-data-cot/code/bronze/cot_bronze_ingest.py`.
- **Served move:** on a carrier-null morning, about 112 accounts carry D-1 rows. In the 10-16 replay, the carried total ran $44,677.35
  (0.008%) from BD's final figure, against $11.2M short as pulled. The land time returns to about 07:31 ET.
- **Named exposure, accepted on Andrew's word:** a genuinely closed account delivered all-null is overstated for up to 5 bdays.
  MDPF's write-once dated keys keep a carried value for that date. Whether MDPF restates is Andrew's open question 2 in his record,
  and this half does not settle it.
- opal-data-bd is not touched.

## Both branches, and the rollback

All four branches are covered, and I accept them as written:
- (a) the carriers are null, so accounts carry and the next sweep re-pulls;
- (b) the carriers are valued, so nothing carries;
- (c) a fail-open case, which lands as pulled;
- (d) a closed account, as named above.

**Rollback:** copy-object VersionId `76XG3l.p2w7ESDsOVU_9lhni3IAloUHg` (the wait, sha eac2d977) onto the code key. No data rollback; a
carried day is re-pulled by the sweep.

## Conditions

1. **The deployed object's sha256 is read back** and must equal the e7d897445f file.
2. **opal-data-bd's object sha is printed** before and after, and restored the same turn if it was written.
3. **A NEVER-2 entry** is opened at the start, and its close is COMMITTED with both read-backs.
4. **The 2026-10-20 07:30 ET read is reported to me and Andrew:**
   - the `carry` count and total;
   - the sidecar `carry` field;
   - the next morning's sweep re-pull of the carried day.

## VERDICT: SIGNED (CTO). The apply gate is OPEN under conditions 1 to 4.

-- 1.0.0_SA_CTO~DELL1
