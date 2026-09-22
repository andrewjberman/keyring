# AMGT_RESAPP task order -- `AMGT-rk-98` -- B2 WIRING: the four filings fetch sites hand their fetched bytes, UNPARSED, to the rk-84 bronze writers through an opt-in sink that is OFF by default; `batch.py` gains a per-name selector; CODE ONLY, 0 live writes

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-98</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~98</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order edits three library modules and adds one test file; it arms no
  cron, alarm, monitor or cadence, reads no schedule and writes none. The DISABLED `OpalResearch-FilingsAnalyzer`
  Windows task is neither read nor changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant is read or changed; no AWS call of any kind is made by
  this order (every test uses a stub S3 client and a stub `http_get`).
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~98`.** Work ONLY in the worktree whose absolute path is given in your spawn prompt. Your
first act prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that `org/`, `.tools/`
and the paths in section 3 exist (the new test file excepted); if any is absent, STOP with a BLOCKING row. Every Bash
call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~98;`. **NEVER RUN AN INSTALL.** Never read, show, diff or
check out branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50` -- it holds an exposed credential.

## 1. THE CELL, inlined in full -- `AMGT-rk-98` (round 25, ahead of the B2 run)

**The ruling of record, verbatim** (1.0.0_SA_CTO~Z msg 24189, 2026-09-22T10:47:03Z, file
`org/mcp/inbox/2.0.0_SA_COO/~Z/read/20260922T104703Z_1.0.0_SA_CTO_Z_Re_24188__all_3_calls_RULED_as_recommend.md`,
lines 9-12):

> CALL 1 (B2 wiring): RULED IN, round 25.
> - Route battery.py:567 / :639 / :1001 and fetch.py:320 through the rk-84 writers, passing the fetched bytes through
> unparsed. Add a per-name selector to batch.py.
> - Ticker-table filename: the SEC's own name, company_tickers.json. C-BRONZE-AS-RECEIVED form (c) keeps the vendor
> file name, and sec_ticker_cik_cache.json was our cache's name, not the vendor's.
> - PAIR: NOT needed for the wiring cell. It is code only, with every writer off by default and 0 live writes, and a
> test proves 0 S3 calls. The RUN cell that later writes filing bronze and silver carries its own pair.

**Why this cell exists:** a "run B2" today would write NOTHING new. The rk-84 bronze writers have ZERO production
callers, and every live fetch site parses the bytes and discards them (the census below).

**THE MEASURED STATE, at `4183e30531` (SITEZ; `lib/` and `integrations/` byte-identical to `7fa3268fd0`). RE-READ every
line at your branch HEAD before editing:**

- **The four fetch sites** (each a `bytes` value that is parsed and never stored):
  - `lib/research/filings/battery.py:567` -- `_sec_ticker_table(http_get, timeout)`:
    `data, status, error = _call_http_get(http_get, _TICKERS_URL, ...)`, then `json.loads(data.decode("utf-8"))` at
    `:570`. `_TICKERS_URL` (`:563`) is `https://www.sec.gov/files/company_tickers.json`. Called only from
    `_step1_edgar_ticker` (`:661`).
  - `battery.py:639` -- `_fetch_and_accept_edgar(located, keys, run_date, http_get, timeout)`: the primary document,
    then `fetch.html_to_text(data)` at `:642`. Called from `_step1_edgar_ticker` (`:705`) and
    `_step2_edgar_bloomberg_cik` (`:741`). `located` carries `accession`, `primary_document` and `url`, but NOT the cik:
    step 1 holds it as `cik = match.get("cik_str")` (`:693`) and step 2 as `cik = keys.get("cik")` (`:724`).
  - `battery.py:1001` -- inside `_step4_company_site`'s crawl loop: `data, status, error = _call_http_get(http_get, url,
    timeout=60)`. The SAME call fetches both NAVIGATION pages (links harvested at `:1040`) and DOCUMENTS (the branch at
    `:1010`, `item["type"] == "candidate" or is_pdf`, where `sha = _sha256(data)` at `:1011`). A document winner's id is
    `"doc-%s" % winner["sha256"][:16]` (`:1111`).
  - `lib/research/filings/fetch.py:320` -- `build_source_object`'s EDGAR-by-CIK path (`battery is None`):
    `raw = http_get(located["url"], timeout=timeout)`, then `html_to_text(raw)` at `:321`. `cik` is the function's own
    argument. This is the path `batch.py:338` (`run_group`) takes.
- **The rk-84 writers** (`lib/research/harvest/filings.py`, UNCHANGED by this order):
  - `bronze_sec_filing(cik, accession, vendor_file_name, body, content_type="text/html", client=None)` (`:101`);
  - `bronze_issuer_document(security_key, document_id, vendor_file_name, body, content_type="application/pdf",
    client=None)` (`:115`);
  - `bronze_sec_company_tickers(fetched_at, body, object_name, client=None)` (`:140`). `object_name` is REQUIRED; the
    CTO has now ruled it `company_tickers.json`.
  - Each goes through `_as_received` (`:77`, bytes only, else `TypeError`) and `store.bronze_put` (the conditional
    never-overwrite put: identical bytes are a no-op, different bytes are `BronzeImmutableError`).
  - `bronze_esef_filing` (`:131`) is NOT in the ruling. The step-3 ESEF site (`battery.py:834`) fetches a JSON INDEX of
    filings, not a filing document, and step 3's acceptance path is unexercised. It stays unwired.
- **Production-caller census of the three writers above** (`git grep`, non-test, excluding `harvest/filings.py` itself): **0**.
  `harvest/filings.py` is imported LAZILY inside functions by `fetch.persist` (`:433`) and `batch.py` (`:345`, `:566`).
  Keep that style (a lazy import inside the call), so importing `fetch` or `battery` never loads the harvest store.
- **`batch.py`** (581 lines): `main` (`:419`) takes `--universe` (a whole U-1 document), `--limit`, `--dry-run`,
  `--plan-only`, `--write-pool`, `--skip-fetch`. There is NO per-name selector. `plan()` (`:149`) builds `fetch_groups`
  (deduped by CIK) and `unresolved` from the whole document.
- **Tests at the cut** (one pytest call per directory): `lib/research/filings/tests` **79 passed**;
  `lib/research/harvest/tests` **64 passed**; `test_battery.py` **22**; `test_batch.py` **11**.
- **Encoding at the cut:** `battery.py`, `fetch.py` and `batch.py` are each 0 CRLF and 0 non-ASCII characters.

**ISSUER RULINGS (L5), what you build:**

1. **The sink.** In `lib/research/filings/fetch.py`, add a small public class `BronzeSink`: `__init__(self,
   client=None, fetched_at=None)`, where `fetched_at` defaults to `datetime.datetime.now(datetime.timezone.utc)` at
   construction. Add a constant `SEC_TICKER_TABLE_FILE = "company_tickers.json"`. The sink has three methods, each a
   thin call into the rk-84 writer through a LAZY `from lib.research.harvest import filings as hf` inside the method:
   - `ticker_table(body)` -> `hf.bronze_sec_company_tickers(self.fetched_at, body, SEC_TICKER_TABLE_FILE, client=self.client)`;
   - `sec_filing(cik, accession, primary_document, body)` -> `hf.bronze_sec_filing(cik, accession, primary_document,
     body, content_type=<"application/pdf" if body starts b"%PDF" else "text/html">, client=self.client)`;
   - `issuer_document(security_key, document_id, vendor_file_name, body)` -> `hf.bronze_issuer_document(...)`, with the
     same content_type rule.
   Each method returns the writer's receipt and hands `body` through UNCHANGED: never decoded, re-encoded, sliced or
   copied into a new object.
2. **OFF BY DEFAULT.** Every function below gains a keyword `bronze_sink=None`. With `None`, the code path is
   byte-for-byte today's behaviour, and not one writer or store function is reached.
   - `fetch.build_source_object(..., bronze_sink=None)`: at `:320`, after `raw` is fetched and BEFORE `html_to_text`,
     `if bronze_sink is not None: bronze_sink.sec_filing(cik, located["accession"], located["primary_document"], raw)`.
     The battery path (`battery is not None`) passes nothing, because the battery writes its own.
   - `battery.run_battery(..., bronze_sink=None)` threads the sink into steps 1, 2 and 4 (not 3 or 5).
   - `:567`: `_sec_ticker_table(http_get, timeout, bronze_sink=None)` hands `data` to `bronze_sink.ticker_table(data)`
     BEFORE `json.loads`.
   - `:639`: `_fetch_and_accept_edgar(located, keys, run_date, http_get, timeout, cik=None, bronze_sink=None)` hands
     `data` to `bronze_sink.sec_filing(cik, located["accession"], located["primary_document"], data)` BEFORE
     `html_to_text`. Steps 1 and 2 pass their own `cik`.
   - `:1001`: ONLY in the DOCUMENT branch (`item["type"] == "candidate" or is_pdf`), after `sha` is computed and BEFORE
     text extraction:
     `bronze_sink.issuer_document(security_key, "doc-%s" % sha[:16], <vendor file name>, data)`.
     The vendor file name is the URL path's last segment, percent-decoded, with the query string dropped; if it is
     empty, use `"document"`. NAVIGATION PAGES ARE NOT BRONZE: a crawled page whose links are harvested is never
     written. The document id MUST equal the id `:1111` gives a winner, so a winner's bronze and its source object
     name the same document.
   - A writer exception PROPAGATES. It is never caught, logged-and-continued, or turned into a failed attempt.
3. **The CLI flags, both default OFF:**
   - `battery.main` gains `--write-bronze` (`store_true`), which builds `fetch.BronzeSink()` and passes it to
     `run_battery`.
   - `batch.main` gains `--write-bronze` (`store_true`), which builds one `fetch.BronzeSink()` for the run and passes
     it through `run_group(group, write_pool, client=None, caller=None, bronze_sink=None)` into
     `fetch.build_source_object(..., bronze_sink=bronze_sink)`.
   - Neither flag implies the other: `--write-pool` stays the silver/state switch, and `--write-bronze` the bronze
     switch.
4. **The per-name selector:** `batch.main` gains `--security-key` (`action="append"`, repeatable).
   - When given, AFTER `plan()` and BEFORE any print of WOULD-FETCH, keep only the `fetch_groups` whose
     `security_keys` intersect the named set (a group keeps only its named members) and only the named `unresolved`
     entries. Recompute every printed denominator from the FILTERED plan.
   - A named key that appears in neither partition is refused: `parser.error("--security-key not in the universe:
     <keys>")`, before any fetch.
   - With no `--security-key`, the plan is exactly today's.
5. **Tests**, in ONE new file `lib/research/filings/tests/test_bronze_wiring.py` (pytest style, QUALIFIED imports
   `lib.research.filings.battery` / `lib.research.filings.fetch` / `lib.research.filings.batch` /
   `lib.research.harvest.filings` / `lib.research.harvest.store`, W85-S1). Each test uses a STUB S3 client that counts
   `put_object` / `head_object` calls and answers them, and a stub `http_get` serving fixed bytes. **No network, no
   boto3 client is constructed.** Names must match AC1:
   - `test_default_off_makes_zero_store_calls` -- `run_battery` over a stubbed step-1 win and `fetch.build_source_object`
     over a stubbed EDGAR path, both with NO sink: `store.bronze_put` is monkeypatched to raise if called and is
     called 0 times; the stub client records 0 calls.
   - `test_ticker_table_bytes_reach_the_writer_unparsed` -- with a sink on the stub client: the ONE ticker-table put's
     body equals the exact bytes `http_get` returned, its key ends
     `company_tickers.json`, and it sits under a `date=` partition.
   - `test_sec_filing_bytes_reach_the_writer_unparsed` -- the step-1 primary-document put's body equals the fetched
     bytes, and its key carries `cik=<10 digits>` and `<accession>/<primary_document>`.
   - `test_issuer_document_bytes_reach_the_writer_unparsed` -- a stubbed step-4 crawl: one navigation page linking to
     one candidate PDF. Exactly ONE put (the PDF, never the page); its body equals the fetched PDF bytes; its
     document id equals `doc-` plus the first 16 hex characters of the PDF's sha256.
   - `test_fetch_build_source_object_writes_the_raw_filing` -- the `fetch.py:320` path with `latest_filing` and
     `http_get` monkeypatched: one put, body equal to the fetched bytes.
   - `test_writer_error_propagates` -- a sink whose client raises on `put_object` makes `run_battery` raise, never
     return an attempt.
   - `test_batch_security_key_selector_filters_and_refuses` -- over an in-memory universe of three names: selecting one
     key plans one group and prints denominators over one name; an unknown key exits via `parser.error`; no
     `--security-key` plans all three; `--write-bronze` defaults False on both CLIs.

**What this cell does NOT change:** `lib/research/harvest/filings.py` and `store.py` (WALLS); `analyze.py`; `document.py`;
step 3 (ESEF) and step 5; the navigation-page crawl; `fetch.persist`; the silver and state writers; any S3 object; the
DISABLED Windows task. No network call, no model call, no AWS call.

## 2. WHERE THIS CAME FROM

**ROUND 25**, decomposition s.33 (cut by `2.0.0_SA_COO~Z`), on the CTO's msg 24189 (answering the COO's msg 24188, the
three calls found while drafting the backfill cells) plus the round-24 analysis (msg 24182, `ledger/ROUND_ANALYSIS.round24.md`).
The B2 RUN cell rides behind this one, on Andrew's per-use word and its own pair. Andrew-direct ~15:12Z governs
one-slug issuance.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/filings/fetch.py
lib/research/filings/battery.py
lib/research/filings/batch.py
lib/research/filings/tests/test_bronze_wiring.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~98/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-98.b2-filings-bronze-wiring.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** Reads need no grant. In particular, `lib/research/harvest/**` and
  every existing test file are walls: if an existing test must change to stay green, STOP and REFUSE with a row.
  Scratch is `<your worktree>/.scratch/r98/` only, never committed. The only shared file is `INVESTIGATION_v1.md`
  (append-only; do not isolate it).
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~98 <0.9.0_WK_AMGT_RESAPP~98@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by the Write tool). Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

