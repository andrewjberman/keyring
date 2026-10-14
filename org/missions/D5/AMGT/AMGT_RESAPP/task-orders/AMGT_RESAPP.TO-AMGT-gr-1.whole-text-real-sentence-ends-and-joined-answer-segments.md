# AMGT_RESAPP task order -- `AMGT-gr-1` -- WHOLE TEXT: REAL SENTENCE ENDS (NEVER 'Ps.') AND ANSWER SEGMENTS JOINED WITH A SPACE (FWD-41 ROUND 106; A FIX, CTO 4(b) AND 4(c))

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md</decomp_doc>
<owned_cells>AMGT-gr-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~450</issued_to>
<issued_by>2.0.0_SA_COO~R2</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-gr-1.whole-text-real-sentence-ends-and-joined-answer-segments</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing is scheduled; a library module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, grant, key or policy is touched; the cell writes and tests local Python only.
comp-adversary: RUN at the cut -- `check_gr1_text.py` is a prepared acceptance check (28 arms: sentence splitting with abbreviations, company suffixes, titles, initials, decimals and quotes; the cut; the segment join; the seam); at the base it fails with `ImportError: cannot import name 'sentences'`, the build check failing as expected.
EGRESS CLASS, declared: NONE. No network call by the cell or its checks (the model is a stub or a recorded response); no Bloomberg call.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-450` (branch `wk-AMGT_RESAPP-450`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-450`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-gr-1` (round 106, workstream AIFILL, decomposition `org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md`)

Two measured defects of the stored text. (1) Each block builder cut an over-cap reply at the last `.`, `!` or `?` followed by a space, so `... a dividend of Ps. 7.36 per unit, totaling Ps.` ended on the page at the abbreviation `Ps.`. (2) `model.parse_response` joined the final answer's text blocks with no separator: 14 places over 7 stored blocks read `February 2022.She has served`.
You add one small shared module and use it in the seam. The five builders adopt it in cell gr-6.

### Why this cell exists (the CVO's five-name read of 2026-10-14, C-S143 to C-S146; the CTO's ruling `ledger/CTO_RULING_FWD41_FIVE_NAME_READ_NOT_MET_20261014.md`, item 4)
FWD-41 graded NOT REALIZED: of five names read on the PROD page, four carried a stated claim that its cited source does not support or contradicts (a figure the release contradicts; a clause no source carries; a stale board proposal a newer source overtakes), one block ended mid-sentence on `... totaling Ps.`
(the cut took an abbreviation for a sentence end), one was garbled, and the page's panel denied the web input the blocks cite. The AI-fill blocks are held off the PROD page until a re-read of five NEW names passes. The CTO's remedy is a GROUNDING PASS in the producer: before a block is stored, every sentence is checked against
the fetched text of the sources it cites, and a sentence they do not carry is dropped; a citation that does not answer (404, refused) grounds nothing; where dated sources conflict the newest wins; the contract refuses a block whose grounding record is missing.

The package `lib/research/aifill/` already holds `contract.py`, `orchestrate.py`, `model.py`, `inputs.py`, `store.py`, `run.py`, `revalidate.py` and the five `block_<id>.py` modules (all merged; read the ones you touch). Python 3.9, ASCII, stdlib only.

### `lib/research/aifill/sentences.py` -- exact interface (pure functions, stdlib `re` only)
- `split_sentences(text) -> list[str]`: the real sentences of `text`, stripped, in order; empty or all-whitespace text gives `[]`; joining the result with single spaces keeps every word in order.
- `cut_at_sentence_end(text, cap) -> Optional[str]`: `text` itself when `len(text) <= cap`; else the prefix that ends at the LAST real sentence end that fits within `cap` characters (the end mark and any closing quote or bracket after it are kept; right-stripped); `None` when no real end fits.
- `join_segments(parts) -> str`: concatenates the non-empty strings of `parts` (None and "" are skipped); between two parts it inserts ONE space exactly when the text so far does not end in whitespace, the next part does not start with whitespace, the text so far ends in `.`, `!` or `?` optionally followed by closing characters (`"`, `'`, `)`, `]`), and the next part starts with a letter or an opening quote or bracket (`"`, `'`, `(`, `[`). Otherwise the parts are joined as they are (a name or a decimal split across two blocks is NOT spaced).
- The REAL SENTENCE END rule, for a mark at position i (`.`, `!` or `?`): it is a candidate end when after the mark, and after any run of closing characters (`"`, `'`, `)`, `]`), the text ends or whitespace follows. A candidate is NOT an end when ANY of these hold (all three apply only to a `.` that is not at the very end of the text):
  (a) the word of letters immediately before the `.`, lowercased, is in `NEVER_END = {ps, rs, no, nos, st, mr, mrs, ms, dr, jr, sr, prof, mt, ft, vs, approx, fig, vol, gen, gov, sen, rep}` (titles and currency units: never an end, whatever follows);
  (b) that word is in `SUFFIX = {inc, ltd, corp, co, plc, llc, bros, bn, mn, cos}` and the next non-space character is a lowercase letter or a digit (`Apple Inc. announced` is not an end; `Apple Inc. The firm` is);
  (c) that word is a single capital letter (an initial: `J. P. Morgan`) and the next non-space character is a letter;
  (d) the next non-space character is a lowercase letter (`the U.S. economy`).
  A `.` at the very end of the text is an end whatever precedes it (`... subsidiary AIA Co.`). A `.` followed directly by another `.` (an ellipsis) is not an end until its last dot. A decimal such as `7.36` is never a candidate (no whitespace follows its dot).
