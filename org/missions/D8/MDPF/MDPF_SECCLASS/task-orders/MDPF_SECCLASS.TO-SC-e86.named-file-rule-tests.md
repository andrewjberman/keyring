# TO MDPF_SECCLASS.TO-SC-e86 -- round 18 SC-e-86: the BD and COT ship-everything tests move to the named-file deploy rule

<to_id>MDPF_SECCLASS.TO-SC-e86</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~76</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>18</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-86` (`decompositions/MDPF_SECCLASS_DECOMP_R18.md`) |
**outcome_ref:** FWD-16 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-86`, rows MDPF_SECCLASS-D1-S19 and D1-S24, CTO ruling R2 (round-17 analysis). Two gold tests pin a deploy rule the deploy tool
retired on 2026-10-08:
- `data/black_diamond/scripts/gold/tests/test_etf_classifier_deployed_resolution.py`
  `test_deploy_tool_ships_the_shared_modules_beside_the_gold_files` (:155);
- `data/cot/scripts/gold/tests/test_cot_etf_classifier_canonical.py`
  `test_deploy_tool_ships_the_shared_modules_beside_cottonwoods_gold_files` (:145).

Both assert that `safe_deploy_core.upload_plan([<a gold thread file>])` also uploads the three `_shared` modules (the DynamoDB client,
the scheduled planner and `etf_classification.py`) under `code/gold/lib/_shared/`. The current rule (CTO msg 107147;
`.tools/safe_deploy_core.py` `shipped_artifacts_for` and its docstring) is that **a deploy ships only the files it names.** A `_shared`
artifact rides only when its own repo path is named, routed per firm by `--tree black_diamond|cot`. So each test fails at HEAD, and each
gold suite reads one failure for every candidate.

**Build:** rewrite each test, renamed to say what it now asserts, to assert the named-file rule from the tool itself. Read
`safe_deploy_core.upload_plan` and `shipped_artifacts_for` first; assert what they do, never a hand-typed list the tool does not hold.
1. A gold thread file named alone (`C_06.client_mix_timeseries.py` of that firm) plans exactly that one file, at its own key in that firm's
   bucket, with no `_shared` member, and `shipped_artifacts_for([<that file>])` is empty.
2. A named `_shared` module, with that firm's tree, ships to that firm's own bucket under `code/gold/lib/_shared/`. Take the module path
   and the tree argument from the tool's own data.
3. Keep each test's existing negative arm:
   - no member goes to another firm's bucket (COT: `{bucket} == {'opal-data-cot'}`; BD: only `opal-data-bd`);
   - a silver deploy ships nothing extra.
4. Change nothing else in either file, and nothing in `.tools/`.

### ACCEPTANCE

<criterion id="SC18-e86-AC1" cell_refs="SC-e-86"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py data/black_diamond/scripts/gold/tests</invocation><expect>PYTEST-OK</expect></criterion>
`SC18-e86-AC1` -- the whole BD gold suite passes at HEAD with the rewritten test (99 tests at the cut).
<criterion id="SC18-e86-AC2" cell_refs="SC-e-86"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py data/cot/scripts/gold/tests</invocation><expect>PYTEST-OK</expect></criterion>
`SC18-e86-AC2` -- the whole COT gold suite passes at HEAD with the rewritten test (28 tests at the cut).

<expected_criteria>SC18-e86-AC1,SC18-e86-AC2</expected_criteria>

Dry-run at the base (dell1 box/dell1, 2026-10-09 ~12:0xZ):
- SC18-e86-AC1: FAIL, as expected (`PYTEST-BAD 1 failed, 98 passed`, the D1-S19 test; 7.6 s).
- SC18-e86-AC2: FAIL, as expected (`PYTEST-BAD 1 failed, 27 passed`, the D1-S24 test; 5.4 s).

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment).
- **No AWS call at all**; the tests read the tool's data only. Never push. Do not edit `.tools/`.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and file a surprise row (id
  `MDPF_SECCLASS-D1-W76-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). Do not weaken any other test.

<paths>
data/black_diamond/scripts/gold/tests/test_etf_classifier_deployed_resolution.py
data/cot/scripts/gold/tests/test_cot_etf_classifier_canonical.py
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R18.md</decomp_doc> (round 18), cell `SC-e-86`.
<owned_cells>SC-e-86</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC18-e86-AC1, SC18-e86-AC2. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~76/MDPF_SECCLASS.TO-SC-e86.named-file-rule-tests.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC18-e86-AC1,SC18-e86-AC2`.
</proof_of_spec>

**REPORT:** what you read and changed (file:line), both criteria's output, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE tests only; no producer changes.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- a test that hand-types the rule instead of reading the tool (build: assert from upload_plan/shipped_artifacts_for); a weakened cross-firm arm (step 3 keeps it); a .tools edit to make the old test pass (bounds forbid)
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-17 analysis section 2 R2 and section 3 item 2 (msg 2374); rows D1-S19 and D1-S24; DECOMP_R18.
