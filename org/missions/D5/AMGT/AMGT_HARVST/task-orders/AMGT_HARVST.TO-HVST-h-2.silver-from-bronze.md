# AMGT_HARVST task order -- `HVST-h-2` -- H2: the silver `article` and `listing_hit` tables are rebuilt FROM BRONZE, with every vendor field typed and three clocks, never from the normalised record; CODE ONLY, stub S3 client, no vendor call

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-h-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~2</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on lib/opal_data_harvest or any harvest surface (C1=23 C2=7 C3=12 C4=21 C5=334); this cell arms nothing.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; every S3 touch in the tests is a STUB client.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_HARVST~2`.** Work ONLY in the worktree whose absolute path is in your spawn prompt.
- **Your first act** prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that `org/`,
  `.tools/`, every EXISTING path in section 3, AND `lib/opal_data_harvest/test_bronze_capture.py` exist.
  - That last file is the predecessor cell's. If it is absent, your base predates it: STOP with a BLOCKING row.
- Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_HARVST~2;`.
- **NEVER RUN AN INSTALL. NEVER CALL A PUBLISHER, NEVER CALL AWS, NEVER RUN THE HARVESTER CLI.**

## 1. THE CELL, inlined in full -- `HVST-h-2` (manifest row H2, outcome FWD-2)

**The contract, verbatim** (PRD v0.2 @9102ccfe81, `C-HV-SILVER-FROM-BRONZE`):
- The silver `article` table (`{source}/harvest/silver/article/date=<d>/part-<stamp>.parquet`) is built ONLY from bronze,
  and is replayable from it.
- Every vendor field present in bronze is kept with standard typing (string, int, bool, timestamp, list, struct).
  Nothing is filtered or summarised.
- Silver carries three clocks, never substituted for one another:
  - `published_utc`, `published_offset_min`, `published_date_utc` and `published_precision`;
  - `fetched_at`;
  - `first_discovered_at`.
- The listing hits land in `{source}/harvest/silver/listing_hit/date=<d>/`.
- The `date=` partition is the FETCH date. `published_date_utc` is a column, never the partition.
- Every row carries `bronze_key`, `fetched_at` and `record_hash`.
- Every row also carries `retrieval_mode` (`backfill | live`) and `run_stamp`.
- The keys:
  - `article`: record key = `article_key` (`<publisher_code>:<article_id>`).
  - `listing_hit`: record key = (listing fetch key, `search_rank`), where the listing fetch key = (source, query sha256,
    UTC date, page).
- This supersedes the silver writer built in `AMGT_RESAPP`'s round-21 bronze writer cell, which shapes the row from the
  18-field normalised record.

**Outcome FWD-2, DONE WHEN:** *"every field present in the received article (including language, paywall flags, the
publisher's own ticker tags, sentiment, themes and summary where sent) appears typed in the queryable table, rebuilt from
the stored original, and a query by company and date returns it"*. This cell builds it; `HVST-h-10` exercises it live.

**THE STATE you start from** (read at your branch HEAD):
- `harvest_grammar.article_silver_row(record, bronze_key)` copies the normalised record (the SUPERSEDED shape).
- After `HVST-h-1`, bronze objects are:
  - article bodies: SA, Bloomberg and Barron's are JSON; WSJ and FT are HTML;
  - listing bodies, under `news_listing`;
  - each carrying the S3 metadata `received-form` (`as_received`, or `normalised_record` for the desktop's legacy
    records, which `HVST-h-9` writes after you).
- The HTML carriers of the vendor fields, as the harvester already parses them (`lib/opal_data_harvest/publishers.py`):
  - WSJ: `script#__NEXT_DATA__` -> `props.pageProps` (`articleData` and its siblings);
  - FT: the JSON-LD object carrying `articleBody` (`json_fields`, `:33-44`), falling back to the page's own fields;
  - Barron's: the articles-API JSON (`articleData` and `body`);
  - Bloomberg: the story JSON (`story`);
  - SA: `/api/v3/articles/{id}` JSON:API (`data.attributes`, `data.relationships`, `included`).
