# TO IRPT_BCKEND.TO-IB-pr-471 -- the names of the opening and closing value members: every emitter, what the wire contract names, and a one-side producer rename ONLY if the contract names them

<to_id>IRPT_BCKEND.TO-IB-pr-471</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~326</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>165</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 6476 (PRD ADDENDUM v0.49 @6bed773b76, section 3 item 3; row IRPT_BCKEND-D2-W321-S1) | **Decomp cell:** `IB-pr-471` (decomposition section 157) | **outcome_ref:** FWD-3

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-326/` (bash `/c/dev/wk-irpt-bckend-326`). Work only there; `git rev-parse HEAD` before your first
commit is `base_commit` (state it).

**HARD BOUNDS.** BUILD ONLY, and only the one rename below. No AWS call, no Lambda invoked, no route called, nobody signs in, no vendor
call. Nothing is deployed or uploaded. NO figure of an account, NO account id and no client name goes into any file you write.

**Why.** The holdings producer (`infra/aws/lambda/investor-reporting/performance/holdings_gold.py`, about line 273) writes the
opening and closing value inside `optional_facts.value_facts` as `start_value` and `end_value`. The portal adapter (a separate
checkout, NOT in your worktree) reads `beginning_market_value` and `ending_market_value` (portal `adapt.ts` about lines 797-799 and
839-840), and the only producer writing those names is `performance/bd_adapter.py` (about lines 194-195). So by the code the Reporting
tab's two value tiles read "not supplied" for a holdings-basis answer. The CTO ruled: the WIRE CONTRACT decides which side is wrong;
the side that disagrees renames. A producer rename moves a served name (it ships later under a never-widen pair, not here); an adapter
rename is a portal product candidate (not here). The CTO's note calls the contract the "v2 report schema"; the planner found only
`infra/aws/lambda/investor-reporting/_contracts/PerformanceReport.schema.json` and `docs/contracts/investor-reporting/v1/PerformanceReport.schema.json`,
in which `optional_facts.value_facts` is an object whose members are NOT enumerated (its description says "start and end values only
when supported"). Whether any contract enumerates the members is the first thing to establish.

**Read (the record).**
1. `wire_contract`: `{names_declared: [every member name any contract file under docs/contracts/investor-reporting/ or
   infra/aws/lambda/investor-reporting/_contracts/ declares for the opening or closing value, or [] if none does], cites: [path:line,
   ...] (the lines you read, including the lines that SHOW the members are open if that is the case), in_words}`. Read the schemas
   whole, their fixtures (`_contracts/fixtures/`), and any PRD CONTRACTS row or contract table they cite that is in the repo.
2. `emitters`: every place under `infra/aws/lambda/investor-reporting/` (the producer, `normalize.py`, `f49_engine.py`, `bd_adapter.py`,
   `orion_adapter.py`, `orion_selected.py`, the fixtures) that WRITES a key meaning the opening or closing value: `{cite, names: [...],
   in_words}` each. `emitter_census: {pattern, files_searched, files_with_a_hit}` with the denominator printed (use the native Grep
   tool; word-boundary patterns for `start_value`, `end_value`, `beginning_market_value`, `ending_market_value`, `startValue`, `endValue`).
3. `consumers_in_repo`: the in-repo readers of those keys (tests, `normalize.py`, narrative) `{cite, reads}`. The portal is NOT read
   (say so in `not_established`); the row's portal cites are the issuer's, not yours.
4. `decision`, exactly one of:
   - `PRODUCER_RENAMED`: ONLY if a contract file NAMES the members as `beginning_market_value` and `ending_market_value` and
     `holdings_gold.py` is the emitter that disagrees. Then rename the two keys in `holdings_gold.py` ONLY (and nowhere else), keep
     every other member and the value unchanged, and add the test below. `renamed: [{from, to}]`, `files_changed`, `test_path`.
   - `ADAPTER_SIDE_DISAGREES`: a contract file names `start_value` and `end_value`. Then edit NO product file; write
     `PORTAL_CANDIDATE.md` in your deliverables folder naming what the adapter must read, with the row's portal cites marked INFERRED.
   - `CONTRACT_NAMES_NONE`: no contract file enumerates the members. Edit NO product
     file. State, in `in_words`, which emitters use which names, so the CTO can name the members in the contract.
   - `NOT_ESTABLISHED`: you could not decide; say why in `not_established`.
   A rename on any ground other than a contract file naming the members is out of this order: file a row and stop on the rename.

**Test (only for `PRODUCER_RENAMED`).** `infra/aws/lambda/investor-reporting/performance/tests/test_value_member_names.py`, at least two
tests over synthetic inputs: the producer's `value_facts` carries `beginning_market_value` and `ending_market_value` with the values
the old keys carried, and carries no `start_value` or `end_value`.

**Outputs** in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~326/`: `IB165-1_value_member_names.json` with the keys
above plus `base_commit`, `not_established` (a list), `files_changed` (a list, possibly empty), and `functions_invoked`, `sign_ins_made`,
`aws_writes_made`, `accounts_written`, `figures_written`, `vendor_requests_sent` each 0; and a one-page `IB165-1_VALUE_MEMBER_NAMES_READ.md`
leading with the decision and the two sets of names.

