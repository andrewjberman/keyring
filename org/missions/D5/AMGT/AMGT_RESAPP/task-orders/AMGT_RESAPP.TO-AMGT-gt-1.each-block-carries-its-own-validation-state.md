# AMGT_RESAPP task order -- `AMGT-gt-1` -- EACH BLOCK OF A STORED FILL DOCUMENT CARRIES ITS OWN VALIDATION STATE (FWD-41 ROUND 108, CTO 6446 (A); A DIRECT ACT)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md</decomp_doc>
<owned_cells>AMGT-gt-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~482</issued_to>
<issued_by>2.0.0_SA_COO~R2</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-gt-1.each-block-carries-its-own-validation-state</to_id>
<placeholders>NONE</placeholders>
<direct_act>true</direct_act>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing is scheduled; a library module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, grant, key or policy is touched; the cell writes and tests local Python only.
comp-adversary: RUN at the cut -- `check_gs2_validation.py` is a prepared acceptance check (16 arms); at the base it reads `AIFILL GS-2 ARMS: NO (1 of 16)`, the build check failing as expected, and the issuer's reference edit in a scratch copy reads 16 of 16.
EGRESS CLASS, declared: NONE. No network call by the cell or its checks; no Bloomberg call.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-482` (branch `wk-AMGT_RESAPP-482`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-482`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-gt-1` (round 108, workstream AIFILL, decomposition `org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md` section 16)

A fill document (`lib/research/aifill/contract.py`, schema `aifill/v1`) holds five blocks; a block is a dict whose keys are the eight `BLOCK_KEYS`, plus optionally `grounding`. Stored documents are read by other tools that pass each block through whole. You add ONE more optional block key, `validation`, so a reader sees beside the text whether the block passed the contract and whether it is still held back until a human read clears it. Everything not listed keeps its behaviour.

### Changes in `lib/research/aifill/contract.py`
1. Constants (beside `GROUNDING_KEY`): `VALIDATION_KEY = "validation"`; `VALIDATION_VERSION = "validation/1"`; `VALIDATION_KEYS = frozenset(("version", "state", "verdict", "contract", "checked_at"))`; `VALIDATION_STATES = ("HELD", "CLEARED")`; `VALIDATION_VERDICTS = ("PASS", "REFUSED")`.
2. The block key rule in `validate_block`: a block's keys must contain all eight `BLOCK_KEYS` and may add `grounding` and/or `validation` and nothing else (today it allows the eight, or the eight plus `grounding`). Keep the existing problem text `block keys differ from the eight block keys (extra ..., missing ...)` for a breach. The key is optional with NO switch: a block without it is valid; a block with it is always checked. It is allowed on every block, a NONE block included.
3. A new function `_validation_problems(state)` returning a list of problem strings, each STARTING with the word `validation`, called from `validate_block` when the key is present (`VALIDATION_KEY in block`). A present value that is not a dict (None included): `validation must be a dict`. Keys not exactly `VALIDATION_KEYS`: `validation keys differ from the five validation keys (extra ..., missing ...)` and stop. Otherwise one problem each for: `version` not `VALIDATION_VERSION`; `state` not in `VALIDATION_STATES`; `verdict` not in `VALIDATION_VERDICTS`; `contract` not a non-empty str; `checked_at` not matching the existing `_STAMP_SHAPE` (`YYYY-MM-DDTHH:MM:SSZ`); and state `CLEARED` with verdict `REFUSED` (`validation of a REFUSED block cannot be CLEARED`).

### New module `lib/research/aifill/validation.py` (stdlib plus `contract`, no I/O, no clock read, ASCII)
`stamp_validation(doc, now, state="HELD")` returns a DEEP COPY of the document (`copy.deepcopy`; the input is not changed) in which every block carries a `validation` dict: `version` = `contract.VALIDATION_VERSION`, `state` = the argument, `verdict` = `"PASS"` when `contract.validate_block(block)` (called on the block with any existing `validation` key removed) returns no problem, else `"REFUSED"`, `contract` = `contract.PRODUCER_VERSION`, `checked_at` = `now` as `%Y-%m-%dT%H:%M:%SZ` in UTC. Raises `contract.ContractError` when: `state` is not in `VALIDATION_STATES` (message contains `validation`); `now` is not a timezone-aware `datetime.datetime` (message contains `validation`); or `state` is `CLEARED` and any block's verdict is `REFUSED` (message contains `validation`). A block that fails the contract does NOT raise under HELD: it is stamped REFUSED.

### Tests
A new module `lib/research/aifill/tests/test_validation.py` (no `__init__.py`; build a valid grounded document the way `tests/test_contract_grounding.py` does, or from `contract.make_block` and `contract.none_block`): at least TEN tests covering: every block stamped with the five keys; the NONE block stamped; the input not changed; the stamped document passes `validate_document`; a contract-breaking block stamped REFUSED and HELD while the others PASS; CLEARED stamped over an all-PASS document; CLEARED over a REFUSED block raises; an unknown state raises; a naive or missing time raises; each malformed validation (wrong version, state, verdict, empty contract, bad stamp, extra key, missing key, a non-dict, None, CLEARED with REFUSED) is a problem starting with `validation`; the block key rule (grounding only, validation only, both, an unknown third key refused); the JSON round trip. If an existing test in `tests/test_contract_grounding.py`, `tests/test_contract_v2.py` or `tests/test_contract_orchestrate.py` pins the old key rule, update that one assertion only (the issuer's reference needed none).

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W482-S<k>`, `disarm_owner` `2.0.0_SA_COO~R2`.

