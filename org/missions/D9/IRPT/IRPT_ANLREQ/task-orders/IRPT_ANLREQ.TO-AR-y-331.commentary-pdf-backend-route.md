# TO IRPT_ANLREQ.TO-AR-y-331.commentary-pdf-backend-route -- the backend route that serves the standalone commentary PDF to the ticket page: operation analysis-request-commentary-pdf, same owner gate as the report PDF route; source and tests only, nothing deployed

<to_id>IRPT_ANLREQ.TO-AR-y-331</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~139</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>ZQ</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the class the `<paths>` imply; source and tests only, the worker deploys NOTHING)
**Decomp cell:** `AR-y-331` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** `AR-y-327` (merged `6240c0530d`), `AR-y-329` (merged `23cac5266d`)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~139`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-139` (branch `wk-IRPT_ANLREQ-139`), provisioned by the issuer. Commit WORKSPACE files with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~139 <0.9.0_WK_IRPT_ANLREQ~139@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W139-S<k>` (take the next free `<k>`). The workspace worktree shows ` M portal` (and may show a modified `.parquet` fixture): never commit either to the WORKSPACE repository. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax). No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. No live call, NO PUSH, no deploy, no upload, no apply, no invoke, no AWS call. Scratch outside the product tree.

### THE CELL (`AR-y-331`, inlined)

*PRD ADDENDUM v0.10: the ticket page opens the AI commentary as a standalone branded PDF. `AR-y-329` (read, merged; record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~137/r41/COMMENTARY_PDF_ROUTE_READ.json`, read it first) found that the existing route `GET /api/scoped/investor-reporting/analysis/requests/{requestId}/pdf` (operation `analysis-request-pdf`) returns the ANALYSIS report's own `release.protected_pdf_ref` and never the commentary PDF that `AR-y-327` retains. This cell adds ONE sibling operation that serves the commentary PDF, under the same owner gate.*

The contract (fixed; the portal cell `AR-y-332` is cut against it): operation `analysis-request-commentary-pdf`, route `GET /api/scoped/investor-reporting/analysis/requests/{requestId}/commentary-pdf`, mode `OWNED_RECORD`, path parameter `requestId`, the same response shape as `analysis-request-pdf` (`{signedUrl, ...}` as that method returns today), the same refusals by name.

