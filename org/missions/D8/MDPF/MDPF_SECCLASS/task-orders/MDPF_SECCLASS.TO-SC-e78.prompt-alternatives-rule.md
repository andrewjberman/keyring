# TO MDPF_SECCLASS.TO-SC-e78 -- round 15 SC-e-78: the AI classifier's prompt states Andrew's alternatives rule

<to_id>MDPF_SECCLASS.TO-SC-e78</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~68</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>15</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-78` (`decompositions/MDPF_SECCLASS_DECOMP_R15.md`) |
**outcome_ref:** FWD-17 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-78`. Andrew-direct 2026-10-08 ~19:0xZ, VERBATIM: "Hedge funds, private funds, real estate funds, all of this falls to
Alternatives." 1.0.0_SA_CTO~DELL1 ruled that the rule binds the AI leg's instructions (msg 1062).
`infra/aws/lambda/v2_portal/_shared/etf_classification_model.py` `build_prompt` (:86-99) names the six classes but not the rule. The
e49 AI leg is paused until it does.

**Build:**
1. Add ONE sentence to `build_prompt`'s instruction text stating that hedge funds, private funds and real estate funds are
   `alternatives`. Use those three phrases literally. Change nothing else:
   - the six-value vocabulary;
   - the JSON shape;
   - the rule that the name and ticker sit only in the trailing data object.
2. Write `infra/aws/lambda/v2_portal/_shared/tests/test_prompt_alternatives_rule.py`. It pins the sentence, and as the control that
   the name and ticker never enter the instruction text.

### ACCEPTANCE

<criterion id="SC15-e78-AC1" cell_refs="SC-e-78"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R15_CHECKS/sc_r15_prompt_rule.py</invocation><expect>PROMPT-RULE ok=True</expect></criterion>
`SC15-e78-AC1` -- the instruction names hedge, private and real estate funds and alternatives; name and ticker stay only in the data object.
<criterion id="SC15-e78-AC2" cell_refs="SC-e-78"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py infra/aws/lambda/v2_portal/_shared/tests</invocation><expect>PYTEST-OK</expect></criterion>
`SC15-e78-AC2` -- the whole _shared suite still passes, the new pin included.

<expected_criteria>SC15-e78-AC1,SC15-e78-AC2</expected_criteria>

Dry-run at the base (dell1 CLOUD, 2026-10-08 ~19:2xZ):
- SC15-e78-AC1: FAIL, as expected (hedge, private and real_estate all read False).
- SC15-e78-AC2: PASS, as expected (control, 349 passed).

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment).
- **AWS is READ-ONLY** (get, list, head, scan): no write to any table or bucket, no deploy, no invoke, no model call. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and file a surprise row (id
  `MDPF_SECCLASS-D1-W68-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). Do not weaken the test.

<paths>
infra/aws/lambda/v2_portal/_shared/etf_classification_model.py
infra/aws/lambda/v2_portal/_shared/tests/test_prompt_alternatives_rule.py
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R15.md</decomp_doc> (round 15), cell `SC-e-78`.
<owned_cells>SC-e-78</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC15-e78-AC1, SC15-e78-AC2. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~68/MDPF_SECCLASS.TO-SC-e78.prompt-alternatives-rule.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC15-e78-AC1,SC15-e78-AC2`. Record a judgment criterion as
`UNVERIFIABLE-BY-INSTRUMENT`, with a `status_reason` naming 3.0.0_SA_CVO, never as PASS or FAIL.
</proof_of_spec>

**REPORT:** what you read and changed (file:line), each criterion's output, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the e49 runner reads the repo module on dell1; any Lambda redeploy of _shared follows in the deploy lane.
comp-iam: DECLARED-NOT-APPLICABLE no grant change, no AWS.
comp-adversary: RUN -- name or ticker leaking into the instruction (control); a seventh class value; BLIND: the model's behaviour on the new sentence (graded by e49's resumed refusals and the e77 scan).
lane: the <paths> block IS the grant.
</preflight>

Source: 1.0.0_SA_CTO~DELL1 msgs 1061, 1066, 1071; Andrew-direct 2026-10-08 ~19:0xZ (alternatives rule); trace @3d9077bdc5; DECOMP_R15.
