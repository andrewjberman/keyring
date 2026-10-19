# AMGT_RESAPP task order -- `AMGT-cf-2` -- THE PEERS ABSENT-COLUMN LINES AND THE CHART LINE OF THE PDF AND EXPORT PRINT `Not available`, NOT THE READER'S STATE WORD `ABSENT`

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-cf-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~528</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-cf-2.a-peers-absent-column-and-the-chart-line-print-not-available-not-the-state-word</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a renderer sentence and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no read or write path changes.
comp-adversary: RUN at the cut (2026-10-19): AC1 at the base fails (the test file is absent, pytest exit 4); AC2 at the base reads `1 failed, 499 passed` and its floor P is unmet there as expected. EGRESS CLASS, declared: NONE (the tests build lines from committed fixtures and synthetic dicts; no HTTP, no S3, no Bloomberg).
</preflight>

**Your worktree:** `C:/dev/wk-resapp-528` (branch `wk-AMGT_RESAPP-528`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-528`.

**FOUR LESSONS THAT BIND YOUR TESTS.** (1) Compare a named LINE or a SECTION, never a pack's whole text. (2) A new check is dry-run at the base first: your test file runs ONCE on the unedited head and must FAIL on the new behaviour and PASS on every control; record the counts. (3) The regexes in your tests are raw strings (`\b` in a non-raw string is a backspace byte). (4) Name the proof instance by the order's FULL name (`<to_id>.proof_of_spec.json`).

## 1. THE CELL -- `AMGT-cf-2` (round 124, decomposition s.133 item 2; the CTO's round-123 ruling, section 2)

**The ruling (CTO, round-123 analysis section 2, quoted):** *"RULING: yes, they are inside it ('0 state tokens' in what a reader reads). A Model-sheet cell that prints `ABSENT` puts a reader-side status word in the reader's sheet, the same class W524-S1 just closed on the CEO line. Each labelled value whose state is not-available prints a plain fixed sentence in place of the token, for example `Not available`, then the plain reason if the reason passes the screen. The chart line takes its state's fixed sentence. It must not keep the `ABSENT` literal at `render_pack.py:2187`. The value itself is unchanged where one exists. Only the not-available rendering moves."* The lines the CVO named are on every live rich export, for example `Cash: ABSENT -- 'Cash to Market Value' is a ratio; no absolute cash level` and `5-yr growth EBIT: ABSENT -- no EBIT growth measure at any window (...)`: they are the Peers section's absent-column lines.

**What is true today (verify at Step A, cite `path:line`).** `lib/research/print/render_pack.py`: `_peers_markdown(peer_set)` (line ~1914) ends its present-columns table and members table with a loop `for col in absent:` (line ~1967) that appends `"{0}: ABSENT -- {1}".format(col.get("column", "?"), _plain_reason(col.get("reason", "no reason recorded"), ABSENT_COLUMN_SENTENCE))`; `_thesis_driver_chart_markdown(thesis_bundle)` (line ~2175) ends with `line = "The chart: ABSENT" + (' -- the thesis driver is "{0}"'.format(series) if series else "")` (line ~2187), returned as a one-line list, and returns `[]` when drafting is not SERVED or the chart is SERVED. `_plain_reason(reason, fixed)` (line ~881) returns the reason when it is plain words, else `fixed`. The constants `ABSENT_COLUMN_SENTENCE` etc. sit near line 1604.

**The rule to build (edit `render_pack.py` in exactly these two places, plus one constant).**
(a) A module constant `NOT_AVAILABLE_WORDS = "Not available"` beside `ABSENT_COLUMN_SENTENCE`, with a one-line comment naming this cell.
(b) The `_peers_markdown` absent-column loop prints `"{0}: {1} -- {2}".format(column, NOT_AVAILABLE_WORDS, <the same _plain_reason(...) as today>)`: the column name, the reason and the fixed fallback are byte-identical to today; ONLY the word `ABSENT` becomes `Not available`.
(c) The chart line prints `"The chart: " + NOT_AVAILABLE_WORDS` followed by the same `-- the thesis driver is "<series>"` tail as today when a plain series name is present. The conditions that print the line, and the `[]` returns, do not change.
(d) NOTHING ELSE moves. These lines keep their `ABSENT` exactly as today and you do not touch them, their builders or their tests: `Posture: ABSENT -- ...`, `ABSENT -- no call was made: ...`, `y/y growth rows: ABSENT -- ...`, `<years>E: ABSENT -- the block carries fiscal years ...`, `Description: ABSENT -- ...`, `Exec Management: ABSENT (...)`, the `## Peers` no-peer-set line `ABSENT -- no peer set supplied to this export`, and the Model Cases lines (`<name> case: ABSENT -- ...`). They are outside the ruling's list and are recorded for the CTO as an open question (the issuer's, not yours). A present value (a present column's table row, a member row, a SERVED chart, a SERVED case) prints byte-identically to today.

**Do this in order.** (A) `cd C:/dev/wk-resapp-528`; `git log -1 --format=%h`; read the two functions, `_plain_reason`, and the tests named below for the house style. Print in the receipt `## Census`: the denominator of every line in `render_pack.py` that contains the literal `ABSENT` BEFORE and AFTER your edit (use the native Grep tool with `-c`-style counting and list the line numbers), which must differ by exactly the two lines (b) and (c). (B) Write `lib/research/print/tests/test_cf2_not_available_words.py` FIRST (tests below) and run it ONCE on the unedited head: record the counts. (C) Build (a) to (c); re-run. (D) Find every existing test or fixture that pins the old words with the native Grep tool over `lib/research/print/tests/` (`ABSENT -- ` after a column name, `C1: ABSENT`, `The chart: ABSENT`, and the committed rich-text base fixtures under `lib/research/print/tests/fixtures/`, for example `bv2_rich_text_base_*.txt`), run them at the base and after, and re-scope each by changing ONLY the pinned peers-column line or chart line to the new words (old and new text in the receipt `## Tests re-scoped`, with the file and line); a test that pins any other ABSENT line is NOT touched. (E) AC1 and AC2, the receipt, the instance and proof-of-spec-check. If a test that compares the export to the portal page's text (for example `test_av2_export_equals_page.py`) fails for a reason other than its one known failure after your edit, do NOT edit the portal or loosen the test: file a surprise row naming the test and the line and report it.

**Tests (`test_cf2_not_available_words.py`; hand-written expectations; build the peer set as a dict `{"basis": "present", "reason": None, "csc_columns": {"columns": [...], "columns_declared": N, "present": [...], "absent": [{"column": C, "reason": R}, ...]}, "members": []}` as `lib/research/print/tests/test_by2_rich_export_rules.py` (variant `drafted_and_refused`) does, and call `rp._peers_markdown(peer_set)`):** T1 to T4 one parametrised case per field (`Cash` with reason `'Cash to Market Value' is a ratio; no absolute cash level`; `5-yr growth Revenue` with reason `the growth category tops out at a THREE-year window`; `5-yr growth EBIT` with reason `no EBIT growth measure at any window ('EBIT to Enterprise Value' is a yield, 'EBIT Estimate Revisions (45D)' an estimate revision)`; `5-yr growth FCF` with reason `no FCF growth measure at any window ('Free Cash Flow Yield' and 'Free Cash Flow to Enterprise Value NTM' are yields)`): the output list contains exactly the line `<field>: Not available -- <reason>` and no output line starts with `<field>: ABSENT`; T5 a column whose reason carries a storage key or a cell id (`no object under s3://opal-data-harvest/x/y.json -- AMGT-rj-11 has not landed one`) prints `<column>: Not available -- ` followed by the fixed `ABSENT_COLUMN_SENTENCE`, never the key; T6 a column with no `reason` key prints `<column>: Not available -- no reason recorded`; T7 the chart: a drafted bundle (`drafting_status` SERVED, `thesis_driver` series `EBITDA`, no chart) returns exactly `['The chart: Not available -- the thesis driver is "EBITDA"']`, the same bundle with no series returns exactly `['The chart: Not available']`, a SERVED chart returns `[]`, an undrafted bundle returns `[]`; T8 CONTROL: a present column's table row and a member row print byte-identically to the unedited head (record the two base lines by hand at Step B and assert them literally); T9 CONTROL: the other ABSENT lines keep their words: `_posture_markdown` of an ABSENT posture still contains `Posture: ABSENT -- `, `_model_sheet_notes_markdown` still returns a first line starting `y/y growth rows: ABSENT -- `, and `_peers_markdown(None)` still returns the line `ABSENT -- no peer set supplied to this export`; T10 the word `ABSENT` (raw regex `\bABSENT\b`) appears in none of the lines T1 to T7 produce.

## 2. BOUNDS

1. Write only the paths below. No deploy, no Terraform, no store write, no schedule, no SEC, vendor, model or Bloomberg call; no `pip install`, `bun` or `npm`; nothing is fetched from the internet. No push; never touch `DEV` or `PROD`; commit nothing under `portal/` or `org/devices/`.
2. Product edit: `lib/research/print/render_pack.py` ONLY, ONLY the places named in (a) to (c). Do NOT edit `lib/research/api/scoped_amgt.py` or any other module.
3. A line the pack prints never carries a storage path, a bucket key, an object name, an order or cell id or an UPPER_SNAKE field code. Pure ASCII in what you write.

## 3. SURFACES

<paths>
lib/research/print/render_pack.py
lib/research/print/tests/
lib/research/api/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~528/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-cf-2"><invocation>cd C:/dev/wk-resapp-528 &amp;&amp; timeout 300 python -m pytest lib/research/print/tests/test_cf2_not_available_words.py -q -p no:cacheprovider --color=no; echo "exit=$?"</invocation><expect>the pytest summary line reads `10 passed` or more with 0 failed and 0 skipped (T1 to T4 once each, T5 to T10 each present by name), and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-cf-2"><invocation>cd C:/dev/wk-resapp-528 &amp;&amp; timeout 580 python -m pytest lib/research/print/tests -q -p no:cacheprovider --color=no 2&gt;&amp;1 | grep -E "^FAILED|passed|failed" | sed "s/ - .*//"</invocation><expect>exactly one FAILED line, `FAILED lib/research/print/tests/test_av2_export_equals_page.py::test_pdf_text_carries_no_field_code_and_names_every_line_in_words` (it fails at the base as well: the base reads `1 failed, 499 passed`), and the summary reads `1 failed, P passed` with P at least 509</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~528 <0.9.0_WK_AMGT_RESAPP~528@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~528/CF2_RECEIPT.md` with the sections `## What changed` (every path, with line counts), `## Census`, `## Tests re-scoped` (or `none`) and `## Not verified` (the deployed Lambda serves the old words until `AMGT-cf-4`; the page (`PeersTab.tsx`) still shows `ABSENT` on these lines because the portal is not in this cell; the whole api folder is not run in this sparse worktree: the issuer runs it in the full tree). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~528/AMGT_RESAPP.TO-AMGT-cf-2.a-peers-absent-column-and-the-chart-line-print-not-available-not-the-state-word.proof_of_spec.json` (the invocations are recorded as the order's literal text). Run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` on the committed bytes and report its verdict line. Do not stage `portal`.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W528-S<k>`, **`disarm_owner` `2.0.0_SA_COO~R1` on EVERY row (a row without it is refused by the gate)**.

Report once: the commit hash and the base; the test run at the base and after; AC1 and AC2 output lines; the census; every existing test or fixture you re-scoped (old and new text); the proof verdict line; any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Item 2 of the CTO's round-123 analysis (`ledger/ROUND_ANALYSIS.round123.R1.md`, msg 8492, `@980ad8c80c`), section 2. The CTO's list is the Peers absent-column fields and the chart literal; the `(d)` lines (Posture, y/y growth, estimate years, Description, Exec Management, no-peer-set, Model Cases) carry the same word but are outside the ruling's list and are put to the CTO as a question in the drain-end slug, not decided here. The issuer's `AMGT-cf-3` census (8 live rich exports plus the PDFs, before and after) lists the moved lines, expected: only the Peers absent-column lines and the chart line; a moved line outside that list is a row and stops the redeploy `AMGT-cf-4` (a never-widen pair, CTO and COO). The page still shows `ABSENT` (portal untouched; client-facing page changes wait on Andrew).

<status>complete</status>
<round>124</round>
<slot>0.9.0_WK_AMGT_RESAPP~528</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
