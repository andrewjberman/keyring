# TO IRPT_ANLREQ.TO-AR-y-300.release-build-resident -- BUILD the resident release (one scratch input, the FWD-1 members) and prove its tests in a scratch tree

<to_id>IRPT_ANLREQ.TO-AR-y-300</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~118</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>30</round>
<workstream>YU</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-300` (`decompositions/IRPT_ANLREQ_DECOMP_R30A_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~118`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-118` (branch `wk-IRPT_ANLREQ-118`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~118 <0.9.0_WK_IRPT_ANLREQ~118@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W118-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call EXCEPT the read-only AWS reads the steps name (`get-function`, `get-function-configuration`, `list-object-versions`, `head-object`, a download of the live zip or of a version of the artifact key, through the `.tools/aws` shim), and a `git fetch` of remote-tracking refs; no push, no deploy, no upload, no apply, no invoke, no Terraform. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

- **THE BUILD GUARD (a past incident: row D2-S69):** every build is `BUILD_ONLY=1`, and before the first build at a base commit you run `git show <commit>:infra/aws/lambda/ci/build-and-upload.sh | grep -c BUILD_ONLY`: it must print at least 1 (the trunk builder prints 8). At a commit older than the guard the script UPLOADS. Print the count in your record. Your run must never reach `aws s3 cp`. The script writes ONE fixed temp path: copy the zip out at once. Stage every artifact under `C:/dev/irpt-release-r28/` (create it; it is outside the repository); never delete anything you did not make; say where scratch copies are.

### THE CELL (`AR-y-300`, inlined) -- BUILD ONLY. Nothing is uploaded, installed, applied or invoked.

*Leg L4 of the FWD-1 consolidated release: the investor-reporting RESIDENT (root `0485393f3a-r19` per record, not read live; tarball `irpt-resident-0485393f3a-r19.tar.gz` sha256 `84df6479655c07ae6000af40404e53eb056b4c403aa9134bbe9c1521317d497a`; the host script `resident_host_install_0485393f3a-r19.sh`; applier lane `0.7.0_AE_CloudOps~YC2`). The CTO's rule since release 19: the members the cells changed and what imports them, nothing else (the builder at the trunk would move 55 other differing paths). Members to move, built the release-19 / release-21 way (a scratch commit at the pin `0485393f3a`, the recipe's recorded arguments, the clock held): `intake/template_reader.py` (r19.3), `intake/portfolio.py`, `intake/uploads.py`, `intake/security_resolution.py`, `ops/status.py`, `ycharts/generate/resident_worker.py` (the registry identity port, AR-y-291), and ADD `ycharts/research/opal_packager.py` (AR-y-285) and `lib/trading_calendar.py` (AR-y-245). NOT in this release: `intake/yfinance_check.py` (nothing imports it yet; census finding S6). Two census findings change the recipe: the pin's builder (`reports/build_resident_package.py`) does not package the `ycharts/research` folder (added at `3775a93368`) and adds only `lib/opal_naming.py` from `lib/`; so the scratch input needs a minimal edit of the BUILDER to add those two sources, printed as a diff. Rows `W113-S3`, `W113-S4`, `W113-S5` in the channel.*

