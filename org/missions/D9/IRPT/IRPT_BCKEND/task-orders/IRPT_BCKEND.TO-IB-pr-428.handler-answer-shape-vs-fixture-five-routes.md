# TO IRPT_BCKEND.TO-IB-pr-428 -- five routes: does the handler's own answer have the producer fixture's shape? Read from the handlers' code and their own tests, no live call (read only)

<to_id>IRPT_BCKEND.TO-IB-pr-428</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~287</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>126</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 4801 ("Who reads the live shape: 2.0.0_SA_COO~P2, from the handlers' code and their own response tests, no live call"), on `2.0.0_SA_COO~D2`'s read `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/FIVE_FIXTURES_VS_CONTRACT_20261011.md` @da62c58fa1 | **Decomp cell:** `IB-pr-428` (decomposition section 119) | **outcome_ref:** FWD-2

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-287/` (bash `/c/dev/wk-irpt-bckend-287`). Work only there. **READ ONLY: no AWS call, no live request,
no vendor call, no product source edit. Local reads and local test runs only.**

**The question.** The portal's readers refuse the producer fixtures of five routes. `2.0.0_SA_COO~D2` validated those five fixtures
against the ratified v1 contract: 5 of 5 valid (read that record first; it says what a producer fixture IS: a wrapper whose `instance`
is the PAYLOAD, the `data` member of a response, not the whole envelope). A fixture is a document somebody wrote. What a user's browser
receives is what the HANDLER builds. The CTO asks, per route: does the handler's own answer have the fixture's shape?

| operation | route | function (routes.json `handler`) | producer fixture (`infra/aws/lambda/investor-reporting/_contracts/fixtures/`) |
|---|---|---|---|
| `directory-browse` | `GET /api/scoped/investor-reporting/directory/browse` | irpt-directory-search | `DirectoryPage.valid.json` |
| `analysis-request-history` | `GET /api/scoped/investor-reporting/analysis/requests` | irpt-status | `OwnedAnalysisRequestHistory.valid.json` |
| `analysis-input-upload` | `POST /api/scoped/investor-reporting/analysis/inputs` | irpt-ycharts-generate | `AnalysisUploadResult.valid.json` |
| `custody-report-read` | `GET /api/scoped/investor-reporting/custody-report/{reportId}` | irpt-export-render | `custody-report-read.response.valid.json` |
| `custody-report-persist` | `POST /api/scoped/investor-reporting/custody-report` | irpt-export-render | `custody-report-persist.response.valid.json` |

Confirm each row yourself from `docs/contracts/investor-reporting/v1/routes.json`, the source map
(`infra/aws/lambda/ci/lambda-source-map.json`, the function's `source_dir`) and the function's Terraform `handler`; if a row above is
wrong, say so and use what you read. Response schemas are in `docs/contracts/investor-reporting/v1/responses/`.

**Per route, in this order of preference:**
1. **Find where the answer is built**: the file and line that assembles the response body, and the wrapper that adds the envelope
   (`contract_version`, `operation`, `firm_id`, `data`, and any other member). Name both.
2. **Find the handler's own test that produces a real answer**: a test that calls the handler (or the function that builds the
   answer) and holds its return value. Run it. If a test already validates that return value against the v1 response schema, name it
   and report its result. If none does, take the answer such a test produces (or call the same builder in process, with in-memory
   fakes the existing tests already use; write no new product code) and:
   - validate the whole answer against the route's v1 response schema (`jsonschema` with a `referencing` registry over the v1 schema
     files, the way `_contracts/tests/test_seam_paired.py` `validate_against_response_contract` does it; reuse that function if you can
     import it);
   - compare the SHAPE of its `data` member with the fixture's `instance`: the set of member names at each level, and each member's
     JSON type. Values are not compared. A member present on one side only, or of a different type, is a difference; an optional
     member the schema allows and one side omits is listed and marked `optional_by_schema`.
3. **Verdict**, exactly one of: `SAME_AS_FIXTURE` (same member names and types, allowing schema-optional omissions, and the answer
   validates); `DIFFERS` (name every differing member with both sides' types); `NOT_ESTABLISHED` (no test and no in-process call could
   produce an answer without AWS; say exactly what stops it). A verdict other than `NOT_ESTABLISHED` must rest on a RUN, never on
   reading the code alone.
4. **For the two custody routes also say**: whether the handler's `data` carries `report.accounts` as an array (the portal's
   `validateCustodyReport` requires it, by a worker's reading in the record above; you are not asked to read the portal).

**Control.** Put `comparison-catalogue`, a route the portal DOES read, through the same steps. The issuer expects `SAME_AS_FIXTURE` and has NOT measured it. If it
reads anything else, stop and report with the differing members: either the method or that route's own handler is off, and the
issuer rules which before the five verdicts are used.

**Outputs**, under `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~287/`:
- `IB126-1_handler_shape_vs_fixture.json`: `{method, routes:[{operation, route_key, function, answer_built_at:"<file>:<line>",
  envelope_built_at, envelope_keys:[...], evidence:"existing_test_run"|"in_process_call"|"code_read_only", invocation,
  handler_answer_vs_response_schema:"VALID"|"INVALID"|"NOT_RUN", schema_failure_path, verdict, differing_members:[{path, handler,
  fixture, optional_by_schema}], why_not, custody_report_accounts_is_array}], control:{operation, verdict, evidence, invocation}}`.
- `IB126-1_HANDLER_SHAPE_READ.md`: one page for the CTO, one short paragraph per route and one table. Standard technical English.
  State plainly what this is NOT: it is the handler's answer in process, not a byte read off the live function; the deployed build of
  a function can be older than the tree (say, per function, whether the source map pins the answer-building file to HEAD or to an
  older commit, and if older, that your verdict is for the TREE and what the pinned blob would need for the same verdict).

<criterion id="IB126-1-AC1" cell_refs="IB-pr-428"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r126/p126_cells.py" . IB126-1-AC1</invocation><expect>IB126-1-AC1 PASS</expect></criterion>
<criterion id="IB126-1-AC2" cell_refs="IB-pr-428"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r126/p126_cells.py" . IB126-1-AC2</invocation><expect>IB126-1-AC2 PASS</expect></criterion>
<criterion id="IB126-1-AC3" cell_refs="IB-pr-428"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r126/p126_cells.py" . IB126-1-AC3</invocation><expect>IB126-1-AC3 PASS</expect></criterion>

<expected_criteria>IB126-1-AC1, IB126-1-AC2, IB126-1-AC3</expected_criteria>

## AMENDMENT 1 (2026-10-11 ~12:0xZ, issuer 2.0.0_SA_COO~P2, on row D2-W287-S1): the control is ruled -- the method is sound; the finding is four closed response schemas

The worker's stop was right, and the issuer had said the control's expected reading was not measured. Ruled, inside this
decomposition, on the issuer's own read:
- `_authz/served.py:403` `response_envelope` ALWAYS adds the top-level member `unprojected_grant` (its docstring cites CTO ruling
  @61627f39f9: non-optional on every served response, present at zero).
- Of the 21 v1 response schemas, 17 declare that member. FOUR are closed (`additionalProperties: false`) and omit it:
  `analysis-request-pdf`, `comparison-catalogue`, `custody-report-persist`, `custody-report-read` (issuer's count over
  `docs/contracts/investor-reporting/v1/responses/`).
- So the control's whole answer DIFFERS from its schema on that one envelope member while its `data` member has the fixture's
  shape. That is a finding about four schemas, not a method failure. The portal reads the control route today, so a reader that
  accepts the extra member exists.

The five verdicts may be used, read in two parts. To finish the order:
- Add to EVERY route row and to the control: `data_verdict` (`SAME_AS_FIXTURE`, `DIFFERS` or `NOT_ESTABLISHED`, graded on the `data`
  member alone) and `envelope_schema_gap` (the list of envelope members the handler emits that the route's response schema does not
  admit; an empty list when there is none). Keep `verdict` as you recorded it (the whole answer against the schema).
- Add a top-level `closed_schemas_omitting_unprojected_grant` list: re-count it yourself over the 21 response schemas and report
  your number beside the issuer's four.
- IB126-1-AC3 now passes when the control's `data_verdict` is `SAME_AS_FIXTURE` and its `envelope_schema_gap` names nothing but
  `unprojected_grant`. Any other envelope difference on the control is still a stop.
- The one-page read states the envelope finding in its first paragraph, with the two custody routes' `report.accounts` reading.
- You still fix nothing: no schema, handler or fixture edit. Which side moves on the four schemas is the CTO's ruling.

Inherited state on the branch: `95a6cf46df` (deliverables, rows D2-W287-S1 and -S2, proof with AC3 FAIL).

Gate limb: GATE (viii) grades this modified order (placeholders NONE).

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No AWS call of any kind, no live request, no product source or test edit. A helper
  script you write lives in your deliverables folder.
- **Do not fix anything and do not rule which side moves.** If a handler's answer fails its own response schema, that is a finding and
  a row; you do not edit the handler, the schema or the fixture.
- **Refusal clause:** a route you cannot answer by a run is `NOT_ESTABLISHED` with its reason, never a guess. If the control does not
  read `SAME_AS_FIXTURE`, stop, file a row and report. If a criterion cannot be met as written, stop, file a row and report. Never
  weaken a check; do not edit `p126_cells.py`.
- **Client data:** the answers your runs produce come from synthetic test fakes; write member NAMES and JSON TYPES only, never values.
- **Row ids** are `IRPT_BCKEND-D2-W287-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; check the id is free just before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~287" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~287@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~287 <0.9.0_WK_IRPT_BCKEND~287@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~287/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-428.handler-answer-shape-vs-fixture-five-routes.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 119 (round 126, workstream ~P), cell `IB-pr-428`.
<owned_cells>IB-pr-428</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB126-1-AC1, IB126-1-AC2, IB126-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~287/IRPT_BCKEND.TO-IB-pr-428.handler-answer-shape-vs-fixture-five-routes.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: per route, where the answer is built, the evidence kind and its invocation, the schema result, the
verdict and any differing members; for the two custody routes, whether `report.accounts` is an array; the control's result; per function,
whether the answer-building file is pinned to HEAD or older in the source map; what you did NOT establish; each criterion's last line;
the proof checker's result; any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read-only local read; nothing is built, deployed or written to AWS.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; no route changes, and the five routes' declarations were read by the issuer from docs/contracts/investor-reporting/v1/routes.json (5 of 5 DECLARED; handlers as on the face).
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p126_cells.py dry-run at base box/dell2 on dell2 2026-10-11 ~11:3xZ: AC1 FAIL, AC2 FAIL, AC3 FAIL (no output file); commit-gate clean.
lane: the <paths> block IS the grant; the five routes' handlers are IRPT_BCKEND's.
</preflight>
