# TO IRPT_ANLREQ.TO-AR-y-212.status-rule-rebase-a -- the status rule rebased on the live packages of pin group A

<to_id>IRPT_ANLREQ.TO-AR-y-212</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~61</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>20</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD
**Decomp cell:** `AR-y-212` (`decompositions/IRPT_ANLREQ_DECOMP_R20_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~61`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-61` (branch `wk-IRPT_ANLREQ-61`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~61 <0.9.0_WK_IRPT_ANLREQ~61@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W61-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call EXCEPT the read-only `get-function` and the download of each `Code.Location` zip named below; no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-212`, inlined) -- THE STATUS RULE REBASED ON THE LIVE PACKAGES OF GROUP A: `irpt-performance-adapter`, `irpt-narrative`, `irpt-status`. Nothing is uploaded, deployed or applied.

*The status rule (AR-y-172: an internal caller selecting another firm is admitted only for an `active` users row; AR-y-184 caller-class log line) is in the trunk's `_authz/served.py` and in none of the eight packagers' shipped bytes.* The CTO (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_20_20261013.md` section 2/3, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_20_20261013.md` round 19 section 1): ONE `served.py` into all eight, both pin groups together, narrative's test staging moved to the new pin so its suite tests what ships. This cell is for ONE pin group and builds nothing live. **Release 19 taught this seat a rule: the package that is LIVE is read from AWS in the run; a record of it is not evidence** (ADVI_FIRMBKTS act 4 replaced `irpt-ycharts-generate` and the other seven on 2026-10-12, and release 19 replaced `irpt-ycharts-generate` again).

**Read first:** `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/r18/SERVED_PY_PACKAGERS.json` (the eight packagers, the two pins 361c44fa9d and 74a62fb46c, `what_moves_together`), `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~56/r19/LAMBDA_LEG_LIVE_REBASE.json` (the method this cell repeats: live read, holds-only control, release patch, comparison; `hold_pins`, `release_build`), the act-4 ledger `org/critical_paths/change_management/20261012T1340Z_advi-firmbkts-fb-f-11-act4-irpt-leg-20261012_deploy_completion.md` (section "Builds": which commit each of the eight was built from), and `infra/aws/lambda/ci/lambda-source-map.json` (each function's entry: `staged_from`, `last_deployed_commit`).

For EACH function in your group, in order:
1. **Live read.** `.tools/aws lambda get-function --function-name <fn> --query Configuration.CodeSha256 --output text` and `Code.Location` (a single-resource read; the `.tools/aws` shim); download the zip into a NEW EMPTY folder under your `.scratch/r20/` (write the URL to a file and read it from Python run with `-I`); check its sha256 base64 equals the CodeSha256; `live_member_manifest` = member name -> sha256 for every file member.
2. **Find the base commit `B`.** A throwaway worktree OUTSIDE the product tree, DETACHED, at a commit whose map builds the live package with NO patch: `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting <fn>` must print the live CodeSha256 (that is the holds-only control; it reproduced the live CodeSha256 byte for byte under AR-y-201). Candidates, in order: the map entry's `last_deployed_commit` and its parent; `e274a0e60c` and `69679b90e3` (act 4's re-pin and flip commits); `5d8b0390ed` (release 19's base); then `git log` over the function's staged paths. Copy each zip at once (the script writes one fixed temp path). If no candidate reproduces the live CodeSha256 after you have tried five, STOP for that function: record which members differ and file a BLOCKING row; do NOT widen.
3. **The release patch.** At `B`, move ONLY the `served.py` row's pin (`repo_path infra/aws/lambda/investor-reporting/_authz/served.py`) to `served_pin`, the latest trunk commit that touched that path (`git log -1 --format=%H -- infra/aws/lambda/investor-reporting/_authz/served.py` at your worktree's HEAD), with its `sha256`. Save `r20/<fn>.release.diff` (git diff of the map only; the trunk map is NOT edited) and print `git hash-object`. BUILD_ONLY. Compare its members with the live manifest: the release must differ in `served.py` and in NOTHING else, unless the new `served.py` cannot be imported without another member at a newer version: then name each such member in `must_move_with` with `reason` (the import line) and do NOT move any other.
4. **Does the rule ship?** Extract the release zip to a scratch folder; `carries_status_rule` is true only if its `served.py` contains the rule markers (`AR-y-172`, `row.get("status") != "active"`, `no users row for an internal caller`) and imports with `PYTHONPATH` set to the extracted folder. Then run the function's own test folder with the release `served.py` staged in place of the head one (narrative's suite does this by staging; for the others, stage it the same way, in a scratch copy), and the two `_authz` tests `test_internal_status_active.py` and `test_caller_class_log.py` against the packaged `served.py`. Record `tests` per function: `folder`, `passed`, `failed`, `staging` (words).
5. **narrative only (group A):** its tests stage the PINNED `served.py` and cannot see the rule (row W54-S5). Move the staging in `infra/aws/lambda/investor-reporting/narrative/tests/` to the new pin, commit it in your branch, and say which test file changed; the suite must pass with the rule in force.
6. **Write the record** (path in the criterion): `served_pin`, `served_blob_sha256`, `functions` (one object per function: `function`, `live_code_sha256`, `live_member_manifest`, `base_commit`, `holds_only_control` {`code_sha256`, `differs_from_live`}, `release` {`code_sha256_b64`, `package_sha256`, `member_manifest`, `differs_from_live`}, `must_move_with`, `carries_status_rule`, `tests`, `patch` {`path`, `git_hash_object`}), `claim`, `not_read`.
7. **In your report:** per function one line: live CodeSha256 prefix, the base commit, the holds-only control result, the members that differ, the tests.

