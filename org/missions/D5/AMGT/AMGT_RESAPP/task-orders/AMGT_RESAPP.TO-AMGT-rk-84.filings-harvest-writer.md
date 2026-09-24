# AMGT_RESAPP task order -- `AMGT-rk-84` -- H2-filings: the filings channel's harvest writer (SEC/EDGAR + issuer-site + ESEF), built on H0-store and NOT yet wired in -- the fetched document's bytes as bronze (form b, fetch key = accession / document id), the SEC ticker table as a request (form c), and the `.source.json` records as LOSSLESS silver `filing_source` rows, proven offline and by a read-only round trip over every live `filings/v1` source object

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-84</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~84</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order adds one new library module and its tests; it arms no cron,
  alarm, monitor or cadence, reads no schedule and writes none (scope checked: the whole write surface is
  lib/research/harvest/filings.py, lib/research/harvest/tests/test_filings.py, its deliverables, the channel and this
  order). No filing is fetched; the filings battery and batch keep running unchanged.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant is read or changed. The one AWS use is AC4's READ-ONLY
  round trip (list_objects_v2 + get_object over filings/v1/ in opal-data-harvest, `.source.json` only) under the
  seat's existing credentials, the same read the issuer ran at the cut; no put, copy or delete anywhere. The served
  roles' read grants on the new prefixes are AMGT-rk-82's (and M2's for the filing homes rk-82 leaves out).
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~84`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that
`org/`, `.tools/`, `lib/opal_naming.py`, `lib/research/filings/fetch.py` and `lib/research/harvest/store.py` exist; if
any is absent, STOP with a BLOCKING row. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~84;`.
**NEVER RUN AN INSTALL.** Never read, show, diff or check out branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50` -- it
holds an exposed credential.

## 1. THE CELL, inlined in full -- `AMGT-rk-84` (H2-filings, round 21 wave 2)

**The acceptance of record (`1.0.0_SA_CTO~Z`, msg 24090, 2026-09-21T21:25:25Z), verbatim:** *"ROUND 21
(2.0.0_SA_COO~Z): waves 1 + 2 (H0-store, H0-iam, H1-H6) = 8 cells is ACCEPTED. It is cut at round 20's L10
(LD-0521), and only when (i) both v0.17 halves are signed (LIMB 6), (ii) Z-S203 has disarmed so the builder prints
harvest, and (iii) rk-79 has drained, for H4/H5."* PRD v0.17 is ADMITTED @`1f7459456a`; the CTO's admission note
(msg 24098) adds: *"The cut must read the v0.17 filings split: .source.json to silver, .analysis.json to gold (after
the backfill)."*

**The contracts, `prd/AMGT_RESAPP_PRD.md` v0.17 @`1f7459456a`, verbatim:**
- `:866` C-BRONZE-AS-RECEIVED: *"Bronze is the response bytes exactly as received -- no parsing, trimming or
  re-serialising -- one object per fetch, never overwritten ... (b) an immutable document:
  `{vendor}/harvest/bronze/{request}/{entity}={id}/{document id}/{vendor file name}`; (c) a request:
  `{vendor}/harvest/bronze/{request}/date=YYYY-MM-DD/{request hash or file}.{ext}`."*
- `:873` C-SILVER-PARQUET: *"Silver is parquet with every vendor field kept and typed, partitioned `date=` by fetch
  date, one part file per run. Every row carries `bronze_key`, `fetched_at` and `record_hash` ..."*
- `:885` C-DEDUPE-BY-KEY: *"... Before any vendor call, the writer checks the bucket for the fetch key. Exactly one
  writer holds a channel's fetch keys at a time ..."*
- `:892` C-SLASH-SAFE-KEY: *"... An entity id sits in a partition, never in the builder's free-form `object`
  argument."*
- `:906-907`: *"A lossless re-serialisation is a copy. An existing JSON object re-written as parquet silver, with
  every field kept, counts as a copy under this contract, not a re-derivation. Each object is graded by a round-trip
  equality check."*
- `:908-911`: *"Derived records split by what they are. The `filings/v1` `.source.json` objects (the filing's own
  sections, cut from a document the pipeline never stored) move to SILVER. The `.analysis.json` objects (the model's
  reading) are what Opal cares about, so they are GOLD under R10 and follow the gold chain after the backfill. The
  document's bronze is filled only by the backfill's first fetch of it."*

**The plan it builds** (`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/PLAN_AMGT_HARVEST_CHANNEL_FORMATS_20260921.md`
@`1a9f1c4469`, s.5.2 `:200-232` and s.5.3 `:234-260`): the filing as fetched under `sec/.../bronze/filing/cik=<cik>/<accession>/<vendor file>`;
the ticker table under `sec/.../bronze/company_tickers/date=.../...`; issuer documents under
`issuer-site/.../bronze/document/security_key=<key>/<16-hex doc id>/<file>`; ESEF packages under
`filings-xbrl/.../bronze/filing/lei=<lei>/<package>`. Fetch key = the accession (SEC, immutable) or the document id
(non-EDGAR). Silver uses the SAME columns across the filing sources so one gold reader unions them (`:249-250`).

**THE MEASURED STATE (issuer, HEAD `5912b7d107`; RE-READ every line at your branch HEAD before editing):**
- **Builder, live registry** (validate 0 refusals): `sec/bronze/filing` `cik=0000012927`
  `000001823026000008/cat-20251231.htm` = `s3://opal-data-harvest/sec/harvest/bronze/filing/cik=0000012927/000001823026000008/cat-20251231.htm`;
  `sec/bronze/company_tickers` `date=2026-09-21` `sec_ticker_cik_cache.json` =
  `s3://opal-data-harvest/sec/harvest/bronze/company_tickers/date=2026-09-21/sec_ticker_cik_cache.json`;
  `issuer-site/bronze/document` `security_key=6861_JP_Equity` `1defdb68a7ffd3b7/AnnualSecuritiesReport_202606_ja.pdf` =
  `s3://opal-data-harvest/issuer-site/harvest/bronze/document/security_key=6861_JP_Equity/1defdb68a7ffd3b7/AnnualSecuritiesReport_202606_ja.pdf`;
  `filings-xbrl/bronze/filing` `lei=529900T8BM49AURSDO55` = `s3://opal-data-harvest/filings-xbrl/harvest/bronze/filing/lei=529900T8BM49AURSDO55/...`;
  silver `sec/silver/filing_source` and `issuer-site/silver/filing_source` both print `s3://opal-data-harvest/...`.
- **H0-store** (`AMGT-rk-81`) provides `lib/research/harvest/store.py`, public interface fixed (23 names). This cell
  CALLS `bronze_put`, `fetch_key_exists`, `silver_append`, `silver_latest`, `record_hash`, `address_of`,
  `entity_partition`, `form_b_object`, `form_c_object`, `date_partition`, `stamp`, `LINEAGE_COLUMNS`,
  `HarvestStoreError` and subclasses -- and never writes S3 itself.
- **The live source objects** (read-only, 2026-09-21 ~21:5xZ): `filings/v1/` holds **206 objects**: **194
  `.source.json`** (2,808,590 bytes) + **12 `.analysis.json`** (GOLD, out of this cell). The 194 split:
  - **14 RESOLVED:** 12 `filing_identity.source edgar` (17 keys, e.g. `ASML_NA_Equity/000162828026011378`;
    `filing_identity {cik, form_expected, source}`), 1 battery `edgar-ticker` (`CAT_US_Equity/000001823026000008`, 24
    keys), 1 battery `company-site` (`6861_JP_Equity/doc-1defdb68a7ffd3b7`, 24 keys, 965,303 bytes, the largest).
  - **180 UNRESOLVED-SOURCE:** 178 `filing_identity.source none` (12 keys, an OLDER shape than today's
    `fetch.unresolved_source_object`, which emits 18) + 2 `source battery` (18 keys).
  - 4 distinct top-level key sets in all. Values nest dicts (`excerpt`, `officer_section`, `filing_identity`,
    `battery`, `entity_evidence`); `document_bytes` / `document_text_chars` are int; many fields are None.
- **The current writers of this channel's keys** -- census by SUBTRACTION over every non-test S3 write call site in
  `integrations/bloomberg/research`, `lib/research/management`, `lib/research/filings`, `lib/research/identity`
  (native Grep `put_object\(|write_pool\(`): **19 call sites**. Minus 5 Bloomberg bronze/silver writers
  (`model_block_pull.py:336`, `pull_baba_daily_px.py:64`, `derive_fye_fixed.py:84`, `bloomberg_fallback.py:100`,
  `add_security.py:122`), minus 3 `.analysis.json` GOLD writers (`analyze.py:1388,1496,1546`), minus 7 other pool
  writers (`pull_consumer.py:67`, `enrich.py:794`, `enrich.py:870`, `crosswalk.py:929`, `crosswalk.py:988`,
  `build_universe.py:918`, `add_security.py:159`) = **4 `.source.json` writers**: `fetch.py:426` (`persist`),
  `batch.py:341`, `batch.py:553`, `battery.py:1314`, all through `crosswalk.write_pool`. **No writer of the filing
  DOCUMENT bytes exists** (the document is fetched, cut and discarded; plan `:202-205`). **No writer of the SEC ticker
  table exists**, while ONE reader of it already reads the new grammar: `lib/research/identity/build_universe.py:456-462`
  (`sec_table_address`, object `sec_ticker_cik_cache.json`), and `battery.py:563` fetches
  `https://www.sec.gov/files/company_tickers.json` per run. **None of these files is changed by this cell**; after it,
  the new module has **zero production callers** until the M2 move and the B2 backfill wire it.
- **Test baselines at HEAD `5912b7d107`:** `lib/research/filings/tests` 79 passed; `lib/research/identity/tests` 55
  passed. `lib/research/harvest/tests` does not exist at the cut; rk-81 adds 10 arms.

**RULED, what you build:**
1. **`lib/research/harvest/filings.py`** (new). It imports `from lib.research.harvest import store` and calls only
   store's public names; it holds NO bucket or key literal and makes no S3 call of its own. It MAY import
   `lib.research.filings.fetch` for READ-ONLY constants, never to call a fetch. boto3 is never imported at top level.
   Every function accepts `client=`.
   - `_as_received(body)`: returns `body` UNCHANGED after asserting `bytes`; anything else raises `TypeError`. The ONLY
     path a body takes to `store.bronze_put`; AC3's first mutant rewrites it.
   - `cik_partition(cik) -> str`: `"cik=" + str(int(cik)).zfill(10)` (an int, a numeric str or a zero-padded str all
     give the same 10 digits); a non-numeric cik raises `ValueError`.
   - **Bronze, fetch-key checks first (C-DEDUPE-BY-KEY):**
     - `sec_filing_fetched(cik, accession, client=None) -> list[str]` = `store.fetch_key_exists("sec", "filing",
       cik_partition(cik), object_prefix=accession + "/", client=client)`.
     - `bronze_sec_filing(cik, accession, vendor_file_name, body, content_type="text/html", client=None)` =
       `store.bronze_put("sec", "filing", cik_partition(cik), store.form_b_object(accession, vendor_file_name),
       _as_received(body), content_type=content_type, client=client)`.
     - `issuer_document_fetched(security_key, document_id, client=None)` and `bronze_issuer_document(security_key,
       document_id, vendor_file_name, body, content_type="application/pdf", client=None)` -- source `issuer-site`,
       request `document`, partition `store.entity_partition("security_key", security_key)`, form (b).
     - `esef_filing_fetched(lei, document_id, client=None)` and `bronze_esef_filing(lei, document_id,
       vendor_file_name, body, content_type="application/zip", client=None)` -- source `filings-xbrl`, request
       `filing`, partition `store.entity_partition("lei", lei)`, form (b).
     - `bronze_sec_company_tickers(fetched_at, body, object_name, client=None)` -- source `sec`, request
       `company_tickers`, partition `store.date_partition(fetched_at)`, object `store.form_c_object(object_name)`.
       `object_name` is REQUIRED (no default): the reader measured above reads `sec_ticker_cik_cache.json`, the SEC
       serves `company_tickers.json`, and which name bronze keeps is an open call for the CTO (RECORD FACE); the
       module does not decide it.
   - **Silver, the `.source.json` copy (v0.17 `:906-911`):**
     - `vendor_source(obj) -> str`: a RESOLVED object maps by its route -- `filing_identity.source == "edgar"` gives
       `sec`; battery route `edgar-ticker` or `edgar-bloomberg-cik` gives `sec`; `company-site` gives `issuer-site`;
       `esef-lei` gives `filings-xbrl`. Any other route (e.g. `national-regulator`) raises `NoVendorSourceError`
       naming it. An `UNRESOLVED-SOURCE` object raises `NoVendorSourceError` too: it has no vendor, and where the 180
       markers go (silver under which source, or STATE `amgt/harvest/state/filing_attempt/`) is an open call for the
       CTO (RECORD FACE). `NoVendorSourceError` subclasses `store.HarvestStoreError`.
     - `filing_source_row(obj, bronze_key, fetched_at) -> dict`: ONE row per source object. Typed scalar columns for
       every top-level scalar the live objects carry (`security_key`, `status`, `accession`, `accession_raw`, `form`,
       `family`, `language`, `entity_name`, `filing_date`, `period_end`, `url`, `primary_document`, `retrieved_at`,
       `parser_version`, `document_bytes` int, `document_sha256`, `document_text_chars` int, `verified_site_reason`,
       `reason`), each None when absent; `object_keys` (the sorted list of the object's top-level keys, as a JSON
       string -- the absent-vs-null carrier); and `object_json` (canonical JSON of the WHOLE object: `json.dumps(obj,
       sort_keys=True, separators=(",", ":"), ensure_ascii=True)`), plus `bronze_key` and `fetched_at`. Nested dicts
       are carried inside `object_json`, never as mixed columns.
     - `source_object_from_row(row) -> dict`: the inverse, from `object_json`; it asserts every typed column equals
       the rebuilt object's value (or is None where the key is absent) and that `object_keys` matches.
       **`source_object_from_row(filing_source_row(obj, ...)) == obj` for every RESOLVED object is the contract.**
     - `write_filing_source_silver(objs, bronze_keys, fetched_at, run_stamp, client=None) -> dict`: groups the objects
       by `vendor_source`, then per source `store.silver_append(source, "filing_source", rows,
       record_key_fields=("security_key", "accession"), run_stamp=run_stamp, client=client)`. Returns
       `{source: receipt}`. Any object raising in `vendor_source` refuses the WHOLE call before any write.
2. **`lib/research/harvest/tests/test_filings.py`** (new). It loads the module under test from
   `HARVEST_FILINGS_UNDER_TEST` (a file path) if set, else from `lib.research.harvest.filings`. It reuses the stub S3
   from `test_store.py` by import if exposed, else defines its own with the same behaviour. Source objects are
   SYNTHETIC, built in the test: one EDGAR-shaped RESOLVED object with the 17-key set above, one battery
   `edgar-ticker` and one `company-site` object via `fetch.build_battery_source_object`, one UNRESOLVED via
   `fetch.unresolved_source_object`, and one UNRESOLVED with the OLDER 12-key set. EXACTLY these 8 arms:
   - `test_sec_filing_bronze_is_form_b_under_cik` -- `cik_partition(12927)`, `("12927")` and `("0000012927")` all give
     `cik=0000012927`; the receipt URI equals `store.address_of("sec", "bronze", "filing", "cik=0000012927",
     "000001823026000008/cat-20251231.htm")`.
   - `test_issuer_esef_and_ticker_addresses_are_builder_output` -- the issuer, ESEF and company_tickers receipts equal
     `store.address_of(...)` for the measured shapes; `bronze_sec_company_tickers` without `object_name` is a
     `TypeError`.
   - `test_bronze_bytes_as_received` -- the stub's stored body equals the input bytes exactly (an HTML body with CRLF
     and a PDF-like binary body); a `str` or `dict` body raises `TypeError`.
   - `test_fetched_by_accession_and_document_id` -- each `*_fetched` is empty before its write and names the key after;
     a different accession under the same cik stays empty.
   - `test_vendor_source_routes` -- edgar, `edgar-ticker`, `edgar-bloomberg-cik` give `sec`; `company-site` gives
     `issuer-site`; `esef-lei` gives `filings-xbrl`; `national-regulator` and both UNRESOLVED shapes raise
     `NoVendorSourceError`.
   - `test_filing_source_round_trip_every_resolved_shape` -- `==` for the 3 RESOLVED synthetic shapes, and the typed
     columns agree with the object.
   - `test_filing_source_silver_write_then_skip_unchanged` -- run 1 writes one row per object under its vendor; run 2
     with the same objects writes 0 and skips all; a batch containing one UNRESOLVED object writes NOTHING and raises.
   - `test_module_writes_only_through_store` -- the module's source holds no `put_object`, no `write_pool`, no
     `opal-data` and no `filings/v1` literal (read with `io.open`).

