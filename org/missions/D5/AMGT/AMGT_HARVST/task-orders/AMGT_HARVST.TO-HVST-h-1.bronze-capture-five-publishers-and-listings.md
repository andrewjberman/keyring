# AMGT_HARVST task order -- `HVST-h-1` -- H1: every publisher path keeps the bytes it RECEIVED (article and listing), captured at the session layer, and the ONE bronze writer puts them with `received-form`; CODE ONLY, stub sessions and a stub S3 client, no vendor call

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-h-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~1</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 2 armed gates estate-wide, 0 on lib/opal_data_harvest or any harvest surface (C1=23 C2=7 C3=12 C4=21 C5=334); this cell arms nothing.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; every S3 touch in the tests is a STUB client.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_HARVST~1`.** Work ONLY in the worktree whose absolute path is in your spawn prompt.
- **Your first act** prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that `org/`,
  `.tools/` and every EXISTING path in section 3 exist. If any is absent, STOP with a BLOCKING row.
- Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_HARVST~1;`.
- **NEVER RUN AN INSTALL. NEVER CALL A PUBLISHER, NEVER CALL AWS, NEVER RUN THE HARVESTER CLI.** Every network object
  in this cell is a stub you write.

## 1. THE CELL, inlined in full -- `HVST-h-1` (manifest row H1, outcome FWD-1)

**The contract, verbatim** (PRD v0.2 @9102ccfe81, `C-HV-BRONZE-AS-RECEIVED`):
> Every publisher's article response is stored as the bytes received, one object per fetch, under
> `{source}/harvest/bronze/article/article_hash=<sha256("<publisher_code>:<article_id>")>/<stamp>.<ext>`. [...] The form
> per publisher: Seeking Alpha, Bloomberg and Barron's: the JSON response. WSJ and FT: the HTML page. [...] The listing
> or search response that found the article is stored too, under `{source}/harvest/bronze/news_listing/date=<d>/...`.
> Each object records `received-form` in its S3 metadata.

**Outcome FWD-1, DONE WHEN:** *"for one run on the validation security, every article from each of the five publishers,
and the listing page that found it, is re-opened from our store and matches what was received, byte for byte"*. This
cell builds the capture. The live run is a later cell.

**THE MEASURED STATE at SITEZ @9fbf337a74** (re-read at your branch HEAD before editing):
- **No publisher keeps the bytes it received** (channel row `AMGT_HARVST-Z-S1`):
  - `publishers.py:216` (SA) and `:241` (Bloomberg) set `raw_bytes` to `json.dumps(<parsed JSON>)`, a
    re-serialisation.
  - `financial_times` (`:255-281`) and `DowJones.article` (`:343-374`) set no `raw_bytes` at all.
- The transport functions live OUTSIDE this package and return parsed JSON: `sa_rest_fetch.py:157` `news`, `:213`
  `article`; `bloomberg_rest_fetch.py:89` `search`, `:101` `article`. **You do NOT edit them.**
- **The one layer every publisher path passes through** is `lib/opal_data_harvest/transport.py:64-93`
  `PacedSession.get`, which holds each `response`. `Publisher.__init__` (`publishers.py:126-149`) wraps every
  publisher's session in it.
- **Listing and search responses are parsed and discarded on every path:**
  - SA `module.news` (`publishers.py:201`);
  - Bloomberg `module.search`, pages 1-3 (`:229`);
  - the FT search page (`:256`);
  - the Dow Jones `discover` search page (`:322`).
- **SA fetches no per-article response today.** It takes the body from the listing item.
- `harvest_grammar.put_article_bronze` (`harvest_grammar.py:70-81`) is the ONE article bronze writer. It calls
  `store.bronze_put` with no `metadata`.
- `store.bronze_put` (`lib/research/harvest/store.py:216-280`) accepts `metadata` keys in lowercase ASCII kebab-case
  (`_validate_bronze_metadata`, `:193-213`), so `received-form` is legal. `store.form_c_object` (`:129-133`) is the
  request form. `store.fetch_key_exists(source, request, partition, object_prefix=...)` (`:181-190`) is the dedupe read.
