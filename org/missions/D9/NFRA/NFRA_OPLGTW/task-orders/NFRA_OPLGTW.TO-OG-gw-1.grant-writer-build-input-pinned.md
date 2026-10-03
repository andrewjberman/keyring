# NFRA_OPLGTW task order -- `OG-gw-1` -- the grant writer's build input is pinned to the gateway's released ref

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-gw-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~25</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a build-script change; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM, no AWS call; the builder reads git and the manifest.
comp-adversary: DECLARED-NOT-APPLICABLE -- the mechanism is the CTO's ruling R1 (ledger/ROUND_ANALYSIS.round14.md @cf6e539a6d).
EGRESS CLASS, declared: NONE -- local git and files only.
</preflight>

## 1. THE CELL -- `OG-gw-1` (decomposition addendum R3-T.8, item 1)

**What is wrong today.** `infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/build_package.py` stages the import
closure of `app.access_state` and `ops.schwab_entitlement_admin`, plus its data files, from the WORKING CHECKOUT into
`.build/staged/`. Terraform's `archive_file` then zips that directory. So every unreleased gateway edit to `app.config`,
`app.data_entitlement` or the contract JSON changes the grant writer's package.

Measured (`deliverables/0.9.0_WK_NFRA_OPLGTW~17/TF_ROOT_FIX.md` s.1): the deployed zip differs from HEAD's build in 3 of
11 files. The live GATEWAY runs the release branch, not CLOUD HEAD: `af2d762970`, which is not an ancestor of HEAD.

**The CTO's ruling R1:** stage from the gateway's RELEASED ref -- `infra/aws/ec2/EC2_MANIFEST.json`
`services.opal-gateway.deployed_commit` -- through a detached worktree or `git archive`, never the working checkout.
Reuse the pattern `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh` already uses for `mcportal_commit` (read it first).

1. `build_package.py`:
   - reads `deployed_commit` from the manifest at the repo root;
   - resolves the closure and the data files from THAT commit's bytes, via `git show <commit>:<path>`, `git archive` or a
     temporary detached worktree that it removes;
   - writes them into `.build/staged/` exactly as today, so the `archive_file` contract is unchanged.
   The derivation (the `ast` walk) runs over the commit's bytes, not the checkout's. A missing manifest, a missing key or
   an unresolvable commit REFUSES (non-zero, a one-line reason) before anything is staged. Print the commit it staged
   from (short sha) as one line.
2. New `tests/test_build_input_pinned.py` with exactly these tests (no network; temporary git repos or the real repo
   read-only):
   - `test_oggw1_ac01`: every staged file's bytes equal `git show <deployed_commit>:<repo path>`;
   - `test_oggw1_ac02`: a planted uncommitted edit to a closure file (for example a comment appended to
     `infra/aws/ec2/opal-gateway/app/config.py`) does NOT appear in the staged output. The test restores the file and
     leaves the tree clean, which the check verifies;
   - `test_oggw1_ac03`: a manifest naming an unresolvable commit makes `build_package.py` exit non-zero with nothing
     staged.
3. `.gitignore` in the grant writer's directory gains `.build/` (row Z-W17-S3: `.build/staged` is untracked and not
   ignored).

## 2. BOUNDS

- **Edit ONLY:** `build_package.py`, the new test file and the grant writer's `.gitignore`.
- **Out of scope here:**
  - Terraform, deploys and AWS calls (`OG-gw-2` applies);
  - the gateway tree, which is read, never written.
- **Never:** push, merge, rebase, stash, `checkout --` or `clean`; override a gate.
- Every `.py` edit passes `.tools/commit-gate.sh`; commit with `.tools/safe-commit.sh`.

## 3. SURFACES

<paths>
infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/build_package.py
infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/tests/test_build_input_pinned.py
infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/.gitignore
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~25/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W25-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-gw-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r15/checks/gw.AC1.sh; echo "exit=$?"</invocation><expect>(?s)named tests passed 3 of 3; failed/error lines 0.*dirty under the grant writer after the run: 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-gw-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r15/checks/gw.AC2.sh; echo "exit=$?"</invocation><expect>(?s)outside the allowed three: 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the three named tests pass and the run leaves no tracked file dirty.
- `AC2`: the cell's commits touch only the three named files.

## 5. WHEN YOU ARE DONE

1. Write the proof instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~25/NFRA_OPLGTW.TO-OG-gw-1.grant-writer-build-input-pinned.proof_of_spec.json`.
2. Validate it with `python .tools/proof-of-spec-check.py <instance>`.
3. If both criteria PASS, append a `complete` status tag after the order's last status line, in the same commit.
4. Report once: the diff summary, the literal AC output, commits and rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round label 15 (addendum R3-T.8, item 1); feeds `OG-gw-2`. Pre-cut 18:2xZ: `gw.AC1` FAIL (test file absent);
  `gw.AC2` FAIL (0 files); `gw2.AC1` FAIL with 3 DIFF (config.py, data_entitlement.py, the contract JSON), the
  measurement OG-tf-1 made.

<status>pending</status>
<round>15</round>
<slot>~25</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