**Your functions (group A):** `irpt-performance-adapter`, `irpt-narrative`, `irpt-status`. The record is `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~61/r20/STATUS_RULE_REBASE_GROUP_A.json`.

### ACCEPTANCE

<criterion id="AR212-y-AC1" cell_refs="AR-y-212"><invocation>python C:/dev/wk-irpt-anlreq-61/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r20/ar20_checks.py y212-rebase --root C:/dev/wk-irpt-anlreq-61</invocation><expect>Y212-REBASE-OK</expect></criterion>
`AR212-y-AC1`: for every function of the group the record holds the live read, a holds-only control that reproduces the live CodeSha256, a release that differs from the live package in `served.py` and in nothing else (but members named in `must_move_with` with a reason), the status rule in the release's `served.py`, and the function's tests passing against it.

<criterion id="AR212-y-AC2J" cell_refs="AR-y-212" judgment="true"/>
`AR212-y-AC2J` (judgment, graded at L9, never by you): the live packages were read from AWS in this run and not taken from a record, each base commit was proved by a holds-only build that equals the live CodeSha256, the release moves nothing but `served.py` (and what it cannot import without), and the tests ran against the packaged `served.py`.

<expected_criteria>AR212-y-AC1 AR212-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~61/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
infra/aws/lambda/investor-reporting/narrative/tests/
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R20_Y.md</decomp_doc>
<owned_cells>AR-y-212</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~61/IRPT_ANLREQ.TO-AR-y-212.status-rule-rebase-a.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-212`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> <the criterion ids>`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- read-only `get-function` and zip downloads, local BUILD_ONLY builds in throwaway worktrees outside the product tree; nothing is uploaded, deployed, applied or called with a write.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading release 19 (the live package had changed under the census) against the cell; the lens: a hold or base taken from a record and not from the live bytes, or a release compared with another build and not with the live package. The order requires the live read in this run and a holds-only build that reproduces the live CodeSha256 before any release is built. NOT seen: the Lambdas' configuration, and whether the functions' tests exercise the packaged `served.py` beyond what the staging covers.
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-20 analysis (the status rule's all-eight pair) as round 20 workstream `Y`, split by pin group. Base: `AR212-y-AC1` FAIL as expected (no record).
- The PAIR and the APPLY are not this order.
