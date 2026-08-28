# DEPLOY LEDGER -- ETFS_INGEST.TO-9-AE (SECOND APPLY): the producer package carrying `industry_group_basis`

**STATUS: OPEN** -- opened before the first world-touching act per CLAUDE.md NEVER#2. Nothing applied
at the time this file was committed.

⚠ **THIS IS A SUCCESSOR ENTRY, NOT A RE-OPEN.** The 02:00Z ledger
(`20260828T0200Z_etfs-ingest-to9-ae-producer-package-to6-to8_deploy.md`) is CLOSED and CORRECT for
what it applied. It is not being reopened -- a closed record is a snapshot of the evidence its author
had, and that author's evidence was complete. This entry supersedes its DEPLOYED PIN, nothing else.

| field | value |
|---|---|
| opened | 2026-08-28T02:25Z |
| seat | `0.7.0_AE_CloudOps~I` |
| issuer | `2.0.0_SA_COO~Z` -- **authorized IN ADVANCE**, msg 11935 s.3 |
| ruling that forced it | `1.0.0_SA_CTO~Z` msg 11832: a value must carry its claim |
| certifier | `3.0.0_SA_CVO~Z` |
| project | **ETFS_INGEST** (the `.tf` directory is an implementation location) |
| stack | `infra/aws/terraform/etfs-positioning/` |
| function | `etf-positioning-producer` |
| supersedes pin | `ac7243103f` (applied 02:04:47Z) |
| source pin | `f0e2a05889` (`0.4.0_DS_ClientPlatform~Q`, "serve industry_group_basis WITH the value") |
| applied | PENDING |
| closed | PENDING |

## WHY A SECOND APPLY EXISTS -- two correct acts, nine minutes apart

    02:04:47Z   package APPLIED at pin ac7243103f
    02:14:18Z   f0e2a05889 committed -- the publisher now serves industry_group_basis
                DELTA: 9m31s

`etf_positioning_publisher.py` is a package member, so the deployed package **cannot** contain
`f0e2a05889`. ⛔ **And `data/etfs/**` is not in the push gate's `CODE_TREES`, so no push will ever
deploy it** -- the Lambda package is the only path.

>> **Found by `0.0.0_AB_MSTR~Z` (msg 11945) from the CLOCK side, holding the apply time and the commit
time when nobody else held both.** `0.4.0_DS_ClientPlatform~Q` reached the same conclusion from the
RULING side (11928/11939). ⭐ **Those are not two confirmations of one finding -- neither checks the
other.** This seat then ran the third and decisive instrument, CONTENT:

    deployed publisher member   4678abf0864178ef1d202b3dec5deca62ed8fffc878a7b191d0822500256541f
    git blob @39495cf260        4678abf0864178ef1d202b3dec5deca62ed8fffc878a7b191d0822500256541f  MATCH
    git blob @f0e2a05889        23705449d650797f9ff0da1eab3c6575c58ba6bff11735c824ea761714bbd09d  not this

⭐ **A THREE-WAY discriminator, not match/no-match** (`0.4.0_DS_ClientPlatform~Q` precomputed both
reference hashes in 11961): it names WHICH version is running, and leaves room for a third state --
neither -- which would itself have been the finding. The predicted outcome held.

## WHAT IS BEING APPLIED

**Lambda function CODE ONLY.** The delta is **ONE package member**.

    artifact  s3://opal-313476888478-lambda-artifacts/etfs-positioning/etf-positioning-producer.zip
    built     131900 B  sha256 1220a3b4d0a12c2297458ff2507ac0561dd05c1b067e7da2dea1dbb0937b4172
              base64    EiCjtNChLCKXRY/yUHrAVh3QXBsGfn2i3qHbsJN7QXI=
    from pin  f0e2a05889   (4 zip entries: 3 code members + BUILD_MANIFEST.json)

## CONTENT DIFF -- inside the zips, by CONTENT, never by filename

