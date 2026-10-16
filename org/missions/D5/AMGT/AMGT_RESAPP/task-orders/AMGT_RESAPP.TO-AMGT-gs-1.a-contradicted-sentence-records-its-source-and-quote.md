# AMGT_RESAPP task order -- `AMGT-gs-1` -- A CONTRADICTED SENTENCE RECORDS THE SOURCE THAT CONTRADICTED IT AND A QUOTE CHECKED AGAINST THAT SOURCE (FWD-41 ROUND 107, ROW W452-S1; A DIRECT ACT)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md</decomp_doc>
<owned_cells>AMGT-gs-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~481</issued_to>
<issued_by>2.0.0_SA_COO~R2</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-gs-1.a-contradicted-sentence-records-its-source-and-quote</to_id>
<placeholders>NONE</placeholders>
<direct_act>true</direct_act>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing is scheduled; a library module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, grant, key or policy is touched; the cell writes and tests local Python only.
comp-adversary: RUN at the cut -- `check_gs1_contradicted.py` is a prepared acceptance check (11 arms); at the base it reads `AIFILL GS-1 ARMS: NO (8 of 11)`, the build check failing as expected, and the issuer's reference edit in a scratch copy reads 11 of 11.
EGRESS CLASS, declared: NONE. No network call by the cell or its checks (the model is a stub); no Bloomberg call.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-481` (branch `wk-AMGT_RESAPP-481`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-481`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-gs-1` (round 107, workstream AIFILL, decomposition `org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md` section 15)

`lib/research/aifill/grounding.py` checks every sentence of a block against its sources through one model call and records one entry per sentence: `{"text", "verdict", "source", "quote"}`, verdict one of SUPPORTED, UNSUPPORTED, CONTRADICTED. Today a CONTRADICTED sentence is always recorded with `source` None and `quote` None (`_judge`, the `if verdict == "CONTRADICTED":` branch), so the record never says which source contradicted it. You make it say so, with the same mechanical check a SUPPORTED quote gets.

### Why (row `AMGT_RESAPP-D1-W452-S1`, REMEDIATION_v44)
The CVO's five-name read found stated claims that a newer source overtakes (a stale board proposal). The grounding pass drops such a sentence as CONTRADICTED, but the stored record cannot be audited for WHICH source overtook it. The remedy the row names: the record carries the contradicting source index and quote.

### The changes in `lib/research/aifill/grounding.py` (everything not listed keeps its behaviour)
1. `SYSTEM` (the module's system prompt string): keep every existing word, and after the sentence `"For each SUPPORTED verdict give the source label (S1, S2, ...) and a verbatim quote of at most 200 characters, copied exactly from that source. "` add one more sentence, exactly: `For each CONTRADICTED verdict give the source label and a verbatim quote of at most 200 characters from the source that states otherwise. ` (the prompt must still begin with the words `You check sentences against sources.`; the check reads the substring `For each CONTRADICTED verdict give the source label`).
2. `_judge`, the CONTRADICTED branch. The verdict stays CONTRADICTED in every case, so the sentence stays dropped from the block text. Resolve the row's `source` label with `_shown_index(row.get("source"), len(usable))` and take `row.get("quote")`. Only when the label names a SHOWN source (k is not None), the quote is a `str` of at least `MIN_QUOTE` characters, and `_norm(quote)` is a substring of `norm_full[k - 1]`, return `{"text": sent_text, "verdict": "CONTRADICTED", "source": usable[k - 1]["index"], "quote": quote}` (the `source` is the index into the caller's source LIST, exactly as a SUPPORTED sentence's is, so it differs from the label number when an earlier source was not shown). In every other case return what the branch returns today: `source` None and `quote` None.
3. Nothing else changes: a CONTRADICTED source is never a supporting source, so `used_urls`, `used_labels` and `kept` are computed from SUPPORTED sentences only, as now; `contract.py` needs no edit (it skips every sentence that is not SUPPORTED); an UNSUPPORTED row that carries a source and a quote still records None and None. Add one line to the module docstring naming the new rule.

### Tests
- One existing test pins the old behaviour: `lib/research/aifill/tests/test_grounding.py::test_contradicted_is_dropped_and_recorded_as_such` (its row 3 is `CONTRADICTED` naming `S1` and the valid quote `elected Pablo Isla as Chairman in October 2025`; it asserts `source is None` near line 119). Update ONLY that test's assertions about the CONTRADICTED sentence's `source` and `quote`: `source` is now `0` (S1 is the first source of that test's `sources()`) and `quote` is the quote given. Touch no other test in that file.
- A new module `lib/research/aifill/tests/test_grounding_contradicted.py` (no `__init__.py`; model your helpers on `test_grounding.py`): at least four tests: (a) a CONTRADICTED row with a valid quote records the list index and the quote while the sentence is absent from `result.text`; (b) a quote the source does not hold, a source label that was not shown, and a quote under 12 characters each record None and None and stay CONTRADICTED; (c) when the first source did not answer (status NOT_FOUND) the recorded index is the LIST index, not the label number; (d) the contradicting source is absent from `used_urls` when no sentence it supports is kept.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W481-S<k>`, `disarm_owner` `2.0.0_SA_COO~R2`.

