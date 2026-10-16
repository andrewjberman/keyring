# TO IRPT_DASHBD.TO-DB-b-306 -- the HOP-2 READER re-cut (row IRPT_DASHBD-D2-S128): `read_filled_report_gold` joins a client to its household through the ACCOUNTS (the table's raw account ids minted with the handler's own `ids.opaque_account` equal the directory's `account_ids`), and indexes the partition ONCE per object version (round 149)

<to_id>IRPT_DASHBD.TO-DB-b-306</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~247</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>149</round>
<workstream>FILLEDRD2</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** FILLEDRD2, round 149 | **Ordered by:** the issuer's finding row `IRPT_DASHBD-D2-S128` (@`05be852c08`) on the drained `DB-b-302` (merge `aec0df87fc`): the relationship-id rule of that reader matches NONE of the 4,012 households of the real `filled_report_values` partition | **Decomp cell:** `DB-b-306` (decomposition section 168).

**Risk class WORLD** is the floor of the path (`infra/`): one handler block and tests in a branch; no Terraform command, no AWS call, no push. The switch stays OFF.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-247` (branch `wk-IRPT_DASHBD-247`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~247/`. Never push; never commit the workspace `portal` gitlink. Counts, dates, hashes and words only in the repo, a row, a commit message or your report; use synthetic ids in tests. **Before every commit, scan what you stage for a client figure and for long identifier runs; the commit gate's client-data list is absent on this box, so that scan is yours.** **Commit order: the artifact first, then the proof instance, then the status flip to complete as the LAST commit.** Tool calls that carry a backslash-r or backslash-n escape inside a shell heredoc can be altered in transit: write patch scripts to a file with the Write tool and run them.

**What was measured (S128).** Against the real partition (2026-10-15, 4,694,024 rows, 5 row groups, 4,012 household refs) and the real 49 Financial directory (4,776 clients): `sha256(relationship_id)` equals none of the household refs. The accounts join: the table's `member_id == "account.last4"` rows carry the household's RAW custodial account ids in `row_key` (10 characters); the directory's `ids.account_ids` are MINTED opaque ids (28 characters); the handler's own `_ids_module().opaque_account(firm, raw)` turns the first into the second (all 6,616 table accounts match directory account ids, 0 mint failures); through it 4,012 clients reach exactly ONE household, 764 reach none, none reaches two. Held in memory as plain Arrow strings the partition is 1,059 MB; read with `read_dictionary` for its string columns it is 269 MB and reads in 0.4 s (the publish function has 1,024 MB). One compose of a household takes under 0.1 s, so the partition is read and indexed ONCE per object version, never per client.

