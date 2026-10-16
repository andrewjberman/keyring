# TO IRPT_DASHBD.TO-DB-b-310 -- the HOP-2 READER MINTS the account ids it composes (worker row IRPT_DASHBD-D2-W247-S1): the filled document carries the handler's own `ids.opaque_account` ids, never the table's raw custodial ids (round 149)

<to_id>IRPT_DASHBD.TO-DB-b-310</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~248</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>149</round>
<workstream>FILLEDRD3</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** FILLEDRD3, round 149 | **Ordered by:** the worker row `IRPT_DASHBD-D2-W247-S1` (the reader of `DB-b-306`, merged @`0a1224e703`, composes each account entry's `account_id` from the table's `row_key`, which is the RAW custodial id) | **Decomp cell:** `DB-b-310` (decomposition section 171).

**Risk class WORLD** is the floor of the path (`infra/`): one handler block and tests in a branch; no Terraform command, no AWS call, no push. The switch stays OFF.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-248` (branch `wk-IRPT_DASHBD-248`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~248/`. Never push; never commit the workspace `portal` gitlink. Counts, dates, hashes and words only in the repo, a row, a commit message or your report; use synthetic ids in tests. **Before every commit, scan what you stage for a client figure and for long identifier runs; the commit gate's client-data list is absent on this box, so that scan is yours.** **Commit order: the artifact first, then the proof instance, then the status flip to complete as the LAST commit.** Tool calls that carry a backslash-r or backslash-n escape inside a shell heredoc can be altered in transit: write patch scripts to a file with the Write tool and run them.

**What is wrong.** The gold table `filled_report_values` keys its account rows by the RAW custodial account id (`row_key`). The reader (`read_filled_report_gold`) joins a client to its household through the directory's MINTED ids, then composes the document from the table's rows, so three places in the composed document carry the raw id: `household.accounts[].account_id`, the keys of every account-grain `by_row` member (for example the per-account ending value) and the names of chart lines that are an account (for example one line per account). The summary builder and the directory carry only the minted opaque id (`ids.opaque_account(firm, raw)`), and this document is client-facing, so it must carry the minted id too. The asset-class keys of an allocation (`equity`, `bonds`, ...) and a line such as `Total` are not accounts and stay as they are.