- `Worker._write_harvest_raw` (`worker.py:59-79`) writes a local `harvest_raw_outbox` row in harvest mode only
  (config key `harvest_grammar`, absent from `config.json`, so OFF).
- `HarvestUploader` (`uploads.py:103-162`) puts from that outbox.

**RULED -- what you build:**
1. **Capture at the session.** `PacedSession.get` appends, for every response it returns or raises on, a record
   `{"url": str(response.url), "status": response.status_code, "body": response.content, "fetched_at": <UTC ISO>}` to
   a list attribute `captured`. The event ledger stays unchanged (no bodies in it).
2. **Article bytes, per publisher.** The article dict `normalize` returns gains `raw_bytes` (the `body` of the ARTICLE
   response, from `captured`, byte for byte), `raw_ext` and `raw_url`:
   - `sa`: SA now fetches each NEW article (not known, not reused) by `self.module.article(self.session, id)`. The
     body of that GET is the raw. Its ext is `json`. The text fields keep coming from the listing item as today.
   - `bbg`: the `module.article` response. Ext `json`.
   - `barrons`: the articles-API response. Ext `json`.
   - `wsj`: the article-page response. Ext `html`.
   - `ft`: the article-page response. Ext `html`, on BOTH the JSON-LD and the last-resort branch.
   - A reused or cached article carries no `raw_bytes`, as today.
3. **Listing bytes.** `Publisher` exposes `listings`, a list reset at each `articles()` call. It gets one dict per
   listing or search GET: `{"publisher", "query", "page", "url", "fetched_at", "raw_bytes", "raw_ext"}`.
   - `query` is the exact query string the path sent: the SA symbol, the quoted Bloomberg query, or the FT or Dow
     Jones company.
   - `page` is 1-based.
4. **The bronze writers** in `harvest_grammar.py`:
   - `put_article_bronze(..., received_form="as_received")` passes `metadata={"received-form": received_form}`. The
     ONLY legal values are `as_received` and `normalised_record`; anything else raises `ValueError` before any call.
   - New `listing_query_hash(query)`, which is sha256 hex of the UTF-8 query.
   - New `put_listing_bronze(publisher_code, query, page, body, ext, fetched_at, client=None)`. The partition is
     `store.date_partition(<fetched_at UTC>)`. The object is `store.form_c_object(f"{qh}_p{page}_{store.stamp(fetched_at)}", ext)`.
     Before the put, `store.fetch_key_exists(source, "news_listing", partition, object_prefix=f"{qh}_p{page}_")` is
     checked; an existing key returns `{"skipped": True, "existing": [...]}`. Metadata is `received-form: as_received`.
5. **Harvest mode**:
   - `Worker` writes each captured listing to a local `harvest_listing_outbox` table, created if absent, in harvest
     mode only.
   - `_write_harvest_raw` stays the article path and now stores `raw_url`.
   - `HarvestUploader.run` puts pending listings through `put_listing_bronze`, and articles through
     `put_article_bronze(..., received_form="as_received")`.
   - The silver step of `HarvestUploader` is NOT this cell's. Leave it as it is; `HVST-h-2` rebuilds it.
6. **New test file** `lib/opal_data_harvest/test_bronze_capture.py`, with STUB inner sessions returning fixed bytes and a
   STUB S3 client. Reuse the stub-client pattern in `lib/research/harvest/tests/test_store.py`. Exactly these twelve
   arms:
   - `test_paced_session_captures_response_bytes`
   - `test_article_raw_bytes_are_response_body_sa`
   - `test_article_raw_bytes_are_response_body_bbg`
   - `test_article_raw_bytes_are_response_body_ft`
   - `test_article_raw_bytes_are_response_body_wsj`
   - `test_article_raw_bytes_are_response_body_barrons`
   - `test_listing_captured_for_each_discovery_call` (all five publishers, and every Bloomberg page)
   - `test_put_article_bronze_sets_received_form`
   - `test_put_article_bronze_refuses_unknown_received_form`
   - `test_put_listing_bronze_key_shape` (the key sits under `<source>/harvest/bronze/news_listing/date=<d>/`)
   - `test_put_listing_bronze_dedupes_on_fetch_key`
   - `test_harvest_mode_writes_listing_outbox`

   Each `raw_bytes` arm asserts EQUALITY with the stub server's body bytes. Make the stub body deliberately
   non-canonical JSON (extra spaces, non-sorted keys), so a re-serialisation would FAIL the arm.

