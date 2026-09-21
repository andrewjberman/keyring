# AMGT_RESAPP task order -- `AMGT-rk-85` -- cell H3: the Seeking Alpha REST channel and the publications channel get ONE harvest-grammar writer through H0-store (bronze = the response as received, silver `article`/`symbol_profile`/`news_item`/`search_result` parquet, the bucket as the fetch-key authority); CODE ONLY, OFF BY DEFAULT, no live fetch, no S3 write, no reader switch, no release upload

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-85</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~85</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order edits library code and adds tests; it arms no cron, alarm,
  monitor or cadence, reads no schedule and writes none, and touches neither the desktop harvester's
  install-schedule.ps1 nor any Lambda or EventBridge rule (AC4 asserts no path under infra/ is in the diff).
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant is read or changed; every test runs against a stub S3
  client with the AWS credential variables pointed at a nonexistent profile (AC3), so the order makes no AWS call at
  all; the read grants for the new prefixes are AMGT-rk-82's, not this cell's.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~85`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that
`org/`, `.tools/` and the paths in section 3 exist; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~85;`. **NEVER RUN AN INSTALL.** Never read, show, diff or check out
branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50` -- it holds an exposed credential. Never read any worktree of
round 20's `AMGT-rk-79`.

## 1. THE CELL, inlined in full -- `AMGT-rk-85` (chain H, wave 2, cell H3; plan s.5.4 + s.5.5)

**The contracts (PRD v0.17 @`1f7459456a`, `prd/AMGT_RESAPP_PRD.md`), verbatim in the parts this cell serves:**
- `:866-871` C-BRONZE-AS-RECEIVED -- *"Bronze is the response bytes exactly as received -- no parsing, trimming or
  re-serialising -- one object per fetch, never overwritten, with the channel's FETCH key in the partition"*, forms
  (a) entity fetched repeatedly, (b) immutable document, (c) request.
- `:873-875` C-SILVER-PARQUET -- *"parquet with every vendor field kept and typed, partitioned `date=` by fetch date,
  one part file per run. Every row carries `bronze_key`, `fetched_at` and `record_hash`"*.
- `:885-890` C-DEDUPE-BY-KEY -- *"Before any vendor call, the writer checks the bucket for the fetch key. Exactly one
  writer holds a channel's fetch keys at a time ... The bucket is the authority for what has been fetched, never a
  file on one desktop."*
- `:892-893` C-SLASH-SAFE-KEY -- *"An entity id sits in a partition, never in the builder's free-form `object`
  argument."*
- `:895-902` C-FORMAT-SEQUENCE -- the source path's readers switch and it retires in the SAME window, in the MOVE cell,
  never as a rider. **So this cell builds the writer and leaves it OFF; the move (M3/M4) turns it on.**

**The plan (`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/PLAN_AMGT_HARVEST_CHANNEL_FORMATS_20260921.md` @`1a9f1c4469`):**
- s.5.4 `:268-275`: SA REST bronze `seeking-alpha/harvest/bronze/{symbol|report|analysis|news}/security_key=<key>/<stamp>.json`
  (form a); articles by article, `seeking-alpha/harvest/bronze/article/article_hash=<sha256>/<stamp>.json`; silver
  `symbol_profile`, `news_item`, `article`.
- s.5.5 `:297-314`: publications bronze `{barrons|wsj|ft|bloomberg|seeking-alpha}/harvest/bronze/article/article_hash=<h>/<stamp>.<ext>`
  (the publisher codes `bbg` -> `bloomberg`, `sa` -> `seeking-alpha`); silver `article` + `search_result` per
  publisher; fetch key `article_hash = sha256(<publisher code>:<article_id>)`, *"unchanged from today, so the 7 live
  objects keep their identity"*; the desktop SQLite *"becomes a cache of the bucket, never the authority"*.

**THE RULINGS OF RECORD ON THIS CELL (`1.0.0_SA_CTO~Z` msg 24106 (2026-09-21T21:53:32Z, answering msg 24105), `org/mcp/inbox/2.0.0_SA_COO/~Z/read/20260921T215332Z_1.0.0_SA_CTO_Z_Re_24105__round_21_s_5_spec_calls_RULED_.md`), verbatim:**
- item 1: *"1. SA hash prefix: keep \"sa:<id>\" for both channels, so one article is one key. The plan's \"seeking-alpha:\" is the typo, since it contradicts its own \"unchanged from today\"."*
- item 5: *"5. The six Lambda-packaged harvester files as WALLS, the grammar change in a new harvest_grammar.py, and a byte-compare of the six: ACCEPTED. So is your L5 widening of rk-85 by publishers.py and worker.py (unpackaged). CONDITION: rk-85's criteria must prove neither Lambda's artifact input changes. The byte-compare covers that, and it must be graded against the Lambdas' BUILD INPUT list, not a filename list (Rule 22a)."*
So ruling 1 and ruling 3 below are the CTO's as well as the issuer's, and ruling 5's widening is ACCEPTED. AC7 is
item 5's CONDITION: both Lambdas' build-input lists DERIVED from their build scripts, compared at the pin and at
your HEAD.

**ISSUER RULINGS for this cell (2.0.0_SA_COO~Z, L5):**
1. **ONE article_hash rule for BOTH channels:** `sha256(<publisher code> + ":" + article_id)` with the HARVESTER's
   publisher code (`sa`, `bbg`, `barrons`, `wsj`, `ft`). **Measured at the cut:** the live object
   `publications/v1/sa/5666ee64...a882.json` (article_key `sa:4635742`) equals `sha256("sa:4635742")` and NOT
   `sha256("seeking-alpha:4635742")`. Plan s.5.4 `:273-274` writes `"seeking-alpha:"`; that line disagrees with s.5.5's
   "unchanged from today" and is NOT followed -- the REST channel's SA article uses `"sa:" + article_id`, so an article
   reached by REST and by the browser lands at ONE `article_hash`. (Named for the CTO at issuance.)
2. **ONE writer function for the shared keyspace:** every article bronze write from EITHER channel goes through ONE
   function, `lib/opal_data_harvest/harvest_grammar.py` `put_article_bronze(...)`, which calls
   `store.fetch_key_exists` then `store.bronze_put`. `rest_fetch.py` imports it; nothing else writes an
   `article_hash=` partition (AC5 counts).
3. **The packaged-closure WALL:** `lib/opal_data_harvest/{__init__.py,catalog.py,storage.py,article.schema.json,
   security-article.schema.json}` are INSIDE BOTH AMGT Lambdas' closures (measured: the chatter-axis closure by
   `build_zip.closure()` = 15 members incl. `__init__.py`, `catalog.py`, `storage.py`; the scoped-api's 58 packaged
   paths in `AMGT-rk-74`'s AC3 include all five). **This cell does not touch any of the five** (AC4 byte-compares them
   to the pin), so it creates no carry-along for either Lambda. The plan's `catalog.py:69,74` key-form change is
   therefore built in the NEW module `harvest_grammar.py`, which no packaged module imports (AC4 re-runs the closure).
4. **OFF BY DEFAULT.** The legacy writers stay the running writers: `rest_fetch.land_raw` (`raw/seekingalpha/...`) and
   `uploads.Uploader` (`publications/v1/...`) are byte-identical in behaviour (AC5). The harvest grammar is reached ONLY
   by an explicit opt-in: `rest_fetch.py run-ticker ... --harvest-grammar`, and `worker.py`/`uploads.py` config key
   `"harvest_grammar": true` (default `false`, and `config.json` is NOT edited).
5. **Publications bronze needs the publisher's RESPONSE BYTES, which today are not carried** (`publishers.normalize`
   keeps only `response_sha256`, and for `sa`/`bbg` that hash is of `json.dumps(item)`, not bytes, `:213`, `:239`).
   This cell adds an OPTIONAL `raw_bytes`/`raw_ext` pair to the article the publisher methods yield (outside the
   schema-validated record -- `catalog.store` never sees it), which `worker.py` writes, ONLY in harvest mode, to a
   local `raw/` outbox file beside the record for the harvest uploader to put as bronze. A publisher method with no
   response object (a cached/`storage_reused` article) yields no raw bytes, and the uploader then writes silver only.
6. **The desktop RELEASE is not this cell's.** `build_release.py`'s `PACKAGE_FILES` gains `harvest_grammar.py` (code
   list only); running `build_release.py --upload` is a live S3 write and belongs to the move.

**WHAT YOU BUILD:**
- NEW `lib/opal_data_harvest/harvest_grammar.py`: `SOURCE_FOR_PUBLISHER = {"sa": "seeking-alpha", "bbg": "bloomberg",
  "barrons": "barrons", "wsj": "wsj", "ft": "ft"}`; `article_hash(publisher_code, article_id)`; `article_partition(...)`
  -> `store.entity_partition("article_hash", h)`; `put_article_bronze(publisher_code, article_id, body, ext,
  fetched_at, client=None)` (the ONE writer, ruling 2; returns the store receipt, or `{"skipped": True, "existing":
  [...]}` when `fetch_key_exists` is non-empty); `article_known(publisher_code, article_id, client=None)` (the
  bucket-authority check the worker calls BEFORE fetching a body); `article_silver_row(record, bronze_key)` and
  `search_result_row(...)` shaping rows from the EXISTING validated record (every field kept); `symbol_rows(...)` /
  `news_rows(...)` for the SA JSON:API envelopes (every `attributes` field kept, flattened one level).
- `integrations/seekingalpha/rest_fetch.py`: a `land_harvest(...)` beside `land_raw` -- symbol/report/analysis/news to
  form (a) under `seeking-alpha/<request>/security_key=<slash-safe key>`; articles through
  `harvest_grammar.put_article_bronze` with the fetch-key check BEFORE the article GET (skip when known); silver via
  `store.silver_append`. Selected only by `--harvest-grammar`.
- `lib/opal_data_harvest/uploads.py`: a NEW `HarvestUploader` class beside `Uploader` (which is untouched): for each
  pending outbox record, `put_article_bronze` for its raw file when present, then `store.silver_append` of the
  `article` row (record key `article_key`) and the security link as a `search_result`-shaped row is NOT written (the
  link is gold, plan `:307-308`).
- `lib/opal_data_harvest/publishers.py`: the optional `raw_bytes`/`raw_ext` on yielded articles (ruling 5).
- `lib/opal_data_harvest/worker.py`: in harvest mode only, `harvest_grammar.article_known` before a body fetch, and the
  raw outbox file write.
- `lib/opal_data_harvest/build_release.py`: `harvest_grammar.py` added to `PACKAGE_FILES`.
- Tests: NEW `integrations/seekingalpha/tests/test_rest_harvest.py` and NEW `lib/opal_data_harvest/test_harvest_grammar.py`,
  offline against a stub S3 (the store's `client=` parameter), with these arms (names must match AC1):
  `test_article_hash_matches_live_sa_object`, `test_one_writer_for_both_channels`,
  `test_fetch_key_known_skips_the_get`, `test_symbol_bronze_is_bytes_as_received`, `test_slash_key_is_a_partition`,
  `test_silver_article_row_keeps_every_field`, `test_harvest_mode_is_off_by_default`,
  `test_pinned_base_has_no_harvest_path` (the DISCRIMINATING arm: `git show` the pin's `rest_fetch.py` and
  `uploads.py` into a temp dir, import them under other names, and show neither has `land_harvest` / `HarvestUploader`
  -- pinned `dbfcfc0817bdd8694796165e3e4489d03973fb0a`, never HEAD or a merge-base, row Z-S193).

**THE FETCH-KEY WRITER CENSUS (by subtraction, measured at the cut @`dbfcfc0817`, native Grep of `.put_object(` and
`write_pool(` over `lib/research`, `lib/opal_data_harvest`, `integrations/bloomberg/research`,
`integrations/seekingalpha`, `infra/aws/terraform/harvest`, `infra/aws/lambda/research`, non-test):** 32 lines, minus 2
comment lines (`batch.py:539`, `run_scores.py:24`) = **30 call sites**. Minus the 28 that write no SA-REST or
publications key = **2 writers of this channel's keys today:** `integrations/seekingalpha/rest_fetch.py:215`
(`raw/seekingalpha/...`) and `lib/opal_data_harvest/uploads.py:76` (`publications/v1/...`,
`publication-links/v1/...`). `build_release.py:65` writes `lib/local-publications/...` (a code artifact, not channel
data) and is excluded by name. **After this cell the new writer exists but is wired into NO production path.**

## 2. WHERE THIS CAME FROM

**ROUND 21**, decomposition s.29 (cut by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s acceptance of the round-21 shape
(msg 24090) and PRD v0.17 ADMITTED @`1f7459456a` (msg 24098), from the chain-H proposal
`.scratch/r21_drafts/HARVEST_CHAIN_DECOMP_PROPOSAL.md` s.3 row H3. Andrew-direct ~17:2xZ holds the BACKFILL until the
pipes have their final shape; this cell builds shape, not backfill.

## 3. SURFACES -- what you may read and write

<paths>
integrations/seekingalpha/rest_fetch.py
integrations/seekingalpha/tests/test_rest_harvest.py
lib/opal_data_harvest/harvest_grammar.py
lib/opal_data_harvest/uploads.py
lib/opal_data_harvest/publishers.py
lib/opal_data_harvest/worker.py
lib/opal_data_harvest/build_release.py
lib/opal_data_harvest/test_harvest_grammar.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~85/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-85.sa-publications-writer.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL** -- above all `lib/opal_data_harvest/{__init__.py,catalog.py,
  storage.py,config.json,article.schema.json,security-article.schema.json}`, `lib/research/harvest/**` (rk-81's),
  `lib/opal_naming.py` and `infra/**`. Reads need no grant. Scratch is `<your worktree>/.scratch/r85/` only.
- **Collision check, done at the cut:** round 21's other cells write `lib/research/harvest/**` (rk-81),
  `infra/aws/terraform/harvest/*.tf` (rk-82) and their own channel files (rk-83/rk-84/rk-86). The only shared file is
  `INVESTIGATION_v1.md` (append-only; do not isolate it).
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~85 <0.9.0_WK_AMGT_RESAPP~85@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by the Write tool). Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

**NO LIVE FETCH, NO VENDOR CALL, NO S3 WRITE, NO AWS CALL AT ALL, NO RELEASE UPLOAD, NO READER SWITCH, NO DEPLOY.**
Every test uses a stub S3 client; AC3 runs them with the credential variables pointed at a nonexistent profile. The
harvest grammar stays OFF by default (ruling 4). No pair is needed: the cell has no live act. **COLLECTION STAYS OFF**;
PORTAL not your surface; NO alarm, monitor, SNS/SES-send, notification or freshness checker. No secrets are needed. No
non-ASCII in anything you write. **PUSH: never** (LD-0522).
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name -- in particular never by editing a WALL file,
never by importing `harvest_grammar` from `catalog.py` or any packaged module, and never by a live call.
**A COUNT BAR IS READ AT SPAWN AND PRINTS its denominator** -- re-measure the two suite baselines before you edit
(at the cut: `integrations/seekingalpha/tests` 4 passed; `lib/opal_data_harvest` 26 passed, 3 failed -- the 3
PRE-EXISTING failures are `test_verification.py::Tests::test_disabled_barrons_contract_defers_before_opening_a_browser`
(FileExistsError, WinError 183) and two in `test_worker.py` at `publishers.py:304` (AttributeError); they must be the
SAME failures after your edit, never more).
**SURPRISE ROWS:** `AMGT_RESAPP-Z-W85-S<k>`, `<k>` from 1; `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`; append by
textual splice inside the one fenced JSON array; never edit an existing row; a worker names the issuer
(`2.0.0_SA_COO~Z`) as `disarm_owner`, never itself.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120 except AC7, which runs under timeout 300)

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-85"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import sys, importlib; sys.path.insert(0, "."); import lib.opal_naming as n; r = n.validate(); print("refusals", len(r[0]) if isinstance(r, tuple) else r); [print(s, t, q, n.address(s, "harvest", t, q, p, o).split("/")[2]) for s, t, q, p, o in (("seeking-alpha", "bronze", "symbol", "security_key=BABA_US_Equity", "20260911T040211Z.json"), ("seeking-alpha", "bronze", "article", "article_hash=" + "0" * 64, "20260915T042900Z.json"), ("barrons", "bronze", "article", "article_hash=" + "0" * 64, "20260915T050100Z.json"), ("seeking-alpha", "silver", "article", "date=2026-09-21", "part-x.parquet"), ("barrons", "silver", "article", "date=2026-09-21", "part-x.parquet"))]; st = importlib.import_module("lib.research.harvest.store"); need = ("bronze_put", "fetch_key_exists", "silver_append", "silver_latest", "entity_partition", "address_of", "stamp", "form_a_object", "record_hash"); print("store_names_present", sum(hasattr(st, x) for x in need), "of", len(need))'</invocation><expect>"refusals 0", then 5 lines each ending "opal-data-harvest" (the duplicate harvest scope row is gone, @10bace8916 -- measured so at the cut @dbfcfc0817), then "store_names_present 9 of 9" (AMGT-rk-81 merged). At the cut the store module was ABSENT (ModuleNotFoundError) because rk-81 had not drained -- a ModuleNotFoundError, any line printing opal-data-assets, or fewer than 9 of 9 is a STOP: file a BLOCKING row and edit nothing</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-85"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest integrations/seekingalpha/tests/test_rest_harvest.py lib/opal_data_harvest/test_harvest_grammar.py -v -p no:cacheprovider 2>&1 | tail -20</invocation><expect>0 failed, and PASSED lines naming test_article_hash_matches_live_sa_object, test_one_writer_for_both_channels, test_fetch_key_known_skips_the_get, test_symbol_bronze_is_bytes_as_received, test_slash_key_is_a_partition, test_silver_article_row_keeps_every_field, test_harvest_mode_is_off_by_default and test_pinned_base_has_no_harvest_path -- 8 of 8 named arms (more arms are allowed; print the total)</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-85"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest integrations/seekingalpha/tests -q -p no:cacheprovider 2>&1 | tail -1 && python -m pytest lib/opal_data_harvest -q -p no:cacheprovider -rf 2>&1 | grep -E "^FAILED|passed|failed"</invocation><expect>the SA suite reads "passed" with 0 failed and a count equal to the spawn baseline (4 at the cut) plus that file's new arms; the harvester suite reads the spawn baseline (26 passed at the cut) plus that file's new arms, and its FAILED lines are EXACTLY the pre-existing ones named in section 4 (3 at the cut, same test ids) -- one more failure, or a different failing id, FAILS this criterion</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-85"><invocation>cd "$(git rev-parse --show-toplevel)" && env -u AWS_ACCESS_KEY_ID -u AWS_SECRET_ACCESS_KEY -u AWS_SESSION_TOKEN AWS_PROFILE=nonexistent-rk85 AWS_CONFIG_FILE=/dev/null AWS_SHARED_CREDENTIALS_FILE=/dev/null python -m pytest integrations/seekingalpha/tests/test_rest_harvest.py lib/opal_data_harvest/test_harvest_grammar.py -q -p no:cacheprovider 2>&1 | tail -1</invocation><expect>the same pass count as AC1 with 0 failed -- with no credentials resolvable, any real AWS call would raise, so a green run proves the tests touched only the stub; zero S3 writes by this cell (the Z-S192 census of the act's own write set)</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-85"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import subprocess, hashlib; pin = "dbfcfc0817bdd8694796165e3e4489d03973fb0a"; wall = ("lib/opal_data_harvest/__init__.py", "lib/opal_data_harvest/catalog.py", "lib/opal_data_harvest/storage.py", "lib/opal_data_harvest/config.json", "lib/opal_data_harvest/article.schema.json", "lib/opal_data_harvest/security-article.schema.json"); same = [f for f in wall if hashlib.sha256(open(f, "rb").read()).hexdigest() == hashlib.sha256(subprocess.run(["git", "show", pin + ":" + f], capture_output=True).stdout).hexdigest()]; print("wall_byte_identical", len(same), "of", len(wall)); d = subprocess.run(["git", "diff", "--name-only", pin, "HEAD"], capture_output=True, text=True).stdout.split(); print("infra_paths_in_diff", [p for p in d if p.startswith("infra/")])' && cd infra/aws/terraform/harvest/lambda_src && python -c 'import build_zip; m = build_zip.closure(); print("closure_members", len(m)); print("harvest_grammar_in_closure", any("harvest_grammar" in k for k in m)); print("store_in_closure", any("research/harvest" in k for k in m))' 2>&1 | tail -3</invocation><expect>"wall_byte_identical 6 of 6", "infra_paths_in_diff []" (at the worker's HEAD the diff from the pin may carry OTHER merged cells' infra files -- if so, list them and show none is written by this cell's commits), then "closure_members 15" (measured 15 at the cut), "harvest_grammar_in_closure False" and "store_in_closure False" -- so neither AMGT Lambda carries this cell's code</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-85"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import ast, subprocess; pin = "dbfcfc0817bdd8694796165e3e4489d03973fb0a"; src = lambda p, ref=None: subprocess.run(["git", "show", ref + ":" + p], capture_output=True, text=True).stdout if ref else open(p, encoding="utf-8").read(); fn = lambda s, name: next((ast.dump(n) for n in ast.walk(ast.parse(s)) if isinstance(n, (ast.FunctionDef, ast.ClassDef)) and n.name == name), None); print("land_raw_unchanged", fn(src("integrations/seekingalpha/rest_fetch.py"), "land_raw") == fn(src("integrations/seekingalpha/rest_fetch.py", pin), "land_raw")); print("Uploader_unchanged", fn(src("lib/opal_data_harvest/uploads.py"), "Uploader") == fn(src("lib/opal_data_harvest/uploads.py", pin), "Uploader")); files = ("integrations/seekingalpha/rest_fetch.py", "lib/opal_data_harvest/uploads.py", "lib/opal_data_harvest/harvest_grammar.py", "lib/opal_data_harvest/worker.py", "lib/opal_data_harvest/publishers.py"); puts = {f: sum(1 for n in ast.walk(ast.parse(src(f))) if isinstance(n, ast.Call) and getattr(n.func, "attr", "") == "put_object") for f in files}; print("put_object_sites", puts); writers = [f for f in files if "article_hash" in src(f) and "bronze_put" in src(f)]; print("article_hash_bronze_writers", writers)'</invocation><expect>"land_raw_unchanged True", "Uploader_unchanged True", "put_object_sites" reading rest_fetch.py 1, uploads.py 1, harvest_grammar.py 0, worker.py 0, publishers.py 0 (the two legacy writers, unchanged; the new path writes only through the store), and "article_hash_bronze_writers ['lib/opal_data_harvest/harvest_grammar.py']" -- exactly ONE file holds the article fetch keys (C-DEDUPE-BY-KEY, ruling 2)</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rk-85"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import io; fs = ("integrations/seekingalpha/rest_fetch.py", "integrations/seekingalpha/tests/test_rest_harvest.py", "lib/opal_data_harvest/harvest_grammar.py", "lib/opal_data_harvest/uploads.py", "lib/opal_data_harvest/publishers.py", "lib/opal_data_harvest/worker.py", "lib/opal_data_harvest/build_release.py", "lib/opal_data_harvest/test_harvest_grammar.py"); [print(f.split("/")[-1], "compiles", bool(compile(io.open(f, "rb").read().decode("utf-8"), f, "exec")), "crlf", io.open(f, "rb").read().count(b"\r\n"), "non_ascii_bytes", len(io.open(f, "rb").read()) - len(io.open(f, "rb").read().decode("utf-8"))) for f in fs]; print("harvest_grammar_in_release", "harvest_grammar.py" in io.open("lib/opal_data_harvest/build_release.py", encoding="utf-8").read())'</invocation><expect>8 lines, each "compiles True crlf 0 non_ascii_bytes 0" (every file ASCII/LF at the cut), then "harvest_grammar_in_release True"</expect></criterion>
  <criterion id="AC7" cell_refs="AMGT-rk-85"><invocation>cd "$(git rev-parse --show-toplevel)" && mkdir -p .scratch/r85 && python -c 'import contextlib, hashlib, io, os, subprocess, sys, importlib.util, pathlib, shutil, tarfile
PIN = "dbfcfc0817bdd8694796165e3e4489d03973fb0a"; SH = "infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh"; BZ = "infra/aws/terraform/harvest/lambda_src/build_zip.py"; Q = chr(39)
def adapter_inputs(root):
    body = open(os.path.join(root, SH), encoding="utf-8").read().split("<<" + Q + "PYEOF" + Q + "\n", 1)[1].split("\nPYEOF", 1)[0].split("# ---- VENDOR", 1)[0]
    g = {"__name__": "adapter_closure"}; old = sys.argv; sys.argv = ["x", root, os.devnull, os.devnull]
    try:
        with contextlib.redirect_stdout(io.StringIO()): exec(compile(body, SH, "exec"), g)
    finally: sys.argv = old
    return sorted(set(os.path.relpath(p, root).replace(os.sep, "/") for p in g["members"].values()) | set(r for r, _, _ in g["DATA_MEMBERS"]))
def chatter_inputs(root, tag):
    spec = importlib.util.spec_from_file_location("bz_" + tag, os.path.join(root, BZ)); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    with contextlib.redirect_stdout(io.StringIO()): code = m.closure()
    r = pathlib.Path(root).resolve(); rel = lambda p: str(pathlib.Path(p).resolve().relative_to(r)).replace(os.sep, "/")
    return sorted(set(rel(p) for p in code.values()) | set(rel(p) for p, _, _ in m._DATA_MEMBERS))
base = os.path.abspath(".scratch/r85/pin_tree"); shutil.rmtree(base, ignore_errors=True); os.makedirs(base)
tar = subprocess.run(["git", "archive", "--format=tar", PIN, "lib", "infra/aws/lambda/research", "infra/aws/terraform/harvest", "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~5/lists", "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~4/universe.json"], capture_output=True, check=True).stdout
tarfile.open(fileobj=io.BytesIO(tar)).extractall(base)
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest() if os.path.isfile(p) else None
mine = ("harvest_grammar.py", "publishers.py", "worker.py", "uploads.py", "build_release.py", "rest_fetch.py")
for name, fn in (("adapter", lambda r, t: adapter_inputs(r)), ("chatter", chatter_inputs)):
    h = fn(os.getcwd(), "head"); b = fn(base, "pin"); ch = [p for p in sorted(set(h) | set(b)) if sha(os.path.join(os.getcwd(), p)) != sha(os.path.join(base, p))]
    print(name, "head_inputs", len(h), "pin_inputs", len(b), "list_equal", h == b, "members_changed", len(ch), ch[:5], "this_cells_files_in_list", [p for p in h if p.split("/")[-1] in mine])
'</invocation><expect>adapter head_inputs 57 pin_inputs 57 list_equal True members_changed 0 [] this_cells_files_in_list [] ; chatter head_inputs 18 pin_inputs 18 list_equal True members_changed 0 [] this_cells_files_in_list [] -- measured so at the issuer cut (HEAD 5912b7d107 and later, against pin dbfcfc0817): the adapter list is the build script's OWN closure (its embedded python up to the VENDOR step: 50 code members + 7 DATA_MEMBERS, repo paths; the earlier "58" censuses counted the build script itself) and the chatter list is build_zip.closure() + _DATA_MEMBERS (15 code + 3 data), each DERIVED from the build script at the worker HEAD and again at the pin from a git-archive copy, never a typed filename list (CTO msg 24106 item 5, Rule 22a). If another merged cell legitimately moved a packaged file between the pin and your HEAD, members_changed is non-zero: list each such path with the commit that changed it (git log --format=%h\ %an) and show NONE is authored by 0.9.0_WK_AMGT_RESAPP~85 -- any member changed by THIS cell FAILS the criterion. harvest_grammar.py is added only to build_release.py PACKAGE_FILES, which builds the desktop harvester release (lib/local-publications/...), not either AMGT Lambda. Pure local reads: no pip download, no AWS call, no install</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~85/AMGT_RESAPP.TO-AMGT-rk-85.sa-publications-writer.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4,AC5,AC6,AC7` (rc 0 is the verdict); flip the status
tag in the record face to `complete` ONLY if every criterion passes; commit with `--only -- <paths>`. Report once.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/r85/` before editing. Never `git checkout --`, never
`git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the cell spawns ONLY after `AMGT-rk-81` (H0-store) has drained -- AC0(b) STOPs otherwise. Named for
the CTO at issuance: ruling 1 (`sa:` not `seeking-alpha:` in the article hash, against plan s.5.4 `:273-274`), ruling 3
(the plan's `catalog.py` change moved to a new unpackaged module to avoid a carry-along into both Lambdas), ruling 5
(`publishers.py` and `worker.py` joined the write surface because the response bytes were never carried).

**CTO msg 24106 conditions carried:** item 1 (`sa:`) and item 5 (walls, the new module, the L5 widening) RULED as
recommended; item 5's condition is AC7 (build-INPUT lists derived from both build scripts, 57 adapter / 18
chatter at the cut, 0 members changed, pin vs HEAD).

<status>pending</status>
<round>21</round>
<slot>~85</slot>
<fabric>site-z</fabric>
