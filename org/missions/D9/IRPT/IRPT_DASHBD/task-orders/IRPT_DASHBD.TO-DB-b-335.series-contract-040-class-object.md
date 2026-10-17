# TO IRPT_DASHBD.TO-DB-b-335 -- the SERIES contract 0.4.0 (round 150): the `class_object` section, the class series object `class_series.json.gz` that sits beside `series.json.gz`, with its closed class and coverage vocabularies, the dated-classification rule and the sum test

<to_id>IRPT_DASHBD.TO-DB-b-335</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~261</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>150</round>
<workstream>CONTRACT</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** CONTRACT, round 150 | **Ordered by:** the issuer as the contract's sole writer (C-SEAM), on the shape named to ~F2 and ~S2 in msg 8846 and ~S2's ask in msg 10638 (its route member waits on this file) | **Decomp cell:** `DB-b-335` (decomposition section 196).

**Risk class LOCAL:** a JSON standard, one new test file and eight one-line edits in four existing test files, in a workspace worktree; nothing is built for upload, deployed or written to AWS. The publisher that WRITES the object, the route that serves it and the page that reads it are later cells.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-261` (branch `wk-IRPT_DASHBD-261`, a FULL checkout cut from the current `box/dell2`). Work only there; never push; never commit the workspace `portal` gitlink. ASCII only; LF line endings; counts, hashes and words only (no account id, name or value of a client in anything you write).

**What exists.** `org/standards/IRPT_DASHBD_SERIES_CONTRACT.json` is at `contract_version` 0.3.3. Read it whole, and read the checker `C:/dev/ajb_workspace/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p202_series_contract_040.py` (it states exactly what the three criteria grade, including the reference validator and the key lists).

**The edit (the contract file; TEXTUAL INSERTIONS, no existing line reformatted; at most 4 existing lines may change).**
1. `contract_version` becomes `"0.4.0"`.
2. `lineage` gains ONE entry at the end: `{"contract_version": "0.3.3", "sha256": <sha256 of the 0.3.3 file bytes at the commit before yours>, "note": <one sentence: the bytes of 0.3.3 before the class_object section and files.class_series were added; series and manifest unchanged>}` with exactly those three keys. Every earlier lineage entry stays byte for byte.
3. `files` gains `"class_series"`: a string that names `class_series.json.gz` (one gzip JSON object per account beside the series file, at the builder address `lib.opal_naming.address("irpt", <firm>, "platinum", "reporting", "account=<id>", "class_series.json.gz")`) and the `class_object` section.
4. A new top-level section `class_object` (place it just before `open_changes`) with EXACTLY these keys:
   - `version` "0.4.0"; `file` "class_series"; `shape` (one sentence that says "columnar": `date` and `coverage` are per-day arrays of one length, `market_value_eod` and `class_return_daily` are objects from a class name to a per-day array of that length);
   - `required` = ["account_id","firm","as_of","method_version","schema_version","date","class_names","coverage","market_value_eod","class_return_daily"]; `per_day_arrays` = ["date","coverage"]; `per_class_arrays` = ["market_value_eod","class_return_daily"];
   - `class_names_enum` = ["fixed_income","equity","commodities","structured","alternatives","cash","unclassified","other"]; `coverage_values` = ["CLASSIFIED","UNCLASSIFIED_PRESENT","SOURCE_ABSENT"];
   - `fields`: one object per required key, each with `kind` and `sentence` (the sentence says what the field is, its null rule and its source in plain words); `schema_version` alone carries `"fixed_value": "class_object-0.4.0"`. The `coverage` sentence explains all three values (CLASSIFIED: every held security had a classification row in force; UNCLASSIFIED_PRESENT: at least one had none and sits in the class `unclassified`; SOURCE_ABSENT: the securities read of the account was unavailable that day). The `class_return_daily` sentence says: the class's CONTRIBUTION to the account's daily total return as a decimal fraction, so the classes sum to the account; null on a SOURCE_ABSENT day and on a day whose `total_return_daily` is null; NEVER filled, carried forward or read as zero;
   - `dated_classification_rule`: a sentence containing the phrases "in force", "never by today", "unclassified" and "SOURCE_ABSENT" (a holding is mapped by the classification row in force ON THE DAY, never by today's row; none in force means `unclassified`, nothing is guessed; an unreadable securities read makes the day SOURCE_ABSENT);
   - `sum_test`: exactly `return_tolerance` 1e-9, `value_tolerance_usd` 0.01, `applies_to` (words: every day whose coverage is not SOURCE_ABSENT), `return_rule` (the sum over `class_names` of `class_return_daily` equals the series file's `total_return_daily` on the same date within `return_tolerance`; both null together) and `value_rule` (the sum of `market_value_eod` equals the series file's `value` on the same date within `value_tolerance_usd`);
   - `absent_means`: a sentence starting "no class view" (the page says so and never derives a class from another source; the series file is unaffected).
5. `series`, `manifest`, `open_changes`, `model_windows` and every other section stay byte for byte (the existing optional series keys `class_value`, `class_weight`, `class_names` stay as they are).
6. **The four existing test files that pin the 0.3.3 version and the lineage length fail after step 1 and 2; change them minimally (eight one-line edits in all, at most 24 changed lines in the four files together):** `data/assets/scripts/gold/irpt_reporting/tests/test_series_contract_030.py` (the version assert becomes "0.4.0"; the lineage length 5 becomes 6), `.../test_series_contract_031.py` (the same two), `.../test_income_reason_rename.py` (the version assert; the 0.3.1 entry is now `lineage[-3]`), `.../test_history_scope_claim_contracts.py` (the version assert; the 0.3.2 entry is now `lineage[-2]`). Keep each assertion's meaning; add a short comment naming this order.
7. **Your test file** `data/assets/scripts/gold/irpt_reporting/tests/test_series_contract_040.py` (pytest; no network; ruff target py39 clean; the line `from __future__ import annotations` right after the module docstring, which the commit gate requires of a new `.py`; at least 10 tests; the words `class_object`, `sum_test` and `SOURCE_ABSENT` appear in it). Cover: the version and the lineage entry; `files.class_series`; the required keys; the enums; the sum-test numbers and rules; the dated-classification phrases; that `series` is untouched; and a small validator driven only by the declarations that accepts a valid document and rejects: classes that do not sum to the account return, class values that do not sum to the account value, a number on a SOURCE_ABSENT day, a class outside the enum, a repeated class, a coverage outside its values, a date the series lacks, class returns on a null total.
8. Commit the files with `.tools/safe-commit.sh --author "0.9.0_WK_IRPT_DASHBD~261 <0.9.0_WK_IRPT_DASHBD~261@opal.agent>" -F <msgfile> -- <paths>` (message file written with a non-shell writer; READ the whole gate output). Then run the three invocations below from your worktree root and report each one's last line.

<criterion id="DB202-1-AC1" cell_refs="DB-b-335"><invocation>python -I "C:/dev/ajb_workspace/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p202_series_contract_040.py" C:/dev/wk-irpt-dashbd-261 DB202-1-AC1</invocation><expect>DB202-1-AC1 PASS</expect></criterion>
`DB202-1-AC1` -- the contract differs from the base only in the version, the appended lineage entry (the sha256 of the 0.3.3 bytes), `files.class_series` and the new `class_object` section (which has exactly the declared keys, enums, fixed value, phrases and sum-test numbers); every other key is byte-identical and at most 4 existing lines of the file changed. Base: FAIL.
<criterion id="DB202-1-AC2" cell_refs="DB-b-335"><invocation>python -I "C:/dev/ajb_workspace/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p202_series_contract_040.py" C:/dev/wk-irpt-dashbd-261 DB202-1-AC2</invocation><expect>DB202-1-AC2 PASS</expect></criterion>
`DB202-1-AC2` -- behaviour: a reference validator driven only by the `class_object` declarations accepts four documents and rejects eleven (classes that do not sum, values that do not sum, a number on a SOURCE_ABSENT day, a class outside the enum, a repeat, a coverage outside its values, a date the series lacks, class returns on a null total, a wrong schema version, a short array, a missing key). Base: FAIL.
<criterion id="DB202-1-AC3" cell_refs="DB-b-335"><invocation>python -I "C:/dev/ajb_workspace/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p202_series_contract_040.py" C:/dev/wk-irpt-dashbd-261 DB202-1-AC3</invocation><expect>DB202-1-AC3 PASS</expect></criterion>
`DB202-1-AC3` -- the proof: the new test file (at least 10 tests, ruff clean, the three words), the four pinned contract test files and the publisher's tests pass; the pinned files changed by at most 24 lines; the worker's commits change only the contract, the new test, the four pinned test files, the folder, the investigation file and task-order files. Base: FAIL.

<expected_criteria>DB202-1-AC1,DB202-1-AC2,DB202-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Reads and writes.** Reads: repo files. Writes: your worktree only. No AWS, no Terraform, no upload, no push.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a checker clause is wrong rather than your edit, file a BLOCKING row naming the clause and stop on it.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W261-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`) and BOTH `project` ("IRPT_DASHBD") and `fabric` ("dell2") keys, class OBSERVATION or BLOCKING; append as BYTES. ASCII only.

