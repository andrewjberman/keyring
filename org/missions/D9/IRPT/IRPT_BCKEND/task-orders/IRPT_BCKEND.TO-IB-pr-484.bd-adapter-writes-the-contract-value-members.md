# TO IRPT_BCKEND.TO-IB-pr-484 -- BUILD ONLY: `bd_adapter.py` writes `start_value` and `end_value` (C-VALUEFACTS), not `beginning_market_value` and `ending_market_value`

<to_id>IRPT_BCKEND.TO-IB-pr-484</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~339</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>167</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 6517 (PRD ADDENDUM v0.51 section 2 item 3, step 2; contract C-VALUEFACTS, ADDENDUM v0.50 line 1320) | **Decomp cell:** `IB-pr-484` (decomposition section 159) | **outcome_ref:** FWD-3

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-339/` (bash `/c/dev/wk-irpt-bckend-339`). Work only there; `git rev-parse HEAD` before your first commit is `base_commit` (state it).

**HARD BOUNDS.** BUILD ONLY. No AWS call, no Lambda invoked, no route called, nobody signs in, nothing deployed. Every value in a test is SYNTHETIC; no real account, client or figure in any file.

**Why.** PRD ADDENDUM v0.50 (C-VALUEFACTS, line 1320 of `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md`; read it whole): `optional_facts.value_facts`, when not null, carries `start_value` and `end_value`, as three emitters write them; no other spelling is a member. `infra/aws/lambda/investor-reporting/performance/bd_adapter.py` (about lines 192-195) alone writes `beginning_market_value` and `ending_market_value`.
It is step 2 of ONE pair (the portal adapter reads the contract members first, in another order of this round; the portal keeps a market-value read for the Black Diamond path until THIS rename is live). This order renames the two keys in the producer and nothing else. It moves a served member name, so it ships later under a never-widen pair; it is not applied here.
Worker ~334's record `deliverables/0.9.0_WK_IRPT_BCKEND~334/IB166-4_value_facts_readers.json` found no in-repo backend reader of the market-value names; verify that yourself.

**Build (one thing).** In `bd_adapter.py`, write the opening value under `start_value` and the closing value under `end_value` in `value_facts`, with the SAME values the old keys carried; every other member, the `value_facts is None` guard, the claim and the window are unchanged. Search `infra/aws/lambda/investor-reporting/` for every READER of the two old names (tests, normalize, narrative, fixtures; the native Grep tool, with its denominator printed) and update each in-repo reader that your rename would break, naming it in the record. Do NOT edit any other emitter (`holdings_gold.py`, `f49_engine.py`, `orion_adapter.py` already conform).

**Tests (the build's own):** `infra/aws/lambda/investor-reporting/performance/tests/test_bd_value_members.py`, at least THREE tests over synthetic inputs: (1) the adapter's `value_facts` carries `start_value` and `end_value` with the values the old keys carried for the same input; (2) it carries NO `beginning_market_value` or `ending_market_value`; (3) the `value_facts is None` case still writes nothing. Run the whole performance folder before and after: it reads `274 passed, 1 failed` at base (the failure is the known calendar test `test_the_fallback_calendar_is_graded_in_its_own_years_and_clipped_outside_them`, not yours); after, no new failure and at least 274 passed.

**Record** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~339/IB167-4_bd_rename_record.json`: `{base_commit, files_changed, renamed:[{from:"beginning_market_value", to:"start_value"},{from:"ending_market_value", to:"end_value"}], in_repo_readers_of_the_old_names:[{cite, reads, what_you_did}] (an empty list if none), reader_census:{pattern, files_searched, files_with_a_hit}, hash_pins:[every place in the repo that pins a hash of a file you changed, with what you did],
host_reach (which Lambda package carries bd_adapter.py: read lambda-source-map.json; nothing is built here), suites:{performance_before, performance_after}, deployed:false}`.

<criterion id="IB167-4-AC1" cell_refs="IB-pr-484"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r167/p167_cells.py" . IB167-4-AC1</invocation><expect>IB167-4-AC1 PASS</expect></criterion>
<criterion id="IB167-4-AC2" cell_refs="IB-pr-484"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r167/p167_cells.py" . IB167-4-AC2</invocation><expect>IB167-4-AC2 PASS</expect></criterion>
<criterion id="IB167-4-AC3" cell_refs="IB-pr-484"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r167/p167_cells.py" . IB167-4-AC3</invocation><expect>IB167-4-AC3 PASS</expect></criterion>

<expected_criteria>IB167-4-AC1, IB167-4-AC2, IB167-4-AC3</expected_criteria>

What the checks grade: AC1 your new test file exists and at least 3 tests pass; AC2 the regression guard (it PASSes at base BY DESIGN): the performance folder reads at least 274 passed and at most the one known failure; AC3 the record: exactly the two renames, `bd_adapter.py` no longer keys either old name, every listed old-name reader cite resolves, and nothing outside `performance/bd_adapter.py`, `performance/tests/`, your deliverables, rows and order changed.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else.
- **Refusal clause:** an in-repo reader of the old names outside `performance/tests/`, or a test you cannot update without weakening it: file a row and report; do not weaken a test. Never weaken a check; do not edit `p167_cells.py`.
- **Hash pins:** list every place that pins a hash of `bd_adapter.py`; regenerate one only if it is inside your `<paths>` and is a generated record of those bytes.
- **Row ids** are `IRPT_BCKEND-D2-W339-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or `INFERRED`; append only, keeping the channel file's line endings byte for byte; check the id is free before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~339" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~339@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~339 <0.9.0_WK_IRPT_BCKEND~339@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
infra/aws/lambda/investor-reporting/performance/bd_adapter.py
infra/aws/lambda/investor-reporting/performance/tests/
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~339/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-484.bd-adapter-writes-the-contract-value-members.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 159 (round 167, workstream ~P), cell `IB-pr-484`.
<owned_cells>IB-pr-484</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB167-4-AC1, IB167-4-AC2, IB167-4-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~339/IRPT_BCKEND.TO-IB-pr-484.bd-adapter-writes-the-contract-value-members.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the base; the rename in a sentence; the in-repo readers of the old names and what you did; the census and its denominator; the new test's arms; the performance folder's last line before and after; the hash pins found and what you did; each criterion's last line; the proof checker's result; commit hashes; row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; the cell renames two keys in one producer file in the repo; nothing is built, deployed or invoked; the served member name moves only when a later release lands it under the pair.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p167_cells.py dry-run at base box/dell2 on dell2 2026-10-12 ~20:4xZ: IB167-4 AC1 FAIL (the new test is absent), AC2 PASS (the regression guard: performance/tests 274 passed, 1 failed, the known calendar test), AC3 FAIL (no record); commit-gate clean. The issuer's source for "bd_adapter alone writes the market-value names, nothing in the repo reads them" is worker ~334's record, not the issuer's own search.
lane: the <paths> block IS the grant. Class WORLD by the L6 floor (an infra path); nothing is deployed.
</preflight>
