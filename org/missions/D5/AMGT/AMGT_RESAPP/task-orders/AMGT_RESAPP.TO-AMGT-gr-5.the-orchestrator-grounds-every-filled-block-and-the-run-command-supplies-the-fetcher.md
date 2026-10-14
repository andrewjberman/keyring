# AMGT_RESAPP task order -- `AMGT-gr-5` -- THE ORCHESTRATOR GROUNDS EVERY FILLED BLOCK BEFORE THE DOCUMENT IS BUILT, AND THE RUN COMMAND SUPPLIES THE FETCHER (FWD-41 ROUND 106; A BUILD, CTO 4(a))

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md</decomp_doc>
<owned_cells>AMGT-gr-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~454</issued_to>
<issued_by>2.0.0_SA_COO~R2</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-gr-5.the-orchestrator-grounds-every-filled-block-and-the-run-command-supplies-the-fetcher</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing is scheduled; a library module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, grant, key or policy is touched; the cell writes and tests local Python only.
comp-adversary: RUN at the cut -- `check_gr5_orchestrate.py` is a prepared acceptance check (20 arms, offline: stub builders, a router model, a stub fetch); at the base it fails on the missing `fetch` argument, the build check failing as expected.
EGRESS CLASS, declared: NONE. No network call by the cell or its checks (the model is a stub or a recorded response); no Bloomberg call.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-454` (branch `wk-AMGT_RESAPP-454`, cut from the merged head that carries cells gr-1 to gr-4 (the issuer cuts this worktree after they merge)). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-454`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-gr-5` (round 106, workstream AIFILL, decomposition `org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md`)

The grounding step sits in ONE place: after a builder returns a usable filled block, the orchestrator fetches the block's cited pages, grounds the text, and replaces the block with the grounded one (or a NONE block saying why). All five builders are covered and none is rewritten for it. The run command supplies the real fetcher.

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

### `lib/research/aifill/orchestrate.py`
- `BlockContext(security_key, inputs, model, now, fetch=None)`: the new attribute `ctx.fetch` is a callable `fetch(url) -> source dict` (the shape of `sources.fetch_source`) or `None`.
- `build_document(security_key, inputs, model, now=None, builders=None, fetch=None, ground=True)`. `fetch` is wrapped in a per-document cache (one fetch per url however many blocks cite it) and handed to every builder's context (None stays None). A builder's block is a DRAFT: it is validated with `require_grounding=False`. When `ground` is true each draft is passed through the grounding step below; when false drafts pass through as they are (and the final document check uses `require_grounding=ground`).
- `GROUNDING_REASON = "None of the model's statements could be confirmed in a source that answered, so the text was withheld."` (exactly).
- The grounding step, for a draft with `source_class` other than NONE (a NONE draft is returned untouched with no fetch and no model call):
  * `WEB_SEARCH`: the unique `url`s of its web citations, the first 8 in order, are fetched with `ctx.fetch` (each result copied and given `kind` web and the asked `url`; an exception or no fetcher gives a source with status `ERROR`, empty text). `OPAL_SOURCE`: no fetch; for each path in the draft's `opal_inputs` the value is resolved by dotted keys in `ctx.inputs`; non-empty values are dumped with `json.dumps(sort_keys=True, default=str)` and joined by newlines into ONE text; there is one source per opal citation, `kind` opal, `label` the citation's `ref`, status `OK`, that text (none usable when no path resolved to a value).
  * `grounding.ground_block(draft["text"], sources, ctx.model, ctx.now)`. Not `ok` (or any exception) -> `contract.none_block(block_id, GROUNDING_REASON)`.
  * Otherwise the grounded block is `contract.make_block(block_id, source_class, result.text, kept_citations, draft["opal_inputs"], draft["model_call"], grounding=result.record, require_grounding=True)` where `kept_citations` are the draft's citations whose `url` is in `result.used_urls` (web) or whose `ref` is in `result.used_labels` (opal), with their titles and quotes unchanged. A `ContractError` -> the NONE block with `GROUNDING_REASON`.
- The document's `producer.version` is the contract's `PRODUCER_VERSION` (`opal-aifill/1.1.0`).
### `lib/research/aifill/run.py`
- `default_fetch = sources.fetch_source` (module attribute); `main(argv=None, client=None, fetch=None)` passes `fetch if fetch is not None else default_fetch` to `build_document(..., fetch=...)`, and passes `None` when `--no-model` is given (a run with no model makes no fetch).

### Tests
A new test module `lib/research/aifill/tests/test_orchestrate_grounding.py` (no `__init__.py`): one test per behaviour above. The existing tests of `tests/test_contract_orchestrate.py` and `tests/test_store_run.py` that build documents from stub builders returning filled blocks pass `ground=False` (or a stub fetch and model) so that they keep their meaning; change only what the new step breaks, and say which in your report.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W454-S<k>`, `disarm_owner` `2.0.0_SA_COO~R2`.