- The module defines `NEVER_END` and `SUFFIX` as module constants (frozensets of lowercase words without the dot).

### `lib/research/aifill/model.py` -- `parse_response` only
The text of the final segment is `sentences.join_segments([text of each text block of the final segment])` in place of the plain concatenation. Everything else about the function is unchanged (citations, counts, errors, the final-segment rule of round 105).

### Tests
A new test module `lib/research/aifill/tests/test_sentences.py` (no `__init__.py`): at least one test per rule above (each of (a) to (d), the end-of-text abbreviation, the ellipsis, the decimal, the cut at the last end that fits, None when none fits, every join case). One new test in `lib/research/aifill/tests/test_model_final_answer.py` for the joined segments; touch no other test.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W450-S<k>`, `disarm_owner` `2.0.0_SA_COO~R2`.

## 2. BOUNDS


1. Write ONLY `lib/research/aifill/sentences.py`, `lib/research/aifill/model.py`, `lib/research/aifill/tests/test_sentences.py` and `lib/research/aifill/tests/test_model_final_answer.py`. The five builders and everything else are other cells'.
- Leave `lib/research/management/`, `lib/research/filings/`, `lib/research/posture/` and every existing module untouched.
- No network, no AWS, no real model call, no `pip install`: every model call in your tests is a stub or the recorded response. The `anthropic` package is never imported (the installed 0.45.0 crashes on web-search blocks).
- Python 3.9 syntax (`from __future__ import annotations`, `typing.Optional`, no `X | Y` unions evaluated at runtime, no `match`); ASCII-only source files (write non-ASCII characters as `\uXXXX` escapes); stdlib only.
- Run the commit gate before you commit: `bash .tools/commit-gate.sh <each .py you wrote>` (it runs `py_compile` and `ruff`); a finding there is yours to fix.

## 3. SURFACES

<paths>
lib/research/aifill/sentences.py
lib/research/aifill/model.py
lib/research/aifill/tests/test_sentences.py
lib/research/aifill/tests/test_model_final_answer.py
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-gr-1"><invocation>cd C:/dev/wk-resapp-450 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round106_aifill_prep/checks/check_gr1_text.py" | tail -4; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `AIFILL GR-1 ARMS: YES (N of N)` with N equal to 28, no `FAIL` arm line above it; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-gr-1"><invocation>cd C:/dev/wk-resapp-450 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python -m pytest -q --color=no -p no:cacheprovider lib/research/aifill/tests/test_sentences.py lib/research/aifill/tests/test_model_final_answer.py lib/research/aifill/tests/test_model_inputs.py | tail -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the last non-empty line before `exit=` reads `N passed` (N at least the count your test module's functions define) with no `failed` and no `error` in the last 3 lines; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-gr-1"><invocation>cd C:/dev/wk-resapp-450 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round105_aifill_prep/checks/check_fc1_seam.py" | tail -1; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `AIFILL FC-1 ARMS: YES (12 of 12)`: the round-105 seam check keeps passing (a control, not a hygiene check); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~450 <0.9.0_WK_AMGT_RESAPP~450@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~450/AMGT_RESAPP.TO-AMGT-gr-1.whole-text-real-sentence-ends-and-joined-answer-segments.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character; each criterion's `expect` recorded as an ordered regex of the printed lines when the prose has regex-active characters.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- each criterion's deciding output line (verbatim) and the arm count;
- the arm lines of AC1 that read FAIL, if any, AC2's pytest summary line and AC3's line.
- any row.
The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** An independent head. The abbreviation rules are proven satisfiable by the issuer's reference implementation (28 of 28) and the check discriminates: the unchanged builders read 10 FAIL arms in gr-6's check on the same fixture. The measured stored defects: 14 joined-without-space places over 7 blocks; 2 blocks ending on an abbreviation (KOFUBL MM team_view `Ps.`, a true defect; 1299 HK `Co.` at the true end).

<status>pending</status>
<status>complete -- 2026-10-14 by the issuer (2.0.0_SA_COO~R2): wk-AMGT_RESAPP-450 @ad9eaa7fc8 merged @95cc319c61, proof instance VALID (rc=0). AC1 PASS (`AIFILL GR-1 ARMS: YES (28 of 28)`, re-run by the issuer in the worker tree), AC2 PASS after the issuer's ruling on row W450-S1 (the round-105 test that pinned the old no-separator join was updated by one assertion; package 542 passed), AC3 PASS (`AIFILL FC-1 ARMS: YES (12 of 12)`).</status>
<round>106</round>
<workstream>AIFILL</workstream>
<slot>0.9.0_WK_AMGT_RESAPP~450</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
