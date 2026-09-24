# AMGT_RESAPP task order -- `AMGT-rk-81` -- H0-store: ONE shared bronze/silver writer for the harvest channels (`lib/research/harvest/store.py`): bronze byte-exact and never overwritten, silver parquet with lineage columns and unchanged-row skip, the bucket-authority fetch-key check, the Lusha exception, the slash-safe partition -- built offline against a stub S3, writing NOTHING live

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-81</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~81</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order adds one new library package and its tests and runs them
  offline; it arms no cron, alarm, monitor or cadence, reads no schedule and writes none (scope checked: the order's
  whole write surface is lib/research/harvest/ plus its own deliverables, channel and order file).
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant is read or changed; the module makes no live AWS call
  in this order (every test runs against an in-process stub S3, and AC4 proves it by running with the AWS credential
  variables pointed at an invalid profile). The READ grants the served roles need on the new prefixes are AMGT-rk-82's,
  a separate cell with its own pair.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~81`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that
`org/`, `.tools/`, `lib/opal_naming.py` and `lib/research/identity/crosswalk.py` exist; if any is absent, STOP with a
BLOCKING row. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~81;`. **NEVER RUN AN INSTALL.**
Never read, show, diff or check out branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50` -- it holds an exposed
credential.

## 1. THE CELL, inlined in full -- `AMGT-rk-81` (H0-store, round 21 wave 1)

**The acceptance of record (`1.0.0_SA_CTO~Z`, msg 24090, 2026-09-21T21:25:25Z), verbatim:** *"ROUND 21
(2.0.0_SA_COO~Z): waves 1 + 2 (H0-store, H0-iam, H1-H6) = 8 cells is ACCEPTED. It is cut at round 20's L10
(LD-0521), and only when (i) both v0.17 halves are signed (LIMB 6), (ii) Z-S203 has disarmed so the builder prints
harvest, and (iii) rk-79 has drained, for H4/H5."*

**The contracts this cell builds to, `prd/AMGT_RESAPP_PRD.md` v0.17 @`6f39881c3c`, verbatim:**
- `:856-864` C-HARVEST-HOME: *"AMGT_RESAPP's bronze, silver, gold, platinum, state and code live exactly where the
  builder prints them. Under scope `harvest` and its GENERAL tenancy, that is `opal-data-harvest` for every tier ...
  Every address is `lib/opal_naming.py address()` output ... a builder refusal is a missing registry row, never a
  hand-typed key ... This contract is NOT MET while the registry carries more than one `harvest` scope row: the
  builder takes the first, a PRODUCT-tenancy row, and prints `opal-data-assets` for bronze and silver. No harvest
  writer is cut against this contract until only the GENERAL row remains (row Z-S203)."*
- `:866-871` C-BRONZE-AS-RECEIVED: *"Bronze is the response bytes exactly as received -- no parsing, trimming or
  re-serialising -- one object per fetch, never overwritten, with the channel's FETCH key in the partition, in one of
  three forms: (a) an entity fetched repeatedly: `{vendor}/harvest/bronze/{request}/{entity}={id}/{YYYYMMDDTHHMMSSZ}.{ext}`;
  (b) an immutable document: `{vendor}/harvest/bronze/{request}/{entity}={id}/{document id}/{vendor file name}`;
  (c) a request: `{vendor}/harvest/bronze/{request}/date=YYYY-MM-DD/{request hash or file}.{ext}`."*
- `:873-875` C-SILVER-PARQUET: *"Silver is parquet with every vendor field kept and typed, partitioned `date=` by
  fetch date, one part file per run. Every row carries `bronze_key`, `fetched_at` and `record_hash` (sha256 of the
  row's vendor fields)."*
- `:877-881` C-LUSHA-EXCEPTION: *"Lusha keeps NO bronze, and its silver DROPS every contact field (emails, phone
  numbers and any other channel for reaching a person) ... Its silver rows carry `fetched_at` and `record_hash`, and
  `bronze_key` is null by rule."*
- `:883-888` C-DEDUPE-BY-KEY: *"Before any vendor call, the writer checks the bucket for the fetch key ... A silver
  writer skips an unchanged `(record key, record_hash)` and writes a changed row as a new row, never an update; a
  reader takes the newest `fetched_at` per record key. The bucket is the authority for what has been fetched, never a
  file on one desktop."*
- `:890-891` C-SLASH-SAFE-KEY: *"One slash-safe security key is minted in the crosswalk module and used everywhere
  downstream. An entity id sits in a partition, never in the builder's free-form `object` argument."*

**THE MEASURED STATE (issuer, HEAD `b832f7b03e`; RE-READ every line at your branch HEAD before editing):**
- `lib/research/harvest/` does NOT exist (`test -e lib/research/harvest/store.py` -> absent). This cell creates it.
- `lib/opal_naming.py`: `key(source, scope, tier, table, partition)` `:1610`; `address(source, scope, tier, table,
  partition, object=None)` `:1626`. `address()` validates each segment and appends `/{object}`.
- `lib/research/identity/crosswalk.py`: `security_key_partition()` `:234` (rk-76). `security_key_partition("BP/_LN_Equity")`
  returns `security_key=BP-SLASH-_LN_Equity`. `write_pool()` `:909` is the estate's existing conditional-put idiom,
  with `IfNoneMatch "*"` / `IfMatch`, Metadata `{document-sha256, schema-version}` and a head read-back. Reuse its
  SHAPE; do not import it for bronze, because bronze is never an `IfMatch` overwrite.
- `pyarrow` 24.0.0 and `pandas` 3.0.3 import on this box. No install is needed.
- **Builder output, measured by the issuer:**
  - On the LIVE registry (Z-S203 armed, registry_hash `d2b29b3dd5794464`), `address("bloomberg","harvest","bronze",
    "refdata","security_key=BP-SLASH-_LN_Equity","20260921T120000Z.json")` =
    `s3://opal-data-assets/bloomberg/harvest/bronze/refdata/security_key=BP-SLASH-_LN_Equity/20260921T120000Z.json`.
  - On a scratch registry with scopes.json row [8] removed (validate 0 refusals, hash `ae3acac5cdddda46`), it is
    `s3://opal-data-harvest/...` with the same key. Silver `lusha/contact_match` behaves the same way.
  - **Re-read at HEAD `ec4e000709`:** 4.0.0_SA_CRO deleted the stale PRODUCT `harvest` row @`10bace8916` (Z-S203's
    fix). The LIVE builder now prints `s3://opal-data-harvest/...` for harvest bronze and silver (live registry_hash
    `3ea1e46b06a8aa14`, validate 0 refusals). AC0 still gates, in case the row is ever re-introduced by an integrate.
