# AMGT_RESAPP task order -- `AMGT-gr-6` -- THE FIVE BUILDERS USE THE SHARED SENTENCE CUT, AND THE BIO NEVER RESTATES THE RESEARCH TEAM'S PASSAGE (FWD-41 ROUND 106; A FIX, CTO 4(b) AND 4(e))

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md</decomp_doc>
<owned_cells>AMGT-gr-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~455</issued_to>
<issued_by>2.0.0_SA_COO~R2</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-gr-6.the-five-builders-use-the-shared-cut-and-the-bio-never-restates-the-pack</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing is scheduled; a library module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, grant, key or policy is touched; the cell writes and tests local Python only.
comp-adversary: RUN at the cut -- `check_gr6_builders.py` is a prepared acceptance check (15 arms, offline, model stubbed: the cut in each builder on a fixture that straddles `Ps.`, a reply within the cap, no end that fits, the restatement rule); against the unchanged builders (with the shared module present) it reads `AIFILL GR-6 ARMS: NO (5 of 15)` (the ten arms for the new behaviour FAIL, including all five cut arms), the build check failing as expected.
EGRESS CLASS, declared: NONE. No network call by the cell or its checks (the model is a stub or a recorded response); no Bloomberg call.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-455` (branch `wk-AMGT_RESAPP-455`, cut from the merged head that carries cell gr-1 (the issuer cuts this worktree after it merges)). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-455`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-gr-6` (round 106, workstream AIFILL, decomposition `org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md`)

Each of the five builders carries its own copy of a cut that ends an over-cap reply at the last `.`, `!` or `?` followed by a space: it took `Ps.` for a sentence end and the KOFUBL MM team view ended `... totaling Ps.` on the page. And the OPAL_SOURCE `mgmt_bio` of V US restated the research team's management passage printed directly above it. You (1) replace the five cuts by the shared module of cell gr-1 and (2) make the bio withhold a restatement.

### Why this cell exists (the CVO's five-name read of 2026-10-14, C-S143 to C-S146; the CTO's ruling `ledger/CTO_RULING_FWD41_FIVE_NAME_READ_NOT_MET_20261014.md`, item 4)
FWD-41 graded NOT REALIZED: of five names read on the PROD page, four carried a stated claim that its cited source does not support or contradicts (a figure the release contradicts; a clause no source carries; a stale board proposal a newer source overtakes), one block ended mid-sentence on `... totaling Ps.`
(the cut took an abbreviation for a sentence end), one was garbled, and the page's panel denied the web input the blocks cite. The AI-fill blocks are held off the PROD page until a re-read of five NEW names passes. The CTO's remedy is a GROUNDING PASS in the producer: before a block is stored, every sentence is checked against
the fetched text of the sources it cites, and a sentence they do not carry is dropped; a citation that does not answer (404, refused) grounds nothing; where dated sources conflict the newest wins; the contract refuses a block whose grounding record is missing.

The package `lib/research/aifill/` already holds `contract.py`, `orchestrate.py`, `model.py`, `inputs.py`, `store.py`, `run.py`, `revalidate.py` and the five `block_<id>.py` modules (all merged; read the ones you touch). Python 3.9, ASCII, stdlib only.

### The change in each of `block_mgmt_bio.py`, `block_mgmt_recent.py`, `block_mgmt_team_view.py`, `block_thesis_pillars.py`, `block_identity_description.py`
1. `from lib.research.aifill import sentences` and the module's own cut function (`_cut`, `_cut_at_sentence`, `_cut_at_sentence_end`) becomes a one-line call to `sentences.cut_at_sentence_end(text, <that module's cap>)`, returning the same shapes as before (the text itself within the cap; the cut text; or `None`, which keeps the existing `too long` reason). Delete the module's own sentence-end loop or regular expression where nothing else uses it. The caps are unchanged (bio 900, recent 800, team view 800, pillars 1000, description 400).
### `block_mgmt_bio.py` only: the restatement rule
2. `RESTATES_REASON = "The research team's passage on this page already says this, so no summary was added."` (exactly). On the OPAL path only, after the reply has passed the existing figure guard and the cut, when the supplied facts include the pack passage (the fact whose ref is `PACK_LABEL`): the reply RESTATES the passage when at least 75 percent of its sentences each have at least 80 percent of their tokens in the passage, where a token is a run of 3 or more lowercase letters or digits (`re.findall(r"[a-z0-9]+", text.lower())` keeping length >= 3) and a sentence comes from `sentences.split_sentences`. A restatement makes the Opal attempt a NONE block with `RESTATES_REASON`; the existing fall-through then runs the web path as for any other Opal NONE, and if both decline the reasons are joined as before. With no pack passage among the facts there is no check.
3. Everything else is unchanged: prompts, caps, guards, citations, the fall-through.

### Tests
Extend the existing `tests/test_block_mgmt_bio.py`, `tests/test_block_mgmt_recent.py` and `tests/test_text_blocks.py`: a cut test per builder using a reply that straddles `Ps.` at the cap, and the bio's restatement cases (restates; adds what the passage lacks; no passage). Touch no existing test except one that asserted the old cut at an abbreviation.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W455-S<k>`, `disarm_owner` `2.0.0_SA_COO~R2`.

## 2. BOUNDS


1. Write ONLY the five `lib/research/aifill/block_*.py` modules named above and the three existing test modules `test_block_mgmt_bio.py`, `test_block_mgmt_recent.py`, `test_text_blocks.py`. The contract, the orchestrator and everything else are other cells'. The modules still do no I/O.
- Leave `lib/research/management/`, `lib/research/filings/`, `lib/research/posture/` and every existing module untouched.
- No network, no AWS, no real model call, no `pip install`: every model call in your tests is a stub or the recorded response. The `anthropic` package is never imported (the installed 0.45.0 crashes on web-search blocks).
- Python 3.9 syntax (`from __future__ import annotations`, `typing.Optional`, no `X | Y` unions evaluated at runtime, no `match`); ASCII-only source files (write non-ASCII characters as `\uXXXX` escapes); stdlib only.
- Run the commit gate before you commit: `bash .tools/commit-gate.sh <each .py you wrote>` (it runs `py_compile` and `ruff`); a finding there is yours to fix.

## 3. SURFACES

<paths>
lib/research/aifill/block_mgmt_bio.py
lib/research/aifill/block_mgmt_recent.py
lib/research/aifill/block_mgmt_team_view.py
lib/research/aifill/block_thesis_pillars.py
lib/research/aifill/block_identity_description.py
lib/research/aifill/tests/test_block_mgmt_bio.py
lib/research/aifill/tests/test_block_mgmt_recent.py
lib/research/aifill/tests/test_text_blocks.py
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-gr-6"><invocation>cd C:/dev/wk-resapp-455 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round106_aifill_prep/checks/check_gr6_builders.py" | tail -4; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `AIFILL GR-6 ARMS: YES (N of N)` with N equal to 15, no `FAIL` arm line above it; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-gr-6"><invocation>cd C:/dev/wk-resapp-455 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python -m pytest -q --color=no -p no:cacheprovider lib/research/aifill/tests/test_block_mgmt_bio.py lib/research/aifill/tests/test_block_mgmt_recent.py lib/research/aifill/tests/test_text_blocks.py | tail -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the last non-empty line before `exit=` reads `N passed` (N at least the count your test module's functions define) with no `failed` and no `error` in the last 3 lines; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-gr-6"><invocation>cd C:/dev/wk-resapp-455 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round105_aifill_prep/checks/check_fc3_prompts.py" | tail -1 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round104_aifill_prep/checks/check_fa3_mgmt_bio.py" | tail -1 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round104_aifill_prep/checks/check_fa4_mgmt_recent.py" | tail -1 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round104_aifill_prep/checks/check_fa5_text_blocks.py" | tail -1; echo "exit=$?"</invocation><expect>the four lines `AIFILL FC-3 ARMS: YES (17 of 17)`, `AIFILL FA-3 ARMS: YES (20 of 20)`, `AIFILL FA-4 ARMS: YES (17 of 17)`, `AIFILL FA-5 ARMS: YES (25 of 25)`: the earlier builder checks keep passing (controls); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~455 <0.9.0_WK_AMGT_RESAPP~455@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~455/AMGT_RESAPP.TO-AMGT-gr-6.the-five-builders-use-the-shared-cut-and-the-bio-never-restates-the-pack.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character; each criterion's `expect` recorded as an ordered regex of the printed lines when the prose has regex-active characters.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- each criterion's deciding output line (verbatim) and the arm count;
- the arm lines of AC1 that read FAIL, if any, AC2's pytest summary line and AC3's four lines.
- any row.
The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** STAGED behind gr-1 (`sentences`) only. Proven satisfiable by the issuer's reference builders (15 of 15) and the check discriminates: the unchanged builders read 10 FAIL arms. The restatement thresholds (75 percent of sentences, 80 percent of tokens) are the issuer's: V US's bio restated its pack passage almost word for word. The web path is not changed by this cell: the orchestrator's grounding step (gr-5) covers it.

<status>staged</status>
<round>106</round>
<workstream>AIFILL</workstream>
<slot>0.9.0_WK_AMGT_RESAPP~455</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
