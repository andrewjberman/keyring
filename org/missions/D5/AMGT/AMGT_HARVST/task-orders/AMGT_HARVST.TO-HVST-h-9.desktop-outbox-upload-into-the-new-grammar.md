# AMGT_HARVST task order -- `HVST-h-9` -- H9: the 83 articles and 84 links held only on this desktop reach the new grammar through the ONE writer, as `normalised_record` bronze plus silver rows, deduped, and the upload is reachable from the CLI; S3 writes to `opal-data-harvest` only, NOT vendor egress

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-h-9</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~9</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on any harvest surface (C1=23 C2=7 C3=12 C4=21 C5=334); the cell writes S3 objects, which is not a deploy, and arms nothing.
comp-iam: RUN at L5 on the DESIRED plane only; this box's own credential for opal-data-harvest bronze and silver writes is NOT read by the lens, so AC4 measures it with a real conditional PUT.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_HARVST~9`.** Work ONLY in the worktree whose absolute path is in your spawn prompt.
- **Your first act** prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that `org/`,
  `.tools/`, every EXISTING path in section 3, `lib/opal_data_harvest/test_bronze_capture.py` and
  `lib/opal_data_harvest/silver_from_bronze.py` exist.
  - The last two are the predecessor cells'. If either is absent, STOP with a BLOCKING row.
- Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_HARVST~9;`.
- **NEVER RUN AN INSTALL. NEVER CALL A PUBLISHER.**
- AWS is allowed ONLY as S3 reads and conditional writes under `s3://opal-data-harvest/`, through the harvester's own
  writers.
- **NEVER run the legacy `upload` command.** It writes the retiring `publications/v1/` prefix.

## 1. THE CELL, inlined in full -- `HVST-h-9` (manifest row H9, outcome FWD-8)

**Outcome FWD-8, DONE WHEN:** *"every article and link held only on the collecting desktop is in the store, with none
duplicated"*.

**The contract, verbatim** (`C-HV-EGRESS`): *"Uploading articles already held on the desktop is not egress."*

**THE MEASURED STATE at SITEZ @9fbf337a74:**
- **The desktop runtime is the MAIN workspace's `.runtime/opal-data-harvest/`.** It is gitignored, so it is NOT in your
  worktree. Derive the main root with `git worktree list --porcelain | head -1`, and never type a drive path.
- The runtime's `progress.sqlite3`, read-only, holds:

  | table | rows |
  |---|---|
  | `article_objects` | 83 |
  | `article_aliases` | 83 |
  | `article_links` | 84 |
  | `articles` | 84 |
  | `upload_outbox` | 167, all `pending` (83 `publications/v1/`, 84 `publication-links/v1/`) |

  `articles` by publisher: `sa` 20, `bbg` 19, `barrons` 15, `ft` 15, `wsj` 15.
- There is no `harvest_raw_outbox` table: harvest mode never ran.
- These records are the harvester's NORMALISED records (`lib/opal_data_harvest/article.schema.json` and
  `security-article.schema.json`). **Their received bytes were never kept**, so they can never be `as_received`.
- The CLI (`__main__.py`) `upload` command reaches only the legacy `Uploader` (`publications/v1/`). `HarvestUploader`
  is reachable from no command.