**What this cell does NOT change:**
- `store.py`;
- the mention gate (`publishers.py` word-bounded relevance, the FLOOR);
- `normalize`'s other fields;
- the legacy `Uploader`;
- the CLI;
- `config.json`;
- any file outside section 3.

## 2. WHERE THIS CAME FROM
Round 1, decomposition v1.0 @9fbf337a74, chain A position 1 of 9. `HVST-h-2` (silver from bronze) is spawned only after
this cell drains VALID, and edits `harvest_grammar.py` and `uploads.py` after you.

## 3. SURFACES -- what you may read and write

<paths>
lib/opal_data_harvest/transport.py
lib/opal_data_harvest/publishers.py
lib/opal_data_harvest/harvest_grammar.py
lib/opal_data_harvest/worker.py
lib/opal_data_harvest/uploads.py
lib/opal_data_harvest/test_bronze_capture.py
lib/opal_data_harvest/test_harvest_grammar.py
lib/opal_data_harvest/test_worker.py
lib/opal_data_harvest/test_catalog.py
lib/opal_data_harvest/test_verification.py
lib/research/harvest/store.py
lib/research/harvest/tests/test_store.py
org/tier1_exec/4.0.0_SA_CRO/scripts/sa_rest_fetch.py
org/tier1_exec/4.0.0_SA_CRO/scripts/bloomberg_rest_fetch.py
org/tier1_exec/4.0.0_SA_CRO/scripts/ft_rest_fetch.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~1/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-h-1.bronze-capture-five-publishers-and-listings.md
</paths>

- **A surface not named in `<paths>` is a wall.**
- `store.py`, the tests you only run, and the three CRO scripts are READ-ONLY for you. AC3 fails if one changes.
- Scratch goes in `<your worktree>/.scratch/hv1/`.
- **Committing:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_HARVST~1 <0.9.0_WK_AMGT_HARVST~1@opal.agent>" -F <msgfile> -- <paths>`.
  Write the message file with a non-shell writer.

## 4. BOUNDS
- **CODE ONLY.** Every session and S3 client is a stub. Run each test FILE with its own pytest call.
- **The pin is `9fbf337a74`** for the measured state. AC3 diffs from your branch's fork point
  (`git merge-base HEAD SITEZ`), so it sees only this branch's own changes (row `AMGT_HARVST-Z-W1-S3`).
- **Pre-existing failures are not this cell's to fix, and their counts must not GROW:** `test_worker.py` 2 failed and
  `test_verification.py` 1 failed, both measured at the cut.
- **All new text is pure ASCII**, the code and the tests alike.
- **Surprise rows:** `AMGT_HARVST-Z-W1-S<k>`, with `disarm_owner` `2.0.0_SA_COO~Y`. File a row and keep working. A row
  that blocks a criterion is class `BLOCKING`.

## 5. PROOF OF SPEC (each invocation LITERAL; timeout 600)

