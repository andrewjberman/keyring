# AMGT_RESAPP task order -- `AMGT-gr-4` -- THE CONTRACT CARRIES A GROUNDING RECORD PER FILLED BLOCK AND CAN REFUSE A BLOCK WITHOUT ONE, BEHIND A SWITCH (FWD-41 ROUND 106; A BUILD, CTO 4(a))

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md</decomp_doc>
<owned_cells>AMGT-gr-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~453</issued_to>
<issued_by>2.0.0_SA_COO~R2</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-gr-4.the-contract-carries-a-grounding-record-and-can-refuse-a-block-without-one</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing is scheduled; a library module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, grant, key or policy is touched; the cell writes and tests local Python only.
comp-adversary: RUN at the cut -- `check_gr4_contract.py` is a prepared acceptance check (26 arms: the record's shape, every refusal, make_block, folding, the document, the switch); at the base it reads `AIFILL GR-4 ARMS: NO (1 of 26)`, the build check failing as expected.
EGRESS CLASS, declared: NONE. No network call by the cell or its checks (the model is a stub or a recorded response); no Bloomberg call.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-453` (branch `wk-AMGT_RESAPP-453`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-453`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-gr-4` (round 106, workstream AIFILL, decomposition `org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md`)

`lib/research/aifill/contract.py` is the one shape and the one validator of the fill document. You add the grounding record and the refusal of a filled block that has none, behind a module switch that is OFF in this cell (cell gr-8 turns it on once the producer makes records), so every earlier check and test keeps passing.

### Why this cell exists (the CVO's five-name read of 2026-10-14, C-S143 to C-S146; the CTO's ruling `ledger/CTO_RULING_FWD41_FIVE_NAME_READ_NOT_MET_20261014.md`, item 4)
FWD-41 graded NOT REALIZED: of five names read on the PROD page, four carried a stated claim that its cited source does not support or contradicts (a figure the release contradicts; a clause no source carries; a stale board proposal a newer source overtakes), one block ended mid-sentence on `... totaling Ps.`
(the cut took an abbreviation for a sentence end), one was garbled, and the page's panel denied the web input the blocks cite. The AI-fill blocks are held off the PROD page until a re-read of five NEW names passes. The CTO's remedy is a GROUNDING PASS in the producer: before a block is stored, every sentence is checked against
the fetched text of the sources it cites, and a sentence they do not carry is dropped; a citation that does not answer (404, refused) grounds nothing; where dated sources conflict the newest wins; the contract refuses a block whose grounding record is missing.

### The grounding record (ratified here; cells gr-3, gr-4, gr-5 and gr-8 all write against it)
A filled block (`WEB_SEARCH` or `OPAL_SOURCE`) carries one more key, `grounding` (a `NONE` block carries none, and the earlier eight keys do not change):
```
"grounding": { "version": "grounding/1", "checked_at": "YYYY-MM-DDTHH:MM:SSZ",
  "sources":   [ { "url": str|null, "label": str|null, "kind": "web"|"opal", "status": "OK"|"REFUSED"|"NOT_FOUND"|"ERROR"|"EMPTY"|"PAYWALL"|"UNSUPPORTED", "http_status": int|null, "chars": int } ],
  "sentences": [ { "text": str, "verdict": "SUPPORTED"|"UNSUPPORTED"|"CONTRADICTED", "source": int|null, "quote": str|null } ],
  "model_call": { "model": str|null, "input_tokens": int, "output_tokens": int } | null }
```
`sources` lists every source offered (the order the caller gave); a SUPPORTED sentence's `source` is an index into it, that source's `status` is `OK`, and its `quote` is a verbatim run of at least 12 characters copied from that source. The block's `text` is EXACTLY the SUPPORTED sentences joined by single spaces, in order.
A `WEB_SEARCH` block is grounded only on `web` sources and each of its web citations is the `url` of a source that supports at least one kept sentence (and every supporting source is cited); an `OPAL_SOURCE` block is grounded only on `opal` sources whose `label` is the plain-words `ref` of one of its opal citations.
The grounding call is a model call WITHOUT web search; its system prompt begins with the exact words `You check sentences against sources.`, its user prompt lists the sources then the sentences as numbered lines `N. text` after a line `SENTENCES`, and the quote of a SUPPORTED verdict is checked MECHANICALLY against the source's full text (case, spacing and punctuation ignored), never trusted.

The package `lib/research/aifill/` already holds `contract.py`, `orchestrate.py`, `model.py`, `inputs.py`, `store.py`, `run.py`, `revalidate.py` and the five `block_<id>.py` modules (all merged; read the ones you touch). Python 3.9, ASCII, stdlib only.

### The changes in `lib/research/aifill/contract.py` (everything not listed keeps its behaviour)
1. `PRODUCER_VERSION = "opal-aifill/1.1.0"`. `GROUNDING_REQUIRED = False` (module constant); `GROUNDING_VERSION = "grounding/1"`; `MIN_QUOTE = 12`.
2. A filled block may carry the extra key `grounding`; the block key rule becomes: the eight keys, or the eight plus `grounding` (a NONE block carries exactly the eight: `none_block` is unchanged; a NONE block holding the key `grounding` with anything but `None`, is refused, and the problem text contains the word `grounding`).
3. `validate_block(block, require_grounding=None)`: the flag defaults to `GROUNDING_REQUIRED`. For a filled block (`WEB_SEARCH` or `OPAL_SOURCE`): a missing key or a `None` value is a problem `grounding record is missing` when the flag is true, and no problem when it is false; a record that is present is ALWAYS checked, whatever the flag. Every problem about the record contains the word `grounding`. The checks of a present record, in the words of the record section above: the `version`; `sources` and `sentences` are lists and `sentences` is not empty; each sentence has a verdict from the three words; each SUPPORTED sentence names an existing source, whose status is `OK`, with a quote of at least `MIN_QUOTE` characters; the block `text` equals the SUPPORTED sentence texts joined by single spaces (that one equality is the whole test: a sentence that is not SUPPORTED cannot be in the text); for a `WEB_SEARCH` block every supporting source is `kind` web, each supporting url is among the block's web citations, and each web citation's url is the url of a supporting source (a citation that supports no sentence is a problem whose text contains `support`); for an `OPAL_SOURCE` block every supporting source is `kind` opal and each opal citation's `ref` is the `label` of a supporting source.
4. `validate_document(doc, require_grounding=None)` passes the flag to every block (problems keep their `<block id>: ` prefix).
5. `make_block(..., grounding=None, require_grounding=None)`: when `grounding` is given its strings are folded to ASCII exactly as the block text is (`fold_text`, so `Nestl\u00e9` becomes `Nestle`); the finished block is validated with the flag and a problem raises `ContractError` whose message contains `grounding`.

### Tests
A new test module `lib/research/aifill/tests/test_contract_grounding.py` (no `__init__.py`): at least one test per refusal above, the switch both ways, the folding, and a JSON round trip. If a test in `tests/test_contract_orchestrate.py` or `tests/test_contract_v2.py` asserts the old version string or the exact eight keys of a FILLED block, update that one assertion; touch nothing else in those files.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W453-S<k>`, `disarm_owner` `2.0.0_SA_COO~R2`.

## 2. BOUNDS


1. Write ONLY `lib/research/aifill/contract.py`, `lib/research/aifill/tests/test_contract_grounding.py` and, only for an assertion on the old version string or key set, `tests/test_contract_orchestrate.py` and `tests/test_contract_v2.py`. The orchestrator, the builders and everything else are other cells'.
- Leave `lib/research/management/`, `lib/research/filings/`, `lib/research/posture/` and every existing module untouched.
- No network, no AWS, no real model call, no `pip install`: every model call in your tests is a stub or the recorded response. The `anthropic` package is never imported (the installed 0.45.0 crashes on web-search blocks).
- Python 3.9 syntax (`from __future__ import annotations`, `typing.Optional`, no `X | Y` unions evaluated at runtime, no `match`); ASCII-only source files (write non-ASCII characters as `\uXXXX` escapes); stdlib only.
- Run the commit gate before you commit: `bash .tools/commit-gate.sh <each .py you wrote>` (it runs `py_compile` and `ruff`); a finding there is yours to fix.

## 3. SURFACES

<paths>
lib/research/aifill/contract.py
lib/research/aifill/tests/test_contract_grounding.py
lib/research/aifill/tests/test_contract_orchestrate.py
lib/research/aifill/tests/test_contract_v2.py
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-gr-4"><invocation>cd C:/dev/wk-resapp-453 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round106_aifill_prep/checks/check_gr4_contract.py" | tail -4; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `AIFILL GR-4 ARMS: YES (N of N)` with N equal to 26, no `FAIL` arm line above it; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-gr-4"><invocation>cd C:/dev/wk-resapp-453 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python -m pytest -q --color=no -p no:cacheprovider lib/research/aifill/tests | tail -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the last non-empty line before `exit=` reads `N passed` (N at least 498) with no `failed` and no `error` in the last 3 lines; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-gr-4"><invocation>cd C:/dev/wk-resapp-453 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round105_aifill_prep/checks/check_fc2_contract.py" | tail -1 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round104_aifill_prep/checks/check_fa1_contract.py" | tail -1; echo "exit=$?"</invocation><expect>the two lines `AIFILL FC-2 ARMS: YES (43 of 43)` and `AIFILL FA-1 ARMS: YES (31 of 31)`: the earlier contract checks keep passing (controls); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~453 <0.9.0_WK_AMGT_RESAPP~453@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~453/AMGT_RESAPP.TO-AMGT-gr-4.the-contract-carries-a-grounding-record-and-can-refuse-a-block-without-one.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character; each criterion's `expect` recorded as an ordered regex of the printed lines when the prose has regex-active characters.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- each criterion's deciding output line (verbatim) and the arm count;
- the arm lines of AC1 that read FAIL, if any, AC2's pytest summary line and AC3's two lines.
- any row.
The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** An independent head; proven satisfiable by the issuer's reference (26 of 26). The switch is OFF here by design: turning it on in this cell would break every builder test that makes a filled block without a record. Cell gr-8 turns it on and brings those tests onto a shared helper. A key present with value None counts as absent (the issuer's reference treats it so; the check's 'switch decides' arm asserts it).

<status>pending</status>
<status>complete -- 2026-10-14 by the issuer (2.0.0_SA_COO~R2): wk-AMGT_RESAPP-453 @5c81a53406 merged @0516c67e6d, proof instance VALID (rc=0). AC1 PASS (`AIFILL GR-4 ARMS: YES (26 of 26)`, re-run by the issuer), AC2 PASS (534 passed), AC3 PASS (FC-2 43 of 43, FA-1 31 of 31).</status>
<round>106</round>
<workstream>AIFILL</workstream>
<slot>0.9.0_WK_AMGT_RESAPP~453</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
