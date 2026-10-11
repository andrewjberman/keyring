# TO IRPT_ANLREQ.TO-AR-y-32 -- irpt-status's served reads: `retained_ref` on analysis-report, `client_id` on each history row, and section dates read by provider branch

<to_id>IRPT_ANLREQ.TO-AR-y-32</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~52</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (code, tests and contract documents; nothing is built into a zip or deployed here --
the release is one apply order after the drain) The class is WORLD because the L6 gate's floor for an `infra/` path is WORLD; the cell itself builds, uploads and applies nothing. | **Decomp cell:** `AR-y-32` (`decompositions/IRPT_ANLREQ_DECOMP_R3_Y.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~52`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-52` (branch `wk-IRPT_ANLREQ-52`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~52 <0.9.0_WK_IRPT_ANLREQ~52@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. Run tests with invalid AWS keys (`AWS_ACCESS_KEY_ID=x AWS_SECRET_ACCESS_KEY=y`).
- `IR` below is `infra/aws/lambda/investor-reporting`. `surfaced_at` of any row = `date -u +%FT%TZ` at filing.

### THE CELL (`AR-y-32`, inlined)

*irpt-status's served reads gain two members: `analysis-report` returns `retained_ref` in the shape Performance serves; each row of the
owned-request history states `client_id`, the client its frozen selection names (null for an upload). Contract documents updated; both
arms of each tested. AND `section_dates()` reads a report by its own provider branch: an `opal_engine` row with status NOT_AVAILABLE and a
null date is an undated row.*

**Part A -- `retained_ref` on analysis-report (interface I9).**
- `IR/ops/owned_report.py`, `OwnedAnalysisReader.read` (:110-154) already builds, for a READY request,
  `ref = {"report_id", "revision", "sha256", "report_kind": "ANALYSIS", "immutable": True}` from the generation job's detail (:128-129) and
  checks the report row against it (`_report_row`). It does not return it.
- `sections` (:73-92) is the public projection of `analysis-report`. Make BOTH of its branches (the `OPAL_ENGINE` form and the v1 form)
  answer one more member, `retained_ref`, equal to that checked ref. Get it from `read` without a second storage read and without
  changing what `read` returns to its other callers (`pdf`, `original`, `persist_inputs`, `owned_status.py` call `read`; read them before
  you choose how to carry the ref).
- `docs/contracts/investor-reporting/v1/AnalysisReport.schema.json` declares `retained_ref`: the same node as
  `PerformanceReport.schema.json`'s `retained_ref` (:352 -- `report_id` `^RPT-[0-9a-f]{32}$`, `revision` and `sha256` 64-hex,
  `report_kind`, `immutable` const true, `additionalProperties` false, and whatever `required` it carries), member for member, with ONE
  difference: `report_kind` is `{"const": "ANALYSIS"}`. Add it wherever that schema lists the members of each provider form. Whether it
  is `required` there: required, since `read` refuses a READY report with no receipt (`READY_REPORT_RECEIPT_REQUIRED`).
- New test file `IR/ops/tests/test_retained_ref_served.py` with EXACTLY these names:
  - `test_ready_report_returns_retained_ref_in_the_performance_shape`
  - `test_retained_ref_equals_the_ref_the_reader_checked`
  - `test_other_firm_is_refused_and_no_ref_is_returned`
  Build its world the way `IR/ops/tests/test_owned_report.py` does.

**Part B -- `client_id` on each history row (interface I8).**
- `IR/ops/owned_requests.py`, `OwnedRequestReader.history` (:316 on). Each returned item is today `{identity, accepted_at}`. Each item
  gains `client_id`: the client the request's frozen selection names, which `_selected_client` (:198-214) already derives from the
  retained composition (`browser.client_id`); JSON null for an upload. Its docstring says "No client field reaches the wire": that was the
  earlier ruling and this cell reverses it for the HISTORY ROW ONLY; correct the docstring.
- Do not add a storage read per row beyond what the page makes today: with no `client_id` filter the page calls `_materialize` per row
  (one retained composition read, :194) and with a filter it calls `_selected_client` (the same one read). Use ONE read per row in both
  cases. `_final` and the cursor are unchanged.
- The SINGLE read (`read`, :233-255, `analysis-request-read`) does NOT gain `client_id`; its wire stays `{identity, accepted_at}` plus its
  opt-in members.
- `docs/contracts/investor-reporting/v1/OwnedAnalysisRequestHistory.schema.json`: `items.items` is today a `$ref` to
  `OwnedAnalysisRequest.schema.json`. Make it an INLINE object schema: `additionalProperties` false, `required`
  `["identity", "accepted_at", "client_id"]`, `identity` and `accepted_at` defined as in `OwnedAnalysisRequest.schema.json` (by `$ref` into
  it if it exposes them, otherwise copied exactly), and `client_id` typed `["string", "null"]` with the pattern `owned_requests.py`'s
  `CLIENT_ID` uses. `OwnedAnalysisRequest.schema.json` itself is NOT changed.