**The cell (`DB-b-306`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p174_filled_reader_accounts.py` (your three criteria; its fake S3 allows only `list_objects_v2`, `get_paginator` and `get_object`, and its listing of a key carries the ETag); `infra/aws/lambda/investor-reporting/reporting-publish/handler.py` (the first `FILLED-REPORT-A` block: the present `read_filled_report_gold`, `_filled_compose`, `_filled_leaf`; and `_ids_module`, `opaque_account` use in `_published_map`); your sibling's tests `reporting-publish/tests/test_filled_report_reader.py`.
2. **handler.py (ONLY inside the FIRST `FILLED-REPORT-A` block, in `read_filled_report_gold` and NEW private helpers; `filled_report_enabled`, `run_filled_report`, `filled_report_fire` MUST stay byte for byte; `_filled_compose` and `_filled_leaf` may stay as they are).**
   - **Helper `_filled_partition_index(s3, firm)` and a module-level cache `_FILLED_CACHE = {}`.** List the `date=` partitions of the gold table `filled_report_values` (the address from `opal_naming.address`, never typed; follow `IsTruncated` and `NextContinuationToken`; none: `NotYetAvailable`). Take the newest day. Read that object's ETag from `s3.list_objects_v2(Bucket, Prefix=<the data.parquet key>)` (its `Contents` entry). When `_FILLED_CACHE["entry"]` was built for the same (bucket, key, ETag), return it WITHOUT fetching the object. Otherwise fetch the object ONCE with `get_object`, read it with `pq.read_table(io.BytesIO(body), read_dictionary=[the string columns])` (firm, household_ref, as_of, member_id, row_key, series_name, point_date, value_text, absent_kind, absent_reason, contract_version, schema_version), and build the index: the household codes (dictionary encode `household_ref`), a stable argsort of the codes with the group start offsets (numpy: `np.argsort(codes, kind="stable")`, `np.bincount`, `np.cumsum`), and a dict from MINTED account id to the set of household codes built from the rows whose `member_id == "account.last4"` (their `row_key` is the raw id; mint it with `_ids_module().opaque_account(firm, raw)`). Store the entry in `_FILLED_CACHE["entry"]` and return it.
   - **`read_filled_report_gold(firm, client_id, s3=None, directory=None)` (same signature).** `s3` defaults to a boto3 client created inside; `directory` defaults to `read_directory(s3, directory_bucket(firm))`. Collect the `ids.account_ids` of the directory entries whose `ids.client_id` equals `client_id`. The client absent from the directory, or with no account ids: `NotYetAvailable`, BEFORE any gold read. Then the index; the households any of the client's account ids belong to: none is `NotYetAvailable`; MORE THAN ONE is `publisher.PublishRefused` (households are never merged); exactly one: take that household's rows by the index (`table.take(order[start:end]).to_pylist()`) and return `_filled_compose(rows, household_ref)`. The reader no longer uses `relationship_id` or `sha256` at all (the words must not appear in the function). It calls only `list_objects_v2` and `get_object`: no write of any kind.
3. **publisher.py, locals.tf and every other file stay byte for byte** (the diff check compares them with the base, commit `787619fad2`).
4. **Tests.** In `reporting-publish/tests/test_filled_report_reader.py`: rewrite the reader tests that used the relationship rule to the account join (synthetic raw ids, minted with the handler's own `ids.opaque_account`) and ADD at least SIX NEW tests whose names contain `accounts`: a client with two accounts in one household gets the household's document; a client whose accounts match no household is `NotYetAvailable`; a client whose accounts span two households is `PublishRefused`; directory ids equal to the RAW ids never match; the partition is fetched once across several clients; a partition rewritten under the same key (a new ETag) is re-read. All other tests keep passing.
5. **Run the checks yourself before the record:** `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p174_filled_reader_accounts.py" . DB174-1-AC1`, then AC2 (it builds a 200 thousand row partition and reads 400 clients, about a minute), then AC3.
6. **Record** `RD_FILLED_READER_ACCOUNTS_FACTS_R149.json` in your folder with EXACTLY these fields: `join` (one sentence: client to account ids to minted table accounts to household); `cache` (one sentence: the key and what it saves); `memory` (one sentence: how the table is read); `tests_added` (the names of the new tests); `words` (one paragraph, 80 to 1800 characters: what changed and why, and what is NOT proven: nothing was deployed, the switch is off, the join was measured by the issuer on the real partition and directory but the reader has not run against real S3, and the Lambda's 1,024 MB and 300 s limits for a whole pass are not exercised).

<criterion id="DB174-1-AC1" cell_refs="DB-b-306"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p174_filled_reader_accounts.py" . DB174-1-AC1</invocation><expect>DB174-1-AC1 PASS</expect></criterion>
`DB174-1-AC1` -- `handler.py` differs from the base only inside the reader and its private helpers in the first `FILLED-REPORT-A` block (the switch, `filled_report_enabled`, `run_filled_report`, `filled_report_fire` and the event branch byte for byte); `publisher.py` and `locals.tf` are byte-identical to the base. Base: FAIL.
<criterion id="DB174-1-AC2" cell_refs="DB-b-306"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p174_filled_reader_accounts.py" . DB174-1-AC2</invocation><expect>DB174-1-AC2 PASS</expect></criterion>
`DB174-1-AC2` -- behaviour over a fake S3: one household composed for a client whose accounts (minted) are in it; no match, no account ids, a client not in the directory, directory ids equal to the RAW table ids, and no partition each raise `NotYetAvailable`; accounts spanning two households raise `PublishRefused`; across a pass the partition's `data.parquet` is fetched ONCE and an older partition never; a partition rewritten under the same key is re-read; 400 clients over 200 thousand rows finish inside the limit; the pass writes one object and records the refused and unavailable clients. Base: FAIL.
<criterion id="DB174-1-AC3" cell_refs="DB-b-306"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p174_filled_reader_accounts.py" . DB174-1-AC3</invocation><expect>DB174-1-AC3 PASS</expect></criterion>
`DB174-1-AC3` -- at least six NEW tests carry `accounts` in their name; the reader no longer mentions `relationship` or `sha256`; the block reads the partition with `read_dictionary` and mints with the handler's own `ids.opaque_account`; both filled-report test files pass under pytest. Base: FAIL.

<expected_criteria>DB174-1-AC1,DB174-1-AC2,DB174-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Reads and writes.** Reads: repo files. No network, no AWS call, no Terraform command, no push. Writes: the one handler, the two test files and your private folder.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a checker clause is wrong rather than your edit, file a BLOCKING row naming the clause and stop on it.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W247-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`) and BOTH `project` ("IRPT_DASHBD") and `fabric` ("dell2") keys, class OBSERVATION or BLOCKING; append as BYTES. Commit with `.tools/safe-commit.sh`; READ the whole gate output: a refused commit leaves your edit uncommitted and blocks every other seat's merge. ASCII only in anything you write.

<paths>
infra/aws/lambda/investor-reporting/reporting-publish/handler.py
infra/aws/lambda/investor-reporting/reporting-publish/tests/test_filled_report_reader.py
infra/aws/lambda/investor-reporting/reporting-publish/tests/test_filled_report_publish.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~247/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-306.hop2-reader-joins-through-the-accounts.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 168 (round 149, workstream FILLEDRD2), cell `DB-b-306`.
<owned_cells>DB-b-306</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB174-1-AC1, DB174-1-AC2, DB174-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~247/IRPT_DASHBD.TO-DB-b-306.hop2-reader-joins-through-the-accounts.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB174-1-AC1,DB174-1-AC2,DB174-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the join and the cache in one line each; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: one handler block and tests in a branch; no plan, no apply, nothing deployed; the switch is off.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: nothing is applied in this cell; no grant changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: the only cache is an in-process dictionary keyed by an object's ETag; no CDN or edge cache is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the issuer ran them on a reference tree (green) and on four single-fault reader mutants and one diff mutant (all red).
lane: the <paths> block IS the grant.
</preflight>
