# NFRA_OPLGTW task order -- `OG-cs-2` -- the cli-shim tools as plain functions: list a folder, describe an object, query a table folder (cli-shim workstream, wave 3; PRD v3.19 FWD-23)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP_CLISHIM.round48.md</decomp_doc>
<owned_cells>OG-cs-2</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-cs-2</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~182</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and tests; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the functions take an S3 client the caller supplies and the tests pass a fake.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is PRD v3.19 FWD-23 (ADMITTED) and the CRO's brief (Part V: no caller string becomes SQL text outside the engine's closed grammar; Part III: nothing hidden except the five sensitive classes dropped by column name; never a bronze or raw prefix), applied as code with no deploy and no route mounted; the release that mounts it is a separate never-widen order.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-cs-2` (decomposition `NFRA_OPLGTW_DECOMP_CLISHIM.round48.md`, workstream CLISHIM-C, wave 3)

WHY. A granted person reads a bucket or a folder the way the AWS CLI would show it: list it, describe an object, query a table. This cell writes the three functions in ONE new module, `app/folder_tools.py` (under `infra/aws/ec2/opal-gateway/`). Nothing mounts them yet (the MCP registration and the release are later orders); they take every dependency as an argument so a test passes fakes. READ first: `app/folder_grant.py` (`folder_decision(is_master_admin, is_opal, rec, bucket, key) -> (allowed, reason)`, `SERVED_BUCKETS`), `app/folder_engine.py` (`SENSITIVE_CLASSES`, `sensitive_class`, `drop_sensitive`, `plan_from_request`, `check_sources`, `describe_parquet`), `app/integrations/schwab/engine.py` (`ExecutionEngine.run_query(principal, plan, sources)`, `SourceObject(path, compressed_bytes, role)`, `JobResult`, `QueryPlan`), `app/integrations/schwab/cursor.py` (`bind_key`, `CursorCodec.issue(binding, offset)`, `.open(token, binding)`, `CursorError`), `app/data_entitlement.py` (`PersonAccess`).

THE INTERFACE (exact names and arguments; the checks call them so):

1. `split_path(path: str) -> tuple[str, str]`: `"bucket/key/prefix"` to `(bucket, key)`; no `/` gives `(path, "")`. A non-str is treated as `""`.
2. `list_folder(principal, rec, is_master_admin, is_opal, s3, path, start_after="") -> dict`.
3. `describe_object(principal, rec, is_master_admin, is_opal, s3, path) -> dict`.
4. `async query_object(principal, rec, is_master_admin, is_opal, s3, engine, codec, path, request, cursor="") -> dict`.

Every function FIRST calls `folder_decision(is_master_admin, is_opal, rec, bucket, key)` on the path it was given. A refusal answers EXACTLY `{"error": <the decision's reason>, "code": "folder_refused", "guard_denied": True, "folder": "<bucket>/<key>"}` and makes ZERO S3 calls. No function raises: every failure is a dict with `error` and `code`.

`list_folder`: one `list_objects_v2(Bucket, Prefix=key, Delimiter="/", MaxKeys=<page>, StartAfter=start_after)` call (page 200; a `key` that is non-empty and has no trailing `/` gets one appended). Answer `{"folder": "<bucket>/<prefix>", "prefixes": [...], "objects": [{"key", "size", "last_modified"} ...], "truncated": bool, "next_start_after": str only when truncated}`; `last_modified` is an ISO-8601 string (`.isoformat()`). A prefix whose segments include `bronze` or `raw`, and an object key under one, is OMITTED from both lists (the AWS-CLI view without the two folders no grant reaches). `next_start_after` is the last key or prefix the page returned (the lexically greatest).

`describe_object`: `path` names ONE object. Size from `head_object(Bucket, Key)` (a missing object, a botocore `ClientError` with a 404/NoSuchKey code or a `KeyError`, answers code `not_found`). Footer through `folder_engine.describe_parquet(read_range, size)` where `read_range(offset, length)` is `get_object(Bucket, Key, Range="bytes=%d-%d")["Body"].read()`; a `ValueError` answers code `not_parquet`. Then `drop_sensitive` on the column names. Answer `{"path", "size", "columns": [{"name","type"} (kept, file order)], "dropped_columns": [names dropped], "num_rows", "row_groups"}`. The object is never downloaded.

`query_object`: `path` names a table FOLDER (a `key` without `.parquet` at its end) or ONE `.parquet` object. A folder is listed with `list_objects_v2` (no delimiter, paged with `StartAfter`, stopping as soon as 14 qualifying keys are seen), keeping keys that end `.parquet` and have no `bronze` or `raw` segment, sorted. No qualifying object answers code `not_found`. The listed sizes go to `folder_engine.check_sources`; a non-None answer is returned as `{"error": <its suggestion>, **that dict}` BEFORE any download. The columns come from the FIRST source's footer (`describe_parquet` as above), `drop_sensitive` gives `allowed_columns`, and `folder_engine.plan_from_request(request, allowed_columns)` builds the plan; an `engine.EngineError` answers `{"error": <reason>, "code": <its code>}` with ZERO downloads. A cursor, when given, is opened with `codec.open(cursor, binding)` (a `CursorError` answers code `INVALID_REQUEST`, error `the cursor is not valid for this request`) and the plan gets `dataclasses.replace(plan, offset=<opened offset>)`. `binding = bind_key("cursor", principal=principal, revision=<rec.revision if rec else 0>, master=bucket, dataset=key, dates=[key], projection=<sha256 hex of json.dumps(request, sort_keys=True)>, source_versions=["%s:%d" % (key, size) for each source])`. Only now are the sources downloaded, in `asyncio.to_thread`, with `s3.download_file(Bucket, Key, Filename)`, into a `tempfile.TemporaryDirectory` that is removed before the function returns; each becomes `engine.SourceObject(path=<local path>, compressed_bytes=<listed size>)`. `await engine.run_query(principal, plan, sources)`: a not-ok `JobResult` answers `{"error": <reason>, "code": <code>, "suggestion": <suggestion or "">}`. An ok result answers `{"path", "columns": value["columns"], "rows": value["rows"], "matched_rows", "returned_rows", "dropped_columns": [...], "next_cursor": codec.issue(binding, offset + returned_rows) ONLY when offset + returned_rows < matched_rows}`.

## 2. TESTS

NEW `tests/test_cs2_folder_tools.py`, at least TWELVE tests, offline, `os.environ.setdefault("MOCK_GRAPH", "1")` before any app import, a fake in-memory S3 (list, head, ranged get, download) holding pyarrow-written parquet bytes under `tmp_path`, a real `ExecutionEngine(temp_root=tmp_path/"engine-root", memory_total_bytes=lambda: 1 << 40)` for the query tests (async via `asyncio.run`): each refusal kind makes zero S3 calls (unserved bucket, bronze, raw, no grant, non-Opal); the sibling master refused for a person granted one master; deny wins; the list view hides `bronze`/`raw`, pages with `next_start_after`; `describe_object` columns, dropped, footer-only bytes under a quarter, `not_parquet`, `not_found`; `query_object` rows, aggregate, a sensitive column refused with zero downloads, `sql` key refused, 13 objects `LIMIT_EXCEEDED` with zero downloads, paging with a cursor and no overlap, a cursor reused for a different request refused, a tampered cursor refused, and the temp directory gone afterwards.

## 3. BOUNDS

- Write only the two files above and, if a row is needed, the channel. No other product file, no other test, no route, no MCP registration, no release, no deploy, no AWS call.
- Counts and hashes only: no e-mail address, account number or token in any file (test data uses `example.invalid` addresses and made-up values).
- Never: push, `git stash`, rebase, `checkout --` or `clean`.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 4. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/folder_tools.py
infra/aws/ec2/opal-gateway/tests/test_cs2_folder_tools.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~182/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-W182-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 5. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-cs-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/clishim/checks/cs2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)refusals answer folder_refused naming the folder, guard_denied true .*: ok.*refusals made ZERO S3 calls \(0\): ok.*bronze/ NOT shown .*: ok.*two table prefixes .*: ok.*key, size and last_modified .*: ok.*truncated and next_start_after are carried .*: ok.*refused for the sibling master with no S3 call: ok.*deny wins.*: ok.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-cs-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/clishim/checks/cs2.AC2.sh; echo "exit=$?"</invocation><expect>(?s)refusals answer folder_refused, guard_denied true, an error naming the folder: ok.*refusals made ZERO S3 calls \(0\): ok.*columns in file order, sensitive classes dropped and named .*: ok.*only the footer was read through ranged GETs: \d+ bytes of \d+: ok.*junk answers not_parquet and an absent object answers not_found, neither raises .*: ok.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-cs-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/clishim/checks/cs2.AC3.sh; echo "exit=$?"</invocation><expect>(?s)a refused path answers folder_refused with ZERO S3 calls \(0\): ok.*INVALID_REQUEST with ZERO downloads .*: ok.*LIMIT_EXCEEDED with ZERO downloads .*: ok.*a rows request answers .*: ok.*an aggregate request answers .*: ok.*the default page is 100 of 300 .*: ok.*the next page continues with no overlap .*: ok.*INVALID_REQUEST .*: ok.*refused for the sibling master .*: ok.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- Three criteria are the cap, and the footprint (the two files only) and your tests (at least twelve, all passing) are the issuer's drain checks, run on the merged tree: `AC1` is list and admission, `AC2` is describe, `AC3` is query against the REAL engine.

