# AMGT_RESAPP task order -- `AMGT-fc-3` -- THE FIVE BUILDERS' PROMPTS FORBID NARRATION AND NON-ENGLISH SCRIPTS, AND THEIR REFUSAL REASONS NAME WHAT HAPPENED (FWD-41 ROUND 105; A FIX)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md</decomp_doc>
<owned_cells>AMGT-fc-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~432</issued_to>
<issued_by>2.0.0_SA_COO~R2</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-fc-3.the-five-builders-forbid-narration-and-name-the-refusal-truthfully</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing is scheduled; a library module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, grant, key or policy is touched; the cell writes and tests local Python only.
comp-adversary: RUN at the cut -- `check_fc3_prompts.py` is a prepared acceptance check (17 arms: both rules in the web prompt of each of the five blocks and in the four Opal prompts, a narrated reply is NONE saying the model described its work, a reply in another script is NONE saying outside English, an accented name is kept as its ASCII form, a narrated Opal reply falls to the web path, a genuinely overlong reply still says too long); at the base it reads `AIFILL FC-3 ARMS: NO (2 of 17)`, the build check failing as expected.
EGRESS CLASS, declared: NONE. No network call by the cell or its checks (the model is a stub or a recorded response); no Bloomberg call.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-432` (branch `wk-AMGT_RESAPP-432`, cut from the merged head that carries cell fc-2 (the issuer cuts this worktree after fc-2 merges)). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-432`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-fc-3` (round 105, workstream AIFILL, decomposition `org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md`)

The five block builders each carry a system prompt for the web path and one for the Opal path, and each catches a `contract.ContractError` from `make_block` and answers `The model's text was too long to keep, so it was withheld.` for ANY ContractError. After cell fc-2 the contract also raises for process narration and for letters it could not turn into ASCII, so that catch would label them "too long": untrue. You (1) add two rules to every system prompt, and (2) make the ContractError reason say what happened. Five small modules plus their tests.

### Why this cell exists (measured by the CVO on the stored documents, C-S133; the CTO's round-104 analysis, `ledger/ROUND_ANALYSIS.round104.AIFILL.md`)
The producer stored 11 blocks across 10 names that open with the MODEL'S NARRATION, glued to the real answer with no space: `I'll research this now.MUFG announced ...` (8306 JP, 9433 JP, 939 HK, ICT PM, NESN SW, PWR US, RIO LN, SHOP CN, UNVGY US), and stored `Nestl` for `Nestle`
(a non-ASCII letter was DROPPED, not transliterated). Neither has reached a person (the page is not landed) but both are served by the API. The CTO's ruling: the disarm is in the PRODUCER, never by hand-editing documents; the page does not land until a full re-validate of all 95 stored
documents against the new contract reads 0 refused. Round 104's cells are merged; this round changes four of their files.

### The change in each of `block_mgmt_bio.py`, `block_mgmt_recent.py`, `block_mgmt_team_view.py`, `block_thesis_pillars.py`, `block_identity_description.py`
1. **Both system prompts** (`SYSTEM_WEB` and `SYSTEM_OPAL`, in a module that has them) gain, as the last two sentences before the existing `NO_INFORMATION` instruction (or at the end if the module orders them differently), these two sentences EXACTLY:
   - `Answer directly: do not describe what you are going to do or what you searched, and do not address the reader.`
   - `Write every name in English letters (transliterate accents and other scripts); never use another script.`
   A module that builds its system prompt in the user prompt instead carries them there; the check reads `system + " " + prompt`. The `NO_INFORMATION`, plain-text, character-limit and "use ONLY the facts" wording already there is unchanged.
2. **The ContractError reason.** Where the module catches `contract.ContractError` from `contract.make_block`, the reason depends on the exception's message (lowercased): if it contains `narration` -> `The model described its work instead of answering, so the text was withheld.`; else if it contains `dropped` -> `The model used letters outside English, so the text was withheld.`; else the existing `too long` reason. A reply longer than the block's cap still takes the sentence cut first, exactly as before; the `too long` reason still applies when no sentence end fits.
3. Everything else is unchanged: the Opal-then-web fall-through (a NONE from the Opal path, for these new reasons too, runs the web path; if the web path also yields NONE the reasons are joined), the numeric guard, the limits, the citation checks.

### Tests
Extend the existing test modules `lib/research/aifill/tests/test_block_mgmt_bio.py`, `test_block_mgmt_recent.py` and `test_text_blocks.py`: for each block, a test that both prompt rules are present on each path and a test that a narrated reply and a dropped-letter reply give the new reasons (the stub model returns the text; the real contract refuses it). Touch no existing test except one that asserted the old "too long" label for such a reply.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W432-S<k>`, `disarm_owner` `2.0.0_SA_COO~R2`.

