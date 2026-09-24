# CVO CUTOVER REVIEW -- `opal-amgt-scoped-api` no-span HOLD repair

**Reviewer** `3.0.0_SA_CVO~Z`. **2026-09-23 ~21:2xZ.** The third control, after the CTO+COO
never-widen pair. **This review is IN ADDITION to that pair and never in place of it.**

## VERDICT: **PASS on the pre-deploy controls, subject to C1-C5. The end-to-end row stands NOT_EVALUATED.**

⛔ **THIS REVIEW DOES NOT AUTHORISE, SCHEDULE OR PERFORM THE DEPLOY**, and it lifts no deploy gate.
**C1 is a BLOCKING condition: it is not satisfied today and the act must not proceed until it is.**

| control | verdict |
|---|---|
| Pair complete, both halves on file | **PASS** |
| Artifact identity, resolved by CONTENT | **PASS** |
| Live baseline undrifted | **PASS** (at 21:2xZ) |
| Blast radius + both branches + writer count | **PASS** |
| Replay reconciliation | **PASS** |
| Coverage of the served population | **PASS** |
| Deploy mechanism named | ⛔ **FAIL -- C1** |
| Artifact durability | ⚠ **C2** |
| Post-deploy acceptance battery | **NOT_EVALUATED -- C4** |

## 1. WHAT THIS SEAT MEASURED ITSELF, ON INSTRUMENTS THAT DIFFER FROM THE PRODUCER'S

The pair's evidence was produced by replay and AST review in a working tree. **This seat did not
re-run that method.** It measured the live planes instead -- the AWS Lambda API, live S3, and the
artifact bytes on disk -- so the confirmations below are corroboration rather than repetition.

**LIVE FUNCTION** (`lambda get-function-configuration`, 21:2xZ):

| field | live | bound by the pair | match |
|---|---|---|---|
| `CodeSha256` | `r93CxQqrk8k8h2Q8KO4Iicn3pk8kyF4SFo47a9Cca5w=` | same | **YES** |
| `RevisionId` | `d906e911-aed5-4e21-afcd-0b9a6dcdbdc7` | same | **YES** |
| `LastModified` | `2026-09-22T10:07:44Z` | same | **YES** |
| `CodeSize` | `807553` | -- | consistent |

**THE BASELINE HAS NOT DRIFTED.** The pair's binding is live and valid as measured.

**CANDIDATE ARTIFACT, RESOLVED BY CONTENT** at `C:/tmp/amgt-r-no-span-package-20260923/candidate.zip`:
sha256 `0c44108821fe52850c77b119490039453b082c3639fae6dbf58de054b1397a55` -- **byte-exact to the hash
amendment 1 binds** -- CodeSha256 `DEQQiCH+UoUMd7EZSQA5RTsILDY5+ubb9Y3gVLE5elU=`, **197 members**,
807,904 bytes. The sibling `rollback.zip` hashes to the live baseline, corroborating it independently.

**REPLAY, RECONCILED FROM THE PER-CASE ROWS rather than read off the summary:** 12 cases,
**210 served + 179 held = 389**, `served_no_span` **0**, `held_on_object` **0**, `source_unchanged`
true on all 12, `anchored_siblings_exact` true on all 12. The summary and the parts agree.

**COVERAGE, ON THE LIVE PLANE** -- the one claim the replay could not make about itself. The deployed
function carries **no drafting overrides** (`Environment.Variables` is exactly
`HARVEST_METRICS_TABLE` + `HARVEST_ARTICLES_TABLE`), so `DRAFTING_BUCKET` and `DRAFTING_PREFIX` fall
through to their defaults `opal-data-harvest` and `drafting/v1/` -- **the same prefix this seat then
censused.** That prefix holds **exactly 12 objects**, and the set of security keys is **IDENTICAL** to
the replay's 12 cases: **zero uncovered, zero stale**. The CTO half's *"the complete set, measured"*
is confirmed on the deployed plane, not merely asserted.

## 2. ⛔ C1 -- BLOCKING. NEITHER HALF NAMES THE DEPLOY MECHANISM, AND THE OBVIOUS ROUTE IS BOTH A `NEVER` VIOLATION AND SELF-REVERTING

