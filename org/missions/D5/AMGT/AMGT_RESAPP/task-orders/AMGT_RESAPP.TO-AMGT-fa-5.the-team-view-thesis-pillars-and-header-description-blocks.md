# AMGT_RESAPP task order -- `AMGT-fa-5` -- THE THREE GAP BLOCKS, `mgmt_team_view`, `thesis_pillars`, `identity_description` (FWD-41 (3), (4), (5); A BUILD)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md</decomp_doc>
<owned_cells>AMGT-fa-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~426</issued_to>
<issued_by>2.0.0_SA_COO~R2</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-fa-5.the-team-view-thesis-pillars-and-header-description-blocks</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing is scheduled; a library module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, grant, key or policy is touched; the cell writes and tests local Python only.
comp-adversary: RUN at the cut -- `check_fa5_text_blocks.py` is a prepared acceptance check (20 arms, the model stubbed); at the base it exits 1 on `ModuleNotFoundError: No module named 'lib.research.aifill'`, the build check failing as expected.
EGRESS CLASS, declared: NONE. No network call by the cell or its checks (the model is a stub or a recorded response); no Bloomberg call.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-426` (branch `wk-AMGT_RESAPP-426`, cut from the merged head that carries cell fa-1 (the issuer cuts this worktree after fa-1 merges)). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-426`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-fa-5` (round 104, workstream AIFILL, decomposition `org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md`)

FWD-41 (3), (4), (5), ratified text (inlined): "(3) Exec Management: 'The research team on management' (`ExecManagementTab.tsx` MANAGEMENT_HEADING) where the pack states none; (4) Thesis: 'The research team's thesis pillars' (`ThesisTab.tsx` PILLARS_HEADING) where the pack states none; (5) the identity header's company description line (`SecurityOverlay.tsx` `identityDescriptionLine`, `data-identity-description`, drawn once per ruling W126-S1), which today prints nothing where none is held." Each is served with its SOURCE CLASS, citations, marked machine-written. These three blocks fill ONLY where the page shows a gap: where the research team's own text exists the block is `NONE` with a reason saying so (the team's text stands; the machine never speaks in the team's voice). You write THREE block builders and one test module. The package already carries `contract.py` and `orchestrate.py` (cell fa-1, merged): read them first.


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

### How every builder handles the model's reply (the same in each module you write; copy the few lines, do not import a helper from another cell)
- `NO_INFORMATION`: after `.strip()`, a reply that is empty or equals `NO_INFORMATION` (a trailing period allowed) -> `contract.none_block(id, "The model found nothing it could support for this block.")`.
- Text: `contract.fold_text(result.text)`; empty after folding -> the same `NONE`.
- OPAL path (the model is called with `web_search_max_uses=0`): the numeric guard -- every digit run in the folded text (remove commas inside a number first, so `1,000` is `1000`) must appear as a digit run in the supplied facts text (same normalisation); one that does not -> `contract.none_block(id, "The model's text carried a figure that the supplied facts do not hold, so it was withheld.")`.
- WEB path (the model is called with `web_search_max_uses=3`): the citations are the result's `citations` whose `url` starts `http://` or `https://`, in order, de-duplicated by url, each as `{"source_kind": "web", "url": url, "title": title or None (folded), "quote": cited_text cut to 300 characters (folded) or None, "ref": None}`; none left -> `contract.none_block(id, "The web search returned no citable source, so the text was withheld.")`.
- `model_call` = `{"model": result.model, "web_search_requests": result.web_search_requests, "input_tokens": result.input_tokens, "output_tokens": result.output_tokens}` on both paths.
- The block is made with `contract.make_block(...)`. A `contract.ContractError` from it (the text is over the limit, for example) -> `contract.none_block(id, "The model's text was too long to keep, so it was withheld.")`.
- The model call is `ctx.model(prompt, system=SYSTEM, web_search_max_uses=N)` with keyword arguments exactly so; an exception from it is NOT caught (the orchestrator turns it into a NONE block).
- Safe reads: the served bodies may be None or hold None where a dict is expected; every nested read is guarded, and a builder never raises on a missing body (it takes the web path with the company named `this company`, or returns the NONE the cell names).
- The company name: `ctx.inputs["overlay"]["display_name"]`, else its `name`, else `"this company"`. The CEO name: the first officer in `ctx.inputs["thesis"]["management"]["officers"]` whose `role` matches `re.search(r"chief executive|\bceo\b", role, re.I)`, or None.
- The two system prompts, copy them exactly:
  - `SYSTEM_WEB = """You write one short block of plain text for an investment research page. Plain text only: no markdown, no bullet characters, no headings, no links in the text. Use the web search tool and prefer the company's own website, regulatory filings and established news; do not rely on social media or data brokers. State only facts your sources support; leave out anything you cannot support. If you cannot support anything, answer exactly NO_INFORMATION."""`
  - `SYSTEM_OPAL = """You write one short block of plain text for an investment research page. Plain text only: no markdown, no bullet characters, no headings. Use ONLY the facts supplied in the prompt: add nothing from your own knowledge and use no figure that is not in the facts. If the facts do not support anything, answer exactly NO_INFORMATION."""`

