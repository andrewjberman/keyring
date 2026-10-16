# TO IRPT_DASHBD.TO-DB-b-302 -- the HOP-2 READER of the 49 Financial publish function (CTO ruling msg 9439): `read_filled_report_gold` composes a client's filled report from the gold table `filled_report_values`; the publisher's validator accepts the contract's per-window `window_status` (row S123); the publish role's read and list grant gains the one prefix (round 149)

<to_id>IRPT_DASHBD.TO-DB-b-302</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~243</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>149</round>
<workstream>FILLEDRD</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** FILLEDRD, round 149 | **Ordered by:** the CTO's ruling msg 9439 on row `IRPT_BCKEND-D2-S222` (the hop-2 reader is a stub that raises `NotYetAvailable`; it is owed once hop 1's first write lands) and the issuer's finding row `IRPT_DASHBD-D2-S123` | **Decomp cell:** `DB-b-302` (decomposition section 164).

**Risk class WORLD** is the floor of the paths below (`infra/` paths). One cell, three code files, one Terraform file, tests: in a branch; no Terraform command, no AWS call, no push. The filled-report switch STAYS OFF; the re-pin, the signed deploy pair and the switch are later cells.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-243` (branch `wk-IRPT_DASHBD-243`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~243/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; use synthetic ids in tests. **Before every commit, scan what you stage for a client figure and for long identifier runs; the commit gate's client-data list is absent on this box, so that scan is yours.** **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends.** Tool calls that carry a backslash-r or backslash-n escape inside a shell heredoc can be altered in transit: write patch scripts to a file with the Write tool and run them.

**Why.** In `infra/aws/lambda/investor-reporting/reporting-publish/handler.py` (block `FILLED-REPORT-A`) the function `read_filled_report_gold(firm, client_id)` raises `NotYetAvailable` always, so the hop-2 pass can never write a client's `filled_report.json`. The gold table `filled_report_values` (one partition per day, `date=<as_of>/data.parquet`, columns `firm, household_ref, as_of, member_id, row_key, series_name, point_date, value_number, value_text, absent_kind, absent_reason, contract_version, schema_version`, written by `reporting-gold`) is the reader's input. Two findings ride in this cell: (1) the table keys rows by `household_ref` = the sha256 hex of the household's relationship id, while the pass keys by client id; the firm's directory (`read_directory(s3, directory_bucket(firm))`, entries with `ids.client_id`, `ids.relationship_id`) joins the two; (2) `publisher.validate_filled_report` requires an account entry's `window_status` to be ONE of three words, while the contract and the table carry it per window (`qtd`, `ytd`, `last_12_months`, `since_inception`, each one of the three words), so the validator would refuse every real document (row S123); and (3) the publish role reads only the returns and method gold prefixes, so the reader's LIST and GET of the filled prefix would be denied.

**The cell (`DB-b-302`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p170_filled_reader.py` (your three criteria; `check_diff`, `check_behaviour` and `check_tests` are the exact spec, including the fake S3 that allows only `list_objects_v2`, `get_paginator` and `get_object`); `infra/aws/lambda/investor-reporting/reporting-publish/handler.py` (the `FILLED-REPORT-A` blocks, `read_directory`, `directory_bucket`, `_split`, `opal_naming`) and `publisher.py` (the second `FILLED-REPORT-A` block); `data/assets/scripts/gold/irpt_reporting/filled_report_values.py` (`to_rows`, `_leaf`, `_one_document`, `rows_to_document`: the inverse you COPY, never import, because that module is not in the Lambda bundle); `infra/aws/terraform/investor-reporting/reporting-publish/locals.tf`; the existing tests in `reporting-publish/tests/test_filled_report_publish.py`.
2. **handler.py (ONLY inside the FIRST `FILLED-REPORT-A` block; every byte outside it, the switch, `run_filled_report`, `filled_report_fire`, `filled_report_enabled`, stays).** Replace `read_filled_report_gold` with `read_filled_report_gold(firm, client_id, s3=None, directory=None)` and add private helpers as needed inside the block: (a) `s3` defaults to a boto3 S3 client created INSIDE the function; `directory` defaults to `read_directory(s3, directory_bucket(firm))`. (b) The client's `ids.relationship_id` comes from the directory entry whose `ids.client_id` equals `client_id`; none (the client is absent, or the entry has no relationship id) raises `NotYetAvailable` BEFORE any gold read. (c) `household_ref` = `hashlib.sha256(str(relationship_id).encode("utf-8")).hexdigest()`. (d) The gold prefix comes from `opal_naming.address("irpt", firm, "gold", "filled_report_values", ...)` (never a typed bucket or key); list its `date=` partitions with `s3.list_objects_v2(Bucket, Prefix, Delimiter="/")` following `IsTruncated` and `NextContinuationToken` to the last page; none raises `NotYetAvailable`. (e) Read ONLY the newest partition's `data.parquet` with `s3.get_object` (pyarrow imported inside the function), keep the rows whose `household_ref` equals the client's; none raises `NotYetAvailable`. (f) Compose the document `{household, values}` with a COPY of the producer's inverse (`_leaf`, `_one_document`: the household's `first_data_date`, one account entry per `row_key` of `account.last4`, `account.first_data_date` and `account.window_status.<window>` rows with `window_status` an object of the four windows, the values by member as a number, a text, the absent form `{absent, kind}`, a `by_row` map, or a list of `{name, points}` series). A household that cannot be composed (a household-grain member with more than one row, a missing key) raises `publisher.PublishRefused`, never `ValueError`. (g) The function calls ONLY `list_objects_v2` and `get_object` on the client: no write of any kind. (h) The filled-report switch and the pass stay as they are.
3. **publisher.py (ONLY inside the SECOND `FILLED-REPORT-A` block, `validate_filled_report` and a new constant).** Add `FILLED_WINDOWS = ("qtd", "ytd", "last_12_months", "since_inception")` beside `FILLED_WINDOW_STATUS`, and make an account entry's `window_status` valid only when it is an object whose keys are EXACTLY those four windows and whose values are each one of `FILLED_WINDOW_STATUS`; any other form (the old single word, a missing or extra window, an unknown word, a null) raises `PublishRefused`. `publish_filled_report`, `report_address`, `_filled_value_ok`, `_filled_absent_ok` and everything outside the block stay byte for byte (`PUBLISHER_VERSION` does not change).
4. **locals.tf (ONE file of the Terraform root, two added lines).** Add the local `irpt_rp_gold_table_filled  = "filled_report_values"` after `irpt_rp_gold_table_method` (same alignment) and add `"irpt/${local.irpt_rp_firm}/gold/${local.irpt_rp_gold_table_filled}/",` as the THIRD entry of `irpt_rp_gold_read_prefixes` (after the returns and method entries). The object arns and the list conditions are built from that list and stay as they are; the write arns stay. Nothing else in the root changes (`iam.tf`, `lambda.tf`, `main.tf`, `schedule.tf`, and the source map, stay byte for byte). Write the file as bytes with LF.
5. **Tests.** In `test_filled_report_publish.py`: the synthetic `_doc()` account entries take the per-window `window_status` object (the old one-word form is now refused), the test that asserts the shipped reader raises is REMOVED, and every remaining test passes. Add `reporting-publish/tests/test_filled_report_reader.py` with at least EIGHT tests over synthetic ids and a fake S3, including tests whose names contain `present`, `absent` and `refused` (the document of a household from the newest partition; no partition; no rows for the household; a client without a relationship id and a client not in the directory, each raising before any read; a household with a duplicated household-grain member raising `PublishRefused`; the pass publishing one document at the builder address; the validator refusing the one-word form).
6. **Run the checks yourself before the record:** `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p170_filled_reader.py" . DB170-1-AC1`, then AC2, then AC3.
7. **Record** `RD_FILLED_READER_FACTS_R149.json` in your folder with EXACTLY these fields: `files_changed` (the repo-relative paths you changed, sorted); `reader_signature` ("read_filled_report_gold(firm, client_id, s3=None, directory=None)"); `mapping_rule` (one sentence: client to relationship id to sha256 hex to household_ref); `validator_change` (one sentence); `grant_change` (one sentence: the one read prefix); `tests_added` (the names of the new tests); `words` (one paragraph, 80 to 1800 characters: what changed and why, and what is NOT proven: nothing was deployed, the switch is off, the id-space match between the directory's relationship ids and the table's household refs is unmeasured until hop 1's first write, and no plan was run for the grant).

<criterion id="DB170-1-AC1" cell_refs="DB-b-302"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p170_filled_reader.py" . DB170-1-AC1</invocation><expect>DB170-1-AC1 PASS</expect></criterion>
`DB170-1-AC1` -- the diff: `handler.py` and `publisher.py` change only inside their `FILLED-REPORT-A` block (the switch, the pass, the inline branch and the series path stay byte for byte); `locals.tf` gains exactly the filled table local and its read prefix as the third list entry; the other root files, `publisher.py` outside its block and the source map are byte-identical to the base. Base: FAIL.
<criterion id="DB170-1-AC2" cell_refs="DB-b-302"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p170_filled_reader.py" . DB170-1-AC2</invocation><expect>DB170-1-AC2 PASS</expect></criterion>
`DB170-1-AC2` -- behaviour over a fake S3: the reader returns the contract document of the client's household from the newest partition only (paged listing, other households ignored) and it validates; every absent form raises `NotYetAvailable` (no partition, no rows, no relationship id, client not in the directory) and the last two read nothing; a malformed household raises `PublishRefused`; the reader writes nothing and calls only list and get; the pass writes one object at the builder address; the validator accepts the per-window form and refuses the one-word form, a missing window, an extra window, an unknown word and a null. Base: FAIL.
<criterion id="DB170-1-AC3" cell_refs="DB-b-302"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p170_filled_reader.py" . DB170-1-AC3</invocation><expect>DB170-1-AC3 PASS</expect></criterion>
`DB170-1-AC3` -- the stub test is gone, the new test file holds at least eight tests including present, absent and refused, and both test files pass under pytest. Base: FAIL.

<expected_criteria>DB170-1-AC1,DB170-1-AC2,DB170-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Reads and writes.** Reads: repo files. No network, no AWS call, no Terraform command, no push. Writes: the three code files, the Terraform file, the two test files and your private folder.
- **Client data.** None is involved: tests use synthetic ids.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a checker clause is wrong rather than your edit, file a BLOCKING row naming the clause and stop on it.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W243-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`) and BOTH `project` ("IRPT_DASHBD") and `fabric` ("dell2") keys, class OBSERVATION or BLOCKING; append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them, and READ the whole gate output: a refused commit leaves your edit uncommitted and blocks every other seat's merge. ASCII only in anything you write.

<paths>
infra/aws/lambda/investor-reporting/reporting-publish/handler.py
infra/aws/lambda/investor-reporting/reporting-publish/publisher.py
infra/aws/lambda/investor-reporting/reporting-publish/tests/test_filled_report_publish.py
infra/aws/lambda/investor-reporting/reporting-publish/tests/test_filled_report_reader.py
infra/aws/terraform/investor-reporting/reporting-publish/locals.tf
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~243/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-302.hop2-filled-report-reader.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 164 (round 149, workstream FILLEDRD), cell `DB-b-302`.
<owned_cells>DB-b-302</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB170-1-AC1, DB170-1-AC2, DB170-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~243/IRPT_DASHBD.TO-DB-b-302.hop2-filled-report-reader.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB170-1-AC1,DB170-1-AC2,DB170-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the reader signature; the three code and one Terraform change in one line each; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: code and one Terraform expression in a branch; no plan, no apply, nothing deployed; the later deploy pair carries its own blast radius (a read grant on the filled prefix and a reader that runs only when the switch is on).
comp-iam: DECLARED-NOT-APPLICABLE -- reason: nothing is applied in this cell; the later pair's plan gate grades the one read and list prefix added to the publish role (no write change, the write arns stay).
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the issuer ran them on a reference tree (green) and on four single-fault reader mutants and one diff mutant (all red).
lane: the <paths> block IS the grant.
</preflight>
