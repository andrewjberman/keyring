# TO IRPT_DASHBD.TO-DB-b-295 -- the PUBLISHER writes the history-scope pair (round 149, CTO ruling msg 9226): publisher 0.4.0 carries `history_scope_claim` = `inferred` and `history_scope_basis` from the NEWEST gold row to the series; both publish handlers read the conditional gold column only from a partition that has it

<to_id>IRPT_DASHBD.TO-DB-b-295</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~238</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>149</round>
<workstream>HSPUB</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** HSPUB, round 149 | **Ordered by:** 1.0.0_SA_CTO~DELL2, msg 9226 ("carry history_scope_claim = inferred, with the method 'first value day vs source floor'", "in the same drain as the unreported-days writer") | **Decomp cell:** `DB-b-295` (decomposition section 156).

**Risk class WORLD** is the floor of the paths below (`infra/` paths): python in a branch, no Terraform command, no AWS write, no build for upload, no run of a handler against S3, no push. The source-map re-pin, the build, the apply and the republish are later cells and signed pairs.

**AMENDMENT 1 (issuer 2.0.0_SA_COO~D2, 2026-10-16 ~11:0xZ, on worker row IRPT_DASHBD-D2-W238-S1; gate limb: GATE (viii), an existing order modified with placeholders NONE unchanged; one path added to the grant, no criterion id or cell change):** the row is a DEFECT OF THE ISSUER'S GRANT: `reporting-publish/tests/test_handler_unreported.py` (cell `DB-b-292`'s test, carried into your tree) also pins the publisher version `0.3.0` and the 0.4.0 bump forces its pin; it is added to the grant as a fourth pinned test, inside the same 20-line ceiling. Change ONLY the pinned version strings, finish AC3, the record, the proof instance and the flip.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-238` (branch `wk-IRPT_DASHBD-238`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~238/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value. Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~238/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** The producers (cell `DB-b-294`) now write the conditional gold column `history_scope_claim` = `inferred` beside a derived `history_scope`; the series contract 0.3.3 (cell `DB-b-293`, already in your tree) declares the pair `history_scope_claim` + `history_scope_basis` (the fixed text `first value day vs source floor`) as optional series fields with `history_scope_rule`. Nothing yet carries the claim from the gold row to the series. A value must carry its claim in a field a consumer can reject on: this cell is that carriage. A gold partition written BEFORE the derivation has no such column, so a series built from it must make no statement, and a handler must not fail on it.

**The cell (`DB-b-295`).** Three code edits, one test file and a few forced version-pin lines; nothing else.
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p163_publisher_pair.py` (your three criteria; `check_publisher` and `check_handlers` are the exact spec); `infra/aws/lambda/investor-reporting/reporting-publish/publisher.py` (`PUBLISHER_VERSION`, `GOLD_COLUMNS`, `build_series` and its income-claim tail, `validate_against_contract`, `_income_claim_failures`); `infra/aws/lambda/investor-reporting/reporting-publish/handler.py` (`_read_rows`); `infra/aws/lambda/investor-reporting/reporting-publish-cot/handler.py` (`_read_partition`); `org/standards/IRPT_DASHBD_SERIES_CONTRACT.json` (0.3.3: `history_scope_rule`, the two new fields).
2. **The publisher (`publisher.py`).** (a) `PUBLISHER_VERSION = "0.4.0"`. (b) Constants beside `INCOME_CLAIM`: `HISTORY_SCOPE_CLAIM_KEY = "history_scope_claim"`, `HISTORY_SCOPE_BASIS_KEY = "history_scope_basis"`, `HISTORY_SCOPE_CLAIM = "inferred"`, `HISTORY_SCOPE_BASIS = "first value day vs source floor"`, and `GOLD_CONDITIONAL_COLUMNS = (HISTORY_SCOPE_CLAIM_KEY,)`. `GOLD_COLUMNS` does NOT change and does not name the claim. (c) In `build_series`, at the end (after the income claim): read the claim of the NEWEST row (`rows[-1]`, after the leading rows are trimmed); when it is not None it must equal `HISTORY_SCOPE_CLAIM`, else `PublishRefused` naming the key and the word; when it equals it, the series gets `history_scope_claim` and `history_scope_basis` (both, in that order, after the existing keys). A null or absent claim writes NO pair; a claim on older rows only writes no pair. (d) `validate_against_contract` gains a call to a new helper `_history_scope_failures(series, contract)`: both keys or neither (a lone field is a failure), and each equal to the contract's `series.fields.<key>.fixed_value` (the module constant when the contract declares none). Nothing else in the file changes.
3. **The two handlers.** `reporting-publish/handler.py` `_read_rows` and `reporting-publish-cot/handler.py` `_read_partition` read `publisher.GOLD_COLUMNS` plus each of `publisher.GOLD_CONDITIONAL_COLUMNS` that the partition's own Parquet schema names (`pq.read_schema(io.BytesIO(body)).names`): a legacy partition has no such column and must neither fail nor write a pair. Nothing else in either file changes (the 49 Financial handler already carries the unreported-days change of cell `DB-b-292`).
4. **The tests** `infra/aws/lambda/investor-reporting/reporting-publish/tests/test_history_scope_pair.py` (new, at least 10 passing tests, self-contained: synthetic rows and fake S3, no AWS, no private data). They assert at least: the pair on a newest row with the claim; no pair for rows without the key, with a null claim, or with the claim on older rows only; the claim on the newest row only writes the pair; a foreign claim word is refused; the validator accepts the pair and refuses a lone claim, a lone basis, another claim word and a free-text basis; `PUBLISHER_VERSION` and `GOLD_CONDITIONAL_COLUMNS`; `GOLD_COLUMNS` unchanged; each handler's read on a partition with the column, on one without it and on a mix.
5. **The forced pin lines.** Four existing tests pin the publisher version: `reporting-publish/tests/test_publisher_claim_calendar.py`, `reporting-publish/tests/test_publisher_unreported.py`, `reporting-publish/tests/test_handler_unreported.py` (cell `DB-b-292`'s, carried into your tree) and `reporting-publish-cot/tests/test_handler.py` (if it pins it). Change ONLY the pinned version strings the 0.4.0 bump forces, at most 20 lines in all (additions plus deletions, as `git diff --numstat` counts them), each commented with this order's id. Any other failure of an earlier test is a BLOCKING row and you stop.
6. **Run the checks yourself before the record:** `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p163_publisher_pair.py" . DB163-1-AC1`, then AC2, then AC3.
7. **Record** `RD_HISTSCOPE_PUBLISHER_FACTS_R149.json` in your folder with EXACTLY these fields: `publisher_version` ("0.4.0"); `pair` (["history_scope_claim", "history_scope_basis"]); `newest_row_decides` (true); `handlers` (["reporting-publish", "reporting-publish-cot"]); `pinned_test_lines` (the number of changed lines you made in the four pinned tests, as `git diff --numstat` counts them against your base); `tests` (the count of passing tests of your new file); `words` (one paragraph, 80 to 1800 characters: what changed and why, that a legacy partition makes no statement, and what is NOT proven: nothing is built, uploaded or republished, the two source-map entries are stale after this cell and are re-pinned by a later cell, and no producer has written the claim to S3 yet).

<criterion id="DB163-1-AC1" cell_refs="DB-b-295"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p163_publisher_pair.py" . DB163-1-AC1</invocation><expect>DB163-1-AC1 PASS</expect></criterion>
`DB163-1-AC1` -- publisher 0.4.0 writes `history_scope_claim` = inferred and `history_scope_basis` (the fixed text) when the NEWEST gold row carries the claim, writes no pair for rows without it, with a null claim or with a claim on older rows only, refuses any other claim word, and validates the pair against series contract 0.3.3 (a lone field, another word or a free-text basis fail). Base: FAIL.
<criterion id="DB163-1-AC2" cell_refs="DB-b-295"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p163_publisher_pair.py" . DB163-1-AC2</invocation><expect>DB163-1-AC2 PASS</expect></criterion>
`DB163-1-AC2` -- both publish handlers, on a fake S3 holding synthetic gold, read the conditional column only from a partition that has it: with the claim in every partition (or only the newer ones) the series carry the pair, with legacy gold none, and every manifest says publisher 0.4.0. Base: FAIL.
<criterion id="DB163-1-AC3" cell_refs="DB-b-295"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p163_publisher_pair.py" . DB163-1-AC3</invocation><expect>DB163-1-AC3 PASS</expect></criterion>
`DB163-1-AC3` -- the new test file holds at least 10 passing tests; the publisher and Cottonwood handler test directories pass with at most 20 forced version-pin lines; the worker's commits change only the publisher, the two handlers, the new test file, the four pinned tests, the folder, the investigation file and task-order files; the facts record equals the checker's recount. Base: FAIL.

<expected_criteria>DB163-1-AC1,DB163-1-AC2,DB163-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the contracts, the producers, the source map, the portal, the issuer's check files.
- **Reads and writes.** Reads: repo files. No network, no AWS call, no run of a handler against S3, no deploy, no push. Writes: the repo files of the grant and your private folder.
- **Client data.** None is involved; fixtures are synthetic.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a checker clause is wrong rather than your edit, file a BLOCKING row naming the clause and stop on it.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W238-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements). Write files with LF line endings (write bytes).