- New test file `IR/ops/tests/test_history_row_client.py` with EXACTLY these names:
  - `test_history_row_states_the_client_its_selection_names`
  - `test_upload_request_row_states_null_client`
  - `test_single_read_wire_is_unchanged`
  Build its world the way `IR/ops/tests/test_history_client_scope.py` does.

**Part D -- section dates by provider branch** (joined to this cell by the CTO after the cut began; one release carries all three).
- `IR/ops/prospect_dates.py`, `section_dates(report)` (:30-47) applies ONE rule to every report: a `sections` row must carry an ISO
  `as_of_date`, and undated rows live under `undated_sections` with `date_claim == "NONE"`. That is the `ycharts` branch's rule.
- The ratified contract `IR/_contracts/AnalysisReport.v2.schema.json` has two branches. `$defs.opal_engine`: NO `undated_sections`
  property; each `sections` item REQUIRES `as_of_date` typed `["string","null"]` ("null only when status is NOT_AVAILABLE") and a `status`
  that is `VALUE` or `NOT_AVAILABLE`. `$defs.ycharts`: has `undated_sections`; its `sections` items carry a string `as_of_date` and no
  `status`. The document's `provider` member states its branch (`owned_report.py` `_provider`, :47-52, is how the reader tells them apart).
- **Change:** `section_dates` reads a document by its own branch. For an `opal_engine` document, a `sections` row whose `status` is
  `NOT_AVAILABLE` and whose `as_of_date` is null is an UNDATED row (`{"section_id", "as_of_date": None}` in the result, as an
  `undated_sections` row gives today). A null beside `VALUE` raises `SECTION_DATE_CENSUS_INVALID`. A non-null date beside
  `NOT_AVAILABLE` that is not an ISO date raises it too. The `ycharts` branch's rule is unchanged, byte for byte in behaviour.
- New test file `IR/ops/tests/test_section_dates_by_branch.py` with EXACTLY these names:
  - `test_opal_engine_not_available_row_with_null_date_is_undated`
  - `test_ycharts_branch_rule_is_unchanged`
  - `test_opal_engine_null_date_beside_value_is_refused`
  - `test_opal_engine_bad_date_beside_not_available_is_refused`
- `IR/ops/tests/test_prospect_dates.py` is in `<paths>` only for an assertion that encoded the one-rule behaviour for an Opal document;
  update only such an assertion and name it.

**Part C -- the contract suite.** The analysis-report response is described in more than one document: the published
`docs/contracts/investor-reporting/v1/AnalysisReport.schema.json` and, under `IR/_contracts/`, `AnalysisReport.schema.json` and
`AnalysisReport.v2.schema.json` (the one with the two provider branches). Find which of them the paired-seam tests bind, and add
`retained_ref` to EVERY one that describes what `sections` answers, the same node in each. `IR/_contracts` has two tests RED at the base, both about `analysis-request-original`'s response contract;
they are not yours and must stay exactly those two. If a fixture or a paired-seam table under `IR/_contracts/` or
`docs/contracts/investor-reporting/v1/` must change for your two members to conform, change it and say so; `routes.json` does not change
(no route is added). If `IR/ops/entry.py` needs a change for either member, it is in your paths; if it needs none, do not touch it.

