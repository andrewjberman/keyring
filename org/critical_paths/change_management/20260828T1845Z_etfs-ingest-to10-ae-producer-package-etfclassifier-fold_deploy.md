# DEPLOY LEDGER -- ETFS_INGEST.TO-10-AE: the etf-positioning-producer package carrying the ETFClassifier fold

**STATUS: CLOSED -- COMPLETE** at 2026-08-28T18:56Z. Applied in full in-session, verified on the
live plane, nothing half-landed. Opened at apply start per CLAUDE.md NEVER#2.

⚠ **CLOSED refers to the DEPLOY, not to the TO.** `INGEST-TO10-AC3` is deliberately undischarged
here: this apply is APPLIED and module-level EXERCISED, but **never EXERCISED END-TO-END**. Whether
the completed labels reach the served artifact is measured on the first SCHEDULED fire and no
ad-hoc run may substitute for it.

| field | value |
|---|---|
| opened | 2026-08-28T18:45Z |
| seat | `0.7.0_AE_CloudOps~I` |
| issuer | `2.0.0_SA_COO~Z` (TO `ETFS_INGEST.TO-10-AE`, face @`b066be7a92`, GO msg 13708) |
| project | **ETFS_INGEST** (NOT ETFS_POSITIONING -- the TO belongs to the project whose CELLS it discharges, never to the directory its `.tf` lives in) |
| cells | `INGEST-T3-6`, `INGEST-T5-1` -- APPLIED rung, no new cell |
| stack | `infra/aws/terraform/etfs-positioning/` |
| function | `etf-positioning-producer` |
| source pin | `b066be7a922a9754ae7f4d278882536a009cbbea` (contains the fold `b0e1f33471`) |
| applied | 2026-08-28T18:49:14Z -- **0 added, 1 changed, 0 destroyed** |
| closed | 2026-08-28T18:56Z |
| tag | `etfs-positioning-v1.4.0` (annotated, cut ON THE PIN) |

## WHY -- MEASURED AT THIS SEAT ON THE APPLIED PLANE, NOT RELAYED

The TO's premise is a timestamp comparison. **A timestamp is the weak form of this claim**, so it was
re-established by CONTENT before anything was touched:

    live CodeSha256          wuu+/cHD5gHb3B1iY3wjGq4rB0ozzF7Hm/ooH086P8I=
    live LastModified        2026-08-28T02:43:57.000+0000        State Active
    deployed zip             150342 B  sha256 c2ebbefdc1c3e601dbdc1d62637c231aae2b074a33cc5ec79bfa281f4f3a3fc2
    deployed member          etf_classifications_dynamodb.py  6452 B  sha256 8138da0300ea83c3...
    in-zip BUILD_MANIFEST    source_vintage.commit = 25f30acc63166f21f47c71550a5dbc12443ab3b6

    git show 25f30acc63:infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py
                             -> 8138da0300ea83c3...   MATCHES the deployed member.
                                The in-zip manifest is TRUTHFUL: the deployed bytes ARE 25f30acc63's.
    git show b0e1f33471:<same path>  -> c677e8a5f6996555...  14027 B   (the fold)
    git show b066be7a92:<same path>  -> c677e8a5f6996555...  14027 B   (identical -- the pin)

**The deployed classifier was the PRE-fold vintage, established by blob identity, not by clock.**
Negative control on the same read: `def resolve` is present at `:262` in the pin's classifier and
**ABSENT** from the deployed member (only `class ETFClassifier` at `:49`). The absence is therefore
discriminating rather than an artifact of the pattern.

## THE DEPLOYED PAIR WAS SELF-CONSISTENT -- NOTHING WAS HALF-LANDED BEFOREHAND

    deployed publisher   sha256 62200af215926aa4   == git show 25f30acc63:<publisher>
    pin publisher        sha256 45cb78b110bd7809   -- imports `resolve` at MODULE SCOPE (:79)

The live function ran the pre-fold publisher AND the pre-fold classifier. It was not broken; it
served the OLD truncated labels. **That also named the hazard this apply had to not create in the
other direction:** shipping the pin's publisher WITHOUT the pin's classifier is an `ImportError` at
`:79`, module scope, inside a publisher that gold imports LAZILY
(`etf_positioning_gold.py:1607`) -- so stage 1 would run and write gold, and stage 2 would raise.
The NEVER#2 half-landed shape. The builder's 3-member PACKAGE ships both.

## WHAT WAS APPLIED