**CODE ONLY.** No network call, no EDGAR or issuer-site fetch, no model call, no AWS call of any kind, and no deploy.
Never run `battery.main`, `batch.main` or `fetch.main` against the live network, with or without `--write-bronze`.
- **Imports in tests use the QUALIFIED `lib.<pkg>.<mod>` names** (W85-S1).
- **Run each test directory in its OWN pytest call.** A multi-directory call trips the W85-S1 module-identity clash.
- **A script that carries a backslash is a FILE** you write from this order's text verbatim, never an inline
  `python -c` (W84-S1). Every script below is a file.
- **The discriminating comparison is pinned to commit `4183e30531`** (Z-S193), never HEAD or a merge-base.
- **THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
  repaired, widened, or satisfied by a route this order did not name, and never by editing a WALL.
- **A COUNT BAR IS READ AT SPAWN AND PRINTS its denominator.** AC0 re-measures every baseline before you edit; every
  later bar is "AC0's value plus N" or "equal to AC0's value", never a number typed here.
- **SURPRISE ROWS:** `AMGT_RESAPP-Z-W98-S<k>`, with `<k>` from 1; `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`.
  Append by textual splice inside the one fenced JSON array; never edit an existing row. A worker names the issuer
  (`2.0.0_SA_COO~Z`) as `disarm_owner`.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 600)