### Your fixtures (read them; the acceptance check and your tests use them)
`C:/dev/wk-resapp-426/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round104_aifill_prep/fixtures/served_inputs_ASML_NA_Equity.json` is `{"overlay": ..., "thesis": ..., "errors": {}}`: the two served route bodies of the real name ASML_NA_Equity, trimmed to the fields the builders read. The shared helpers of the acceptance checks (stub model, fixture loader) are in `C:/dev/wk-resapp-426/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round104_aifill_prep/checks/aifill_check_lib.py`; you may copy what you need into your own test module.
Paths in the served bodies that matter: `overlay.name`, `overlay.display_name`, `overlay.description.{status,text}`, `overlay.top_band.description_line`, `overlay.feed.items[].{publisher,publisher_name,published_date,article_key,url,title}`; `thesis.management.{management_status,officers[].{name,role,role_start,tenure_years},ceo_public_profile.{status,title,snippet,url,ceo_name}}`; `thesis.dossier_fields.{management.{status,value},thesis_pillars[]}`; `thesis.drafted_sections[].{section_id,sentences[].{text,evidence}}`.

### `lib/research/aifill/block_mgmt_team_view.py` -- `build_block(ctx)` for `mgmt_team_view`
- The pack STATES management when `ctx.inputs["thesis"]["dossier_fields"]["management"]` is a dict with `status == "SERVED"` and a non-empty string `value`. Then -> `none_block("mgmt_team_view", "The research team's pack already states a management passage.")` and the model is NOT called.
- `ctx.inputs["thesis"]` None (the page data could not be read) -> `none_block(..., "The page data could not be read, so no outside summary was added.")`, no model call.
- Otherwise (the pack is silent, including a missing `management` key) -> the WEB path (there is no Opal source): the prompt names the company and the CEO when known, and asks for two to four plain sentences assessing the quality and track record of the company's management team (strategy execution, capital allocation, governance) from public sources; it says in so many words that this is an outside summary and NOT the research team's view, and that the text must not claim to be the research team's or speak as `we`. `ctx.model(prompt, system=SYSTEM_WEB, web_search_max_uses=3)`; reply rules above; `WEB_SEARCH`.

### `lib/research/aifill/block_thesis_pillars.py` -- `build_block(ctx)` for `thesis_pillars`
- The pack STATES pillars when `thesis.dossier_fields.thesis_pillars` is a non-empty list. Then -> `none_block("thesis_pillars", "The research team's pack already states thesis pillars.")`, no model call. `thesis` None -> `none_block(..., "The page data could not be read, so no outside summary was added.")`.
- The Opal source: the `text` of the sentences of the `thesis.drafted_sections` entry whose `section_id == "investment_thesis"` (the machine-drafted filing thesis sentences, each non-empty string), at most 6. Two or more -> the OPAL path: the prompt lists them as lines and asks to condense them into three to five short thesis pillars, one plain sentence per line, from those sentences only; `ctx.model(prompt, system=SYSTEM_OPAL, web_search_max_uses=0)`; reply rules above (numeric guard against the sentences you sent); `OPAL_SOURCE` with ONE opal citation `{"source_kind": "opal", "ref": "Company filing analysis, thesis sentences", "url": None, "title": None, "quote": None}`; `opal_inputs` `["thesis.drafted_sections.investment_thesis"]`.
- Fewer than two -> the WEB path: the prompt names the company and asks for three to five key investment thesis pillars, one plain sentence per line, from public sources; `ctx.model(prompt, system=SYSTEM_WEB, web_search_max_uses=3)`; reply rules above; `WEB_SEARCH`.

### `lib/research/aifill/block_identity_description.py` -- `build_block(ctx)` for `identity_description`
- `ctx.inputs["overlay"]` None -> `none_block("identity_description", "The page header could not be read, so a description was not drafted.")`, no model call.
- The header HOLDS a description when `overlay.top_band.description_line` is a non-empty string, or `overlay.description.status == "SERVED"` with a non-empty string `text`. Then -> `none_block("identity_description", "The identity header already has a company description.")`, no model call.
- The Opal source: the `text` of the sentences of the `thesis.drafted_sections` entry whose `section_id == "company_description"` (non-empty strings, at most 4). One or more -> the OPAL path: ask for one or two plain sentences saying what the company does, from those sentences only; `SYSTEM_OPAL`, `web_search_max_uses=0`; `OPAL_SOURCE` with ONE opal citation (ref `Company filing analysis, business description sentences`), `opal_inputs` `["thesis.drafted_sections.company_description"]`.
- None -> the WEB path: ask for one or two plain sentences saying what the company does, from public sources (the company is named); `SYSTEM_WEB`, `web_search_max_uses=3`; `WEB_SEARCH`.
- This block's text limit is 400 characters, tighter than the contract's 1200: a reply whose folded text is longer than 400 characters -> `none_block("identity_description", "The model's description was too long to keep, so it was withheld.")`.

