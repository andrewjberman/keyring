# NFRA_OPLGTW task order -- `OG-en-27` -- `test_og_db3.py::test_ogdb3_ac03` reads the worktree, not git history, so it passes in a release tree (round 42; CTO round-41 analysis item 2, `ROUND_ANALYSIS.round41.md`)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-en-27</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-en-27</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~142</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one offline test file; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-41 analysis item 2 (a test defect carried by name since `OG-ap-36`).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-en-27` (decomposition addendum R3-T.119, round 42, workstream ENRICH-R42-A)

THE DEFECT. `infra/aws/ec2/opal-gateway/tests/test_og_db3.py::test_ogdb3_ac03` (read the whole file; its other two tests are fine) finds the worker commit that first touched `deploy-to-ec2.sh` by `git log --author=...`, diffs the file against that commit's parent with `difflib`, and asserts the change was ONE pure insertion of exactly two lines (a comment starting `# OG-db-3`, then the marker code line), placed right after `TAR_LINE`. A release branch cut from the live ref cannot hold that worker commit, so the test FAILS in every release tree and passes only on trunk.

THE FIX (the test file only): make `test_ogdb3_ac03` read the WORKTREE and nothing else. Keep what it protects, as assertions on the CURRENT text of `deploy-to-ec2.sh` (use the file's own `_lines()` and `_marker_index()` helpers): (1) there is exactly one `TAR_LINE`; (2) the single non-comment line naming `deployed_commit` (the marker line) comes after it; (3) the line immediately before the marker line is a comment that starts with `# OG-db-3`; (4) the marker line is not the tar line and the comment is not blank. Remove every `git` call from the body of `test_ogdb3_ac03` (the helper `_git` may stay if another test uses it; if none does, delete it and the unused imports). Do NOT change `test_ogdb3_ac01` or `test_ogdb3_ac02`, and do NOT touch `deploy-to-ec2.sh`.

## 2. BOUNDS

- Write only the files in `<paths>`. No release, no deploy, no product code, no IAM, no env key.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; weaken a test; print a secret or a client value.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/tests/test_og_db3.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You WRITE `tests/test_og_db3.py`; the rest you only READ. `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~142/`. Rows: id `NFRA_OPLGTW-Z-W142-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-en-27"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r42/checks/en27.AC1.sh; echo "exit=$?"</invocation><expect>(?s)copy outside any git repository: in a repo no \(want no\); pytest rc=0; the three db3 tests passed 3 of 3; git tokens in the body of test_ogdb3_ac03: none \(want none\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-en-27"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_wkbound.sh 0.9.0_WK_NFRA_OPLGTW~142 '^infra/aws/ec2/opal-gateway/tests/test_og_db3\.py$'; echo "exit=$?"</invocation><expect>(?s)write-set bound for 0\.9\.0_WK_NFRA_OPLGTW~142: files touched [1-9]\d*; product files 1; outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-en-27"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_named.sh tests/test_og_db3.py test_ogdb3_ac01 test_ogdb3_ac02 test_ogdb3_ac03; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 3 of 3; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the three tests pass in a copy of the test file and the deploy script placed OUTSIDE any git repository (the old `ac03` fails there), and the body of `test_ogdb3_ac03` holds no `git` token. `AC2`: your commits touch only the test file. `AC3`: the same three tests pass in the repository.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-en-27.round-42-db3-test-reads-the-worktree.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if all three PASS, and report once (commit hash, the AC lines).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 42, workstream ENRICH-R42-A (decomposition addendum R3-T.119). A test-only cell of the batched release `OG-ap-39`. Carried since `OG-ap-36` as a test defect, not a code defect (nothing runs the suite on the host).
- Pre-cut: `AC1` base FAIL as expected (the old `ac03` shells out to git and holds `git` in its body); `AC3` passes at the base in the repository (the history exists on trunk), which is why `AC1` is the real oracle.

<status>complete</status>
<round>42</round>
<workstream>ENRICH-R42-A</workstream>
<slot>~142</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