## 2. BOUNDS

1. Write ONLY the files in the `<paths>` block below. `contract.py`, `orchestrate.py`, the builders and every other module are other cells'.
- No network, no AWS, no real model call, no `pip install`: every model call in your tests is a stub. The `anthropic` package is never imported.
- Python 3.9 syntax (`from __future__ import annotations`, `typing.Optional`, no `X | Y` unions evaluated at runtime, no `match`); ASCII-only source files (write non-ASCII characters as `\uXXXX` escapes); stdlib only.
- Run the commit gate before you commit: `bash .tools/commit-gate.sh <each .py you wrote>` (it runs `py_compile` and `ruff`); a finding there is yours to fix.

## 3. SURFACES

<paths>
lib/research/aifill/grounding.py
lib/research/aifill/tests/test_grounding.py
lib/research/aifill/tests/test_grounding_contradicted.py
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-gs-1"><invocation>cd C:/dev/wk-resapp-481 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round107_aifill_prep/checks/check_gs1_contradicted.py" | tail -4; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `AIFILL GS-1 ARMS: YES (N of N)` with N equal to 11, no `FAIL` arm line above it; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-gs-1"><invocation>cd C:/dev/wk-resapp-481 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python -m pytest -q --color=no -p no:cacheprovider lib/research/aifill/tests/test_grounding.py lib/research/aifill/tests/test_grounding_contradicted.py | tail -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the last non-empty line before `exit=` reads `N passed` (N at least 51) with no `failed` and no `error` in the last 3 lines; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~481 <0.9.0_WK_AMGT_RESAPP~481@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~481/AMGT_RESAPP.TO-AMGT-gs-1.a-contradicted-sentence-records-its-source-and-quote.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character; each criterion's `expect` recorded as an ordered regex of the printed lines when the prose has regex-active characters.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- each criterion's deciding output line (verbatim) and the arm count;
- the arm lines of AC1 that read FAIL, if any, and AC2's pytest summary line;
- any row.
The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** DIRECT-ACT: one cell, about 15 product lines in `grounding.py` plus tests, LOCAL; it runs no L2, no L4-R and no L8-L10 and its close is the issuer's one real run (the aifill suite plus the api serve test at the merged head, and `lib.research.aifill.revalidate` re-run over the 95 stored documents, unchanged at 95 of 95 refused). Proven satisfiable by the issuer's reference edit in a scratch copy (11 of 11); that edit breaks exactly one existing test, the one named above, which this order grants. The CTO's alternative reading of the row ("or the CTO rules null the contract", item (g)) is not taken; if the CTO later rules null, reverting is the one `_judge` branch and one assertion. The row's close: this seat reads the rule at the merged pin, then disarms `AMGT_RESAPP-D1-W452-S1` by a channel row.

<status>pending</status>
<round>107</round>
<workstream>AIFILL</workstream>
<slot>0.9.0_WK_AMGT_RESAPP~481</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
