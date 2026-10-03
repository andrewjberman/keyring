# NFRA_OPLGTW task order -- `OG-ts-1` -- the grant writer's tests run against the pinned staged closure (row Z-W26-S4)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ts-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~25</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a test-harness change; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE -- the requirement is row Z-W26-S4 graduated by the CVO (ADJUDICATION_v5.Z C-S19) and listed by the CTO (round-15 analysis item 4).
EGRESS CLASS, declared: NONE -- local git and files.
</preflight>

## 1. THE CELL -- `OG-ts-1` (decomposition addendum R3-T.9, item 4)

Row Z-W26-S4: `infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/tests/conftest.py` puts HEAD's gateway tree on
`sys.path`. So the writer's tests grade code the Lambda does not ship. The Lambda ships the closure `build_package.py`
stages from the manifest's `deployed_commit` (your OG-gw-1).

1. `conftest.py` stages the closure ONCE per session with `build_package.py` into a temporary directory (`--stage-dir`,
   your flag), and puts THAT directory first on `sys.path`. It never imports from the working tree's
   `infra/aws/ec2/opal-gateway/app`. If staging fails, the session errors with the builder's reason.
2. New `tests/test_closure_under_test.py` with exactly `test_ogts1_ac01`. It asserts that the imported `app.config`,
   `app.data_entitlement` and the loaded contract JSON are the STAGED bytes (sha256 of `__file__` / the contract path
   equals the staged copy), not the working tree's.
3. The whole existing suite passes against the staged closure, and the run leaves no tracked file dirty.

## 2. BOUNDS

- **Edit ONLY:** `tests/conftest.py` and the new test file.
- **Untouched:** `build_package.py` and the Lambda.
- **No** deploy and no AWS call.
- **Never:** push, merge, rebase, stash, `checkout --` or `clean`; override a gate.

## 3. SURFACES

<paths>
infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/tests/conftest.py
infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/tests/test_closure_under_test.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~25/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W25-S<k>` (next unused), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ts-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r16/checks/ts1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)suite rc=0; test_ogts1_ac01 passed 1 of 1; failed/error lines 0; tracked files dirty after the run 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~25/NFRA_OPLGTW.TO-OG-ts-1.grant-writer-tests-on-closure.proof_of_spec.json`.
2. Validate it with `python .tools/proof-of-spec-check.py <instance>`.
3. If AC1 PASSes, edit this order's ONE `<status>` tag IN PLACE to `complete`, in the same commit. Never append a second
   tag.
4. Report once: the diff, the literal AC output, commits and rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round label 16 (addendum R3-T.9, item 4). Alone in its chain. Pre-cut 22:1xZ: `ts1.AC1` FAIL (test absent).

<status>pending</status>
<round>16</round>
<slot>~25</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