**Script files.** Write each block below to the named file under `<your worktree>/.scratch/r98/`, byte-for-byte, then
run it from the worktree root as the criterion states.

`.scratch/r98/ac0.py`:
```
import subprocess
def run(args):
    return subprocess.run(args, capture_output=True, text=True).stdout
print("pin_object", run(["git", "cat-file", "-t", "4183e30531"]).strip())
bat = open("lib/research/filings/battery.py", "rb").read().decode("utf-8").splitlines()
fet = open("lib/research/filings/fetch.py", "rb").read().decode("utf-8").splitlines()
for n in (567, 639, 1001):
    print("battery_%d" % n, bat[n - 1].strip())
print("fetch_320", fet[319].strip())
writers = ["bronze_sec_filing", "bronze_issuer_document", "bronze_sec_company_tickers"]
hits = []
for w in writers:
    for line in run(["git", "grep", "-n", w + "(", "--", "lib", "integrations", "data", ".tools"]).splitlines():
        path = line.split(":", 1)[0]
        if path != "lib/research/harvest/filings.py" and "/tests/" not in path:
            hits.append(line.split(":", 2)[0] + ":" + line.split(":", 2)[1])
print("production_writer_calls", len(hits), sorted(hits))
for f in ("lib/research/filings/fetch.py", "lib/research/filings/battery.py", "lib/research/filings/batch.py"):
    b = open(f, "rb").read()
    print(f, "crlf", b.count(bytes([13, 10])), "non_ascii_chars", sum(1 for c in b.decode("utf-8") if ord(c) > 127))
```

