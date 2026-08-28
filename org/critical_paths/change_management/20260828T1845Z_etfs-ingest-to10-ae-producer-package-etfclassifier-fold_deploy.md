# DEPLOY LEDGER -- ETFS_INGEST.TO-10-AE: the etf-positioning-producer package carrying the ETFClassifier fold

**STATUS: OPEN** -- opened at apply start per CLAUDE.md NEVER#2, before the first world-touching act
(the S3 upload). Closed at completion in the same session, or rolled back and escalated loud.

| field | value |
|---|---|
| opened | 2026-08-28T18:45Z |
| seat | `0.7.0_AE_CloudOps~I` |
| issuer | `2.0.0_SA_COO~Z` (TO `ETFS_INGEST.TO-10-AE`, face @`b066be7a92`, GO msg 13708) |
| project | **ETFS_INGEST** (NOT ETFS_POSITIONING -- the TO belongs to the project whose CELLS it discharges, never to the directory its `.tf` lives in) |
| cells | `INGEST-T3-6`, `INGEST-T5-1` -- APPLIED rung, no new cell |
| stack | `infra/aws/terraform/etfs-positioning/` |
| function | `etf-positioning-producer` |
| source pin | `b066be7a92` (contains the fold `b0e1f33471`) |
| applied | PENDING |
| closed | PENDING |
| tag | PENDING |

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

**The deployed classifier is the PRE-fold vintage, established by blob identity, not by clock.**
Negative control on the same read: `def resolve` is present at `:262` in the pin's classifier and
**ABSENT** from the deployed member (only `class ETFClassifier` at `:49`). The absence is therefore
discriminating rather than an artifact of the pattern.

## THE DEPLOYED PAIR IS SELF-CONSISTENT -- NOTHING IS HALF-LANDED RIGHT NOW

    deployed publisher   sha256 62200af215926aa4   == git show 25f30acc63:<publisher>
    pin publisher        sha256 45cb78b110bd7809   -- imports `resolve` at MODULE SCOPE (:79)

The live function runs the pre-fold publisher AND the pre-fold classifier. It is not broken; it
serves the OLD truncated labels. **That also names the hazard this apply must not create:** shipping
the pin's publisher WITHOUT the pin's classifier is an `ImportError` at `:79`, module scope, inside a
publisher that gold imports LAZILY (`etf_positioning_gold.py:1607`) -- so stage 1 would run and write
gold, and stage 2 would raise. The NEVER#2 half-landed shape. The builder's 3-member PACKAGE ships
both, which is why the member list is the thing to verify and not the zip's existence.

## WHAT IS BEING APPLIED

**Lambda function CODE ONLY.** No IAM change, no schedule change, no new resource, no destruction.
The only Terraform-visible movement expected is
`module.etf_positioning_producer.aws_lambda_function.this` picking up a new `s3_object_version` +
`source_code_hash`.

    artifact  s3://opal-313476888478-lambda-artifacts/etfs-positioning/etf-positioning-producer.zip
    from pin  b066be7a92
    members   3 code + BUILD_MANIFEST.json

⛔ **The schedule must NOT move.** `aws_cloudwatch_event_rule.etf_positioning_producer_daily`
(`cron(0 13 * * ? *)`) is the event AC3 is gated on; a plan that touches it is a STOP, not a nuance.

## ROLLBACK

Same-window: the previous artifact is addressable by its S3 VersionId, and the previous package is
already on disk at this seat (sha256 `c2ebbefd...`). Re-upload + re-apply restores byte-identity.
No data is mutated by this deploy.

## PIN CURRENCY

The three PACKAGE members are byte-identical between the fold `b0e1f33471` and the pin `b066be7a92`
(`git diff --name-only` over exactly those three paths: EMPTY; positive control over all paths:
2 files, the ledger and the TO face). So pinning at the TO's own face commit ships the fold's bytes
and nothing else.
