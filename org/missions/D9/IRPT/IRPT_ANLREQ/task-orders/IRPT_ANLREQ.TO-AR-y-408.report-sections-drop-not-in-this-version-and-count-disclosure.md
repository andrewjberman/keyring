# TO IRPT_ANLREQ.TO-AR-y-408.report-sections-drop-not-in-this-version-and-count-disclosure -- the producer's report document also lists no section for a layout entry whose status is not VALUE and whose reason is NOT_IN_THIS_VERSION, and gains ONE disclosure line with the count of the entries it did not list; proven on the real multi-comparison map (the variant of Andrew's report), where the first fix leaves about 144 entries

<to_id>IRPT_ANLREQ.TO-AR-y-408</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~299</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-19</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ68</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the class the L6 path floor implies for a served Lambda module path; the work is producer code and tests only, nothing is built into a package or applied by this order)
**Decomp cell:** `AR-y-408` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (a clean report) | **depends_on:** `AR-y-404` (merged `3676d5836b`), CTO ruling `RULING_REPORT_425_TEXT_CARDS_DROP_BUILDER_ONLY_SECTIONS_20261019.md` ADDENDUM 1 (msg 10759)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~299`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-299` (branch `wk-IRPT_ANLREQ-299`), provisioned by the issuer from the current branch (sparse; the producer, the tests, the maps and the contract schemas are present). First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~299 <0.9.0_WK_IRPT_ANLREQ~299@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture: never commit it. A row id has the form `IRPT_ANLREQ-D2-W299-S<k>`; `surfaced_at` = `date -u +%FT%TZ`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (ruff clean: no single-letter names `l`, `O`, `I`; no non-ASCII). Run every invocation under `timeout 120`.
- **NO** package build, no upload, no AWS or network call, no change outside `<paths>`.

### THE CELL (AR-y-408, inlined)

*Context.* `AR-y-404` (merged `3676d5836b`) made `infra/aws/lambda/investor-reporting/ycharts/research/opal_producer.py` build `sections` without the entries `e` where `e["method"] == "BUILDER_ONLY" and e["status"] != "VALUE"` (read the comprehension after your base, just under the comment `AR-y-404`). Andrew's page (the issuer read the request item: tenant 49financial, request `REQ-d6231c013ae90519c67d18e9`, `report_variant` `multicomp`) shows 425 empty cards; the multi map `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/multi_map.json` has 424 elements, of which 280 have `source` BUILDER_ONLY and 144 have a source object. The first fix therefore leaves cards for entries that are `NOT_AVAILABLE` with reason `NOT_IN_THIS_VERSION` (the `lo.NOT_IN_THIS_VERSION` constant, set at `_entry` for a vendor-sourced element with no value, and by `closed_reason` at lines 140-150). The CTO ruling (ADDENDUM 1, msg 10759): the report lists neither of them; other `NOT_AVAILABLE` reasons stay as cards; `disclosures[]` gains ONE line with the count of the dropped entries.

*The change.*
1. `sections` is built from the entries that are NOT dropped, where an entry is dropped when `e["status"] != "VALUE"` and (`e["method"] == "BUILDER_ONLY"` or `e["reason"] == lo.NOT_IN_THIS_VERSION`). A `VALUE` entry is never dropped (if you find a VALUE entry with method BUILDER_ONLY or reason NOT_IN_THIS_VERSION, keep it and file a BLOCKING row naming its element id). `entries`, `run_doc`, `run.json`, `_validation(entries, computed)`, `settings` and the order of the remaining sections stay as they are.
2. Let `dropped` be the number of dropped entries. When `dropped > 0`, append ONE disclosure `{"disclosure_id": <a new constant NOT_SHOWN_ID, "NOT_SHOWN">, "text": <a new constant NOT_SHOWN_TEXT % dropped>}` to `disclosures` AFTER every existing disclosure (including the pricing, benchmark, risk-free, weighting and swap ones), in every branch that builds `disclosures` (the priced and the unpriced one). The text states the count in plain words, for example `"%d report elements that this version of the report does not produce are not listed."`; no vendor word, no time-budget word (the Opal-form page wording rule, see `test_opal_producer_page_wording.py`). When `dropped == 0` no disclosure is added.
3. Check, before you rely on a new `disclosure_id`, that the report document validators and schemas accept it: read `ReportValidator` in `infra/aws/lambda/investor-reporting/reports/resident_installed.py` (about lines 212-252) and the disclosures definition in `docs/contracts/investor-reporting/v1/AnalysisReport.schema.json` and `infra/aws/lambda/investor-reporting/_contracts/AnalysisReport.v2.schema.json` (is `disclosure_id` free text, an enum or a pattern; is `text` length-bounded). If the id or the text length would be refused, use the closest accepted form and say so; if no accepted form exists, STOP with a BLOCKING row (do not edit a schema).

