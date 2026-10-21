# NFRA_OPLGTW task order -- `OG-cs-3` -- the folder engine helpers: the five sensitive column classes dropped by name, the request mapped to the engine's closed-grammar plan, the source-size caps, and a footer-only parquet describe (cli-shim workstream, wave 2; PRD v3.19 FWD-23)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP_CLISHIM.round48.md</decomp_doc>
<owned_cells>OG-cs-3</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-cs-3</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~183</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and tests; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the module is pure (no AWS call, no network).
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is PRD v3.19 FWD-23 (ADMITTED) and the CRO's brief (Part V: no caller string becomes SQL text outside the engine's closed grammar; Part III: nothing hidden except the five sensitive classes dropped by column name), applied as code with no deploy; the release that carries it is a separate never-widen order.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-cs-3` (decomposition `NFRA_OPLGTW_DECOMP_CLISHIM.round48.md`, workstream CLISHIM-B, wave 2)

WHY. The cli-shim tools (the cell `OG-cs-2`, built in parallel by another worker against THIS module's interface below) let a granted person list, describe and query parquet tables under the folders they may read. Four things they need are pure and testable on their own, and this cell writes them in ONE new module, `app/folder_engine.py` (under `infra/aws/ec2/opal-gateway/`). It imports `app.integrations.schwab.engine` (the bounded DuckDB engine: `QueryPlan`, `Filter`, `Aggregate`, `OrderBy`, `validate_plan`, `EngineError`, `ERROR_INVALID_REQUEST`, `ERROR_LIMIT_EXCEEDED`, `EngineLimits`) and `pyarrow`. It calls no AWS API, opens no network connection, and starts no child process. READ `app/integrations/schwab/engine.py` (the plan dataclasses at lines 227-295, `validate_plan` at 327, the `FILTER_OPERATORS` and `AGGREGATE_FUNCTIONS` constants near line 125, `EngineLimits` at 177) before you write a line.

THE INTERFACE (exact names; the other worker codes against them):

1. `SENSITIVE_CLASSES = ("tax_identifier", "mailing_address", "email", "phone", "date_of_birth")`.
2. `sensitive_class(name: str) -> Optional[str]`: the class a COLUMN NAME belongs to, or `None`. Match on whole TOKENS of the name, case-insensitively, after splitting on `_` and `-` and on CamelCase boundaries (`TaxID` is `tax`, `id`; `MailingAddress` is `mailing`, `address`; never on a bare substring, so `mail_flag` is not email and `taxable_amount` is not a tax identifier): `tax_identifier` = a token in {`tin`, `ssn`, `ein`, `taxid`, `taxpayer`} or the adjacent token pairs (`tax`, `id`), (`tax`, `identifier`), (`social`, `security`); `mailing_address` = a token in {`address`, `addr`, `street`, `postal`, `zip`, `zipcode`, `mailing`, `city`}; `email` = the token `email` or the adjacent pair (`e`, `mail`); `phone` = a token in {`phone`, `telephone`, `tel`, `mobile`, `fax`}; `date_of_birth` = a token in {`dob`, `birth`, `birthday`, `birthdate`}. Check the classes in the order listed; the first that matches names the column. `tax_lot_id` (tokens `tax`, `lot`, `id`), `tax_amount`, `taxable_amount`, `mail_flag`, `account_id`, `trade_date` and `quantity` are NOT sensitive.
3. `drop_sensitive(names: Sequence[str]) -> tuple[list[str], list[str]]`: `(kept, dropped)`, each in the input order; a name is dropped exactly when `sensitive_class(name)` is not None.
4. `plan_from_request(request: dict, allowed_columns: Sequence[str]) -> QueryPlan`: maps the caller's JSON request to the engine's plan and runs `validate_plan` on it. Request keys (ALL optional): `columns` (list of names), `filters` (list of `{field, op, value}`), `group_by` (list), `aggregates` (list of `{function, alias, field}`), `order_by` (list of `{field, direction}`), `limit` (int). Any OTHER top-level key (for example `sql`) is refused. Mode is `aggregate` when `aggregates` or `group_by` is non-empty, else `rows`. `limit` omitted is 100; above 500 it is clamped to 500; below 1, a bool or a non-int is refused. `allowed_columns` is passed through to the plan (the dropped sensitive columns are never in it, so referencing one is refused by the engine's own `field_not_granted`). Every refusal is `engine.EngineError(engine.ERROR_INVALID_REQUEST, <fixed reason>)`: never echo a caller string in the reason, and never let another exception type escape (a request that is not a dict, a malformed filter entry, a wrong type anywhere).
5. `check_sources(sizes: Sequence[int]) -> Optional[dict]`: `sizes` are the compressed byte sizes of the objects a query would read. Returns `None` when there are at most 12 objects AND at most 67108864 bytes in all (use the values of `engine.EngineLimits()`, do not retype them); otherwise `{"code": "LIMIT_EXCEEDED", "reason": "source_objects" or "source_bytes", "suggestion": <a sentence that says to narrow the request to fewer partitions or one table and retry>}`.
6. `describe_parquet(read_range: Callable[[int, int], bytes], size: int) -> dict`: reads ONLY the parquet FOOTER through `read_range(offset, length)` (a callable the caller supplies; for an S3 object it is a ranged GET) and returns `{"columns": [{"name": <str>, "type": <str of the arrow type>}, ...] in file order, "num_rows": <int>, "row_groups": <int>}`. Column names are returned AS STORED, the sensitive ones included (dropping is the caller's job with `drop_sensitive`). It must not read the whole file: wrap `read_range` in a small file-like object (an `io.RawIOBase` with `readable`, `seekable`, `seek`, `tell`, `readinto`) and hand it to `pyarrow.parquet.read_metadata`; a 350 KB test file must cost under a quarter of its bytes. Any failure to parse (not parquet, truncated, a `read_range` that raises) is a `ValueError` and nothing else.

## 2. TESTS

NEW `tests/test_cs3_folder_engine.py`, at least EIGHT tests, offline, `os.environ.setdefault("MOCK_GRAPH", "1")` before any app import, pyarrow tables written to `tmp_path`: the drop table of the interface (every sensitive name of every class, snake_case and CamelCase, and every look-alike kept, order kept), `sensitive_class` per class and `None`, `plan_from_request` rows and aggregate and the limit rules, each refusal kind (a column outside `allowed_columns`, an unknown operator, `limit` 0, `limit` True, no columns in a rows request, an unknown top-level key, a non-dict request), `check_sources` at 12 and 13 objects and at 64 MiB and 64 MiB + 1, `describe_parquet` on a multi-row-group file (columns, `num_rows`, `row_groups`, bytes read under a quarter) and on junk bytes (`ValueError`).

## 3. BOUNDS

- Write only the two files above, `W/` and, if a row is needed, the channel. No other product file, no other test, no release, no deploy, no AWS call.
- Counts and hashes only: no e-mail address, account number or token in any file (test data uses `example.invalid` addresses and made-up values).
- Never: push, `git stash`, rebase, `checkout --` or `clean`.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 4. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/folder_engine.py
infra/aws/ec2/opal-gateway/tests/test_cs3_folder_engine.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~183/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-W183-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 5. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-cs-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/clishim/checks/cs3.AC1.sh; echo "exit=$?"</invocation><expect>(?s)exactly the 17 sensitive probe names are dropped and the 7 look-alikes kept .*: ok.*kept and dropped keep the input order: ok.*sensitive_class names the class or None: ok.*a rows request becomes a rows plan with its parts: ok.*an aggregate request becomes an aggregate plan: ok.*limit: omitted is 100, 9999 is clamped to 500: ok.*refusals raise EngineError INVALID_REQUEST .*: ok.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-cs-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/clishim/checks/cs3.AC2.sh; echo "exit=$?"</invocation><expect>(?s)inside the caps answers None .*: ok.*13 objects and 64 MiB \+ 1 byte answer LIMIT_EXCEEDED with a suggestion that says narrow: ok.*columns in file order with types, num_rows 60000, row_groups >= 1 .*: ok.*only the footer was read: \d+ bytes of \d+: ok.*control: a 5-row file answers num_rows 5 and the same columns: ok.*bytes that are not parquet raise ValueError: ok.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-cs-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/clishim/checks/cs_foot.sh org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-cs-3.cli-shim-the-folder-engine-helpers.md app/folder_engine.py,tests/test_cs3_folder_engine.py tests/test_cs3_folder_engine.py 8 tests/test_schwab_engine.py tests/test_schwab_query.py; echo "exit=$?"</invocation><expect>(?s)files that differ from HEAD under the gateway folder: .*: ok.*tests/test_cs3_folder_engine\.py: (?:[89]|[1-9]\d+) test functions.*: ok.*new file tests/test_cs3_folder_engine\.py: (?:[89]|[1-9]\d+) passed, 0 failed.*neighbours \(2\): [1-9]\d* passed, failed names \[\].*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1` (the pure half) and `AC2` (the byte-bounded half) are graded by issuer-written probes independent of your tests. `AC3`: the footprint is exactly the two files, and your tests plus the two engine neighbours pass.