Before AC3, write `.scratch/hv1/ac3.py`:
```
import subprocess
allowed = {"lib/opal_data_harvest/transport.py", "lib/opal_data_harvest/publishers.py", "lib/opal_data_harvest/harvest_grammar.py", "lib/opal_data_harvest/worker.py", "lib/opal_data_harvest/uploads.py", "lib/opal_data_harvest/test_bronze_capture.py"}
base = subprocess.run(["git", "merge-base", "HEAD", "SITEZ"], capture_output=True, text=True).stdout.strip()
print("fork_base", base)
out = subprocess.run(["git", "diff", "--name-only", base, "HEAD", "--", "lib", "integrations", "infra", ".tools", "portal", "org/tier1_exec"], capture_output=True, text=True).stdout.split()
print("changed_code_files", sorted(out))
print("outside_allowed", sorted(set(out) - allowed))
for f in sorted(x for x in out if x.endswith(".py")):
    b = open(f, "rb").read()
    compile(b.decode("utf-8"), f, "exec")
    print(f, "compiles True crlf", b.count(bytes([13, 10])), "non_ascii_chars", sum(1 for ch in b.decode("utf-8") if ord(ch) > 127))
```

<proof_of_spec>
  <criterion id="AC0" cell_refs="HVST-h-1"><invocation>cd "$(git rev-parse --show-toplevel)" && for t in lib/opal_data_harvest/test_harvest_grammar.py lib/opal_data_harvest/test_worker.py lib/opal_data_harvest/test_catalog.py lib/opal_data_harvest/test_verification.py lib/research/harvest/tests/test_store.py; do echo "$t :: $(python -m pytest $t -q --color=no -p no:cacheprovider 2>&1 | tail -1)"; done</invocation><expect>BEFORE any edit, five baseline lines recorded; measured at the cut: 7 passed; 2 failed, 18 passed; 5 passed; 1 failed, 3 passed; 11 passed</expect></criterion>
  <criterion id="AC1" cell_refs="HVST-h-1"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/opal_data_harvest/test_bronze_capture.py -v --color=no -p no:cacheprovider 2>&1 | tail -16</invocation><expect>"12 passed" and no "failed" -- the twelve arms named in section 1 item 6, each raw_bytes arm asserting equality with a non-canonical stub body</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-h-1"><invocation>cd "$(git rev-parse --show-toplevel)" && for t in lib/opal_data_harvest/test_harvest_grammar.py lib/opal_data_harvest/test_worker.py lib/opal_data_harvest/test_catalog.py lib/opal_data_harvest/test_verification.py lib/research/harvest/tests/test_store.py; do echo "$t :: $(python -m pytest $t -q --color=no -p no:cacheprovider 2>&1 | tail -1)"; done</invocation><expect>each line's passed and failed counts EQUAL its AC0 line (the timing suffix may differ): no new failure and no pre-existing failure removed</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-h-1"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/hv1/ac3.py</invocation><expect>"outside_allowed []"; every changed file "compiles True crlf 0 non_ascii_chars 0" (every edited file is pure ASCII at the pin, measured at the cut)</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR.** No judgment criterion.

## 6. WHEN YOU ARE DONE
1. Write the instance to
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~1/AMGT_HARVST.TO-HVST-h-1.bronze-capture-five-publishers-and-listings.proof_of_spec.json`.
2. Grade it with `python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3`, which must return rc 0.
3. Flip `<status>` to `complete` ONLY if every criterion passes.
4. Commit with `--only`.
5. Report once.

**MUTATION DISCIPLINE:** snapshot the working-tree bytes of every file you edit to `.scratch/hv1/` first. Never
`git checkout --`, `stash` or `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**
1. **Why the session layer.** Row `-Z-S1`: the transport functions return parsed JSON, and they are the CRO's scripts,
   not this project's. Capturing at `PacedSession.get` gives byte-for-byte bodies on all five paths without editing a
   foreign file.
2. **The SA per-article GET is a NEW vendor call per NEW SA article.** `HVST-h-3`'s plan counts it. It is how "the
   JSON response" in the contract is met for SA, and the only source of the article-level fields gold needs.
3. **The received-form enum** (`as_received | normalised_record`) is the decomposition's s.2 record.
   `normalised_record` is written only by `HVST-h-9`.
4. **CHAINED:** `HVST-h-2` edits `harvest_grammar.py` and `uploads.py` after this cell drains.

<status>pending</status>
<round>1</round>
<slot>~1</slot>
<fabric>site-z</fabric>
