# AMGT_RESAPP task order -- `AMGT-rk-83` -- H1-bloomberg: the Bloomberg channel's harvest writer, built on H0-store and NOT yet wired in -- six bronze requests as received under `security_key=` (form a), and `model_block` silver as a LOSSLESS re-serialisation of the existing JSON (typed rows keyed `(security_key, fiscal_year, mnemonic)`), proven offline and by a read-only round trip over every live `derived/model_block` object

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-83</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~83</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order adds one new library module and its tests; it arms no cron,
  alarm, monitor or cadence, reads no schedule and writes none (scope checked: the whole write surface is
  lib/research/harvest/bloomberg.py, lib/research/harvest/tests/test_bloomberg.py, its deliverables, the channel and
  this order). No Bloomberg pull is made; the existing pull producers keep running unchanged.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant is read or changed. The one AWS use is AC4's READ-ONLY
  round trip (list_objects_v2 + get_object over derived/model_block/ in opal-data-harvest) under the seat's existing
  credentials, the same read the issuer ran at the cut; no put, copy or delete anywhere. The served roles' read grants
  on the new prefixes are AMGT-rk-82's.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~83`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that
`org/`, `.tools/`, `lib/opal_naming.py` and `lib/research/harvest/store.py` exist; if any is absent, STOP with a
BLOCKING row. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~83;`. **NEVER RUN AN INSTALL.**
Never read, show, diff or check out branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50` -- it holds an exposed
credential.

## 1. THE CELL, inlined in full -- `AMGT-rk-83` (H1-bloomberg, round 21 wave 2)

**The acceptance of record (`1.0.0_SA_CTO~Z`, msg 24090, 2026-09-21T21:25:25Z), verbatim:** *"ROUND 21
(2.0.0_SA_COO~Z): waves 1 + 2 (H0-store, H0-iam, H1-H6) = 8 cells is ACCEPTED. It is cut at round 20's L10
(LD-0521), and only when (i) both v0.17 halves are signed (LIMB 6), (ii) Z-S203 has disarmed so the builder prints
harvest, and (iii) rk-79 has drained, for H4/H5."* PRD v0.17 is ADMITTED @`1f7459456a` (CTO msg 24098).

**THE RULING OF RECORD ON THIS CELL (`1.0.0_SA_CTO~Z` msg 24106 (2026-09-21T21:53:32Z, answering msg 24105), `org/mcp/inbox/2.0.0_SA_COO/~Z/read/20260921T215332Z_1.0.0_SA_CTO_Z_Re_24105__round_21_s_5_spec_calls_RULED_.md`), item 2, verbatim:** *"2. Bloomberg bronze \"as received\": ACCEPTED. The Terminal client's JSON serialisation of the dict it hands the producer IS Bloomberg's as-received form, because the wire bytes are unreachable in our client. CONDITION: the serialisation is deterministic (sort_keys, fixed separators, UTF-8), so that a repeated fetch of unchanged data yields identical bytes. The bronze object records `received_form: \"bbg-client-json\"`. I write it into C-BRONZE-AS-RECEIVED at the next bump, so a reader of the contract is not misled. It binds from this ruling."*
(Items 1 and 3 of the same message rule the SA hash prefix and the UNRESOLVED filings markers -- rk-85's and
rk-84's concerns, not this cell's.)

**The contracts, `prd/AMGT_RESAPP_PRD.md` v0.17 @`1f7459456a`, verbatim:**
- `:866` C-BRONZE-AS-RECEIVED: *"Bronze is the response bytes exactly as received -- no parsing, trimming or
  re-serialising -- one object per fetch, never overwritten, with the channel's FETCH key in the partition, in one of
  three forms: (a) an entity fetched repeatedly: `{vendor}/harvest/bronze/{request}/{entity}={id}/{YYYYMMDDTHHMMSSZ}.{ext}`
  ..."*
