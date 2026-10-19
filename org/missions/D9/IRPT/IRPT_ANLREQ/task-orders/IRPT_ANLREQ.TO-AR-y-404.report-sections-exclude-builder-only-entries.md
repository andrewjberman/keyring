# TO IRPT_ANLREQ.TO-AR-y-404.report-sections-exclude-builder-only-entries -- the producer's report document lists no section for a layout entry whose method is BUILDER_ONLY and whose status is not VALUE, so the ticket's report page stops showing 425 empty cards titled "text"; run.json and every VALUE section are unchanged

<to_id>IRPT_ANLREQ.TO-AR-y-404</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~296</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-19</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ65</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the class the L6 path floor implies for a served Lambda module path; the work is producer code and tests in the repository; nothing is built into a package, uploaded, planned or applied by this order)
**Decomp cell:** `AR-y-404` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (the report a staff user reads) | **depends_on:** none (CTO msg 10696, TOP PRIORITY, Andrew-direct defect)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~296`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-296` (branch `wk-IRPT_ANLREQ-296`), provisioned by the issuer from the current branch (sparse). First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~296 <0.9.0_WK_IRPT_ANLREQ~296@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. The worktree may show ` M portal` and a modified `.parquet` fixture: never commit either. A row id has the form `IRPT_ANLREQ-D2-W296-S<k>`; `surfaced_at` = `date -u +%FT%TZ`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (ruff clean: no single-letter names `l`, `O`, `I`; no non-ASCII). Run every invocation under `timeout 120`.
- **NO** build of a package, no upload, no AWS or network call, no change to any file outside `<paths>`.

### THE CELL (AR-y-404, inlined)

*Context.* Andrew's PROD run at 13:43Z (MSTR msg 10692, CTO msg 10696): the report page shows 425 cards titled "text" with method BUILDER_ONLY and reason NOT_IN_THIS_VERSION. Cause: in `infra/aws/lambda/investor-reporting/ycharts/research/opal_producer.py` the function that writes the report document builds `sections` from EVERY layout entry (line 531 at HEAD):

`sections = [_section(by_id[e["id"]], e, computed.get(e["id"]), run_date) for e in entries]`

An entry for a layout element with no computed value and `state == "builder_only"` is made at `_entry` (line 168-171): `{"method": "BUILDER_ONLY", "inputs": [], "coverage": None, "status": "NOT_AVAILABLE", "reason": lo.NOT_IN_THIS_VERSION}`; `_section` (line 174-189) turns it into a section of `section_type` from the element kind (often "text") with `status` NOT_AVAILABLE and `reason` NOT_IN_THIS_VERSION, which the portal renders as an empty card. `run.json` (the `entries` list written at line 511, and `_validation(entries, computed)` at line 567) must stay as it is: the run record keeps every entry.

*The change.* Build `sections` from the entries that are NOT (`e["method"] == "BUILDER_ONLY"` and `e["status"] != "VALUE"`). Nothing else changes: `entries`, `run_doc`, `_validation`, `disclosures`, `settings` and the order of the remaining sections are untouched. If you find an entry with `method == "BUILDER_ONLY"` AND `status == "VALUE"` (a builder-written value, for example a title), KEEP its section (it is a VALUE section, which must not change) and file a BLOCKING surprise row naming its element id; do not drop it.

