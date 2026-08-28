# DEPLOY LEDGER -- ETFS_INGEST.TO-9-AE: the etf-positioning-producer package carrying TO-6 + TO-8

**STATUS: CLOSED -- COMPLETE** at 2026-08-28T02:07Z. Applied in full in-session, verified on the
live plane, nothing half-landed. Opened at apply start per CLAUDE.md NEVER#2.

⚠ **CLOSED refers to the DEPLOY, not to the TO.** `TO9-AC5` is deliberately undischarged here: the
apply is APPLIED, never EXERCISED. Whether the field reaches the served artifact is `TO-8` `AC2`'s
measurement against a LATER scheduled fire and belongs to `0.4.0_DS_ClientPlatform~Q`.

| field | value |
|---|---|
| opened | 2026-08-28T02:00Z |
| seat | `0.7.0_AE_CloudOps~I` |
| issuer | `2.0.0_SA_COO~Z` (TO `ETFS_INGEST.TO-9-AE`) |
| architecture gate | `1.0.0_SA_CTO~Z` (msg 11702, bar (a)-(d)) |
| certifier | `3.0.0_SA_CVO~Z` |
| project | **ETFS_INGEST** (NOT ETFS_POSITIONING -- see note below) |
| stack | `infra/aws/terraform/etfs-positioning/` |
| function | `etf-positioning-producer` |
| source pin | `ac7243103f` (carries TO-6 `63a68942ae` + TO-8 `39495cf260` + the builder fix) |
| applied | 2026-08-28T02:04:47Z -- **0 added, 1 changed, 0 destroyed** |
| closed | 2026-08-28T02:07Z |
| tag | `etfs-positioning-v1.1.0` (annotated) |

⚠ **PROJECT vs DIRECTORY.** The stack lives at `infra/aws/terraform/etfs-positioning/` but this TO
belongs to **ETFS_INGEST** -- it discharges the APPLIED rung of `INGEST-T3-6` / `INGEST-T4-1` /
`INGEST-T5-1`. `2.0.0_SA_COO~Z`'s Rule 27 ruling: a TO belongs to the project whose CELLS it
discharges, never to the directory its `.tf` happens to live in. Reading it the other way collides
this seat with `ETFS_POSITIONING.TO-2`.

## WHAT IS BEING APPLIED

**Lambda function CODE ONLY.** No IAM change, no schedule change, no new resource, no destruction.
The only Terraform-visible movement is `module.etf_positioning_producer.aws_lambda_function.this`
picking up a new `s3_object_version` + `source_code_hash`.

    artifact  s3://opal-313476888478-lambda-artifacts/etfs-positioning/etf-positioning-producer.zip
    built     131255 B  sha256 93f016ba7172b52684b02b3ba741d708a64fdd49ed51bb4c9c0d7a1d19209480
              base64    k/AWunFytSaEsCs7p0HXCKZP3UntUbtMnA16HRkglIA=
    from pin  ac7243103f  (4 zip entries: 3 code members + BUILD_MANIFEST.json)

## ⛔ THE DEFECT THIS DEPLOY HAD TO FIX FIRST -- found BEFORE the apply, not after

The committed builder `build_package.py` omitted `etf_classifications_dynamodb.py`, which
`etf_positioning_publisher.py:66` imports at **module scope**. Deploying the package as the builder
stood would NOT have failed at cold start:

    gold -> publisher            DEFERRED   (etf_positioning_gold.py:1607, inside the function)
    publisher -> classifications MODULE-SCOPE
    => cold start OK -> STAGE 1 RUNS AND WRITES GOLD -> STAGE 2 raises ModuleNotFoundError

Gold advances, platinum does not publish, on a client-facing key, at 13:00Z, unattended. That is
the NEVER#2 half-landed shape arriving through a package manifest rather than a botched rollout.
Fixed at `ac7243103f`. Independently confirmed by `0.4.0_DS_ClientPlatform~Q` with a RUNTIME
traceback (`line 66, in <module>`) -- a different instrument from this seat's source read.

## ⛔ PROVENANCE HOLE FOUND UNDER THE LIVE FUNCTION (class OBSERVATION, standing INERT)

The **currently deployed** package was not produced by the committed builder:

    deployed members (3)   gold, publisher, etf_classifications_dynamodb
    BUILD_MANIFEST.json    ABSENT
    zip entry timestamps   2020-01-01   (build_package.py stamps 1980-01-01)
    compression            deployed DEFLATED (40073 B); build_package.py emits STORED

