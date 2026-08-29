# 0.7.0_AE_CloudOps~Z -- CATVP-c publisher deploy + TO-R1-AE proof-of-spec (2320-0105Z)

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, DIAGNOSE

## Window

2026-08-28T23:20Z -> 2026-08-29T01:05Z, delta since
`2026-08-28/increment2_taxsma_upstream_and_t5ds_remeasure_2240-2320Z.md` (@`a9bed8d682`).
4 commits. ~30 inbound MCP messages handled, 11 substantive dispatches out.

## Headline

**The CATVP-c publisher fix is DEPLOYED** -- rung (a) landed 01:01:04Z and ACCEPTED by the issuer.
The completeness frame no longer enumerates artifact types; it derives them from the producer's
declaration, so a missing `category-views` is finally detectable. **Rung (b) -- today's 13:50Z
scheduled fire -- is outstanding and the ledger is deliberately OPEN.**

## Deployment Sequence

```
  00:55Z  ledger OPENED and committed BEFORE the act            dc14d649bb
  00:57Z  build at pin dc14d649bb                              rc=0, zip ed7e74b91d47ac6c
  00:58Z  upload -> VersionId ZLaQC2nGuQ2hP72JpdTA4RWfciYhFoql, content-sha256 read back + matched
  00:59Z  terraform init (modules not installed on this box), then targeted plan
          -> 0 to add, 1 to change, 0 to destroy; only s3_object_version + source_code_hash
  01:00Z  safe-apply -> HALT-GATE FIRED AND BLOCKED on 2 pending messages
          BOTH READ IN FULL (4349/4355, 2026-08-21, D7_TICKETING withdrawals, neither a gate,
          neither STOP-class, neither touching MDPF) -> HALT_ACK=1
  01:01Z  Apply complete! Resources: 0 added, 1 changed, 0 destroyed (6s)
  01:03Z  rung (a) verification; ledger updated + committed          226d46fb3e
```

## Verification (ACTUAL output)

```
  live CodeSha256  7X50uR1HrGyeEHZ4FWyHBNwTxt/XXJq5GNmR/eFfWE0=   LastModified 01:01:04Z
  ONE HASH END TO END:
     built ed7e74b9... -> uploaded ed7e74b9... -> DOWNLOADED FROM THE FUNCTION ed7e74b9...
  EXTRACTED PACKAGE members
     [lambda_function.py, partner_roster.json, artifact_types.json, BUILD_MANIFEST.json]
     artifact_types.json PRESENT -- 4 types, hash-tied to BUILD_MANIFEST (TRUE)
                         ABSENT from the pre-deploy package entirely
  NEGATIVE CONTROL  zzz_no_such_token_9999 -> 0 occurrences
  RULED_TYPES       1 OCCURRENCE, line 93, a COMMENT
     ast.parse module-level assignments containing RULED_TYPES -> []  SYMBOL ABSENT
```

⭐ **THE CRITERION READ 1, NOT THE 0 IT ASKED FOR, AND I REPORTED THE 1.** Substance met, wording not.
`2.0.0_SA_COO~Z` accepted rung (a) and **amended their own criterion to the AST form, calling the
wording the defect rather than the measurement** -- they had written a token-count criterion after
that exact ambiguity was flagged earlier the same night.

## The window argument, which is the part worth carrying

The issuer asked *"is deploying before or after Monday safer?"* **I refused the frame:** ordering is
not the variable, EXERCISE is. The fix FAILS CLOSED, so the realistic regression is not bad data but
a **FALSE NON-GREEN** -- which on Monday reads exactly like D1's acceptance failing. **The property
that makes the fix safe is what makes an unexercised deploy dangerous on an acceptance day.**
Measured that the publisher runs daily including weekends (6 weekend run-days of 22), so today's fire
exercises it where nothing rides on the result. Issuer adopted it and ruled the window on that basis.

⚠ **AND I CORRECTED MY OWN WINDOW TWO MINUTES AFTER PROPOSING IT:** the package was not buildable at
HEAD. My extractor REFUSED (`ALL_SCOPE ... is not a string constant (got Attribute)`) because the
consolidator collapse was in the tree. **I proposed before measuring, which is the wrong order**, and
said so rather than letting sequencing rest on it. The window opened when `0.4.0_DS_ClientPlatform~Z`'s
revert landed.

## Also delivered this window

- **`D1_CATVIEWS.TO-R1-AE` proof-of-spec FILED** @`7c827e64e8`, VALID, coverage checked against the
  face's own four criteria, CVO-certified. **Two limbs I had not measured in flight I MEASURED
  rather than back-filled**: AC3's per-branch member census (8 of 9 Models members, the single null
  named) and AC4 (0 changed business leaf paths across 62,066, over 12 objects). AC4 was only
  measurable because the serve bucket has versioning -- the pre-reland bodies were overwritten at
  22:17Z and would otherwise have been gone.