- **Test-suite baselines at HEAD `b832f7b03e`:** `lib/research/identity/tests` 55 passed, `lib/research/api/tests`
  191 passed.

**RULED, what you build -- the WHOLE public interface, exactly these names (AC5 checks the set):**
1. `lib/research/harvest/__init__.py`, empty apart from a one-line docstring.
2. `lib/research/harvest/store.py` defines:
   - **Constants:** `SCOPE = "harvest"`; `HARVEST_BUCKET = "opal-data-harvest"` (used ONLY to ASSERT a builder URI's
     bucket, never to build one); `SCHEMA_VERSION = 1`; `LINEAGE_COLUMNS = ("bronze_key", "fetched_at",
     "record_hash")`; `CONTACT_FIELDS = frozenset({"email", "emails", "phone", "phones", "phone_number",
     "phone_numbers", "mobile", "mobile_phone", "direct_dial", "work_phone", "personal_email", "contact_info",
     "email_addresses"})`. **Matching is by NORMALISED name** (lowercase, `_` and `-` removed) on both sides, so
     Lusha's camelCase `emailAddresses` / `phoneNumbers` / `directDial` are caught (issuer L5 ruling at the round-21
     cut, from the H4 drafter's finding: a snake_case-only set misses Lusha's own key names).
   - **Errors:** `HarvestStoreError(Exception)` and its subclasses `NotHarvestHomeError`, `BronzeImmutableError`,
     `LushaExceptionError`, `SilverRowError`.
   - **Pure helpers:**
     - `entity_partition(entity, entity_id)`: `security_key` goes through `crosswalk.security_key_partition`; any
       other id containing "/" raises `ValueError`.
     - `date_partition(d)`: returns `"date=YYYY-MM-DD"`.
     - `stamp(dt)`: a tz-aware datetime gives `YYYYMMDDTHHMMSSZ` in UTC; a naive one raises `ValueError`.
     - `form_a_object(fetched_at, ext)`, `form_b_object(document_id, vendor_file_name)`,
       `form_c_object(request_hash_or_file, ext=None)`.
   - **Addressing:**
     - `address_of(source, tier, table, partition, object_name=None)` returns `address(source, SCOPE, ...)`. It
       raises `NotHarvestHomeError` unless the URI's bucket is `HARVEST_BUCKET`.
     - `table_prefix(source, tier, table)` returns the key prefix `"{source}/harvest/{tier}/{table}/"`, derived by
       calling `key(source, SCOPE, tier, table, "date=1970-01-01")` and cutting the final segment. It is never typed.
   - **Bronze:**
     - `fetch_key_exists(source, request, partition, object_prefix="", client=None)` returns a list of keys
       (paginated `list_objects_v2`).
     - `bronze_put(source, request, partition, object_name, body, content_type="application/octet-stream",
       metadata=None, client=None)`:
       - ONE `put_object(..., IfNoneMatch="*", Metadata={"document-sha256": ..., "schema-version": ...,
         **<validated caller metadata>})`.
       - `metadata` (optional dict, default None): extra S3 USER METADATA merged into the fixed Metadata. Rule: every key is
         lowercased and must match `^[a-z0-9][a-z0-9-]*$` (ASCII, no spaces, no underscores); every value is a str of
         printable ASCII (0x20-0x7E, no newline). The reserved keys `document-sha256` and `schema-version` are REFUSED
         with `HarvestStoreError` (the family's base class, so the public name set is unchanged), as is any key or value
         breaking the rule -- all before any call. Metadata never enters the idempotency test: it is keyed on the BYTES'
         sha256 only. Same bytes with DIFFERENT metadata give `existed=True, put_performed=False` and nothing is
         rewritten -- bronze is write-once, so the first write's metadata stands.
       - Why: CTO msg 24106 item 2 CONDITION -- Bloomberg bronze records `received_form "bbg-client-json"`;
         rk-83 passes `metadata={"received-form": "bbg-client-json"}`.
       - On a `PreconditionFailed` (the object exists), a `head_object`: the same sha256 gives
         `existed=True, put_performed=False`, and a different one raises `BronzeImmutableError`.
       - Then a head read-back that checks sha256 and ContentLength, exactly as `write_pool` does.
       - Receipt: `{uri, bucket, key, sha256, content_length, put_performed, existed}`.
       - `source == "lusha"` raises `LushaExceptionError` before any call.
   - **Silver:**
     - `record_hash(row)`: sha256 hex of `json.dumps({k: v for k, v in row.items() if k not in LINEAGE_COLUMNS},
       sort_keys=True, default=str, separators=(",", ":"))`.
     - `_unchanged(latest_row, new_hash)`: a single private function returning whether the latest row's
       `record_hash` equals `new_hash`. It is the ONLY place the skip decision is made, and AC3's mutant rewrites it.
     - `silver_latest(source, table, record_key_fields, client=None)`: reads every `part-*.parquet` under
       `table_prefix(source, "silver", table)` and returns `{record_key_tuple: row}` holding the newest `fetched_at`.
     - `silver_append(source, table, rows, record_key_fields, run_stamp, client=None)`:
       - Validates every row BEFORE any write: `fetched_at` present and tz-aware; `bronze_key` present, and `None`
         if and only if `source == "lusha"`; no `CONTACT_FIELDS` key (by normalised name, so `emailAddresses` counts) when `source == "lusha"`; the
         existing Lusha-refusal test arm ALSO asserts a camelCase `emailAddresses` row is refused (no new arm).
       - Computes `record_hash` and skips rows where `_unchanged` is true.
       - Groups the remaining rows by fetch date and writes ONE `part-<run_stamp>.parquet` per `date=` partition
         with `IfNoneMatch="*"`, built with `pyarrow.Table.from_pylist`. A type conflict raises `SilverRowError`.
       - Receipt: `{written_rows, skipped_unchanged, parts}`.
   - Every URI the module touches comes from `address_of`. The module holds no bucket or key literal other than
     `HARVEST_BUCKET` and the `part-` / `.parquet` object-name pieces.
   - boto3 is imported LAZILY inside the functions that need a default client, and every function accepts `client=`.
3. `lib/research/harvest/tests/test_store.py`. It loads the module under test from the environment variable
   `HARVEST_STORE_UNDER_TEST` (a file path) if set, and otherwise from `lib.research.harvest.store`, so that AC3 can run
   the same arms against a mutant. It defines ONE in-process stub S3 client. The stub honours `IfNoneMatch="*"` by
   raising a botocore `ClientError` with code `PreconditionFailed`; it stores `Metadata` per key and returns it from `head_object`; and it accepts and ignores
   any other keyword. It
   has `put_object`, `head_object`, `get_object`, `list_objects_v2` and `get_paginator("list_objects_v2")`. There are
   EXACTLY these 11 arms:
   - `test_address_is_builder_output`
   - `test_refuses_when_builder_prints_another_bucket`: monkeypatch `address` to return an `opal-data-assets` URI
     and expect `NotHarvestHomeError`.
   - `test_bronze_bytes_as_received`: `get_object` returns the body byte-for-byte, and `document-sha256` matches.
   - `test_bronze_never_overwritten`: the same bytes give `existed=True, put_performed=False`; different bytes give
     `BronzeImmutableError`; the stub holds the FIRST bytes.
   - `test_forms_abc_objects`: the three helpers against the three contract forms.
   - `test_security_key_partition_is_slash_safe`: `BP/_LN_Equity` becomes `security_key=BP-SLASH-_LN_Equity`, and
     `entity_partition("cik", "a/b")` raises.
   - `test_fetch_key_exists`: an empty list before the put, the key after.
   - `test_silver_append_lineage_and_one_part_per_date`: rows over 2 fetch dates give 2 parts; every row carries the 3
     lineage columns; the parquet reads back; `record_hash` matches `record_hash(row)`.
   - `test_silver_skips_unchanged_and_appends_changed`: run 2 has one row unchanged and one changed, giving
     `written_rows 1`, `skipped_unchanged 1`; `silver_latest` returns the newer `fetched_at` for the changed key.
   - `test_lusha_exception`: `bronze_put("lusha", ...)` raises; a Lusha silver row with a non-None `bronze_key`
     raises; a Lusha row carrying `email` raises; a valid Lusha row with `bronze_key None` writes.
   - `test_bronze_metadata_merged_reserved_refused`: `metadata={"received-form": "bbg-client-json"}` lands on
     the object beside `document-sha256` and `schema-version`; `metadata={"document-sha256": "x"}` and
     `metadata={"Bad Key": "v"}` each raise `HarvestStoreError` before any `put_object`; a second
     `bronze_put` of the SAME bytes with DIFFERENT metadata returns `existed=True, put_performed=False` and the
     stored metadata is still the first write's.

**What this cell does NOT change:**
- It writes no S3 object, no registry row, no Terraform, and no channel writer. H1-H6 (rk-83..rk-86 and the H4/H5
  cells) are the callers, in wave 2.
- It edits no existing file. Its write surface is new files only, plus its deliverable, the channel and this order.
- It never edits `lib/opal_naming.py` or `infra/logic/registry/**`.

## 2. WHERE THIS CAME FROM

- **Round 21**, decomposition s.29, cut by `2.0.0_SA_COO~Z`.
- The proposal it comes from: `HARVEST_CHAIN_DECOMP_PROPOSAL`, cell "H0 store", s.3.
- The CTO's rulings: msg 24090 (round-21 shape accepted) and msg 24086 (platinum and the builder binds).
- PRD v0.17 @`6f39881c3c`.
- Andrew-direct ~17:2xZ (the backfill held for the bronze/silver shape), record @e70b949ba0.
- Andrew-direct ~15:12Z (one slug per round).

## 3. SURFACES -- what you may read and write

<paths>
lib/research/harvest/__init__.py
lib/research/harvest/store.py
lib/research/harvest/tests/test_store.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~81/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-81.harvest-store-writer.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** A READ needs no grant: `lib/opal_naming.py`, `crosswalk.py`, the
  PRD and the plan. Scratch goes in `<your worktree>/.scratch/r81/` only and is never committed.
- **Collision check, done at the cut:** the other round-21 cells write `infra/aws/terraform/harvest/*.tf` (rk-82) and
  their channels' writer files (wave 2), and none writes `lib/research/harvest/`. Round-20 rk-79 writes
  `lib/research/management/*`, which is disjoint. The only shared file is `INVESTIGATION_v1.md`; it is append-only,
  so do not isolate it.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~81 <0.9.0_WK_AMGT_RESAPP~81@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by the Write tool). Never push, merge, rebase, `checkout --`, `stash` or `clean`. Every `.py`
  passes `.tools/commit-gate.sh` inside safe-commit (py_compile, ds-precommit, ruff py39, and the naming limb).