### `lib/research/aifill/tests/test_text_blocks.py`
Your own pytest module (no `__init__.py`): a stub model, the fixture, and a test per branch of each of the three builders (the gap, the pack/header that already holds text, the Opal path where one exists, the web path, the numeric guard, NO_INFORMATION, no citation, a missing body, the 400-character limit, a model exception propagating). Python 3.9, ASCII.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W426-S<k>`, `disarm_owner` `2.0.0_SA_COO~R2`.

## 2. BOUNDS


1. Write ONLY `lib/research/aifill/block_mgmt_team_view.py`, `lib/research/aifill/block_thesis_pillars.py`, `lib/research/aifill/block_identity_description.py` and `lib/research/aifill/tests/test_text_blocks.py`. The other blocks, `model.py`, `inputs.py`, `store.py` and `run.py` are other cells': do not create them. The modules do no I/O and import only `re` and `lib.research.aifill.contract` (plus `__future__`).
- Leave `lib/research/management/`, `lib/research/filings/`, `lib/research/posture/` and every existing module untouched.
- No network, no AWS, no real model call, no `pip install`: every model call in your tests is a stub or the recorded response. The `anthropic` package is never imported (the installed 0.45.0 crashes on web-search blocks).
- Python 3.9 syntax (`from __future__ import annotations`, `typing.Optional`, no `X | Y` unions evaluated at runtime, no `match`); ASCII-only source files (write non-ASCII characters as `\uXXXX` escapes); stdlib only.
- Run the commit gate before you commit: `bash .tools/commit-gate.sh <each .py you wrote>` (it runs `py_compile` and `ruff`); a finding there is yours to fix.

## 3. SURFACES

<paths>
lib/research/aifill/block_mgmt_team_view.py
lib/research/aifill/block_thesis_pillars.py
lib/research/aifill/block_identity_description.py
lib/research/aifill/tests/test_text_blocks.py
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-fa-5"><invocation>cd C:/dev/wk-resapp-426 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round104_aifill_prep/checks/check_fa5_text_blocks.py" | tail -4; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `AIFILL FA-5 ARMS: YES (N of N)` with N equal to the count printed and N at least 20, no `FAIL` arm line above it; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-fa-5"><invocation>cd C:/dev/wk-resapp-426 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python -m pytest -q --color=no -p no:cacheprovider lib/research/aifill/tests/test_text_blocks.py | tail -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the last non-empty line before `exit=` reads `N passed` (N at least the count your test module's functions define) with no `failed` and no `error` in the last 3 lines; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~426 <0.9.0_WK_AMGT_RESAPP~426@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~426/AMGT_RESAPP.TO-AMGT-fa-5.the-team-view-thesis-pillars-and-header-description-blocks.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character; each criterion's `expect` recorded as an ordered regex of the printed lines when the prose has regex-active characters.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- each criterion's deciding output line (verbatim) and the arm count;
- the arm lines of AC1 that read FAIL, if any, and the pytest summary line.
- any row.
The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**AMENDMENT 1 (2026-10-13 ~23:5xZ, the issuer, after worker ~426's BLOCKING row W426-S1; no gate limb graded it: the order is open, `<placeholders>NONE` stands):** the arm count was the issuer's miscount: `check_fa5_text_blocks.py` defines 20 arms (the preflight and AC1 said 21). AC1 read `YES (20 of 20)`, 0 FAIL, so the expectation is corrected to 20; the worker's code is not at fault and no check arm was removed.

**ISSUER NOTES:** STAGED behind `AMGT-fa-1`'s merge. Three blocks in one order because they are one pattern (a gap test, an optional Opal source, a web path) at about 60 lines each; each stays its own module with its own arms. The `identity_description` block is the only one the page header draws, and the header draws it once (ruling W126-S1): the serve puts it in the `/thesis` bundle (cell fa-7) and the page passes it down (cell fa-8), so the overlay route gains no read.

<status>staged</status>
<status>pending -- GO 2026-10-13T23:0xZ by the issuer (2.0.0_SA_COO~R2): fa-1 merged @ebe4c8d287, so `contract.py` and `orchestrate.py` exist at the base this worktree is cut from.</status>
<round>104</round>
<workstream>AIFILL</workstream>
<slot>0.9.0_WK_AMGT_RESAPP~426</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
