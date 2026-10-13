# TO IRPT_BCKEND.TO-IB-pr-496 -- the 49F builder leaves no Tax-snapshot temp file; raw_keys.json cites the live mint (rows D2-W345-S3, D2-W344-S2)

<to_id>IRPT_BCKEND.TO-IB-pr-496</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~347</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>171</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO ROUND-171 ANALYSIS (msg 6764) section 1 (rows D2-W345-S3, FIRST, and D2-W344-S2) and section 2 item 1 | **Decomp cell:** `IB-pr-496` (decomposition section 163) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Cell `IB-pr-496` (inlined):** every live 49 Financial build copies the Tax membership snapshot, which carries client account numbers, to a system temp file and never removes it. `data/assets/scripts/gold/investor_reporting/holdings_49f.py` `build_49f_meshed` (:633) calls `holdings_snapshot.retained_capture(...)` (`holdings_snapshot.py:1266`), which, when the operator's env var `IRPT_49F_TAX_MEMBERSHIP_SNAPSHOT` is unset, reads the snapshot object with the build's own `s3` and writes its bytes with `tempfile.mkstemp(suffix="-" + obj)` and returns that path; nothing removes it, so a build that returns AND a build that raises both leave one account-bearing file. **BUILD ONLY: no deploy, no AWS call, no run of the live builder. Client data stays out of every file.**

**Fix it, in `holdings_49f.py` and/or `holdings_snapshot.py` (your choice of the smaller edit; no other module):** the builder either reads the snapshot in memory, or removes the file it created in a `finally` that runs on return AND on a raise. A file the OPERATOR supplied through the env var is NEVER removed (it is theirs): remove only a file the builder itself created. Read `build_49f_meshed` (:603-650) and `retained_capture` (:1266-1290) and every other caller of `retained_capture` (`grep` the gold-runner tree; if another caller leaks the same way, fix it the same way and say so).

**Also, in `infra/aws/lambda/investor-reporting/_ids/raw_keys.json`:** `firms.49financial.account.holdings_source` still names `smartx/platform/silver/fact_allocation_account_map.account_number, zero-padded by holdings_snapshot._pad10`, while the live builder mints the ACCOUNT node id from the Schwab custody key `dim_balance.account_id` (`holdings_49f.py:339`). Correct the declared key: name `dim_balance.account_id` (Schwab custody master) as the source, cite `holdings_49f.py:339`, and say the node's `account_id` member (merged: IB-pr-493) is the directory's id. Keep the file valid JSON; keep every other key (including `node_account_id_member`) unchanged.

**Your NEW test file** `data/assets/scripts/gold/investor_reporting/tests/test_retained_capture_cleanup.py`, at least THREE arms, synthetic data only (a stub `s3` whose `get_object` returns a tiny JSON; monkeypatch `holdings_snapshot._latest_date_partition`; see how `tests/test_holdings_49f.py` stubs the builder): a build that raises leaves no new file ending `-taxsma_workbook_projected_snapshot.json` in `tempfile.gettempdir()`; a build that returns leaves none; a file the operator supplied through the env var survives the build.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB171-1-AC1" cell_refs="IB-pr-496"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r171/p171_cells.py" . IB171-1-AC1</invocation><expect>IB171-1-AC1 PASS</expect></criterion>
<criterion id="IB171-1-AC2" cell_refs="IB-pr-496"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r171/p171_cells.py" . IB171-1-AC2</invocation><expect>IB171-1-AC2 PASS</expect></criterion>
<criterion id="IB171-1-AC3" cell_refs="IB-pr-496"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r171/p171_cells.py" . IB171-1-AC3</invocation><expect>IB171-1-AC3 PASS</expect></criterion>

<expected_criteria>IB171-1-AC1, IB171-1-AC2, IB171-1-AC3</expected_criteria>

What the checks grade: AC1 your new test file passes (3 or more, none failed); AC2 the issuer's seam probe on stubs: a build that raises, a build that returns, and an operator-owned env-var file (kept) leave no builder-created snapshot temp file; AC3 `raw_keys.json`'s `holdings_source` cites `dim_balance` and `holdings_49f` and no longer names the smartx map. Do not edit the checks. Existing tests: run `data/assets/scripts/gold/investor_reporting/tests/test_holdings_49f.py` ONCE at the end (22 pass at base) and report; do NOT run the whole `tests/` folder (one test in it makes live read-only AWS calls).

## BOUNDS

- **Grant:** the `paths` block and nothing else. No deploy, no AWS call, no run of the live builder, no edit of an existing test.
- **Refusal clause:** STOP, file a row, change nothing more, if the leak cannot be closed without changing the builder's returned values or its path-based reader's contract, or if you find a caller that must keep the file after the build returns (say which).
- **Row ids** are `IRPT_BCKEND-D2-W347-S<k>` (the next free `k`). **Commit** on your worktree branch per your definition; ASCII only. Report once, under 150 words.

<paths>
data/assets/scripts/gold/investor_reporting/holdings_49f.py
data/assets/scripts/gold/investor_reporting/holdings_snapshot.py
data/assets/scripts/gold/investor_reporting/tests/test_retained_capture_cleanup.py
infra/aws/lambda/investor-reporting/_ids/raw_keys.json
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~347/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-496.builder-temp-file-and-raw-keys-citation.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 163 (round 171, workstream ~P), cell `IB-pr-496`.
<owned_cells>IB-pr-496</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB171-1-AC1, IB171-1-AC2, IB171-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~347/IRPT_BCKEND.TO-IB-pr-496.builder-temp-file-and-raw-keys-citation.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- BUILD ONLY. Gold-runner code (an SSM host bundle, in no Lambda's members) and `raw_keys.json` (a member of Lambdas that ship it: this order edits a DECLARED-KEY text field only; any release of `raw_keys.json` rides a later pair); nothing is deployed from this order.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p171_cells.py dry-run at base on dell2 2026-10-13 ~04:0xZ: IB171-1 AC1 FAIL (no test file), AC2 FAIL ("a build that raises leaves 1 Tax-snapshot temp file(s) behind": the leak, reproduced offline with a stub s3 and cleaned up), AC3 FAIL (holdings_source names the smartx map). The base tests of `test_holdings_49f.py` pass (22).
lane: the paths block IS the grant; worker slot ~347 of IRPT_BCKEND. Class WORLD (the `infra/` floor).
</preflight>
