# AMGT_RESAPP task order -- `AMGT-gr-2` -- FETCH A CITED SOURCE AND SAY WHAT HAPPENED TO IT: THE SOURCES MODULE (FWD-41 ROUND 106; A BUILD, CTO 4(a) AND 4(f))

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md</decomp_doc>
<owned_cells>AMGT-gr-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~451</issued_to>
<issued_by>2.0.0_SA_COO~R2</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-gr-2.fetch-a-cited-source-and-say-what-happened-to-it</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing is scheduled; a library module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, grant, key or policy is touched; the cell writes and tests local Python only.
comp-adversary: RUN at the cut -- `check_gr2_sources.py` is a prepared acceptance check (21 arms, offline through a stub transport: answering page, six non-answers, a raising transport, PDFs, empty and paywall pages, bad urls, the declared agent, truncation, charsets, paywall titles, windows); at the base it fails with `ImportError: cannot import name 'sources'`, the build check failing as expected.
EGRESS CLASS, declared: NONE by the cell and its checks (a stub transport). The module's own default transport (urllib) is exercised only in production by the issuer.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-451` (branch `wk-AMGT_RESAPP-451`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-451`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-gr-2` (round 106, workstream AIFILL, decomposition `org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md`)

The grounding pass must read what the model's cited pages actually say. You build the module that fetches ONE url and reports what happened to it, in a shape the grounding step consumes. The CVO measured 78 web citations: 47 answered, 26 refused a script (403, paywall or bot wall), 2 were 404, 1 a TLS error, and 5 of the answers were PDFs. A page that does not answer grounds nothing (the CTO's ruling).

### Why this cell exists (the CVO's five-name read of 2026-10-14, C-S143 to C-S146; the CTO's ruling `ledger/CTO_RULING_FWD41_FIVE_NAME_READ_NOT_MET_20261014.md`, item 4)
FWD-41 graded NOT REALIZED: of five names read on the PROD page, four carried a stated claim that its cited source does not support or contradicts (a figure the release contradicts; a clause no source carries; a stale board proposal a newer source overtakes), one block ended mid-sentence on `... totaling Ps.`
(the cut took an abbreviation for a sentence end), one was garbled, and the page's panel denied the web input the blocks cite. The AI-fill blocks are held off the PROD page until a re-read of five NEW names passes. The CTO's remedy is a GROUNDING PASS in the producer: before a block is stored, every sentence is checked against
the fetched text of the sources it cites, and a sentence they do not carry is dropped; a citation that does not answer (404, refused) grounds nothing; where dated sources conflict the newest wins; the contract refuses a block whose grounding record is missing.

The package `lib/research/aifill/` already holds `contract.py`, `orchestrate.py`, `model.py`, `inputs.py`, `store.py`, `run.py`, `revalidate.py` and the five `block_<id>.py` modules (all merged; read the ones you touch). Python 3.9, ASCII, stdlib only.

### `lib/research/aifill/sources.py` -- exact interface
- `STATUS` words: `OK`, `REFUSED`, `NOT_FOUND`, `ERROR`, `EMPTY`, `PAYWALL`, `UNSUPPORTED`.
- `USER_AGENT = "Opal-AIFill-Grounding/1.0 (research; declared agent)"`.
- `default_transport(url, headers, timeout) -> (http_status:int, content_type:str, body:bytes)`: stdlib `urllib.request` with redirects followed, at most 3,000,000 bytes read, an `HTTPError` returned as its code and headers with an empty body, other errors raised. It is the ONLY place that opens a connection.
- `fetch_source(url, transport=None, max_chars=60000) -> dict` with exactly the keys `url`, `status`, `http_status`, `title`, `text`, `chars`, `note`; it NEVER raises:
  * a `url` that is not a string starting `http://` or `https://` -> `status` ERROR, `note` `not an http(s) url`, NO transport call;
  * otherwise ONE transport call `transport(url, {"User-Agent": USER_AGENT, "Accept": "text/html,application/xhtml+xml,text/plain;q=0.9"}, 20)` (`transport` defaults to `default_transport`); an exception -> ERROR, `http_status` None, `note` `<ExceptionClassName>: <message cut to 80 characters>`;
  * `http_status` 401, 403, 429 or 451 -> REFUSED; 404 or 410 -> NOT_FOUND; any other status outside 200-299 -> ERROR with `note` `http <code>`; in all of these `text` is `""`;
  * 2xx: a `content_type` starting `application/pdf`, or a body starting `%PDF-`, -> UNSUPPORTED (`note` `pdf`, `text` `""`); else the body is decoded (the `charset` of the content type, else a `charset=` in the first 2,000 bytes of the body, else UTF-8; undecodable bytes replaced, an unknown charset falls back to UTF-8) and `extract_text` gives `(title, text)`; `text` is cut to `max_chars`; `chars` is `len(text)`;
  * then, on a 2xx page: fewer than 200 characters of text with none of the paywall markers -> EMPTY (`text` `""`); fewer than 3000 characters of text whose first 2,500 characters (lowercased) hold one of the paywall markers -> PAYWALL (`text` `""`); else OK. The markers: `to continue reading`, `subscribe or sign in`, `sign in to continue`, `verify you are human`, `just a moment`, `enable javascript and cookies`, `access denied`, `please subscribe`.
