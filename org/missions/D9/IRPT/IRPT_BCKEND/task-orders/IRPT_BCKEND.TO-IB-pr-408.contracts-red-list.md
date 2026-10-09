# TO IRPT_BCKEND.TO-IB-pr-408 -- the investor-reporting _contracts red list: bisect each red test to the cell that broke it, then fix it or name it with its owner and expected green commit

<to_id>IRPT_BCKEND.TO-IB-pr-408</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~271</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>109</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO ADDENDUM 18 (msg 3272; `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUNDS_75_76_P_64_Y_20261008.md`), row D2-S46 | **Decomp cell:** `IB-pr-408` (decomposition section 102) | **outcome_ref:** FWD-2

---

## WORKER FACE

**The cell.** At box/dell2 HEAD, `pytest _contracts -rf` (root `C:/dev/wk-irpt-bckend-271/infra/aws/lambda/investor-reporting/`) reads
9 failed, 176 passed, 13 skipped. Known members include:
- `test_owned_request_contracts.py::test_public_routes_are_declared_against_the_installed_status_handler`, `assert 21 == 22`, which follows
  IRPT_ANLREQ AR-y-22's `/original` route;
- `test_upload_contract.py::test_route_denominators_are_measured_and_upload_is_declared_against_generate`;
- several `tests/test_seam_paired.py` cases, where export-receipt and submit-export fixtures lack `covered_account_ids`.

The CTO gave this list ONE owner. Until it is empty or every entry is named, no investor-reporting release packet may say "suite green".

1. **Record the base.** Note `git rev-parse HEAD` and the exact failing node ids (`base_red`).
2. **Bisect each red test** to its first failing commit. Use `git bisect` or a scripted walk over `git log` on the files the test reads,
   running only that test. Name the cell (the TO id or the `cell` in the commit subject) and its owner (the issuing COO serial). Run
   bisects in a SEPARATE scratch worktree outside this one, e.g. `git worktree add C:/dev/_bisect271 <rev>`. Remove it at the end
   with `git worktree remove`; that is not a recursive delete.
3. **Fix it, or name it.**
   - **FIX** only when the fix sits inside your grant and changes no product code. Examples: a stale count or fixture in `_contracts/`,
     or a missing contract declaration in `docs/contracts/investor-reporting/v1/` that the shipped code already serves. A fix never
     weakens what a test asserts.
   - Otherwise **NAME** it: the breaking cell, its owner, and `expected_green` (the order or commit expected to turn it green, or
     `"owner to state"` if none is on record).
4. **Write** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~271/IB109-1_contracts_red_list.json` as
   `{base, base_red:[...], entries:[{test, first_red_commit, cell, owner, disposition, expected_green?, note}]}`. `test` is the node id
   exactly as pytest prints it.

<criterion id="IB109-1-AC1" cell_refs="IB-pr-408"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r109/p109_cells.py" . IB109-1-AC1</invocation><expect>IB109-1-AC1 PASS</expect></criterion>
<criterion id="IB109-1-AC2" cell_refs="IB-pr-408"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r109/p109_cells.py" . IB109-1-AC2</invocation><expect>IB109-1-AC2 PASS</expect></criterion>

<expected_criteria>IB109-1-AC1, IB109-1-AC2</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No product code, no deploy.
- **Every `.py` edit passes `.tools/commit-gate.sh`**; safe-commit runs it.
- **Refusal clause:** if a criterion cannot be met as written, stop, file a row, and report. Never weaken a check or a test.
- **Row ids** are `IRPT_BCKEND-D2-W271-S<k>`; `surfaced_at` is the real time; check the id is still free just before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~271" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~271@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~271 <0.9.0_WK_IRPT_BCKEND~271@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools.

<paths>
infra/aws/lambda/investor-reporting/_contracts/
docs/contracts/investor-reporting/v1/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~271/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-408.contracts-red-list.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 102 (round 109, workstream ~P), cell `IB-pr-408`.
<owned_cells>IB-pr-408</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB109-1-AC1, IB109-1-AC2. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~271/IRPT_BCKEND.TO-IB-pr-408.contracts-red-list.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message, give the base, the red list (test, breaking cell, owner, disposition), what you fixed, each criterion's last line and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- contract tests, fixtures and contract documents only; FIX limited to stale tests/fixtures/declarations that shipped code already serves; no product code, no deploy.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route added or removed; at most a contract declaration of an already-served route.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p109_cells.py dry-run at base box/dell2 on dell2 2026-10-09 ~12:3xZ: AC1 and AC2 FAIL (no red list); 0 control bytes; ruff clean.
lane: the <paths> block IS the grant; ~P's (CTO ADDENDUM 18: one owner, 2.0.0_SA_COO~P2).
</preflight>
