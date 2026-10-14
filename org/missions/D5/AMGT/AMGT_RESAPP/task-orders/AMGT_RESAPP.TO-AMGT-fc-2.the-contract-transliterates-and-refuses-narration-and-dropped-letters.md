# AMGT_RESAPP task order -- `AMGT-fc-2` -- THE CONTRACT TRANSLITERATES, REFUSES A DROPPED LETTER AND REFUSES PROCESS NARRATION (FWD-41 ROUND 105; A FIX)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md</decomp_doc>
<owned_cells>AMGT-fc-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~431</issued_to>
<issued_by>2.0.0_SA_COO~R2</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-fc-2.the-contract-transliterates-and-refuses-narration-and-dropped-letters</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing is scheduled; a library module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, grant, key or policy is touched; the cell writes and tests local Python only.
comp-adversary: RUN at the cut -- `check_fc2_contract.py` is a prepared acceptance check (43 arms: fourteen transliterations, the dropped-letter report and refusal, the narration refusals for thirteen real and likely openers at the start of the text and of a later line, seven legitimate openers that must NOT be refused, the document refusal, the name-mangling finder); at the base it reads `AIFILL FC-2 ARMS: NO (5 of 43)`, the build check failing as expected.
EGRESS CLASS, declared: NONE. No network call by the cell or its checks (the model is a stub or a recorded response); no Bloomberg call.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-431` (branch `wk-AMGT_RESAPP-431`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-431`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-fc-2` (round 105, workstream AIFILL, decomposition `org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md`)

`lib/research/aifill/contract.py` is the one shape and the one validator of the fill document. It must (1) turn accented and special Latin letters into their ASCII forms instead of dropping them, (2) refuse a block whose model text had letters it could not turn into ASCII, and (3) refuse a block whose text opens with
the model's process narration. One file plus tests.

### Why this cell exists (measured by the CVO on the stored documents, C-S133; the CTO's round-104 analysis, `ledger/ROUND_ANALYSIS.round104.AIFILL.md`)
The producer stored 11 blocks across 10 names that open with the MODEL'S NARRATION, glued to the real answer with no space: `I'll research this now.MUFG announced ...` (8306 JP, 9433 JP, 939 HK, ICT PM, NESN SW, PWR US, RIO LN, SHOP CN, UNVGY US), and stored `Nestl` for `Nestle`
(a non-ASCII letter was DROPPED, not transliterated). Neither has reached a person (the page is not landed) but both are served by the API. The CTO's ruling: the disarm is in the PRODUCER, never by hand-editing documents; the page does not land until a full re-validate of all 95 stored
documents against the new contract reads 0 refused. Round 104's cells are merged; this round changes four of their files.

### The contract every cell of this workstream writes against (ratified in the decomposition, inlined)

`fill/v1` document, one per security key, and its five blocks:
```
{ "schema": "aifill/v1", "security_key": "<K>", "as_of": "YYYY-MM-DD", "generated_at": "YYYY-MM-DDTHH:MM:SSZ",
  "producer": {"version": "opal-aifill/1.0.0", "model": "claude-opus-5"},
  "blocks": { "mgmt_bio": B, "mgmt_recent": B, "mgmt_team_view": B, "thesis_pillars": B, "identity_description": B } }   # exactly these five
B = { "block_id": "<id>", "source_class": "OPAL_SOURCE" | "WEB_SEARCH" | "NONE", "machine_written": true,
      "text": "<plain ASCII text, 1..1200 chars>" | null, "reason": "<plain sentence>" | null,
      "citations": [ {"source_kind": "opal"|"web", "url": str|null, "title": str|null, "quote": str|null, "ref": str|null} ],
      "opal_inputs": [str], "model_call": {"model","web_search_requests","input_tokens","output_tokens"} | null }
```
Block rules: `NONE` has `text` null, `reason` a non-empty plain sentence with no underscore, and no citations. Any other class has `text` non-empty (at most 1200 characters, ASCII, no `**`),
`reason` null and at least one citation. A `web` citation has an http(s) `url`. An `opal` citation has a plain-words `ref` an analyst reads (no `_`, `[`, `]`, `{`, `}`, and not starting `thesis.` or
`overlay.`); it may also carry an http(s) `url`. `WEB_SEARCH` has at least one web citation, no opal citation, and `model_call.web_search_requests >= 1`. `OPAL_SOURCE` has at least one opal
citation and no web citation. `machine_written` is always `true`. `opal_inputs` holds the code-path names of the served fields used (never displayed).