**`opal-amgt-scoped-api` is TERRAFORM-MANAGED.**
`infra/aws/terraform/harvest/scoped-amgt-api.tf:256-259` declares it through `modules/yang-lambda`
with `artifact_key = "research/opal-amgt-scoped-api.zip"`, and that file states the contract in its
own words (`:44-46`): *"modules/yang-lambda reads that object's content-sha256 as source_code_hash, so
an apply BEFORE the upload will fail. Build and upload first, then apply."*

**So the artifact of record is the S3 object, not the function's inline code.** Measured:

- `s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip` -- ContentLength
  **807,553**, ETag `324d0d55f9828d13de4a1f61a872c0e1`.
- `rollback.zip` MD5 is **the same value**, and a single-part ETag IS the MD5, so **the S3 artifact is
  byte-identical to the currently deployed package.**
- **THERE IS NO DRIFT TODAY:** Terraform's source, the S3 object and the running code all agree at the
  baseline. **This finding is about the FORWARD path, not an existing defect.**

**THE HAZARD.** `aws lambda update-function-code` is forbidden outright by CLAUDE.md -- *"NEVER ...
`aws lambda update-function-code` (Terraform only)"*. Beyond the prohibition, applying the candidate
directly to the function **without updating the S3 key** leaves the deployed code and Terraform's
`source_code_hash` disagreeing. ⛔ **The next `terraform apply` touching the harvest stack -- for any
unrelated reason -- then silently restores the S3 artifact, which is the DEFECTIVE package, re-serving
the 179 held sentences.**

⚠ **That is precisely the outcome amendment 2 was written to prevent** -- *"a rollback that restores a
known contract violation is not a rollback, it is a SECOND DEPLOYMENT OF THE DEFECT"* -- reached here
not by a deliberate rollback but as a **side effect of someone else's apply, with no alarm and nobody
deciding anything.** Amendment 2 closed the deliberate path and this one stayed open.

**WHAT CLEARS C1.** The cutover is recorded, before it runs, as: **(i)** upload `candidate.zip` to
`research/opal-amgt-scoped-api.zip` -- the key must afterwards hold MD5
`cb90ed8636c79c9dbc29120923349bc5`, 807,904 bytes; **(ii)** `safe-apply` on the harvest stack, never a
bare `terraform apply`; **(iii)** confirm the function's `CodeSha256` reads
`DEQQiCH+UoUMd7EZSQA5RTsILDY5+ubb9Y3gVLE5elU=`. `build-and-upload-scoped-amgt.sh` already exists for
step (i) and should be read before use rather than assumed to match this artifact. **Any route that
changes the function without changing the S3 key is refused by this review.**

## 3. ⚠ C2 -- THE SIGNED ARTIFACT IS NOT DURABLY STORED

`candidate.zip` exists **only** at `C:/tmp/amgt-r-no-span-package-20260923/` on **this device**. It is
not in git, not in the artifact bucket, and no ledger records it. A signature bound to a content hash
is worthless if the content is lost, and `C:/tmp` is a cleanup target.

⭐ **The recovery path exists and is sound, which is why this is C2 and not blocking:**
`prepare_repair_package.py` rebuilds deterministically -- it copies each original `ZipInfo`
(`copy.copy(member)`), preserving member order, timestamps and compression, so a rebuild reproduces
the bytes. ⚠ **But it is CONDITIONAL:** `:26-27` asserts the downloaded baseline equals the deployed
`CodeSha256`, so **the rebuild reproduces the bound hash only while the baseline is still
`r93CxQ...`.** If the baseline moves and the ZIP is gone, the artifact is unrecoverable and the pair
must be re-signed. **Record the location and the conditional rebuild recipe in the change-management
entry**; step (i) of C1 also discharges this by putting the bytes in S3.

## 4. ⚠ C3 -- AT THE PRE-DEPLOY REMEASURE, `RevisionId` AND `CodeSha256` ARE NOT THE SAME TEST

The COO half correctly requires the deployer to remeasure both immediately before applying. **This
seat's 21:2xZ reading answers a MOMENT, not a standing property, and does not relieve that
obligation.** The two fields differ in what they can see, and the halves do not say which governs:

- **`CodeSha256` changes only on a code change.**
- **`RevisionId` changes on ANY update, including configuration-only** -- env vars, memory, timeout,
  layers.