## 4. BOUNDS

- **NO LIVE ACT.** No S3 call, no Bloomberg, no vendor, no Lusha, no IAM, no Terraform. AC4 is the proof.
- **AC0 IS A GATE.** If the REAL registry's builder still prints `opal-data-assets` for harvest bronze, row Z-S203 has
  not disarmed and C-HARVEST-HOME is NOT MET: STOP, file a BLOCKING row (disarm_owner `2.0.0_SA_COO~Z`) and build
  nothing.
- **COLLECTION STAYS OFF.** **NO alarm, monitor, SNS/SES-send, notification or freshness checker.** No secret. No
  non-ASCII in anything you write. **PUSH: never** (LD-0522).
- **THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row. It is
  never repaired, never widened, and never satisfied by a route this order did not name: never by editing
  `opal_naming.py` or the registry, never by typing a bucket or key, never by a live call.
- **A COUNT BAR IS READ AT SPAWN AND PRINTS its denominator.** Re-measure the identity (55) and api (191) baselines
  before you edit.
- **SURPRISE ROWS:** `AMGT_RESAPP-Z-W81-S<k>`, `<k>` from 1; `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`.
  Append by textual splice inside the one fenced JSON array and never edit an existing row. A row's `disarm_owner` is
  never a worker serial; name the issuer, `2.0.0_SA_COO~Z`.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-81"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import sys; sys.path.insert(0, "."); import lib.opal_naming as n; r = n.validate(); print("validate_refusals", len(r[0])); print("builder", n.address("bloomberg", "harvest", "bronze", "refdata", "security_key=BP-SLASH-_LN_Equity", "20260921T120000Z.json")); print("builder_silver", n.address("lusha", "harvest", "silver", "contact_match", "date=2026-09-21", "part-x.parquet"))'</invocation><expect>validate_refusals 0; builder s3://opal-data-harvest/bloomberg/harvest/bronze/refdata/security_key=BP-SLASH-_LN_Equity/20260921T120000Z.json; builder_silver s3://opal-data-harvest/lusha/harvest/silver/contact_match/date=2026-09-21/part-x.parquet -- the REAL registry after Z-S203's disarm. At the cut (HEAD b832f7b03e, Z-S203 armed) the same call printed s3://opal-data-assets/...; at ec4e000709, after 4.0.0_SA_CRO's fix @10bace8916 deleted the stale PRODUCT harvest row, it printed s3://opal-data-harvest/... as expected; any opal-data-assets output here means C-HARVEST-HOME is NOT MET: STOP, file a BLOCKING row, build nothing</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-81"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/harvest/tests/test_store.py -v -p no:cacheprovider 2>&1 | tail -17</invocation><expect>"11 passed" and 0 failed, the PASSED lines naming exactly test_address_is_builder_output, test_refuses_when_builder_prints_another_bucket, test_bronze_bytes_as_received, test_bronze_never_overwritten, test_forms_abc_objects, test_security_key_partition_is_slash_safe, test_fetch_key_exists, test_silver_append_lineage_and_one_part_per_date, test_silver_skips_unchanged_and_appends_changed, test_lusha_exception, test_bronze_metadata_merged_reserved_refused</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-81"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/harvest/tests lib/research/identity/tests lib/research/api/tests -q -p no:cacheprovider 2>&1 | tail -2</invocation><expect>one final line "N passed" with 0 failed, N = 11 + the identity and api baselines re-measured at spawn (55 + 191 = 246 at the cut, so 257 if unmoved) -- the new package adds exactly its 11 arms and breaks nothing it imports</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-81"><invocation>cd "$(git rev-parse --show-toplevel)" && mkdir -p .scratch/r81 && python -c 'import io, re, subprocess, os, sys; src = io.open("lib/research/harvest/store.py", encoding="utf-8").read(); n1 = src.count("IfNoneMatch=\"*\""); m1 = src.replace("IfNoneMatch=\"*\"", "ContentLanguage=\"mutant\""); m2 = src + "\n\ndef _unchanged(latest_row, new_hash):\n    return False\n"; io.open(".scratch/r81/m1.py", "w", encoding="utf-8", newline="\n").write(m1); io.open(".scratch/r81/m2.py", "w", encoding="utf-8", newline="\n").write(m2); print("ifnonematch_sites", n1)