## 6. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-cs-2.cli-shim-the-folder-tools-list-describe-query.proof_of_spec.json`. Validate it after your last commit with `python3 -I .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-cs-2.cli-shim-the-folder-tools-list-describe-query.md` (`python3`, not `python`: ruling msg 35901). Report once; the `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Workstream CLISHIM-C, wave 3, decomposition `NFRA_OPLGTW_DECOMP_CLISHIM.round48.md`. Source: PRD v3.19 FWD-23, the CRO's brief, the CTO's msgs 36299 and 36308. Staged: spawn after OG-cs-1 (drained) and OG-cs-3 (pending) are on the base.
- Widening, plainly: none by this order (functions nothing mounts). The tools they become, and the release that carries them, are later orders with their own never-widen halves.
- DISCLOSED READINGS: (1) a folder query reads at most 13 objects and 64 MiB compressed in all (the engine's own caps); a larger table is narrowed by path; (2) the columns the plan may use come from the FIRST object's footer, so a folder whose objects differ in schema is a disclosed limit; (3) the cursor's `master` and `dataset` dimensions carry the bucket and the folder key because the binding needs seven non-empty dimensions; (4) the five dropped classes and the bronze/raw omission are the only things hidden.
- Pre-cut: `AC1`, `AC2` and `AC3` base FAIL as expected (`app.folder_tools` absent). Arming: the three probes are graded green against the worker's module at the drain; a probe that fails for a reason that is the probe's own is the issuer's defect, amended with the gate limb named.

- AMENDED 2026-10-21 ~18:0xZ (2.0.0_SA_COO~O, worker ~182's BLOCKING row Z-W182-S6): the AC1 expect required a space after `deny wins` where the probe's label reads `deny wins: a denied sub-folder ...`; the defect was mine, in the expect. It now reads `deny wins.*: ok`; the probe is unchanged. Gate limb: none graded (an existing tree order that declares no placeholders).

<status>pending</status>
<status>complete</status>
<round>48</round>
<workstream>CLISHIM-C</workstream>
<slot>~182</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