- The listing carriers: SA news JSON:API `data[]`; Bloomberg search `results[]`; the FT search page's teaser links; the
  Dow Jones search page (`__NEXT_DATA__` `searchData.articles[]` for Barron's, `searchResults[]` for WSJ, anchors
  otherwise).
- `store.silver_append(source, table, rows, record_key_fields, run_stamp, client=None)`
  (`lib/research/harvest/store.py:348-401`):
  - it validates each row (a tz-aware `fetched_at`, and a non-None `bronze_key`);
  - it skips unchanged rows;
  - it adds `record_hash`;
  - it writes one `part-<run_stamp>.parquet` per fetch-date partition.
  **Use it; do not edit it.**
- `HarvestUploader.run` (`uploads.py`) builds its silver row from the queued record JSON. That is the step you replace.

**RULED -- what you build:**
1. **A new module, `lib/opal_data_harvest/silver_from_bronze.py`, pure and without I/O:**
   - `article_rows(publisher_code, body_bytes, received_form, bronze_key, fetched_at, retrieval_mode, run_stamp, discovery=None)`
     returns one `article` row.
     - It extracts the vendor object from the bytes per publisher, as above. For `normalised_record`, the object is
       the record itself.
     - It keeps EVERY field. A nested dict stays a struct and a list stays a list. Scalar strings that parse as
       ISO-8601 timestamps become tz-aware datetimes ONLY for fields it names in a documented `TIMESTAMP_FIELDS`
       table per publisher. It never guesses.
     - It adds `article_key`, `publisher`, `article_id`, `title`, `text_blocks` (a list of strings, as the harvester's
       block logic builds them), the three clocks, `bronze_key`, `fetched_at`, `retrieval_mode` and `run_stamp`.
     - `discovery` is an optional dict carrying `first_discovered_at`, `retrieval_rung`, `search_query`,
       `search_rank`, `search_page` and `discovered_for` (a LIST of security keys: one article found for two securities
       carries both). When it is None those columns are present and None;
       `HVST-h-3` fills them.
   - `listing_hit_rows(publisher_code, body_bytes, query, page, bronze_key, fetched_at, retrieval_mode, run_stamp)`
     returns one row per hit, carrying `search_rank` (1-based within the page), `search_page`, `search_query`,
     `query_sha256`, the hit's article id and/or URL, and every field the listing item carries.
   - **The published clock:**
     - `published_utc` is the instant in UTC.
     - `published_offset_min` is the offset the vendor wrote, in minutes. `Z` gives 0. An absent offset gives None and
       `published_precision="naive_assumed_utc"`.
     - `published_date_utc` is the UTC date.
     - `published_precision` is one of `instant`, `date_only` or `naive_assumed_utc`.
   - **`retrieval_mode` must be `backfill` or `live`.** Anything else raises `ValueError`.
2. **`HarvestUploader.run`** (`uploads.py`) takes `retrieval_mode` (default `live`). After each bronze put, it builds the
   silver row with `silver_from_bronze.article_rows`, from the SAME bytes it put, never from `record_json`, and appends
   it with record key `("article_key",)`. Each listing's hits go through `silver_from_bronze.listing_hit_rows` into
   `listing_hit`, with record key `("query_sha256", "fetch_date_utc", "search_page", "search_rank", "source")`.
3. **`harvest_grammar.article_silver_row` and `search_result_row`** are KEPT (other callers may exist), but no path in
   `HarvestUploader` calls them any more.
