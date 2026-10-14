# TO IRPT_ANLREQ.TO-AR-y-311.release29-build-resident -- BUILD the resident release 29 (the Shares words) over the release-28 root, write its three host scripts, and prove its tests in a scratch tree

<to_id>IRPT_ANLREQ.TO-AR-y-311</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~125</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>39</round>
<workstream>ZD</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-311` (`decompositions/IRPT_ANLREQ_DECOMP_R39A_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~125`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-125` (branch `wk-IRPT_ANLREQ-125`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~125 <0.9.0_WK_IRPT_ANLREQ~125@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W125-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call EXCEPT the read-only AWS reads the steps name (`get-function`, `get-function-configuration`, `list-object-versions`, `head-object`, a download of the live zip or of a version of the artifact key, through the `.tools/aws` shim), and a `git fetch` of remote-tracking refs; no push, no deploy, no upload, no apply, no invoke, no Terraform. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

- **THE BUILD GUARD (a past incident: row D2-S69):** every build is `BUILD_ONLY=1`, and before the first build at a base commit you run `git show <commit>:infra/aws/lambda/ci/build-and-upload.sh | grep -c BUILD_ONLY`: it must print at least 1 (the trunk builder prints 8). At a commit older than the guard the script UPLOADS. Print the count in your record. Your run must never reach `aws s3 cp`. The script writes ONE fixed temp path: copy the zip out at once. Stage every artifact under `C:/dev/irpt-release-r29/` (create it; it is outside the repository); never delete anything you did not make; say where scratch copies are.

### THE CELL (`AR-y-311`, inlined) -- BUILD ONLY. Nothing is uploaded, installed, applied or invoked; the scripts are files you write and do not run.

*Leg L4 of release 29: the investor-reporting RESIDENT, root `0485393f3a-r28` (installed 2026-10-14T02:29:14Z; tarball `irpt-resident-0485393f3a-r28.tar.gz` sha256 `80f4743091a10c0d82b6cba4f66ba4afb6188ece0b64b269066c5426a6335a68`; applier `0.7.0_AE_CloudOps~YC2`). Members to move: `intake/uploads.py` and `ops/status.py` (the one word entry, AR-y-308) and nothing else; the resident does NOT move `reports/generate_installed.py` or add `ordinary_viewer.py` in this release (the door runs in the Lambda; the module is imported lazily). New root `0485393f3a-r29`; rollback root `0485393f3a-r28`.*

Read first: the release-28 build records of YOUR package (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~116/r30/IRPT_STATUS_BUILD.json` for irpt-status, `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~117/r30/IRPT_YCHARTS_GENERATE_BUILD.json` for irpt-ycharts-generate, `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~118/r30/RESIDENT_BUILD.json` for the resident: they hold the base, the recorded inputs, the build commands, the guard counts and the control that reproduced the package that was live), the closing reports of the release-28 apply orders (`org/tier2_senior/0.7.0_AE_CloudOps~AQ2/deliverables/irpt_anlreq_r28/A_AFTER_R28a.txt` and `G_AFTER_R28c.txt`; `org/tier2_senior/0.7.0_AE_CloudOps~YC2/deliverables/irpt_anlreq_r28/D2_V1_INSTALL_R28.txt`: what is live now, with the VersionIds), the release-28 pair `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/release28/NEVER_WIDEN_PAIR_ANLREQ_RELEASE28_FWD1_CONSOLIDATED_FOUR_LEG.md` sections 2 and 3 (the shape the issuer will write for this release), and the trunk map entry of YOUR function in `infra/aws/lambda/ci/lambda-source-map.json` (the applier updated it at the close of release 28: its `last_deployed_commit` and `deployed_code_sha256` are what you test, not what you trust). RELEASE 29 moves ONLY: the plain words for `SHARES_PRICE_SOURCE_NOT_COMPOSED` (`intake/uploads.py`, `ops/status.py`; cell AR-y-308) and the ordinary-viewer authorizer of the upload door (`_scope/ordinary_viewer.py` NEW and `reports/generate_installed.py`; cell AR-y-306). If the comparison with the live package shows ANY other differing member, STOP the build, file a BLOCKING row naming it, and record what you have.

Read also, as the method you repeat: the order `org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-300.release-build-resident.md` with its AMENDMENT 1 and its record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~118/r30/RESIDENT_BUILD.json` (the recipe builder, the `--pin` / `--base-pin` / `--files-from` route, the clock held, the determinism control), and the order `org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-301.resident-apply-scripts-r28.md` with its record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~119/r31/RESIDENT_APPLY_SCRIPTS.json` and the three scripts `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~119/r31/pre_read_r28.sh`, `install_r28.sh`, `rollback_r28.sh` (they ran on the host under `0.7.0_AE_CloudOps~YC2`; their output is in `org/tier2_senior/0.7.0_AE_CloudOps~YC2/deliverables/irpt_anlreq_r28/`).

1. **Build.** As AR-y-300, with the BASE the release-28 tarball (check its sha256 first) and the replaced members `intake/uploads.py` and `ops/status.py` at the TRUNK HEAD blobs (print old and new sha256). Stage the tarball as `C:/dev/irpt-release-r29/irpt-resident-0485393f3a-r29.tar.gz` (record path, sha256, bytes, member count, the determinism control). New HOST_ROOT `/opt/irpt-resident/0485393f3a-r29`. Delta against the release-28 tarball: EXPECTED differing exactly `intake/uploads.py`, `ops/status.py`, `reports/resident_bindings.json` (say what changed inside) and `SHA256SUMS`; only_in_new none; removed 0. Anything else: BLOCKING row.
2. **Host script.** Copy `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~118/r30/resident_host_install_0485393f3a-r28.sh` to `r39/resident_host_install_0485393f3a-r29.sh`, change ONLY the lines that name the release (`NEW`, `OLD` (= `0485393f3a-r28`), `WANT_TAR`, the member checks for the two moved members, the ledger string, the header comment); print a `diff` and the sha256; its member-check hashes must equal the new tarball's members.
3. **Stage the package sums** `C:/dev/irpt-release-r29/irpt-resident-0485393f3a-r29.package.SHA256SUMS` = the tarball's own `SHA256SUMS` member (record sha256 and line count; control: the r28 file reproduces the same way).
4. **Write `r39/pre_read_r29.sh`, `r39/install_r29.sh`, `r39/rollback_r29.sh`** from the three r28 scripts by the AR-y-301 method: change ONLY what the old root changed (the running root is now r28 and the r29 root must be absent; the reader and worker members read at the r28 values: `intake/uploads.py` sha256 `80ace2d376c854d6208bc0c17810e053bc538ff9e71ec5a96d8dc89629d01951`, `ops/status.py` `03fa9c78c9dd3ef2cd1321ad295ad4ea3df0ee996c473ee963652788332737d3` before, the new values after; the other six r28 members unchanged and read back at their r28 values; the sums check against the new file; the rollback root r28). Keep every fetch, sha256 and refusal guard with its exit code. `bash -n` each, ASCII only, a dry run of the two sha256 gates with a one-byte change that must refuse. Print the diffs against the r28 scripts with every changed line justified. Never run the scripts.
5. **Tests in a scratch tree** as AR-y-300 step 5 (the named test files covering the two members: `intake/tests/test_correction_words.py`, `test_shares_not_composed_words.py`, `test_deferred_resolution.py`, and the ops status tests that run on the extracted package); report counts and explain each failure against the release-28 baselines (the S26 digest test and the repository-path test are known).
6. **Write `r39/RESIDENT_BUILD.json`:** `base_tarball`, `release_input`, `artifact` {`path`, `sha256`, `bytes`, `member_count`, `determinism_control`}, `delta_vs_live` (differing against the r28 tarball), `only_in_live`, `only_in_release`, `removed_members_count`, `root_naming`, `host_script` {`path`, `sha256`, `member_checks_equal_tarball`}, `scripts` (objects: `name`, `path`, `sha256`, `bash_n_rc`), `sums_file` {`path`, `sha256`, `lines`}, `rollback`, `tests`, `claim`, `not_read`.
7. **In your report:** the delta in one line, the tarball sha256, the scripts' sha256 values, the tests.

### ACCEPTANCE

<criterion id="AR311-y-AC1" cell_refs="AR-y-311"><invocation>python C:/dev/wk-irpt-anlreq-125/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y311-build --root C:/dev/wk-irpt-anlreq-125</invocation><expect>Y311-BUILD-OK</expect></criterion>
`AR311-y-AC1`: the record carries a staged tarball whose sha256 the checker recomputes, a delta against the release-28 tarball of exactly the two moved members, the bindings and the sums with nothing added or removed, the host script with member checks equal to the tarball, the three scripts (bash -n rc 0, re-hashed) and the staged sums file, and the tests with every failure explained.

<criterion id="AR311-y-AC2J" cell_refs="AR-y-311" judgment="true"/>
`AR311-y-AC2J` (judgment, graded at L9, never by you): the delta is exactly uploads.py, status.py, the bindings and SHA256SUMS, the host script changes only the release-naming lines, the three scripts change only what the old root changed with every guard kept and a one-byte change refused by the dry run, and nothing was uploaded, installed, applied or run on the host.

<expected_criteria>AR311-y-AC1 AR311-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~125/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R39A_Y.md</decomp_doc>
<owned_cells>AR-y-311</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~125/IRPT_ANLREQ.TO-AR-y-311.release29-build-resident.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-311`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR311-y-AC1,AR311-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a package zip staged outside the product tree, throwaway worktrees outside the repository, and read-only live AWS reads (get-function, list-object-versions, a download of the live zip); nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the release-28 build records and the applier's closing reports against the cell; the lens: a control that reproduces a stale package instead of the one live now, a map record taken for the live state, a member that moves that no cell changed. The order requires the delta to be compared with the LIVE package member by member and the staged artifact to be re-hashed by the checker. NOT seen: the live users and partner rows, the portal. NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the drained cells AR-y-306 (the ordinary-viewer authorizer) and AR-y-308 (the Shares words) as workstream `ZD` round 39: three builds feed the release-29 never-widen pair. Base: `AR311-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.