1. **Read first** (under `C:/dev/wk-irpt-anlreq-139/infra/aws/lambda/investor-reporting/`): the record above (`q1`, `q2`, `q4` with their evidence); `ops/owned_report.py` (`OwnedAnalysisReader.pdf`, about lines 292-320, and the helpers it uses: owner re-read, retention, final re-reads, signer); `ops/entry.py` (`pdf` handler about lines 215-217, routes about 240, operations 244-245, `owner_read_modes` 250, `record_id_parameters` 252); `reports/status_installed.py` (`HISTORY_ROUTES`, about lines 57-64, whose comment says it must match `ops/entry.py`); `ycharts/research/opal_producer.py` (`commentary_logical_id`, about line 237, added by `AR-y-327`; `OPAL_FAMILY`); `ycharts/research/opal_packager.py` (`live_retained_package`, which shows how the packager binds an artifact id from owner, family and logical id and reads it with `artifacts.head`); and the authorization table that lists operations (find with a name search for `analysis-request-pdf` over `infra/aws/lambda/investor-reporting/_authz/` and `_contracts/`; tests such as `_authz/tests/test_svc_custody_statement.py` line about 138 list the same route).
2. **The change.** (a) `OwnedAnalysisReader.commentary_pdf(self, principal, request_id, *, signer, data_firm=None)` beside `pdf`: it does EXACTLY what `pdf` does for owner re-read, retention and final re-reads, but resolves the artifact as follows: read the request's acceptance record's `commentary_ref` (the sibling attribute the packager reads, `get_commentary_ref`, or the record's own field, as `opal_packager.handle_commentary_ready` does), take its `sha256`, compute the logical id with a LOCAL helper in `ops/owned_report.py` (AMENDMENT 1, below: the irpt-status Lambda stages no `opal_producer.py`, so the rule is not imported there), bind the artifact id from the owner, family `YCHARTS_OPAL_REPORT` and that logical id (as `live_retained_package` does), and sign it. A request with no commentary ref, or whose commentary PDF is not retained, is refused with a closed code `COMMENTARY_PDF_NOT_RETAINED` (modelled on `ANALYSIS_PDF_NOT_RETAINED`). (b) `ops/entry.py`: the handler `commentary_pdf` beside `pdf`, and its route, operation, `owner_read_modes` and `record_id_parameters` entries, identical in kind to `analysis-request-pdf`. (c) `reports/status_installed.py`: the same route key in `HISTORY_ROUTES` so the installed table matches. (d) every table or test that lists the operations and pins their count or names (find them from step 1) is updated for the one new operation; no existing operation changes.
3. **The tests** (NEW file `ops/tests/test_commentary_pdf_route.py` if `ops/tests/` exists, else the folder the neighbouring `analysis-request-pdf` tests live in; copy their style and fakes): (a) the owner of a request whose commentary is retained gets a signed URL for the commentary artifact (the fake artifact store records which logical id was read: `<request_id>-commentary-<sha>`); (b) a non-owner of another firm is refused exactly as `pdf` refuses; (c) an OPAL_GLOBAL viewer is admitted as for `pdf`; (d) a request with no commentary ref and a request whose PDF is not retained are refused `COMMENTARY_PDF_NOT_RETAINED`; (e) the route is registered with mode OWNED_RECORD and parameter `requestId` and `HISTORY_ROUTES` carries the same key; (f) a test whose NAME states the scope: `the commentary pdf route serves the commentary artifact, never the report's own pdf`; (g) the CROSS-CHECK test required by AMENDMENT 1. `before_arm`: run the new tests on the base so (a), (d), (e), (f) FAIL.
4. **Commit** the source and tests; record the full sha and `git diff --stat <base> <commit>` printing exactly the paths you touched.
5. **Write `r41/COMMENTARY_PDF_ROUTE_RECORD.json`**: `base`, `commit`, `files_changed`, `contract` (the operation, route, mode, parameter), `tests` {`added`, `passed`, `failed`, `folders`}, `before_arm`, `source_map_edit` (what you did about the irpt-status source map), `claim`, `not_read` (the live route, the deployed bytes, the concrete authorizer the composition installs).
6. **Write the three checker scripts** named in ACCEPTANCE. In your report: the commit, the counts, the before-arm failures, the source-map decision, every existing test you had to re-pin and why.


### ACCEPTANCE

<criterion id="AR331-y-AC1" cell_refs="AR-y-331"><invocation>python C:/dev/wk-irpt-anlreq-139/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~139/tests_check.py</invocation><expect>^TESTS-OK </expect></criterion>
`AR331-y-AC1` (AMENDED by AMENDMENT 2): you write `tests_check.py`: it runs the new test files AND every test file under `infra/aws/lambda/investor-reporting/ops/tests/`, `reports/tests/`, `_authz/tests/` and `_contracts/tests/` (print the file list), parses the failing test NAMES, and compares them with the failing names recorded in `r41/baseline_failures.json`, which you take ONCE at the start from a clean `git worktree add --detach` at your base commit outside the product tree (a full worktree, not an archive; remove it after). It prints `TESTS-OK <new passed> new, <others passed> others, <n> baseline failures unchanged, 0 new failures` only when every case of the new files passes and every failing name is in the baseline; otherwise `TESTS-BAD <why>` and exit 1.

<criterion id="AR331-y-AC2" cell_refs="AR-y-331"><invocation>python C:/dev/wk-irpt-anlreq-139/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~139/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`AR331-y-AC2` (the one mutant that fails): you write `mutant_check.py`: it copies `ops/owned_report.py` to a scratch folder OUTSIDE the product tree with `commentary_pdf` made to resolve the report's own `protected_pdf_ref` (the `pdf` shape), runs the new test file against the copy (copy first on the import path, with whatever sibling modules the import needs), and prints `MUTANT-FIRES` only when that run FAILS (else `MUTANT-SURVIVES`, exit 1).

<criterion id="AR331-y-AC3" cell_refs="AR-y-331"><invocation>python C:/dev/wk-irpt-anlreq-139/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~139/scope_check.py</invocation><expect>SCOPE-OK</expect></criterion>
`AR331-y-AC3` (a third check, with a reason: the cell adds a served route and widens what the PDF signer may sign, and a later signed release carries both; AMENDED by AMENDMENT 2): you write `scope_check.py`: it prints `SCOPE-OK` only when `git diff --name-only <base> HEAD` (`<base>` = the `base` field of your record JSON, the parent of your first commit, printed) lists only files under `infra/aws/lambda/investor-reporting/` (the named source files incl. `ops/pdf_link.py`, tests), `docs/contracts/investor-reporting/v1/routes.json`, the one new response schema file named below, and paths under `org/missions/D9/IRPT/IRPT_ANLREQ/`; AND `git diff <base> HEAD -- infra/aws/lambda/investor-reporting/ops/pdf_link.py` changes the `FAMILIES` tuple by exactly one added family `YCHARTS_OPAL_REPORT` (plus what the destination check needs, nothing else), AND `git diff <base> HEAD -- docs/contracts/investor-reporting/v1/routes.json` only ADDS one route row and raises the `_denominator` `declared` and `total` counts by one each, AND the only other path under `docs/` is the NEW file `docs/contracts/investor-reporting/v1/responses/analysis-request-commentary-pdf.response.schema.json`; otherwise `SCOPE-BAD <why>`, exit 1.

<criterion id="AR331-y-AC4J" cell_refs="AR-y-331" judgment="true"/>
`AR331-y-AC4J` (judgment, graded at L9, never by you): the new route serves only the commentary PDF of the request the viewer owns, refuses everyone the report PDF route refuses, widens no existing operation, and the report PDF route is unchanged.

<expected_criteria>AR331-y-AC1 AR331-y-AC2 AR331-y-AC3 AR331-y-AC4J</expected_criteria>

## BOUNDS

- **AMENDMENT 3 (2026-10-14 ~19:2xZ, 2.0.0_SA_COO~Y2; gate limb: none stated; row `IRPT_ANLREQ-D2-W139-S7` answered; criterion AC3 amended above; row S8 acknowledged).** The third pass left ONE failing name outside the baseline: `_contracts/tests/test_seam_paired.py::test_control_a_known_good_document_conforms_and_a_known_bad_one_does_not[analysis-request-commentary-pdf]`, because a DECLARED route needs a response contract file and the census pin counts declared routes. The ruling: the grant ALSO names (1) the NEW file `docs/contracts/investor-reporting/v1/responses/analysis-request-commentary-pdf.response.schema.json`, modelled on `responses/analysis-request-pdf.response.schema.json` with the operation const changed to `analysis-request-commentary-pdf` and nothing else different (read how the neighbour is written; the response is the same `{signedUrl, ...}` shape), and (2) in `routes.json` the `_denominator` counts (`declared` 22 to 23, `total` 24 to 25 as the file now reads; raise each by one) and the route row's `response_schema` field pointing at the new file instead of the absence reason you set. Change nothing else under `docs/`. After this the `[analysis-request-commentary-pdf]` case must PASS and the failing set must equal the baseline set. The `FAMILY_REVISION` mapping you added in `pdf_link.py` (S8) is accepted as part of the stated widening: keep it in the record's `widening`.
- **INHERITED STATE.** Branch `wk-IRPT_ANLREQ-139` holds commits `d9013483dc`, `e322a3fbfb`, `7ea150fb25`, `97560c8c7b`. READ them, add the two items, amend `scope_check.py` for the amended AC3, re-run `tests_check.py` (it must print TESTS-OK), re-run the proof check, flip the status only when `tests_check.py` prints TESTS-OK AND the proof prints VALID. The next free row is S10.

- **AMENDMENT 2 (2026-10-14 ~19:0xZ, 2.0.0_SA_COO~Y2; gate limb: none stated; rows `IRPT_ANLREQ-D2-W139-S2` and `-S3` answered; criteria AC1 and AC3 amended above).** The worker built the route and its tests and stopped, correctly, on two facts. (S3) `ops/pdf_link.py` `PdfSigner.sign` refuses any family outside `FAMILIES` (`ORIGINAL_VENDOR_PDF`, `ORIGINAL_HOLDINGS`, `ORIGINAL_CSV`; lines about 19-21 and 86-87) with `PDF_LINK_FAMILY`, so in production the route cannot sign the commentary artifact; the unit tests passed on a recording fake. (S2) the route is declared by the entry but is not a row of `docs/contracts/investor-reporting/v1/routes.json`, so `_authz/tests/test_unguarded_census.py::test_every_entry_carries_the_published_route_table_it_serves` fails. The ruling: the grant ALSO names `infra/aws/lambda/investor-reporting/ops/pdf_link.py` and `docs/contracts/investor-reporting/v1/routes.json`, with these limits. (1) In `pdf_link.py` add ONE family, `YCHARTS_OPAL_REPORT`, to `FAMILIES`, and make whatever destination check the signer performs for a family (the stored blob key must equal the key `reporting_destination` gives for that family and logical id; read how it is done for the existing families) hold for it too; NOTHING else changes in the file. THIS IS A WIDENING of what the signer may sign (it can then sign the Opal report family's artifacts under the same owner and retention re-reads); state it in your record under `widening` with the exact diff, and add tests that the signer still refuses an unknown family and that a commentary key whose destination does not match is refused. (2) In `routes.json` publish the new route as ONE added row modelled on the row of `analysis-request-pdf` (operation, handler, mode, parameter, response contract as that row has it); change no other row. (3) The `_contracts/tests` suite has failures you could not compare to a clean base: take the baseline from a clean `git worktree add --detach <base>` (a FULL worktree, never an archive), record the failing NAMES in `r41/baseline_failures.json`, and make sure your change adds NO failing name to `_contracts/tests`, `_authz/tests`, `ops/tests` or `reports/tests`; a baseline failure is not yours to fix.
- **INHERITED STATE (the slot is re-seated).** The branch holds the first worker's commits `2a535a7859` (route, helper, tests), `f9ec0f7ecf` (checkers, record, rows S1 to S6) and `4f2263c400` (proof instance). READ them, keep what is right, add the two grant items above with their tests, amend the checkers for the amended AC1 and AC3, update the record (`widening`, `baseline`), re-run the proof check, flip the status only when it prints VALID. Rows S2 and S3 are answered; the next free row is S7. Row S4 (the owner gate follows `persist_inputs` and does not call `read()`, so no READY report is required) and S5 stand as observations.

- **AMENDMENT 1 (2026-10-14 ~18:2xZ, 2.0.0_SA_COO~Y2; gate limb: none stated; row `IRPT_ANLREQ-D2-W139-S1` answered).** The first worker of slot 139 stopped, correctly: the irpt-status Lambda's source map (`infra/aws/lambda/ci/lambda-source-map.json`, the `irpt-status` entry) stages none of `opal_producer.py`, `held_data.py`, `layout_overview.py`, `runner.py`, `keeper.py`, and each staged file is bound by a pin and a sha256, so the source map and the shared `_keys/keys.py` are NOT touched by this cell. The ruling: `ops/owned_report.py` carries a small LOCAL helper `_commentary_logical_id(request_id, commentary_sha256)` returning `"%s-commentary-%s" % (request_id, commentary_sha256)` and a local constant for the family name `YCHARTS_OPAL_REPORT` (use the family constant `owned_report.py` or `repository.py` already exposes if one exists, and say which). NO import of `ycharts/research/opal_producer.py` into any `ops/` module. The drift is guarded by a CROSS-CHECK test (g) in a test file that CAN import both (under `infra/aws/lambda/investor-reporting/ycharts/research/tests/`, which is added to the grant: the new file `test_commentary_logical_id_matches_ops.py`): it asserts `opal_producer.commentary_logical_id(r, s) == owned_report._commentary_logical_id(r, s)` for three (request_id, sha) pairs and `opal_producer.OPAL_FAMILY ==` the local family constant. The source-map edit named in the first version of step 2 is NOT done. The existing operation pins the previous worker named (`reports/tests/test_status_installed.py` lines about 95 and 105, `_authz/tests/test_svc_custody_statement.py` line about 138) are inside the grant: update them for the one new operation.
- **INHERITED STATE.** The slot is re-seated; the previous worker built nothing and committed only its blocking row (`8bc810e18d`, `IRPT_ANLREQ-D2-W139-S1`, now answered). The next free row is S2.

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~139/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
infra/aws/lambda/investor-reporting/ops/owned_report.py
infra/aws/lambda/investor-reporting/ops/entry.py
infra/aws/lambda/investor-reporting/reports/status_installed.py
infra/aws/lambda/investor-reporting/ops/tests/
infra/aws/lambda/investor-reporting/reports/tests/
infra/aws/lambda/investor-reporting/_authz/tests/
infra/aws/lambda/investor-reporting/_contracts/tests/
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_commentary_logical_id_matches_ops.py
infra/aws/lambda/investor-reporting/ops/pdf_link.py
docs/contracts/investor-reporting/v1/responses/analysis-request-commentary-pdf.response.schema.json
infra/aws/lambda/investor-reporting/ops/tests/
docs/contracts/investor-reporting/v1/routes.json
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-331</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~139/IRPT_ANLREQ.TO-AR-y-331.commentary-pdf-backend-route.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-331`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR331-y-AC1,AR331-y-AC2,AR331-y-AC3,AR331-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- source and tests in a worktree; nothing is landed, pushed, deployed or called. The route is served only after a later resident release under a signed never-widen pair.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed by the worker; any route this cell adds is source only and is served only after a later signed release. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the CTO's ADDENDUM v0.10 and the route read against the cell; the lens: a route that serves another firm's commentary, a route that skips the retention or owner re-reads that `pdf` performs, a logical-id rule typed a second time, a changed `analysis-request-pdf`, an operation count pinned elsewhere left stale. The cell requires the same owner gate, the naming function imported, the report route untouched and a before-arm that fails. NOT seen (blind): the live system and the deployed bytes; denominator: 6 test cases (a) to (f), 1 new operation, 3 route tables.
</preflight>


---

## RECORD FACE

- Cut on the CTO's ADDENDUM v0.10 item 2 and the route read (`AR-y-329`, merged `23cac5266d`). Workstream `ZQ` of round 40. Base: `AR331-y-AC1`, `AC2`, `AC3` FAIL as expected (no checker files).
- The members it changes (`ops/`, `reports/status_installed.py`) are members of the resident package AND the irpt-status Lambda package; the issuer carries them in the single resident release and decides the Lambda leg at that cell.
