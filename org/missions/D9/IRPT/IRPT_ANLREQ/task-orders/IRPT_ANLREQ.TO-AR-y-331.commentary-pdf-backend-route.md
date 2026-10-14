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
2. **The change.** (a) `OwnedAnalysisReader.commentary_pdf(self, principal, request_id, *, signer, data_firm=None)` beside `pdf`: it does EXACTLY what `pdf` does for owner re-read, retention and final re-reads, but resolves the artifact as follows: read the request's acceptance record's `commentary_ref` (the sibling attribute the packager reads, `get_commentary_ref`, or the record's own field, as `opal_packager.handle_commentary_ready` does), take its `sha256`, compute the logical id with `opal_producer.commentary_logical_id(request_id, sha256)` (import it; the naming rule is NOT re-typed; if the irpt-status Lambda's source map does not stage `ycharts/research/opal_producer.py`, add the source-map row the way the neighbouring members are listed and say which file you edited, or STOP with a BLOCKING row if the map is outside your grant), bind the artifact id from the owner, family `YCHARTS_OPAL_REPORT` and that logical id (as `live_retained_package` does), and sign it. A request with no commentary ref, or whose commentary PDF is not retained, is refused with a closed code `COMMENTARY_PDF_NOT_RETAINED` (modelled on `ANALYSIS_PDF_NOT_RETAINED`). (b) `ops/entry.py`: the handler `commentary_pdf` beside `pdf`, and its route, operation, `owner_read_modes` and `record_id_parameters` entries, identical in kind to `analysis-request-pdf`. (c) `reports/status_installed.py`: the same route key in `HISTORY_ROUTES` so the installed table matches. (d) every table or test that lists the operations and pins their count or names (find them from step 1) is updated for the one new operation; no existing operation changes.
3. **The tests** (NEW file `ops/tests/test_commentary_pdf_route.py` if `ops/tests/` exists, else the folder the neighbouring `analysis-request-pdf` tests live in; copy their style and fakes): (a) the owner of a request whose commentary is retained gets a signed URL for the commentary artifact (the fake artifact store records which logical id was read: `<request_id>-commentary-<sha>`); (b) a non-owner of another firm is refused exactly as `pdf` refuses; (c) an OPAL_GLOBAL viewer is admitted as for `pdf`; (d) a request with no commentary ref and a request whose PDF is not retained are refused `COMMENTARY_PDF_NOT_RETAINED`; (e) the route is registered with mode OWNED_RECORD and parameter `requestId` and `HISTORY_ROUTES` carries the same key; (f) a test whose NAME states the scope: `the commentary pdf route serves the commentary artifact, never the report's own pdf`. `before_arm`: run the new tests on the base so (a), (d), (e), (f) FAIL.
4. **Commit** the source and tests; record the full sha and `git diff --stat <base> <commit>` printing exactly the paths you touched.
5. **Write `r41/COMMENTARY_PDF_ROUTE_RECORD.json`**: `base`, `commit`, `files_changed`, `contract` (the operation, route, mode, parameter), `tests` {`added`, `passed`, `failed`, `folders`}, `before_arm`, `source_map_edit` (what you did about the irpt-status source map), `claim`, `not_read` (the live route, the deployed bytes, the concrete authorizer the composition installs).
6. **Write the three checker scripts** named in ACCEPTANCE. In your report: the commit, the counts, the before-arm failures, the source-map decision, every existing test you had to re-pin and why.


### ACCEPTANCE

<criterion id="AR331-y-AC1" cell_refs="AR-y-331"><invocation>python C:/dev/wk-irpt-anlreq-139/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~139/tests_check.py</invocation><expect>^TESTS-OK </expect></criterion>
`AR331-y-AC1`: you write `tests_check.py`: it runs the new test file AND every test file under `infra/aws/lambda/investor-reporting/ops/tests/`, `reports/tests/` and `_authz/tests/` whose name contains `pdf`, `route`, `entry`, `status`, `owned` or `operation` (print the file list), parses the counts, and prints `TESTS-OK <new passed> new, <others passed> others, 0 failed` only when the new file has every case (a) to (f) passing and the others have 0 failed; otherwise `TESTS-BAD <why>` and exit 1.

<criterion id="AR331-y-AC2" cell_refs="AR-y-331"><invocation>python C:/dev/wk-irpt-anlreq-139/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~139/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`AR331-y-AC2` (the one mutant that fails): you write `mutant_check.py`: it copies `ops/owned_report.py` to a scratch folder OUTSIDE the product tree with `commentary_pdf` made to resolve the report's own `protected_pdf_ref` (the `pdf` shape), runs the new test file against the copy (copy first on the import path, with whatever sibling modules the import needs), and prints `MUTANT-FIRES` only when that run FAILS (else `MUTANT-SURVIVES`, exit 1).

<criterion id="AR331-y-AC3" cell_refs="AR-y-331"><invocation>python C:/dev/wk-irpt-anlreq-139/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~139/scope_check.py</invocation><expect>SCOPE-OK</expect></criterion>
`AR331-y-AC3` (a third check, with a reason: the cell adds a served route that a later signed release carries): you write `scope_check.py`: it prints `SCOPE-OK` only when `git diff --name-only <base> HEAD` (`<base>` = the `base` field of your record JSON, the parent of your first commit, printed) lists only files under `infra/aws/lambda/investor-reporting/` (the named source files, tests, the one source-map file if you edited it) and paths under `org/missions/D9/IRPT/IRPT_ANLREQ/`; otherwise `SCOPE-BAD <why>`, exit 1.

<criterion id="AR331-y-AC4J" cell_refs="AR-y-331" judgment="true"/>
`AR331-y-AC4J` (judgment, graded at L9, never by you): the new route serves only the commentary PDF of the request the viewer owns, refuses everyone the report PDF route refuses, widens no existing operation, and the report PDF route is unchanged.

<expected_criteria>AR331-y-AC1 AR331-y-AC2 AR331-y-AC3 AR331-y-AC4J</expected_criteria>

## BOUNDS

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