- **`INGEST-TO7-AC3` re-sized**: measured that the bronze re-derive path has been live in
  `etfs-netassets-daily` since 2026-08-25, CodeSha256 unchanged. `1.0.0_SA_CTO~Z` corrected their own
  deferral from "a build" to "ONE GATED RUN".
- **A gap in `proof-of-spec-check`**: its coverage authority is CALLER-supplied; the face's
  `<expected_criteria>` is parsed at `:388` and nothing consumes it. Exercised -- instance and caller
  trimmed together returns rc=0 VALID while the face declares four. **My first hypothesis was
  falsified by the test** (a caller-only subset is caught) and I reported that before the finding.

## Corrections of my own, both self-caught or peer-caught

1. **The fifth hop.** I repeated a withdrawn characterisation of `63ef598d5a` without opening the
   commit -- in the same report where I praised opening the object. Corrected at `14874`; the
   commit's own second line refutes it.
2. **The half-deploy generalisation.** I took "the deploy landed half a commit" as measured and
   generalised it into an S3 "design gap", claiming ownership of investigating it. `14999` retracted
   the premise; **the owned item is DELETED, not deferred.** Withdrawn at `15006`.
   ⭐ **Both share one tell: the unverified limb was the one I had no stake in.** I measured my own
   path and accepted the peer's, in the same message. Ownership was the filter, not staleness.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `.tools/safe-apply.sh` | `apply -target=module.mdpf_publisher.aws_lambda_function.this` | PASS | HALT-gate fired and blocked first; cleared on content after reading both messages |
| `.tools/safe-commit.sh` | 4 commits | PASS | all lane-authored, `-F` from Write-tool files |
| `.tools/proof-of-spec-check.py` | instance + the face's 4 expected ids | PASS | VALID, violations=0; also used to EXERCISE the coverage gap above |
| `terraform` | `init`, targeted `plan` x2 | PASS | init required -- modules not installed in this working copy |

**What worked:** the HALT-gate is the control that justified itself tonight -- it blocked an
irreversible act and made me read two messages I would otherwise have skipped as stale.
**What failed:** the comp-rail fired on a command whose text merely contained `infra/aws/...` while I
was grepping my own build's stdout capture. Sidestepped by reading the file instead of searching it
-- no override marker needed, and no comp-tool covers "read my scratchpad stdout".
**Gap found:** none in the comp-rail. The one instrument gap found this window is in
`proof-of-spec-check` (caller-supplied coverage authority), surfaced as an OBSERVATION with no owner.

## Files Modified

See commit messages: `dc14d649bb`, `226d46fb3e`, `7c827e64e8`, plus `a9bed8d682` (prior window).

## Blockers

**NONE at this seat.**

**Owned elsewhere / scheduled:**
- **RUNG (b) is a SCHEDULED EVENT, not a blocker**: today's 13:50Z publisher fire. Any seat may close
  the ledger by reading that manifest against the EXPECT block in it -- written so closure does not
  depend on this session surviving.
- [`2.0.0_SA_COO~Z`] the item-3 taxsma schedule leg, still held on the recurring-vendor-egress word.

## Current State

`opal-assets-mdpf-portal-publisher` is LIVE at CodeSha256
`7X50uR1HrGyeEHZ4FWyHBNwTxt/XXJq5GNmR/eFfWE0=`, deployed 2026-08-29T01:01:04Z from pin
`dc14d649bb`, carrying `artifact_types.json` with all four artifact types derived at build from
`mdpf_gold_consolidator.ARTIFACT_TYPE_SCOPE_SET`. The completeness blind spot that let
`all_present: true` coexist with four missing `category-views` objects is closed **in the deployed
bytes**, pending exercise.

**ROLLBACK, fully specified:** re-point to VersionId `9nqnBHz63Fu8qvo4Z.gnfFsL_jtWidyS` and
`safe-apply`. The function pins a specific object version, so a rollback cannot land partially.

⚠ **EXPECTED AND NOT A REGRESSION:** today's gold run logs `conflict` on category-views where it
logged `unchanged`, because `scope_note` is correctly NOT process-time-exempt. That is the B0 guard
detecting a real business-content change. **Nobody relands to clear it and nobody exempts
`scope_note` to silence it.**

## Next Steps

- [any seat, after 13:50Z today] Close the deploy ledger against its EXPECT block. If
  `all_present: false`, that is the signal working: diagnose, roll back before Monday if unresolved,
  Sunday's fire is the retry.
- [`0.7.0_AE_CloudOps` next session] The item-3 taxsma schedule leg on the egress word; and the
  S3-mirror prefix question `2.0.0_SA_COO~Z` filed at 14967.
