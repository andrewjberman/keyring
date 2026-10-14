# TO IRPT_ANLREQ.TO-AR-y-323.release30-build-ycharts-generate -- BUILD the Lambda `irpt-ycharts-generate` package for the intake release (AR-y-318 and AR-y-319) and compare it with the live package; nothing is uploaded or applied

<to_id>IRPT_ANLREQ.TO-AR-y-323</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~131</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>ZI</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the class the infrastructure `<paths>` imply; the worker builds only: nothing is uploaded, applied or invoked)
**Decomp cell:** `AR-y-323` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (hop 1, the owned-input analysis of a partner advisor) | **depends_on:** `AR-y-318` (merged `ece60105e1`), `AR-y-319` (merged `1176eb009a`)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~131`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-131` (branch `wk-IRPT_ANLREQ-131`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~131 <0.9.0_WK_IRPT_ANLREQ~131@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W131-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet` fixture): never commit either to the WORKSPACE repository. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. No live call EXCEPT the read-only AWS reads the steps name (`get-function`, `get-function-configuration`, `list-object-versions`, `head-object`, a download of the live zip or of a version of the artifact key, through the `.tools/aws` shim), and a `git fetch` of remote-tracking refs; no push, no deploy, no upload, no apply, no invoke, no Terraform. No non-ASCII in what you add. Scratch outside the product tree (you may not delete recursively; say where it is).
- **THE BUILD GUARD (a past incident: row D2-S69):** every build is `BUILD_ONLY=1`, and before the first build at a base commit you run `git show <commit>:infra/aws/lambda/ci/build-and-upload.sh | grep -c BUILD_ONLY`: it must print at least 1 (the trunk builder prints 8). At a commit older than the guard the script UPLOADS. Print the count in your record. Your run must never reach `aws s3 cp`. The script writes ONE fixed temp path per function: use a PRIVATE `TMPDIR` (a new empty folder outside the repository) for every build and copy the artifact out at once. Stage every artifact under `C:/dev/irpt-release-r30/` (create it; it is outside the repository; another worker builds the other package there at the same time: touch only your own file names); never delete anything you did not make.

### THE CELL (`AR-y-323`, inlined) -- BUILD ONLY. Nothing is uploaded, applied, deployed or invoked.

*The intake release moves THREE members of Lambda `irpt-ycharts-generate` package, each equal to the trunk blob: `ycharts/generate/composition_admission.py` (AR-y-318: `validate` names the failing step and error class in one log line and still raises the same public code), `intake/uploads.py` (AR-y-318: `load_input_owner` raises the declared typed `InputUnavailable` instead of a bare `PermissionError`) and `_scope/interactive_access.py` (AR-y-319: `prospect_owner()` omits `home_firm_id` unless the class is OPAL_GLOBAL, so a partner advisor's frozen composition passes the schema, row D2-S97). Live now (release 29, 2026-10-14T13:03:45Z): CodeSha256 `5TRFZf6Grgd9V9jWBVu2QDPRVbgfWBjsuuw8rtf8hRA=`, 635191 bytes, 106 members, S3 `investor-reporting/irpt-ycharts-generate.zip` latest VersionId `sf9zrBdAUPuzO3qgCpk52_iVf6EFle_C`; the Lambda is released by Terraform (`s3_object_version`), never by a code update call, and the applier does that, not you.*

Read first: the release-29 build record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~124/r39/IRPT_YCHARTS_GENERATE_BUILD.json` (the base, the recorded inputs, the build command, the guard counts and the control that reproduced the package that was live), the applier's closing report `org/tier2_senior/0.7.0_AE_CloudOps~AQ2/deliverables/irpt_anlreq_r29/G_AFTER_R29c.txt` (what is live now, with the VersionId), and the cells' records `.../0.9.0_WK_IRPT_ANLREQ~128/r40/COMPOSITION_CAUSE.json` and `.../0.9.0_WK_IRPT_ANLREQ~129/r40/OWNER_FIX.json`. The release moves ONLY those three members; if the comparison with the live package shows ANY other differing member, STOP the build, file a BLOCKING row naming it, and record what you have.

1. **The live read.** `.tools/aws lambda get-function --function-name irpt-ycharts-generate --query Configuration.CodeSha256 --output text` and `Code.Location`; download the zip into a NEW EMPTY folder under your `.scratch/r40/` (write the URL to a file and read it from Python run with `-I`), check its sha256 base64 equals the CodeSha256, and take `member_manifest` = member name -> sha256 for every file member. `list-object-versions` for the key `investor-reporting/irpt-ycharts-generate.zip` in bucket `opal-313476888478-lambda-artifacts` (prefix exact; read the listing as a WHOLE JSON, never a paged `--query length()`; print the latest VersionId and the version count as the denominator): the latest VersionId is the rollback target. Print each next to the release-29 applier's report (CodeSha256 `5TRFZf6Grgd9V9jWBVu2QDPRVbgfWBjsuuw8rtf8hRA=`, 635191 bytes, 106 members, VersionId `sf9zrBdAUPuzO3qgCpk52_iVf6EFle_C`, 55 versions); a difference is a finding (someone released since): say what changed and carry on only if the change is already on the trunk.
2. **The no-move control.** Reproduce the live package: its base and inputs are in the release-29 build record (`release_input`, `base_determination`: base `0c0ae5a8f5` plus the release-28 input diff plus the release-29 map diff) and in the applier's close commit (`0d92e7d7c7`, which moved the TRUNK map). Rebuild the live package in a throwaway worktree OUTSIDE the product tree (guard count printed; `git -c core.longpaths=true worktree add --detach`): `TMPDIR=<private> BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-ycharts-generate`. Its CodeSha256 must equal the live one and `differs_from_live` must be `[]`. If the live package cannot be reproduced, name the members that differ and STOP with a BLOCKING row. Say, from the map at the trunk HEAD, whether the trunk map now reproduces the live package by itself (the applier re-pinned it); if it does, the release input is simpler.
3. **The release input.** Check out the trunk HEAD in a throwaway worktree (state its full sha; it must contain `1176eb009a`). The three members must equal the trunk blobs (print both sha256). Make any map edit ONLY in a second throwaway worktree (never the trunk's map or recipe): move the three members' pins and sha256 in the `irpt-ycharts-generate` block, nothing else; save `git diff` as `r40/<name>.diff` in your deliverable folder and print its `git hash-object`.
4. **Build the release.** `BUILD_ONLY=1`, same command, private TMPDIR, twice (byte-identical). Stage the zip as `C:/dev/irpt-release-r30/irpt-ycharts-generate-r30.zip`. Record `artifact` {`path`, `sha256` (hex of the zip), `bytes`, `code_sha256_base64`}. The builder's import-closure check must pass (print it).
5. **Compare with the LIVE package, member by member.** `delta_vs_live` = members whose sha256 differ; `only_in_live`; `only_in_release`. EXPECTED: EXACTLY `["composition_admission.py", "interactive_access.py", "uploads.py"]`, each equal to its trunk blob, nothing only in live, nothing only in the release (106 members). Anything else: BLOCKING row, do not widen.
6. **Tests.** From the release-faithful test trees of worker 124's method (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~124/r39/`: the builder's staging replayed, the cell test files copied from trunk), run: `_scope/tests/test_ordinary_viewer.py` (43 expected) and `test_ordinary_owner_composition.py`, `intake/tests/` whole (including `test_load_input_owner_typed.py`), `ycharts/generate/tests/` whole with `--continue-on-collection-errors` (including `test_composition_refusal_cause.py` and `test_ordinary_owner_legacy_row.py`). The failing test ids MUST be a subset of the 108 rows of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~124/r39/failures_explained.json` (print the set difference; ANY failing id outside the set is a BLOCKING row). Report `named_tests`, `passed`, `failed`, `skipped`, `denominator`.
7. **Write `r40/IRPT_YCHARTS_GENERATE_BUILD.json`:** `live_read`, `guard_counts`, `no_move_control` {`code_sha256`, `differs_from_live`}, `release_input` (the diff path and hash, the members moved with old and new sha256), `artifact`, `delta_vs_live`, `only_in_live`, `only_in_release`, `rollback` (the S3 latest VersionId and sha256 of the key, read in step 1), `tests`, `claim`, `not_read`.
8. **In your report:** the live read in one line, the control (equal or not), the delta (members), the artifact path and sha256, the tests and the failing-id set difference.

### ACCEPTANCE

<criterion id="AR323-y-AC1" cell_refs="AR-y-323"><invocation>python C:/dev/wk-irpt-anlreq-131/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y323-build --root C:/dev/wk-irpt-anlreq-131</invocation><expect>Y323-BUILD-OK</expect></criterion>
`AR323-y-AC1`: the record carries the live read, a no-move control equal to the live CodeSha256, a staged release zip whose sha256 the checker recomputes, a delta against the live package of exactly composition_admission.py, interactive_access.py and uploads.py (nothing added or removed), passing tests with the failing ids inside the explained set, and the rollback VersionId.

<criterion id="AR323-y-AC2J" cell_refs="AR-y-323" judgment="true"/>
`AR323-y-AC2J` (judgment, graded at L9, never by you): the live package was read from AWS in this run and not taken from a record, the guard count was printed before each build, both builds were BUILD_ONLY with a private TMPDIR, the delta is exactly the three members, and nothing was uploaded or applied.

<expected_criteria>AR323-y-AC1 AR323-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~131/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-323</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~131/IRPT_ANLREQ.TO-AR-y-323.release30-build-ycharts-generate.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-323`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR323-y-AC1,AR323-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- an artifact staged outside the product tree, throwaway worktrees outside the repository, and read-only live AWS reads; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no change.
comp-adversary: RUN -- by reading the release-29 build record of this package, the applier's closing report, and rows W123-S1, W124-S3, W125-S1 and D2-S69 against the cell; the lens: a control that reproduces a stale package instead of the one live now, a map record taken for the live state, a build at a commit without the guard that uploads, a member that moves that no cell changed. The order requires the live read in the run, the guard count before each build, the member-by-member comparison with the live package and the staged artifact re-hashed by the checker. NOT seen: the live users and partner rows, the portal.
</preflight>

---

## RECORD FACE

- Cut on the merged cells `AR-y-318` and `AR-y-319` for the intake release pair (the issuer's, after the two builds), workstream `ZI` of round 40. Base: `AR323-y-AC1` FAIL as expected (`y323-build` prints `Y323-BUILD-FAIL`: no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.
