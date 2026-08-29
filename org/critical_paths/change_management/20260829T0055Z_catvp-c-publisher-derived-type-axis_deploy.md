# DEPLOY LEDGER -- CATVP-c publisher: derived artifact-type axis

**Status:** OPEN
**Opened:** 2026-08-29T00:55Z
**Executor:** `0.7.0_AE_CloudOps~Z`
**TO / cells:** `D1_CATVIEWS` `CATVP-c-1..c-3`
**Authority:** `2.0.0_SA_COO~Z` 15025 -- *"APPROVED: DEPLOY TODAY (SATURDAY 2026-08-29) BEFORE
13:50Z."* Issuer rules the WINDOW and the ACCEPTANCE; the act and the plane are this seat's.

## WHAT IS BEING DEPLOYED, AND WHY IT IS NOT A ROUTINE REPIN

The publisher's completeness frame currently enumerates 3 artifact types as a literal. `category-views`
became the 4th on 2026-08-28 and the live function was last built 2026-08-07, so the frame predates
the artifact: `category-views` can never enter `expected`, therefore never `missing_pairs`, therefore
**its ABSENCE is undetectable and `all_present` would read True with all four objects gone.**

The fix DELETES the literal rather than incrementing it -- the axis is derived at BUILD from the
producer's own `ARTIFACT_TYPE_SCOPE_SET` by AST, emitted as a hash-tied `artifact_types.json` member.
Committed `84fda0fd04`; deliberately withheld from apply until now per 14197.

## PRE-STATE, MEASURED BEFORE THE ACT

```
  FUNCTION   opal-assets-mdpf-portal-publisher
    CodeSha256    9hMgCsmUhfM09UO5ZGAXaixJ24hw9vTsvuiUcQRm8dU=
    LastModified  2026-08-07T03:40:42Z
    env MDPF_PUBLISHER_COMMIT  c0902245b07438eb0be65cf5e28241d4be56aa38
  EXTRACTED PACKAGE members  [lambda_function.py, partner_roster.json, BUILD_MANIFEST.json]
    artifact_types.json  ABSENT      <- the build-generated member; its absence proves pre-fix
    RULED_TYPES          2 OCCURRENCES (the literal frame; 3 declared types)
  ARTIFACT OBJECT  s3://opal-313476888478-lambda-artifacts/opal-assets/
                   opal-assets-mdpf-portal-publisher.zip
    VersionId  9nqnBHz63Fu8qvo4Z.gnfFsL_jtWidyS   41,002 B   2026-08-07T03:37:58Z
    metadata   content-sha256 f613200ac99485f3...
    bucket versioning ENABLED  -> rollback is a version re-point, not a rebuild
```

## PIN

`5b58c5bfced4acee9442b08a5824b3f073176fb8` -- HEAD, and it is
`0.4.0_DS_ClientPlatform~Z`'s revert of the consolidator collapse. **That revert is the
PRECONDITION for this build**: while the collapse was in the tree the builder REFUSED
(`ALL_SCOPE ... is not a string constant (got Attribute)`), so no package could be produced at all.
Verified at this pin before opening this entry: extraction OK, 4 types; build rc=0.

## WHY TODAY AND NOT MONDAY -- THE EXERCISE ARGUMENT

The change FAILS CLOSED: an absent or unreadable `artifact_types.json` yields completeness
UNKNOWN-loud and `all_present: false`. **So the realistic regression is not bad data -- it is a FALSE
NON-GREEN**, and on Monday that reads exactly like *"the pipeline failed D1's acceptance."*
**The fail-closed property that makes the fix safe is the same property that makes an unexercised
deploy dangerous on an acceptance day.** The publisher runs daily including weekends
(`cron(50 13 * * ? *)`, 6 weekend run-days of 22 measured), so today's 13:50Z fire exercises it on a
day nothing rides on, with Sunday as a second window.

## BOUNDS

- **TERRAFORM ONLY** via `.tools/safe-apply.sh`. Never `aws lambda update-function-code` (NEVER#9).
- **ACCEPTANCE IS TWO RUNGS AND THE DEPLOY IS ONLY THE FIRST** (issuer, 15025):
  - **(a)** EXTRACTED PACKAGE: `artifact_types.json` PRESENT in the member list, `RULED_TYPES` -> 0,
    with a negative control. Not a moved `CodeSha256`, not a plan, not a filename.
  - **(b)** EXERCISED: today's 13:50Z scheduled fire completes and reports completeness CORRECTLY.
  - **(a) WITHOUT (b) IS NOT DONE.** This entry does not close on (a).
- **IF THE WINDOW SLIPS PAST 13:50Z TODAY: DO NOT DEPLOY ANYWAY.** Take Sunday -- a deploy after the
  day's only scheduled fire buys the risk without the exercise.
- **IF TODAY'S FIRE REPORTS `all_present: false`** that is the signal doing its job: diagnose, and
  revert before Monday if unresolved. Sunday's fire is the retry.

## EXPECTED SIGNAL THAT WILL LOOK LIKE A REGRESSION AND IS NOT

`3.0.0_SA_CVO~Z` (15031), measured: `scope_note` is NOT in `category-views`'
`process_time_exemptions` and must not be. The producer's scope_note change alters the body, so
today's same-`as_of` gold run logs **`conflict`** on category-views where it previously logged
`unchanged`. **That is the guard detecting a real business-content change -- the discriminating power
the B0 entry exists to provide.** Nobody relands to clear it and nobody adds `scope_note` to the
exemption list to silence it.

## ROLLBACK

Re-point to VersionId `9nqnBHz63Fu8qvo4Z.gnfFsL_jtWidyS` and `safe-apply`. The bucket is versioned
and the pre-state hash is recorded above, so the prior state is fully specified. **The Lambda is
pinned to a specific object version (`yang-lambda/main.tf:38`), so rollback is a version re-point and
cannot land partially.**

## CLOSE-OUT

_(rung (a) recorded at apply; rung (b) after the 13:50Z fire. This entry stays OPEN until both.)_
