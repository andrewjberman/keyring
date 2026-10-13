# AMGT_RESAPP task order -- `AMGT-fa-1` -- THE FILL DOCUMENT CONTRACT AND THE BLOCK ORCHESTRATOR (FWD-41; A BUILD)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md</decomp_doc>
<owned_cells>AMGT-fa-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~420</issued_to>
<issued_by>2.0.0_SA_COO~R2</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-fa-1.the-fill-document-contract-and-the-block-orchestrator</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing is scheduled; a library module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, grant, key or policy is touched; the cell writes and tests local Python only.
comp-adversary: RUN at the cut -- `check_fa1_contract.py` is a prepared acceptance check (31 arms: the contract, the refusals, the orchestrator's four failure paths, the default discovery); at the base it exits 1 on `ModuleNotFoundError: No module named 'lib.research.aifill'`, the build check failing as expected.
EGRESS CLASS, declared: NONE. No network call by the cell or its checks (the model is a stub or a recorded response); no Bloomberg call.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-420` (branch `wk-AMGT_RESAPP-420`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-420`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-fa-1` (round 104, workstream AIFILL, decomposition `org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md`)

FWD-41 of PRD v0.44 (ratified text, inlined): for every one of the 93 names, five blocks of the Security Analysis page (a management bio summary, recent developments on management, "The research team on management" where the pack states none, "The research team's thesis pillars" where the pack states none, and the identity header's company description line) serve content with its SOURCE CLASS (Opal source / web search / none, with a reason) and its citations, marked machine-written. This cell builds the package, the one document shape, its validator and the orchestrator that assembles a document from five block builders other cells write. You write three modules and one test module; nothing else.


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

### `lib/research/aifill/__init__.py`
An empty file (zero bytes). The package `lib/research/aifill/` is new; `lib/research/` itself has no `__init__.py` and stays that way.

### `lib/research/aifill/contract.py` -- exact interface (other cells import these names)
- Constants: `SCHEMA = "aifill/v1"`, `PRODUCER_VERSION = "opal-aifill/1.0.0"`, `PRODUCER_MODEL = "claude-opus-5"`, `BLOCK_IDS = ("mgmt_bio", "mgmt_recent", "mgmt_team_view", "thesis_pillars", "identity_description")`, `SOURCE_CLASSES = ("OPAL_SOURCE", "WEB_SEARCH", "NONE")`, `MAX_TEXT = 1200`.
- `class ContractError(Exception)`.
- `fold_text(text) -> str`: returns plain ASCII for stored text. Replace U+2018 and U+2019 with `'`; U+201C and U+201D with `"`; U+2013 and U+2014 with `-`; U+2026 with `...`; U+00A0 with a space; U+20AC with `EUR `; U+00A3 with `GBP `; U+00A5 with `JPY `; U+00D7 with `x`. Remove every `**`. Remove a markdown heading prefix (`#` characters and the space after them) at the start of any line. Collapse each run of spaces or tabs to one space, collapse three or more newlines to two, strip the ends, and drop any character still outside ASCII. Write these characters as `\uXXXX` escapes in the source so the file stays ASCII.
- `none_block(block_id, reason) -> dict`: a `NONE` block (`machine_written` True, `text` None, `citations` [], `opal_inputs` [], `model_call` None); `reason` is passed through `fold_text`; an unknown `block_id` raises `ContractError`.
- `make_block(block_id, source_class, text, citations, opal_inputs=(), model_call=None) -> dict`: builds a non-`NONE` block. `source_class` `"NONE"` raises `ContractError` (use `none_block`). `text` and each citation's `title`/`quote` go through `fold_text`; each citation is copied into a dict with all five keys (`source_kind`, `url`, `title`, `quote`, `ref`, a missing key becoming None); `opal_inputs` becomes a list; `reason` None; `machine_written` True. The result goes through `validate_block`; any problem raises `ContractError("; ".join(problems))`.
- `validate_block(block) -> list`: the list of problems (strings), `[]` when valid. It checks: a dict with exactly the eight keys of `B`; `block_id` in `BLOCK_IDS`; `source_class` in `SOURCE_CLASSES`; `machine_written is True`; every string in the block ASCII (use `str.isascii()`); for `NONE`: `text` None, `reason` a non-empty string with no `_`, `citations == []`; otherwise: `text` a non-empty string after strip, at most `MAX_TEXT` characters, containing no `**`, `reason` None, `citations` a non-empty list of dicts each with exactly the five keys, `source_kind` in `("opal","web")`, a `web` citation with a `url` starting `http://` or `https://`, an `opal` citation with a non-empty `ref` holding none of `_ [ ] { }` and not starting `thesis.` or `overlay.` (and a `url`, if not None, starting `http://` or `https://`); `WEB_SEARCH`: at least one web citation, no opal citation, `model_call` a dict whose `web_search_requests` is an int of at least 1; `OPAL_SOURCE`: at least one opal citation and no web citation; `opal_inputs` a list of strings; `model_call` None or a dict with the four keys.
- `validate_document(doc) -> list`: the list of problems, `[]` when valid. A dict with exactly the keys `schema`, `security_key`, `as_of`, `generated_at`, `producer`, `blocks`; `schema == SCHEMA`; `security_key` a non-empty string; `as_of` matching `YYYY-MM-DD` and parsing as a date; `generated_at` matching `YYYY-MM-DDTHH:MM:SSZ`; `producer` a dict with string `version` and `model`; `blocks` a dict whose keys are exactly `BLOCK_IDS`, each value valid under `validate_block` (problems prefixed with the block id) and each `blocks[id]["block_id"] == id`.

### `lib/research/aifill/orchestrate.py` -- exact interface
- `class BlockContext`: `__init__(self, security_key, inputs, model, now)` storing the four as attributes of the same names.
- `build_document(security_key, inputs, model, now=None, builders=None) -> dict`: returns a document that ALWAYS passes `validate_document` (before returning, validate it; a problem there raises `ContractError`).
  - `now` defaults to `datetime.datetime.now(datetime.timezone.utc)`; a naive `now` raises `ValueError`. `as_of` is `now.date().isoformat()`; `generated_at` is `now.strftime("%Y-%m-%dT%H:%M:%SZ")`; `producer` is `{"version": PRODUCER_VERSION, "model": PRODUCER_MODEL}`.
  - For each id in `BLOCK_IDS`, in order, make a `BlockContext(security_key, inputs, model, now)` and call the builder. `builders`, when given, is a dict id -> callable(ctx); an id missing from it is "not built yet". When `builders` is None, the builder for an id is `build_block` of the module `lib.research.aifill.block_<id>`, loaded with `importlib.import_module("lib.research.aifill.block_" + id)` (call it through the `importlib` module attribute at call time: the acceptance check patches `importlib.import_module`).
  - A `ModuleNotFoundError` whose `.name` equals the module name requested means "not built yet"; a `ModuleNotFoundError` for any other name is a builder error, not "not built yet".
  - The block recorded for an id is the builder's return value when it is a dict that passes `validate_block` with `block_id == id`; otherwise a `none_block(id, reason)` with one of these reasons: not built yet -> `"This block is not built yet."`; the builder returned something invalid (or for another id) -> `"This block could not be produced (the builder returned an invalid block)."`; the builder raised an exception any class of whose MRO is named `ModelError` -> `"This block could not be produced (the model call failed: <message>)."` where `<message>` is `str(exc)` through `fold_text`, with every `_` replaced by a space, cut to 160 characters; the builder raised anything else -> `"This block could not be produced (an internal error: <ClassName>)."`. No exception from a builder escapes `build_document`.

### `lib/research/aifill/tests/test_contract_orchestrate.py`
Your own pytest module (no `__init__.py` in `tests/`; run with `PYTHONPATH` set to the repo root). At least one test function for each bullet above, including each refusal in `validate_block`/`make_block` and each of the orchestrator's four failure paths, plus a green document test (five valid blocks -> `validate_document == []`) and a negative control (a broken document is refused). Use no fixture file; build blocks by hand.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W420-S<k>`, `disarm_owner` `2.0.0_SA_COO~R2`.

## 2. BOUNDS


1. Write ONLY `lib/research/aifill/__init__.py`, `contract.py`, `orchestrate.py` and `lib/research/aifill/tests/test_contract_orchestrate.py`. The model seam (`model.py`), the served-inputs reader (`inputs.py`), the block builders (`block_*.py`), `store.py` and `run.py` are other cells': do not create them.
- Leave `lib/research/management/`, `lib/research/filings/`, `lib/research/posture/` and every existing module untouched.
- No network, no AWS, no real model call, no `pip install`: every model call in your tests is a stub or the recorded response. The `anthropic` package is never imported (the installed 0.45.0 crashes on web-search blocks).
- Python 3.9 syntax (`from __future__ import annotations`, `typing.Optional`, no `X | Y` unions evaluated at runtime, no `match`); ASCII-only source files (write non-ASCII characters as `\uXXXX` escapes); stdlib only.
- Run the commit gate before you commit: `bash .tools/commit-gate.sh <each .py you wrote>` (it runs `py_compile` and `ruff`); a finding there is yours to fix.

## 3. SURFACES

<paths>
lib/research/aifill/__init__.py
lib/research/aifill/contract.py
lib/research/aifill/orchestrate.py
lib/research/aifill/tests/test_contract_orchestrate.py
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-fa-1"><invocation>cd C:/dev/wk-resapp-420 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round104_aifill_prep/checks/check_fa1_contract.py" | tail -4; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `AIFILL FA-1 ARMS: YES (N of N)` with N equal to the count printed and N at least 31, no `FAIL` arm line above it; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-fa-1"><invocation>cd C:/dev/wk-resapp-420 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python -m pytest -q --color=no -p no:cacheprovider lib/research/aifill/tests/test_contract_orchestrate.py | tail -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the last non-empty line before `exit=` reads `N passed` (N at least the count your test module's functions define) with no `failed` and no `error` in the last 3 lines; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~420 <0.9.0_WK_AMGT_RESAPP~420@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~420/AMGT_RESAPP.TO-AMGT-fa-1.the-fill-document-contract-and-the-block-orchestrator.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character; each criterion's `expect` recorded as an ordered regex of the printed lines when the prose has regex-active characters.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- each criterion's deciding output line (verbatim) and the arm count;
- the arm lines of AC1 that read FAIL, if any, and the pytest summary line.
- any row.
The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** The head of the contract chain. fa-3, fa-4 and fa-5 import `contract` and `orchestrate` and are STAGED behind this order's merge; fa-6 is staged behind all of them. The check is the issuer's, prepared and dry-run at the base (exit 1, `ModuleNotFoundError`); its green arm is not provable before a reference exists, so a check defect found by the worker is a surprise row and the issuer re-cuts the check, never the worker's code to a wrong check. Order of work for the issuer after this order: merge through `safe-merge.sh`, run `ruff` and `py_compile` on the package once at the drain, then flip fa-3, fa-4, fa-5 to pending and cut their worktrees from the merged head.

<status>pending</status>
<round>104</round>
<workstream>AIFILL</workstream>
<slot>0.9.0_WK_AMGT_RESAPP~420</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