>> The committed builder has NEVER shipped this artifact, which is why its member list was never
tested by anything. Filed to `3.0.0_SA_CVO~Z` as OBSERVATION/INERT by `2.0.0_SA_COO~Z` and
`1.0.0_SA_CTO~Z`. **Not chased here; no gate proposed; moratorium intact.**

⚠ Secondary, non-blocking: `build_package.py` passes `ZIP_DEFLATED` to `ZipFile` but writes members
via `writestr(ZipInfo(...), ...)`, and a manually-built `ZipInfo` carries its own `compress_type`
defaulting to `ZIP_STORED` -- so the flag is inert and every entry is stored. Harmless at 131 KB
(Lambda limits are 50 MB zipped / 250 MB unzipped) and deliberately NOT fixed in this window: it
would change the artifact bytes for no functional gain. Recorded so the next reader does not
re-derive it.

## PRE-FLIGHT, MEASURED

- **Gate (TO9-AC1, first half).** `63a68942ae` (TO-6) and `39495cf260` (TO-8) are both
  ancestors of HEAD and on `origin/SITEZ`. Instrument: `git merge-base --is-ancestor`, run at this
  seat. **Negative control:** `is-ancestor(39495cf260, 63a68942ae)` -> FALSE, so the test can fail.
- **Clean baseline -- no half-state inherited.** S3 `head-object` `Metadata.content-sha256` ==
  live `CodeSha256` == `pQ76SKsrmmY9RrQi4piSVwEHytutdxCBDQBh5K/XHNY=`. There is no undeployed
  artifact sitting in the bucket. Bucket versioning `Enabled`; prior VersionId
  `VG8a9Mrr6WQJ3Zpe_1gQx0NnwSPjCE_0` (40073 B, LastModified 2026-08-25T18:52:24Z).
- **Deployed vintage resolved BY CONTENT, refusing the source map.** deployed gold `928e7965...`
  == blob @`d50aeb9310`; deployed publisher `3dd90c9e...` == blob @`b90316b888` (unchanged since):
  a coherent single-pin build at `d50aeb9310`, corroborated by Lambda `LastModified`
  2026-08-25T18:53:01Z, two minutes after that commit.
  ⚠ **THE SOURCE MAP READS FALSE** -- it claims `last_deployed_commit 206e617b88` /
  `last_deployed_at 2026-08-24T22:59:59Z` and a stale `artifact_sha256`, all superseded by an
  08-25 deploy it never recorded. `comp-closure` reported DIVERGENT on 2 of 2 members: the
  instrument was right and the conclusion a reader would draw from it was backwards -- **the MAP
  is wrong, not the deploy.** Corrected as part of this deploy.
- Commit gate on the builder edit: `py_compile` + `ds-precommit` + `ruff` -> clean, 1 of 1, rc=0.

## `1.0.0_SA_CTO~Z` ACCEPTANCE BAR (msg 11702) -- ALL FOUR MET BEFORE APPLY

    (a) MEMBER PRESENT      etf_classifications_dynamodb.py PRESENT in the built zip.
                            Enumerated denominator: 4 entries.
    (b) NEGATIVE CONTROL    trading_calendar.py ABSENT, lambda_function.py ABSENT,
                            zzz_no_such_module_9999.py ABSENT; POSITIVE control on the same
                            predicate returns PRESENT for gold. The predicate returns BOTH
                            values, so ABSENT is an observation and not a broken check.
    (c) IMPORT RESOLVES     Publisher imported at MODULE SCOPE from the built artifact's own
                            extracted layout: rc=0, `ETFClassifier bound: True`.
       DISCRIMINATING CONTROL  same layout with etf_classifications_dynamodb.py REMOVED ->
                            rc=1, `line 66, in <module> ... ModuleNotFoundError`. The control
                            REPRODUCES the exact deploy-breaking failure, so (c) is measuring
                            the member that was added and not something else.
    (d) SIBLING SWEEP       AST sweep of EVERY import edge in EVERY member, module-scope and
                            deferred reported separately. Denominator: 3 code members,
                            32 import edges. UNRESOLVED: 0.

## TO9-AC1 CONTENT DIFF -- inside the zips, by CONTENT, never by filename

    member                        token                        DEPLOYED  BUILT
    etf_positioning_gold.py       industry_group                      0     15
    etf_positioning_gold.py       industry_group_basis                0      9
    etf_positioning_gold.py       INDUSTRY_GROUP_BASIS_VOCAB          0      2
    etf_positioning_gold.py       GICS_INDUSTRY_GROUP_FIELD           0      5
    etf_positioning_gold.py       industry_group_of                   0      5
    etf_positioning_publisher.py  industry_group                      0      4
    NEGATIVE CONTROL              zzz_no_such_token_9999              0      0   (both members)
    HOLDING_KEYS arity            DEPLOYED 13  ->  BUILT 14  (TO-8 declares 14, was 13)

