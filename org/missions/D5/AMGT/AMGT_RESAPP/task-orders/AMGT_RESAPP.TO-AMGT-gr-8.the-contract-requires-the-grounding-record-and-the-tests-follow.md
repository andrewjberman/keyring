# AMGT_RESAPP task order -- `AMGT-gr-8` -- THE CONTRACT REQUIRES THE GROUNDING RECORD, THE BUILDERS' DRAFTS ARE DRAFTS, AND THE EARLIER TESTS FOLLOW (FWD-41 ROUND 106; A FIX, CTO 4(a))

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md</decomp_doc>
<owned_cells>AMGT-gr-8</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~457</issued_to>
<issued_by>2.0.0_SA_COO~R2</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-gr-8.the-contract-requires-the-grounding-record-and-the-tests-follow</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing is scheduled; a library module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, grant, key or policy is touched; the cell writes and tests local Python only.
comp-adversary: RUN at the cut -- `check_gr8_required.py` is a prepared acceptance check (10 arms, offline: the real builders, orchestrator and grounding with a router model and a stub fetch, under the requirement); at the base it reads `AIFILL GR-8 ARMS: NO (1 of 10)`, the build check failing as expected.
EGRESS CLASS, declared: NONE. No network call by the cell or its checks (the model is a stub or a recorded response); no Bloomberg call.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-457` (branch `wk-AMGT_RESAPP-457`, cut from the merged head that carries cells gr-1 to gr-6 (the issuer cuts this worktree after they merge)). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-457`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-gr-8` (round 106, workstream AIFILL, decomposition `org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md`)

Cell gr-4 added the grounding record behind a switch left OFF, and cell gr-5 grounds every filled block in the orchestrator. This cell turns the requirement ON: from here the contract refuses a filled block without a record, so an ungrounded document cannot be built, written or pass `revalidate`.

### Why this cell exists (the CVO's five-name read of 2026-10-14, C-S143 to C-S146; the CTO's ruling `ledger/CTO_RULING_FWD41_FIVE_NAME_READ_NOT_MET_20261014.md`, item 4)
FWD-41 graded NOT REALIZED: of five names read on the PROD page, four carried a stated claim that its cited source does not support or contradicts (a figure the release contradicts; a clause no source carries; a stale board proposal a newer source overtakes), one block ended mid-sentence on `... totaling Ps.`
(the cut took an abbreviation for a sentence end), one was garbled, and the page's panel denied the web input the blocks cite. The AI-fill blocks are held off the PROD page until a re-read of five NEW names passes. The CTO's remedy is a GROUNDING PASS in the producer: before a block is stored, every sentence is checked against
the fetched text of the sources it cites, and a sentence they do not carry is dropped; a citation that does not answer (404, refused) grounds nothing; where dated sources conflict the newest wins; the contract refuses a block whose grounding record is missing.

The package `lib/research/aifill/` already holds `contract.py`, `orchestrate.py`, `model.py`, `inputs.py`, `store.py`, `run.py`, `revalidate.py` and the five `block_<id>.py` modules (all merged; read the ones you touch). Python 3.9, ASCII, stdlib only.

### The changes
1. `contract.py`: `GROUNDING_REQUIRED = True`. Nothing else in that file.
2. The five `block_*.py` builders produce DRAFTS (the orchestrator grounds them): every `contract.make_block(...)` call in them passes `require_grounding=False`. Nothing else in those files.
3. `orchestrate.py`: nothing to change if cell gr-5 left `_usable` and the final document check as specified (drafts validated with `require_grounding=False`; the document with `require_grounding=ground`); if it did not, make it so.
4. The earlier tests that build filled blocks or documents without a record now fail the requirement. Add a test helper module `lib/research/aifill/tests/grounded.py` (no `__init__.py` changes) with `grounded_web_block(block_id="mgmt_bio", text=..., urls=(...))` and `grounded_opal_block(block_id=..., text=..., ref=...)` that return blocks valid under the requirement (a record built by hand: one source per url or ref, one SUPPORTED sentence per sentence of `text` with a quote of at least 12 characters, the citations matching), and move the failing tests onto it (or onto `require_grounding=False`/`ground=False` where the test is about something else). Change only what the requirement breaks, and list the tests you changed in your report. The package must read all passed.

### Tests
Your helper module is exercised by the tests that use it; add `tests/test_grounded_helper.py` with a few tests that its blocks validate under the requirement and that a mutation (a changed text, a dropped citation) is refused.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W457-S<k>`, `disarm_owner` `2.0.0_SA_COO~R2`.