**What this cell does NOT change:**
- It edits NO existing file. `fetch.py`, `batch.py`, `battery.py`, `analyze.py`, `build_universe.py`, `roster.py` and
  `scoped_amgt.py` are untouched; `filings/v1/` keeps its one writer and its readers until M2 (a later round, its own
  pair).
- It makes no fetch (SEC, issuer site, ESEF), no S3 write, no copy of any existing object, and no reader switch.
- It does not touch the 12 `.analysis.json` objects (GOLD, the gold chain after the backfill) or decide where the 180
  UNRESOLVED markers go (an open call).

## 2. WHERE THIS CAME FROM

- **Round 21**, decomposition s.29, cut by `2.0.0_SA_COO~Z`; cell "H2 filings" of `HARVEST_CHAIN_DECOMP_PROPOSAL`
  s.3 (5.2 + 5.3 merged: one writer family, one fetch keyspace, C-DEDUPE `:885-890`).
- The CTO's rulings: msg 24090 (round-21 shape), msg 24098 (the v0.17 filings split), and the v0.17 rulings on the
  COO's calls 2 and 3 (lossless re-serialisation; `.source.json` to silver, filing bronze from the first fetch).
- Andrew-direct ~17:2xZ (backfill held for the bronze/silver shape), record @e70b949ba0; ~15:12Z (one slug per round).

