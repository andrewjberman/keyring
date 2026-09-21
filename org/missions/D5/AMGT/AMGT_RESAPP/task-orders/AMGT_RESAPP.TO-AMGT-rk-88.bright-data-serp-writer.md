# AMGT_RESAPP task order -- `AMGT-rk-88` -- the Bright Data SERP channel gets ONE harvest writer: bronze = the response bytes exactly as received, captured by a teeing TRANSPORT (form (c), `bright-data/harvest/bronze/serp/date=.../<query_sha256>-p<page>.json`), silver `serp_result` keyed `(query_sha256, rank)`, and a bucket fetch-key check that reuses a stored answer instead of paying again; CODE ONLY -- built and tested offline, off by default, wired into nothing

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-88</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~88</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order adds one library module and one test file; it arms no cron,
  alarm, monitor or cadence, reads no schedule and writes none, and runs no producer.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant is read or changed; every test runs offline against a
  stub S3 and a stub transport with AWS credentials pointed at a non-existent profile (AC4), and nothing is written to
  AWS by this order.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~88`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that
`org/`, `.tools/` and the paths in section 3 exist (the two new files excepted); if any is absent, STOP with a
BLOCKING row. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~88;`. **NEVER RUN AN INSTALL.**
Never read, show, diff or check out branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50` -- it holds an exposed
credential. **No Bright Data call, no secret:** your tests use a stub transport and never import the estate SERP
script (whose `serp_brightdata_records` reads the API key at call time).

## 1. THE CELL, inlined in full -- `AMGT-rk-88` (round 22, cell H5)

**The contracts, verbatim (PRD v0.17 `prd/AMGT_RESAPP_PRD.md` @1f7459456a, ADMITTED):** `:866-871` *"C-BRONZE-AS-
RECEIVED. Bronze is the response bytes exactly as received -- no parsing, trimming or re-serialising -- one object per
fetch, never overwritten, with the channel's FETCH key in the partition, in one of three forms ... (c) a request:
`{vendor}/harvest/bronze/{request}/date=YYYY-MM-DD/{request hash or file}.{ext}`."* `:873-875` *"C-SILVER-PARQUET.
Silver is parquet with every vendor field kept and typed, partitioned `date=` by fetch date, one part file per run.
Every row carries `bronze_key`, `fetched_at` and `record_hash`."* `:885-890` *"C-DEDUPE-BY-KEY ... Before any vendor
call, the writer checks the bucket for the fetch key. Exactly one writer holds a channel's fetch keys at a time ...
The bucket is the authority for what has been fetched, never a file on one desktop."*

**The design source (plan `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/PLAN_AMGT_HARVEST_CHANNEL_FORMATS_20260921.md`
s.5.8 @1a9f1c4469):** *"Proposed: bronze `s3://opal-data-harvest/bright-data/harvest/bronze/serp/date=2026-09-21/
<query_sha256>.json`; silver `.../bright-data/harvest/silver/serp_result/date=.../part-*.parquet` (row per result).
Record key / dedupe. Fetch key `query_sha256` = sha256 of (normalised query, engine, locale): a stored answer is
reused inside its window instead of paying again. Silver key `(query_sha256, rank)`."* The decomposition proposal
(`.scratch/r21_drafts/HARVEST_CHAIN_DECOMP_PROPOSAL.md:152`, cell H5): *"`management/ceo_search.py` -> bronze serp +
silver `serp_result`; stored-answer reuse inside window | none (code) | no | H0 store, rk-79 drained"*. rk-79 DRAINED
@a13b0fc140.

**THE MEASURED STATE, at HEAD `3863a8200d` (SITEZ). RE-READ every line at your branch HEAD before editing:**
- **The SERP primitive** (`data/find/dualbiz/scripts/serp.py`, 561 lines, NOT in your paths and NOT imported by your
  code or tests): `serp_brightdata_records(query, max_pages=1, gl="us", hl="en", retries=2, transport=None) -> dict`
  `:399`. **Its `transport` is injectable**: `(gurl, zone, key) -> (http_status, headers, body_bytes)` (`:377-396`,
  `:412`, `:442`), so the RAW BODY BYTES are reachable -- true as-received bronze, unlike a client that hands back a
  parsed dict. It parses `body` (`:461-466`), scrubs contact keys (`_scrub_body` `:312-340`, `general.mobile` exempt),
  and returns `{status, failure, attempts[], query, detected_query, query_rewritten, original_empty, gl, results_cnt,
  records[]}` (`:500-502`); each record is `{rank, link, link_form, host, title, snippet, display_link, source,
  answers_detected_query}` (`:485-489`). A captcha or 5xx attempt retries up to `retries` times (`:452-457`).
- **SERP call sites, census by subtraction** (`serp_brightdata_records\(|serp_brightdata\(|_bd_transport\(|
  _default_serp_records\(` over the 6664 tracked `*.py` files): **21 hit lines; minus 8 in the FIND pipeline
  (`data/find/**`) and 7 in test files = 6 AMGT lines**: `ceo_search.py:333` (a `def`) and `:334`; `enrich.py:515`
  (inside the legacy `enrich.ceo_public_profile` `:489`, which NO production code calls -- an AST call census finds its
  only callers in `tests/test_management.py:537,547,554`), `:535` (a string, not a call), `:657` (`build_document`) and
  `:999` (`research_stored_ceo`, rk-79's `--research-stored-ceo` mode). **Every live path ends in
  `ceo_search.ceo_profile` (`:544`: `serp_fn = serp or _default_serp_records`), which folds the result into the
  management document's `ceo_profile` (`search`, `cost`, `items`)** -- written by the management document writer, not
  by a SERP-channel writer. **0 SERP-channel objects exist**: `list_objects_v2` over `s3://opal-data-harvest/
  bright-data/`, paginated, read-only at the cut = **0 objects**. This cell adds the channel's ONE writer.
- **The builder, LIVE at HEAD** (`validate()` 0 refusals; the duplicate `harvest` scope row deleted @10bace8916):
  `address("bright-data","harvest","bronze","serp","date=2026-09-21","<64 hex>.json")` =
  `s3://opal-data-harvest/bright-data/harvest/bronze/serp/date=2026-09-21/<64 hex>.json`; silver `serp_result` =
  `s3://opal-data-harvest/bright-data/harvest/silver/serp_result/date=2026-09-21/part-20260921T120000Z.parquet`.
- **H0-store** (`AMGT-rk-81`, `lib/research/harvest/store.py`; interface `.scratch/r21_drafts/H0_STORE_INTERFACE.md`,
  fixed at issuance): `bronze_put(source, request, partition, object_name, body, content_type, client)` (write-once,
  idempotent on equal bytes, `BronzeImmutableError` on different bytes), `fetch_key_exists(source, request,
  partition, object_prefix, client)`, `silver_append(...)`, `form_c_object(...)`, `date_partition(...)`, `stamp(...)`.
  `bronze_put` also takes an optional `metadata` dict (keys `^[a-z0-9][a-z0-9-]*$`, printable-ASCII values, the two
  reserved keys refused; interface `:70-80`, the amendment rk-83 uses for `received-form`). **Every SERP bronze put
  passes `metadata={"received-form": "bd-raw-body"}`** -- the transport's body bytes, unparsed. Never re-implement the
  put.
- **Test baselines at the cut:** `lib/research/management/tests` **95 passed** (13 subtests), 0 failed.
  `lib/research/harvest/tests` arrives with rk-81 (re-measure at spawn).

**RULED, what you build (a NEW module; no existing file changes):**
1. **`lib/research/harvest/bright_data_serp.py`**, module constants: `SOURCE = "bright-data"`, `BRONZE_REQUEST =
   "serp"`, `SILVER_TABLE = "serp_result"`, `ENGINE = "google"`, `RECORD_KEY = ("query_sha256", "rank")`.
2. **`query_sha256(query, engine=ENGINE, gl="us", hl="en") -> str`** -- sha256 hex over `json.dumps({"q": " ".join(
   query.split()), "engine": engine, "gl": gl, "hl": hl}, sort_keys=True, separators=(",", ":"))`. Pure.
3. **`teeing_transport(inner, sink) -> callable`** -- returns `(gurl, zone, key) -> inner(gurl, zone, key)`, UNCHANGED,
   after appending `{"gurl": gurl, "http_status": status, "body": body_bytes}` to `sink`. It NEVER records `key` (a
   secret) or the request headers.
4. **`stored_answer(qsha, fetch_date, client=None) -> list[str]`** -- `store.fetch_key_exists(SOURCE, BRONZE_REQUEST,
   store.date_partition(fetch_date), object_prefix=qsha, client=client)`. The window is the fetch date's partition;
   the move cell may widen it.
5. **`harvest_serp(records_fn, query, *, inner, gl="us", hl="en", max_pages=1, now=None, client=None) -> dict`** --
   the ONE writer path, for the move cell to wire in later. `inner` is the REAL transport and is a REQUIRED keyword
   argument (the primitive's own default transport is not reachable from outside it). (a) `qsha = query_sha256(query,
   gl=gl, hl=hl)`; (b) if `stored_answer(qsha, now)` is non-empty, return `{"status": "REUSED", "bronze_keys": [...],
   "vendor_called": False}` WITHOUT calling `records_fn`; (c) else call `records_fn(query, max_pages=max_pages, gl=gl,
   hl=hl, transport=teeing_transport(inner, sink))`; (d) for each page, bronze-put the LAST
   captured attempt's body whose `http_status` is 2xx as `store.form_c_object("%s-p%d" % (qsha, page), "json")` under
   `date=` of `now` -- bytes EXACTLY as received; a FAILED result writes NO bronze and NO silver and returns
   `{"status": "FAILED", ...}`; (e) silver: one row per `records[]` item (every record field kept, `query_sha256`,
   `query`, `gl`, `hl`, `detected_query`, `page_bronze_key` as `bronze_key`, `fetched_at`), text fields passed
   through `ceo_search.contact_scrub_text` (the estate's rule -- do not duplicate it), appended with
   `store.silver_append(SOURCE, SILVER_TABLE, rows, RECORD_KEY, store.stamp(now), client)`. Return the
   `records_fn` result plus the bronze and silver receipts.
6. **Not wired.** No existing file imports `lib.research.harvest.bright_data_serp`; `enrich.py` and `ceo_search.py`
   stay BYTE-EQUAL to the pin. **rk-79's `--research-stored-ceo` path is NOT changed** (it keeps calling the
   primitive directly and writing only the management object); the move cell wires `harvest_serp` in under its own
   pair.
7. **Tests, a NEW file `lib/research/harvest/tests/test_bright_data_serp.py`** (offline: a stub S3 of the store's own
   test idiom, and a FAKE `records_fn` that calls the transport it is given with a canned body and returns a dict of
   the primitive's shape). Arms, names must match AC1:
   - `test_query_sha256_is_normalised_and_stable` -- whitespace variants hash equal; a different `gl` hashes different.
   - `test_teeing_transport_is_transparent_and_captures_bytes` -- returns the inner tuple unchanged; the sink holds
     the exact bytes; the sink never holds the `key` argument.
   - `test_bronze_is_the_exact_response_bytes` -- the stub's stored object equals the canned body byte-for-byte, at
     `bright-data/harvest/bronze/serp/date=<now>/<qsha>-p0.json`, and its user metadata carries
     `received-form: bd-raw-body`.
   - `test_silver_rows_are_keyed_by_query_and_rank_and_scrubbed` -- one row per record, a contact string in a
     snippet is redacted by `contact_scrub_text`, every row carries `bronze_key`, `fetched_at`, `record_hash`.
   - `test_stored_answer_skips_the_vendor_call` -- with the fetch key already in the stub bucket, `records_fn` is
     never called and the result is `REUSED`.
   - `test_failed_result_writes_nothing` -- a FAILED fake result leaves the stub bucket empty.
   - `test_module_never_writes_outside_the_store` -- an AST read of `bright_data_serp.py` finds no `put_object`,
     `upload_file` or `boto3` import, and no import of the estate `serp` script.
   - `test_module_imports_no_network` -- the same AST read finds no `urllib`, `requests` or `http.client` import.
   - `test_patched_store_is_the_one_production_reaches` -- the W85-S1 identity arm (CTO round-21 analysis `:29-33`): the test imports
     `lib.research.harvest.store` and `lib.research.harvest.bright_data_serp` by their QUALIFIED names, asserts
     `bright_data_serp.store is store`, then monkeypatches `store.bronze_put` with a recording fake and asserts
     that the module's bronze write reached that fake. Every other arm that patches across modules also uses the
     qualified names.

**What this cell does NOT change:** `enrich.py`, `ceo_search.py`, `data/find/dualbiz/scripts/serp.py`, `store.py`
(rk-81's; a WALL), any management object, any S3 object. **No served change.** It retires no phrase any test pins
(standing rule, CTO msg 24100): it edits no existing file.

## 2. WHERE THIS CAME FROM

**Rulings of record for round 22** (`1.0.0_SA_CTO~Z`, `ledger/ROUND_ANALYSIS.round21.md` @`739eb5f288`, msg 24119,
quoted verbatim):
- `:29-33` (row W85-S1): *"Disarmed for this project by a cutting rule, binding from round 22: every AMGT test that
  patches or asserts on code outside its own module imports the QUALIFIED `lib.<package>.<module>` name, never a
  relative or bare one. Each order's criteria include one arm proving the patched object is the one the production
  caller reaches (an `is` identity check against the qualified import)."* -- this order's arm `test_patched_store_is_the_one_production_reaches`.
- `:34-35`: *"The COO's cutting note from W84-S1 is adopted alongside: a criterion with a backslash escape inside
  `python -c` is written as a file its invocation runs."* -- this order's criteria carry NO backslash escape (AC5 reads
  lines with `splitlines()`, AC6 counts CRLF with `bytes([13, 10])`), so each stays a literal `python -c`; a
  criterion that needs an escape is written as a file under your scratch dir and its invocation runs that file.
- `:43` (rk-88's two calls): *"(a) SERP bronze keeps the raw public results body, and silver is scrubbed; (b) a Lusha
  zero-result lands as a placeholder SILVER row, not a state object, so "asked and found nothing" is a record with
  its fetch key."*  For THIS order, (a) is binding: bronze is the raw response body exactly as received (no scrub), and every
  silver row passes through `ceo_search.contact_scrub_text`; `test_bronze_is_the_exact_response_bytes` and
  `test_silver_rows_are_keyed_by_query_and_rank_and_scrubbed` are the two arms that prove each half.

**ROUND 22**, decomposition s.30 (cut by `2.0.0_SA_COO~Z`), cell H5 of the harvest format-migration chain, accepted by
`1.0.0_SA_CTO~Z` (msg 24090, *"(iii) rk-79 has drained, for H4/H5"*; msg 24098, v0.17 ADMITTED). The plan's own
recommendation for this channel (s.5.8): *"adopt; it is the cheapest channel to fix and the one where keeping the
response saves money directly."* Every live SERP call stays under Andrew's per-use word (the `bright-data` registry
row's note); this cell makes none. Andrew-direct ~15:12Z governs the one-slug issuance.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/harvest/bright_data_serp.py
lib/research/harvest/tests/test_bright_data_serp.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~88/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-88.bright-data-serp-writer.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** Reads need no grant (`store.py`, `test_store.py`, `ceo_search.py`,
  `enrich.py`, `data/find/dualbiz/scripts/serp.py`, the PRD, the plan). Scratch is `<your worktree>/.scratch/r88/`
  only (never committed).
- **Collision check, done at the cut** (a `<paths>` census over round 21's other drafts): rk-81 `lib/research/harvest/
  {__init__.py, store.py, tests/test_store.py}`; rk-82 two `infra/aws/terraform/harvest/*.tf`; rk-83 `harvest/
  {bloomberg.py, tests/test_bloomberg.py}`; rk-84 `harvest/{filings.py, tests/test_filings.py}`; rk-85 seven
  `integrations/seekingalpha/*` and `lib/opal_data_harvest/*` files; rk-86 `lib/research/social/*`; rk-87 `harvest/
  {lusha.py, tests/test_lusha.py}`. **Zero code-path overlap.** The only shared file is `INVESTIGATION_v1.md`
  (append-only; do not isolate it).
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~88 <0.9.0_WK_AMGT_RESAPP~88@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by the Write tool). Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

**THIS CELL IS CODE ONLY: NO BRIGHT DATA CALL, NO S3 WRITE OR READ, NO DEPLOY, NO NEVER-WIDEN PAIR.** No USD is spent;
no secret is read. **COLLECTION STAYS OFF. NO alarm, monitor, SNS/SES-send, notification or freshness checker.**
PORTAL not your surface. No non-ASCII in anything you write. **PUSH: never** (LD-0522).
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name -- in particular never by editing `store.py`,
`ceo_search.py`, `enrich.py` or the estate `serp.py`, and never by re-serialising a body before bronze.
**A COUNT BAR IS READ AT SPAWN AND PRINTS its denominator** -- re-measure both suites before you edit.
**SURPRISE ROWS:** `AMGT_RESAPP-Z-W88-S<k>`, `<k>` from 1; `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`; append by
textual splice inside the one fenced JSON array; never edit an existing row; `disarm_owner` is never a worker serial
(name `2.0.0_SA_COO~Z`). A pure disarm sets `DISMISSED_WITH_REASON` with a `dismissal_reason`.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-88"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c '
import importlib, os
print("store_file", os.path.exists("lib/research/harvest/store.py"))
s = importlib.import_module("lib.research.harvest.store")
need = ["SCOPE", "HARVEST_BUCKET", "BronzeImmutableError", "address_of", "date_partition", "stamp", "form_c_object", "fetch_key_exists", "bronze_put", "silver_append", "silver_latest", "record_hash"]
print("store_names_present", sum(1 for x in need if hasattr(s, x)), "of", len(need), "missing", [x for x in need if not hasattr(s, x)])
import inspect
print("bronze_put_takes_metadata", "metadata" in inspect.signature(s.bronze_put).parameters)
from lib import opal_naming as n
r = n.validate()
print("validate_refusals", len(r[0]) if isinstance(r, tuple) else r)
print("bronze", n.address("bright-data", "harvest", "bronze", "serp", "date=2026-09-21", "0" * 64 + "-p0.json"))
print("silver", n.address("bright-data", "harvest", "silver", "serp_result", "date=2026-09-21", "part-20260921T120000Z.parquet"))
'</invocation><expect>"store_file True"; "store_names_present 12 of 12 missing []"; "bronze_put_takes_metadata True"; "validate_refusals 0"; "bronze s3://opal-data-harvest/bright-data/harvest/bronze/serp/date=2026-09-21/0000000000000000000000000000000000000000000000000000000000000000-p0.json"; "silver s3://opal-data-harvest/bright-data/harvest/silver/serp_result/date=2026-09-21/part-20260921T120000Z.parquet". Any other reading -- store absent (rk-81 not merged), a missing name, a refusal, or a bucket other than opal-data-harvest -- is a STOP: file a BLOCKING row (disarm_owner 2.0.0_SA_COO~Z) and edit nothing</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-88"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/harvest/tests/test_bright_data_serp.py -v -p no:cacheprovider 2>&1 | tail -14</invocation><expect>a final line "9 passed" and 0 failed, the PASSED lines naming test_query_sha256_is_normalised_and_stable, test_teeing_transport_is_transparent_and_captures_bytes, test_bronze_is_the_exact_response_bytes, test_silver_rows_are_keyed_by_query_and_rank_and_scrubbed, test_stored_answer_skips_the_vendor_call, test_failed_result_writes_nothing, test_module_never_writes_outside_the_store, test_module_imports_no_network, test_patched_store_is_the_one_production_reaches</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-88"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/harvest/tests -q -p no:cacheprovider 2>&1 | tail -1 && python -m pytest lib/research/management/tests -q -p no:cacheprovider 2>&1 | tail -1</invocation><expect>two lines: first "N passed" and 0 failed where N is the harvest suite's count re-measured at spawn plus this cell's 9 (measured at 739eb5f288: harvest 28 = rk-81 11 + rk-83 9 + rk-84 8, so 37 if no sibling merges first); then "95 passed" (13 subtests) and 0 failed, UNCHANGED from the cut -- re-measure both before you edit and print the two baselines in your instance</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-88"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c '
import importlib
m = importlib.import_module("lib.research.harvest.bright_data_serp")
sink = []
def inner(gurl, zone, key): return 200, {"x-brd-status-code": "200"}, b"{\"organic\": [1]}"
t = m.teeing_transport(inner, sink)
out = t("https://www.google.com/search?q=x", "zone", "SECRET-KEY-VALUE")
print("transparent", out == inner("u", "z", "k"), "captured_bytes_exact", sink[0]["body"] == b"{\"organic\": [1]}", "key_leaked_into_sink", "SECRET-KEY-VALUE" in repr(sink))
a = m.query_sha256("  Tetsuya   Nakano Keyence CEO ")
b = m.query_sha256("Tetsuya Nakano Keyence CEO")
c = m.query_sha256("Tetsuya Nakano Keyence CEO", gl="jp")
print("normalised_equal", a == b, "locale_differs", a != c, "len", len(a))
'</invocation><expect>"transparent True captured_bytes_exact True key_leaked_into_sink False", then "normalised_equal True locale_differs True len 64" -- the tee is transparent to the primitive, keeps the exact bytes, never records the key argument, and the fetch key is normalised and locale-sensitive</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-88"><invocation>cd "$(git rev-parse --show-toplevel)" && env -u AWS_ACCESS_KEY_ID -u AWS_SECRET_ACCESS_KEY -u AWS_SESSION_TOKEN -u BRIGHT_DATA_API_KEY AWS_PROFILE=__rk88_no_such_profile__ AWS_CONFIG_FILE=/nonexistent AWS_SHARED_CREDENTIALS_FILE=/nonexistent python -m pytest lib/research/harvest/tests/test_bright_data_serp.py -q -p no:cacheprovider 2>&1 | tail -1</invocation><expect>"9 passed" and 0 failed with every AWS credential source pointed at nothing and BRIGHT_DATA_API_KEY unset -- the tests make no AWS, vendor or network call</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-88"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c '
import ast, hashlib, subprocess
PIN = "3863a8200d382e8b9943f7d03141326b93a86d26"
files = [f for f in subprocess.run(["git", "ls-files", "*.py"], capture_output=True, text=True).stdout.splitlines() if f]
files += [f for f in ("lib/research/harvest/bright_data_serp.py", "lib/research/harvest/tests/test_bright_data_serp.py") if f not in files]
importers, bad = [], 0
for f in files:
    try: tree = ast.parse(open(f, "rb").read().decode("utf-8"))
    except Exception: bad += 1; continue
    for node in ast.walk(tree):
        mods = []
        if isinstance(node, ast.Import): mods = [a.name for a in node.names]
        elif isinstance(node, ast.ImportFrom) and node.module: mods = [node.module] + [node.module + "." + a.name for a in node.names]
        if any(x == "lib.research.harvest.bright_data_serp" for x in mods): importers.append(f); break
print("py_files", len(files), "unparsed", bad, "importers", sorted(set(importers)))
for f in ("lib/research/management/enrich.py", "lib/research/management/ceo_search.py", "data/find/dualbiz/scripts/serp.py"):
    base = subprocess.run(["git", "show", PIN + ":" + f], capture_output=True).stdout
    print(f, "byte_equal_to_pin", open(f, "rb").read() == base, "pin_sha16", hashlib.sha256(base).hexdigest()[:16])
'</invocation><expect>"unparsed 0" and "importers ['lib/research/harvest/tests/test_bright_data_serp.py']" -- the new writer is imported by its own test ONLY, wired into nothing (rk-79's --research-stored-ceo path unchanged); then enrich.py "byte_equal_to_pin True pin_sha16 b1f2edb2550c037c", ceo_search.py "byte_equal_to_pin True pin_sha16 2b5da242faf81c50" and data/find/dualbiz/scripts/serp.py "byte_equal_to_pin True pin_sha16 2ea860ebc085e814" (PINNED commit, never HEAD or a merge-base -- row Z-S193)</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rk-88"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c '
import io
for f in ("lib/research/harvest/bright_data_serp.py", "lib/research/harvest/tests/test_bright_data_serp.py"):
    b = io.open(f, "rb").read()
    print(f, "compiles", bool(compile(b.decode("utf-8"), f, "exec")), "crlf", b.count(bytes([13, 10])), "non_ascii_bytes", len(b) - len(b.decode("utf-8")))
'</invocation><expect>both files print compiles True, crlf 0 and non_ascii_bytes 0 (both are NEW, absent at the pin)</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~88/AMGT_RESAPP.TO-AMGT-rk-88.bright-data-serp-writer.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4,AC5,AC6` (rc 0 is the verdict); flip the order's
status to `complete`; commit with `--only -- <paths>`. Report once, naming both suite counts before and after, the
AC3 outputs, and the AC5 importer list.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/r88/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**Issuer notes (not for the worker):** spawn only after rk-81 DRAINS (AC0 stops otherwise). Open questions carried to
the issuer at draft time: (1) RAW SERP BRONZE AND CONTACT DATA -- the primitive scrubs contact keys from the PARSED body
before building records (`serp.py:470`, `_scrub_body`), so today nothing reaches storage unscrubbed; bronze "as
received" keeps the RAW body, which can carry any contact key a result block holds (measured by the primitive's author:
only `general.mobile`, a locale flag, was ever removed from a real response). REC: keep raw bronze per
C-BRONZE-AS-RECEIVED (public search results, not a contact broker; silver stays scrubbed), and name it to the CTO -- the
alternative is a C-LUSHA-EXCEPTION-style declared departure; (2) bronze keeps the LAST 2xx attempt per page, not every
retry attempt -- "one object per fetch" read as one per page served; (3) `harvest_serp` takes the real transport as a
required `inner=` argument because the primitive's default transport is not reachable from outside it; the move cell
passes `serp._bd_transport` there; (4) the stored-answer window is the fetch-date partition; the move cell may widen it.

<status>pending</status>
<round>22</round>
<slot>~88</slot>
<fabric>site-z</fabric>