- `seeking-alpha/harvest/bronze/article/` already holds 6 objects from the SA REST channel, hashed
  `sha256("sa:"+id)` (the handoff's measurement). A legacy SA article with the same id is a DEDUPE HIT, never a second
  object.

**RULED -- what you build:**
1. **A new CLI command `upload-legacy`** (`__main__.py`), which reads the legacy tables READ-ONLY. It opens the SQLite
   with `mode=ro` and never writes to `progress.sqlite3`. For each article object:
   - It puts the stored record file's bytes as bronze through
     `harvest_grammar.put_article_bronze(publisher, article_id, <bytes>, "json", <record fetched_at>, received_form="normalised_record")`.
   - It builds the silver row with `silver_from_bronze.article_rows(..., received_form="normalised_record", retrieval_mode="live", discovery=...)`,
     from those SAME bytes, and appends it with record key `("article_key",)`.
   - `discovery` comes from the article's links:
     - `discovered_for` is the LIST of every linked `security_key`;
     - `first_discovered_at` is the earliest link's value;
     - `retrieval_rung` is `symbol_listing` for `sa` and `name_search` for the other four;
     - `search_query` is the query the legacy harvester sent: the security's `sa_symbol` for `sa`, else its `company`,
       from `config.json` `pilot_securities`;
     - `search_rank` and `search_page` are None, because the legacy run recorded neither.

   The command prints ONE JSON receipt:
   `{"articles_seen", "bronze_put", "bronze_skipped", "silver_rows_written", "silver_rows_unchanged", "links_seen", "links_carried", "errors", "bronze_keys"}`,
   where `links_carried` counts (article, security) pairs present in `discovered_for`, and `bronze_keys` lists the S3
   key of every article bronze object the run put OR skipped as already held (one per article, so its length equals
   `articles_seen`). AC6 reads that list.
2. **A new CLI command `upload-harvest`** runs `HarvestUploader(...).run(max_objects, retrieval_mode=...)` with a
   `--retrieval-mode` flag. It makes the new-grammar uploader reachable; `HVST-h-10` uses it.
3. **Both commands take `--runtime-root`**, which already exists. No path is hardcoded.
4. **New test file `lib/opal_data_harvest/test_legacy_upload.py`,** with a STUB S3 client and a temp SQLite built from a
   fixture. Exactly six arms:
   - `test_legacy_article_uploaded_as_normalised_record`
   - `test_legacy_links_become_discovered_for`
   - `test_legacy_upload_dedupes_existing_hash`
   - `test_legacy_upload_is_read_only_on_sqlite` (the DB file's bytes are unchanged after a run)
   - `test_cli_upload_legacy_reachable`
   - `test_cli_upload_harvest_reachable`

**What this cell does NOT change:**
- the legacy `Uploader`, the `upload` command and `upload_outbox`;
- `store.py`;
- the bronze and silver builders' behaviour for `as_received`;
- `config.json`;
- anything under `publications/v1/` or `publication-links/v1/`.

## 2. WHERE THIS CAME FROM
Round 1, decomposition v1.0 @9fbf337a74, chain A position 3 of 9. After `HVST-h-2`; before `HVST-h-3`. The pilots'
articles you land are the gold cells' second sample.

## 3. SURFACES -- what you may read and write

<paths>
lib/opal_data_harvest/__main__.py
lib/opal_data_harvest/uploads.py
lib/opal_data_harvest/test_legacy_upload.py
lib/opal_data_harvest/harvest_grammar.py
lib/opal_data_harvest/silver_from_bronze.py
lib/opal_data_harvest/catalog.py
lib/opal_data_harvest/storage.py
lib/opal_data_harvest/config.json
lib/opal_data_harvest/article.schema.json
lib/opal_data_harvest/security-article.schema.json
lib/opal_data_harvest/test_bronze_capture.py
lib/opal_data_harvest/test_silver_from_bronze.py
lib/opal_data_harvest/test_harvest_grammar.py
lib/opal_data_harvest/test_worker.py
lib/opal_data_harvest/test_catalog.py
lib/opal_data_harvest/test_verification.py
lib/research/harvest/store.py
lib/research/harvest/tests/test_store.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~9/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-h-9.desktop-outbox-upload-into-the-new-grammar.md
</paths>

- **Only `__main__.py`, `uploads.py` and the new test file may change.** AC3 fails otherwise.
- **The main workspace's `.runtime/`** is read (and its SQLite opened read-only). It is not a repo path and is never
  committed.
- Scratch goes in `<your worktree>/.scratch/hv9/`.
- **Committing:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_HARVST~9 <0.9.0_WK_AMGT_HARVST~9@opal.agent>" -F <msgfile> -- <paths>`.

## 4. BOUNDS
- **The code and tests come first** (AC1-AC3). The live upload (AC4-AC6) runs ONLY after they pass.
- **A refused PUT (AccessDenied) is a BLOCKING row.** Never a hand-typed key, and never another bucket.
- **Pre-existing test failures must not GROW.**
- **All new text is pure ASCII.**
- **Surprise rows:** `AMGT_HARVST-Z-W9-S<k>`, with `disarm_owner` `2.0.0_SA_COO~Y`.

## 5. PROOF OF SPEC (each invocation LITERAL; timeout 600)

Write two scratch scripts first.

`.scratch/hv9/ac3.py`:
```
import subprocess
allowed = {"lib/opal_data_harvest/transport.py", "lib/opal_data_harvest/publishers.py", "lib/opal_data_harvest/harvest_grammar.py", "lib/opal_data_harvest/worker.py", "lib/opal_data_harvest/uploads.py", "lib/opal_data_harvest/test_bronze_capture.py", "lib/opal_data_harvest/silver_from_bronze.py", "lib/opal_data_harvest/test_silver_from_bronze.py", "lib/opal_data_harvest/__main__.py", "lib/opal_data_harvest/test_legacy_upload.py"}
base = subprocess.run(["git", "merge-base", "HEAD", "SITEZ"], capture_output=True, text=True).stdout.strip()
print("fork_base", base)
out = subprocess.run(["git", "diff", "--name-only", base, "HEAD", "--", "lib", "integrations", "infra", ".tools", "portal", "org/tier1_exec"], capture_output=True, text=True).stdout.split()
print("outside_allowed", sorted(set(out) - allowed))
for f in ["lib/opal_data_harvest/__main__.py", "lib/opal_data_harvest/uploads.py", "lib/opal_data_harvest/test_legacy_upload.py"]:
    b = open(f, "rb").read()
    compile(b.decode("utf-8"), f, "exec")
    print(f, "compiles True crlf", b.count(bytes([13, 10])), "non_ascii_chars", sum(1 for ch in b.decode("utf-8") if ord(ch) > 127))
```

`.scratch/hv9/ac6.py` reads the receipt that AC4 saved to
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~9/upload_legacy.receipt.json`, which lists every
bronze key it put or skipped. For each key it calls `head_object` on `opal-data-harvest` and prints
`heads <ok> of <n>` and `received_form_counts <dict>`.

<proof_of_spec>
  <criterion id="AC0" cell_refs="HVST-h-9"><invocation>cd "$(git rev-parse --show-toplevel)" && for t in lib/opal_data_harvest/test_bronze_capture.py lib/opal_data_harvest/test_silver_from_bronze.py lib/opal_data_harvest/test_harvest_grammar.py lib/opal_data_harvest/test_worker.py lib/opal_data_harvest/test_catalog.py lib/opal_data_harvest/test_verification.py; do echo "$t :: $(python -m pytest $t -q --color=no -p no:cacheprovider 2>&1 | tail -1)"; done</invocation><expect>BEFORE any edit, six baseline lines recorded; test_bronze_capture.py "12 passed" and test_silver_from_bronze.py "14 passed"</expect></criterion>
  <criterion id="AC1" cell_refs="HVST-h-9"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/opal_data_harvest/test_legacy_upload.py -v --color=no -p no:cacheprovider 2>&1 | tail -10</invocation><expect>"6 passed" and no "failed" -- the six arms named in section 1 item 4</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-h-9"><invocation>cd "$(git rev-parse --show-toplevel)" && for t in lib/opal_data_harvest/test_bronze_capture.py lib/opal_data_harvest/test_silver_from_bronze.py lib/opal_data_harvest/test_harvest_grammar.py lib/opal_data_harvest/test_worker.py lib/opal_data_harvest/test_catalog.py lib/opal_data_harvest/test_verification.py; do echo "$t :: $(python -m pytest $t -q --color=no -p no:cacheprovider 2>&1 | tail -1)"; done</invocation><expect>each line's passed and failed counts EQUAL its AC0 line</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-h-9"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/hv9/ac3.py</invocation><expect>"outside_allowed []" and three lines each "compiles True crlf 0 non_ascii_chars 0"</expect></criterion>
  <criterion id="AC4" cell_refs="HVST-h-9"><invocation>cd "$(git rev-parse --show-toplevel)" && MAIN="$(git worktree list --porcelain | head -1 | sed 's/^worktree //')" && python -m lib.opal_data_harvest upload-legacy --runtime-root "$MAIN/.runtime/opal-data-harvest" | tee org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~9/upload_legacy.receipt.json</invocation><expect>a receipt with "articles_seen": 83, bronze_put plus bronze_skipped equal to 83, "links_seen": 84, "links_carried": 84 and "errors": 0</expect></criterion>
  <criterion id="AC5" cell_refs="HVST-h-9"><invocation>cd "$(git rev-parse --show-toplevel)" && MAIN="$(git worktree list --porcelain | head -1 | sed 's/^worktree //')" && python -m lib.opal_data_harvest upload-legacy --runtime-root "$MAIN/.runtime/opal-data-harvest"</invocation><expect>the SECOND run's receipt reads "bronze_put": 0 and "silver_rows_written": 0 with "errors": 0 -- none duplicated</expect></criterion>
  <criterion id="AC6" cell_refs="HVST-h-9"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/hv9/ac6.py</invocation><expect>"heads 83 of 83", and received_form_counts showing normalised_record for every key AC4 put (any pre-existing SA REST object skipped by dedupe shows its own form)</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR.** No judgment criterion.

## 6. WHEN YOU ARE DONE
1. Write the instance to
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~9/AMGT_HARVST.TO-HVST-h-9.desktop-outbox-upload-into-the-new-grammar.proof_of_spec.json`.
2. Grade it with `python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4,AC5,AC6`, which must return rc 0.
3. Flip to `complete` only if all pass.
4. Commit with `--only`.
5. Report once.

**MUTATION DISCIPLINE:** snapshot the working-tree bytes to `.scratch/hv9/` first. Never `git checkout --`, `stash` or
`git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**
1. **The links are carried as provenance, not as a judgement.** `discovered_for` records the security a search was run
   for, which is a retrieval fact. Whether the article is ABOUT that company is gold (`C-HV-LINK-IS-GOLD`, `HVST-h-4`).
2. **`retrieval_mode="live"` for the legacy records.** The legacy harvester collected recent articles forward; it never
   paged back to a floor.
3. **The legacy `upload_outbox` stays pending, untouched.** Its prefixes retire under `AMGT_RESAPP`'s
   `C-FORMAT-SEQUENCE`, which is not this round's act.

<status>pending</status>
<round>1</round>
<slot>~9</slot>
<fabric>site-z</fabric>