The builder seam: a block builder is `lib.research.aifill.block_<id>.build_block(ctx) -> dict` and does no I/O of its own. `ctx` is a `BlockContext(security_key, inputs, model, now)` with
`ctx.inputs = {"overlay": dict|None, "thesis": dict|None, "errors": {...}}` (the two served route bodies of `/api/scoped/amgt/security/<key>/overlay` and `/thesis`), `ctx.now` a tz-aware UTC
datetime, and `ctx.model(prompt, *, system=None, web_search_max_uses=0, max_tokens=1500)` returning an object with `.text`, `.citations` (a list of `{"url","title","cited_text"}`), `.searches`,
`.input_tokens`, `.output_tokens`, `.web_search_requests`, `.model`, `.stop_reason`; it RAISES `ModelError` on any failure and never returns partial text.

### The changes in `lib/research/aifill/contract.py` (everything not listed here keeps its behaviour)
1. **`fold_text(text) -> str`: transliterate.** Keep the existing mapping of punctuation (curly quotes, dashes, ellipsis, no-break space, euro, pound, yen, multiplication sign), the removal of `**` and heading marks and the whitespace collapse, and ADD, in this order: (a) an explicit letter map applied first: `U+00DF`->`ss`, `U+1E9E`->`SS`, `U+00C6`->`AE`, `U+00E6`->`ae`, `U+00D8`->`O`, `U+00F8`->`o`, `U+0141`->`L`, `U+0142`->`l`, `U+0110`->`D`, `U+0111`->`d`, `U+0152`->`OE`, `U+0153`->`oe`, `U+00DE`->`Th`, `U+00FE`->`th`, `U+00D0`->`D`, `U+00F0`->`d`, `U+0131`->`i`;
   (b) `unicodedata.normalize("NFKD", text)` then removal of every combining mark (`unicodedata.category(ch) == "Mn"`); (c) only then the drop of any character still outside ASCII. Examples that must hold: `Nestl` + U+00E9 -> `Nestle`; `Z` + U+00FC + `rich` -> `Zurich`; `S` + U+00E3 + `o Paulo` -> `Sao Paulo`; U+0141 + U+00F3 + `d` + U+017A -> `Lodz`; U+0130 + `stanbul` -> `Istanbul`; U+FB01 + `nance` -> `finance`. Write the non-ASCII characters in the source as `\uXXXX` escapes (the file stays ASCII).
2. **`fold_report(text) -> (folded, dropped)`**: the same folding, returning also the list of the characters of step (c) that were DROPPED (each character once per occurrence, in order). `fold_text` is `fold_report(text)[0]`.
3. **`make_block` refuses a dropped LETTER.** It folds `text` with `fold_report`; if any dropped character is a letter (`unicodedata.category(ch).startswith("L")`) it raises `ContractError` whose message contains the word `dropped` and the characters, e.g. `a letter was dropped in folding the text (...)`: the model wrote outside English letters. A dropped non-letter (a symbol) is dropped silently as before. Citation titles and quotes are still folded without refusal.
4. **`NARRATION_OPENERS`**: a module constant, a tuple of lowercase strings, exactly these (the stated list the CTO ruled; printed in the contract): `"i'll"`, `"i will"`, `"i'm going to"`, `"i am going to"`, `"i need to"`, `"i should"`, `"i can"`, `"i found"`, `"i've"`, `"i have"`, `"i would"`, `"i want to"`, `"i'd"`, `"let me"`, `"let's"`, `"first, i"`, `"now, i"`, `"now i"`, `"okay, i"`, `"sure, i"`, `"based on my search"`, `"based on my research"`.
5. **`validate_block` refuses narration.** For a non-`NONE` block, take the text and each line of it after the first (split on newline). For each, strip leading whitespace and any leading quote or bracket characters (`"`, `'`, `(`, `[`) and lowercase it; if it starts with an opener of `NARRATION_OPENERS` that is NOT followed by a letter or digit (a regular-expression negative lookahead `(?![a-z0-9])`, so `i can` does not match `i cannot`... and `intel`, `ibm`, `illumina`, `iberdrola`, `lets holding`, `looking ahead` are never matches), add the problem `<block id>: text opens with process narration (<the opener>)`. The word `narration` must appear in the problem. The rule applies to `text` only: a `NONE` block's `reason` is not checked.
6. **`name_mangling_problems(text, names) -> list`**: for each string in `names` (a list of strings the page already knows: display name, company name, officer names) and each whitespace-separated token of it that holds a non-ASCII letter: `ok = fold_text(token)`; `drop` = the token with every non-ASCII character REMOVED (no transliteration); a problem string is returned when `drop` differs from `ok` AND `drop` occurs in `text` as a whole word (not preceded or followed by an ASCII letter) AND `ok` does not occur in `text` as a whole word. The problem reads `a character was dropped from the name <token>: the text carries <drop>`. ASCII-only names never produce a problem. This is how a stored `Nestl` is found when the inputs carry `Nestl` + U+00E9; it is used by cell fc-4, not by `validate_block` (which has no inputs).

