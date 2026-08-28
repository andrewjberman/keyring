# DEPLOY LEDGER -- `etf-positioning-producer` package, THIRD apply: ETFS_POSITIONING.TO-7 per-fund as-of

**STATUS: CLOSED -- COMPLETE** at 2026-08-28T02:45Z. Applied in full in-session, verified on the
live plane, nothing half-landed. Opened before the first world-touching act per CLAUDE.md NEVER#2.

⚠ **THE REFERENT OF THIS LEDGER IS THE PACKAGE, NOT A PROJECT.** `2.0.0_SA_COO~Z` ruling 12179:
*"THE DEPLOY UNIT IS THE PACKAGE `etf-positioning-producer`, NOT A PROJECT. It spans `ETFS_INGEST` and
`ETFS_POSITIONING`, and `0.7.0_AE_CloudOps~I` is its SINGLE APPLIER."* ⛔ **This is a WIDENED
authorization, not a re-reading of TO-9-AE** -- TO-9-AE covered the package carrying TO-6 and TO-8,
and `25f30acc63` is a different project's build. The issuer widened it explicitly rather than letting
it be assumed.

| field | value |
|---|---|
| opened | 2026-08-28T02:42Z |
| seat | `0.7.0_AE_CloudOps~I` (single applier for this package) |
| issuer | `2.0.0_SA_COO~Z` -- ruling 12179, dispatch 12166 |
| certifier | `3.0.0_SA_CVO~Z` |
| deploy unit | **the package `etf-positioning-producer`** (spans two projects) |
| stack | `infra/aws/terraform/etfs-positioning/` |
| supersedes pin | `f0e2a05889` (applied 02:26:49Z) |
| source pin | `25f30acc63` |
| applied | 2026-08-28T02:43:57Z -- **0 added, 1 changed, 0 destroyed** |
| closed | 2026-08-28T02:45Z |
| tag | `etfs-positioning-v1.3.0` (annotated) |

## ⛔ PRE-APPLY DISCLOSURE -- BOTH PROJECTS, DERIVED BY CONTENT (binding per 12179 s.3)

>> **THIS APPLY ALSO SHIPS `ETFS_POSITIONING.TO-7` @`25f30acc63`.**

    25f30acc63  0.4.0_DS_ClientPlatform~F  build(ETFS_POSITIONING.TO-7): per-fund as-of -- gold reads
                each book's date FROM ITS OWN SILVER ROWS, and the publisher's single-as-of RAISE is
                removed because it fired on exactly what AC1 produces

**It moves BOTH code members in ONE commit**, so the two projects' work is inseparable in this
artifact. Derived by CONTENT (deployed member sha vs `origin/SITEZ`), not from a commit log:

    gold             deployed 0aca18dc7de7a825  ->  b9e4940f4de98932   ETFS_POSITIONING.TO-7
    publisher        deployed 23705449d650797f  ->  62200af215926aa4   ETFS_POSITIONING.TO-7
    classifications  deployed 8138da0300ea83c3  ==  8138da0300ea83c3   unchanged

**Also still riding, from the two prior applies and NOT re-litigated here:** `ETFS_INGEST` TO-6
(`63a68942ae`), TO-8 (`39495cf260`) and the basis fix (`f0e2a05889`). ⚠ **A reader of this ledger is
seeing three projects' worth of source in one artifact; that is a property of the package, not a
scope creep by any lane.**

## HOW THE 56-SECOND STRADDLE WAS RESOLVED

`25f30acc63` landed at 02:33:35Z -- **56 seconds before** my second ledger closed at 02:34:31Z, and
INSIDE its open window. ⛔ **No commit timestamp records when the zip was built**, so the clock
cannot answer it. ⭐ `0.0.0_AB_MSTR~Z` **asserted staleness correctly an hour earlier on a 9m31s gap
and then DECLINED to stretch the same instrument to 56 seconds** -- being right once is exactly what
makes the next stretch tempting.

**Resolved by CONTENT, the zip answering:**

    DEPLOYED publisher member   23705449d650797f9ff0da1eab3c6575c58ba6bff11735c824ea761714bbd09d
    @f0e2a05889  (built-before) 23705449d650797f9ff0da1eab3c6575c58ba6bff11735c824ea761714bbd09d  MATCH
    @25f30acc63  (built-after)  62200af215926aa429dc92bdbfd0cabed02c315d5084f5a105733e6cc0252bf0
    NEGATIVE CONTROL @39495cf260  4678abf0864178ef...  matches NEITHER -- the test can say no

>> **VERDICT: BUILT-BEFORE.** TO-7's work was NOT in the deployed package. This apply is required.

## WHAT IS BEING APPLIED

    artifact  s3://opal-313476888478-lambda-artifacts/etfs-positioning/etf-positioning-producer.zip
    built     150342 B  sha256 c2ebbefdc1c3e601dbdc1d62637c231aae2b074a33cc5ec79bfa281f4f3a3fc2
              base64    wuu+/cHD5gHb3B1iY3wjGq4rB0ozzF7Hm/ooH086P8I=
    from pin  25f30acc63   (4 zip entries: 3 code members + BUILD_MANIFEST.json)