⛔ **So `CodeSha256` unchanged + `RevisionId` changed means a CONFIGURATION change landed that the pair
never reviewed -- and that is not a nuisance here.** `DRAFTING_BUCKET`, `DRAFTING_PREFIX` and
`DRAFTING_ROOT` are all env-overridable (`scoped_amgt.py:1378-1380`, `:1374`). An override introduced
between now and the deploy would point the function at a different prefix and **silently void the
12-object coverage finding in section 1**, which is the evidence the 210/179/389 rests on.
**RULED: a `RevisionId`-only change is a STOP requiring re-read, not a difference to wave through.**

## 5. C4 -- THE POST-DEPLOY BATTERY, WHICH IS THIS SEAT'S TO GRADE AND STANDS NOT_EVALUATED

The COO half names these as post-deploy obligations and this seat adopts them as the acceptance
battery, with expected values stated so the grading is not a judgement call:

1. **Deployed `CodeSha256` == `DEQQiCH+UoUMd7EZSQA5RTsILDY5+ubb9Y3gVLE5elU=`**, and the S3 key holds
   the candidate bytes (C1 iii).
2. **All 12 served GETs** -- one per security in `drafting/v1/`, the set enumerated in section 1 --
   returning **210 served and 0 no-span served** in aggregate. ⛔ **A subset is not the battery**; the
   12 are named precisely so a partial run cannot read as a pass.
3. **Missing-firm 401**, with the negative control the CTO already exercised: a nonexistent path under
   the same prefix returning the identical 401, showing the 401 fires before path resolution.
4. **Both overlay controls** -- thesis bundle and overlay description fallback, the two production
   consumers the writer census says cross the repaired reader.

⚠ **UNTIL THAT BATTERY RUNS AGAINST THE DEPLOYED FUNCTION, END-TO-END STANDS `NOT_EVALUATED`.** Both
seats stated the limit themselves and this seat agrees rather than treating it as a defect: the replay
is **Windows Python 3.11 with host jsonschema, not the Linux Lambda runtime**, so it proves the LOGIC
and cannot prove the RUNTIME. **An ungraded boundary is never an implied pass and no lane should read
consent into this seat's silence.**

## 6. C5 -- THE LEDGER ENTRY

CLAUDE.md NEVER-2 requires a `org/critical_paths/change_management/` entry **opened at start** and
closed at completion, and an IMAGE-class act names every family pulling a moved tag. This is a Lambda
artifact rather than a container tag, so the tag-sweep clause does not bind; **the entry does.** The
CTO half is itself filed in that directory and declares *"Status: OPEN at signing"*, which covers the
signature; **the entry for the DEPLOY ACT, naming the S3 key and the apply, is still owed by whoever
runs it.** The worktree caveat does not apply -- a non-worker seat deploying in the shared tree means
the shared read IS the population.

## 7. WHAT THIS REVIEW DOES NOT REACH

No retained-object rewrite or re-emission; no source rewrite; no schema change; no vendor call; no S3
delete; no credential, IAM or routing change; no unrelated package refresh. **Raw-D1 posture,
machine-empty print prose, portal rendering of the new counters and human viewing of the served
sentences all remain separate and UNMEASURED**, exactly as both halves state. Nothing here closes the
served-output incident -- the 179 sentences are being served **at this moment**, and the operator's
authenticated Boeing render is diagnostic of reachability, never acceptance.

## 8. ON THE PAIR ITSELF

**Both halves meet the rule's shape**, which this seat checked rather than assumed: each names the
act's blast radius rather than the producer's decision; each covers **both branches** of the producer's
own rule (210 serve / 179 hold) rather than predicting from the input's shape; and **the writer count
is PRINTED** -- N=1 materializer, N=1 response-key writer with 4 call sites, N=2 production consumers
that both cross the repaired reader, N=0 injection callers, over a census with **zero parse failures**,
which is the coverage control that makes an N sayable at all.

⭐ **The rollback correction is the strongest thing in the pair and it is recorded here so it is not
lost:** the original half authorised reverting to the current package, which **is** the defective one,
so the signature would have pre-authorised a second deployment of the known incident -- *the failure
mode the never-widen rule exists to catch, committed inside a never-widen half*. It was found by
`2.0.0_SA_COO~Z` **in the document it was declining to sign.** C1 above is the same class, one plane
further out: the deliberate rollback path is now closed, and the **incidental** one through Terraform
is not.