**Lambda function CODE ONLY.** No IAM change, no schedule change, no new resource, no destruction.

    artifact  s3://opal-313476888478-lambda-artifacts/etfs-positioning/etf-positioning-producer.zip
    built     162733 B  sha256 a9093da212e284e227267be3fcd9dc026b3522ea04224923470a5bf04205a2e4
              base64    qQk9ohLihOInJnvj/NncAms1IuoEIkkjRwpb8EIFouQ=
    from pin  b066be7a92  (4 zip entries: 3 code members + BUILD_MANIFEST.json)
    VersionId hJpn.bewspw6DHf8Suot920st5dxfAhN -> 7r5NQeGQE9Nj.2G9ARqpZMBfEfIwfiii

    PLAN      0 to add, 1 to change, 0 to destroy
              the ONLY moving resource: module.etf_positioning_producer.aws_lambda_function.this
              (s3_object_version + source_code_hash + last_modified)
    APPLY     .tools/safe-apply.sh, applying the REVIEWED PLAN FILE (tfplan.to10ae), 18:49:14Z
              -> 0 added, 1 changed, 0 destroyed
    RE-PLAN   "No changes." -- and verified with `-detailed-exitcode` rc=0 rather than by reading
              the sentence, because the sentence is not a discriminating oracle.

**DID NOT MOVE: 9 of the 10 managed resources in state** -- denominator from
`terraform state list`. Named explicitly because it is the one that matters:
`aws_cloudwatch_event_rule.etf_positioning_producer_daily` reads
`cron(0 13 * * ? *)` / `ENABLED` on the live primitive after the apply. **That rule is the event
AC3 is gated on.**

## VERIFICATION -- AC1, against the BUILD INPUT

The live package was re-downloaded from `Code.Location` AFTER the apply and is **byte-identical**
to the artifact built at the pin (`cmp`, sha256 `a9093da2...`). Every member then compared to git:

    IDENTICAL  etf_positioning_gold.py          <- b066be7a92:data/etfs/scripts/gold/...
    IDENTICAL  etf_positioning_publisher.py     <- b066be7a92:data/etfs/scripts/gold/...
    IDENTICAL  etf_classifications_dynamodb.py  <- b066be7a92:infra/aws/lambda/v2_portal/_shared/...
    in-zip BUILD_MANIFEST source_vintage.commit == b066be7a922a9754ae7f4d278882536a009cbbea

    NEGATIVE CONTROLS (both must differ, and both do):
      deployed classifier vs 25f30acc63's  -> DIFFERS
      deployed publisher  vs 25f30acc63's  -> DIFFERS

⛔ **`CodeSha256` moved and `LastModified` advanced. NEITHER IS CITED AS ACCEPTANCE** -- both are
true of any deploy, including one built from the wrong input. The byte-identity above is the claim.

## EXERCISED -- at the module rung, on the bytes AWS is serving

`self_test()` run against the classifier extracted from the POST-APPLY download:

    completions: 7 PASS / 0 FAIL     negative controls: 5 REFUSED / 0 ACCEPTED

⚠ **This is the MODULE rung, not the pipeline rung.** It proves the decode works in the shipped
bytes. It does not prove the producer runs, and it is not AC3.

## AC4 -- NO REGRESSION

Pre-state MEASURED on the served artifact `s3://opal-data-portal-v2/platinum/etfs/positioning_data.json`
(146944 B, LastModified 2026-08-28T13:01:26Z, `data_date` 2026-08-27 -- today's fire, i.e. the
pre-fold bytes):

    ROW DENOMINATOR                189
    rows carrying industry_group   189 of 189
    non-null values                180
    basis: observed 180 | not-applicable-non-equity 8 | absent-from-source 1
    distinct industry_group values 23

The deployed module was then driven over all 189 served rows through the publisher's own
`_industry_group` logic (`code=None`, the current production path -- `industry_group_code` reaches
gold on a later act):

    rows in / rows out             189 / 189
    rows MISSING either key        0
    rows that LOSE a value         0
    non-null before / after        180 / 180
    rows the decode CHANGES        59, across 7 distinct labels

⚠ **THAT 59-OF-189 IS A PREDICTION, NOT A SERVED MEASUREMENT.** It is computed from TODAY's served
artifact as input; the fire's input is tomorrow's pull, so the count can legitimately move with the
holdings. It is recorded here because it independently reproduces the issuing seat's figure **from a
different instrument** (their simulation was pre-deploy from source; this is the deployed bytes over
the served rows) -- corroboration of the radius, never a bar for AC3 to clear.

## ROLLBACK -- NOT EXERCISED, stated as available

Same-window: the previous artifact is addressable at VersionId `hJpn.bewspw6DHf8Suot920st5dxfAhN`
and the previous package is on disk at this seat (sha256 `c2ebbefd...`). Re-upload + re-apply
restores byte-identity. No data is mutated by this deploy. **Not needed and not run.**

## RULE 4 -- SOURCE MAP UPDATED

`infra/aws/lambda/ci/lambda-source-map.json` `functions["etf-positioning-producer"]`: the three
vintage fields advanced `25f30acc63` / `wuu+...` / `02:43:57Z` -> `b066be7a92` / `qQk9...` /
`18:49:14Z`. Diff is exactly 3 changed lines; JSON round-trip verified byte-clean before editing so
the write could not reformat the other 197 entries.
