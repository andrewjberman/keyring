# TO IRPT_ANLREQ.TO-AR-y-472.overview-pdf-route-resolves-the-retained-opal-pdf-without-a-protected-pdf-ref -- FIX AND PROVE OFFLINE: the status route that opens a request's Opal Overview PDF refuses every real Opal report because it requires a `release.protected_pdf_ref` that only the vendor path writes; resolve the retained Opal PDF through the artifact binding when the ref is absent; vendor path unchanged; no release, no deploy

<to_id>IRPT_ANLREQ.TO-AR-y-472.overview-pdf-route-resolves-the-retained-opal-pdf-without-a-protected-pdf-ref</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~346</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ131</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by the path floor | **Decomp cell:** `AR-y-472` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-9 and FWD-1 (the Opal Overview PDF opens from the ticket) | **depends_on:** AR-y-471's record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~345/PDF_ROUTE_READ.md` (read it first, all four sections), AR-y-470 (the commentary route, the pattern to follow; trunk d8497f8adc5)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~346`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-346` (branch `wk-IRPT_ANLREQ-346`), provisioned by the issuer from the current branch. First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~346 <0.9.0_WK_IRPT_ANLREQ~346@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W346-S<k>`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING, with `spec_asserts` and `world_is` fields. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (ruff clean; no single-letter names `l`, `O`, `I`; no non-ASCII).
- **No AWS call, no network, no push, no deploy.** The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/IRPT_ANLREQ.TO-AR-y-459.run7b-browser-leg-script-re-proved-offline-against-the-advisor-required-form.proof_of_spec.json` (read it first), with `to_id` exactly the order's id, a `controls.mutant` that FIRES and a `controls.determinism` really run; run `python .tools/proof-of-spec-check.py <instance> "AR472-y-AC1,AR472-y-AC2,AR472-y-AC3"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (with the instance, one commit) only on VALID.

### THE CELL (`AR-y-472`, inlined)