<criterion id="IB165-1-AC1" cell_refs="IB-pr-471"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r165/p165_cells.py" . IB165-1-AC1</invocation><expect>IB165-1-AC1 PASS</expect></criterion>
<criterion id="IB165-1-AC2" cell_refs="IB-pr-471"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r165/p165_cells.py" . IB165-1-AC2</invocation><expect>IB165-1-AC2 PASS</expect></criterion>
<criterion id="IB165-1-AC3" cell_refs="IB-pr-471"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r165/p165_cells.py" . IB165-1-AC3</invocation><expect>IB165-1-AC3 PASS</expect></criterion>

<expected_criteria>IB165-1-AC1, IB165-1-AC2, IB165-1-AC3</expected_criteria>

What the checks grade: AC1 the record's form, that each cite resolves and the census has a denominator; AC2 the decision against the tree (a rename needs its
passing test and no old key left; any other decision needs NO product file changed); AC3 the performance suite (`performance/tests`: 251 passed and 1 failed at base,
the one failure being `test_the_fallback_calendar_is_graded_in_its_own_years_and_clipped_outside_them`, which is not yours and which you do not touch).

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No other emitter is renamed; no portal file is read or written.
- **Refusal clause:** a criterion that cannot be met as written, or a contract that names the members two ways: file a row and report. Never weaken a check or a test;
  do not edit `p165_cells.py`.
- **Hash pins:** if a test, manifest or SHA256SUMS in the repo pins the bytes of `holdings_gold.py`, list it in the record (`hash_pins`) and say what you did; regenerate it only if it is inside your `<paths>`.
- **Row ids** are `IRPT_BCKEND-D2-W326-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or `INFERRED`; append only, keeping the channel file's
  line endings byte for byte; check the id is free before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~326" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~326@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~326 <0.9.0_WK_IRPT_BCKEND~326@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
infra/aws/lambda/investor-reporting/performance/holdings_gold.py
infra/aws/lambda/investor-reporting/performance/tests/
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~326/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-471.value-member-names-census-and-one-side-rename.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 157 (round 165, workstream ~P), cell `IB-pr-471`.
<owned_cells>IB-pr-471</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB165-1-AC1, IB165-1-AC2, IB165-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~326/IRPT_BCKEND.TO-IB-pr-471.value-member-names-census-and-one-side-rename.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the base; what each contract file declares for the two members (or that it declares none); each emitter with its names; the decision and why;
if renamed, the test's last line; the performance suite's last line; each criterion's last line; the proof checker's result; commit hashes; row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; the cell edits at most one producer file in the repo; no running byte moves until a later release under its own never-widen pair.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change; no route is called.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p165_cells.py dry-run at base box/dell2 on dell2 2026-10-12 ~18:0xZ: IB165-1 AC1 FAIL, AC2 FAIL, AC3 FAIL (no file); commit-gate clean. Measured by the issuer at base: pytest performance/tests reads 251 passed, 1 failed (the calendar-fallback test, row D2-W282-S3, routed to its owner). The issuer's read of the schema: value_facts is `type [object, null]` with no members listed (_contracts/PerformanceReport.schema.json lines 328-334), so CONTRACT_NAMES_NONE is the expected decision and is not on the worker face as the answer.
lane: the <paths> block IS the grant. Class WORLD by the L6 floor (an infra path); nothing is deployed.
</preflight>