## 2. BOUNDS


1. Write ONLY `lib/research/aifill/orchestrate.py`, `lib/research/aifill/run.py`, `lib/research/aifill/tests/test_orchestrate_grounding.py`, `lib/research/aifill/tests/test_contract_orchestrate.py` and `lib/research/aifill/tests/test_store_run.py`. The contract, the grounding and sources modules and the five builders are other cells'.
2. `orchestrate.py` does no network of its own (the fetcher arrives as an argument).
- Leave `lib/research/management/`, `lib/research/filings/`, `lib/research/posture/` and every existing module untouched.
- No network, no AWS, no real model call, no `pip install`: every model call in your tests is a stub or the recorded response. The `anthropic` package is never imported (the installed 0.45.0 crashes on web-search blocks).
- Python 3.9 syntax (`from __future__ import annotations`, `typing.Optional`, no `X | Y` unions evaluated at runtime, no `match`); ASCII-only source files (write non-ASCII characters as `\uXXXX` escapes); stdlib only.
- Run the commit gate before you commit: `bash .tools/commit-gate.sh <each .py you wrote>` (it runs `py_compile` and `ruff`); a finding there is yours to fix.

## 3. SURFACES

<paths>
lib/research/aifill/orchestrate.py
lib/research/aifill/run.py
lib/research/aifill/tests/test_orchestrate_grounding.py
lib/research/aifill/tests/test_contract_orchestrate.py
lib/research/aifill/tests/test_store_run.py
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-gr-5"><invocation>cd C:/dev/wk-resapp-454 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round106_aifill_prep/checks/check_gr5_orchestrate.py" | tail -4; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `AIFILL GR-5 ARMS: YES (N of N)` with N equal to 20, no `FAIL` arm line above it; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-gr-5"><invocation>cd C:/dev/wk-resapp-454 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python -m pytest -q --color=no -p no:cacheprovider lib/research/aifill/tests | tail -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the last non-empty line before `exit=` reads `N passed` (N at least 498) with no `failed` and no `error` in the last 3 lines; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~454 <0.9.0_WK_AMGT_RESAPP~454@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~454/AMGT_RESAPP.TO-AMGT-gr-5.the-orchestrator-grounds-every-filled-block-and-the-run-command-supplies-the-fetcher.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character; each criterion's `expect` recorded as an ordered regex of the printed lines when the prose has regex-active characters.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- each criterion's deciding output line (verbatim) and the arm count;
- the arm lines of AC1 that read FAIL, if any, AC2's pytest summary line, and the list of existing tests you changed.
- any row.
The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** STAGED behind gr-1, gr-2, gr-3 and gr-4. Proven satisfiable by the issuer's reference (20 of 20). Centralising the step in the orchestrator is a deliberate simplification: five builders each calling the grounding step would be five copies of the same fetch-and-ground code and five test rewrites. OPAL_SOURCE blocks are grounded on the served fields they list in `opal_inputs`, so the contract's rule applies to them too; the numeric guard the Opal builders already have stays.

<status>staged</status>
<round>106</round>
<workstream>AIFILL</workstream>
<slot>0.9.0_WK_AMGT_RESAPP~454</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
