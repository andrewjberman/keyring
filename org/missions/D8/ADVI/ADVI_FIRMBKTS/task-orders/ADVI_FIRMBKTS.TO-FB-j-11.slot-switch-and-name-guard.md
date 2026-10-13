# ADVI_FIRMBKTS task order -- `FB-j-11` -- THE GENERATOR GAINS A SLOT SWITCH (top_nna_mover OFF BY CONFIG), A CLIENT-NAME GUARD, AND THE TERRAFORM CARRIER OF THE SWITCH

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R7.md</decomp_doc>
<owned_cells>FB-j-11</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~74</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and a Terraform variable, not applied here; no cron, rule, schedule or cadence is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS act and no grant; the test stubs every client.
comp-adversary: RUN by the issuer -- at the base the test file is absent (AC1 FAIL), `tfslots` reads 1 of 3 (T3 passes as a control) and nothing changed (AC3 FAIL). Blindness: stubs prove the branch logic and the Terraform text, not the deployed function, a real model reply or a plan.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-j-11` (round 7; the CTO's reading of the ten-advisor sample, `ledger/CTO_SAMPLE_READ_FB_J_10_EXEC_SUMMARIES_20261013.md`, rulings (a) and (b))

The sample read: four slots (`top_gainer`, `top_loser`, `concentration_risk`, `tax_loss_candidate`) read well; `top_nna_mover` is broken: it
attributes one placeholder relationship `rel_id "0"` ($9,625,309.46) to two advisors, prints raw relationship ids, and in one artifact a client
DISPLAY NAME reached the text (the PII guard did not drop it). The CTO rules: (a) `top_nna_mover` is DISABLED by config for the first
regeneration (a switch, NOT deleted code; the product fix goes to the CRO's brief); (b) the PII guard learns client display names. You build
the switch, the guard and the Terraform carrier of the switch, and change nothing else.

### 1a. Part A -- the slot switch (`infra/aws/lambda/exec-summary-generator/lambda_function.py`)

1. A helper `_disabled_slots()` returns a `frozenset` of slot names from the environment variable `EXEC_SUMMARY_DISABLED_SLOTS`
   (comma separated, whitespace trimmed, empty or absent gives the empty set). Read at CALL time, not import time (so a test can set it).
2. `process_advisor` computes it once, and for each of the six slots (`top_gainer`, `top_loser`, `concentration_risk`, `tax_loss_candidate`,
   `leaderboard_rank_delta`, `top_nna_mover`) a slot named in the set is SKIPPED ENTIRELY: its evaluator is not called, no context is built,
   no model call is made, no bullet and no drop. A name that is not one of the six is ignored.
3. With the variable absent or empty the behaviour is byte-for-byte as at the base. The dry-run branch and the drop log of `FB-j-5`/`FB-j-9`
   are untouched.

### 1b. Part B -- the client-name guard (`infra/aws/lambda/exec-summary-generator/lambda_function.py`, in `_build_slot`)

The context fed to the model carries `client_rel_id` (a pseudonymous relationship id such as `z08374526`); in the sampled data it can hold a
client's display name instead. Two checks, both raising the module's existing `PIIDetectedError` (so the drop is logged `exc=PIIDetectedError
msg=redacted` and the metric fires as for any drop):
1. **Before the model call:** if `advisor_context.get('client_rel_id')` is a string that does NOT fully match `^[A-Za-z]?[0-9]+$` (an id),
   it may be a name: drop the slot (no model call is made with a name in the context).
2. **After the reply:** collect the string values (length of at least 4) of the context keys `client_rel_id` and every key ending in
   `_name` EXCEPT `security_name` and `ticker`-like keys; if any of them appears in the validated `detail` text, compared case-insensitively
   after collapsing whitespace, drop the slot.
Security names (for example an ETF's name in `security_name`) are NOT client names and must keep passing.

### 1c. Part C -- the Terraform carrier (`infra/aws/terraform/exec-summary/variables.tf` and `infra/aws/terraform/exec-summary/main.tf`)

Mirror exactly what `platinum_mode` does there: a new variable `disabled_slots` (type string, default `""`) with a `validation` that every
comma-separated name is one of the six slot names (or the string is empty), and in the `environment` block's `merge(...)` one more term:
`var.disabled_slots == "" ? {} : { EXEC_SUMMARY_DISABLED_SLOTS = var.disabled_slots }`. The six existing environment keys and the
`platinum_mode` term do not change; with the variable at its default the plan is unchanged.

### 1d. The test (`infra/aws/lambda/exec-summary-generator/tests/test_slot_switch_guard.py`, yours, pytest, stubs only: no network, no AWS call, no model call)

Six named tests (stub the evaluators, `_call_llm`, `validate_slot_response` and the metrics on the module):
1. `test_disabled_slot_is_skipped_entirely`: with `EXEC_SUMMARY_DISABLED_SLOTS=top_nna_mover` the NNA evaluator and `_call_llm` are never
   called for that slot, the other slots still produce bullets.
2. `test_default_unchanged`: with the variable absent, all six slots are evaluated as at the base (compare the call log with an empty set).
3. `test_unknown_name_ignored`: `EXEC_SUMMARY_DISABLED_SLOTS=top_nna_mover, nonsense` disables only the first.
4. `test_name_in_reply_is_dropped`: context `{'client_rel_id': 'Z9000001', 'client_display_name': 'Jane Q Public'}` and a reply containing
   `Jane Q Public`: `_build_slot` returns `None` and the logged class is `PIIDetectedError`.
5. `test_non_id_client_rel_id_dropped_before_model_call`: `client_rel_id = 'Jane Q Public'`: `_call_llm` is never called, the slot is dropped.
6. `test_security_names_still_pass`: a reply containing `ISHARES CORE MSCI EAFE ETF` with `security_name` in the context is returned as a bullet.
Also run TWO MUTANT controls (temporary local edits, reverted before you commit): (i) make the switch ignore the variable: test 1 FAILS;
(ii) remove the post-reply name check: test 4 FAILS. Never commit a mutant.

## 2. BOUNDS

1. One commit: `lambda_function.py`, the test file, `variables.tf` and `main.tf`. No deploy, no `terraform apply`, no AWS call, no model call. ASCII only.
2. Do not delete the `top_nna_mover` code or its prompt: the slot is switched off, not removed.
3. If `process_advisor` or `_build_slot` does not look as described, STOP before editing and file a BLOCKING row.

## 3. SURFACES

<paths>
infra/aws/lambda/exec-summary-generator/lambda_function.py
infra/aws/lambda/exec-summary-generator/tests/test_slot_switch_guard.py
infra/aws/terraform/exec-summary/variables.tf
infra/aws/terraform/exec-summary/main.tf
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~74/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~74/ADVI_FIRMBKTS.TO-FB-j-11.slot-switch-and-name-guard.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-j-11"><invocation>cd /c/dev/wk-firmbkts-74/infra/aws/lambda/exec-summary-generator &amp;&amp; timeout 110 python -m pytest tests/test_slot_switch_guard.py -q 2&gt;&amp;1 | sed "s/\x1b\[[0-9;]*m//g" | tail -1</invocation><expect>^6 passed</expect></criterion>
  <criterion id="AC2" cell_refs="FB-j-11"><invocation>cd /c/dev/wk-firmbkts-74 &amp;&amp; timeout 60 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round7/checks/r7_checks.py tfslots --root /c/dev/wk-firmbkts-74</invocation><expect>^TFSLOTS: 3 of 3 arms$</expect></criterion>
  <criterion id="AC3" cell_refs="FB-j-11"><invocation>cd /c/dev/wk-firmbkts-74 &amp;&amp; timeout 60 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-firmbkts-74 --allow infra/aws/lambda/exec-summary-generator/lambda_function.py --allow infra/aws/lambda/exec-summary-generator/tests/test_slot_switch_guard.py --allow infra/aws/terraform/exec-summary/variables.tf --allow infra/aws/terraform/exec-summary/main.tf --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~74/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 is the six named arms (the mutant controls are reported, not criteria), AC2 the three Terraform text arms (the carrier mirrors `platinum_mode`), AC3 the write-surface bound.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~74/ADVI_FIRMBKTS.TO-FB-j-11.slot-switch-and-name-guard.proof_of_spec.json`. Commit the code, the test and the two Terraform files FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids: `ADVI_FIRMBKTS-D1-W74-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: AC1 to AC3 outputs, the mutant controls' failing test names and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's sample read (`ledger/CTO_SAMPLE_READ_FB_J_10_EXEC_SUMMARIES_20261013.md`): defects 1 and 2, rulings (a) and (b). The disabled slot is the product defect (one placeholder `rel_id "0"` pools unrelated flows under one fake client; raw relationship ids are printed); the fix of the slot goes to the CRO's exec-summary brief, not here. The guard is the CTO's (b): it is needed before ANY slot that can name a client serves. The environment carrier mirrors `platinum_mode` so the deploy (`FB-j-13`) is a scoped plan whose only added key is `EXEC_SUMMARY_DISABLED_SLOTS`. Class WORLD by the path floor.

<status>complete</status>
<round>7</round>
<workstream>SLOTSWITCH</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-j-11</to_id>
<slot>~74</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