## 3. SURFACES -- what you may read and write

<paths>
lib/research/harvest/filings.py
lib/research/harvest/tests/test_filings.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~84/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-84.filings-harvest-writer.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** A READ needs no grant: `store.py` and its tests, `fetch.py`,
  `battery.py`, `batch.py`, `build_universe.py`, the PRD, the plan. Scratch goes in `<your worktree>/.scratch/r84/`
  only and is never committed.
- **Collision check, done at the cut:** the other wave-2 cells write their own new modules under
  `lib/research/harvest/` (rk-83 `bloomberg.py`, rk-85/rk-86 their own) and their own test files; none writes
  `filings.py` or `test_filings.py`. `store.py` and `test_store.py` are rk-81's and are READ-ONLY here. Round-20 rk-79
  writes `lib/research/management/*`, which this cell only reads. The only shared file is `INVESTIGATION_v1.md`; it is
  append-only, so do not isolate it.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~84 <0.9.0_WK_AMGT_RESAPP~84@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by the Write tool). Never push, merge, rebase, `checkout --`, `stash` or `clean`. Every `.py`
  passes `.tools/commit-gate.sh` inside safe-commit (py_compile, ds-precommit, ruff py39, and the naming limb).

## 4. BOUNDS

- **NO LIVE WRITE, NO FETCH.** No S3 put, copy or delete; no call to the SEC, an issuer site or an ESEF host; no IAM;
  no Terraform. The ONLY live AWS use is AC4's read-only round trip over `filings/v1/*.source.json`.
