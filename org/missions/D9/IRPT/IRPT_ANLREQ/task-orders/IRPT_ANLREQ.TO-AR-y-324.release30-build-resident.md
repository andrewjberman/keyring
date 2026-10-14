# TO IRPT_ANLREQ.TO-AR-y-324.release30-build-resident -- BUILD the investor-reporting RESIDENT package for the intake release (AR-y-318 and AR-y-319) and compare it with the live package; nothing is uploaded or applied

<to_id>IRPT_ANLREQ.TO-AR-y-324</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~132</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>ZJ</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the class the infrastructure `<paths>` imply; the worker builds only: nothing is uploaded, applied or invoked)
**Decomp cell:** `AR-y-324` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (hop 1, the owned-input analysis of a partner advisor) | **depends_on:** `AR-y-318` (merged `ece60105e1`), `AR-y-319` (merged `1176eb009a`)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~132`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-132` (branch `wk-IRPT_ANLREQ-132`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~132 <0.9.0_WK_IRPT_ANLREQ~132@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W132-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet` fixture): never commit either to the WORKSPACE repository. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. No live call EXCEPT the read-only AWS reads the steps name (`get-function`, `get-function-configuration`, `list-object-versions`, `head-object`, a download of the live zip or of a version of the artifact key, through the `.tools/aws` shim), and a `git fetch` of remote-tracking refs; no push, no deploy, no upload, no apply, no invoke, no Terraform. No non-ASCII in what you add. Scratch outside the product tree (you may not delete recursively; say where it is).
- **THE BUILD GUARD (a past incident: row D2-S69):** every build is `BUILD_ONLY=1`, and before the first build at a base commit you run `git show <commit>:infra/aws/lambda/ci/build-and-upload.sh | grep -c BUILD_ONLY`: it must print at least 1 (the trunk builder prints 8). At a commit older than the guard the script UPLOADS. Print the count in your record. Your run must never reach `aws s3 cp`. The script writes ONE fixed temp path per function: use a PRIVATE `TMPDIR` (a new empty folder outside the repository) for every build and copy the artifact out at once. Stage every artifact under `C:/dev/irpt-release-r30/` (create it; it is outside the repository; another worker builds the other package there at the same time: touch only your own file names); never delete anything you did not make.

### THE CELL (`AR-y-324`, inlined) -- BUILD ONLY. Nothing is uploaded, applied, deployed or invoked.

*The intake release moves THREE members of investor-reporting RESIDENT package, each equal to the trunk blob: `ycharts/generate/composition_admission.py` (AR-y-318: `validate` names the failing step and error class in one log line and still raises the same public code), `intake/uploads.py` (AR-y-318: `load_input_owner` raises the declared typed `InputUnavailable` instead of a bare `PermissionError`) and `_scope/interactive_access.py` (AR-y-319: `prospect_owner()` omits `home_firm_id` unless the class is OPAL_GLOBAL, so a partner advisor's frozen composition passes the schema, row D2-S97). Live now (release 29, 2026-10-14T12:42Z): root `/opt/irpt-resident/0485393f3a-r29`, tarball sha256 `2de2adce622f8bb9bbd5ebc071e862446b056303c0d9ffd7d41b050bd17f51a4`. The resident is installed by a host script, never by a Terraform call, and the applier (`0.7.0_AE_CloudOps~YC2`) does that, not you.*

Read first: the release-29 build record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~125/r39/RESIDENT_BUILD.json` and its scripts (the base, the recorded inputs, the builder, the pack method), the applier's V1 output `org/tier2_senior/0.7.0_AE_CloudOps~YC2/deliverables/irpt_anlreq_r29/D2_V1_INSTALL_R29.txt` (what runs now) and the cells' records `.../0.9.0_WK_IRPT_ANLREQ~128/r40/COMPOSITION_CAUSE.json` and `.../0.9.0_WK_IRPT_ANLREQ~129/r40/OWNER_FIX.json`. The release moves ONLY those three members (plus the bindings file's `package_pin` and the sums, which follow from them); if the comparison with the live package shows ANY other differing member, STOP the build, file a BLOCKING row naming it, and record what you have.

1. **The base.** The live resident root is `/opt/irpt-resident/0485393f3a-r29` from the tarball `irpt-resident-0485393f3a-r29.tar.gz` (sha256 `2de2adce622f8bb9bbd5ebc071e862446b056303c0d9ffd7d41b050bd17f51a4`, 1036774 bytes, 299 members; YC2's `D2_V1_INSTALL_R29.txt` is the record of what runs). The host is NOT read by you (no host call). Hash the staged r29 tarball at `C:/dev/irpt-release-r29/irpt-resident-0485393f3a-r29.tar.gz` and compare with the value above; extract it into a NEW EMPTY folder under your `.scratch/r40/` for the member comparison. Print each next to the record; a difference is a finding.
2. **The release input.** The recipe is the release-29 one: the build record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~125/r39/RESIDENT_BUILD.json` (`release_input`, `pin_source`, the builder blob `e1e58c2d94`, the `files_from` list and its sha256 `ba5bd2c2...`) and its scripts under `.../0.9.0_WK_IRPT_ANLREQ~125/r39/`. Use the SAME builder copy (the blob `e1e58c2d94`; the worktree HEAD builder differs: row W125-S1) from an outside builder root, with `--pin` the full sha of the trunk HEAD (state it; it must contain `1176eb009a`; use `git fetch origin` for remote-tracking refs only) and `--base-pin 0485393f3ad0a7e564f4867f5e70003e2e62195b` as in release 29, a build clock held fixed and the packing of release 29 (`pack_one.py`: SHA256SUMS first then sorted names, mode 0644, uid/gid/mtime zero, gzip mtime zero). The files-from list is the release-29 list of 7 repo paths PLUS the two new members `_scope/interactive_access.py` and `ycharts/generate/composition_admission.py` IF the recipe needs them listed (read how the recipe takes a member from the pin: if a member is not in `files_from` the base pin's copy ships; the three moved members MUST come from the trunk pin: say how you ensured it). Every moved member's new bytes must equal the trunk HEAD's blob (print both sha256).
3. **Build the release root `0485393f3a-r30`** (the old root is `0485393f3a-r29`) TWICE with the same arguments: the two builds must be identical 299 of 299 by name and sha256. Stage `C:/dev/irpt-release-r30/irpt-resident-0485393f3a-r30.tar.gz` (single packing of build A) and `irpt-resident-0485393f3a-r30.package.SHA256SUMS`. Record `artifact` {`path`, `sha256`, `bytes`, `member_count`, `code_sha256_base64` is not applicable: write the field `code_sha256_base64` as the string `n/a`}.
4. **Compare with the r29 tarball, member by member.** `delta_vs_live` = members whose sha256 differ; `only_in_live`; `only_in_release`; `removed_members_count`. EXPECTED: EXACTLY `composition_admission.py`, `interactive_access.py`, `uploads.py`, plus `resident_bindings.json` (ONLY `provenance.package_pin` changes: verify by a diff of the two extracted bindings files) and `SHA256SUMS`; nothing added, nothing removed (299 members). Anything else: BLOCKING row, do not widen.
5. **The scripts.** Derive from the release-29 scripts by the AR-y-301 and AR-y-311 method, changing only NEW, OLD, WANT, WANTSUM and the member read-backs: `resident_host_install_0485393f3a-r30.sh`, `pre_read_r30.sh`, `install_r30.sh`, `rollback_r30.sh` (the names the checker reads), all `bash -n` rc 0 and ASCII, each with its sha256 in the record. The host script's member checks must equal the tarball (print the count). Run the one-byte dry run: the install script must refuse both sha256 gates (rc 31 and rc 33) as in release 29. Do NOT run any script against the host.
6. **Tests.** Extract the tarball and run, as in release 29 (`.../~125/r39/`: the trunk test folders extracted from the pin by `git archive`, PYTHONPATH on the package root): `_scope/tests/test_ordinary_viewer.py` (43 expected), `test_ordinary_owner_composition.py`, `intake/tests/test_load_input_owner_typed.py`, `ycharts/generate/tests/test_composition_refusal_cause.py`, `test_ordinary_owner_legacy_row.py` and the release-29 named files (`intake/tests/test_correction_words.py`, `test_shares_not_composed_words.py`, `test_deferred_resolution.py`, `ops/tests/test_status.py`); report `named_tests`, `passed`, `failed`, `skipped`, `denominator`, and explain each failure one by one (a failure that also fails at the r29 base is baseline: name it).
7. **Write `r40/RESIDENT_BUILD.json`** (the checker `y324-build` reads it): `live_read` (the r29 tarball hash comparison), `guard_counts` (not applicable: no ci script is run: say so), `release_input`, `artifact`, `delta_vs_live`, `only_in_live`, `only_in_release`, `removed_members_count`, `host_script` {`path`, `sha256`, `member_checks_equal_tarball`}, `scripts` [{`name`, `path`, `sha256`, `bytes`, `ascii_only`, `bash_n_rc`} for the three scripts], `sums_file` {`path`, `sha256`, `lines`}, `rollback` {`running_root`: `/opt/irpt-resident/0485393f3a-r29`, `rollback_root`, `base_tarball_sha256`}, `tests`, `claim`, `not_read`.
8. **In your report:** the base hash comparison in one line, the delta (members), the artifact path and sha256, the tests, the scripts' hashes.

### ACCEPTANCE

<criterion id="AR324-y-AC1" cell_refs="AR-y-324"><invocation>python C:/dev/wk-irpt-anlreq-132/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y324-build --root C:/dev/wk-irpt-anlreq-132</invocation><expect>Y324-BUILD-OK</expect></criterion>
`AR324-y-AC1`: the record carries the base hash comparison, a staged release tarball whose sha256 the checker recomputes, two identical builds, a delta against the r29 tarball of exactly composition_admission.py, interactive_access.py, uploads.py, resident_bindings.json and SHA256SUMS (nothing added or removed), the three scripts re-hashed (ASCII, bash -n clean), the staged sums, and passing tests.

<criterion id="AR324-y-AC2J" cell_refs="AR-y-324" judgment="true"/>
`AR324-y-AC2J` (judgment, graded at L9, never by you): the base tarball was hashed in this run and not taken from a record, the two builds are identical 299 of 299, the delta is exactly the named members with only the bindings' package_pin changed, the scripts differ from release 29's only in the root names, hashes and the member read-backs, no script was run against the host, and nothing was uploaded or applied.

<expected_criteria>AR324-y-AC1 AR324-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~132/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-324</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~132/IRPT_ANLREQ.TO-AR-y-324.release30-build-resident.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-324`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR324-y-AC1,AR324-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- an artifact staged outside the product tree, throwaway worktrees outside the repository, and read-only live AWS reads; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no change.
comp-adversary: RUN -- by reading the release-29 build record of this package, the applier's closing report, and rows W123-S1, W124-S3, W125-S1 and D2-S69 against the cell; the lens: a control that reproduces a stale package instead of the one live now, a map record taken for the live state, a build at a commit without the guard that uploads, a member that moves that no cell changed. The order requires the live read in the run, the guard count before each build, the member-by-member comparison with the live package and the staged artifact re-hashed by the checker. NOT seen: the live users and partner rows, the portal.
</preflight>

---

## RECORD FACE

- Cut on the merged cells `AR-y-318` and `AR-y-319` for the intake release pair (the issuer's, after the two builds), workstream `ZJ` of round 40. Base: `AR324-y-AC1` FAIL as expected (`y324-build` prints `Y324-BUILD-FAIL`: no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.