4. **New test file `lib/opal_data_harvest/test_silver_from_bronze.py`,** with a STUB S3 client (the pattern in
   `lib/research/harvest/tests/test_store.py`) and synthetic bronze fixtures shaped like the carriers above. Exactly
   these fourteen arms:
   - `test_article_rows_keep_every_field_sa`
   - `test_article_rows_keep_every_field_bbg`
   - `test_article_rows_keep_every_field_barrons`
   - `test_article_rows_keep_every_field_wsj`
   - `test_article_rows_keep_every_field_ft`
   - `test_article_rows_from_normalised_record`
   - `test_published_clock_offset_kept`
   - `test_published_clock_date_only_and_naive`
   - `test_listing_hit_rows_each_publisher`
   - `test_lineage_and_mode_columns_present`
   - `test_retrieval_mode_refuses_unknown`
   - `test_partition_is_fetch_date_not_published_date`
   - `test_replay_is_identical`
   - `test_uploader_silver_reads_bronze_not_record`

   What some arms must assert:
   - Each "every field" arm flattens the fixture's vendor object and the row. It asserts every fixture leaf path is
     present in the row, with its value, and that the count of missing leaves is 0.
   - `test_published_clock_offset_kept` uses a `+08:00` stamp and asserts `published_offset_min == 480`.
   - `test_uploader_silver_reads_bronze_not_record` changes the queued record's title and asserts the silver title
     still equals the bronze title.

**What this cell does NOT change:**
- `store.py`;
- the bronze capture (`transport.py`, `publishers.py`);
- `worker.py`;
- the legacy `Uploader`;
- the CLI;
- `config.json`.

## 2. WHERE THIS CAME FROM
Round 1, decomposition v1.0 @9fbf337a74, chain A position 2 of 9. After `HVST-h-1`; before `HVST-h-9`, which uploads the
desktop's legacy records through your builder.

## 3. SURFACES -- what you may read and write

<paths>
lib/opal_data_harvest/silver_from_bronze.py
lib/opal_data_harvest/test_silver_from_bronze.py
lib/opal_data_harvest/uploads.py
lib/opal_data_harvest/harvest_grammar.py
lib/opal_data_harvest/publishers.py
lib/opal_data_harvest/test_bronze_capture.py
lib/opal_data_harvest/test_harvest_grammar.py
lib/opal_data_harvest/test_worker.py
lib/opal_data_harvest/test_catalog.py
lib/opal_data_harvest/test_verification.py
lib/opal_data_harvest/article.schema.json
lib/research/harvest/store.py
lib/research/harvest/tests/test_store.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~2/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-h-2.silver-from-bronze.md
</paths>

- **A surface not named in `<paths>` is a wall.** Only `silver_from_bronze.py`, `test_silver_from_bronze.py`,
  `uploads.py` and `harvest_grammar.py` may change. AC3 fails otherwise.
- Scratch goes in `<your worktree>/.scratch/hv2/`.
- **Committing:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_HARVST~2 <0.9.0_WK_AMGT_HARVST~2@opal.agent>" -F <msgfile> -- <paths>`.

## 4. BOUNDS
- **CODE ONLY.** Stubs for every S3 touch. Run each test FILE with its own pytest call.
- **The pin is `9fbf337a74`.** AC3 diffs against it, so `HVST-h-1`'s files will also show as changed. They are listed
  in AC3's allowed set.
- **Pre-existing failures must not GROW** (`test_worker.py` and `test_verification.py`, measured at AC0).
- **All new text is pure ASCII.**
- **Surprise rows:** `AMGT_HARVST-Z-W2-S<k>`, with `disarm_owner` `2.0.0_SA_COO~Y`.

## 5. PROOF OF SPEC (each invocation LITERAL; timeout 600)