- `:873` C-SILVER-PARQUET: *"Silver is parquet with every vendor field kept and typed, partitioned `date=` by fetch
  date, one part file per run. Every row carries `bronze_key`, `fetched_at` and `record_hash` (sha256 of the row's
  vendor fields)."*
- `:885` C-DEDUPE-BY-KEY: *"Each channel names a FETCH key and a RECORD key. Before any vendor call, the writer checks
  the bucket for the fetch key. Exactly one writer holds a channel's fetch keys at a time ..."*
- `:892` C-SLASH-SAFE-KEY: *"One slash-safe security key is minted in the crosswalk module and used everywhere
  downstream. An entity id sits in a partition, never in the builder's free-form `object` argument."*
- `:906-907` (C-FORMAT-SEQUENCE): *"A lossless re-serialisation is a copy. An existing JSON object re-written as
  parquet silver, with every field kept, counts as a copy under this contract, not a re-derivation. Each object is
  graded by a round-trip equality check."*

**The plan it builds** (`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/PLAN_AMGT_HARVEST_CHANNEL_FORMATS_20260921.md`
@`1a9f1c4469`, s.5.1 `:158-198`): bronze requests `refdata`, `histdata`, `histdata_daily_px`, `bestdata`, `identity`,
`exec_officers`, each `.../bloomberg/harvest/bronze/<request>/security_key=<key>/<stamp>.json`; silver
`model_block`, record key `(security_key, fiscal_year, mnemonic)` (`:182-186`); `pull_log.json` is a run log that
moves to STATE, not bronze (`:179-180`); retire `model_block_fye` (`:197`).

