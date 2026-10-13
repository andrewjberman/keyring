# TO IRPT_BCKEND.TO-IB-pr-505 -- the builder validates its own snapshot against the repository's v1 schema before it writes, and a planted member refuses the build (row D2-W354-S2; CTO round-174 analysis section 1)

<to_id>IRPT_BCKEND.TO-IB-pr-505</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~356</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>174</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO ROUND-174 ANALYSIS (msg 6812) section 1 (row D2-W354-S2) and section 2 item 1 | **Decomp cell:** `IB-pr-505` (decomposition section 166) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Cell `IB-pr-505` (inlined):** the live `irpt-holdings` function validates nothing at serve (round 172 and 173), so the contract is enforced at BUILD. The CTO's ruling: the builder validates its own output against the repository's v1 `HoldingsSnapshot` schema before it writes, so a stray member fails the build and never reaches a client; one test plants an unknown member and the build refuses. **The issuer's read of the code says most of this is already so:** `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` has `validate_snapshot(snapshot)` (about `:2824`, jsonschema against `CONTRACT_PATH` = `docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json`), called in the build `main` path (about `:3133`, before the refusal logic that follows) and as the `validate=` hook of `land` (about `:2881`). What is missing is the PROOF: no test plants an unknown ACCOUNT-node member and shows the build refuses and writes nothing. **Read the build path, then add that proof.** BUILD ONLY: no deploy, no AWS call, no run of the live builder. Synthetic data only; client data stays out of every file.

**Do:**
1. READ the build path from `main` down to the first write: find every place the snapshot is validated before anything is put to S3 (the `validate_snapshot` call in `main`, the `validate=` hook in `land`, and any other), and what each does on an invalid snapshot (raise, return a refusal, or continue). Cite each as `file`, `line` and an exact one-line `quote`. Cover BOTH builders that write a `HoldingsSnapshot` (`holdings_49f.py` and `holdings_inf.py`) by following what each returns into `main`; say in the record if either reaches a write without passing `validate_snapshot`.
2. Write the new test file `data/assets/scripts/gold/investor_reporting/tests/test_build_refuses_planted_member.py`, at least THREE arms, synthetic data only (see how `tests/test_holdings_publish_gate.py`, `tests/test_holdings_49f.py` and `tests/test_runner_jsonschema_tolerance.py` stub the builder, the publisher and the contract fixture `infra/aws/lambda/investor-reporting/_contracts/fixtures/HoldingsSnapshot.valid.json`, key `instance`): (a) a snapshot whose ACCOUNT node carries a planted unknown member makes the build REFUSE, through `main` or `land` as it really runs, with a stub S3/publisher that records every put: ZERO puts; (b) the same snapshot without the planted member and with the optional `account_id` member on the ACCOUNT node validates and the build proceeds to its writes (puts recorded on the stub); (c) the error line for (a) names the planted member. Do not edit any existing test.
3. If the read shows a path that reaches a write WITHOUT validation, STOP, file a row, and change nothing in `holdings_snapshot.py` (the order grants no product-code edit unless the issuer amends it).
4. Write the record `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~356/IB174-1_build_validation_read.json`:
`{"call_sites":[{"file":"...","line":N,"quote":"..."}],"refuses_on_invalid":true,"refusal":{"file":"...","line":N,"quote":"..."},"builders_covered":["holdings_49f","holdings_inf"],"unvalidated_write_paths":[],"functions_invoked":0,"aws_writes_made":0}`
(`refusal` is the line that stops the build on an invalid snapshot; `unvalidated_write_paths` lists any write path found without validation, empty if none.)

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB174-1-AC1" cell_refs="IB-pr-505"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r174/p174_cells.py" . IB174-1-AC1</invocation><expect>IB174-1-AC1 PASS</expect></criterion>
<criterion id="IB174-1-AC2" cell_refs="IB-pr-505"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r174/p174_cells.py" . IB174-1-AC2</invocation><expect>IB174-1-AC2 PASS</expect></criterion>
<criterion id="IB174-1-AC3" cell_refs="IB-pr-505"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r174/p174_cells.py" . IB174-1-AC3</invocation><expect>IB174-1-AC3 PASS</expect></criterion>

<expected_criteria>IB174-1-AC1, IB174-1-AC2, IB174-1-AC3</expected_criteria>

What the checks grade: AC1 your new test file passes (3 or more, none failed); AC2 the issuer's own probe: the valid fixture validates with and without `account_id` and a planted ACCOUNT-node member is refused with an error naming it (this one already reads PASS at the base: it is a regression guard on the validator, not a progress mark); AC3 your record: at least two validation call sites resolve (file exists, quote within 3 lines of the line), `refuses_on_invalid` true and the refusing line cited. Do not edit the checks. Run `python -m pytest data/assets/scripts/gold/investor_reporting/tests/test_holdings_49f.py data/assets/scripts/gold/investor_reporting/tests/test_holdings_inf.py data/assets/scripts/gold/investor_reporting/tests/test_runner_jsonschema_tolerance.py -q` ONCE at the end and report; do NOT run the whole `tests/` folder (one test in it makes live read-only AWS calls).

## BOUNDS

- **Grant:** the `paths` block and nothing else. No deploy, no AWS call, no run of the live builder, no edit of an existing test, no edit of `holdings_snapshot.py`, `holdings_49f.py` or `holdings_inf.py` (a gap found there is a ROW, not an edit).
- **Refusal clause:** STOP, file a row, change nothing more, if a write path reaches S3 without `validate_snapshot` (name it), or the build cannot be exercised without an AWS call or a secret.
- **Row ids** are `IRPT_BCKEND-D2-W356-S<k>` (the next free `k`). **Commit** on your worktree branch per your definition with `.tools/safe-commit.sh`; ASCII only. Report once, under 150 words.

<paths>
data/assets/scripts/gold/investor_reporting/tests/test_build_refuses_planted_member.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~356/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-505.builder-refuses-a-planted-member-at-build.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 166 (round 174, workstream ~P), cell `IB-pr-505`.
<owned_cells>IB-pr-505</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB174-1-AC1, IB174-1-AC2, IB174-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~356/IRPT_BCKEND.TO-IB-pr-505.builder-refuses-a-planted-member-at-build.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a new test and a read of gold-runner code (an SSM host bundle, in no Lambda's members); nothing is deployed from this order.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p174_cells.py dry-run at base on dell2 2026-10-13 ~05:5xZ: IB174-1 AC1 FAIL (no test file), AC3 FAIL (no record); AC2 PASS at the base (the validator already refuses a planted ACCOUNT-node member: a regression guard). The contract line "enforced at build; not at serve" is the PRD's (the schema is generated from the PRD CONTRACTS table): the issuer sends it to the CTO, it is not in this grant.
lane: the paths block IS the grant; worker slot ~356 of IRPT_BCKEND. Class LOCAL.
</preflight>