for tag, arm in (("m1", "test_bronze_never_overwritten"), ("m2", "test_silver_skips_unchanged_and_appends_changed")):
    env = dict(os.environ, HARVEST_STORE_UNDER_TEST=os.path.abspath(".scratch/r81/%s.py" % tag)); r = subprocess.run([sys.executable, "-m", "pytest", "lib/research/harvest/tests/test_store.py", "-q", "-p", "no:cacheprovider", "-k", arm], capture_output=True, text=True, env=env); print(tag, arm, "rc", r.returncode, (r.stdout.strip().splitlines() or [""])[-1])'</invocation><expect>ifnonematch_sites at least 2 (bronze_put and silver_append); then "m1 test_bronze_never_overwritten rc 1 ... 1 failed" and "m2 test_silver_skips_unchanged_and_appends_changed rc 1 ... 1 failed" -- each arm FAILS against its mutant (the conditional put removed; the unchanged-row skip disabled), so the arms that pass in AC1 discriminate the two contract behaviours rather than pass vacuously. A mutant arm that PASSES fails this criterion</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-81"><invocation>cd "$(git rev-parse --show-toplevel)" && AWS_PROFILE=rk81-no-such-profile AWS_ACCESS_KEY_ID=invalid AWS_SECRET_ACCESS_KEY=invalid AWS_SESSION_TOKEN=invalid python -m pytest lib/research/harvest/tests/test_store.py -q -p no:cacheprovider 2>&1 | tail -1 && python -c 'import ast, io; t = ast.parse(io.open("lib/research/harvest/store.py", encoding="utf-8").read()); top = [n for n in t.body if isinstance(n, (ast.Import, ast.ImportFrom))]; names = sorted({a.name for n in top for a in n.names} | {n.module or "" for n in top if isinstance(n, ast.ImportFrom)}); print("top_level_imports", names); print("boto3_at_top", any("boto3" in x for x in names))'</invocation><expect>"11 passed" with the AWS credentials pointed at an invalid profile -- so no arm makes a live call; then top_level_imports listing no boto3/botocore module and boto3_at_top False (boto3 imported lazily inside the functions that build a default client)</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-81"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import sys; sys.path.insert(0, "."); from lib.research.harvest import store as s; want = sorted(["SCOPE", "HARVEST_BUCKET", "SCHEMA_VERSION", "LINEAGE_COLUMNS", "CONTACT_FIELDS", "HarvestStoreError", "NotHarvestHomeError", "BronzeImmutableError", "LushaExceptionError", "SilverRowError", "entity_partition", "date_partition", "stamp", "form_a_object", "form_b_object", "form_c_object", "address_of", "table_prefix", "fetch_key_exists", "bronze_put", "record_hash", "silver_latest", "silver_append"]); have = sorted(k for k, v in vars(s).items() if not k.startswith("_") and ((callable(v) and getattr(v, "__module__", None) == s.__name__) or (k.isupper() and not callable(v)))); print("missing", sorted(set(want) - set(have))); print("extra", sorted(set(have) - set(want))); print("public", len(want))'</invocation><expect>missing [] and extra [] with public 23 -- the module's public names are EXACTLY the interface the wave-2 channel cells are drafted against (.scratch interface H0_STORE_INTERFACE.md, fixed at issuance); a renamed, missing or added public name fails this criterion, because rk-83..rk-86 call these names</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rk-81"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import io; [print(f, "compiles", bool(compile(io.open(f, "rb").read().decode("utf-8"), f, "exec")), "crlf", io.open(f, "rb").read().count(b"\r\n"), "non_ascii_bytes", len(io.open(f, "rb").read()) - len(io.open(f, "rb").read().decode("utf-8"))) for f in ("lib/research/harvest/__init__.py", "lib/research/harvest/store.py", "lib/research/harvest/tests/test_store.py")]'</invocation><expect>all 3 files print compiles True, crlf 0 and non_ascii_bytes 0 (the files are new; the base figure is absent by construction)</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this
order.

## 6. WHEN YOU ARE DONE

1. Write your instance to
   `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~81/AMGT_RESAPP.TO-AMGT-rk-81.harvest-store-writer.proof_of_spec.json`
   per `org/standards/PROOF_OF_SPEC.schema.json`.
2. Grade it with YOUR WORKTREE'S OWN `python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4,AC5,AC6`;
   rc 0 is the verdict.
3. Flip the order's status tag to `complete`, then commit with `--only -- <paths>`.
4. Report once, naming: the suite counts before and after; AC3's two mutant outcomes; and the module's public names.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/r81/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**Issuer notes:**
- No never-widen pair: the cell has no live act.
- AC0 gates the whole cell on Z-S203's disarm. The interface section above is the contract `rk-83..rk-86` are
  drafted against, and it is saved standalone at `.scratch/r21_drafts/H0_STORE_INTERFACE.md`.
- Wave 1 runs beside `AMGT-rk-82` (H0-iam, `infra/aws/terraform/harvest/*.tf`), with a disjoint write surface.
- Wave 2 channel cells may be SPAWNED only after this cell DRAINS, because they import `lib.research.harvest.store`.

<status>complete</status>
<round>21</round>
<slot>~81</slot>
<fabric>site-z</fabric>