<paths>
org/standards/IRPT_DASHBD_SERIES_CONTRACT.json
data/assets/scripts/gold/irpt_reporting/tests/test_series_contract_040.py
data/assets/scripts/gold/irpt_reporting/tests/test_series_contract_030.py
data/assets/scripts/gold/irpt_reporting/tests/test_series_contract_031.py
data/assets/scripts/gold/irpt_reporting/tests/test_income_reason_rename.py
data/assets/scripts/gold/irpt_reporting/tests/test_history_scope_claim_contracts.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~261/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-335.series-contract-040-class-object.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 196 (round 150, workstream CONTRACT), cell `DB-b-335`.
<owned_cells>DB-b-335</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB202-1-AC1, DB202-1-AC2, DB202-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~261/IRPT_DASHBD.TO-DB-b-335.series-contract-040-class-object.proof_of_spec.json`
(model it on a sibling instance, e.g. the one in `.../0.9.0_WK_IRPT_DASHBD~260/`). Validate it with `python .tools/proof-of-spec-check.py <instance> DB202-1-AC1,DB202-1-AC2,DB202-1-AC3` BEFORE the status flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it. The status flip to complete is your LAST commit.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; your last workspace commit (git read); the number of existing lines changed in the contract file and in the four pinned test files; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a JSON standard and tests in a branch; nothing is planned, applied or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed; no AWS is written.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; the route that serves the object is another seat's later cell.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; the criteria FAIL at the base, the issuer's reference edit passes all three, and the checker's selftest refuses 30 single-fault arms of the diff clause plus the behaviour and grant clauses.
lane: the <paths> block IS the grant.
</preflight>