## 2. BOUNDS


1. Write ONLY `lib/research/aifill/contract.py` (the one switch), the `make_block` calls of the five `lib/research/aifill/block_*.py`, `lib/research/aifill/orchestrate.py` (only if item 3 requires), `lib/research/aifill/tests/grounded.py`, `lib/research/aifill/tests/test_grounded_helper.py` and the existing test modules the requirement breaks. No other file.
- Leave `lib/research/management/`, `lib/research/filings/`, `lib/research/posture/` and every existing module untouched.
- No network, no AWS, no real model call, no `pip install`: every model call in your tests is a stub or the recorded response. The `anthropic` package is never imported (the installed 0.45.0 crashes on web-search blocks).
- Python 3.9 syntax (`from __future__ import annotations`, `typing.Optional`, no `X | Y` unions evaluated at runtime, no `match`); ASCII-only source files (write non-ASCII characters as `\uXXXX` escapes); stdlib only.
- Run the commit gate before you commit: `bash .tools/commit-gate.sh <each .py you wrote>` (it runs `py_compile` and `ruff`); a finding there is yours to fix.

## 3. SURFACES

<paths>
lib/research/aifill/contract.py
lib/research/aifill/orchestrate.py
lib/research/aifill/block_mgmt_bio.py
lib/research/aifill/block_mgmt_recent.py
lib/research/aifill/block_mgmt_team_view.py
lib/research/aifill/block_thesis_pillars.py
lib/research/aifill/block_identity_description.py
lib/research/aifill/tests/grounded.py
lib/research/aifill/tests/test_grounded_helper.py
lib/research/aifill/tests/test_block_mgmt_bio.py
lib/research/aifill/tests/test_block_mgmt_recent.py
lib/research/aifill/tests/test_text_blocks.py
lib/research/aifill/tests/test_contract_orchestrate.py
lib/research/aifill/tests/test_contract_v2.py
lib/research/aifill/tests/test_contract_grounding.py
lib/research/aifill/tests/test_orchestrate_grounding.py
lib/research/aifill/tests/test_store_run.py
lib/research/aifill/tests/test_revalidate.py
lib/research/aifill/tests/test_model_final_answer.py
lib/research/aifill/tests/test_model_inputs.py
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-gr-8"><invocation>cd C:/dev/wk-resapp-457 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round106_aifill_prep/checks/check_gr8_required.py" | tail -4; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `AIFILL GR-8 ARMS: YES (N of N)` with N equal to 10, no `FAIL` arm line above it; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-gr-8"><invocation>cd C:/dev/wk-resapp-457 &amp;&amp; PYTHONPATH="$(pwd)" timeout 600 python -m pytest -q --color=no -p no:cacheprovider lib/research/aifill/tests | tail -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the last non-empty line before `exit=` reads `N passed` (N at least 498) with no `failed` and no `error` in the last 3 lines; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-gr-8"><invocation>cd C:/dev/wk-resapp-457 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python -m pytest -q --color=no -p no:cacheprovider lib/research/api/tests/test_ai_fill_serve.py | tail -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the last non-empty line before `exit=` reads `N passed` with no `failed` and no `error` in the last 3 lines (the served validator is untouched and still passes); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~457 <0.9.0_WK_AMGT_RESAPP~457@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~457/AMGT_RESAPP.TO-AMGT-gr-8.the-contract-requires-the-grounding-record-and-the-tests-follow.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character; each criterion's `expect` recorded as an ordered regex of the printed lines when the prose has regex-active characters.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- each criterion's deciding output line (verbatim) and the arm count;
- the arm lines of AC1 that read FAIL, if any, AC2's and AC3's pytest summary lines, and the list of existing tests you changed.
- any row.
The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** STAGED behind gr-5 and gr-6 (and so behind gr-1 to gr-4). The reference run (all earlier references merged, requirement on) reads 9 of 10: the tenth arm is the helper file this cell creates. After this merges, every document the producer writes carries a record and `revalidate` refuses all 95 stored round-105 documents (`grounding record is missing`): that is the point of the re-run.

<status>staged</status>
<round>106</round>
<workstream>AIFILL</workstream>
<slot>0.9.0_WK_AMGT_RESAPP~457</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