Do NOT touch the portal (its generated wire types are another project's, after the release). Do NOT edit the source map or build a zip.

### ACCEPTANCE

<criterion id="AR32-y-AC1" cell_refs="AR-y-32"><invocation>python C:/dev/wk-irpt-anlreq-52/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r3/ar3_checks.py y32-ref --root C:/dev/wk-irpt-anlreq-52</invocation><expect>Y32-REF-OK</expect></criterion>
`AR32-y-AC1`: Part A's three named tests exist and pass.

<criterion id="AR32-y-AC2" cell_refs="AR-y-32"><invocation>python C:/dev/wk-irpt-anlreq-52/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r3/ar3_checks.py y32-history --root C:/dev/wk-irpt-anlreq-52</invocation><expect>Y32-HISTORY-OK</expect></criterion>
`AR32-y-AC2`: Part B's three named tests exist and pass.

<criterion id="AR32-y-AC3" cell_refs="AR-y-32"><invocation>python C:/dev/wk-irpt-anlreq-52/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r3/ar3_checks.py y32-contract --root C:/dev/wk-irpt-anlreq-52</invocation><expect>Y32-CONTRACT-OK</expect></criterion>
`AR32-y-AC3`: both contract documents declare the members in the shapes above, the single-read schema is untouched, and the `_contracts`
failing SET is exactly the two ids known at the base.

<criterion id="AR32-y-AC4" cell_refs="AR-y-32"><invocation>python C:/dev/wk-irpt-anlreq-52/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r3/ar3_checks.py y32-dates --root C:/dev/wk-irpt-anlreq-52</invocation><expect>Y32-DATES-OK</expect></criterion>
`AR32-y-AC4`: Part D's four named tests exist and pass. A FOURTH criterion, for one reason: the CTO joined a third item to this cell after
the cut began (IRPT_YCDGEN round-8 ADDENDUM 8.1), and it is a separate behaviour with its own two refusing cases.

<expected_criteria>AR32-y-AC1 AR32-y-AC2 AR32-y-AC3 AR32-y-AC4</expected_criteria>

The issuer runs the whole `IR/ops/tests`, `IR/reports/tests` and `IR/_authz/tests` folders at the drain.

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/` and this order's
  file (status flip only).
- READ only: everything else under `infra/aws/lambda/investor-reporting/` and `docs/contracts/`.
- No live act: never push, never deploy, never call a live API. No non-ASCII. Synthetic test data only.

<paths>
infra/aws/lambda/investor-reporting/ops/owned_report.py
infra/aws/lambda/investor-reporting/ops/owned_requests.py
infra/aws/lambda/investor-reporting/ops/entry.py
infra/aws/lambda/investor-reporting/ops/prospect_dates.py
infra/aws/lambda/investor-reporting/ops/tests/test_section_dates_by_branch.py
infra/aws/lambda/investor-reporting/ops/tests/test_prospect_dates.py
infra/aws/lambda/investor-reporting/ops/tests/test_retained_ref_served.py
infra/aws/lambda/investor-reporting/ops/tests/test_history_row_client.py
infra/aws/lambda/investor-reporting/ops/tests/test_history_client_scope.py
infra/aws/lambda/investor-reporting/ops/tests/test_owned_requests.py
infra/aws/lambda/investor-reporting/ops/tests/test_owned_report.py
infra/aws/lambda/investor-reporting/_contracts/
docs/contracts/investor-reporting/v1/AnalysisReport.schema.json
docs/contracts/investor-reporting/v1/OwnedAnalysisRequestHistory.schema.json
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The four existing test files in `<paths>` are there ONLY for an assertion that pins the old wire of a history row or of the report
projection (an exact-key-set equality): update only such an assertion, and name each in your report.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R3_Y.md</decomp_doc> (round 3, workstream Y), cell `AR-y-32`.
<owned_cells>AR-y-32</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR32-y-AC1 AR32-y-AC2 AR32-y-AC3 AR32-y-AC4. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/IRPT_ANLREQ.TO-AR-y-32.served-retained-ref-and-history-client.proof_of_spec.json`.
Validate it AFTER its commit with `python .tools/proof-of-spec-check.py <instance> AR32-y-AC1,AR32-y-AC2,AR32-y-AC3,AR32-y-AC4`.
</proof_of_spec>

**REPORT (once):** each check line verbatim; the commit; how `sections` obtains the ref; every existing assertion you updated; the count of
storage reads per history row before and after, as your tests' fakes counted them; any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- owned_report.read has four callers besides sections (pdf, original, persist_inputs, owned_status.OwnedJobStatusReader.read); the face tells the worker to read them before choosing how to carry the ref. comp-routes: DECLARED-NOT-APPLICABLE -- no route is added; routes.json is out of the grant. comp-cache: DECLARED-NOT-APPLICABLE -- the read memo (read_memo.py) is not in the grant. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no new read family: the history row's client comes from the composition read the page already makes. comp-adversary: RUN -- AR32-y-AC1, -AC2, -AC3 dry-run at the base: FAIL, FAIL, FAIL as expected (no test files; the two schema members absent; the _contracts failing set measured as exactly the two known ids).
lane: irpt-status's read plane is workstream Y's surface (AR-y-11, AR-y-21, AR-y-22).
</preflight>

Source: CTO round-3 analysis @430d79e86d section 4 Y2; rows IRPT_ANLREQ-D2-S21 (DSGN_IRPTV1 W39-S2, CTO analysis @10d7d46e49) and
IRPT_ANLREQ-D2-S24 (1.0.0_SA_CTO~DELL2 msg 4235); Part D is row IRPT_YCDGEN-D2-S38 as ruled in CTO_ROUND_ANALYSIS_IRPT_YCDGEN_ROUND_8_20261011.md ADDENDUM 8.1 @02689893e2 (msg 4333). AR32-y-AC4 dry-run at the base: FAIL as expected (no test file). Interfaces I8 and I9 are fixed in the decomposition. Performance's `report_kind` is the
const PERFORMANCE, so "the shape Performance serves" is cut as the same members with the const ANALYSIS.