- `extract_text(body, content_type) -> (title, text)`: with `html.parser`; the subtrees of `script`, `style`, `noscript`, `svg`, `template`, `iframe` and `nav` are dropped; the text of block tags (`p`, `div`, `li`, `br`, `tr`, `h1` to `h6`, `section`, `article`, `table`) is put on separate lines; entities are decoded; each line's whitespace is collapsed and empty lines dropped; the `title` is the `<title>` text with whitespace collapsed. Malformed markup never raises (a parser error ends the extraction with what was read).
- `is_paywall_title(title) -> bool`: False for `None` or blank; True when the lowercased title contains any of `free trial`, `subscribe`, `subscription`, `sign in`, `log in`, `login`, `just a moment`, `access denied`, `attention required`, `404`, `not found`, `verify you are human`, `cookie`.
- `select_windows(text, needles, max_chars) -> str`: `text` itself when `len(text) <= max_chars`; else the paragraphs (lines) of `text` scored by how many distinct tokens of `needles` they contain (a token is a run of 4 or more lowercase letters, or a run of digits, from the lowercased needles), highest score first, kept while they fit `max_chars` (a paragraph with score 0 is kept only if nothing scored), returned in their ORIGINAL order joined by newlines; the result is never longer than `max_chars`.

### Tests
A new test module `lib/research/aifill/tests/test_sources.py` (no `__init__.py`): every status, every branch above, the declared agent and timeout, the charset cases and `select_windows`; all through a stub transport; no network.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W451-S<k>`, `disarm_owner` `2.0.0_SA_COO~R2`.

## 2. BOUNDS


1. Write ONLY `lib/research/aifill/sources.py` and `lib/research/aifill/tests/test_sources.py`. Your tests and checks make NO network call: the stub transport is the only transport they use.
- Leave `lib/research/management/`, `lib/research/filings/`, `lib/research/posture/` and every existing module untouched.
- No network, no AWS, no real model call, no `pip install`: every model call in your tests is a stub or the recorded response. The `anthropic` package is never imported (the installed 0.45.0 crashes on web-search blocks).
- Python 3.9 syntax (`from __future__ import annotations`, `typing.Optional`, no `X | Y` unions evaluated at runtime, no `match`); ASCII-only source files (write non-ASCII characters as `\uXXXX` escapes); stdlib only.
- Run the commit gate before you commit: `bash .tools/commit-gate.sh <each .py you wrote>` (it runs `py_compile` and `ruff`); a finding there is yours to fix.

## 3. SURFACES

<paths>
lib/research/aifill/sources.py
lib/research/aifill/tests/test_sources.py
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-gr-2"><invocation>cd C:/dev/wk-resapp-451 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round106_aifill_prep/checks/check_gr2_sources.py" | tail -4; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `AIFILL GR-2 ARMS: YES (N of N)` with N equal to 21, no `FAIL` arm line above it; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-gr-2"><invocation>cd C:/dev/wk-resapp-451 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python -m pytest -q --color=no -p no:cacheprovider lib/research/aifill/tests/test_sources.py | tail -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the last non-empty line before `exit=` reads `N passed` (N at least the count your test module's functions define) with no `failed` and no `error` in the last 3 lines; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~451 <0.9.0_WK_AMGT_RESAPP~451@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~451/AMGT_RESAPP.TO-AMGT-gr-2.fetch-a-cited-source-and-say-what-happened-to-it.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character; each criterion's `expect` recorded as an ordered regex of the printed lines when the prose has regex-active characters.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- each criterion's deciding output line (verbatim) and the arm count;
- the arm lines of AC1 that read FAIL, if any, and the pytest summary line.
- any row.
The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** An independent head; proven satisfiable by the issuer's reference (21 of 21). PDFs are UNSUPPORTED (no stdlib extractor): the CTO's rule that a citation that does not answer grounds nothing applies, and the yield consequence (5 of 78 in the CVO's sample are PDFs, 26 refuse a script) is stated in the analysis, not hidden. Bot walls are never circumvented: a declared agent, one request, no retry.

<status>pending</status>
<round>106</round>
<workstream>AIFILL</workstream>
<slot>0.9.0_WK_AMGT_RESAPP~451</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