*What to do.*
1. Make the one-expression change above in `opal_producer.py`, with a one-line comment (AR-y-404) saying why.
2. Add a NEW test file `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer_builder_only_sections.py`, in the style of the existing `test_opal_producer.py` (read it first: it builds a layout map, calls `produce_package` or the function that writes the report document with fake stores, and reads the persisted `document`; reuse its helpers by import or copy, do not invent new fixtures). The test must: (a) use an overview-shaped layout map with at least 3 builder-only text elements, 2 VALUE elements and 1 NOT_AVAILABLE element that is NOT builder-only (a vendor-sourced element outside the budget); (b) call the producer and take `document["sections"]`; (c) assert there are 0 sections whose `method` is `BUILDER_ONLY` and `status` is not `VALUE`; (d) assert every VALUE section equals, byte for byte (`json.dumps(sort_keys=True)`), the same section computed by the unfiltered rule `[_section(...) for e in entries]` taken from the same run (build the unfiltered list in the test from the producer's own `_entry` and `_section` functions); (e) assert the NOT_AVAILABLE non-builder section is still present; (f) assert the run record (`run.json` as the fake object store received it) still lists ALL entries, including the builder-only ones; (g) print the section count before (unfiltered) and after (filtered) with `print`; and (h) the DIFFERENCE CONTROL: assert that the unfiltered list from (d) DOES contain builder-only NOT_AVAILABLE sections, so the test cannot pass on a layout with none.
3. Run the existing producer tests and your new test; commit `opal_producer.py` and the new test (and nothing else) together.
4. On the real overview layout map in the repository (find the map the existing tests or the resident load; do not call any API), run the producer with the existing test fakes and print the section counts before and after the change and the number of builder-only entries in run.json. Put the three numbers in your report. If the real map cannot be loaded offline, say so and report the test fixture's numbers only.
5. Write the proof instance and flip the order only after the checker prints VALID, as the other orders of this project do (copy the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~295/IRPT_ANLREQ.TO-AR-y-402.original-holdings-blob-delete-path-code-and-policy-read.proof_of_spec.json` if it is in your worktree, else `git show HEAD:<that path>`), with `to_id` exactly `IRPT_ANLREQ.TO-AR-y-404`; commit it, then run `python .tools/proof-of-spec-check.py <instance> "AR404-y-AC1,AR404-y-AC2"`; flip `<status>` to `complete` and commit that flip alone only on VALID.

---

## ACCEPTANCE

<criterion id="AR404-y-AC1" cell_refs="AR-y-404"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer_builder_only_sections.py -q --color=no -p no:cacheprovider</invocation><expect>[0-9]+ passed</expect></criterion>
<criterion id="AR404-y-AC2" cell_refs="AR-y-404"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer.py infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer_benchmark.py infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer_page_wording.py infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer_prices.py infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer_swap.py -q --color=no -p no:cacheprovider</invocation><expect>[0-9]+ passed</expect></criterion>

`AR404-y-AC1`: the new test passes, and (inside it) 0 builder-only non-VALUE sections, every VALUE section byte-identical to the unfiltered rule, run.json lists all entries, the difference control sees builder-only sections in the unfiltered list; at base the file is absent ("no tests ran") and it FAILS. `AR404-y-AC2`: the five existing producer test files pass with no `failed` in the summary line (48 passed at base); a summary line containing `failed` or `error` is a FAIL even if it also contains `passed`; if an existing test asserted a section count that included builder-only entries, update THAT assertion in the same commit and say which test and why in your report.

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~296/IRPT_ANLREQ.TO-AR-y-404.report-sections-exclude-builder-only-entries.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-404`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR404-y-AC1,AR404-y-AC2"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-404</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, the deliverables folder `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~296/`, this order's file (status line only) and the surprise investigation file are the only places you write.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/opal_producer.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer_builder_only_sections.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer_benchmark.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer_page_wording.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer_prices.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer_swap.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~296/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-404.report-sections-exclude-builder-only-entries.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a one-expression change to a producer module and a new test in the repository; nothing is built into a package, uploaded, planned, applied or invoked. The change reaches the served report only through a later resident release (a separate pair and an IB2 apply order).
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-adversary: RUN -- by reading opal_producer.py:153-189 and :530-571 against this cell; the lens: dropping a VALUE section whose method is BUILDER_ONLY (the guard keeps it and files a row), editing the entries list so run.json changes (forbidden: the filter sits on the sections comprehension only), a validation count that reads the filtered list (it reads `entries`, unchanged), a test that passes on a layout with no builder-only entries (the difference control), and an existing test that counted all sections. NOT seen (blind): the report schema validator that the resident applies to the persisted document, and any portal code that expects a section per layout element; the worker greps the validator (ReportValidator in infra/aws/lambda/investor-reporting/reports/resident_installed.py and the schema under docs/contracts/investor-reporting/v1/) for a minimum section count or a per-element requirement and reports what it finds; denominator: two criteria.
</preflight>

---

## RECORD FACE

- Cut on the CTO's TOP PRIORITY ruling (msg 10696) after Andrew's PROD run showed 425 "text" cards. The resident release pair and IB2's apply (after 14:15Z) are the issuer's next cells and wait on this one. Base: AR404-y-AC1 FAILS (the test file is absent: "no tests ran"), AR404-y-AC2 PASSES (48 passed in the five existing producer test files).