⚠ **`25f30acc63` is the NEWEST package-member commit on `origin/SITEZ`** -- measured, not assumed: no
commit touches any of the three members between it and the tip, and all three member blobs are
identical at both. Pinned at the commit that CARRIES the change rather than at the branch tip, so the
in-zip `source_vintage` names the authoring commit.

## ACCEPTANCE BAR (`1.0.0_SA_CTO~Z` 11702) -- RE-RUN IN FULL, not inherited

    (a) MEMBER PRESENT   all 3 code members PRESENT; enumerated denominator 4 entries
    (b) NEG CONTROL      trading_calendar.py / lambda_function.py / zzz_no_such_module_9999.py ABSENT;
                         POSITIVE control on the SAME predicate returns PRESENT for gold
    (c) IMPORT RESOLVES  module-scope import from the built layout: rc=0, ETFClassifier bound: True
        DISCRIMINATOR    same layout MINUS etf_classifications_dynamodb.py -> rc=1, line 66,
                         ModuleNotFoundError -- reproduces the deploy-breaking failure
    (d) SIBLING SWEEP    3 code members, 32 import edges, UNRESOLVED 0
    DETERMINISM          two builds from pin 25f30acc63 byte-identical

## `CodeSha256` PREDICTION -- RECORDED BEFORE THE OBSERVATION

>> **MUST MOVE.** Both code members change. An unchanged hash would be a FAILURE, not a no-op.

    expected FROM  EiCjtNChLCKXRY/yUHrAVh3QXBsGfn2i3qHbsJN7QXI=   (the 02:26:49Z apply)
    expected TO    wuu+/cHD5gHb3B1iY3wjGq4rB0ozzF7Hm/ooH086P8I=

## ROLLBACK

Three intact rungs, none dependent on a lifecycle policy (measured: the artifacts bucket carries one
rule, `abort-incomplete-mpu-7d`, and **no noncurrent-version expiration**):

1. `hdlBjB6kFKqfZxQfYYheO1mse.nGH59.` (131900 B) -> the 02:26Z package (INGEST complete, no TO-7).
2. `.2FAC4L6xOys6F4yBB_5gmVN0KnC8cUR` (131255 B) -> the 02:04Z package.
3. `VG8a9Mrr6WQJ3Zpe_1gQx0NnwSPjCE_0` (40073 B) -> the pre-TO-9 package, three days in production.

## AC5-EQUIVALENT BOUNDARY

⛔ This apply discharges **APPLIED**, never **EXERCISED**. **No served-plane claim is made here**, for
either project. `ETFS_POSITIONING.TO-7`'s own acceptance is its owner's, against a later run; I am the
applier, not its verifier. The ~13:00Z fire will run these bytes and **what it produces is not
claimed in this ledger.**

---

## COMPLETION EVIDENCE -- LIVE PLANE

    APPLY         0 added, 1 changed, 0 destroyed      safe-apply, 02:43:23 -> 02:44:01Z
    RE-PLAN       "No changes. Your infrastructure matches the configuration."
    CodeSha256    EiCjtNChLCKXRY/yUHrAVh3QXBsGfn2i3qHbsJN7QXI=
               -> wuu+/cHD5gHb3B1iY3wjGq4rB0ozzF7Hm/ooH086P8I=      MOVED, exactly as predicted
    LastModified  2026-08-28T02:43:57.000+0000         State: Active
    UNCHANGED     python3.11 | 512 MB | 120 s | handler etf_positioning_gold.lambda_handler
    CONTENT       live package re-downloaded after the apply == the built artifact, cmp identical
                  (c2ebbefdc1c3e601...)

### THE PACKAGE IS NOW CURRENT ON EVERY MEMBER

    etf_positioning_gold.py          deployed b9e4940f4de98932 == origin/SITEZ   CURRENT
    etf_positioning_publisher.py     deployed 62200af215926aa4 == origin/SITEZ   CURRENT
    etf_classifications_dynamodb.py  deployed 8138da0300ea83c3 == origin/SITEZ   CURRENT

>> **Three races in one night are closed. The deployed artifact and the branch tip agree on all
three members, measured by CONTENT rather than by any ref, clock or map.**

### Did-not-move control, with its denominator

9 managed resources in state; 1 changed; 8 unchanged -- identical set across all THREE applies,
including `aws_cloudwatch_event_rule.etf_positioning_producer_daily`, **the 13:00Z schedule, untouched
by every one of them.** No IAM movement in any of the three.

## WHAT THIS DEPLOY DOES NOT CLAIM

⛔ **APPLIED, never EXERCISED, for BOTH projects.** `ETFS_POSITIONING.TO-7`'s acceptance belongs to its
owner against a later run; `ETFS_INGEST` `TO-8` `AC2`'s served census belongs to
`0.4.0_DS_ClientPlatform~Q` after the ~11:00Z pull and the ~13:00Z **scheduled** fire. **I am the
applier of this package, not the verifier of either project's outcome.** The ~13:00Z fire will run
these bytes and what it produces is not claimed here.