- **AC0 IS A GATE.** If the real builder prints anything but `opal-data-harvest` for these addresses, or
  `lib/research/harvest/store.py` is absent or lacks a name you call, STOP, file a BLOCKING row (disarm_owner
  `2.0.0_SA_COO~Z`) and build nothing.
- **COLLECTION STAYS OFF.** **NO alarm, monitor, SNS/SES-send, notification or freshness checker.** No secret. No
  non-ASCII in anything you write. **PUSH: never** (LD-0522).
- **THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row -- never
  repaired, widened, or satisfied by a route this order did not name: never by editing `store.py`, an existing writer,
  `lib/opal_naming.py` or the registry, never by typing a bucket or key, never by a fetch or a live write.
- **A COUNT BAR IS READ AT SPAWN AND PRINTS its denominator.** Re-measure the harvest, filings and identity baselines
  before you edit.
- **SURPRISE ROWS:** `AMGT_RESAPP-Z-W84-S<k>`, `<k>` from 1; `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`. Append by
  textual splice inside the one fenced JSON array; never edit an existing row. A row's `disarm_owner` is never a
  worker serial; name the issuer, `2.0.0_SA_COO~Z`.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120 except AC4, which runs under timeout 900)

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-84"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import sys; sys.path.insert(0, "."); import lib.opal_naming as n; r = n.validate(); print("validate_refusals", len(r[0])); calls = [("sec", "bronze", "filing", "cik=0000012927", "000001823026000008/cat-20251231.htm"), ("sec", "bronze", "company_tickers", "date=2026-09-21", "sec_ticker_cik_cache.json"), ("issuer-site", "bronze", "document", "security_key=6861_JP_Equity", "1defdb68a7ffd3b7/AnnualSecuritiesReport_202606_ja.pdf"), ("filings-xbrl", "bronze", "filing", "lei=529900T8BM49AURSDO55", "p.zip"), ("sec", "silver", "filing_source", "date=2026-09-21", "part-x.parquet"), ("issuer-site", "silver", "filing_source", "date=2026-09-21", "part-x.parquet"), ("filings-xbrl", "silver", "filing_source", "date=2026-09-21", "part-x.parquet")]; print("not_harvest", [c[:3] for c in calls if not n.address(c[0], "harvest", c[1], c[2], c[3], c[4]).startswith("s3://opal-data-harvest/")]); from lib.research.harvest import store as s; need = ["bronze_put", "fetch_key_exists", "silver_append", "silver_latest", "record_hash", "address_of", "entity_partition", "form_b_object", "form_c_object", "date_partition", "stamp", "LINEAGE_COLUMNS", "HarvestStoreError"]; print("store_names_missing", [x for x in need if not hasattr(s, x)])'</invocation><expect>validate_refusals 0; not_harvest []; store_names_missing [] -- the builder half measured so at the cut (HEAD 5912b7d107, 7 of 7 addresses print s3://opal-data-harvest/); the store half reads [] only once rk-81 has drained. Any other output: STOP, BLOCKING row, build nothing</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-84"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/harvest/tests/test_filings.py -v -p no:cacheprovider 2>&1 | tail -14</invocation><expect>"8 passed" and 0 failed, the PASSED lines naming exactly test_sec_filing_bronze_is_form_b_under_cik, test_issuer_esef_and_ticker_addresses_are_builder_output, test_bronze_bytes_as_received, test_fetched_by_accession_and_document_id, test_vendor_source_routes, test_filing_source_round_trip_every_resolved_shape, test_filing_source_silver_write_then_skip_unchanged, test_module_writes_only_through_store</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-84"><invocation>cd "$(git rev-parse --show-toplevel)" && AWS_PROFILE=rk84-no-such-profile AWS_ACCESS_KEY_ID=invalid AWS_SECRET_ACCESS_KEY=invalid AWS_SESSION_TOKEN=invalid python -m pytest lib/research/harvest/tests lib/research/filings/tests lib/research/identity/tests -q -p no:cacheprovider 2>&1 | tail -2</invocation><expect>one final line "N passed" with 0 failed, N = the harvest, filings and identity baselines re-measured at spawn + 8 (10 + 79 + 55 + 8 = 152 if rk-81 landed its 10 arms, the other two are unmoved, and no sibling wave-2 cell has drained into this branch), with the AWS credentials pointed at an invalid profile -- so no arm makes a live call, and the unchanged filings suite proves the existing writers were not touched</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-84"><invocation>cd "$(git rev-parse --show-toplevel)" && mkdir -p .scratch/r84 && python -c 'import io, re, subprocess, os, sys; src = io.open("lib/research/harvest/filings.py", encoding="utf-8").read(); print("as_received_defs", len(re.findall(r"^def _as_received\(", src, re.M)), "vendor_source_defs", len(re.findall(r"^def vendor_source\(", src, re.M))); m1 = src + "\n\ndef _as_received(body):\n    return body.replace(b\"\\r\\n\", b\"\\n\")\n"; m2 = src + "\n\ndef vendor_source(obj):\n    return \"sec\"\n"; io.open(".scratch/r84/m1.py", "w", encoding="utf-8", newline="\n").write(m1); io.open(".scratch/r84/m2.py", "w", encoding="utf-8", newline="\n").write(m2)
for tag, arm in (("m1", "test_bronze_bytes_as_received"), ("m2", "test_vendor_source_routes")):
    env = dict(os.environ, HARVEST_FILINGS_UNDER_TEST=os.path.abspath(".scratch/r84/%s.py" % tag)); r = subprocess.run([sys.executable, "-m", "pytest", "lib/research/harvest/tests/test_filings.py", "-q", "-p", "no:cacheprovider", "-k", arm], capture_output=True, text=True, env=env); print(tag, arm, "rc", r.returncode, (r.stdout.strip().splitlines() or [""])[-1])'</invocation><expect>as_received_defs 1 vendor_source_defs 1; then "m1 test_bronze_bytes_as_received rc 1 ... 1 failed" and "m2 test_vendor_source_routes rc 1 ... 1 failed" -- each arm FAILS against its mutant (a body normalised on the way to bronze; every object routed to sec, so the issuer, ESEF and UNRESOLVED cases are lost), so the arms that pass in AC1 discriminate rather than pass vacuously. A mutant arm that PASSES fails this criterion</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-84"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import sys, json, collections; sys.path.insert(0, "."); import boto3; from lib.research.harvest import filings as hf; s3 = boto3.client("s3", region_name="us-east-1"); b = "opal-data-harvest"; objs = [o for p in s3.get_paginator("list_objects_v2").paginate(Bucket=b, Prefix="filings/v1/") for o in p.get("Contents", []) if o["Key"].endswith(".source.json")]; eq = 0; diff = []; by_vendor = collections.Counter(); refused = collections.Counter()
