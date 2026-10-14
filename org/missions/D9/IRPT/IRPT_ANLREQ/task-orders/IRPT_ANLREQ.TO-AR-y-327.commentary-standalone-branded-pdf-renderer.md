# TO IRPT_ANLREQ.TO-AR-y-327.commentary-standalone-branded-pdf-renderer -- the AI commentary renders as a STANDALONE branded Opal PDF marked DRAFT, and the packager attaches that PDF (not the combined package PDF); source and tests only, nothing deployed

<to_id>IRPT_ANLREQ.TO-AR-y-327</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~134</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>ZL</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the class the infrastructure `<paths>` imply; source and tests only, the worker deploys NOTHING)
**Decomp cell:** `AR-y-327` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (the fourth attachment) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~134`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-134` (branch `wk-IRPT_ANLREQ-134`), provisioned by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~134 <0.9.0_WK_IRPT_ANLREQ~134@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W134-S<k>` (take the next free `<k>`). The workspace worktree shows ` M portal` (and may show a modified `.parquet` fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit (Python 3.9 syntax). No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. No live call, NO PUSH, no deploy, no upload, no apply, no invoke. Scratch outside the product tree.

### THE CELL (`AR-y-327`, inlined)

*Andrew, verbatim (PRD ADDENDUM v0.10, record `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261014_160xZ_COMMENTARY_STANDALONE_BRANDED_PDF_AND_ATTACHMENTS.md`): "Yes it should be a standalone branded PDF." The package is four STANDALONE items: the original holdings upload, the form selections as filed, the Opal report, and the AI commentary as a standalone branded Opal PDF marked DRAFT. The combined package PDF (the report with a commentary page inside) is NEVER posted as an attachment.*

Today `opal_producer.produce_package` renders the whole Overview PLUS a commentary page as ONE PDF (`package.pdf`), and `opal_packager.handle_commentary_ready` attaches that combined PDF as `pdf_ref`. The commentary is only a page inside it. This cell makes the commentary its own PDF and attaches THAT.

1. **Read first** (all under `C:/dev/wk-irpt-anlreq-134/infra/aws/lambda/investor-reporting/ycharts/research/`): `layout_overview.py` (`build`, about lines 1096-1160, and `_commentary_section`, about line 1079: the branded page with the DRAFT mark and disclaimer), `opal_producer.py` (`produce_package` about lines 237-282, `package_logical_id` about line 232, `_read_stage`, `_address`, `OPAL_FAMILY`, `OPAL_POLICY_REVISION`), `opal_packager.py` (`handle_commentary_ready` about lines 146-199, `_attach` about lines 211-223, `live_retained_package` about lines 234-256), and the existing tests `tests/test_opal_packager.py`, `tests/test_opal_packager_request_id.py`, and any test of `produce_package` / `layout_overview.build` with `commentary=` (find them with a name search inside `ycharts/research/tests/`). Record in your report what each of `build(..., commentary=)` appends (page, DRAFT mark, disclaimer, logo) so the standalone PDF reuses the same elements.
2. **The layout.** In `layout_overview.py` add a new function `build_commentary_only(run_doc, brand, commentary, pricing=True)` (or an equivalent keyword on `build` that your tests pin) that returns the HTML of a document whose ONLY body is the commentary: the same brand, logo, DRAFT mark, Opal disclaimer and page chrome that `_commentary_section` gives today, no Overview section, no holdings table, no charts. `build(...)` with `commentary=None` is byte-identical to what it was (a test pins it); `build(..., commentary=...)` is unchanged too (the combined layout may stay in the code; it is simply no longer posted).
3. **The producer.** In `opal_producer.py` add `commentary_logical_id(request_id, commentary_sha256)` returning `"%s-commentary-%s" % (request_id, commentary_sha256)` and `produce_commentary_pdf(request_ref, firm, stores, commentary, *, commentary_sha256=None)`, shaped like `produce_package` (same store-required checks, same `_read_stage` for the run document, same `render`, same `_address` call with object name `commentary.pdf` of the same family, same artifacts-port branch with family `OPAL_FAMILY` and the new logical id, same return shape `{"pdf_ref", "sha256", "byte_length", "key", "ref"}`). It renders `build_commentary_only`. Do not change `produce` or `produce_package`.
4. **The packager.** In `opal_packager.py`, `handle_commentary_ready` calls `produce_commentary_pdf` (the default port; the `produce_package` port name in `ports` may stay as an alias only if an existing test needs it, and then you say which) and `live_retained_package` asks the store for the NEW logical id (`commentary_logical_id`). The attach payload keys are UNCHANGED: `pdf_ref` now carries the I7 ref of the standalone commentary PDF (no combined PDF is rendered, retained or attached by this path). Update the module docstring's step 5 and 6 to say so, and update the existing tests that pinned the combined package so they pin the standalone commentary PDF.
5. **The tests** (NEW file `ycharts/research/tests/test_commentary_standalone_pdf.py`; copy the style of the neighbouring tests; run with `python -m pytest <file>` from the folder those tests run in, as the existing ones do): (a) `build_commentary_only` HTML contains the commentary text, the DRAFT mark and the disclaimer text and contains NO Overview marker (assert the absence of a section marker `build` emits for the holdings table; find it in step 1); (b) `build(..., commentary=None)` equals the pre-change output for a fixture (compare with the same call on `origin`'s copy of the file via a pinned expected string or hash computed on the base and recorded in the test); (c) `produce_commentary_pdf` through the injected fakes retains the PDF under `<request_id>-commentary-<sha>` and returns the I7 ref; (d) `handle_commentary_ready` with fakes calls the commentary producer, NEVER `produce_package`, and its attach payload's `pdf_ref` is the canonical string of that ref; (e) a retained commentary PDF means no render and the attach of the stored ref (the existing idempotence case, re-pinned); (f) a test whose NAME states the scope: `the commentary is a standalone branded PDF; the combined package PDF is never produced by the packager`. `before_arm`: run the new tests on the base (stash nothing: use a scratch copy of the three files from `HEAD~0` before your edit) so (a), (c), (d), (f) FAIL.
6. **Commit** the source, the updated tests and the new test in your worktree; record the full sha and `git diff --stat <base> <commit>` printing exactly the paths you touched.
7. **Write `r41/COMMENTARY_PDF_RENDERER_RECORD.json`** in your deliverable folder: `base`, `commit`, `files_changed`, `layout_elements_reused` (step 1), `tests` {`added`, `passed`, `failed`, `folders`}, `before_arm`, `what_a_person_sees` (the commentary PDF in words: pages, DRAFT mark, disclaimer, brand), `claim`, `not_read` (the live engine's rendered bytes: the issuer renders one sample at close; the ticket service's reading of `pdf_ref`).
8. **Write the three checker scripts** named in ACCEPTANCE into your deliverable folder. In your report: the commit, the counts, the layout elements reused, the before-arm failures, and every existing test you had to re-pin and why.

### ACCEPTANCE

<criterion id="AR327-y-AC1" cell_refs="AR-y-327"><invocation>python C:/dev/wk-irpt-anlreq-134/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~134/tests_check.py</invocation><expect>^TESTS-OK </expect></criterion>
`AR327-y-AC1`: you write `deliverables/0.9.0_WK_IRPT_ANLREQ~134/tests_check.py`: it runs the new test file AND every existing test file in `ycharts/research/tests/` whose name contains `packager`, `producer` or `layout` (print the file list), parses the counts, and prints `TESTS-OK <new passed> new, <others passed> others, 0 failed` only when the new file has every case (a) to (f) passing and the others have 0 failed; otherwise `TESTS-BAD <why>` and exit 1. A failing test OUTSIDE the grant that your change causes is a BLOCKING row.

<criterion id="AR327-y-AC2" cell_refs="AR-y-327"><invocation>python C:/dev/wk-irpt-anlreq-134/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~134/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`AR327-y-AC2` (the one mutant that fails): you write `mutant_check.py`: it copies `opal_packager.py` to a scratch folder OUTSIDE the product tree with the call changed back to `produce_package` (the combined shape), runs the new test file against the copy, and prints `MUTANT-FIRES` only when that run FAILS (else `MUTANT-SURVIVES`, exit 1).

<criterion id="AR327-y-AC3" cell_refs="AR-y-327"><invocation>python C:/dev/wk-irpt-anlreq-134/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~134/scope_check.py</invocation><expect>SCOPE-OK</expect></criterion>
`AR327-y-AC3` (a third check, with a reason: the cell edits shared producer code that a later resident release carries): you write `scope_check.py`: it prints `SCOPE-OK` only when `git diff --name-only <base> HEAD` in the worktree lists only `layout_overview.py`, `opal_producer.py`, `opal_packager.py` under `infra/aws/lambda/investor-reporting/ycharts/research/`, test files under `infra/aws/lambda/investor-reporting/ycharts/research/tests/`, and paths under `org/missions/D9/IRPT/IRPT_ANLREQ/` (`<base>` = the `base` field of your `r41/COMMENTARY_PDF_RENDERER_RECORD.json`, the commit your branch started from, which you take as the parent of your first commit of this order and print); otherwise `SCOPE-BAD <why>`, exit 1.

<criterion id="AR327-y-AC4J" cell_refs="AR-y-327" judgment="true"/>
`AR327-y-AC4J` (judgment, graded at L9, never by you): the commentary renders as its own branded Opal PDF marked DRAFT with the disclaimer, the packager attaches only that PDF, no combined PDF is produced on this path, and the Overview/report path is untouched.

<expected_criteria>AR327-y-AC1 AR327-y-AC2 AR327-y-AC3 AR327-y-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~134/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else. The ticket service (`infra/aws/lambda/ticket_center/`), the resident worker and the portal are NOT in this cell.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py
infra/aws/lambda/investor-reporting/ycharts/research/opal_producer.py
infra/aws/lambda/investor-reporting/ycharts/research/opal_packager.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-327</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~134/IRPT_ANLREQ.TO-AR-y-327.commentary-standalone-branded-pdf-renderer.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-327`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR327-y-AC1,AR327-y-AC2,AR327-y-AC3,AR327-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- source and tests in a worktree outside the product tree's live deploy; nothing is landed, pushed, deployed or called. A later resident release (a signed never-widen pair) carries these members; this cell widens nothing.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed; the attach payload keys are unchanged. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading PRD ADDENDUM v0.10, C-PACKAGER, and the packager's code against the cell; the lens: a combined package still produced and attached, a changed attach payload shape the ticket service refuses, a second logical id colliding with the package's, a commentary page that still carries the Overview, and a DRAFT mark or disclaimer lost. The cell requires one standalone PDF, unchanged payload keys, a distinct logical id, no Overview marker in the HTML and the DRAFT mark and disclaimer kept. NOT seen: the live engine's rendered bytes, how the ticket service and the portal read `pdf_ref`.
</preflight>

---

## RECORD FACE

- Cut on PRD v0.11 (signed both halves) and the CTO's round-41 path (msg 7723, item 5 as restated by ADDENDUM v0.10 item 2). Workstream `ZL` of round 40. Base: `AR327-y-AC1`, `AC2` and `AC3` FAIL as expected (no checker files).
- The standalone PDF travels in the existing `pdf_ref` field, so the ticket service is unchanged; its page reader is the next cell (portal) and reads `pdf_ref` as the commentary PDF. The resident release that carries `layout_overview.py`, `opal_producer.py` and `opal_packager.py` is a later cell under its own pair.