Read first: the census record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~113/r28/FWD1_RELEASE_CENSUS.json` (the member list, the writers, the live reads and the rollback of YOUR package; where it says INFERRED or NOT READ, read it yourself), the release-21 pair sections 1 to 3 `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/release21/NEVER_WIDEN_PAIR_ANLREQ_RELEASE21_READER_R193_TWO_LEG.md`, and the order `org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-228.lambda-leg-live-r193.md` (its steps 1 to 6 are the method for a Lambda build against the LIVE package: a live read, a no-move control, the release build, the member-by-member comparison). The release moves ONLY the members the cells changed and what they import; if the comparison with the live package shows ANY other differing member, STOP the build, file a BLOCKING row naming it, and record what you have.

Read also, as the method you repeat: `org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-227.resident-one-member-release-r193.md` (its THE CELL steps 1 to 7 are this cell's method; read its record `r21/RESIDENT_ONE_MEMBER_RELEASE.json` under its worker's folder and the release-19 records it names) and the host script `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/release19/resident_host_install_0485393f3a-r19.sh`.

1. **Make the build input.** As AR-y-227 step 1, with the replaced members above: in a throwaway worktree OUTSIDE the product tree cut at `0485393f3a`, replace each listed member with the TRUNK HEAD's blob (print old and new sha256 of each; `intake/uploads.py` must be the HEAD blob, not the r19 blob), ADD `ycharts/research/opal_packager.py` and `lib/trading_calendar.py`, and EDIT the scratch copy of the builder minimally so it packages `ycharts/research` (only the files the packager imports, if the builder supports a file list; otherwise the folder, and say which files that adds) and `lib/trading_calendar.py`. Print the builder diff and its `git hash-object`; say which of the packager's imports (its import closure) are satisfied by the package and which are not (a missing name is a finding for the CTO, never a silent widening). Make ONE local scratch commit (never pushed); say its hash.
2. **Build with the SAME recipe** as AR-y-227 (same arguments, the clock held to the recorded `generated_at`), with the scratch commit as the pin source and the new HOST_ROOT `/opt/irpt-resident/0485393f3a-r28` (rollback root: the running `0485393f3a-r19`). Stage the tarball as `C:/dev/irpt-release-r28/irpt-resident-0485393f3a-r28.tar.gz` and record its path, sha256, bytes, member count and the determinism control (two builds: every file identical by name and sha256).
3. **Delta against the release-19 tarball** (`C:/dev/irpt-release-r19/irpt-resident-0485393f3a-r19.tar.gz` if present, else `C:/dev/irpt-release-r193/`; check its sha256 first, extract to a scratch folder): `differing`, `only_in_old`, `only_in_new`, `removed_members_count`. EXPECTED differing: the six replaced members, `reports/resident_bindings.json` (root name and `provenance.member_overrides` only; say what changed inside) and `SHA256SUMS`; EXPECTED only_in_new: `ycharts/research/opal_packager.py` (and what the builder edit adds with it) and `lib/trading_calendar.py`; EXPECTED removed: 0. Anything else is a BLOCKING row.
4. **Host script.** Copy the release-19 host script to `r30/resident_host_install_0485393f3a-r28.sh` in your deliverable folder and change ONLY the lines that name the release (`NEW`, `OLD` (= `0485393f3a-r19`), `WANT_TAR`, the member checks for the moved and added members, the ledger and the header comment); print a `diff` and the sha256 of yours. Its member-check hashes must equal the new tarball's members (compute and say so).
5. **Prove the tests on the build, in a scratch tree.** Extract the tarball outside the tree, copy the test files from your worktree (the tarball carries none), run against the extracted package with `PYTHONPATH` set to the package root: the test files the cells above added or edited that cover the moved members (from the cells' records: `intake/tests/test_kept_holding.py`, `test_correction_words.py`, the price-date and portfolio tests, `test_template_reader.py`, `test_stored_input_contract.py`, the registry-port test under `ycharts/generate/tests/`, `ycharts/research/tests/test_opal_packager_request_id.py`), report `named_tests`, `passed`, `failed`, `skipped`, `denominator`; explain each failure one by one against the known baselines of the release-19 and release-21 records.
6. **Write `r30/RESIDENT_BUILD.json`:** `scratch_commit`, `base_tarball` {`path`, `sha256`}, `release_input` (members with old and new sha256, the builder diff path and hash, the import-closure finding), `artifact` {`path`, `sha256`, `bytes`, `member_count`, `determinism_control`}, `delta_vs_live` (the differing member names against the release-19 tarball, the same list as `differing`), `only_in_live` (= `only_in_old`), `only_in_release` (= `only_in_new`), `removed_members_count`, `root_naming` (`NEW`, `OLD`, what the bindings carry), `host_script` {`path`, `sha256`, `lines_changed`, `member_checks_equal_tarball`}, `rollback` (the running root and the base tarball's sha256), `tests`, `claim`, `not_read`.
7. **In your report:** the delta in one line, the tarball sha256, the tests, the builder diff in one line, the host script's changed lines.

### ACCEPTANCE

<criterion id="AR300-y-AC1" cell_refs="AR-y-300"><invocation>python C:/dev/wk-irpt-anlreq-118/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y300-build --root C:/dev/wk-irpt-anlreq-118</invocation><expect>Y300-BUILD-OK</expect></criterion>
`AR300-y-AC1`: the record carries a scratch input with the listed members at the trunk HEAD blobs, a staged tarball whose sha256 the checker recomputes, a delta against the release-19 tarball of exactly the expected members with zero removed, the builder diff, the host script with member checks equal to the tarball, and the tests run in a scratch tree with every failure explained.

<criterion id="AR300-y-AC2J" cell_refs="AR-y-300" judgment="true"/>
`AR300-y-AC2J` (judgment, graded at L9, never by you): the delta against the release-19 tarball is exactly the six replaced members, the bindings, SHA256SUMS and the two additions with nothing removed, the builder edit is minimal and printed, the packager's import closure is stated, the host script changes only the release-naming lines, and nothing was uploaded, installed or applied.

<expected_criteria>AR300-y-AC1 AR300-y-AC2J</expected_criteria>

**AMENDMENT 1 (issuer `2.0.0_SA_COO~Y2`, 2026-10-14 ~01:3xZ, after the worker's BLOCKING row `IRPT_ANLREQ-D2-W118-S2`; the worker was right).** `ycharts/research/opal_packager.py` is ALREADY in the release-19 tarball, so this release REPLACES it (a differing member), it does not add it; the census finding that the pin's builder could not package the `ycharts/research` folder concerned a different builder file (row `W118-S3`: the recipe builder ran unedited, so the builder diff is empty). The expected delta against the release-19 tarball is therefore: differing = the six replaced members, `opal_packager.py`, `resident_bindings.json` and `SHA256SUMS`; only_in_new = `lib/trading_calendar.py` only; removed 0. The checker `y300-build` is corrected to that expectation; the criterion text is unchanged. Gate limb that graded this amendment: none stated (the issuer amends its own pending order's expectation and checker).

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~118/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R30A_Y.md</decomp_doc>
<owned_cells>AR-y-300</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~118/IRPT_ANLREQ.TO-AR-y-300.release-build-resident.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-300`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR300-y-AC1,AR300-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a package zip staged outside the product tree, throwaway worktrees outside the repository, and read-only live AWS reads (get-function, list-object-versions, a download of the live zip); nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the census record and the release-19 / release-21 build records against the cell; the lens: a build that moves a member no cell changed, a control that reproduces a stale package instead of the one live now, a record that names an artifact that does not hash to its claim. The order requires the delta to be compared with the LIVE package member by member and the staged artifact to be re-hashed by the checker. NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the FWD-1 consolidated release census `AR-y-295` (drained; legs L1 to L4) as workstream `YU` round 30. Four independent builds feed the never-widen pair; the appliers are named in the pair, not here. Base: `AR300-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.
