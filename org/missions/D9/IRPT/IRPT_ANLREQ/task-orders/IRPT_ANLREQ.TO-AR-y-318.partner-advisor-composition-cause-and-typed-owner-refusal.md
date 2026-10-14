# TO IRPT_ANLREQ.TO-AR-y-318.partner-advisor-composition-cause-and-typed-owner-refusal -- NAME the CompositionAdmission check that refuses a partner advisor's own input (row D2-S97), LOG it, and make the owner-lookup refusal typed (row D2-S98); source and tests only, nothing deployed

<to_id>IRPT_ANLREQ.TO-AR-y-318</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~128</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>ZF</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the class the infrastructure `<paths>` imply; the worker deploys, applies and invokes NOTHING)
**Decomp cell:** `AR-y-318` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (hop 1, the owned-input analysis of a partner advisor) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~128`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-128` (branch `wk-IRPT_ANLREQ-128`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~128 <0.9.0_WK_IRPT_ANLREQ~128@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W128-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet` fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. **No live call EXCEPT the read-only AWS reads step 2 names** (through the `.tools/aws` shim); no push, no deploy, no upload, no apply, no invoke, no Terraform. No non-ASCII in what you add. Scratch outside the product tree. The data you read is SYNTHETIC (a sitting's test files, rows `SYNTHA` style); write no account identifier, name or holding value into any file, log or message: print hashes, counts, field NAMES and check names only.

### THE CELL (`AR-y-318`, inlined) -- a cause read plus two small source changes. Nothing is deployed.

*Release 29's partner-advisor sitting (`TO-EXERCISE-R29`, applier `0.7.0_AE_CloudOps~AQ2`) proved the UPLOAD route for a minted `FIRM_ADVISOR` of 49financial (D1: `NORMALIZED`) but the OWNED-INPUT ANALYSIS route refused the same advisor's own input: D2 answered HTTP 200 with public code `INVALID_INPUT`; the function's own record reads `exception_type SubmissionRefused`, `exception_text CLOSED_COMPOSITION_REQUIRED`. The same body shape from the internal viewer on its own input was ADMITTED (D6b). That code comes from `CompositionAdmission.validate` (`infra/aws/lambda/investor-reporting/ycharts/generate/composition_admission.py`, the `try` block of `validate`, lines 38-55), which catches `(ValueError, TypeError, KeyError, UnicodeError, ValidationError)` from FIVE steps and re-raises one code with the real cause chained (`raise ... from error`) and NEVER logged, so which step fails is unknown. CTO rulings (msg 7677): S97 (BLOCKING, FWD-1 critical): log which check fails and reproduce offline on A's frozen D1 composition compared with D6's, then the fix follows under the next intake pair (a LATER cell: do NOT fix the cause here); S98: `load_input_owner` raises a bare `PermissionError`, make it the declared typed refusal.*

The five steps of `validate` (in order): (1) `canonical_bytes(document)` and `json.loads`; (2) `self.validator.validate(frozen)` against `RequestComposition.schema.json`; (3) `compose_frozen_request(frozen["browser"], frozen["resolved"], recipe_version=..., settings=...)` (`ycharts/generate/submission.py`); (4) `validate_bindings(frozen)` (`reports/request_composition.py`); (5) `verify_frozen_portfolio({**resolved["input_ref"], "document": resolved["document"]})` (`intake/portfolio.py`), preceded by the `"document" in resolved` test that raises `SubmissionRefused("FROZEN_NORMALIZED_DOCUMENT_REQUIRED")`.

1. **The facts of the sitting (SYNTHETIC; all in `org/tier2_senior/0.7.0_AE_CloudOps~AQ2/deliverables/irpt_anlreq_r29/`):** `DOOR_RESULT_R29.txt`, `OBJECTS_WRITTEN_R29.txt` (the keys), `sitting_r29.py` (read `analysis_body` at line 72: the body was `{"request_id": <id>, "client_id": null, "account_ids": [], "snapshot_id": null, "variant": "overview", "comparison_keys": [], "report_title": <TITLE>, "prepared_for": "SYNTHETIC", "input_id": <the input id>}` posted to `/api/scoped/investor-reporting/analysis?selected_tenant=49financial`), and rows `IRPT_ANLREQ-D2-S97` and `-S98` in `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md`. The inputs: D1 (advisor A, REFUSED at analysis) input id `portfolio_ac6ac6bd0ddb9e33c3766b44b88da5d2253db219848824b202a2ee84b2c40cb0`; D6 (the internal viewer, ADMITTED) input id `portfolio_bccc5a4ad77f77a668d23038e6b532c99623451db1a0e0a6653784543ea806b6`; both tenant `49financial`. The ACCEPTED frozen composition of D6b is stored at `irpt/49financial/state/request_compositions/ART-8b5b8be1835401deaa5e223202026feea6c077b79d68a15eb96bb3837889126e/00cce0b000ace95608d37a11a4cfd44d7d143a9af0f3189f10e92b28c02c59ce.json` in bucket `opal-data-irpt` (the CONTROL).
2. **The only AWS reads (read-only, `.tools/aws`, results saved under your `.scratch/r40/` OUTSIDE the product tree, never printed in full):** `s3api get-object` of the CONTROL composition above; `s3api get-object` of the two normalized-portfolio documents under `irpt/49financial/state/normalized_portfolios/` whose file leaf is `<the 64-hex of the input id>.json` (find each key by `list-object-versions` on that prefix and the leaf, exactly one key each; the keys are in `OBJECTS_WRITTEN_R29.txt`: `ART-e0d3255c.../ac6ac6bd...json` is D1's, `ART-68c1f856.../bccc5a4a...json` is D6's); `dynamodb get-item` on table `irpt-requests` for `Key={"tenant": "49financial", "request_revision": "INPUT#<the input id>"}` for each of the two inputs (the retained `owner` record: `firm_id`, `principal_id`, `principal_class`, `advisor_id`). Print for each read only the status, the size and the sha256, and the FIELD NAMES of the owner record with its `principal_class` value; do not print `principal_id` or any other value of a person.
3. **THE CAUSE READ.** Build, OFFLINE and with the product's own functions (import them; do not re-implement), the frozen composition the analysis route would build for each input: from the sitting's `analysis_body`, the retained owner record and the normalized document (read how the analysis route composes it: `infra/aws/lambda/investor-reporting/ycharts/generate/` `served.py`, `submission.py` `compose_frozen_request` and the route's caller; and `reports/request_composition.py`). Then run the FIVE steps of `validate` ONE AT A TIME for (a) D1 (advisor A, expected to fail somewhere), (b) D6 (the internal viewer, built the same way, expected to pass), (c) the stored CONTROL composition (expected to pass), recording for each step PASS or the exception CLASS and the first line of its message with every value of a person removed. The first step that fails for D1 and passes for D6 is THE CAUSE: name it (step number, file, line, and the field or comparison that differs between D1 and D6, by FIELD NAME, with the difference described in words: for example "owner.principal_class is FIRM_ADVISOR for D1 and OPAL_GLOBAL for D6, and validate_bindings requires ..."). If D1 does NOT fail offline, say so and name what differs between the offline build and the live request (the live route's own composition path), and file a BLOCKING row. You may NOT change the cause in this cell.
4. **THE LOG (source change 1).** In `composition_admission.py`, make `validate` run its five steps so the failing step is NAMED without changing the public result: on the caught exception, `print` ONE ASCII line `COMPOSITION-REFUSED step=<1..5 or the name: canonical|schema|compose|bindings|portfolio> error_class=<the exception class name>` (no message text, no values) and still raise `SubmissionRefused("CLOSED_COMPOSITION_REQUIRED") from error` exactly as today. The `FROZEN_NORMALIZED_DOCUMENT_REQUIRED` raise is unchanged. Tests in a NEW file `infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_composition_refusal_cause.py` (self-contained: build a tiny valid composition from the product's own fixtures or functions and break ONE step at a time by a monkeypatch on the imported name, five cases): each case prints the matching `step=` and `error_class=`, the raised code is still `CLOSED_COMPOSITION_REQUIRED`, and the log line contains no value from the document. `before_arm`: the new tests FAIL on the tree without the change.
5. **THE TYPED REFUSAL (source change 2, row S98).** In `infra/aws/lambda/investor-reporting/intake/uploads.py`, `load_input_owner` (about line 260-270) raises a bare `PermissionError("INPUT_UNAVAILABLE")`, which the Entry clamps to public code `UNEXPECTED`. The neighbouring `_load` (about line 312) raises the DECLARED `InputUnavailable` (public `NOT_FOUND`). Make `load_input_owner` raise the declared `InputUnavailable` in the same four cases (row missing, tenant mismatch, identity mismatch, owner firm mismatch), keeping the `INPUT_REFERENCE` refusal for a malformed id. Read how the other owner-access refusals declare their public reason (the comment citing row `IRPT_BCKEND-W142-S1`) and match it. Tests in a NEW file `infra/aws/lambda/investor-reporting/intake/tests/test_load_input_owner_typed.py`: the four cases raise `InputUnavailable` (not `PermissionError`), and through the analysis entry the public code for another firm's input is the declared one (find the seam the existing `test_stored_input_contract.py` or `test_uploads*.py` uses), the owner's own input is still returned. Edit an existing assertion ONLY where it pinned the bare `PermissionError` (list each). `before_arm`: the new tests FAIL on the tree without the change.
6. **Write `r40/COMPOSITION_CAUSE.json`** in your deliverable folder: the per-step table for D1, D6 and the CONTROL (step, result, exception class), `cause` {`step`, `file`, `line`, `field`, `difference_in_words`}, `reads` (each AWS read with status, size, sha256), `tests` {`added`, `passed`, `failed`, `folders`}, `before_arm`, `claim`, `not_read` (the live function's log, the live route's composition path if you could not run it).

### ACCEPTANCE

<criterion id="AR318-y-AC1" cell_refs="AR-y-318"><invocation>python C:/dev/wk-irpt-anlreq-128/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~128/cause_check.py</invocation><expect>^CAUSE-NAMED step=</expect></criterion>
`AR318-y-AC1`: you write `deliverables/0.9.0_WK_IRPT_ANLREQ~128/cause_check.py`: it reads `r40/COMPOSITION_CAUSE.json` and prints `CAUSE-NAMED step=<n> file=<path> line=<n>` only when the record carries a cause whose step is the FIRST step that fails for D1, passes for D6 and for the CONTROL in the table (it re-derives that from the table), and every value in the record is a hash, a count, a field name or a check name; otherwise `CAUSE-NOT-NAMED <why>`, exit 1.

<criterion id="AR318-y-AC2" cell_refs="AR-y-318"><invocation>python -m pytest C:/dev/wk-irpt-anlreq-128/infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_composition_refusal_cause.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed</expect></criterion>
`AR318-y-AC2`: the five step cases of step 4 pass (and fail on the tree without the change).

<criterion id="AR318-y-AC3" cell_refs="AR-y-318"><invocation>python -m pytest C:/dev/wk-irpt-anlreq-128/infra/aws/lambda/investor-reporting/intake/tests/test_load_input_owner_typed.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed</expect></criterion>
`AR318-y-AC3`: the typed-refusal cases of step 5 pass (and fail on the tree without the change).

<criterion id="AR318-y-AC4J" cell_refs="AR-y-318" judgment="true"/>
`AR318-y-AC4J` (judgment, graded at L9, never by you): the named step is the true cause (D1 fails there and D6 and the control pass, shown in the table), the log line names the step and the error class and nothing else, the public result of `validate` is unchanged, the owner-lookup refusal is the declared typed one for all four cases, nothing of a person was written into any file or message, and no fix of the cause was made here.

<expected_criteria>AR318-y-AC1 AR318-y-AC2 AR318-y-AC3 AR318-y-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~128/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else, including `submission.py`, `reports/request_composition.py`, `intake/portfolio.py` and `served.py` (the cause may sit in one of them; its FIX is a later cell).

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/composition_admission.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_composition_refusal_cause.py
infra/aws/lambda/investor-reporting/intake/uploads.py
infra/aws/lambda/investor-reporting/intake/tests/test_load_input_owner_typed.py
infra/aws/lambda/investor-reporting/intake/tests/test_uploads.py
infra/aws/lambda/investor-reporting/intake/tests/test_stored_input_contract.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-318</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~128/IRPT_ANLREQ.TO-AR-y-318.partner-advisor-composition-cause-and-typed-owner-refusal.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-318`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR318-y-AC1,AR318-y-AC2,AR318-y-AC3,AR318-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- source and tests in a worker worktree plus six read-only AWS reads of synthetic sitting objects; nothing is deployed, applied or invoked. The members touched are carried by the Lambda irpt-ycharts-generate and the resident (N = 2 each: composition_admission.py, uploads.py); the release pair (the issuer's, after this cell) counts them.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed; a refusal's public code changes from UNEXPECTED to the declared NOT_FOUND and the composition refusal gains a log line. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-iam: DECLARED-NOT-APPLICABLE -- the reads are the dell2 operator's own; no policy changes.
comp-adversary: RUN -- by reading rows D2-S97 and D2-S98 and the CTO ruling msg 7677 against the cell; the lens: a cause named from the first plausible step instead of the step that differs from the control, a log line that carries a value of a person, a typed refusal that now reveals another firm's input, a fix of the cause slipped into a read cell. The cell requires the per-step table with a control, values reduced to names and hashes, and no fix. NOT seen: the live function's own log, the live route's composition path beyond what the code shows.
</preflight>

---

## RECORD FACE

- Cut on the CTO's rulings msg 7677 (S97 cause read first, the fix a later cell under the next intake pair; S98 typed refusal rides the same release) after the release-29 sitting (AQ2 msg 7674; rows D2-S97, D2-S98, D2-S99). Workstream `ZF` of round 40 (the L6 one-issuer-per-round limb keys one issuance to a round and workstream; `ZD` and `ZE` are issued). Base: `AR318-y-AC1`, `AC2` and `AC3` FAIL as expected (no checker file, no test file).
- The fix of the named cause is the NEXT cell, cut by the issuer from this record; it ships with the owner-lookup change as one intake release under a never-widen pair.