## 2. BOUNDS

1. Write ONLY the files in the `<paths>` block below. `orchestrate.py`, `run.py`, `store.py`, `revalidate.py`, `grounding.py`, the builders and every other module are other cells'; do not make any of them stamp or require the key.
- No network, no AWS, no real model call, no `pip install`.
- Python 3.9 syntax (`from __future__ import annotations`, no `X | Y` unions evaluated at runtime, no `match`); ASCII-only source files (write non-ASCII characters as `\uXXXX` escapes); stdlib only.
- Run the commit gate before you commit: `bash .tools/commit-gate.sh <each .py you wrote>` (it runs `py_compile` and `ruff`); a finding there is yours to fix.

## 3. SURFACES

<paths>
lib/research/aifill/contract.py
lib/research/aifill/validation.py
lib/research/aifill/tests/test_validation.py
lib/research/aifill/tests/test_contract_grounding.py
lib/research/aifill/tests/test_contract_v2.py
lib/research/aifill/tests/test_contract_orchestrate.py
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-gt-1"><invocation>cd C:/dev/wk-resapp-482 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round107_aifill_prep/checks/check_gs2_validation.py" | tail -4; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `AIFILL GS-2 ARMS: YES (N of N)` with N equal to 16, no `FAIL` arm line above it; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-gt-1"><invocation>cd C:/dev/wk-resapp-482 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python -m pytest -q --color=no -p no:cacheprovider lib/research/aifill/tests/test_validation.py lib/research/aifill/tests/test_contract_grounding.py lib/research/aifill/tests/test_contract_v2.py lib/research/aifill/tests/test_contract_orchestrate.py lib/research/aifill/tests/test_grounding.py | tail -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the last non-empty line before `exit=` reads `N passed` (N at least 313) with no `failed` and no `error` in the last 3 lines; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~482 <0.9.0_WK_AMGT_RESAPP~482@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~482/AMGT_RESAPP.TO-AMGT-gt-1.each-block-carries-its-own-validation-state.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character; each criterion's `expect` recorded as an ordered regex of the printed lines when the prose has regex-active characters.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- each criterion's deciding output line (verbatim) and the arm count;
- the arm lines of AC1 that read FAIL, if any, and AC2's pytest summary line;
- any row.
The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** DIRECT-ACT: one cell, about 70 product lines plus tests, LOCAL; no L2, L4-R or L8-L10; the close is the issuer's one real run (the aifill suite plus the api serve test at the merged head; and `stamp_validation` over a real stored document from the live read, written to a local file only). The CTO's ruling (msgs 6444, 6446) and the four-postulate record are in the decomposition section 16. The stored documents are stamped by the issuer at the store write under its own never-widen pair, not by this cell. Reference edit proven in a scratch copy: 16 of 16 arms, 303 contract and grounding tests pass with it.

<status>pending</status>
<round>108</round>
<workstream>AIFILL</workstream>
<slot>0.9.0_WK_AMGT_RESAPP~482</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
