# AMGT_RESAPP task order -- `AMGT-fc-1` -- THE MODEL SEAM KEEPS ONLY THE MODEL'S FINAL ANSWER, NEVER ITS NARRATION (FWD-41 ROUND 105; A FIX)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md</decomp_doc>
<owned_cells>AMGT-fc-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~430</issued_to>
<issued_by>2.0.0_SA_COO~R2</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-fc-1.the-model-seam-keeps-only-the-final-answer</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing is scheduled; a library module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, grant, key or policy is touched; the cell writes and tests local Python only.
comp-adversary: RUN at the cut -- `check_fc1_seam.py` is a prepared acceptance check (12 arms: the recorded real response, a preamble before the search, several searches, no search, citations from the final segment only, an empty answer, max_tokens, counts); at the base it reads `AIFILL FC-1 ARMS: NO (6 of 12)` (the six arms for the new behaviour FAIL; the six controls PASS), the build check failing as expected.
EGRESS CLASS, declared: NONE. No network call by the cell or its checks (the model is a stub or a recorded response); no Bloomberg call.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-430` (branch `wk-AMGT_RESAPP-430`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-430`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-fc-1` (round 105, workstream AIFILL, decomposition `org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md`)

When a Messages API reply uses the web search tool, its `content` is a SEQUENCE: `text` blocks of the model thinking aloud ("I'll research this now."), then `server_tool_use` blocks (the queries), `web_search_tool_result` blocks, and finally the `text` block(s) of the ANSWER. `lib/research/aifill/model.py` `parse_response`
joined EVERY text block, so the narration was stored in front of the answer (`now.MUFG announced...`). You fix the seam so only the final answer survives. One file plus tests.

### Why this cell exists (measured by the CVO on the stored documents, C-S133; the CTO's round-104 analysis, `ledger/ROUND_ANALYSIS.round104.AIFILL.md`)
The producer stored 11 blocks across 10 names that open with the MODEL'S NARRATION, glued to the real answer with no space: `I'll research this now.MUFG announced ...` (8306 JP, 9433 JP, 939 HK, ICT PM, NESN SW, PWR US, RIO LN, SHOP CN, UNVGY US), and stored `Nestl` for `Nestle`
(a non-ASCII letter was DROPPED, not transliterated). Neither has reached a person (the page is not landed) but both are served by the API. The CTO's ruling: the disarm is in the PRODUCER, never by hand-editing documents; the page does not land until a full re-validate of all 95 stored
documents against the new contract reads 0 refused. Round 104's cells are merged; this round changes four of their files.

### The change in `lib/research/aifill/model.py` (`parse_response` only; every other function keeps its behaviour)
- The FINAL SEGMENT of `resp["content"]` is the run of blocks after the LAST block whose `type` is `server_tool_use` or `web_search_tool_result` (when the reply has no such block, the whole `content` is the final segment).
- `ModelResult.text` is the concatenation, with no separator (the API already carries each block's own spacing), of the `text` of the `text` blocks of the FINAL segment only.
- `ModelResult.citations` are taken from the `citations` of the `text` blocks of the FINAL segment only (de-duplicated by url, in order, as before). A citation attached to an earlier text block is dropped.
- `searches`, `web_search_requests`, `input_tokens`, `output_tokens`, `model`, `stop_reason` still cover the WHOLE reply, as before.
- `ModelError` when the final segment's text is empty after `.strip()` (the model searched and then said nothing); the existing `ModelError` cases (non-dict, error body, non-list content, `stop_reason == "max_tokens"`) are unchanged. Update the empty-text message to say the model gave no final answer.
- `call_model` needs no change (it calls `parse_response`).

### Tests
A new test module `lib/research/aifill/tests/test_model_final_answer.py` (no `__init__.py`): at least one test per bullet above, built from small hand-made response dicts and from the recorded fixture
`C:/dev/wk-resapp-430/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round104_aifill_prep/fixtures/web_search_response_asml.json` (the recorded real response; every one of its text blocks comes after its searches, so its text must be unchanged). If a test in the existing `tests/test_model_inputs.py` asserts the old behaviour, update that one test; touch nothing else in it.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W430-S<k>`, `disarm_owner` `2.0.0_SA_COO~R2`.

## 2. BOUNDS


1. Write ONLY `lib/research/aifill/model.py` (`parse_response`), `lib/research/aifill/tests/test_model_final_answer.py` and, only if one asserts the old joining, a test in `lib/research/aifill/tests/test_model_inputs.py`. The contract, the builders, the store and everything else are other cells'.
- Leave `lib/research/management/`, `lib/research/filings/`, `lib/research/posture/` and every existing module untouched.
- No network, no AWS, no real model call, no `pip install`: every model call in your tests is a stub or the recorded response. The `anthropic` package is never imported (the installed 0.45.0 crashes on web-search blocks).
- Python 3.9 syntax (`from __future__ import annotations`, `typing.Optional`, no `X | Y` unions evaluated at runtime, no `match`); ASCII-only source files (write non-ASCII characters as `\uXXXX` escapes); stdlib only.
- Run the commit gate before you commit: `bash .tools/commit-gate.sh <each .py you wrote>` (it runs `py_compile` and `ruff`); a finding there is yours to fix.

## 3. SURFACES

<paths>
lib/research/aifill/model.py
lib/research/aifill/tests/test_model_final_answer.py
lib/research/aifill/tests/test_model_inputs.py
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-fc-1"><invocation>cd C:/dev/wk-resapp-430 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round105_aifill_prep/checks/check_fc1_seam.py" | tail -4; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `AIFILL FC-1 ARMS: YES (N of N)` with N equal to 12, no `FAIL` arm line above it; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-fc-1"><invocation>cd C:/dev/wk-resapp-430 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python -m pytest -q --color=no -p no:cacheprovider lib/research/aifill/tests/test_model_final_answer.py lib/research/aifill/tests/test_model_inputs.py | tail -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the last non-empty line before `exit=` reads `N passed` (N at least the count your test module's functions define) with no `failed` and no `error` in the last 3 lines; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-fc-1"><invocation>cd C:/dev/wk-resapp-430 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round104_aifill_prep/checks/check_fa2_model.py" | tail -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `AIFILL FA-2 ARMS: YES (21 of 21)`: the round-104 seam check keeps passing (a control, not a hygiene check); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~430 <0.9.0_WK_AMGT_RESAPP~430@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~430/AMGT_RESAPP.TO-AMGT-fc-1.the-model-seam-keeps-only-the-final-answer.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character; each criterion's `expect` recorded as an ordered regex of the printed lines when the prose has regex-active characters.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- each criterion's deciding output line (verbatim) and the arm count;
- the arm lines of AC1 that read FAIL, if any, AC2's pytest summary line and AC3's line.
- any row.
The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** An independent head (the seam does not import the contract). The real defect it fixes is measured, not inferred: 11 stored blocks over 10 names. AC3 is the round-104 check for this same module, kept as a regression control. The builders' prompts and the contract's refusal list (cells fc-2, fc-3) are the second and third lines of defence; this is the structural one.

<status>pending</status>
<round>105</round>
<workstream>AIFILL</workstream>
<slot>0.9.0_WK_AMGT_RESAPP~430</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
