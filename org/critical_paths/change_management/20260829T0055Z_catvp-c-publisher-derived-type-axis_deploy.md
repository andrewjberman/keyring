# DEPLOY LEDGER -- CATVP-c publisher: derived artifact-type axis

> ⛔ **THIS FILE IS THE NARRATIVE DETAIL. THE PRIMARY, GATE-VISIBLE RECORD IS THE SENTINEL.**
> Added 2026-08-29T01:15Z on `2.0.0_SA_COO~Z`'s 15074 -- a hand-authored markdown ledger carries no
> `.open_deploys/*.json` sentinel, so it is **structurally invisible to NEVER#6's PRIMARY scan** and
> is caught only by the secondary markdown sweep that exists because this class happened before.
> **That mattered here specifically**: this deploy is half-complete BY DESIGN for ~12.6h, which is
> exactly the state the gate exists to make visible, and the window outlasts sessions.
> ```
>   PRIMARY   .open_deploys/catvp-c-publisher-derived-type-axis.json          (sentinel, gate-visible)
>   PRIMARY   change_management/20260829T0114Z_catvp-c-publisher-derived-type-axis_deploy_completion.md
>             (tool-written; REGENERATED on every leg close -- never hand-edit it)
>   THIS FILE narrative detail: pre-state, the window argument, the expected-conflict note, rollback
>   JOIN KEY  the slug `catvp-c-publisher-derived-type-axis` appears in all three
> ```
> **If this file and the sentinel ever disagree, THE SENTINEL IS RIGHT** -- it is what the gate reads
> and what `close-leg` updates. L1 is CLOSED in it with the full rung-(a) proof; **L2 is OPEN and is
> the 13:50Z fire.**

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

**BUILT AT `dc14d649bb3e8e7853ed9f648b08f7ca7017b7c8`**, which is THIS LEDGER'S OWN OPENING COMMIT --
opening the entry advanced HEAD, so the build pinned the ledger commit rather than the revert named
below. **Not a drift and not a substitution: verified byte-identical across the two pins for all
three packaged inputs** (`lambda_function.py`, `mdpf_gold_consolidator.py`, `partner_roster.json`),
and `dc14d649bb` changes exactly one file -- this ledger. Recorded because `BUILD_MANIFEST` stamps
the real pin, and a ledger naming a different one would read as a discrepancy to the next auditor.

`5b58c5bfced4acee9442b08a5824b3f073176fb8` -- the substantive parent, and it is
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

## RUNG (a) -- DEPLOYED AND VERIFIED AT THE EXTRACTED PACKAGE. 2026-08-29T01:01Z.

### The act

```
  ARTIFACT UPLOAD  s3://opal-313476888478-lambda-artifacts/opal-assets/
                   opal-assets-mdpf-portal-publisher.zip
    new VersionId  ZLaQC2nGuQ2hP72JpdTA4RWfciYhFoql   53,286 B   00:58:31Z
    metadata content-sha256 ed7e74b91d47ac6c... -- READ BACK and matches the body
  PLAN (targeted)  0 to add, 1 to change, 0 to destroy
                   s3_object_version 9nqnBHz63F... -> ZLaQC2nGuQ...
                   source_code_hash  f613200ac9... -> ed7e74b91d...
                   28 attributes and 4 blocks unchanged
  APPLY  .tools/safe-apply.sh (NEVER#9 -- no bare apply, no update-function-code)
    HALT-GATE FIRED AND BLOCKED on 2 pending messages. BOTH READ IN FULL before HALT_ACK=1:
      4349 / 4355, both 2026-08-21, both `2.0.0_SA_COO~Z`, both WITHDRAWALS of D7_TICKETING
      apply TOs, both stating in terms "nothing to approve, decline or hand back; neither is
      a gate". Neither STOP-class, neither touching MDPF. Acked on the content, not the age.
    RESULT  Apply complete! Resources: 0 added, 1 changed, 0 destroyed. (6s)
```

### Rung (a) evidence -- at the EXTRACTED PACKAGE, never a moved CodeSha256

```
  live CodeSha256   7X50uR1HrGyeEHZ4FWyHBNwTxt/XXJq5GNmR/eFfWE0=
  LastModified      2026-08-29T01:01:04Z
  BYTE-IDENTITY CHAIN, one hash end to end:
    built ed7e74b91d47ac6c... -> uploaded ed7e74b9... -> DOWNLOADED FROM THE FUNCTION ed7e74b9...
  MEMBERS  [lambda_function.py, partner_roster.json, artifact_types.json, BUILD_MANIFEST.json]
    artifact_types.json  PRESENT  <- the build-generated member; ABSENT pre-deploy
    types: account-distribution, aggregate-aua-timeseries, aum-metrics, category-views
    derived_from  mdpf_gold_consolidator.py @dc14d649bb ; hash tie to BUILD_MANIFEST TRUE
  NEGATIVE CONTROL  zzz_no_such_token_9999 -> 0 occurrences (the matcher can return zero)
```

⚠ **ONE CRITERION IS MET IN SUBSTANCE AND NOT ON ITS LITERAL WORDING, AND I AM NOT ROUNDING IT.**
The issuer's (a) says `RULED_TYPES -> 0`. **Measured on the deployed bytes: 1 OCCURRENCE.** It is
line 93, a COMMENT (*"# This was a literal 3-tuple, RULED_TYPES, frozen at the 2026-08-06 capability
snapshot"*). Classified two ways rather than asserted:
```
  every occurrence printed and labelled  ->  1, COMMENT
  ast.parse module-level assignments containing RULED_TYPES  ->  []   THE SYMBOL IS ABSENT
  ast has ARTIFACT_TYPES_MEMBER assignment                   ->  True
```
**The literal frame is gone; a token census cannot say that and an AST read can.** Reported as 1
occurrence with its unit and its classification, per `3.0.0_SA_CVO~Z` 14905 -- a bare `0` here would
have been the more convenient number and the less true one.

## RUNG (b) -- OUTSTANDING. THIS ENTRY REMAINS OPEN.

**The 13:50Z scheduled fire on 2026-08-29 must complete and report completeness CORRECTLY.**
(a) without (b) is NOT done -- issuer, 15025.

```
  EXPECT  category-views INSIDE `expected`; missing_pairs [];
          unexpected_pairs NO LONGER listing the four category-views pairs
  IF all_present:false  -> the signal has done its job. Diagnose; revert before Monday if
          unresolved. ROLLBACK = re-point to VersionId 9nqnBHz63Fu8qvo4Z.gnfFsL_jtWidyS and
          safe-apply. Sunday's 13:50Z fire is the retry.
  UNRELATED AND EXPECTED  today's gold run logs `conflict` on category-views where it logged
          `unchanged` -- scope_note is correctly NOT exempt (3.0.0_SA_CVO~Z 15031). Not a
          regression, not this deploy's doing, and nobody relands to clear it.
```
**Any seat may close this entry by reading the 13:50Z manifest against the EXPECT block above.**
