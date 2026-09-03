# Deploy Completion Record
**Date opened:** 2026-09-03T19:46:01.572264+00:00
**Status:** OPEN
**Deploy:** NFRA_OPSEC202609.TO-OP-S-1 limb 2a (Z-S62 ruling): extract the two-slot origin-secret read from opal-portal-authorizer/index.mjs into a shared module so the REST authorizer can REUSE it rather than hold a second copy. A PURE MOVE on index.mjs; bounds widened on the record for this Lambda, extraction only
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | the extracted module + index.mjs importing it + lambda-source-map.json files-array addition, committed under 0.7.0_AE_CloudOps~Z. PURE MOVE PROOF: index.mjs's diff is ONLY the import line and the moved code (three functions and the five declarations they exclusively own); any other line is a STOP and a row | commit hash + the line-by-line diff accounting |  | OPEN |
| L2 | verify | THE MANIFEST CATCH, verified before the build: lambda-source-map.json:633 declared files:[index.mjs] ONLY. A module not in that array is not packaged, and the deployed index.mjs would MODULE_NOT_FOUND at cold start on EVERY invocation of the authorizer guarding 69 of 72 routes. The files array must list both source files before any build | the manifest entry quoted before and after | THE MANIFEST CATCH, closed BEFORE any build. BEFORE: lambda-source-map.json:633 declared for opal-portal-authorizer a files array of exactly ONE entry, index.mjs. AFTER: the array lists index.mjs AND originVerify.mjs; the edit asserted uniqueness (exactly 1 textual match) before writing and the file re-parses as JSON. WHY IT MATTERS AND WHAT IT PREVENTED: the build packages only what this array names. A pure move that put the two-slot read in a new module without this edit would have shipped a zip whose index.mjs imports a file that is not in it -- MODULE_NOT_FOUND at cold start, on EVERY invocation, on the authorizer that currently guards 69 of 72 routes on the HTTP API including the nine TO-OP-S-2 attached an hour ago. That is a TOTAL OUTAGE produced by a refactor that reads as clean in every source diff, and the manifest is the only surface on which it is visible beforehand. The new module carries a WARN header saying so, so the next person extracting into this Lambda meets the rule at the file rather than in a ledger. ALSO OBSERVED AND NOT YET REMEDIED (separate from this limb): the same entry's last_deployed_commit 5585e9c6b4 and last_deployed_at 2026-05-14T22:26:21Z are ALREADY STALE -- TO-OP-S-3 redeployed this Lambda on 2026-09-03 and the manifest still names a May deploy, so the drift predates limb 2a. | CLOSED 20260903T195808Z |
| L3 | activation | build the nodejs artifact and deploy through TERRAFORM ONLY (aws_lambda_function.portal_authorizer in portal-auth/lambdas.tf; never update-function-code) -- ROLLBACK NAMED BEFORE THE DEPLOY: restore index.mjs from git, delete the module, restore the manifest files array, rebuild, re-apply; the pre-change live CodeSha256 is RvHb6Lj55WjOKCvBAkxQvKIXEEl5jdZfhyT1AY6ZEf4= | apply output + the new CodeSha256 |  | OPEN |
| L4 | verify | THE OPERATIONAL PIN updated in the same commit as the deploy: lambda-source-map.json artifact_sha256 set to the NEW value. This carrier is consumed by the next build comparison, so it asserts the PRESENT and must match; it is treated OPPOSITELY to the filed-proof pin, which is a record of a vintage and gets a supersession note instead of an edit | the manifest's before and after values |  | OPEN |
| L5 | verify | THE NINE DATA ROUTES RE-PROBED as an acceptance criterion on TO-OP-S-2's own discriminator -- a valid fixture login 403 at the direct execute-api address and 200 through CloudFront, plus the anonymous pair. A regression is a ROLLBACK FIRST, then a row | the captured invocations and responses |  | OPEN |
| L6 | verify | CodeSha256 supersession recorded in TO-OP-S-3's instance at S3-AC3 with BOTH values carrying an ISO vintage; re-plan 0-diff on portal-auth; push state MEASURED by ls-remote + is-ancestor with a positive control | the amended row + plan + ls-remote |  | OPEN |

## Log

- 20260903T194601Z OPENED by 0.7.0_AE_CloudOps~Z with 6 leg(s)
- 20260903T195808Z LEG L2 closed: THE MANIFEST CATCH, closed BEFORE any build. BEFORE: lambda-source-map.json:633 declared for opal-portal-authorizer a fi
