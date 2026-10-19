# AMGT_RESAPP task order -- `AMGT-ce-1` -- A SERVED REASON THAT CARRIES THE READER'S OWN STATUS WORD IS NOT PLAIN, SO THE PDF AND EXPORT CEO LINE TAKES THE STATE'S FIXED SENTENCE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ce-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~525</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-ce-1.a-reason-carrying-a-reader-status-word-is-not-plain</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a renderer pattern and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no read or write path changes.
comp-adversary: RUN at the cut (2026-10-19): AC1 at the base fails (the test file is absent, pytest exit 4); AC2 at the base reads `1 failed, 471 passed` and its floor P is unmet there as expected. EGRESS CLASS, declared: NONE (the tests build lines from committed fixtures and synthetic dicts; no HTTP, no S3, no Bloomberg).
</preflight>

**Your worktree:** `C:/dev/wk-resapp-525` (branch `wk-AMGT_RESAPP-525`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-525`.

**FOUR LESSONS THAT BIND YOUR TESTS.** (1) Compare a named LINE or a SECTION, never a pack's whole text. (2) A new check is dry-run at the base first: your test file runs ONCE on the unedited head and must FAIL on the new behaviour and PASS on every control; record the counts. (3) The regexes in your tests are raw strings (`\b` in a non-raw string is a backspace byte). (4) Name the proof instance by the order's FULL name (`<to_id>.proof_of_spec.json`).

## 1. THE CELL -- `AMGT-ce-1` (round 123, decomposition s.132 item 1; row `AMGT_RESAPP-D1-W524-S1`)

**The ruling (CTO, round-122 analysis section 3, quoted):** *"RULING: yes. The reason 'ABSENT, the CEO web search returned 10 url(s).' prints a machine state word into a reader's sentence. `_NOT_PLAIN_PATTERNS` gains a word-boundary pattern for the reader's own status and reading words: the `scoped_amgt` constants and `ABSENT`. A reason that carries one of them takes its state's fixed sentence. The screen goes at the print layer, where every surface passes. `scoped_amgt`'s NOT_SEARCHED branch, which passes the basis verbatim (`scoped_amgt.py:4973-4979`), is not edited in this cell."* Grade: a test that W524-S1's exact string and one per status word take the fixed sentence; the 101-name census then reads DELTA 0 (the issuer's read).

**What is true today (verify at Step A, cite `path:line`).** `lib/research/print/render_pack.py` `_NOT_PLAIN_PATTERNS` (lines 856-867) is a tuple of ten compiled patterns; `_plain_reason(reason, fixed)` (lines 881-891) returns the served reason when it is plain words, else `fixed`. No pattern matches a bare uppercase word, so a NOT_SEARCHED basis `ABSENT, the CEO web search returned 10 url(s).` is plain and `_ceo_profile_sentence` prints `CEO public profile (<name>): ABSENT, the CEO web search returned 10 url(s).`. The reader's words are the constants at `lib/research/api/scoped_amgt.py:4886-4892`: `CONFIRMED`, `NOT_SEARCHED`, `SEARCHED_NOTHING_FOUND`, `SEARCHED_LINKS_UNREADABLE`, `SEARCH_FAILED`, `NOT_WRITTEN`, `UNREADABLE_OBJECT`; the six with an underscore are already caught by the `\w_\w` pattern; `CONFIRMED` and `ABSENT` are not.

**The rule to build.**
(a) ONE new entry in `_NOT_PLAIN_PATTERNS`: a compiled, CASE-SENSITIVE, word-bounded pattern that matches any of the eight words `ABSENT`, `CONFIRMED`, `NOT_SEARCHED`, `SEARCHED_NOTHING_FOUND`, `SEARCHED_LINKS_UNREADABLE`, `SEARCH_FAILED`, `NOT_WRITTEN`, `UNREADABLE_OBJECT` (list the six underscore words explicitly even though `\w_\w` already catches them: the list is the record of the reader's vocabulary) with a one-line comment naming the cell. Lowercase or mixed-case prose (`confirmed`, `absent`, `Absent`) stays PLAIN.
(b) A reason that carries one of the words is NOT plain, so `_plain_reason` returns the caller's fixed sentence; for the CEO line that is the state's own fixed sentence already built by `_ceo_profile_sentence` (round 122, `AMGT-cd-1`). Every other caller of `_plain_reason` takes its own fixed sentence by the same mechanism; that is by design.
(c) A plain reason with no such word prints BYTE-IDENTICALLY as today (HD US and BA US, from the committed fixtures, are the proof).

**Do this in order.** (A) `cd C:/dev/wk-resapp-525`; `git log -1 --format=%h`; read `_NOT_PLAIN_PATTERNS`, `_plain_reason`, `_ceo_profile_sentence` (find it in `render_pack.py`) and `lib/research/print/tests/test_cd1_ceo_sentence_per_state.py` (the round-122 test, which shows how a profile dict is turned into a line) and print in the receipt `## Census`: for each of the eight words, the line `_ceo_profile_sentence` prints BEFORE and AFTER for a NOT_SEARCHED profile whose basis carries it, and the BEFORE/AFTER of every caller of `_plain_reason` you can find with the native Grep tool (a count of call sites is enough, with the denominator printed). (B) Write `lib/research/print/tests/test_ce1_status_word_screen.py` FIRST (tests below) and run it ONCE on the unedited head: record the counts. (C) Build (a) and (b); re-run. (D) Run once at the base and once after the existing tests that name `_plain_reason`, `_NOT_PLAIN_PATTERNS` or a CEO line (`test_by1_reason_mapper.py`, `test_cd1_ceo_sentence_per_state.py`, `test_ca1_ceo_three_states.py`, `test_bz2_rich_management_equals_pdf.py`); a test that pins a served reason containing one of the eight words is re-scoped by ONE hand-written assertion (old and new in the receipt `## Tests re-scoped`). (E) AC1 and AC2, the receipt, the instance, and proof-of-spec-check.

**Tests (`test_ce1_status_word_screen.py`; hand-written expectations):** T1 W524-S1's EXACT string (basis `ABSENT, the CEO web search returned 10 url(s).`, a NOT_SEARCHED profile for a named CEO) prints that state's fixed sentence and does NOT contain `ABSENT`; T2 one parametrised case per word (eight) with a basis of the form `<WORD>, the CEO web search returned 10 url(s).` for the profile state the word belongs to (use `NOT_SEARCHED` where the word is not a state), prints a fixed sentence and does NOT contain the word; T3 `_plain_reason` directly: each of the eight words inside a sentence returns the `fixed` argument; T4 CONTROL: lowercase `confirmed`, `absent` and mixed-case `Absent` inside a sentence return the reason unchanged; T5 CONTROL: HD US and BA US from the committed fixtures print the same CEO line as the unedited head (record the two base lines by hand at Step B); T6 CONTROL: a plain reason with none of the words prints byte-identically for each of the four searched states; T7 the export prints the same line as the PDF for the W524-S1 string (build both from one bundle); T8 the pattern tuple has exactly one more entry than at the base (eleven).

**Region you own in `render_pack.py`:** the `_NOT_PLAIN_PATTERNS` tuple and its comment ONLY. You do NOT edit `scoped_amgt.py`, `_plain_reason`, `_ceo_profile_sentence`, the figure builders, the appendix or the export's other sections.

## 2. BOUNDS

1. Write only the paths below. No deploy, no Terraform, no store write, no schedule, no SEC, vendor, model or Bloomberg call; no `pip install`, `bun` or `npm`; nothing is fetched from the internet. No push; never touch `DEV` or `PROD`; commit nothing under `portal/` or `org/devices/`.
2. Product edit: `lib/research/print/render_pack.py` ONLY, ONLY the tuple named above. Do NOT edit `lib/research/api/scoped_amgt.py`.
3. A line the pack prints never carries a storage path, a bucket key, an object name, an order or cell id or an UPPER_SNAKE field code.

## 3. SURFACES

<paths>
lib/research/print/render_pack.py
lib/research/print/tests/
lib/research/api/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~525/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ce-1"><invocation>cd C:/dev/wk-resapp-525 &amp;&amp; timeout 300 python -m pytest lib/research/print/tests/test_ce1_status_word_screen.py -q -p no:cacheprovider --color=no; echo "exit=$?"</invocation><expect>the pytest summary line reads `16 passed` or more with 0 failed and 0 skipped (T1 once, T2 eight times, T3 once or more, T4 to T8 each present by name), and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ce-1"><invocation>cd C:/dev/wk-resapp-525 &amp;&amp; timeout 580 python -m pytest lib/research/print/tests -q -p no:cacheprovider --color=no 2&gt;&amp;1 | grep -E "^FAILED|passed|failed" | sed "s/ - .*//"</invocation><expect>exactly one FAILED line, `FAILED lib/research/print/tests/test_av2_export_equals_page.py::test_pdf_text_carries_no_field_code_and_names_every_line_in_words` (it fails at the base as well: the base reads `1 failed, 471 passed`), and the summary reads `1 failed, P passed` with P at least 487</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~525 <0.9.0_WK_AMGT_RESAPP~525@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~525/CE1_RECEIPT.md` with the sections `## What changed` (every path, with line counts), `## Census`, `## Tests re-scoped` (or `none`) and `## Not verified` (the deployed Lambda serves the old pattern set until `AMGT-ce-4`; the whole api folder is not run in this sparse worktree: the issuer runs it in the full tree). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~525/AMGT_RESAPP.TO-AMGT-ce-1.a-reason-carrying-a-reader-status-word-is-not-plain.proof_of_spec.json` (the invocations are recorded as the order's literal text). Run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` on the committed bytes and report its verdict line. Do not stage `portal`.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W525-S<k>`, **`disarm_owner` `2.0.0_SA_COO~R1` on EVERY row (a row without it is refused by the gate)**.

Report once: the commit hash and the base; the test run at the base and after; AC1 and AC2 output lines; the census; every existing test you re-scoped (old and new assertion); the proof verdict line; any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Item 2 of the CTO's round-122 analysis (`ledger/ROUND_ANALYSIS.round122.R1.md`, msg 8323, `@3583db8527`); row W524-S1 (the CVO's latent finding). The 101-name census (`AMGT-ce-3`) is the issuer's and should read DELTA 0 since no current name carries a status word. LOCAL code cell; served only through `AMGT-ce-4` (a pair only if a printed line moves).

<status>pending</status>
<round>123</round>
<slot>0.9.0_WK_AMGT_RESAPP~525</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