**THE MEASURED STATE (issuer, HEAD `5912b7d107`; RE-READ every line at your branch HEAD before editing):**
- **Builder, live registry** (validate 0 refusals, after 4.0.0_SA_CRO's fix @`10bace8916`):
  `address("bloomberg","harvest","bronze","refdata","security_key=BP-SLASH-_LN_Equity","20260921T120000Z.json")` =
  `s3://opal-data-harvest/bloomberg/harvest/bronze/refdata/security_key=BP-SLASH-_LN_Equity/20260921T120000Z.json`;
  the same shape for `histdata`, `bestdata`, `histdata_daily_px`, `identity`, `exec_officers` (6 of 6 print
  `opal-data-harvest`); silver `model_block`, `date=2026-09-21`, `part-20260921T120000Z.parquet` =
  `s3://opal-data-harvest/bloomberg/harvest/silver/model_block/date=2026-09-21/part-20260921T120000Z.parquet`.
- **H0-store** (`AMGT-rk-81`, wave 1) provides `lib/research/harvest/store.py`. Its public interface is fixed
  (23 names; its own AC5 checks the set). This cell CALLS it and never writes S3 itself. The names you use:
  `bronze_put`, `fetch_key_exists`, `silver_append`, `silver_latest`, `record_hash`, `address_of`, `entity_partition`,
  `form_a_object`, `stamp`, `date_partition`, `LINEAGE_COLUMNS`, `HarvestStoreError` and subclasses.
  `entity_partition("security_key", "BP/_LN_Equity")` = `"security_key=BP-SLASH-_LN_Equity"`.
- **The live silver source to be copied later** (read-only, 2026-09-21 ~21:5xZ): `derived/model_block/` in
  `opal-data-harvest` holds **122 objects**, all leaf `model_block.json`, 13,179,447 bytes, **0 with zero figures**
  (min 129 figures), **23,998 figures** in all, **0 duplicate `(fiscal_year, mnemonic)` within an object**.
  - Top-level key sets: **4** -- 113 `{figures, fiscal_year_row_count, fiscal_years, orphan_price_rows,
    raw_stamp_used, security, security_key, unresolved}`; 3 add `history_window`; 3 add `history_window,
    forecast_fallback`; 3 add `history_window, forecast_fallback, cases`. Types: `fiscal_years` list, `unresolved`
    list, `history_window` / `forecast_fallback` / `cases` dict.
  - Figure key sets: **3** -- 22,752 `{basis, currency_caveat, fiscal_year, mnemonic, scope, sign, source, unit,
    value, vintage}`; 1,156 the same WITHOUT `currency_caveat`; 90 without `currency_caveat` and WITH `estimate_basis,
    fiscal_period, override, period_end_date`.
  - `value` types: **23,504 float, 494 str** -- a mixed column, which H0-store's `silver_append` refuses. `basis` is a
    dict on every figure; `fiscal_year` is None on header rows.
- **The current writers of this channel's fetch keys** -- census by SUBTRACTION over every non-test S3 write call site
  in `integrations/bloomberg/research`, `lib/research/management`, `lib/research/filings`, `lib/research/identity`
  (native Grep `put_object\(|write_pool\(`): **19 call sites**. Minus 4 filings `.source.json` writers
  (`fetch.py:426`, `batch.py:341`, `batch.py:553`, `battery.py:1314`), minus 3 `.analysis.json` writers
  (`analyze.py:1388,1496,1546`), minus 7 non-Bloomberg pool writers (`pull_consumer.py:67` packs status,
  `enrich.py:794`, `enrich.py:870`, `crosswalk.py:929`, `crosswalk.py:988`, `build_universe.py:918`,
  `add_security.py:159`) = **5 Bloomberg writers**: `model_block_pull.py:336` (`s3_put_if_absent`: refdata, histdata,
  bestdata, pull_log, model_block), `pull_baba_daily_px.py:64` (histdata_daily_px), `derive_fye_fixed.py:84`
  (model_block_fye, 0 readers), `bloomberg_fallback.py:100` (exec_officers), `add_security.py:122` (identity).
  **They are NOT changed by this cell.** They stay the channel's one writer until the M1 move rewires them to this
  module in one window (C-FORMAT-SEQUENCE); after this cell the new module has **zero production callers**.
- **Test baselines at HEAD `5912b7d107`:** `lib/research/identity/tests` 55 passed. `lib/research/harvest/tests`
  does not exist yet at the cut; rk-81 adds 10 arms. `integrations/bloomberg/research/tests` is NOT a bar for this
  cell (at the cut: 4 failed, 35 passed, 2 collection errors, all pre-existing and untouched by this cell).

**RULED, what you build:**
1. **`lib/research/harvest/bloomberg.py`** (new). It imports `from lib.research.harvest import store` and calls only
   store's public names; it holds NO bucket or key literal and makes no S3 call of its own. boto3 is never imported
   at top level. Every function accepts `client=` and passes it to store.
   - `BRONZE_REQUESTS = ("refdata", "histdata", "histdata_daily_px", "bestdata", "identity", "exec_officers")`.
   - `RECEIVED_FORM = "bbg-client-json"` (CTO msg 24106 item 2).
   - `client_json(obj) -> bytes`: THE ONE deterministic serialisation of the dict the Terminal client hands a
     producer -- `json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")`, fixed
     (ensure_ascii=True makes the bytes pure ASCII, so UTF-8 and ASCII agree byte for byte). Two dicts equal as
     values produce IDENTICAL bytes whatever their key insertion order, so a repeated fetch of unchanged data is
     byte-identical and H0-store's `bronze_put` reads it as already present. The M1 move calls it on the client's
     dict and hands the bytes to `bronze_write`; `bronze_write` itself still takes `bytes` only and never
     re-serialises (`_as_received`).
   - `_as_received(body)`: returns `body` UNCHANGED after asserting it is `bytes`; a `str`, `dict` or anything else
     raises `TypeError` (the writer never re-serialises). It is the ONLY path a body takes to `store.bronze_put`,
     and AC3's first mutant rewrites it.
   - `bronze_fetched(request, security_key, client=None) -> list[str]`: `store.fetch_key_exists("bloomberg", request,
     store.entity_partition("security_key", security_key), client=client)`.
   - `bronze_write(request, security_key, fetched_at, body, client=None) -> dict`: refuses a request not in
     `BRONZE_REQUESTS` with `ValueError` (`pull_log` and `model_block_fye` are named in the message as STATE / RETIRED,
     plan `:179-180`, `:197`); otherwise `store.bronze_put("bloomberg", request, <entity_partition>,
     store.form_a_object(fetched_at, "json"), _as_received(body), content_type="application/json",
     metadata={"received-form": RECEIVED_FORM}, client=client)` -- the received form is recorded as S3 USER METADATA
     on the bronze object (the bytes stay exactly as received; a sidecar would break one-object-per-fetch and a
     wrapper would break the bytes). This REQUIRES `store.bronze_put` to accept a `metadata=` mapping merged into
     its fixed `{document-sha256, schema-version}` Metadata; the interface as drafted at the cut does NOT take one
     (`H0_STORE_INTERFACE.md` `:70-71`). AC0 checks the parameter at spawn and STOPs if it is absent -- this cell
     never edits `store.py`.
   - `model_block_rows(doc, bronze_key, fetched_at) -> list[dict]`: ONE row per figure. Each row carries:
     `security_key` (from `doc["security_key"]`, else the spaced `security` with spaces turned to `_`, the producer's
     own rule), `fiscal_year` (str or None), `mnemonic`, `scope`, `unit`, `sign`, `source`, `vintage`,
     `value_number` (float or None) and `value_text` (str or None) -- the mixed `value` split by ONE private pair
     `_split_value(v)` / `_join_value(number, text)` (AC3's second mutant rewrites `_join_value`) -- `basis_json`
     (canonical JSON of the figure's `basis`), `figure_json` (canonical JSON of the whole figure: the lossless carrier
     for optional keys such as `currency_caveat`, `estimate_basis`, `fiscal_period`, `override`, `period_end_date`),
     `doc_json` (canonical JSON of the document WITHOUT `figures`: `security`, `security_key`, `raw_stamp_used`,
     `fiscal_years`, `fiscal_year_row_count`, `orphan_price_rows`, `unresolved`, and any of `history_window`,
     `forecast_fallback`, `cases`), plus `bronze_key` and `fetched_at`. Canonical JSON = `json.dumps(x,
     sort_keys=True, separators=(",", ":"), ensure_ascii=True)`. A document with ZERO figures raises `ValueError`
     (it would vanish from silver; measured 0 of 122 live). A duplicate `(security_key, fiscal_year, mnemonic)`
     inside one document raises `ValueError` (measured 0).
   - `model_block_from_rows(rows) -> dict`: the inverse. Rebuilds the document from `doc_json` and the rows'
     `figure_json`, figures in their original order (carry a `figure_index` int column), and asserts every row's typed
     columns agree with its `figure_json` (`value_number`/`value_text` rejoin to `value` through `_join_value`).
     **`model_block_from_rows(model_block_rows(doc, ...)) == doc` for every document is the contract** (v0.17 `:906-907`).
   - `write_model_block_silver(doc, bronze_key, fetched_at, run_stamp, client=None) -> dict`:
     `store.silver_append("bloomberg", "model_block", model_block_rows(doc, bronze_key, fetched_at),
     record_key_fields=("security_key", "fiscal_year", "mnemonic"), run_stamp=run_stamp, client=client)`.
2. **`lib/research/harvest/tests/test_bloomberg.py`** (new). It loads the module under test from the environment
   variable `HARVEST_BLOOMBERG_UNDER_TEST` (a file path) if set, else from `lib.research.harvest.bloomberg`, so AC3 can
   run the same arms against mutants. It reuses the in-process stub S3 from `test_store.py` by import if that module
   exposes it, else defines its own with the same behaviour (`IfNoneMatch="*"` raises a botocore `ClientError`
   `PreconditionFailed`; the stub keeps each put's `Metadata`). Documents are SYNTHETIC, built in the test to mirror each measured variant above (4
   top-level key sets, 3 figure key sets, a str `value` and a float `value`, a None `fiscal_year`). EXACTLY these 9 arms:
   - `test_bronze_addresses_are_builder_output` -- the 6 requests, a security key with a slash, each receipt URI equal
     to `store.address_of("bloomberg", "bronze", request, "security_key=BP-SLASH-_LN_Equity", "<stamp>.json")`.
   - `test_bronze_bytes_as_received` -- the stub's stored body equals the input bytes exactly, including a body that
     is NOT canonical JSON (extra whitespace and key order preserved); a `dict` or `str` body raises `TypeError`.
   - `test_bronze_refuses_state_and_retired_requests` -- `pull_log` and `model_block_fye` raise `ValueError`.
   - `test_bronze_fetched_reports_prior_fetch` -- `bronze_fetched` is empty before a write and names the key after.
   - `test_client_json_deterministic_and_form_recorded` -- two dicts with the SAME content and DIFFERENT key
     insertion order (nested dicts included) give byte-identical `client_json` output; the bytes are ASCII with no
     space after `,` or `:`; a `bronze_write` of those bytes records `received-form` = `bbg-client-json` in the stub's
     stored Metadata; and a second `bronze_write` of the re-serialised reordered dict is reported already present
     (same key, same bytes), never a second object.
   - `test_model_block_rows_typed_and_keyed` -- `value_number` float or None, `value_text` str or None, never both
     set; record keys unique; every row carries the 3 lineage columns once `silver_append` computes `record_hash`.
   - `test_model_block_round_trip_every_variant` -- the round trip is `==` for each of the 4 top-level and 3 figure
     variants; a zero-figure document raises.
   - `test_model_block_silver_write_then_skip_unchanged` -- run 1 writes N rows; run 2 with the SAME document writes 0
     and skips N; run 3 with ONE figure's value changed writes 1.
   - `test_module_writes_only_through_store` -- the module's source holds no `put_object`, no `opal-data`, no
     `raw/bloomberg` and no `derived/model_block` literal (read with `io.open`).

**What this cell does NOT change:**
- It edits NO existing file. `model_block_pull.py`, `pull_baba_daily_px.py`, `derive_fye_fixed.py`,
  `bloomberg_fallback.py` and `add_security.py` are untouched; the old `raw/bloomberg/` and `derived/model_block/`
  keys keep their one writer and their readers until M1 (a later round, its own pair).
- It makes no Bloomberg call, no S3 write, no copy of any existing object and no reader switch.
- It does not move `pull_log` (STATE) or retire `model_block_fye`; both are named, not done.

## 2. WHERE THIS CAME FROM

- **Round 21**, decomposition s.29, cut by `2.0.0_SA_COO~Z`; cell "H1 bloomberg" of
  `HARVEST_CHAIN_DECOMP_PROPOSAL` s.3.
- The CTO's rulings: msg 24090 (round-21 shape), msg 24086 (the builder binds), and the v0.17 "lossless
  re-serialisation is a copy" ruling (the COO's call 2, ruled as recommended).
- Andrew-direct ~17:2xZ (backfill held for the bronze/silver shape), record @e70b949ba0; ~15:12Z (one slug per round).

## 3. SURFACES -- what you may read and write

<paths>
lib/research/harvest/bloomberg.py
lib/research/harvest/tests/test_bloomberg.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~83/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-83.bloomberg-harvest-writer.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** A READ needs no grant: `lib/research/harvest/store.py` and its
  tests, the five Bloomberg writers, the PRD, the plan. Scratch goes in `<your worktree>/.scratch/r83/` only and is
  never committed.
- **Collision check, done at the cut:** the other wave-2 cells write their own new modules under
  `lib/research/harvest/` (rk-84 `filings.py`, rk-85/rk-86 their own) and their own test files; none writes
  `bloomberg.py` or `test_bloomberg.py`. `store.py` and `test_store.py` are rk-81's and are READ-ONLY here. The only
  shared file is `INVESTIGATION_v1.md`; it is append-only, so do not isolate it.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~83 <0.9.0_WK_AMGT_RESAPP~83@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by the Write tool). Never push, merge, rebase, `checkout --`, `stash` or `clean`. Every `.py`
  passes `.tools/commit-gate.sh` inside safe-commit (py_compile, ds-precommit, ruff py39, and the naming limb).

## 4. BOUNDS

- **NO LIVE WRITE.** No S3 put, copy or delete; no Bloomberg call; no IAM; no Terraform. The ONLY live AWS use is
  AC4's read-only round trip over `derived/model_block/`.
- **AC0 IS A GATE.** If the real builder prints anything but `opal-data-harvest` for these addresses, or
  `lib/research/harvest/store.py` is absent or lacks a name you call, STOP, file a BLOCKING row (disarm_owner
  `2.0.0_SA_COO~Z`) and build nothing.
- **COLLECTION STAYS OFF.** **NO alarm, monitor, SNS/SES-send, notification or freshness checker.** No secret. No
  non-ASCII in anything you write. **PUSH: never** (LD-0522).
- **THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row -- never
  repaired, widened, or satisfied by a route this order did not name: never by editing `store.py`, an existing writer,
  `lib/opal_naming.py` or the registry, never by typing a bucket or key, never by a live write.
- **A COUNT BAR IS READ AT SPAWN AND PRINTS its denominator.** Re-measure the harvest and identity baselines before
  you edit.
- **SURPRISE ROWS:** `AMGT_RESAPP-Z-W83-S<k>`, `<k>` from 1; `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`. Append by
  textual splice inside the one fenced JSON array; never edit an existing row. A row's `disarm_owner` is never a
  worker serial; name the issuer, `2.0.0_SA_COO~Z`.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120 except AC4, which runs under timeout 900)

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-83"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import sys; sys.path.insert(0, "."); import lib.opal_naming as n; r = n.validate(); print("validate_refusals", len(r[0])); bad = [q for q in ("refdata", "histdata", "histdata_daily_px", "bestdata", "identity", "exec_officers") if not n.address("bloomberg", "harvest", "bronze", q, "security_key=CSL_AU_Equity", "20260921T120000Z.json").startswith("s3://opal-data-harvest/")]; print("bronze_not_harvest", bad); print("silver", n.address("bloomberg", "harvest", "silver", "model_block", "date=2026-09-21", "part-x.parquet")); from lib.research.harvest import store as s; need = ["bronze_put", "fetch_key_exists", "silver_append", "silver_latest", "record_hash", "address_of", "entity_partition", "form_a_object", "stamp", "date_partition", "LINEAGE_COLUMNS", "HarvestStoreError"]; print("store_names_missing", [x for x in need if not hasattr(s, x)]); import inspect; print("bronze_put_takes_metadata", "metadata" in inspect.signature(s.bronze_put).parameters)'</invocation><expect>validate_refusals 0; bronze_not_harvest []; silver s3://opal-data-harvest/bloomberg/harvest/silver/model_block/date=2026-09-21/part-x.parquet; store_names_missing []; bronze_put_takes_metadata True -- measured so at the cut (HEAD 5912b7d107) for the builder half; the store half reads [] and True only once rk-81 has drained WITH a metadata= parameter (CTO msg 24106 item 2 needs it to record received_form). Any other output: STOP, BLOCKING row, build nothing</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-83"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/harvest/tests/test_bloomberg.py -v -p no:cacheprovider 2>&1 | tail -14</invocation><expect>"9 passed" and 0 failed, the PASSED lines naming exactly test_bronze_addresses_are_builder_output, test_bronze_bytes_as_received, test_bronze_refuses_state_and_retired_requests, test_bronze_fetched_reports_prior_fetch, test_client_json_deterministic_and_form_recorded, test_model_block_rows_typed_and_keyed, test_model_block_round_trip_every_variant, test_model_block_silver_write_then_skip_unchanged, test_module_writes_only_through_store</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-83"><invocation>cd "$(git rev-parse --show-toplevel)" && AWS_PROFILE=rk83-no-such-profile AWS_ACCESS_KEY_ID=invalid AWS_SECRET_ACCESS_KEY=invalid AWS_SESSION_TOKEN=invalid python -m pytest lib/research/harvest/tests lib/research/identity/tests -q -p no:cacheprovider 2>&1 | tail -2</invocation><expect>one final line "N passed" with 0 failed, N = the harvest and identity baselines re-measured at spawn + 9 (10 + 55 + 9 = 74 if rk-81 landed its 10 arms and identity is unmoved), with the AWS credentials pointed at an invalid profile -- so no arm makes a live call and the new module breaks nothing it imports</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-83"><invocation>cd "$(git rev-parse --show-toplevel)" && mkdir -p .scratch/r83 && python -c 'import io, re, subprocess, os, sys; src = io.open("lib/research/harvest/bloomberg.py", encoding="utf-8").read(); print("as_received_defs", len(re.findall(r"^def _as_received\(", src, re.M)), "join_value_defs", len(re.findall(r"^def _join_value\(", src, re.M))); m1 = src + "\n\ndef _as_received(body):\n    import json as _j\n    return _j.dumps(_j.loads(body), sort_keys=True).encode()\n"; m2 = src + "\n\ndef _join_value(number, text):\n    return number\n"; io.open(".scratch/r83/m1.py", "w", encoding="utf-8", newline="\n").write(m1); io.open(".scratch/r83/m2.py", "w", encoding="utf-8", newline="\n").write(m2)
for tag, arm in (("m1", "test_bronze_bytes_as_received"), ("m2", "test_model_block_round_trip_every_variant")):
    env = dict(os.environ, HARVEST_BLOOMBERG_UNDER_TEST=os.path.abspath(".scratch/r83/%s.py" % tag)); r = subprocess.run([sys.executable, "-m", "pytest", "lib/research/harvest/tests/test_bloomberg.py", "-q", "-p", "no:cacheprovider", "-k", arm], capture_output=True, text=True, env=env); print(tag, arm, "rc", r.returncode, (r.stdout.strip().splitlines() or [""])[-1])'</invocation><expect>as_received_defs 1 join_value_defs 1; then "m1 test_bronze_bytes_as_received rc 1 ... 1 failed" and "m2 test_model_block_round_trip_every_variant rc 1 ... 1 failed" -- each arm FAILS against its mutant (a body re-serialised instead of stored as received; the str half of a mixed value dropped on the way back), so the arms that pass in AC1 discriminate the two contract behaviours rather than pass vacuously. A mutant arm that PASSES fails this criterion</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-83"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import sys, json, collections; sys.path.insert(0, "."); import boto3; from lib.research.harvest import bloomberg as hb; s3 = boto3.client("s3", region_name="us-east-1"); b = "opal-data-harvest"; objs = [o for p in s3.get_paginator("list_objects_v2").paginate(Bucket=b, Prefix="derived/model_block/") for o in p.get("Contents", [])]; eq = 0; diff = []; rows = 0; dup = 0