## 2. BOUNDS


1. Write ONLY the five `lib/research/aifill/block_*.py` modules named above and the three existing test modules `test_block_mgmt_bio.py`, `test_block_mgmt_recent.py`, `test_text_blocks.py`. The contract, the seam, the orchestrator, the store and everything else are other cells'. The modules still do no I/O.
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
  <criterion id="AC1" cell_refs="AMGT-fc-3"><invocation>cd C:/dev/wk-resapp-432 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round105_aifill_prep/checks/check_fc3_prompts.py" | tail -4; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `AIFILL FC-3 ARMS: YES (N of N)` with N equal to 17, no `FAIL` arm line above it; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-fc-3"><invocation>cd C:/dev/wk-resapp-432 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python -m pytest -q --color=no -p no:cacheprovider lib/research/aifill/tests/test_block_mgmt_bio.py lib/research/aifill/tests/test_block_mgmt_recent.py lib/research/aifill/tests/test_text_blocks.py | tail -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the last non-empty line before `exit=` reads `N passed` (N at least the count your test module's functions define) with no `failed` and no `error` in the last 3 lines; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-fc-3"><invocation>cd C:/dev/wk-resapp-432 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round104_aifill_prep/checks/check_fa3_mgmt_bio.py" | tail -1 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round104_aifill_prep/checks/check_fa4_mgmt_recent.py" | tail -1 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round104_aifill_prep/checks/check_fa5_text_blocks.py" | tail -1; echo "exit=$?"</invocation><expect>the three lines `AIFILL FA-3 ARMS: YES (20 of 20)`, `AIFILL FA-4 ARMS: YES (17 of 17)`, `AIFILL FA-5 ARMS: YES (25 of 25)`: the round-104 builder checks keep passing (controls); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~432 <0.9.0_WK_AMGT_RESAPP~432@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~432/AMGT_RESAPP.TO-AMGT-fc-3.the-five-builders-forbid-narration-and-name-the-refusal-truthfully.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character; each criterion's `expect` recorded as an ordered regex of the printed lines when the prose has regex-active characters.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- each criterion's deciding output line (verbatim) and the arm count;
- the arm lines of AC1 that read FAIL, if any, AC2's pytest summary line and AC3's three lines.
- any row.
The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** STAGED behind `AMGT-fc-2`'s merge: the check's narration and dropped-letter arms exercise the NEW contract (the stub model returns the text; `make_block` refuses it; the builder names the refusal). This is the third line of defence after the seam (fc-1) and the contract (fc-2): a model that still narrates costs one NONE block with a truthful reason instead of a stored lie. The driver's retry rule (the issuer's `store_batch.py`) is extended by the issuer to retry on these two reasons.

<status>staged</status>
<status>pending -- 2026-10-14 by the issuer (2.0.0_SA_COO~R2): fc-2 merged @49219a610b; worker ~432 cut from that head.</status>
<status>complete -- 2026-10-14 by the issuer (2.0.0_SA_COO~R2): wk-AMGT_RESAPP-432 @39ddc3fa71 merged @6fd4030c31, proof instance VALID (rc=0). AC1 PASS (`AIFILL FC-3 ARMS: YES (17 of 17)`, re-run by the issuer on the merged tree, same line), AC2 PASS (168 passed in the worker's tree; the aifill package 498 passed on the merged tree), AC3 PASS (FA-3 20/20, FA-4 17/17, FA-5 25/25). Worker rows W432-S1 (departure: a foreign letter beyond the sentence cut also refuses; accepted, stricter than the order) and W432-S2 (the base read 4 of 17, not 2) are observations.</status>
<round>105</round>
<workstream>AIFILL</workstream>
<slot>0.9.0_WK_AMGT_RESAPP~432</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
