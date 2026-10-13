# AMGT_RESAPP task order -- `AMGT-fa-4` -- THE RECENT MANAGEMENT DEVELOPMENTS BLOCK, `mgmt_recent` (FWD-41 (2); A BUILD)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md</decomp_doc>
<owned_cells>AMGT-fa-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~425</issued_to>
<issued_by>2.0.0_SA_COO~R2</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-fa-4.the-recent-management-developments-block</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing is scheduled; a library module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, grant, key or policy is touched; the cell writes and tests local Python only.
comp-adversary: RUN at the cut -- `check_fa4_mgmt_recent.py` is a prepared acceptance check (12 arms, the model stubbed); at the base it exits 1 on `ModuleNotFoundError: No module named 'lib.research.aifill'`, the build check failing as expected.
EGRESS CLASS, declared: NONE. No network call by the cell or its checks (the model is a stub or a recorded response); no Bloomberg call.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-425` (branch `wk-AMGT_RESAPP-425`, cut from the merged head that carries cell fa-1 (the issuer cuts this worktree after fa-1 merges)). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-425`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-fa-4` (round 104, workstream AIFILL, decomposition `org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md`)

FWD-41 (2), ratified text (inlined): "Exec Management: a recent-developments block (new)", served with its SOURCE CLASS (Opal source / web search / none, with a reason), its citations, marked machine-written; Opal sources first (the harvest estate's news is the natural source), else a web search on the existing Anthropic path. V1 serves harvest data as derived layers and links only: this builder reads article HEADLINES and links the served feed already carries, never an article body. You write ONE block builder, `lib/research/aifill/block_mgmt_recent.py`, and its test module. The package already carries `contract.py` and `orchestrate.py` (cell fa-1, merged): read them first.


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
`C:/dev/wk-resapp-425/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round104_aifill_prep/fixtures/served_inputs_ASML_NA_Equity.json` is `{"overlay": ..., "thesis": ..., "errors": {}}`: the two served route bodies of the real name ASML_NA_Equity, trimmed to the fields the builders read. The shared helpers of the acceptance checks (stub model, fixture loader) are in `C:/dev/wk-resapp-425/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round104_aifill_prep/checks/aifill_check_lib.py`; you may copy what you need into your own test module.
Paths in the served bodies that matter: `overlay.name`, `overlay.display_name`, `overlay.description.{status,text}`, `overlay.top_band.description_line`, `overlay.feed.items[].{publisher,publisher_name,published_date,article_key,url,title}`; `thesis.management.{management_status,officers[].{name,role,role_start,tenure_years},ceo_public_profile.{status,title,snippet,url,ceo_name}}`; `thesis.dossier_fields.{management.{status,value},thesis_pillars[]}`; `thesis.drafted_sections[].{section_id,sentences[].{text,evidence}}`.

### What `build_block(ctx)` does for `mgmt_recent` (OPAL FIRST, else WEB, else NONE)
1. The candidate items: `ctx.inputs["overlay"]["feed"]["items"]` (a list; anything else, or a missing body, is an empty list). An item is EVIDENCE when its `published_date` (a `YYYY-MM-DD` string) is within the 90 days before `ctx.now.date()` (inclusive; measured from `ctx.now`, never the wall clock) AND its `title` matches this management-event pattern, case-insensitive: `\b(ceo|cfo|coo|cto|chief (executive|financial|operating|technology|risk|investment) officer|chair(man|woman|person)?|president|appoint\w*|names?|named|resign\w*|steps? down|retire\w*|succe(ssor|ed|eds|ssion)|leadership|executive|board|director)\b`. Keep the newest five by `published_date` (ties by `article_key`).
2. At least one evidence item -> the OPAL path: the prompt names the company and lists the items as lines `- <published_date> | <publisher_name, else publisher>: <title>`, and asks for one to three plain sentences saying what these headlines say about the company's executive management, from the headlines only, nothing inferred beyond them; `ctx.model(prompt, system=SYSTEM_OPAL, web_search_max_uses=0)`; apply the reply rules above (the numeric guard checks against the lines you sent); the block is `OPAL_SOURCE` with ONE opal citation per item sent: `{"source_kind": "opal", "ref": "Harvested article: <publisher_name, else publisher>, <published_date>", "url": <the item's url when http(s) else None>, "title": <the item's title>, "quote": None}`; `opal_inputs` `["overlay.feed.items"]`.
3. No evidence item -> the WEB path: the prompt names the company (and the CEO when known) and asks for two to four plain sentences on the MOST RECENT developments (the last twelve months) concerning the company's executive management: appointments, departures, succession, notable statements of strategy by management; `ctx.model(prompt, system=SYSTEM_WEB, web_search_max_uses=3)`; apply the reply rules above; the block is `WEB_SEARCH`. The word `recent` appears in the prompt.

### `lib/research/aifill/tests/test_block_mgmt_recent.py`
Your own pytest module (no `__init__.py`): a stub model, the fixture with the feed items replaced by items you build, and a test per branch above (a matching recent headline, an old one, a non-management one, an empty or null feed, the numeric guard, NO_INFORMATION, no citation, the window measured from `ctx.now`, a model exception propagating). Python 3.9, ASCII.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W425-S<k>`, `disarm_owner` `2.0.0_SA_COO~R2`.