Before AC3, write `.scratch/hv2/ac3.py`:
```
import subprocess
allowed = {"lib/opal_data_harvest/transport.py", "lib/opal_data_harvest/publishers.py", "lib/opal_data_harvest/harvest_grammar.py", "lib/opal_data_harvest/worker.py", "lib/opal_data_harvest/uploads.py", "lib/opal_data_harvest/test_bronze_capture.py", "lib/opal_data_harvest/silver_from_bronze.py", "lib/opal_data_harvest/test_silver_from_bronze.py"}
mine = {"lib/opal_data_harvest/silver_from_bronze.py", "lib/opal_data_harvest/test_silver_from_bronze.py", "lib/opal_data_harvest/uploads.py", "lib/opal_data_harvest/harvest_grammar.py"}
out = subprocess.run(["git", "diff", "--name-only", "9fbf337a74", "HEAD", "--", "lib", "integrations", "infra", ".tools", "portal", "org/tier1_exec"], capture_output=True, text=True).stdout.split()
print("changed_code_files", sorted(out))
print("outside_allowed", sorted(set(out) - allowed))
for f in sorted(set(out) & mine):
    b = open(f, "rb").read()
    compile(b.decode("utf-8"), f, "exec")
    print(f, "compiles True crlf", b.count(bytes([13, 10])), "non_ascii_chars", sum(1 for ch in b.decode("utf-8") if ord(ch) > 127))
```

<proof_of_spec>
  <criterion id="AC0" cell_refs="HVST-h-2"><invocation>cd "$(git rev-parse --show-toplevel)" && for t in lib/opal_data_harvest/test_bronze_capture.py lib/opal_data_harvest/test_harvest_grammar.py lib/opal_data_harvest/test_worker.py lib/opal_data_harvest/test_catalog.py lib/opal_data_harvest/test_verification.py lib/research/harvest/tests/test_store.py; do echo "$t :: $(python -m pytest $t -q --color=no -p no:cacheprovider 2>&1 | tail -1)"; done</invocation><expect>BEFORE any edit, six baseline lines recorded; test_bronze_capture.py reads "12 passed" (the predecessor's bar)</expect></criterion>
  <criterion id="AC1" cell_refs="HVST-h-2"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/opal_data_harvest/test_silver_from_bronze.py -v --color=no -p no:cacheprovider 2>&1 | tail -18</invocation><expect>"14 passed" and no "failed" -- the fourteen arms named in section 1 item 4</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-h-2"><invocation>cd "$(git rev-parse --show-toplevel)" && for t in lib/opal_data_harvest/test_bronze_capture.py lib/opal_data_harvest/test_harvest_grammar.py lib/opal_data_harvest/test_worker.py lib/opal_data_harvest/test_catalog.py lib/opal_data_harvest/test_verification.py lib/research/harvest/tests/test_store.py; do echo "$t :: $(python -m pytest $t -q --color=no -p no:cacheprovider 2>&1 | tail -1)"; done</invocation><expect>each line's passed and failed counts EQUAL its AC0 line: no new failure</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-h-2"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/hv2/ac3.py</invocation><expect>"outside_allowed []"; each of this cell's changed files prints "compiles True crlf 0 non_ascii_chars 0"</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR.** No judgment criterion.

## 6. WHEN YOU ARE DONE
1. Write the instance to
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~2/AMGT_HARVST.TO-HVST-h-2.silver-from-bronze.proof_of_spec.json`.
2. Grade it with `python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3`, which must return rc 0.
3. Flip to `complete` only if every criterion passes.
4. Commit with `--only`.
5. Report once. Your report NAMES the silver columns you built, because `HVST-h-4` reads them.

**MUTATION DISCIPLINE:** snapshot the working-tree bytes to `.scratch/hv2/` first. Never `git checkout --`, `stash` or
`git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**
1. **The listing_hit record key** spells out the contract's (listing fetch key, `search_rank`) as five columns, because
   `silver_append` takes field names.
2. **`TIMESTAMP_FIELDS` is declared, never guessed.** A guessing typer would retype a vendor's free-text field and lose
   fidelity silently.
3. **CHAINED:** `HVST-h-9` calls `article_rows` with `received_form="normalised_record"`.

<status>pending</status>
<round>1</round>
<slot>~2</slot>
<fabric>site-z</fabric>