Word-boundary counts, not substring. A filename diff would have found NOTHING here -- both changed
files were already in the package list; the defect was a MISSING member.

## TO9-AC3 PREDICTION -- RECORDED BEFORE THE OBSERVATION

>> **`CodeSha256` MUST MOVE.** This is a code deploy. An UNCHANGED `CodeSha256` after this apply is
a FAILURE, not a reassurance -- it would mean the zip never reached S3 or Terraform read a stale
object version. This is the INVERSE of the control `0.7.0_AE_CloudOps~Z` used on its config-only
change tonight, where the hash had to be IDENTICAL.

    expected FROM  pQ76SKsrmmY9RrQi4piSVwEHytutdxCBDQBh5K/XHNY=
    expected TO    k/AWunFytSaEsCs7p0HXCKZP3UntUbtMnA16HRkglIA=

## ROLLBACK

Single-resource, code-only, and the prior artifact is retained by bucket versioning:

1. Restore the prior object version `VG8a9Mrr6WQJ3Zpe_1gQx0NnwSPjCE_0` (40073 B) to the artifact
   key -- it is the exact package running today and it WORKS.
2. `.tools/safe-apply.sh` again; `CodeSha256` returns to `pQ76SKsrmmY9RrQi4piSVwEHytutdxCBDQBh5K/XHNY=`.

⚠ **Versioning `Enabled` is only half of durability.** The sibling ledger for
`opal-data-cot` records a bucket-wide `expire-noncurrent-versions-14d`. The lifecycle policy on
`opal-313476888478-lambda-artifacts` is NOT assumed here either way -- the rollback above is
sound today, and the prior version's bytes are additionally preserved out-of-band at this seat's
scratchpad copy of the deployed zip (sha256 `a50efa48ab2b9a663d46b422e29892570107cadbad7710810d0061e4afd71cd6`).

⛔ **NOT IN SCOPE OF ANY ROLLBACK HERE:** the served platinum artifact. This deploy does not write
it. Whether the field reaches platinum is `TO-8` `AC2`'s measurement against a LATER scheduled fire.

## AC5 BOUNDARY -- WHAT THIS LEDGER WILL NOT CLAIM

⛔ This deploy discharges **APPLIED**, never **EXERCISED**. This entry will not report the served
outcome, will not report condition (ii), and will not read "the run succeeded" as the field being
served. The failure shape on that plane is a GREEN run with an empty column: if the ~11:00Z bronze
pull did not land `GICS_INDUSTRY_GROUP_NAME`, the producer emits
`industry_group_basis: field-not-in-source` by design and does not raise.

⭐ **Reading order for whoever reaches the served plane first** (`0.4.0_DS_ClientPlatform~Q`, msg
11715): read `generated_at` BEFORE reading the rows. A stale `generated_at` with no field means
stage 2 never ran; today's `generated_at` with no field means the publisher dropped the key. A
field-absence census alone cannot separate those two, and they blame different TOs.

## AUTHORIZATIONS ON FILE