for o in objs:
    obj = json.loads(s3.get_object(Bucket=b, Key=o["Key"])["Body"].read())
    try:
        v = hf.vendor_source(obj)
    except hf.NoVendorSourceError:
        refused[obj.get("status")] += 1; continue
    by_vendor[v] += 1; row = hf.filing_source_row(obj, "copy-of:" + o["Key"], "2026-09-21T00:00:00+00:00")
    if hf.source_object_from_row(row) == obj: eq += 1
    else: diff.append(o["Key"])
print("source_objects", len(objs), "by_vendor", dict(by_vendor), "refused", dict(refused)); print("rt_equal", eq, "rt_diff", len(diff), diff[:3])'</invocation><expect>source_objects 194 by_vendor {"sec": 13, "issuer-site": 1} refused {"UNRESOLVED-SOURCE": 180}; rt_equal 14 rt_diff 0 [] -- the live counts at the cut; if source objects have landed since, the four numbers move together and rt_equal must EQUAL the sum of by_vendor. READ-ONLY (list_objects_v2 + get_object only, no put, copy or delete; the 12 .analysis.json objects are not read): every live RESOLVED source object routes to its vendor and round-trips losslessly, which is the per-object grading v0.17 :906-907 names for the M2 move</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-84"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import subprocess; out = subprocess.run(["git", "grep", "-l", "-E", "harvest[.]filings|harvest import filings", "--", "*.py"], capture_output=True, text=True).stdout.split(); prod = [f for f in out if not f.startswith("lib/research/harvest/")]; print("production_importers", prod); w = ["lib/research/filings/fetch.py", "lib/research/filings/batch.py", "lib/research/filings/battery.py", "lib/research/filings/analyze.py", "lib/research/identity/build_universe.py"]; log = subprocess.run(["git", "log", "--format=%h %an", "5912b7d107..HEAD", "--"] + w, capture_output=True, text=True).stdout.split("\n"); mine = [l for l in log if "0.9.0_WK_AMGT_RESAPP~84" in l]; print("existing_writers_touched_by_this_worker", len(mine))'</invocation><expect>production_importers [] and existing_writers_touched_by_this_worker 0 -- the new module has zero production callers, and none of the channel's 4 current .source.json writers, the analysis writer or the ticker-cache reader changed on this branch (the diff base 5912b7d107 is the cut's pinned HEAD, never HEAD or a merge-base, per row Z-S193): the channel keeps ONE writer (C-DEDUPE-BY-KEY) until M2 rewires it in one window</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rk-84"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import io; [print(f, "compiles", bool(compile(io.open(f, "rb").read().decode("utf-8"), f, "exec")), "crlf", io.open(f, "rb").read().count(b"\r\n"), "non_ascii_bytes", len(io.open(f, "rb").read()) - len(io.open(f, "rb").read().decode("utf-8"))) for f in ("lib/research/harvest/filings.py", "lib/research/harvest/tests/test_filings.py")]'</invocation><expect>both files print compiles True, crlf 0 and non_ascii_bytes 0 (the files are new; the base figure is absent by construction; test bodies that need CRLF build it with an escape, never a literal carriage return in the file)</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this
order.

