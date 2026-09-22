# AMGT_HARVST task order -- `HVST-h-3` -- H3: discovery records its rung and search provenance, pages back to the later of the 2026-01-01 FLOOR and the WATERMARK, dedupes BEFORE any vendor call (articles and listings), prints a zero-network PLAN, and can refuse the network outright; CODE ONLY, stubs, no vendor call

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-h-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~3</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on any harvest surface (C1=23 C2=7 C3=12 C4=21 C5=334); this cell arms nothing.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; every S3 touch in the tests is a STUB client.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_HARVST~3`.** Work ONLY in the worktree whose absolute path is in your spawn prompt.
- **Your first act** prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that `org/`,
  `.tools/`, every EXISTING path in section 3, `lib/opal_data_harvest/test_bronze_capture.py`,
  `lib/opal_data_harvest/silver_from_bronze.py` and `lib/opal_data_harvest/test_legacy_upload.py` exist.
  - The last three are the predecessor cells'. If any is absent, STOP with a BLOCKING row.
- Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_HARVST~3;`.
- **NEVER RUN AN INSTALL. NEVER CALL A PUBLISHER, NEVER CALL AWS, NEVER RUN `run` OR `upload-*` FROM THE CLI.**
- The new `plan` command MAY be run: it makes no network call by construction, and AC5 proves that.

## 1. THE CELL, inlined in full -- `HVST-h-3` (manifest row H3, outcomes FWD-3 and FWD-9)

**The contract, verbatim** (PRD v0.2 @9102ccfe81, `C-HV-RETRIEVAL-PROVENANCE`):
- Every silver row states `retrieval_rung` (`symbol_listing | name_search | ticker_search`), `search_query`,
  `search_rank` and `search_page`.
- A publisher's own per-symbol listing is used wherever one exists and works.
- A search pages back to the later of the FLOOR (2026-01-01) and the newest `published_utc` already held for that
  (security, publisher), the WATERMARK.
- Dedupe is by `article_hash`, so a known article is never fetched twice.
- **The mention floor is unchanged:** one word-bounded mention of the company keeps the article. Retrieval never grades.

**And `C-DEDUPE-BY-KEY`, as PRD v0.2 binds it:** before any vendor call, the writer checks the bucket for the fetch key.
- `article`: fetch key = `article_hash`.
- `listing`: fetch key = (source, query sha256, UTC date, page).

**Outcome FWD-3, DONE WHEN:** *"every stored article states whether it came from the publisher's own list for that
company or from a search, with the search words and its position in the results; a second run the same day fetches no
article we already hold"*.