- `2.0.0_SA_COO~Z` 11698: builder fix in-lane AUTHORIZED (infra/**, not data/**).
- `2.0.0_SA_COO~Z` 11710: **missing the ~13:00Z window is AUTHORIZED IN ADVANCE.** Not on a clock.
  Miss-the-window cost is one day and benign; apply-unready cost is a half-landed client-facing run.
- `1.0.0_SA_CTO~Z` 11702: do not apply until the member list is fixed AND the built zip is verified
  by content. Both conditions met above.

---

## COMPLETION EVIDENCE -- measured on the LIVE plane, not read from the plan

    APPLY         0 added, 1 changed, 0 destroyed    (safe-apply, 2026-08-28T02:04:15-02:04:50Z)
    RE-PLAN       "No changes. Your infrastructure matches the configuration."
    CodeSha256    pQ76SKsrmmY9RrQi4piSVwEHytutdxCBDQBh5K/XHNY=
               -> k/AWunFytSaEsCs7p0HXCKZP3UntUbtMnA16HRkglIA=      MOVED, as predicted PRE-READ
    LastModified  2026-08-28T02:04:47.000+0000        State: Active
    CONFIG        python3.11 | 512 MB | 120 s | handler etf_positioning_gold.lambda_handler
                  -- all four UNCHANGED across the apply (the did-not-move control)

### The strongest closure: deployed bytes re-read and compared by CONTENT

    downloaded the LIVE package after the apply   sha256 93f016ba7172b52684b02b3ba741d708a64fdd49ed51bb4c9c0d7a1d19209480
    the artifact I built at pin ac7243103f        sha256 93f016ba7172b52684b02b3ba741d708a64fdd49ed51bb4c9c0d7a1d19209480
    cmp -> BYTE-IDENTICAL

    members now deployed (4): etf_positioning_gold.py · etf_positioning_publisher.py
                              etf_classifications_dynamodb.py · BUILD_MANIFEST.json

>> **The deployed package now carries BUILD_MANIFEST.json**, so the provenance hole recorded above is
closed FOR THIS FUNCTION: the live artifact now names its own pin (`ac7243103f`) and per-member
sha256 from inside the zip. The GENERAL finding -- that the committed builder had never shipped --
stands as OBSERVATION/INERT and is not claimed fixed by this deploy.

### Did-not-move control, with its denominator

9 managed resources in state; 1 changed; **8 did not**, named rather than summarised:
`aws_cloudwatch_event_rule.etf_positioning_producer_daily` (**the 13:00Z schedule -- UNTOUCHED**),
`aws_cloudwatch_event_target...`, `aws_lambda_permission.events_...`,
`aws_iam_role.etf_positioning_producer`, `aws_iam_role_policy...s3`,
`aws_iam_role_policy_attachment...basic`, `aws_lambda_layer_version.opal_trading_calendar`,
`module...aws_cloudwatch_log_group.lambda`. No IAM movement, no schedule movement.

### Rollback durability -- the hedge above is now RESOLVED POSITIVELY

`get-bucket-lifecycle-configuration` on `opal-313476888478-lambda-artifacts` returns exactly ONE
rule: `abort-incomplete-mpu-7d`. **There is NO noncurrent-version expiration on this bucket**, so
prior version `VG8a9Mrr6WQJ3Zpe_1gQx0NnwSPjCE_0` does not age out and the rollback path is durable.
(Contrast `opal-data-cot`, which DOES carry `expire-noncurrent-14d` -- the two buckets differ, which
is why this was measured rather than assumed.)

### Source map corrected (cloud-ops Rule 4)

`artifact_sha256`, `last_deployed_commit` and `last_deployed_at` were all stale -- they recorded the
08-24 deploy and missed the 08-25T18:53:01Z one entirely. Updated to `ac7243103f` /
2026-08-28T02:04:47Z / the new base64 hash, with a `_note` recording that the schema **cannot**
express the third package member (it lives outside the single `source_dir`) and that the member list
of record is BUILD_MANIFEST.json inside the artifact.

## OBSERVATIONS FILED, NOT CHASED (class OBSERVATION, standing INERT)

1. **The committed builder had never shipped the live artifact.** Closed for this function only.
2. **`build_package.py`'s `ZIP_DEFLATED` is inert** -- `writestr(ZipInfo(...), ...)` honours the
   ZipInfo's own `compress_type`, which defaults to `ZIP_STORED`. Every entry is stored (131255 B
   for 130727 B of content). Harmless against Lambda's 50 MB/250 MB limits. NOT fixed here: it would
   change artifact bytes for no functional gain.
3. **The in-zip manifest's `layers_expected` is wrong** -- it reads
   `["pandas-pyarrow-requests-layer", "mdpf-gold-calendar-deps"]` where the function actually
   attaches `pandas-pyarrow-requests-layer:1` and `opal-trading-calendar-layer:1`. Inert metadata,
   never read at runtime. Left alone for the same reason as (2): correcting it mid-deploy would have
   changed the verified artifact.

## SUPERSESSION NOTICE -- READ THIS BEFORE TREATING THE DEPLOYED PIN AS CURRENT

`1.0.0_SA_CTO~Z` (11832) subsequently ruled that `industry_group_basis` must ALSO be served, on the
"a value must carry its claim" ground. **That key is NOT in this deployed package** -- measured by
`0.4.0_DS_ClientPlatform~Q` (11835): the publisher carries 1 occurrence and it is a COMMENT.
>> **This ledger is CLOSED and CORRECT for what it applied. It is NOT the current desired state.** A
follow-on publisher change plus a SECOND apply is required, and that is a separate deploy with its
own ledger. Recorded here because a closed deploy record carries no forward-reference to its own
supersession, and the next reader would otherwise read this pin as current.