## 6. WHEN YOU ARE DONE

1. Write your instance to
   `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~84/AMGT_RESAPP.TO-AMGT-rk-84.filings-harvest-writer.proof_of_spec.json`
   per `org/standards/PROOF_OF_SPEC.schema.json`.
2. Grade it with YOUR WORKTREE'S OWN `python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4,AC5,AC6`;
   rc 0 is the verdict.
3. Flip the order's status tag to `complete`, then commit with `--only -- <paths>`.
4. Report once, naming: the suite counts before and after; AC3's two mutant outcomes; AC4's routing and round-trip
   counts.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/r84/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**Issuer notes:**
- No never-widen pair: no live write. AC4 is a read-only S3 read under the seat's credentials.
- Spawn ONLY after rk-81 (H0-store) drains: AC0 reads `store.py` names. Disjoint from rk-82 (terraform), rk-83
  (`bloomberg.py`) and the other wave-2 cells.
- Open for the CTO, not blocking this cell:
  1. **Where the 180 UNRESOLVED-SOURCE markers go.** v0.17 `:908-911` sends `.source.json` to silver, but an
     UNRESOLVED object has no vendor, so there is no `{source}` for its silver home. The proposal's route is STATE
     (`amgt/harvest/state/filing_attempt/`, plan `:216`). REC: STATE, one object per attempt; `vendor_source` refuses
     them here so nothing guesses.
  2. **The silver table name.** This order uses `filing_source` (one row per source object, lossless per `:906-907`).
     The plan names `filing_section` (row per accession x item, `:214`), which cannot be built losslessly from the
     stored excerpt (the items are concatenated). REC: `filing_source` now; `filing_section` rows are derived from
     the document bronze once B2 fills it.
  3. **The SEC ticker table's bronze object name.** The existing reader reads `sec_ticker_cik_cache.json`
     (`build_universe.py:453`); the SEC serves `company_tickers.json`. REC: keep the vendor file name in bronze
     (C-BRONZE-AS-RECEIVED) and switch the reader at M2; the function takes `object_name` explicitly so neither is
     baked in.

<status>complete</status>
<round>21</round>
<slot>~84</slot>
<fabric>site-z</fabric>