for o in objs:
    doc = json.loads(s3.get_object(Bucket=b, Key=o["Key"])["Body"].read()); rr = hb.model_block_rows(doc, "copy-of:" + o["Key"], "2026-09-21T00:00:00+00:00"); rows += len(rr); c = collections.Counter((r["security_key"], r["fiscal_year"], r["mnemonic"]) for r in rr); dup += sum(1 for v in c.values() if v > 1)
    if hb.model_block_from_rows(rr) == doc: eq += 1
    else: diff.append(o["Key"])
print("objects", len(objs), "rt_equal", eq, "rt_diff", len(diff), diff[:3]); print("rows", rows, "record_key_dups", dup); print("mixed_value_columns_ok", all(isinstance(r["value_number"], (float, type(None))) and isinstance(r["value_text"], (str, type(None))) for r in hb.model_block_rows(doc, "x", "2026-09-21T00:00:00+00:00")))'</invocation><expect>objects 122 rt_equal 122 rt_diff 0 [] (the live count at the cut; if model blocks have landed since, objects is the new count and rt_equal must EQUAL it); rows 23998 at the cut (the live figure count, re-read) with record_key_dups 0; mixed_value_columns_ok True -- READ-ONLY (list_objects_v2 + get_object only, no put, copy or delete): every live derived/model_block object round-trips losslessly through the new silver rows, which is the per-object grading v0.17 :906-907 names for the move this module will serve</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-83"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import subprocess; out = subprocess.run(["git", "grep", "-l", "-E", "harvest[.]bloomberg|harvest import bloomberg", "--", "*.py"], capture_output=True, text=True).stdout.split(); prod = [f for f in out if not f.startswith("lib/research/harvest/")]; print("production_importers", prod); w = ["integrations/bloomberg/research/model_block_pull.py", "integrations/bloomberg/research/pull_baba_daily_px.py", "integrations/bloomberg/research/derive_fye_fixed.py", "lib/research/management/bloomberg_fallback.py", "lib/research/identity/add_security.py"]; log = subprocess.run(["git", "log", "--format=%h %an", "5912b7d107..HEAD", "--"] + w, capture_output=True, text=True).stdout.split("\n"); mine = [l for l in log if "0.9.0_WK_AMGT_RESAPP~83" in l]; print("existing_writers_touched_by_this_worker", len(mine))'</invocation><expect>production_importers [] and existing_writers_touched_by_this_worker 0 -- the new module has zero production callers and none of the channel's 5 current writers changed on this branch (the diff base 5912b7d107 is the cut's pinned HEAD, never HEAD or a merge-base, per row Z-S193): the channel keeps ONE writer (C-DEDUPE-BY-KEY) until the M1 move rewires it in one window</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rk-83"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import io; [print(f, "compiles", bool(compile(io.open(f, "rb").read().decode("utf-8"), f, "exec")), "crlf", io.open(f, "rb").read().count(b"\r\n"), "non_ascii_bytes", len(io.open(f, "rb").read()) - len(io.open(f, "rb").read().decode("utf-8"))) for f in ("lib/research/harvest/bloomberg.py", "lib/research/harvest/tests/test_bloomberg.py")]'</invocation><expect>both files print compiles True, crlf 0 and non_ascii_bytes 0 (the files are new; the base figure is absent by construction)</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this
order.

