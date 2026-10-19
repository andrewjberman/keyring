# TO IRPT_ANLREQ.TO-AR-y-412.not-in-this-version-tests-agree-with-trunk-as-built -- REPAIR (test file only): the five failing tests of AR-y-408 count ~G2's per-holding price-table element, so they pass on trunk as built

<to_id>IRPT_ANLREQ.TO-AR-y-412</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~307</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-19</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ72</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by the path floor (a test file under infra/); in fact one test file, no deploy, no AWS call, no producer change
**Decomp cell:** `AR-y-412` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (a clean report) | **depends_on:** `AR-y-408` (merged `31c3dc1d4f`), `AR-g-166` (merged `3b589f17ea`, ~G2); CTO msg 11011 (the one LOCAL repair cell under the pause)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~307`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-307` (branch `wk-IRPT_ANLREQ-307`), provisioned by the issuer from the current branch. First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~307 <0.9.0_WK_IRPT_ANLREQ~307@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture: never commit it. A row id has the form `IRPT_ANLREQ-D2-W307-S<k>`; `surfaced_at` = `date -u +%FT%TZ`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (ruff clean; no non-ASCII).
- **No AWS call, no network, no push.** You edit ONE product file, the test file named below. You do NOT edit `opal_producer.py`, `layout_overview.py` or any map: the product code is right as built; the tests are what disagree with it.

### THE CELL (AR-y-412, inlined)

*Context.* `AR-y-408` (worker 299, merged `31c3dc1d4f`) made the Opal report document drop sections whose entry is not shown (builder-only, or reason NOT_IN_THIS_VERSION) and add ONE last disclosure `NOT_SHOWN` that counts them (`opal_producer.py`: `_not_shown`, `NOT_SHOWN_ID`, `NOT_SHOWN_TEXT`, the `dropped` list). Its test file is `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer_not_in_this_version.py` (9 tests, 163 lines). `AR-g-166` (~G2, merged `3b589f17ea`) then added to every Opal report one more layout element, `opal.prices.holdings` (the per-holding price table, appended after the last page by `_price_table_element`; it reads NOT_IN_THIS_VERSION when pricing is off and is therefore dropped and counted like any other such entry). On trunk the file now reads `5 failed, 4 passed`: `test_the_fixture_has_the_composition_the_test_claims`, `test_run_json_still_lists_every_entry`, `test_exactly_one_not_shown_disclosure_comes_last_and_counts_the_dropped_entries`, `test_no_not_shown_disclosure_when_nothing_is_dropped`, `test_difference_control_the_unfiltered_list_holds_both_kinds`. Measured by the issuer on `003fae44dd`: the failures are the extra element (a list that now ends in `opal.prices.holdings`, a count one higher, a disclosure that appears where the test expects none).

*What to do.*
1. Read the test file and the producer functions it exercises (`build_report_document`-level code that builds `entries`, `sections` and `disclosures`; `_price_table_element`; `_not_shown`). Change ONLY the test file so each of the five tests states what the producer, as built on trunk, must do WITH the price-table element counted: its id in the expected entry list, the dropped count one higher where it is NOT_IN_THIS_VERSION, and where a test asserts "no NOT_SHOWN disclosure when nothing is dropped" build its fixture so that the price-table element is present as a VALUE (pricing on) or make the assertion about the fixture's own entries, whichever keeps the test's stated intent. Keep every test's name. Do not weaken an assertion to make it pass: each must still FAIL against a copy of the producer without the 408 filter (the difference control, see 3).
2. Print the test file's `git diff --stat` and the pytest line before and after.
3. Proof instance (copy the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~306/IRPT_ANLREQ.TO-AR-y-406.resident-release-r34l-build-only-two-movers.proof_of_spec.json`; read it first, `git show HEAD:<path>` if absent) at the path below, `to_id` exactly `IRPT_ANLREQ.TO-AR-y-412`, with `controls.mutant` = the corrected test file run against a temporary copy of `opal_producer.py` with the `_not_shown` filter removed from the `sections` line (it must FAIL, say how many tests) and `controls.determinism` = the corrected file run twice, equal. Commit it, run `python .tools/proof-of-spec-check.py <instance> "AR412-y-AC1,AR412-y-AC2"`, and flip `<status>` to `complete` (commit alone) only on VALID.

You also write `check_412_bound.py` in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~307/` (a small script, ruff clean): it takes the branch point `git merge-base HEAD box/dell2`, lists `git diff --name-only <that> HEAD` and keeps the paths NOT under `org/`; it prints `AR412-BOUND-OK files=1` only when that kept list is exactly the one test file named above, otherwise `AR412-BOUND-BAD <paths>` and a non-zero exit. Run it before your first edit (it must print BAD or error: no change yet) and after.

---

## ACCEPTANCE

<criterion id="AR412-y-AC1" cell_refs="AR-y-412"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer_not_in_this_version.py -q --color=no -p no:cacheprovider</invocation><expect>9 passed</expect></criterion>
<criterion id="AR412-y-AC2" cell_refs="AR-y-412"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~307/check_412_bound.py</invocation><expect>AR412-BOUND-OK files=1</expect></criterion>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~307/IRPT_ANLREQ.TO-AR-y-412.not-in-this-version-tests-agree-with-trunk-as-built.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-412`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR412-y-AC1,AR412-y-AC2"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-412</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer_not_in_this_version.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~307/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-412.not-in-this-version-tests-agree-with-trunk-as-built.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one test file; no producer, layout, map, Lambda, resident or host moves; nothing deployed.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-adversary: RUN -- by reading the test file's failures on `003fae44dd` against this cell; the lens: a test weakened until it passes (the difference control must fail the corrected file against a producer without the 408 filter), a producer edit riding a test repair (the bound script allows exactly one non-org file), a fixture that hides the price-table element instead of counting it. NOT seen (blind): the release pin, where the producer is held at 404+408 only (r34l pin C) and the price-table element does not exist; the file is correct for trunk, not for that pin; denominator: two criteria.
</preflight>
