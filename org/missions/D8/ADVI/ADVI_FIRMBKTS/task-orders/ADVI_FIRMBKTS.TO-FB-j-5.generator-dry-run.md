# ADVI_FIRMBKTS task order -- `FB-j-5` -- THE EXEC-SUMMARY GENERATOR GAINS A DRY-RUN PATH (event.dry_run + advisor_ids, AT MOST 10, NO S3 WRITE)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R7.md</decomp_doc>
<owned_cells>FB-j-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~70</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a Lambda handler change, not deployed here; no cron, rule, schedule or cadence is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS act and no grant; the test stubs every client.
comp-adversary: RUN by the issuer -- at the base `tests/test_dry_run.py` is absent (AC1 FAIL) and `git diff --stat` shows nothing (AC2 FAIL); AC3 FAILs with nothing changed. Blindness: the stubbed test proves the handler's branch logic, not the deployed Lambda or a real model call.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-j-5` (round 7, enrichment item 2; the CTO's ruling, ROUND_ANALYSIS.round6.md ADDENDUM 1 item 1)

`exec-summary-generator`'s handler (`infra/aws/lambda/exec-summary-generator/lambda_function.py`, `lambda_handler` at about line 426) hard-codes `upload=True`
(line 442): every fire writes every advisor's `exec_summary.json` to the served prefix. When the dispatcher's emit works, the first chain
regenerates up to 158 client-facing LLM summaries that have been stale for five months, and the CTO requires a SAMPLE to be read BEFORE
they serve. You add the sample path; the production path stays byte-unchanged in behaviour.

### 1a. The edit (`infra/aws/lambda/exec-summary-generator/lambda_function.py` and one new test file)

1. `lambda_handler` reads `event.get('dry_run')` and `event.get('advisor_ids')`.
2. When `dry_run` is truthy: `advisor_ids` MUST be a list of 1 to 10 strings (else return `{'statusCode': 400, 'error': ...}` BEFORE any read or
   model call); the handler processes ONLY those advisors with `process_advisor(..., upload=False)` (the function already supports it),
   makes NO S3 write of any kind and emits no HANDLER-level metric (the per-call token metrics inside the model path stay: a dry run calls the model, so those tokens are real), and returns `{'statusCode': 200, 'dry_run': True, 'artifacts': {advisor_id:
   artifact, ...}, 'advisors_processed': n, 'firm_id': ...}`.
3. When `dry_run` is absent or falsy the handler behaves exactly as at the base: the same advisors, `upload=True`, the same metrics, the same
   return value, byte for byte.
4. No new dependency, no change to `config.py`, prompts, the model id or any other file under the generator directory.

### 1b. The test (`infra/aws/lambda/exec-summary-generator/tests/test_dry_run.py`, yours, pytest, stubs only: no network, no AWS call, no model call)

Stub the S3 client, the platinum reader, the model call and the metrics. Arms, each a named test:
1. `test_dry_run_writes_nothing`: a dry run for 2 advisor ids returns 2 artifacts and the stub S3's `put_object` and the metrics emitters are
   never called (0 objects written).
2. `test_dry_run_refuses_more_than_ten_and_empty`: 11 ids, an empty list and a non-list each return 400 and call nothing.
3. `test_non_dry_unchanged`: with no `dry_run`, the same stubs, `put_object` is called once per advisor with the same Bucket, Key and Body
   as the base implementation produces (compare against the output of the base function captured in the test by calling `process_advisor`
   directly with `upload=True`), and the return dict equals the base's keys and values.
Also run one MUTANT control (a temporary local edit, reverted before you commit): make the dry path call `put_object`, and show
`test_dry_run_writes_nothing` FAILS; revert and show it passes. Never commit the mutant.

## 2. BOUNDS

1. One commit: the handler and the test file. No deploy, no Terraform, no AWS call, no model call. ASCII only.
2. If the handler or `process_advisor` does not look as described, STOP before editing and file a BLOCKING row.

## 3. SURFACES

<paths>
infra/aws/lambda/exec-summary-generator/lambda_function.py
infra/aws/lambda/exec-summary-generator/tests/test_dry_run.py
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~70/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~70/ADVI_FIRMBKTS.TO-FB-j-5.generator-dry-run.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-j-5"><invocation>cd /c/dev/wk-firmbkts-70/infra/aws/lambda/exec-summary-generator &amp;&amp; timeout 110 python -m pytest tests/test_dry_run.py -q 2&gt;&amp;1 | sed "s/\x1b\[[0-9;]*m//g" | tail -1</invocation><expect>^3 passed</expect></criterion>
  <criterion id="AC2" cell_refs="FB-j-5"><invocation>cd /c/dev/wk-firmbkts-70 &amp;&amp; git diff --stat $(git merge-base HEAD box/dell1) HEAD -- infra/aws/lambda/exec-summary-generator | tail -1</invocation><expect>^ 2 files changed</expect></criterion>
  <criterion id="AC3" cell_refs="FB-j-5"><invocation>cd /c/dev/wk-firmbkts-70 &amp;&amp; timeout 60 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-firmbkts-70 --allow infra/aws/lambda/exec-summary-generator/lambda_function.py --allow infra/aws/lambda/exec-summary-generator/tests/test_dry_run.py --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~70/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 is the three named arms (the mutant control is reported, not a criterion), AC2 the two-file bound, AC3 the write-surface bound.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~70/ADVI_FIRMBKTS.TO-FB-j-5.generator-dry-run.proof_of_spec.json`. Commit the handler and the test FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids: `ADVI_FIRMBKTS-D1-W70-S<k>`. Report once: AC1 to AC3 outputs, the mutant control's failing test name and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's ADDENDUM 1 item 1 (YES; "serve, then read, then roll back" refused): arms are "a dry run writes 0 objects; a non-dry invocation is byte-unchanged in behaviour"; Terraform-deployed under its own pair (FB-j-6). The dry-run path stays as the QA route for every later regeneration. The test is the worker's (it needs the generator's internals); AC1 expects exactly 3 passed. Class WORLD by the path floor.

**AMENDMENT 1 (2.0.0_SA_COO~B1, 2026-10-13 ~09:2xZ):** (a) AC1 strips ANSI colour before the match (the host sets FORCE_COLOR; the worker's row W70-S2; the same trap round 4 recorded and the issuer failed to carry into this face). (b) Section 1a item 2: the worker's row W70-S1 found that `_call_llm` and `_build_slot` emit per-call token metrics, so "no CloudWatch metric emission" cannot hold on a real dry run without threading a flag through the model path. The CTO's arm is "a dry run writes 0 objects (bucket listing before and after)"; the per-call metrics count real model tokens and are kept; only the handler-level metrics are suppressed (as built). The worker's handler is accepted as built; no code change is owed. The criteria are otherwise unchanged. Issuer amends its own pending order; GATE viii reads `<placeholders>NONE</placeholders>` and no token.

<status>pending</status>
<round>7</round>
<workstream>EXECSUMFIX</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-j-5</to_id>
<slot>~70</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