*The measured defect (worker 345, row IRPT_ANLREQ-D2-W345-S1, verified by the issuer).* `GET analysis/requests/{REQ}/pdf` (`ops/entry.py:245`, method `pdf` of `infra/aws/lambda/investor-reporting/ops/owned_report.py`, near lines 305-333) opens the report's own PDF. For an OPAL_ENGINE report it requires `report["release"]["protected_pdf_ref"]` to be a dict with `server_only` true (else `ANALYSIS_PDF_NOT_RETAINED`, lines 321-322). The real Opal writer `ycharts/research/opal_producer.py:590-601` persists `"release": {"released_revision": None}` and no `protected_pdf_ref`; the publisher persists it unchanged; the only writers of `protected_pdf_ref` in the tree are the vendor-form ones (`ycharts/generate/resident_worker.py:517-518`, `ycharts/generate/job.py:557-562`). So the route refuses every real Opal report. The report does carry `opal_artifact` = `{sha256 (the PDF bytes'), byte_length, ...}` (`opal_producer.py:593-594`), and the PDF bytes ARE retained (`opal_producer.py:549-552`) and attached to the ticket package as `pdf_ref`. The test `ops/tests/test_pdf_route_real_shapes.py` (worker 345, trunk ee2c94f5532) builds the report through the real producer and currently FAILS with `ANALYSIS_PDF_NOT_RETAINED`; it is the test this cell turns green.

*The change.* In `ops/owned_report.py` `pdf` only. KEEP the existing path exactly as it is whenever `release.protected_pdf_ref` is a dict with `server_only` true (vendor reports and the hand-built Opal fixture: `ops/tests/test_owned_report.py:337-345` must stay green unchanged). WHEN the report is OPAL_ENGINE and `protected_pdf_ref` is absent, resolve the retained Opal PDF the way `commentary_pdf` (same file, near lines 335-380, as fixed by AR-y-470) resolves the commentary PDF: through the repository's artifact binding, not through a ref stored in the report. To do that you must find, by reading, (a) how the Opal Overview PDF is retained: the artifact family (`YCHARTS_OPAL_REPORT` of policy `irpt-ycdgen-research-v1`), and the LOGICAL ID or reference under which `opal_producer.py:549-552` / `ycharts/generate/publisher.py:184-211` retain it and return `opal_artifact_ref`; (b) where that reference is kept so the route can read it for a request (the acceptance record, the report index, or the report's own `opal_artifact.run_record_key`; follow the publisher, `ycharts/generate/acceptance.py` and `report_index.py`); then call `self.requests.artifacts.head(...)` on it exactly as `commentary_pdf` does, require the retained artifact's `family` to be the Opal report family, `byte_length` an int greater than 0, and its `sha256` to EQUAL `report["opal_artifact"]["sha256"]` (this is the binding: the PDF the report describes), read the storage key from the artifact index item as `commentary_pdf` does, run the same final re-authorization (`self.requests._final(...)`), sign with the retained sha and answer `{download_route, sha256, byte_length}` like the existing branch. A request whose Opal PDF cannot be resolved answers `ANALYSIS_PDF_NOT_RETAINED`; a retained PDF whose sha differs from the report's answers `ANALYSIS_PDF_BINDING`. If (a) or (b) cannot be established from source, STOP with a BLOCKING row naming what is missing and change nothing. No other method, route or error text changes.

*Prove.* (1) Change worker 345's test only as far as needed to supply the retained-artifact side of the fake (the real producer's retained PDF through the artifact port its fakes already have), keeping its three tests; the real-shape test now asserts a link signed with the retained PDF's sha, the control (ref present) still passes, the negative (differing sha) still raises `ANALYSIS_PDF_BINDING`; add one test that a request with no retained Opal PDF answers `ANALYSIS_PDF_NOT_RETAINED`. (2) Run the three route test files together: `ops/tests/test_pdf_route_real_shapes.py`, `ops/tests/test_owned_report.py`, `ops/tests/test_commentary_pdf_binding.py`: all pass. (3) `MUTANT_REPORT.txt` in your deliverables: the real-shape test run against `git show ee2c94f5532:infra/aws/lambda/investor-reporting/ops/owned_report.py` in a scratch copy FAILS (record the line). Commit the route edit and the test as ONE commit (message citing AR-y-472), then your deliverables and instance.

*The checks.* In `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~346/`: `check_pdf_route.py` (stdlib only, ruff clean, offline) reads `owned_report.py` by AST and prints `PDF-ROUTE-OK opal_fallback=yes vendor_path_unchanged=yes sha_bound_to_report=yes signs_retained_sha=yes` when the `pdf` method keeps the `protected_pdf_ref` branch as before and adds the artifact-binding fallback with those properties, else `PDF-ROUTE-BAD <why>` (rc 1); `--selftest` mutates the source text in memory (the fallback's sha comparison removed; the vendor branch altered) and prints `CONTROL-FIRES` only when BOTH read BAD.

---

## ACCEPTANCE

<criterion id="AR472-y-AC1" cell_refs="AR-y-472"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ops/tests/test_pdf_route_real_shapes.py infra/aws/lambda/investor-reporting/ops/tests/test_owned_report.py infra/aws/lambda/investor-reporting/ops/tests/test_commentary_pdf_binding.py -q --color=no -p no:cacheprovider 2>&1 | tail -1</invocation><expect>^[0-9]+ passed in </expect></criterion>
<criterion id="AR472-y-AC2" cell_refs="AR-y-472"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~346/check_pdf_route.py</invocation><expect>^PDF-ROUTE-OK opal_fallback=yes vendor_path_unchanged=yes sha_bound_to_report=yes signs_retained_sha=yes$</expect></criterion>
<criterion id="AR472-y-AC3" cell_refs="AR-y-472"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~346/check_pdf_route.py --selftest</invocation><expect>^CONTROL-FIRES$</expect></criterion>

<proof_of_spec>
The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~346/IRPT_ANLREQ.TO-AR-y-472.overview-pdf-route-resolves-the-retained-opal-pdf-without-a-protected-pdf-ref.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-472.overview-pdf-route-resolves-the-retained-opal-pdf-without-a-protected-pdf-ref`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR472-y-AC1,AR472-y-AC2,AR472-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-472</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
infra/aws/lambda/investor-reporting/ops/owned_report.py
infra/aws/lambda/investor-reporting/ops/tests/test_pdf_route_real_shapes.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~346/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-472.overview-pdf-route-resolves-the-retained-opal-pdf-without-a-protected-pdf-ref.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one route method edited (a fallback branch added), one test file extended, checks in the worker deliverables; nothing is released, deployed or run against AWS; the irpt-status release that ships it with AR-y-470 is a later order under a signed pair.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker; the grant the route needs (read of the ycharts_opal_reports family by irpt-status-role) is applied (ledger irpt-status-opal-report-read-20261020).
comp-adversary: RUN -- by reading worker 345's record, the producer and publisher writers and the route against this cell; the lens: the vendor or hand-built-fixture path changed (it must be byte-identical in behaviour), a PDF of another request or family accepted (the artifact binding and owner checks must apply as in commentary_pdf), the binding to the report's own opal_artifact.sha256 dropped (without it any retained PDF of the owner would open), a reference invented instead of read from where the writers store it, a test that hand-types the retained side so it passes on any code. NOT seen (blind): the live artifact index and a real retained Overview; denominator: three criteria.
</preflight>