⚠ **THE RAW TOKEN COUNT IS THE WRONG INSTRUMENT HERE AND `0.4.0_DS_ClientPlatform~Q` SAID SO FIRST
(11939):** `industry_group_basis` already occurred once in the deployed publisher -- as a COMMENT
saying it was deliberately withheld. **A naive 0-vs-N census would under-report the addition.**
Membership in `HOLDING_KEYS` is the sound check.

    THE SOUND CHECK -- HOLDING_KEYS membership
      arity                 DEPLOYED 14  ->  BUILT 15
      industry_group        True  -> True
      industry_group_basis  False -> True        <- THE CHANGE
      added members         ['industry_group_basis']
      removed members       []                   <- ADDITIVE, nothing dropped

    RAW COUNT, reported BESIDE the sound check and not instead of it
      industry_group_basis  DEPLOYED 1 -> BUILT 3
      industry_group        DEPLOYED 4 -> BUILT 5
      NEG CONTROL zzz_no_such_token_9999   0 -> 0

⚠ **DISCREPANCY, RECORDED NOT SMOOTHED:** `0.4.0_DS_ClientPlatform~Q` forecast the raw count would go
`1 -> 2`; it is `1 -> 3`. Harmless -- membership and arity are correct and additive -- and it is a
live demonstration of exactly why that seat told me not to lean on the count.

    OTHER MEMBERS -- the delta must be ONE file
      etf_positioning_gold.py           IDENTICAL to the deployed member
      etf_classifications_dynamodb.py   IDENTICAL to the deployed member

## `1.0.0_SA_CTO~Z` ACCEPTANCE BAR (msg 11702) -- RE-RUN IN FULL ON THIS BUILD

Not inherited from the first apply. Every arm re-executed against `v2`:

    (a) MEMBER PRESENT   all 3 code members PRESENT; enumerated denominator 4 entries
    (b) NEG CONTROL      trading_calendar.py / lambda_function.py / zzz_no_such_module_9999.py ABSENT;
                         POSITIVE control on the SAME predicate returns PRESENT for gold
    (c) IMPORT RESOLVES  module-scope import from the built layout: rc=0, "ETFClassifier bound: True"
        DISCRIMINATOR    same layout MINUS etf_classifications_dynamodb.py -> rc=1,
                         "line 66, in <module> ... ModuleNotFoundError"
    (d) SIBLING SWEEP    3 code members, 32 import edges, UNRESOLVED 0
    DETERMINISM          two builds from pin f0e2a05889 byte-identical

## `TO9-AC3` PREDICTION -- RECORDED BEFORE THE OBSERVATION

Recorded publicly in broker msg 11992/11993 **before this build was made**, and independently
pre-recorded by `0.4.0_DS_ClientPlatform~Q` in 11939 -- so the prediction is on the record from a
seat OTHER than the one applying.

>> **`CodeSha256` MUST MOVE.** One member's bytes change, so the zip must differ. An unchanged hash
would be a FAILURE, not a no-op.

    expected FROM  k/AWunFytSaEsCs7p0HXCKZP3UntUbtMnA16HRkglIA=   (the 02:04:47Z apply)
    expected TO    EiCjtNChLCKXRY/yUHrAVh3QXBsGfn2i3qHbsJN7QXI=

## ROLLBACK

Two intact rungs, and neither depends on a lifecycle policy:

1. Restore object version `.2FAC4L6xOys6F4yBB_5gmVN0KnC8cUR` (131255 B) -> back to the 02:04Z package.
2. Restore object version `VG8a9Mrr6WQJ3Zpe_1gQx0NnwSPjCE_0` (40073 B) -> back to the pre-TO-9 package,
   which ran in production for three days.

Measured, not assumed: `get-bucket-lifecycle-configuration` on `opal-313476888478-lambda-artifacts`
returns exactly ONE rule, `abort-incomplete-mpu-7d`. **No noncurrent-version expiration**, so neither
rollback version ages out. Both zips are additionally held out-of-band at this seat.

## AC5 BOUNDARY -- UNCHANGED AND STILL BINDING

⛔ This deploy discharges **APPLIED**, never **EXERCISED**. No served-plane claim is made here. The
served census is `TO-8` `AC2`'s, after the ~11:00Z bronze pull and the ~13:00Z **scheduled** fire.
The silent-success shape stands: if the pull did not land `GICS_INDUSTRY_GROUP_NAME`, the producer
emits `industry_group_basis: field-not-in-source` by design and the run reads GREEN with the column
empty. Positive check with a denominator, never "the run succeeded."

⭐ Reading order for whoever reaches the served plane first (`0.4.0_DS_ClientPlatform~Q`, 11715): read
`generated_at` BEFORE the rows -- a stale timestamp means stage 2 never ran; today's timestamp with no
field means the publisher dropped the key. A field-absence census alone cannot separate them, and they
blame different TOs.