## 6. WHEN YOU ARE DONE

1. Write your instance to
   `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~83/AMGT_RESAPP.TO-AMGT-rk-83.bloomberg-harvest-writer.proof_of_spec.json`
   per `org/standards/PROOF_OF_SPEC.schema.json`.
2. Grade it with YOUR WORKTREE'S OWN `python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4,AC5,AC6`;
   rc 0 is the verdict.
3. Flip the order's status tag to `complete`, then commit with `--only -- <paths>`.
4. Report once, naming: the suite counts before and after; AC3's two mutant outcomes; AC4's round-trip counts.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/r83/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**Issuer notes:**
- No never-widen pair: no live write. AC4 is a read-only S3 read under the seat's credentials.
- Spawn ONLY after rk-81 (H0-store) drains: AC0 reads `store.py` names. Disjoint from rk-82 (terraform) and the other
  wave-2 cells (their own new modules).
- RULED (CTO msg 24106 item 2): the client's deterministic JSON IS Bloomberg's as-received form, recorded as
  `received_form: "bbg-client-json"`; this order builds `client_json` and the metadata record.
- OPEN FOR THE ISSUER, BLOCKING THIS CELL'S AC0: rk-81's `store.bronze_put` as drafted has NO `metadata=` parameter
  (its Metadata is fixed to `{document-sha256, schema-version}`). REC: amend rk-81 BEFORE issuance to accept an
  optional `metadata: dict | None` merged into the fixed Metadata (reserved keys refused), with one test arm. Without
  it, rk-83's AC0 STOPs by design. Alternative: record received_form in a silver lineage column instead -- but the
  ruling says the BRONZE object records it.
- `pull_log` to STATE and `model_block_fye` retirement are named here and done by M1.

<status>pending</status>
<round>21</round>
<slot>~83</slot>
<fabric>site-z</fabric>