**Outcome FWD-9 (this cell's part):** *"the number of listing pages each publisher would be asked for was printed before
the run"*.

**THE MEASURED STATE at SITEZ @9fbf337a74** (re-read at your branch HEAD; `HVST-h-1`, `HVST-h-2` and `HVST-h-9` have
edited the package since):
- **Discovery cannot backfill today:**
  - `config.json` sets `articles_per_security: 5` and `candidate_limit: 20`, and `Worker.run_job` stops at `target`
    accepted.
  - The FT search (`publishers.py` `financial_times`) and the Dow Jones `discover` each read ONE search page.
  - Bloomberg reads pages 1-3 (`bloomberg`).
  - SA reads one `news` call (`sa_rest_fetch.py:157`, `page[size]=limit`, no page number).
- The SA transport module exposes `get_json(s, path, referer)` (`sa_rest_fetch.py`). Call it with your own path to page.
  **Do not edit the module.**
- `harvest_grammar.article_known` is the article dedupe read. It is used in harvest mode for non-reused articles
  (`worker.py`).
- **The mention floor** is the word-bounded company relevance check inside `publishers.py` `normalize` (`:76-122` at
  the pin; the handoff cites `:99-105`). **You do not edit it.** AC4 proves it is byte-identical.
- The CLI (`__main__.py`) commands after `HVST-h-9` are: `run status universe import-session migrate upload
  upload-legacy upload-harvest`.
- The security comes from `pilot_securities` or the universe (`--tickers`). There is no way to pass a one-off security.

**RULED -- what you build:**
1. **Rungs and provenance.** Every discovered article carries `discovery = {"retrieval_rung", "search_query",
   "search_rank", "search_page", "first_discovered_at", "discovered_for": [security_key]}`:
   - `sa` is `symbol_listing`. Bloomberg's per-symbol probe (item 6) is `symbol_listing`.
   - `bbg`, `ft`, `wsj` and `barrons` searches are `name_search`.
   - `ticker_search` is reserved in the enum and emitted by no path in this round.
   - The discovery dict rides through the harvest outbox to `HarvestUploader`, which passes it to
     `silver_from_bronze.article_rows(discovery=...)`.
2. **Paging to a bound.**
   - `config.json` gains `backfill_floor: "2026-01-01"` and a per-publisher `max_listing_pages` (working caps: `sa` 25,
     `bbg` 25, `ft` 25, `wsj` 25, `barrons` 25).
   - The bound for (security, publisher) is `max(floor, watermark)`.
   - Each publisher pages through a documented `PAGE_PARAM` table: `sa` `page[number]`; `bbg` `page`; `ft` `page`
     plus `sort=date`; `wsj` and `barrons` `page`. Each entry is flagged `verified: False` until a live run measures
     it.
   - **Paging stops at the FIRST of:**
     - every hit on the page dated older than the bound;
     - an empty page;
     - a page whose hit set repeats the previous page's (a param the site ignores);
     - `max_listing_pages`.
   - The stop reason is recorded per publisher.
   - In backfill mode, `articles_per_security` and `candidate_limit` do NOT cap acceptance.
3. **The watermark.** `watermark(security_key, publisher_code, client=None)` is the newest `published_utc` among silver
   `article` rows of that publisher whose `discovered_for` holds the security. It reads through
   `store.silver_latest`, and returns None when nothing is held.
4. **Dedupe before the vendor call:**
   - `article_known` is checked for EVERY new article on every path, before its article GET (including the SA
     per-article GET that `HVST-h-1` added).
   - Before any listing GET, the listing fetch key is checked. If it is held, the stored bronze body is read (a new
     `harvest_grammar.get_listing_bronze`) and used instead of the GET.
   - **The publisher session opens LAZILY, at the first real GET.** So a run whose every needed listing page and
     article is held opens no session and makes no call.
5. **The network refuser.** With env `HARVEST_REFUSE_NETWORK=1`, `PacedSession.get` and session construction raise
   `RuntimeError("network refused")` BEFORE any I/O. The run records any refusal it hit.
6. **Bloomberg's per-symbol probe.** A function `bbg_symbol_news_probe(publisher, security)` calls the transport's
   `news(s, symbol, name)` ONCE (`bloomberg_rest_fetch.py:119-123`), captures the listing like any other, and returns
   `{"status", "items", "adoptable": <bool>}`. It is called ONLY by a run with `--bbg-symbol-probe`, and never in this
   cell.
7. **The CLI:**
   - `plan --publishers ... (--tickers ... | --security-json FILE) [--floor D] [--retrieval-mode backfill|live]` prints
     one JSON line per publisher `{"publisher", "bound", "max_listing_pages", "planned_listing_pages", "watermark_source"}`
     and a total. It makes NO network call: the watermark is read only when `--with-watermark` is passed, and that is
     never passed in this cell.
   - `run` gains `--security-json FILE` (one security object `{"key", "ticker", "company", "aliases", "sa_symbol"}`),
     `--floor`, `--retrieval-mode` and `--bbg-symbol-probe`.
   - Harvest mode is set with `--harvest-grammar`, never by editing `config.json`'s default.
8. **New test file `lib/opal_data_harvest/test_retrieval_provenance.py`,** with STUB sessions and a STUB S3 client.
   Exactly twelve arms:
   - `test_rung_recorded_per_publisher`
   - `test_search_provenance_query_rank_page`
   - `test_paging_stops_at_floor`
   - `test_paging_stops_at_watermark`
   - `test_paging_stops_on_repeat_page`
   - `test_paging_stops_at_max_pages`
   - `test_article_dedupe_before_vendor_call_every_publisher`
   - `test_listing_dedupe_replays_bronze_without_network`
   - `test_second_same_day_run_makes_zero_vendor_calls` (the refuser is set and the run completes with 0 http events)
   - `test_network_refuser_raises_before_io`
   - `test_plan_prints_counts_with_zero_network`
   - `test_bbg_symbol_probe_captures_listing`

**What this cell does NOT change:**
- the mention floor;
- `store.py`;
- the CRO transport scripts;
- the legacy `Uploader`;
- the bronze and silver builders' outputs for a given input.

## 2. WHERE THIS CAME FROM
Round 1, decomposition v1.0 @9fbf337a74, chain A position 4 of 9. After `HVST-h-9`. **`HVST-h-10` (the one live Lenovo
run) is spawned only after this cell drains VALID, and runs on exactly what you build.**

## 3. SURFACES -- what you may read and write

<paths>
lib/opal_data_harvest/publishers.py
lib/opal_data_harvest/transport.py
lib/opal_data_harvest/worker.py
lib/opal_data_harvest/harvest_grammar.py
lib/opal_data_harvest/uploads.py
lib/opal_data_harvest/__main__.py
lib/opal_data_harvest/config.json
lib/opal_data_harvest/test_retrieval_provenance.py
lib/opal_data_harvest/silver_from_bronze.py
lib/opal_data_harvest/test_bronze_capture.py
lib/opal_data_harvest/test_silver_from_bronze.py
lib/opal_data_harvest/test_legacy_upload.py
lib/opal_data_harvest/test_harvest_grammar.py
lib/opal_data_harvest/test_worker.py
lib/opal_data_harvest/test_catalog.py
lib/opal_data_harvest/test_verification.py
lib/research/harvest/store.py
lib/research/harvest/tests/test_store.py
org/tier1_exec/4.0.0_SA_CRO/scripts/sa_rest_fetch.py
org/tier1_exec/4.0.0_SA_CRO/scripts/bloomberg_rest_fetch.py
org/tier1_exec/4.0.0_SA_CRO/scripts/ft_rest_fetch.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~3/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-h-3.retrieval-rungs-provenance-watermark-and-plan.md
</paths>

- **A surface not named in `<paths>` is a wall.** `store.py`, the tests you only run and the CRO scripts are READ-ONLY.
- Scratch goes in `<your worktree>/.scratch/hv3/`.
- **Committing:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_HARVST~3 <0.9.0_WK_AMGT_HARVST~3@opal.agent>" -F <msgfile> -- <paths>`.

## 4. BOUNDS
- **CODE ONLY.** No network. `plan` runs with `HARVEST_REFUSE_NETWORK=1` in AC5, so any call would FAIL it.
- **The working caps** (`max_listing_pages` 25 each) and the `PAGE_PARAM` table are defaults, stated in your report,
  never findings.
- **Pre-existing test failures must not GROW.**
- **All new text is pure ASCII.**
- **Surprise rows:** `AMGT_HARVST-Z-W3-S<k>`, with `disarm_owner` `2.0.0_SA_COO~Y`.

## 5. PROOF OF SPEC (each invocation LITERAL; timeout 600)

Write two scratch files first.

`.scratch/hv3/ac4.py`:
```
import subprocess
pin = subprocess.run(["git", "show", "9fbf337a74:lib/opal_data_harvest/publishers.py"], capture_output=True, text=True).stdout.splitlines()
block = pin[98:105]
head = open("lib/opal_data_harvest/publishers.py", encoding="utf-8").read().splitlines()
found = any(head[i:i + len(block)] == block for i in range(len(head)))
print("pin_block_lines", len(block), "present_verbatim_in_head", found)
```

`.scratch/hv3/lenovo_probe.json`:
`{"key": "992_HK_Equity", "ticker": "992_HK_Equity", "company": "Lenovo Group", "aliases": ["Lenovo"], "sa_symbol": "LNVGY"}`

<proof_of_spec>
  <criterion id="AC0" cell_refs="HVST-h-3"><invocation>cd "$(git rev-parse --show-toplevel)" && for t in lib/opal_data_harvest/test_bronze_capture.py lib/opal_data_harvest/test_silver_from_bronze.py lib/opal_data_harvest/test_legacy_upload.py lib/opal_data_harvest/test_harvest_grammar.py lib/opal_data_harvest/test_worker.py lib/opal_data_harvest/test_catalog.py lib/opal_data_harvest/test_verification.py; do echo "$t :: $(python -m pytest $t -q --color=no -p no:cacheprovider 2>&1 | tail -1)"; done</invocation><expect>BEFORE any edit, seven baseline lines recorded; the three predecessor files read 12, 14 and 6 passed</expect></criterion>
  <criterion id="AC1" cell_refs="HVST-h-3"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/opal_data_harvest/test_retrieval_provenance.py -v --color=no -p no:cacheprovider 2>&1 | tail -16</invocation><expect>"12 passed" and no "failed" -- the twelve arms named in section 1 item 8</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-h-3"><invocation>cd "$(git rev-parse --show-toplevel)" && for t in lib/opal_data_harvest/test_bronze_capture.py lib/opal_data_harvest/test_silver_from_bronze.py lib/opal_data_harvest/test_legacy_upload.py lib/opal_data_harvest/test_harvest_grammar.py lib/opal_data_harvest/test_worker.py lib/opal_data_harvest/test_catalog.py lib/opal_data_harvest/test_verification.py; do echo "$t :: $(python -m pytest $t -q --color=no -p no:cacheprovider 2>&1 | tail -1)"; done</invocation><expect>each line's passed and failed counts EQUAL its AC0 line</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-h-3"><invocation>cd "$(git rev-parse --show-toplevel)" && git diff --name-only 9fbf337a74 HEAD -- lib/research org/tier1_exec && echo "--- end of forbidden-surface diff" && for f in lib/opal_data_harvest/test_retrieval_provenance.py lib/opal_data_harvest/publishers.py lib/opal_data_harvest/__main__.py; do python -c "import sys;b=open(sys.argv[1],'rb').read();compile(b.decode('utf-8'),sys.argv[1],'exec');print(sys.argv[1],'crlf',b.count(bytes([13,10])),'non_ascii',sum(1 for c in b.decode('utf-8') if ord(c)>127))" $f; done</invocation><expect>NOTHING printed before "--- end of forbidden-surface diff" (store.py and the CRO scripts unchanged since the pin), then three lines each "crlf 0 non_ascii 0"</expect></criterion>
  <criterion id="AC4" cell_refs="HVST-h-3"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/hv3/ac4.py</invocation><expect>"pin_block_lines 7 present_verbatim_in_head True" -- the mention floor's lines at the pin appear verbatim in HEAD</expect></criterion>
  <criterion id="AC5" cell_refs="HVST-h-3"><invocation>cd "$(git rev-parse --show-toplevel)" && HARVEST_REFUSE_NETWORK=1 python -m lib.opal_data_harvest plan --publishers sa bbg ft wsj barrons --security-json .scratch/hv3/lenovo_probe.json --floor 2026-01-01 --retrieval-mode backfill</invocation><expect>five per-publisher JSON lines each carrying "bound": "2026-01-01" and an integer "planned_listing_pages", plus a total line, and NO "network refused" anywhere in the output</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR.** No judgment criterion.

## 6. WHEN YOU ARE DONE
1. Write the instance to
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~3/AMGT_HARVST.TO-HVST-h-3.retrieval-rungs-provenance-watermark-and-plan.proof_of_spec.json`.
2. Grade it with `python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4,AC5`, which must return rc 0.
3. Flip to `complete` only if all pass.
4. Commit with `--only`.
5. Report once. Your report NAMES:
   - the exact `run` flags that `HVST-h-10` must use;
   - the `PAGE_PARAM` table;
   - the caps.

**MUTATION DISCIPLINE:** snapshot the working-tree bytes to `.scratch/hv3/` first. Never `git checkout --`, `stash` or
`git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**
1. **The page caps (25 per publisher) bound the one Lenovo run's cost.** `HVST-h-10` prints the plan before any call,
   under the trial word's "cost printed first".
2. **The PAGE_PARAM table is flagged unverified on purpose.** The repeat-page stop makes a wrong parameter cost one
   page, not a loop.
3. **AC4 pins the floor by content, not by line number.** The worker edits `publishers.py` above those lines, so the
   line numbers move.
4. **The Lenovo probe JSON is the issuer's working identity for the plan only.** `HVST-h-10` resolves Lenovo's real
   record and measures the SA ADR symbol.

<status>pending</status>
<round>1</round>
<slot>~3</slot>
<fabric>site-z</fabric>
