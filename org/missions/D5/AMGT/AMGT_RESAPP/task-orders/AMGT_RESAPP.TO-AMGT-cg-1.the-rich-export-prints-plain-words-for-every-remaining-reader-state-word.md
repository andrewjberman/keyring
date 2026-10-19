# AMGT_RESAPP task order -- `AMGT-cg-1` -- THE RICH EXPORT PRINTS `Not available` WHERE IT STILL PRINTS THE READER'S STATE WORDS `ABSENT`, `REFUSED` AND `SERVED` (EIGHT LINE KINDS, ELEVEN WRITERS, ONE FILE)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-cg-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~530</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-cg-1.the-rich-export-prints-plain-words-for-every-remaining-reader-state-word</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a renderer's words and their tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no read or write path changes.
comp-adversary: RUN at the cut (2026-10-19): AC1 at the base fails (the new test file is absent, pytest exit 4); AC2 at the base reads `1 failed, 512 passed` and its floor P is unmet there as expected. EGRESS CLASS, declared: NONE (the tests build lines from committed fixtures and synthetic dicts; no HTTP, no S3, no Bloomberg).
</preflight>

**Your worktree:** `C:/dev/wk-resapp-530` (branch `wk-AMGT_RESAPP-530`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-530`.

**FIVE LESSONS THAT BIND YOUR TESTS.** (1) Compare a named LINE or a SECTION, never a pack's whole text. (2) A new check is dry-run at the base first: your test file runs ONCE on the unedited head and must FAIL on the new behaviour and PASS on every control; record the counts. (3) The regexes in your tests are raw strings. (4) Name the proof instance by the order's FULL name (`<to_id>.proof_of_spec.json`). (5) Existing tests and fixtures that PIN today's words are re-scoped by ONE hand-written assertion each (old and new in the receipt), never silently and never by loosening.

## 1. THE CELL -- `AMGT-cg-1` (round 125, decomposition s.134; the CTO's round-124 analysis item 1, msg 8560, quoted below; the issuer's census `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round125_prep/READER_STATE_WORD_CENSUS.md`, which you READ FIRST)

**The ruling (CTO, round-123 analysis section 2, which round 124 applied to two kinds and round 125 extends to the rest):** *"A cell that prints `ABSENT` puts a reader-side status word in the reader's sheet ... Each labelled value whose state is not-available prints a plain fixed sentence in place of the token, for example `Not available`, then the plain reason if the reason passes the screen. The value itself is unchanged where one exists. Only the not-available rendering moves."* Round 124 (`cf-2`, merged `6f65da85da`, live) did this for the Peers absent-column lines and the chart line with the constant `NOT_AVAILABLE_WORDS = "Not available"` (`render_pack.py:1609`). The census lists what is left.

**What is true today (verify at Step A, cite `path:line`).** `lib/research/print/render_pack.py` prints a reader state word on these export lines (line numbers at the issuance commit; the live export shows 290 `ABSENT` and 27 `REFUSED` lines on 101 names; the PDF prints none and has no writer):
- K1 `_posture_markdown`: line ~2027 `"Posture: ABSENT -- {0}".format(reason)` and ~2029 `"Posture: ABSENT -- {0}. Nothing is rendered in its place.".format(reason)`.
- K2 `_posture_markdown`: ~2037 `"ABSENT -- no call was made: {0}"` and ~2041 `"ABSENT -- no call was made: {0}{1}"` (the second carries `_POSTURE_MACHINE_DISCLAIMER`).
- K3 `_model_sheet_notes_markdown`: ~2130 `"y/y growth rows: ABSENT -- the block carries none and this page computes none."`.
- K4 `_model_sheet_notes_markdown`: ~2140 `"{0}: ABSENT -- the block carries fiscal years {1} to {2} only."`.
- K5 `Description:` ~1703 (`_drafted_section_markdown`) and ~1800 (`_header_description_lines`): `"Description: ABSENT -- {0}"`.
- K6 `_management_markdown`: ~1887 `"Exec Management: ABSENT ({0})."`.
- K7 `_model_case_line` (called by `_model_cases_markdown`, which `build_rich_text` does NOT call: no live line): the head `"{label}: {status}"` / `"{name} case: {status}"` (~2096) prints the state word `ABSENT` for an absent case AND `SERVED` for a present one.
- K8 `_refused_figures_markdown` ~2173 and `build_rich_text` ~2430: `"{mnemonic}: REFUSED -- {reasons}"`.
- K9 `_peers_markdown` ~1928: `["## Peers", "", "ABSENT -- no peer set supplied to this export", ""]`.

**The rule to build (edit `render_pack.py` ONLY, ONLY these writers; reuse the existing constant `NOT_AVAILABLE_WORDS`).**
(a) The state word becomes `Not available` and NOTHING else on the line moves (the label, the reason, the tail, the closing sentence, the order and the blank lines are byte-identical): K1 `Posture: Not available -- {reason}` and `Posture: Not available -- {reason}. Nothing is rendered in its place.`; K2 `Not available -- no call was made: {reason}` (the disclaimer variant likewise); K3 `y/y growth rows: Not available -- the block carries none and this page computes none.`; K4 `{years}: Not available -- the block carries fiscal years {a} to {b} only.`; K5 `Description: Not available -- {reason}` (both writers); K6 `Exec Management: Not available ({words}).`; K8 `{mnemonic}: Not available -- {reasons}` (both writers; the mnemonic label stays); K9 `Not available -- no peer set supplied to this export`.
(b) K7: an ABSENT (or any non-SERVED) case prints `{head}: Not available -- {detail}`; a SERVED case prints `{head}: {detail}` with NO state word, where `head` is the case's `label` or `"{name} case"` and `detail` is exactly what it is today (value with two decimals, currency, formula).
(c) NOTHING else moves: not the Peers present columns, not the Peers absent-column lines or the chart line (cf-2), not any PDF writer, not `scoped_amgt.py`, not a figure, a table or a citation line. A present value (a SERVED posture verdict, a drafted description, a served management object, a served case, an unrefused figure) prints byte-identically to today.

**Do this in order.** (A) `cd C:/dev/wk-resapp-530`; `git log -1 --format=%h`; read the census file, then each writer. Print in the receipt `## Census`: the lines of `render_pack.py` that contain the literal `ABSENT` or `REFUSED` BEFORE and AFTER your edit (native Grep tool; list the line numbers); after your edit the only remaining PRINTING writers of a state word must be none, and the remaining occurrences are comments, docstrings, comparisons and constant names (classify each). (B) Write `lib/research/print/tests/test_cg1_reader_state_words.py` FIRST (tests below) and run it ONCE on the unedited head: record the counts. (C) Build (a) and (b); re-run. (D) Find every existing test or fixture that pins an old word with the native Grep tool over `lib/research/print/tests/` and `lib/research/api/tests/` (`ABSENT -- `, `Posture: ABSENT`, `no call was made`, `y/y growth rows`, `Description: ABSENT`, `Exec Management: ABSENT`, `: REFUSED --`, `case: SERVED`, `case: ABSENT`, `ABSENT -- no peer set`, and the committed rich-text base fixtures under `lib/research/print/tests/fixtures/`, for example `bv2_rich_text_base_*.txt`), run them at the base and after, and re-scope each by changing ONLY the pinned line to the new words (old and new text in the receipt `## Tests re-scoped`, with file and line); a test that pins a line this order does not move is NOT touched. (E) AC1 and AC2, the receipt, the instance, proof-of-spec-check. If a test that compares the export to the portal page's text (for example `test_av2_export_equals_page.py`) fails for a reason other than its one known failure after your edit, do NOT edit the portal or loosen the test: file a surprise row naming the test and the line and report it (the portal side is the issuer's cell `AMGT-cg-2`).

**Tests (`test_cg1_reader_state_words.py`; hand-written expectations; build inputs as synthetic dicts the way `test_posture_markdown.py`, `test_model_cases_markdown.py`, `test_build_rich_text.py` and `test_av2_export_equals_page.py` do, and call the writer functions directly):** one test per kind, each with its present-value counterpart: T1 K1 an ABSENT posture prints both lines exactly (`Posture: Not available -- no posture object for this name` and the `. Nothing is rendered in its place.` variant) and a SERVED posture prints its verdict line unchanged; T2 K2 the no-call lines for a SERVED posture with verdict `absent`, with and without the disclaimer; T3 K3 the y/y line exactly; T4 K4 the estimate-years line for a block that stops at 2027E (`2028E: Not available -- the block carries fiscal years 2023 to 2027E only.`) and for one that stops at 2025 (`2026E, 2027E, 2028E: ...`), and NO such line when the block carries all years; T5 K5 both Description writers (an undrafted description and a header description with a reason, and a reason that carries a storage key prints the fixed sentence) and a served description unchanged; T6 K6 `Exec Management: Not available (no management object is on file).` for an absent management object and a served roster unchanged; T7 K7 an ABSENT case prints `Upside case: Not available -- <reason>`, a labelled absent case prints `<label>: Not available -- <reason>`, a SERVED case prints `Base case: 537.70 (formula)` (the value with two decimals, no state word), and `_model_cases_markdown` of the three default cases reads the same; T8 K8 a REFUSE verdict in `check_face` prints `<MNEMONIC>: Not available -- <reason>` from BOTH writers (the notes line from `_refused_figures_markdown` and the Model Notes line from `build_rich_text`), a plain reason prints as served and a reason carrying a storage key prints the fixed `REFUSED_SENTENCE`; T9 K9 `_peers_markdown(None)` returns the `Not available -- no peer set supplied to this export` line; T10 CONTROL: the Peers absent-column line and the chart line keep their `cf-2` words (`Cash: Not available -- ...`, `The chart: Not available ...`); T11 CONTROL: a whole export built by `build_rich_text` from a committed fixture bundle contains no line that matches the raw regex `\b(?:ABSENT|REFUSED|SERVED)\b` as a state word in any line the census lists (print the matched lines if any; the allowed remainder is only `> cites:` lines and mnemonic labels); T12 CONTROL: the PDF text of the same fixture bundle is byte-identical to the unedited head's (record the sha256 of the base PDF text at Step B and assert it).

## 2. BOUNDS

1. Write only the paths below. No deploy, no Terraform, no store write, no schedule, no SEC, vendor, model or Bloomberg call; no `pip install`, `bun` or `npm`; nothing is fetched from the internet. No push; never touch `DEV` or `PROD`; commit nothing under `portal/` or `org/devices/`.
2. Product edit: `lib/research/print/render_pack.py` ONLY, ONLY the writers named in (a) and (b). Do NOT edit `lib/research/api/scoped_amgt.py` or any other module, and do NOT touch the portal.
3. A line the pack prints never carries a storage path, a bucket key, an object name, an order or cell id or an UPPER_SNAKE field code other than a `K8` line's own mnemonic label. Pure ASCII in what you write.

## 3. SURFACES

<paths>
lib/research/print/render_pack.py
lib/research/print/tests/
lib/research/api/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~530/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-cg-1"><invocation>cd C:/dev/wk-resapp-530 &amp;&amp; timeout 300 python -m pytest lib/research/print/tests/test_cg1_reader_state_words.py -q -p no:cacheprovider --color=no; echo "exit=$?"</invocation><expect>the pytest summary line reads `12 passed` or more with 0 failed and 0 skipped (T1 to T12 each present by name), and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-cg-1"><invocation>cd C:/dev/wk-resapp-530 &amp;&amp; timeout 580 python -m pytest lib/research/print/tests -q -p no:cacheprovider --color=no 2&gt;&amp;1 | grep -E "^FAILED|passed|failed" | sed "s/ - .*//"</invocation><expect>exactly one FAILED line, `FAILED lib/research/print/tests/test_av2_export_equals_page.py::test_pdf_text_carries_no_field_code_and_names_every_line_in_words` (it fails at the base as well: the base reads `1 failed, 512 passed`), and the summary reads `1 failed, P passed` with P at least 524</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~530 <0.9.0_WK_AMGT_RESAPP~530@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~530/CG1_RECEIPT.md` with the sections `## What changed` (every path, with line counts), `## Census`, `## Tests re-scoped` (or `none`) and `## Not verified` (the deployed Lambda serves the old words until `AMGT-cg-4`; the page and the page-vs-export harness move in `AMGT-cg-2`; the whole api folder is not run in this sparse worktree: the issuer runs it in the full tree). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~530/AMGT_RESAPP.TO-AMGT-cg-1.the-rich-export-prints-plain-words-for-every-remaining-reader-state-word.proof_of_spec.json` (the invocations are recorded as the order's literal text). Run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` on the committed bytes and report its verdict line. Do not stage `portal`.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W530-S<k>`, **`disarm_owner` `2.0.0_SA_COO~R1` on EVERY row (a row without it is refused by the gate)**.

Report once: the commit hash and the base; the test run at the base and after; AC1 and AC2 output lines; the census; every existing test or fixture you re-scoped (old and new text); the proof verdict line; any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Item 1 of the CTO's round-124 analysis (`ledger/ROUND_ANALYSIS.round124.R1.md`, msg 8560, `@e8adcc7300`). The CTO's "one cell" is one enrichment item: it is cut by write set into `cg-1` (this file, the workspace repo) and `cg-2` (the portal repo). The redeploy `cg-4` goes under its own never-widen pair that names the moved lines (live: 290 `ABSENT` lines on 101 names, 27 `REFUSED` lines on 16 names, by kind in the census) and both branches of each writer; the expected moved set is exactly the census table. K7 has no live line; its change is graded by the test only. LOCAL code cell.

<status>pending</status>
<round>125</round>
<slot>0.9.0_WK_AMGT_RESAPP~530</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