## 6. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-cs-3.cli-shim-the-folder-engine-helpers.proof_of_spec.json`. Validate it after your last commit with `python3 -I .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-cs-3.cli-shim-the-folder-engine-helpers.md` (`python3`, not `python`: ruling msg 35901). Report once; the `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Workstream CLISHIM-B, wave 2, decomposition `NFRA_OPLGTW_DECOMP_CLISHIM.round48.md`. Source: PRD v3.19 FWD-23, the CRO's brief, the CTO's msgs 36299 and 36308.
- Widening, plainly: none by this order (pure functions nothing calls yet). The sensitive-class drop is the CRO's and Andrew's one exception to "nothing hidden" (tax identifiers, mailing addresses, email, phone, date of birth, by column name); the tools that apply it and the release that carries it are later orders with their own never-widen halves.
- DISCLOSED READINGS: (1) `city` is read as part of a mailing address; `state` and `country` are not dropped (a status or a country code is not an address alone); (2) the class names a COLUMN by tokens, so a table that stores such data under an unrelated column name is not caught: the census of real column names across Schwab, Orion and Cottonwood Black Diamond is the CTO's/CVO's to run against the three sources; (3) a request's `limit` above 500 is clamped, not refused.
- Pre-cut: `AC1` and `AC2` base FAIL as expected (`app.folder_engine` absent); `AC3` base FAIL as expected. Arm on a SCRATCH copy of the gateway app (the shared tree untouched): a scratch `folder_engine.py` reads `AC1` OK (all seven arms) and `AC2` OK (all six arms; the footer read cost 65,536 of 357,521 bytes).

<status>pending</status>
<status>complete</status>
<round>48</round>
<workstream>CLISHIM-B</workstream>
<slot>~183</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
