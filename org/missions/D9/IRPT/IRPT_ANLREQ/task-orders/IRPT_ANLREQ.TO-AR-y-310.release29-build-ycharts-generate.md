# TO IRPT_ANLREQ.TO-AR-y-310.release29-build-ycharts-generate -- BUILD the irpt-ycharts-generate package for release 29 (the Shares words and the ordinary-viewer authorizer) against the package that is live NOW, and compare it

<to_id>IRPT_ANLREQ.TO-AR-y-310</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~124</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>39</round>
<workstream>ZD</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-310` (`decompositions/IRPT_ANLREQ_DECOMP_R39A_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~124`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-124` (branch `wk-IRPT_ANLREQ-124`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~124 <0.9.0_WK_IRPT_ANLREQ~124@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W124-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call EXCEPT the read-only AWS reads the steps name (`get-function`, `get-function-configuration`, `list-object-versions`, `head-object`, a download of the live zip or of a version of the artifact key, through the `.tools/aws` shim), and a `git fetch` of remote-tracking refs; no push, no deploy, no upload, no apply, no invoke, no Terraform. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

- **THE BUILD GUARD (a past incident: row D2-S69):** every build is `BUILD_ONLY=1`, and before the first build at a base commit you run `git show <commit>:infra/aws/lambda/ci/build-and-upload.sh | grep -c BUILD_ONLY`: it must print at least 1 (the trunk builder prints 8). At a commit older than the guard the script UPLOADS. Print the count in your record. Your run must never reach `aws s3 cp`. The script writes ONE fixed temp path: copy the zip out at once. Stage every artifact under `C:/dev/irpt-release-r29/` (create it; it is outside the repository); never delete anything you did not make; say where scratch copies are.

### THE CELL (`AR-y-310`, inlined) -- BUILD ONLY. Nothing is uploaded, applied, deployed or invoked.

*Leg L3 of release 29: `irpt-ycharts-generate` (the upload door) gets, from the trunk: `intake/uploads.py` (the one new word entry, AR-y-308), `reports/generate_installed.py` (the wiring of the ordinary-viewer authorizer over the two canonical readers, AR-y-306), and ADDS `_scope/ordinary_viewer.py` at the package root as `ordinary_viewer.py` (the module `generate_installed.py` imports lazily; the package does not carry it today). Live now (release 28, 2026-10-14T02:50:16Z): CodeSha256 `reAjAQOVVfD4Wui2u0UfZRt7cr9o6ioFKIwXa+8EVgc=`, 632858 bytes, 105 members, S3 VersionId `edHLV8L0.FETO34.wAag6i7FHBJvfAuW`. This leg is the AUTHORIZATION CHANGE of the release: after it a FIRM_ADVISOR or FIRM_OPERATIONS viewer of a firm with a partner row and a users row naming the firm may upload and request owned-input analysis for its own firm. Check that the new `generate_installed.py` imports nothing the package lacks (the import closure of the three moved/added members against the package) and that `ordinary_viewer.py` finds `resolve.classify_principal` and `trusted_only` flat at the package root.*

Read first: the release-28 build records of YOUR package (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~116/r30/IRPT_STATUS_BUILD.json` for irpt-status, `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~117/r30/IRPT_YCHARTS_GENERATE_BUILD.json` for irpt-ycharts-generate, `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~118/r30/RESIDENT_BUILD.json` for the resident: they hold the base, the recorded inputs, the build commands, the guard counts and the control that reproduced the package that was live), the closing reports of the release-28 apply orders (`org/tier2_senior/0.7.0_AE_CloudOps~AQ2/deliverables/irpt_anlreq_r28/A_AFTER_R28a.txt` and `G_AFTER_R28c.txt`; `org/tier2_senior/0.7.0_AE_CloudOps~YC2/deliverables/irpt_anlreq_r28/D2_V1_INSTALL_R28.txt`: what is live now, with the VersionIds), the release-28 pair `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/release28/NEVER_WIDEN_PAIR_ANLREQ_RELEASE28_FWD1_CONSOLIDATED_FOUR_LEG.md` sections 2 and 3 (the shape the issuer will write for this release), and the trunk map entry of YOUR function in `infra/aws/lambda/ci/lambda-source-map.json` (the applier updated it at the close of release 28: its `last_deployed_commit` and `deployed_code_sha256` are what you test, not what you trust). RELEASE 29 moves ONLY: the plain words for `SHARES_PRICE_SOURCE_NOT_COMPOSED` (`intake/uploads.py`, `ops/status.py`; cell AR-y-308) and the ordinary-viewer authorizer of the upload door (`_scope/ordinary_viewer.py` NEW and `reports/generate_installed.py`; cell AR-y-306). If the comparison with the live package shows ANY other differing member, STOP the build, file a BLOCKING row naming it, and record what you have.

1. **The live read.** `.tools/aws lambda get-function --function-name irpt-ycharts-generate --query Configuration.CodeSha256 --output text` and `Code.Location`; download the zip into a NEW EMPTY folder under your `.scratch/r39/` (write the URL to a file and read it from Python run with `-I`), check its sha256 base64 equals the CodeSha256, and take `member_manifest` = member name -> sha256 for every file member. `list-object-versions` for the artifact key (prefix exact; print the latest VersionId and the version count as the denominator): the latest VersionId is the rollback target. Print each next to the release-28 applier's report (irpt-status VersionId V_g2PtX08Ktkbo5XYohrB5pHDFctjzZE, CodeSha256 MIVrDbv+/w8ioVB24xS97gnETVbNRCroDiY+Ne5osbA=; irpt-ycharts-generate VersionId edHLV8L0.FETO34.wAag6i7FHBJvfAuW, CodeSha256 reAjAQOVVfD4Wui2u0UfZRt7cr9o6ioFKIwXa+8EVgc=); a difference is a finding (someone released since): say what changed and carry on only if the change is already on the trunk.
2. **The no-move control.** Find the base and any diff the LIVE package was built from: the release-28 build record's recorded inputs (its base, its diff and build command) and the applier's closing report; the map entry's `last_deployed_commit` as the applier recorded it (test that it reproduces the live zip: row W116-S1 said the earlier record did not). Rebuild the live package in a throwaway worktree OUTSIDE the product tree at that base (guard count printed): `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-ycharts-generate` (read the script's usage header for the exact arguments; the release-28 record's command is the one that ran). Its CodeSha256 must equal the live one and `differs_from_live` must be `[]`. If the live package cannot be reproduced, name the members that differ and STOP with a BLOCKING row: the base is then not what runs.
3. **The release input.** In the throwaway worktree at the live package's base (the release-28 record's recorded inputs, which the applier closed into the trunk map), move ONLY the map pins of `intake/uploads.py` and `reports/generate_installed.py` to commits whose blobs equal the trunk HEAD's (full 40-hex commits; confirm each blob sha256), and ADD one `staged_from` row AND one `files[]` entry for `_scope/ordinary_viewer.py` packaged as `ordinary_viewer.py` at the package root, in the map entry only, following the shape of the calendar row the release-28 applier added (read it: rows W117-S1 and W117-S2 say a staged_from row alone does not ship a member and a pin move must also move the declared sha256). Check the import closure of each moved member against the package; a missing name is a finding for the CTO, not a silent widening. Make the change ONLY in a second throwaway worktree (never the trunk's map or recipe); save `git diff` of anything you edit there (the map, a builder) as `r39/<name>.diff` in your deliverable folder and print its `git hash-object`. Every moved member's new bytes must equal the trunk HEAD's blob (print both sha256).
4. **Build the release.** `BUILD_ONLY=1`, same command, in that worktree. Stage the zip as `C:/dev/irpt-release-r29/irpt-ycharts-generate-r29.zip`. Record `artifact` {`path`, `sha256` (hex of the zip), `bytes`, `code_sha256_base64` (the digest the script prints)}.
5. **Compare with the LIVE package, member by member.** `delta_vs_live` = members whose sha256 differ; `only_in_live`; `only_in_release`. EXPECTED: EXACTLY `["uploads.py", "generate_installed.py"]` as differing and `["ordinary_viewer.py"]` as only_in_release, each equal to the trunk HEAD's blob. Anything else: BLOCKING row, do not widen.
6. **Tests.** Run, from the build's source tree, every test file the cells above added or edited that this package's members are covered by (find them in the cells' records under `deliverables/0.9.0_WK_IRPT_ANLREQ~<n>/r2*/`), and the package's own folder's tests; report `named_tests`, `passed`, `failed`, `skipped`, `denominator`, and explain each failure one by one (a failure that also fails at the live base is baseline: name it).
7. **Write `r39/IRPT_YCHARTS_GENERATE_BUILD.json`:** `live_read`, `guard_counts`, `no_move_control` {`code_sha256`, `differs_from_live`}, `release_input` (the diff path and hash, the members moved with old and new sha256), `artifact`, `delta_vs_live`, `only_in_live`, `only_in_release`, `rollback` (the S3 latest VersionId and sha256 of the key, read in step 1 (expected edHLV8L0.FETO34.wAag6i7FHBJvfAuW)), `tests`, `claim`, `not_read`.
8. **In your report:** the live read in one line, the control (equal or not), the delta (members), the artifact path and sha256, the tests.

### ACCEPTANCE

<criterion id="AR310-y-AC1" cell_refs="AR-y-310"><invocation>python C:/dev/wk-irpt-anlreq-124/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y310-build --root C:/dev/wk-irpt-anlreq-124</invocation><expect>Y310-BUILD-OK</expect></criterion>
`AR310-y-AC1`: the record carries the live read of the package that is live now, a no-move control that reproduces its CodeSha256, a staged release zip whose sha256 the checker recomputes, a delta against the live package of exactly uploads.py and generate_installed.py plus the one added ordinary_viewer.py, passing tests, the import-closure finding (none or named), and the rollback VersionId.

<criterion id="AR310-y-AC2J" cell_refs="AR-y-310" judgment="true"/>
`AR310-y-AC2J` (judgment, graded at L9, never by you): the live package was read from AWS in this run and not taken from a record, the control reproduces the package that is live NOW, the guard count was printed before each build, the delta is exactly the two members plus the added module, and nothing was uploaded or applied.

<expected_criteria>AR310-y-AC1 AR310-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~124/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R39A_Y.md</decomp_doc>
<owned_cells>AR-y-310</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~124/IRPT_ANLREQ.TO-AR-y-310.release29-build-ycharts-generate.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-310`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR310-y-AC1,AR310-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a package zip staged outside the product tree, throwaway worktrees outside the repository, and read-only live AWS reads (get-function, list-object-versions, a download of the live zip); nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the release-28 build records and the applier's closing reports against the cell; the lens: a control that reproduces a stale package instead of the one live now, a map record taken for the live state, a member that moves that no cell changed. The order requires the delta to be compared with the LIVE package member by member and the staged artifact to be re-hashed by the checker. NOT seen: the live users and partner rows, the portal. NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the drained cells AR-y-306 (the ordinary-viewer authorizer) and AR-y-308 (the Shares words) as workstream `ZD` round 39: three builds feed the release-29 never-widen pair. Base: `AR310-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.