<paths>
infra/aws/lambda/investor-reporting/reporting-publish/publisher.py
infra/aws/lambda/investor-reporting/reporting-publish/handler.py
infra/aws/lambda/investor-reporting/reporting-publish-cot/handler.py
infra/aws/lambda/investor-reporting/reporting-publish/tests/test_history_scope_pair.py
infra/aws/lambda/investor-reporting/reporting-publish/tests/test_publisher_claim_calendar.py
infra/aws/lambda/investor-reporting/reporting-publish/tests/test_publisher_unreported.py
infra/aws/lambda/investor-reporting/reporting-publish/tests/test_handler_unreported.py
infra/aws/lambda/investor-reporting/reporting-publish-cot/tests/test_handler.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~238/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-295.publisher-writes-history-scope-pair.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 156 (round 149, workstream HSPUB), cell `DB-b-295`.
<owned_cells>DB-b-295</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB163-1-AC1, DB163-1-AC2, DB163-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~238/IRPT_DASHBD.TO-DB-b-295.publisher-writes-history-scope-pair.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB163-1-AC1,DB163-1-AC2,DB163-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the changed functions in one line per file; the test count and the number of pinned-test lines changed; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: python in a branch; no handler is run against S3 and nothing is deployed, so no served output moves; the republish is a later signed pair.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS is read or written and no grant changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the behaviour clauses were validated by the issuer against a scratch reference of the edits (green: AC1 and AC2) and 11 single-fault mutants (all red).
lane: the <paths> block IS the grant.
</preflight>