### Tests
A new test module `lib/research/aifill/tests/test_contract_v2.py` (no `__init__.py`): at least one test per numbered point, including each transliteration example above, a dropped CJK letter, every opener of the list at the start of a text and on a later line, the legitimate openers that must pass, the document-level refusal naming the block, and the name finder both ways. If a test in the existing `tests/test_contract_orchestrate.py` asserts the old drop behaviour of `fold_text`, update that one test; touch nothing else in it.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W431-S<k>`, `disarm_owner` `2.0.0_SA_COO~R2`.

## 2. BOUNDS


1. Write ONLY `lib/research/aifill/contract.py`, `lib/research/aifill/tests/test_contract_v2.py` and, only if one asserts the old drop behaviour, a test in `lib/research/aifill/tests/test_contract_orchestrate.py`. The orchestrator, the seam, the builders and everything else are other cells'.
- Leave `lib/research/management/`, `lib/research/filings/`, `lib/research/posture/` and every existing module untouched.
- No network, no AWS, no real model call, no `pip install`: every model call in your tests is a stub or the recorded response. The `anthropic` package is never imported (the installed 0.45.0 crashes on web-search blocks).
- Python 3.9 syntax (`from __future__ import annotations`, `typing.Optional`, no `X | Y` unions evaluated at runtime, no `match`); ASCII-only source files (write non-ASCII characters as `\uXXXX` escapes); stdlib only.
- Run the commit gate before you commit: `bash .tools/commit-gate.sh <each .py you wrote>` (it runs `py_compile` and `ruff`); a finding there is yours to fix.

## 3. SURFACES

<paths>
lib/research/aifill/contract.py
lib/research/aifill/tests/test_contract_v2.py
lib/research/aifill/tests/test_contract_orchestrate.py
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-fc-2"><invocation>cd C:/dev/wk-resapp-431 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round105_aifill_prep/checks/check_fc2_contract.py" | tail -4; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `AIFILL FC-2 ARMS: YES (N of N)` with N equal to 43, no `FAIL` arm line above it; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-fc-2"><invocation>cd C:/dev/wk-resapp-431 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python -m pytest -q --color=no -p no:cacheprovider lib/research/aifill/tests/test_contract_v2.py lib/research/aifill/tests/test_contract_orchestrate.py | tail -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the last non-empty line before `exit=` reads `N passed` (N at least the count your test module's functions define) with no `failed` and no `error` in the last 3 lines; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-fc-2"><invocation>cd C:/dev/wk-resapp-431 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round104_aifill_prep/checks/check_fa1_contract.py" | tail -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `AIFILL FA-1 ARMS: YES (31 of 31)`: the round-104 contract check keeps passing (a control, not a hygiene check); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~431 <0.9.0_WK_AMGT_RESAPP~431@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~431/AMGT_RESAPP.TO-AMGT-fc-2.the-contract-transliterates-and-refuses-narration-and-dropped-letters.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character; each criterion's `expect` recorded as an ordered regex of the printed lines when the prose has regex-active characters.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- each criterion's deciding output line (verbatim) and the arm count;
- the arm lines of AC1 that read FAIL, if any, AC2's pytest summary line and AC3's line.
- any row.
The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** An independent head. The opener list is the CTO's ruled "stated list printed in the contract" and is drawn from the 11 narrated blocks measured (all `I'll research ...` or `I'll search ...`) plus the obvious first-person starters; `Looking`, `Searching` and `Based on public ...` are deliberately NOT on it (legitimate sentence starts). The structural fix is cell fc-1 (the seam); this is the backstop that makes a narrated document unwritable. `name_mangling_problems` exists because a dropped letter cannot be seen in the stored text alone: it needs the names the inputs carry (fc-4 supplies them). The 43 arms include a loop of 14 transliterations, 13 narration refusals and 7 legitimate openers.

<status>pending</status>
<round>105</round>
<workstream>AIFILL</workstream>
<slot>0.9.0_WK_AMGT_RESAPP~431</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
