# TO IRPT_ANLREQ.TO-AR-y-298.release-build-status-words -- BUILD the irpt-status package for the FWD-1 consolidated release (three new finding-code words) and compare it with the live package

<to_id>IRPT_ANLREQ.TO-AR-y-298</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~116</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>30</round>
<workstream>YU</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-298` (`decompositions/IRPT_ANLREQ_DECOMP_R30A_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~116`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-116` (branch `wk-IRPT_ANLREQ-116`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~116 <0.9.0_WK_IRPT_ANLREQ~116@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W116-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call EXCEPT the read-only AWS reads the steps name (`get-function`, `get-function-configuration`, `list-object-versions`, `head-object`, a download of the live zip or of a version of the artifact key, through the `.tools/aws` shim), and a `git fetch` of remote-tracking refs; no push, no deploy, no upload, no apply, no invoke, no Terraform. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

- **THE BUILD GUARD (a past incident: row D2-S69):** every build is `BUILD_ONLY=1`, and before the first build at a base commit you run `git show <commit>:infra/aws/lambda/ci/build-and-upload.sh | grep -c BUILD_ONLY`: it must print at least 1 (the trunk builder prints 8). At a commit older than the guard the script UPLOADS. Print the count in your record. Your run must never reach `aws s3 cp`. The script writes ONE fixed temp path: copy the zip out at once. Stage every artifact under `C:/dev/irpt-release-r28/` (create it; it is outside the repository); never delete anything you did not make; say where scratch copies are.

### THE CELL (`AR-y-298`, inlined) -- BUILD ONLY. Nothing is uploaded, applied, deployed or invoked.

*Leg L2 of the FWD-1 consolidated release: `irpt-status` (`infra/aws/lambda/investor-reporting/ops`) gets `ops/status.py` (packaged as `status.py`) from the trunk: `CORRECTION_WORDS` gains exactly three keys (`TICKER_KEPT_BY_HISTORY`, `TICKER_CHECK_FAILED`, `TICKER_NOT_CHECKED`; AR-y-293, words only by an AST comparison). Live now (census): CodeSha256 `vlGh380QUKvBMOhJn0GJGgDi1/WLI9qTaSP2uETmdP4=`, 363594 bytes, last modified 2026-10-13T12:55:10Z. The status envelope must know the three words before a KEPT answer uses them.*

Read first: the census record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~113/r28/FWD1_RELEASE_CENSUS.json` (the member list, the writers, the live reads and the rollback of YOUR package; where it says INFERRED or NOT READ, read it yourself), the release-21 pair sections 1 to 3 `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/release21/NEVER_WIDEN_PAIR_ANLREQ_RELEASE21_READER_R193_TWO_LEG.md`, and the order `org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-228.lambda-leg-live-r193.md` (its steps 1 to 6 are the method for a Lambda build against the LIVE package: a live read, a no-move control, the release build, the member-by-member comparison). The release moves ONLY the members the cells changed and what they import; if the comparison with the live package shows ANY other differing member, STOP the build, file a BLOCKING row naming it, and record what you have.

1. **The live read.** `.tools/aws lambda get-function --function-name irpt-status --query Configuration.CodeSha256 --output text` and `Code.Location`; download the zip into a NEW EMPTY folder under your `.scratch/r30/` (write the URL to a file and read it from Python run with `-I`), check its sha256 base64 equals the CodeSha256, and take `member_manifest` = member name -> sha256 for every file member. `list-object-versions` for the artifact key (prefix exact; print the latest VersionId and the version count as the denominator): the latest VersionId is the rollback target. Print each next to the census record's value; a difference is a finding (someone released since the census): say what changed and carry on only if the change is already on the trunk.
2. **The no-move control.** Find the base and any diff the LIVE package was built from (the map entry's `staged_from` pins and `deployed_code_sha256`, the ledger entry of the last release named in the census record, the release record of the seat that last released it: name what you read). Rebuild the live package in a throwaway worktree OUTSIDE the product tree at that base (guard count printed): `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-status` (read the script's usage header for the exact arguments; the census record's signature is INFERRED). Its CodeSha256 must equal the live one and `differs_from_live` must be `[]`. If the live package cannot be reproduced, name the members that differ and STOP with a BLOCKING row: the base is then not what runs.
3. **The release input.** Check out the trunk HEAD in a throwaway worktree (state its full sha). The only packaged member expected to differ is `ops/status.py` (`status.py` in the zip); print an AST comparison of the live package's `status.py` against the trunk's showing that only the `CORRECTION_WORDS` literal differs and only by the three added keys. Make the change ONLY in a second throwaway worktree (never the trunk's map or recipe); save `git diff` of anything you edit there (the map, a builder) as `r30/<name>.diff` in your deliverable folder and print its `git hash-object`. Every moved member's new bytes must equal the trunk HEAD's blob (print both sha256).
4. **Build the release.** `BUILD_ONLY=1`, same command, in that worktree. Stage the zip as `C:/dev/irpt-release-r28/irpt-status-r28.zip`. Record `artifact` {`path`, `sha256` (hex of the zip), `bytes`, `code_sha256_base64` (the digest the script prints)}.
5. **Compare with the LIVE package, member by member.** `delta_vs_live` = members whose sha256 differ; `only_in_live`; `only_in_release`. EXPECTED: EXACTLY `["status.py"]`, equal to the trunk HEAD's blob, the AST comparison words-only. Anything else: BLOCKING row, do not widen.
6. **Tests.** Run, from the build's source tree, every test file the cells above added or edited that this package's members are covered by (find them in the cells' records under `deliverables/0.9.0_WK_IRPT_ANLREQ~<n>/r2*/`), and the package's own folder's tests; report `named_tests`, `passed`, `failed`, `skipped`, `denominator`, and explain each failure one by one (a failure that also fails at the live base is baseline: name it).
7. **Write `r30/IRPT_STATUS_BUILD.json`:** `live_read`, `guard_counts`, `no_move_control` {`code_sha256`, `differs_from_live`}, `release_input` (the diff path and hash, the members moved with old and new sha256), `artifact`, `delta_vs_live`, `only_in_live`, `only_in_release`, `rollback` (the S3 latest VersionId and sha256 of the key, read in step 1), `tests`, `claim`, `not_read`.
8. **In your report:** the live read in one line, the control (equal or not), the delta (members), the artifact path and sha256, the tests.

### ACCEPTANCE

<criterion id="AR298-y-AC1" cell_refs="AR-y-298"><invocation>python C:/dev/wk-irpt-anlreq-116/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y298-build --root C:/dev/wk-irpt-anlreq-116</invocation><expect>Y298-BUILD-OK</expect></criterion>
`AR298-y-AC1`: the record carries the live read, a no-move control equal to the live CodeSha256, a staged release zip whose sha256 the checker recomputes, a delta against the live package of exactly status.py, an AST words-only comparison, passing tests, and the rollback VersionId.

<criterion id="AR298-y-AC2J" cell_refs="AR-y-298" judgment="true"/>
`AR298-y-AC2J` (judgment, graded at L9, never by you): the live package was read from AWS in this run and not taken from a record, the guard count was printed before each build, both builds were BUILD_ONLY, the delta is exactly the one member and words-only, and nothing was uploaded or applied.

<expected_criteria>AR298-y-AC1 AR298-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~116/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R30A_Y.md</decomp_doc>
<owned_cells>AR-y-298</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~116/IRPT_ANLREQ.TO-AR-y-298.release-build-status-words.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-298`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR298-y-AC1,AR298-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a package zip staged outside the product tree, throwaway worktrees outside the repository, and read-only live AWS reads (get-function, list-object-versions, a download of the live zip); nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the census record and the release-19 / release-21 build records against the cell; the lens: a build that moves a member no cell changed, a control that reproduces a stale package instead of the one live now, a record that names an artifact that does not hash to its claim. The order requires the delta to be compared with the LIVE package member by member and the staged artifact to be re-hashed by the checker. NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the FWD-1 consolidated release census `AR-y-295` (drained; legs L1 to L4) as workstream `YU` round 30. Four independent builds feed the never-widen pair; the appliers are named in the pair, not here. Base: `AR298-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.