*What to do.*
1. Make the change with one-line comments (AR-y-408). Extend the existing test file `tests/test_opal_producer_builder_only_sections.py` or add `tests/test_opal_producer_not_in_this_version.py` (your choice) to assert, on an overview-shaped fixture with 3 builder-only elements, 2 VALUE elements, 2 vendor-sourced elements that resolve `NOT_IN_THIS_VERSION`, and 1 `NOT_AVAILABLE` element with another closed reason (an `INPUT_MISSING:` reason): 0 sections with method BUILDER_ONLY, 0 sections with reason NOT_IN_THIS_VERSION, every VALUE section byte-equal (`json.dumps(sort_keys=True)`) to the unfiltered rule, the other-reason `NOT_AVAILABLE` section still present, run.json still listing ALL entries, exactly one disclosure with id `NOT_SHOWN` whose text carries the number of dropped entries and which comes last, and no such disclosure when nothing is dropped; plus the DIFFERENCE CONTROL (the unfiltered list does contain both kinds, so the test cannot pass on a layout with none). Update any existing assertion that counted all sections or compared the disclosures list exactly, and say which and why in your report.
2. On the REAL maps (find them under `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/`; read them from the file; do not call any API), run the producer with the existing test fakes for the `multi_map.json` (the variant of Andrew's report, 424 elements) and the `overview_map.json` and the `comparison_map.json`, and print for each map: entries, sections before the first fix (the unfiltered count), sections after AR-y-404, sections after this change, the dropped count, the number of sections whose method is BUILDER_ONLY and whose reason is NOT_IN_THIS_VERSION in the final list (both 0), the status counts of the remaining sections, and the disclosure line's text. If a real map cannot be run offline with the test fakes (the multi map needs an input the fixtures lack), say exactly what is missing and run the largest part you can (for example the entry and section functions over the element list with empty computed values), labelling it as that. Put the numbers in your report.
3. Run the five existing producer test files and your new/extended test; commit `opal_producer.py` and the tests (nothing else) together.
4. Write the proof instance and flip the order only after the checker prints VALID: copy the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~296/IRPT_ANLREQ.TO-AR-y-404.report-sections-exclude-builder-only-entries.proof_of_spec.json` (it exists in your worktree after the merge; else `git show HEAD:<path>`) with `to_id` exactly `IRPT_ANLREQ.TO-AR-y-408` and real `controls.mutant` (the new test run against a copy of the producer with the NOT_IN_THIS_VERSION clause removed must FAIL) and `controls.determinism` (the new test twice, the same result); commit it, run `python .tools/proof-of-spec-check.py <instance> "AR408-y-AC1,AR408-y-AC2"`, and flip `<status>` to `complete` (commit alone) only on VALID.

---

## ACCEPTANCE

<criterion id="AR408-y-AC1" cell_refs="AR-y-408"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer_not_in_this_version.py -q --color=no -p no:cacheprovider</invocation><expect>[0-9]+ passed</expect></criterion>
<criterion id="AR408-y-AC2" cell_refs="AR-y-408"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer.py infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer_benchmark.py infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer_page_wording.py infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer_prices.py infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer_swap.py infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer_builder_only_sections.py -q --color=no -p no:cacheprovider</invocation><expect>[0-9]+ passed</expect></criterion>

The new test for this cell is the file `tests/test_opal_producer_not_in_this_version.py` (a NEW file; put the new assertions there, not in the AR-y-404 file, so `AR408-y-AC1` can fail at base: at base the file is absent and pytest prints "no tests ran"). `AR408-y-AC2`: the five existing producer test files and the AR-y-404 test file pass with no `failed` or `error` (50 passed at base).

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~299/IRPT_ANLREQ.TO-AR-y-408.report-sections-drop-not-in-this-version-and-count-disclosure.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-408`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR408-y-AC1,AR408-y-AC2"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-408</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, the deliverables folder, this order's file (status line only) and the surprise investigation file are the only places you write.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/opal_producer.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer_not_in_this_version.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer_benchmark.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer_page_wording.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer_prices.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer_swap.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer_builder_only_sections.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~299/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-408.report-sections-drop-not-in-this-version-and-count-disclosure.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- producer code and tests in the repository; nothing is built into a package, uploaded, planned, applied or invoked. The change reaches the served report only through the resident release (TO-AR-y-406 rebuilt at a later pin, a separate pair).
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-adversary: RUN -- by reading opal_producer.py:140-189 and :530-571 and the AR-y-404 merge against this cell; the lens: dropping a VALUE section (never), a validator or schema that refuses the new disclosure id or text (step 3 reads them first), a disclosure placed before the existing ones (it comes last), a count that disagrees with the dropped sections (the test compares them), run.json changing (it lists all entries), and the multi map not runnable offline (said, not hidden). NOT seen (blind): the portal's reading of the disclosures list; denominator: two criteria.
</preflight>

---

## RECORD FACE

- Cut on the CTO's ruling (ADDENDUM 1 to `RULING_REPORT_425_TEXT_CARDS_DROP_BUILDER_ONLY_SECTIONS_20261019.md`, msg 10759) after the issuer read Andrew's request variant (`multicomp`, request `REQ-d6231c013ae90519c67d18e9`, accepted 2026-10-17T05:14:30Z; no newer request exists in the three tenants' request tables, so the 13:43Z filing is not an accepted request). It rides the r34l resident release as a mover (the build cell `TO-AR-y-406` is rebuilt at the pin that contains this merge). Base: `AR408-y-AC1` FAILS (the test file is absent), `AR408-y-AC2` PASSES.