**The cell (`DB-b-310`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p178_filled_reader_mints_ids.py` (your three criteria); `infra/aws/lambda/investor-reporting/reporting-publish/handler.py` (the first `FILLED-REPORT-A` block: `_filled_compose`, `_filled_partition_index`, `read_filled_report_gold`; and `_ids_module`); `reporting-publish/tests/test_filled_report_reader.py`.
2. **handler.py (ONLY inside the FIRST `FILLED-REPORT-A` block; only `read_filled_report_gold`, `_filled_compose` and NEW private helpers may differ from the base; every other function stays byte for byte).** Add one helper `_filled_mint(doc, firm)`: it builds a map `{raw account id: ids.opaque_account(firm, raw)}` from the document's own `household.accounts[].account_id` values (with `ids = _ids_module()`), then rewrites IN PLACE (a) each `household.accounts[].account_id` to its minted id; (b) for every member whose value is a dict holding `by_row`, each key that is in the map to its minted id (a key not in the map stays); (c) for every member whose value is a list of chart lines, each line's `name` that is in the map to its minted id (a name not in the map stays). It returns the document. The ORDER of the account entries and of every list stays as `_filled_compose` made it (sorted by the raw id BEFORE minting; do not re-sort). `read_filled_report_gold` returns `_filled_mint(_filled_compose(rows, household_ref), firm)`. `_filled_compose` itself may stay as it is, so its direct tests keep their raw ids.
3. **publisher.py, locals.tf and every other file stay byte for byte** (the diff check compares them with the base, commit `923e562c61`).
4. **Tests.** In `reporting-publish/tests/test_filled_report_reader.py`: the seven tests that compare the reader's result with the raw contract document now expect the MINTED form: write a small test helper that returns the contract document with each raw account id replaced by `mint(raw)` (the file already has `mint`), and use it in `test_present_household_is_composed_from_the_newest_partition_only`, `test_present_document_validates_and_equals_the_producer_inverse`, `test_present_newest_partition_is_found_across_the_listing_pages`, `test_present_pass_publishes_one_document_at_the_builder_address_and_absent_client_is_not_available`, `test_accounts_two_accounts_in_one_household_get_that_household_document`, `test_accounts_partition_is_fetched_once_across_several_clients` and `test_accounts_partition_rewritten_under_the_same_key_is_re_read`. ADD at least FOUR NEW tests whose names contain `mint`: the composed `account_id` values are the minted ids in the compose order; no raw account id remains anywhere in the serialized document (`json.dumps`); the allocation's class keys and a non-account chart line keep their names; the minted document still passes `publisher.validate_filled_report`. All other tests keep passing.
5. **Run the checks yourself before the record:** `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p178_filled_reader_mints_ids.py" . DB178-1-AC1`, then AC2 (it builds a 200 thousand row partition and reads 400 clients, about a minute), then AC3.
6. **Record** `RD_FILLED_READER_MINT_FACTS_R149.json` in your folder with EXACTLY these fields: `where` (one sentence: the three places the document carried the raw id); `rule` (one sentence: which keys and names are minted and which are left); `tests_added` (the names of the new tests); `words` (one paragraph, 80 to 1800 characters: what changed and why, and what is NOT proven: nothing was deployed, the switch is off, and whether every real by_row member of the real table is keyed by an account or a class was not read here).

<criterion id="DB178-1-AC1" cell_refs="DB-b-310"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p178_filled_reader_mints_ids.py" . DB178-1-AC1</invocation><expect>DB178-1-AC1 PASS</expect></criterion>
`DB178-1-AC1` -- `handler.py` differs from the base only in `read_filled_report_gold`, `_filled_compose` and new functions of the first `FILLED-REPORT-A` block; `publisher.py` and `locals.tf` are byte-identical to the base. Base: FAIL.
<criterion id="DB178-1-AC2" cell_refs="DB-b-310"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p178_filled_reader_mints_ids.py" . DB178-1-AC2</invocation><expect>DB178-1-AC2 PASS</expect></criterion>
`DB178-1-AC2` -- behaviour over a fake S3: the composed document equals the contract document with its account ids minted (`account_id`, the account-grain `by_row` keys, the account-named chart lines); no raw id remains in the serialized document; the allocation's class keys and a `Total` line are untouched; the minted document validates; the partition is fetched once; no match and an unknown client raise `NotYetAvailable`; accounts spanning two households raise `PublishRefused`; 400 clients over 200 thousand rows finish inside the limit; the pass writes one object. Base: FAIL.
<criterion id="DB178-1-AC3" cell_refs="DB-b-310"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p178_filled_reader_mints_ids.py" . DB178-1-AC3</invocation><expect>DB178-1-AC3 PASS</expect></criterion>
`DB178-1-AC3` -- at least four NEW tests carry `mint` in their name; the block mints with the handler's own `ids.opaque_account`; both filled-report test files pass under pytest. Base: FAIL.

<expected_criteria>DB178-1-AC1,DB178-1-AC2,DB178-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Reads and writes.** Reads: repo files. No network, no AWS call, no Terraform command, no push. Writes: the one handler, the two test files and your private folder.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a checker clause is wrong rather than your edit, file a BLOCKING row naming the clause and stop on it.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W248-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`) and BOTH `project` ("IRPT_DASHBD") and `fabric` ("dell2") keys, class OBSERVATION or BLOCKING; append as BYTES. Commit with `.tools/safe-commit.sh`; READ the whole gate output: a refused commit leaves your edit uncommitted and blocks every other seat's merge. ASCII only in anything you write.

<paths>
infra/aws/lambda/investor-reporting/reporting-publish/handler.py
infra/aws/lambda/investor-reporting/reporting-publish/tests/test_filled_report_reader.py
infra/aws/lambda/investor-reporting/reporting-publish/tests/test_filled_report_publish.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~248/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-310.hop2-reader-mints-account-ids.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 171 (round 149, workstream FILLEDRD3), cell `DB-b-310`.
<owned_cells>DB-b-310</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB178-1-AC1, DB178-1-AC2, DB178-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~248/IRPT_DASHBD.TO-DB-b-310.hop2-reader-mints-account-ids.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB178-1-AC1,DB178-1-AC2,DB178-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the three places and the rule in one line each; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: one handler block and tests in a branch; no plan, no apply, nothing deployed; the switch is off.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: nothing is applied in this cell; no grant changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache is added or changed; the reader's ETag cache keeps the RAW table, and the minting runs on the composed copy.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the issuer ran them on a reference tree (green) and on five single-fault handler mutants and one diff mutant (all red).
lane: the <paths> block IS the grant.
</preflight>