## 2. BOUNDS


1. Write ONLY `lib/research/aifill/block_mgmt_recent.py` and `lib/research/aifill/tests/test_block_mgmt_recent.py`. The other blocks, `model.py`, `inputs.py`, `store.py` and `run.py` are other cells': do not create them. The module does no I/O and imports only `re`, `datetime` and `lib.research.aifill.contract` (plus `__future__`).
- Leave `lib/research/management/`, `lib/research/filings/`, `lib/research/posture/` and every existing module untouched.
- No network, no AWS, no real model call, no `pip install`: every model call in your tests is a stub or the recorded response. The `anthropic` package is never imported (the installed 0.45.0 crashes on web-search blocks).
- Python 3.9 syntax (`from __future__ import annotations`, `typing.Optional`, no `X | Y` unions evaluated at runtime, no `match`); ASCII-only source files (write non-ASCII characters as `\uXXXX` escapes); stdlib only.
- Run the commit gate before you commit: `bash .tools/commit-gate.sh <each .py you wrote>` (it runs `py_compile` and `ruff`); a finding there is yours to fix.

## 3. SURFACES

<paths>
lib/research/aifill/block_mgmt_recent.py
lib/research/aifill/tests/test_block_mgmt_recent.py
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-fa-4"><invocation>cd C:/dev/wk-resapp-425 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round104_aifill_prep/checks/check_fa4_mgmt_recent.py" | tail -4; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `AIFILL FA-4 ARMS: YES (N of N)` with N equal to the count printed and N at least 12, no `FAIL` arm line above it; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-fa-4"><invocation>cd C:/dev/wk-resapp-425 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python -m pytest -q --color=no -p no:cacheprovider lib/research/aifill/tests/test_block_mgmt_recent.py | tail -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the last non-empty line before `exit=` reads `N passed` (N at least the count your test module's functions define) with no `failed` and no `error` in the last 3 lines; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~425 <0.9.0_WK_AMGT_RESAPP~425@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~425/AMGT_RESAPP.TO-AMGT-fa-4.the-recent-management-developments-block.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character; each criterion's `expect` recorded as an ordered regex of the printed lines when the prose has regex-active characters.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- each criterion's deciding output line (verbatim) and the arm count;
- the arm lines of AC1 that read FAIL, if any, and the pytest summary line.
- any row.
The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** STAGED behind `AMGT-fa-1`'s merge. "Do not serve raw publisher article text through the gateway in V1" (cluster direction): this builder sends headlines and links only, by construction. The 90-day window and the keyword pattern are the issuer's first cut; a miss on the 93-name census is round 104's input.

<status>staged</status>
<status>pending -- GO 2026-10-13T23:0xZ by the issuer (2.0.0_SA_COO~R2): fa-1 merged @ebe4c8d287, so `contract.py` and `orchestrate.py` exist at the base this worktree is cut from.</status>
<status>complete -- 2026-10-13T23:4xZ by the issuer (2.0.0_SA_COO~R2): wk-AMGT_RESAPP-425 @bd91e2adb3 merged @6c10ae95c6, proof instance VALID (rc=0). AC1 PASS (`AIFILL FA-4 ARMS: YES (12 of 12)`, re-run by the issuer in the worker's tree and on the integrated package), AC2 PASS (28 passed); `ruff check lib/research/aifill` clean.</status>
<round>104</round>
<workstream>AIFILL</workstream>
<slot>0.9.0_WK_AMGT_RESAPP~425</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
