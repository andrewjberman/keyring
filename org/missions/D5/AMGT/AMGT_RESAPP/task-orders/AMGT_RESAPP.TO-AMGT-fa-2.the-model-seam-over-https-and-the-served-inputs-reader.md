# AMGT_RESAPP task order -- `AMGT-fa-2` -- THE MODEL SEAM OVER HTTPS (WEB SEARCH, CITED) AND THE SERVED-INPUTS READER (FWD-41; A BUILD)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md</decomp_doc>
<owned_cells>AMGT-fa-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~421</issued_to>
<issued_by>2.0.0_SA_COO~R2</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-fa-2.the-model-seam-over-https-and-the-served-inputs-reader</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing is scheduled; a library module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- the cell writes and tests local Python only; `inputs.py` calls `lambda.invoke` (GET) in production use, but the checks use a fake client and no AWS call is made.
comp-adversary: RUN at the cut -- `check_fa2_model.py` is a prepared acceptance check (18 arms: the parser over the recorded real response, the request shape, five ModelError paths, the default transport's url and headers with urlopen faked, the no-key stop, the served-inputs reader over a fake Lambda); at the base it exits 1 on `ModuleNotFoundError: No module named 'lib.research.aifill'`, the build check failing as expected.
EGRESS CLASS, declared: NONE by the cell and its checks (urlopen and the Lambda client are faked); the module's production use is one HTTPS POST to api.anthropic.com per model call, run later by the issuer.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-421` (branch `wk-AMGT_RESAPP-421`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-421`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-fa-2` (round 104, workstream AIFILL, decomposition `org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md`)

FWD-41 asks that the web fill be "a model call on the EXISTING Anthropic path with its server-side web search tool, never OpenAI". MEASURED at the cut: the installed `anthropic` SDK is 0.45.0 and CRASHES on the web-search response (`AttributeError: 'typing.Union' object has no attribute '__discriminator__'` on the server-tool blocks), while the same request over plain HTTPS returns in about 7 s with cited text. So the seam is the stdlib HTTPS call. You write `model.py` (the seam) and `inputs.py` (how the producer reads the two served route bodies), and one test module.

### The recorded real response (your fixture)
`C:/dev/wk-resapp-421/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round104_aifill_prep/fixtures/web_search_response_asml.json` is `{"request": ..., "response": ...}`: the request that was sent and the real Messages API response (`content` holds, in order, two `server_tool_use` blocks each with `input.query`, two `web_search_tool_result` blocks, and nine `text` blocks, five of which carry `citations` of type `web_search_result_location` with `url`, `title` and `cited_text`; `usage` carries `input_tokens`, `output_tokens` and `server_tool_use.web_search_requests`; `stop_reason` is `end_turn`; `model` is set). Read it before you write the parser.

### `lib/research/aifill/model.py` -- exact interface (the builders' `ctx.model` is `call_model`)
- `MODEL = "claude-opus-5"`; `WEB_SEARCH_TOOL_TYPE = "web_search_20250305"`; `API_URL = "https://api.anthropic.com/v1/messages"`; `API_VERSION = "2023-06-01"`.
- `class ModelError(Exception)`: every failure of a model call. (Its class name `ModelError` is how the orchestrator recognises it.)
- `class ModelResult`: a small class or dataclass with attributes `text` (str), `citations` (list of dicts with exactly the keys `url`, `title`, `cited_text`), `searches` (list of str), `input_tokens` (int), `output_tokens` (int), `web_search_requests` (int), `model` (str), `stop_reason` (str).
- `parse_response(resp) -> ModelResult` (pure): `text` is the concatenation, with no separator, of the `text` of every `text` content block (the API already carries each block's own spacing); `citations` are the `citations` entries of the text blocks that have a `url`, in order of first appearance, de-duplicated by `url`, each as `{"url", "title", "cited_text"}` (a missing title or cited_text is None); `searches` are the `input.query` strings of the `server_tool_use` blocks; `web_search_requests` is `usage.server_tool_use.web_search_requests` (0 when absent); `input_tokens` and `output_tokens` from `usage` (0 when absent); `model` is `resp["model"]` or `MODEL`; `stop_reason` as given. It raises `ModelError` when: `resp` is not a dict; `resp.get("type") == "error"` (the message is the API's own `error.message`, with its `error.type`); `content` is not a list; `stop_reason == "max_tokens"` (message says the answer was truncated); or the concatenated text is empty after strip.
- `call_model(prompt, *, system=None, web_search_max_uses=0, max_tokens=1500, model=None, transport=None, timeout=120) -> ModelResult`: builds the request body `{"model": model or MODEL, "max_tokens": max_tokens, "messages": [{"role": "user", "content": prompt}]}`, adds `"system": system` only when given, and adds `"tools": [{"type": "web_search_20250305", "name": "web_search", "max_uses": web_search_max_uses}]` only when `web_search_max_uses > 0`. It sends the body through `transport(body) -> response dict` (an injectable seam, default `_default_transport`) and returns `parse_response(response)`. `_default_transport(body, timeout)` reads `ANTHROPIC_API_KEY` from the environment BEFORE any request and raises `ModelError` naming `ANTHROPIC_API_KEY` when it is missing or empty; POSTs `json.dumps(body)` to `API_URL` with `urllib.request.urlopen(request, timeout=timeout)` and the headers `x-api-key`, `anthropic-version: 2023-06-01`, `content-type: application/json`; parses the JSON; turns `urllib.error.HTTPError` (read its body for the API's message), `urllib.error.URLError`, `OSError`/`TimeoutError` and a JSON decode failure into `ModelError` with a short plain message. The key is never printed, logged or put in an exception message. When `transport` is given, the key is not read.
- The module imports only the standard library; it never imports `anthropic`.

### `lib/research/aifill/inputs.py` -- exact interface
- `served_inputs(security_key, lam=None, function_name="opal-amgt-scoped-api") -> dict`: returns `{"overlay": <body dict or None>, "thesis": <body dict or None>, "errors": {<route>: <short string>}}`. For each route in `("overlay", "thesis")` it invokes the function once with the event `{"rawPath": "/api/scoped/amgt/security/<security_key>/<route>", "queryStringParameters": None, "requestContext": {"http": {"method": "GET"}}, "headers": {"x-firm-id": "opal"}}` (`lam.invoke(FunctionName=function_name, Payload=json.dumps(event).encode("utf-8"))`), reads `["Payload"].read()`, parses it as JSON, and takes `statusCode` and `json.loads(body)`. A status other than 200, an unparseable body, or any exception from `invoke` leaves that route's body None and sets `errors[route]` to a string naming the status (`"status 500"`) or the exception class and message. One route failing never blocks the other. When `lam` is None, build `boto3.client("lambda", region_name="us-east-1")` inside the function (import `boto3` inside the function, so importing the module needs no AWS library). The key goes into the path as is (the same call the V1 census instrument makes).

### `lib/research/aifill/tests/test_model_inputs.py`
Your own pytest module (no `__init__.py`): the parser over the recorded fixture, the request body with and without web search, every `ModelError` path, the no-key stop (no network used), the default transport with `urllib.request.urlopen` faked, and `served_inputs` over a fake Lambda client (both routes ok, one route failing, both failing).

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W421-S<k>`, `disarm_owner` `2.0.0_SA_COO~R2`.

## 2. BOUNDS


1. Write ONLY `lib/research/aifill/model.py`, `lib/research/aifill/inputs.py` and `lib/research/aifill/tests/test_model_inputs.py`. `__init__.py`, `contract.py` and `orchestrate.py` are cell fa-1's (written in parallel): do not create them; Python imports `lib.research.aifill.model` without an `__init__.py` (a namespace package), and your checks run that way.
2. The real network and the real key are out of bounds: the test and the checks fake `urllib.request.urlopen` and the Lambda client; the issuer runs the one live call at the drain.
- Leave `lib/research/management/`, `lib/research/filings/`, `lib/research/posture/` and every existing module untouched.
- No network, no AWS, no real model call, no `pip install`: every model call in your tests is a stub or the recorded response. The `anthropic` package is never imported (the installed 0.45.0 crashes on web-search blocks).
- Python 3.9 syntax (`from __future__ import annotations`, `typing.Optional`, no `X | Y` unions evaluated at runtime, no `match`); ASCII-only source files (write non-ASCII characters as `\uXXXX` escapes); stdlib only.
- Run the commit gate before you commit: `bash .tools/commit-gate.sh <each .py you wrote>` (it runs `py_compile` and `ruff`); a finding there is yours to fix.

## 3. SURFACES

<paths>
lib/research/aifill/model.py
lib/research/aifill/inputs.py
lib/research/aifill/tests/test_model_inputs.py
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-fa-2"><invocation>cd C:/dev/wk-resapp-421 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round104_aifill_prep/checks/check_fa2_model.py" | tail -4; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `AIFILL FA-2 ARMS: YES (N of N)` with N equal to the count printed and N at least 17, no `FAIL` arm line above it; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-fa-2"><invocation>cd C:/dev/wk-resapp-421 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python -m pytest -q --color=no -p no:cacheprovider lib/research/aifill/tests/test_model_inputs.py | tail -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the last non-empty line before `exit=` reads `N passed` (N at least the count your test module's functions define) with no `failed` and no `error` in the last 3 lines; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~421 <0.9.0_WK_AMGT_RESAPP~421@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~421/AMGT_RESAPP.TO-AMGT-fa-2.the-model-seam-over-https-and-the-served-inputs-reader.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character; each criterion's `expect` recorded as an ordered regex of the printed lines when the prose has regex-active characters.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- each criterion's deciding output line (verbatim) and the arm count;
- the arm lines of AC1 that read FAIL, if any, and the pytest summary line.
- any row.
The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** An independent head: it imports nothing of fa-1. `model.MODEL` repeats the producer model name that fa-1's `contract.PRODUCER_MODEL` carries; the drain reads both and they must agree. The recorded response is the real one (a live call at the cut, about 13 cents); the seam's request shape follows the Anthropic Messages API web search tool `web_search_20250305` (`max_uses`). The 21,743 input tokens of the fixture's call are the cost driver to remember at the 93-name run (round 104): about 13 cents per two-search call at the module's rates.

<status>pending</status>
<round>104</round>
<workstream>AIFILL</workstream>
<slot>0.9.0_WK_AMGT_RESAPP~421</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