`.scratch/r98/ac4.py`:
```
import subprocess
def run(args):
    return subprocess.run(args, capture_output=True, text=True).stdout
changed = sorted(run(["git", "diff", "--name-only", "4183e30531", "HEAD", "--", "lib", "integrations", "infra", ".tools", "data"]).split())
print("changed_code_files", changed)
writers = ["bronze_sec_filing", "bronze_issuer_document", "bronze_sec_company_tickers"]
hits = []
for w in writers:
    for line in run(["git", "grep", "-n", w + "(", "--", "lib", "integrations", "data", ".tools"]).splitlines():
        path = line.split(":", 1)[0]
        if path != "lib/research/harvest/filings.py" and "/tests/" not in path:
            hits.append(line.split(":", 2)[0] + ":" + line.split(":", 2)[1])
print("production_writer_calls", len(hits), sorted(hits))
print("callers_by_file", sorted(set(h.split(":")[0] for h in hits)))
```

`.scratch/r98/ac5.py`:
```
for f in ("lib/research/filings/fetch.py", "lib/research/filings/battery.py", "lib/research/filings/batch.py", "lib/research/filings/tests/test_bronze_wiring.py"):
    b = open(f, "rb").read()
    compile(b.decode("utf-8"), f, "exec")
    print(f, "compiles True crlf", b.count(bytes([13, 10])), "non_ascii_chars", sum(1 for c in b.decode("utf-8") if ord(c) > 127))
```

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-98"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r98/ac0.py && python -m pytest lib/research/filings/tests -q -p no:cacheprovider 2>&1 | tail -1 && python -m pytest lib/research/harvest/tests -q -p no:cacheprovider 2>&1 | tail -1</invocation><expect>BEFORE any edit, the baseline every later bar reads against. It prints "pin_object commit"; the four site lines (battery_567 and battery_639 carry "_call_http_get(http_get, _TICKERS_URL" and "_call_http_get(http_get, located[" respectively, battery_1001 carries "_call_http_get(http_get, url, timeout=60)", and fetch_320 carries "raw = http_get(located["); "production_writer_calls N0" (measured 0 at the cut); and each of the three modules' crlf and non_ascii_chars (measured 0 and 0). Then the filings suite's "F0 passed" (measured 79) and the harvest suite's "H0 passed" (measured 64). A drifted line NUMBER is recorded, not a fail, if the SITE is the same; a differing N0, F0 or H0 is recorded and becomes the baseline</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-98"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/filings/tests/test_bronze_wiring.py -v -p no:cacheprovider 2>&1 | tail -12</invocation><expect>a final line "7 passed" and 0 failed, with the PASSED lines naming test_default_off_makes_zero_store_calls, test_ticker_table_bytes_reach_the_writer_unparsed, test_sec_filing_bytes_reach_the_writer_unparsed, test_issuer_document_bytes_reach_the_writer_unparsed, test_fetch_build_source_object_writes_the_raw_filing, test_writer_error_propagates and test_batch_security_key_selector_filters_and_refuses</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-98"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/filings/tests -q -p no:cacheprovider 2>&1 | tail -1</invocation><expect>"(F0 + 7) passed" and 0 failed, where F0 is AC0's printed filings count (measured 79, so 86): every pre-existing filings test stays green unedited</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-98"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/harvest/tests -q -p no:cacheprovider 2>&1 | tail -1</invocation><expect>"H0 passed" and 0 failed, where H0 is AC0's printed harvest count (measured 64): the writers this cell calls are unchanged and their own tests hold</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-98"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r98/ac4.py</invocation><expect>"changed_code_files" lists EXACTLY lib/research/filings/batch.py, lib/research/filings/battery.py, lib/research/filings/fetch.py and lib/research/filings/tests/test_bronze_wiring.py -- no file under lib/research/harvest and no other code file; "production_writer_calls" is N0 + 3, where N0 is AC0's value, and "callers_by_file" is exactly ['lib/research/filings/fetch.py'], since the three writers are called only from BronzeSink's three methods and battery.py and batch.py reach them only through the sink</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-98"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r98/ac5.py</invocation><expect>all four files print "compiles True", crlf 0, and non_ascii_chars EQUAL to AC0's measured value for each existing file (measured 0 for all three) and 0 for the new test file</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~98/AMGT_RESAPP.TO-AMGT-rk-98.b2-filings-bronze-wiring.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4,AC5` (rc 0 is the verdict). Flip the order's status
(on the record face) to `complete` only if every criterion PASSES, and commit with `--only -- <paths>`. Report once,
naming AC0's baselines, the suite counts before and after, and AC4's file list and caller census.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES of the three modules to `.scratch/r98/` before editing. Never
`git checkout --`, never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES -- the L5 choices, flagged to the CTO at issuance:**
1. **Navigation pages are NOT bronze; only step-4 DOCUMENTS are.** The ruling routes `:1001` through the issuer-document
   writer, and that call site fetches both pages and documents. Only a document has a document id and a vendor file
   name, and writing every crawled page (up to 40 per name) would store HTML nobody reads.
2. **Every document candidate fetched is written, not only the winner.** Bronze is one object per fetch, and a
   rejected candidate is still a fetched document the silver/gold re-cuts may re-read. The alternative (winner only)
   is one line if the CTO prefers it.
3. **The sink lives in `fetch.py`, not in `harvest/filings.py`.** This keeps the harvest writers a WALL and the lazy
   import direction the estate already uses (`fetch.persist`).
4. **Not in scope, named for the run cell:** `batch.py`'s real run also calls `analyze.analyze_source` (a model call,
   USD). The B2 RUN cell must either declare that spend or add a `--no-analyze` switch. The battery CLI makes no model
   call.
5. **Ticker table under a `date=` partition:** a second fetch on the same UTC day whose bytes differ (the SEC
   republishes the file) raises `BronzeImmutableError`, and under ruling 2 it propagates. The run cell should fetch it
   once per day; the RUN pair names it.
6. **Pin:** `4183e30531`. Re-pin to the issuance commit if s.33 moves anything under `lib/`.

<status>pending</status>
<round>25</round>
<slot>~98</slot>
<fabric>site-z</fabric>
