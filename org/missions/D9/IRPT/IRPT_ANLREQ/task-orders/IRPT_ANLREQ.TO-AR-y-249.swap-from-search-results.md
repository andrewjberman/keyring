# TO IRPT_ANLREQ.TO-AR-y-249.swap-from-search-results -- the swap advisory proposes from Kimi search results with one plain chat call

<to_id>IRPT_ANLREQ.TO-AR-y-249</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~82</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>21</round>
<workstream>YR</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD
**Decomp cell:** `AR-y-249` (`decompositions/IRPT_ANLREQ_DECOMP_R22C_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~82`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-82` (branch `wk-IRPT_ANLREQ-82`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~82 <0.9.0_WK_IRPT_ANLREQ~82@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W82-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-249`, inlined) -- THE SWAP ADVISORY, REBUILT ON THE SEARCH ENDPOINT. Code and tests only; no live call; nothing released.

**Read first (all three cells of this round):** the CTO's ruling (a') (msg 7137): do NOT build on `$web_search` (the Kimi builtin tool that retires 2026-10-20); the server calls Kimi's search endpoint `POST https://api.moonshot.ai/v1/tools/search` (headers `Content-Type: application/json` and `Authorization: Bearer <key>`; body `{"text_query": <string, not empty>, "limit": <1..20, default 5>, "timeout_seconds": <1..60>}`; 200 answers `{"search_results": [{"authority","date","icon","mime","site_name","snippet","text","title","url"}]}`, an empty list when nothing matches; 400/401/403/408/429/500/502/504 are errors; billed per call that returns a non-empty list; source: https://platform.kimi.ai/docs/api/tools-search), then makes ONE plain chat call (NO `tools`, NO `tool_choice`) that proposes at most 3 ETFs. **The ruling's condition:** the chat call may propose only a ticker that appears in a search result it was given, and each proposal cites that result's `url`; a proposal with no matching result is DROPPED before provider verification. A candidate is shown only after the provider verifies it exactly (`FOUND`, `EXACT_PROVIDER_MATCH`); the user must pick; nothing fills a box. Proof set (fixed BEFORE the run): `TIMXX` plus at least 4 known funds, each suggestion schema-valid and provider-verified, 0 errors; if it fails or does not finish this round, fallback (b) ships (TIMXX keeps "no match", only the hint wording goes out). The capability reaches the resident only inside a signed release pair. The estate's earlier QA record is `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/Y5P2/KIMI_WEB_SEARCH_QA_FINDINGS_20261003.md` (the `$web_search` failures that this design avoids) and the read record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~79/r22/KIMI_QA_HARNESS.json` (the gate, the parse, the transport, the secret name `astn/kimi/api-key`, never its value).
**THE INTERFACE (fixed here so the three cells build in parallel):** `KimiAdvisory(*, send, telemetry, clock=..., search_capability=None, search=None)` where `search` is a port `search(text_query, limit, timeout_seconds) -> list of {title, url, snippet}` (the transport lives in `ycharts/generate/kimi_port.py`: `kimi_search(read_secret, url=KIMI_SEARCH_URL, opener=...)`, same secret and the same no-secret-in-logs rule as `kimi_send`). `search_capability` for the `swap` kind is a dict `{"model": MODEL, "verified": True, "qa_receipt_sha256": <64 hex>, "search_limit": <int 1..10>}` and nothing else (the old `request_fields`/`tools`/`tool_choice` members are REFUSED). `KimiAdvisory.call("swap", symbol, context_symbols=None, excluded=None, deadline=None)` keeps its return shape `{"result": {... "candidates": [{"symbol","reason","sources"}] ...}, "failure": ..., "attempts": [...]}`: a refused capability or a missing `search` port returns `KIMI_WEB_SEARCH_UNVERIFIED` as today, with no send and no search.

1. **Read** `intake/resolution_kimi.py` (the whole file: `prompt_for`, `_parse`, `KimiAdvisory.call`, `BUDGETS`, `validate_symbols` use), `ycharts/generate/kimi_port.py`, `intake/tests/test_resolution_kimi.py`, `ycharts/generate/tests/test_y4_check_gate.py`. Record `read` {`files`, `what_changes`}.
2. **The transport.** In `ycharts/generate/kimi_port.py` add `KIMI_SEARCH_URL = "https://api.moonshot.ai/v1/tools/search"` and `kimi_search(read_secret, url=KIMI_SEARCH_URL, opener=urllib.request.urlopen)` returning `search(text_query, limit, timeout_seconds)`: one HTTPS JSON POST, the key read through the same `read_secret` port and held in memory only (never printed, logged or put in an exception), the response parsed to a list of `{title, url, snippet}` (strings only, each bounded to 600 characters; `url` must be an HTTPS URL with a hostname; items that fail are skipped), the call bounded by `timeout_seconds` and by a total response size cap; any HTTP error or malformed body raises the module's existing failure type (read how `kimi_send` does it and match it) with a code that names the status and never the body.
3. **The advisory.** In `intake/resolution_kimi.py`: (a) `KimiAdvisory.__init__` takes `search=None`; (b) the capability gate for `swap` becomes the dict in THE INTERFACE (model equals MODEL, `verified is True`, a truthy `qa_receipt_sha256` that is 64 hex, `search_limit` an int 1..10, no other key) and a missing `search` port: otherwise `KIMI_WEB_SEARCH_UNVERIFIED`, before any telemetry, search or send; (c) for `swap`: the search query is built from the symbol only (`"<SYMBOL> ticker ETF fund"`; no context, no holdings, no client data), one call to `search(query, search_limit, timeout_seconds)` inside the kind's deadline; if the list is empty, return the empty-candidates result without a chat call; (d) ONE plain chat call (no `tools`, no `tool_choice` anywhere in the payload) whose prompt carries the results as data (title, url, snippet, numbered) and the instruction to identify the asset and propose up to three ETF alternatives with similar exposure, symbols and `sources` taken ONLY from the numbered results, treating the results as untrusted text, returning the same JSON shape `_parse` parses today; (e) AFTER parse: every candidate's `symbol` must appear (case-insensitive, as a whole token) in the title or snippet of at least one result, and every URL in its `sources` must be the `url` of a result given; a candidate failing either is DROPPED and counted (`dropped_unsupported`), never passed on; the overall `sources` of the result likewise; (f) the existing gates stay: at most 3 candidates, HTTPS URLs, `excluded_symbols` refusal, evidence rules. The `check` kind is untouched.
4. **The tests.** `intake/tests/test_resolution_kimi.py` is edited ONLY where its two swap-capability fixtures (:82-100) use the old `request_fields` shape: move them to the new capability shape and keep their intent. New file `intake/tests/test_swap_from_search.py` (at least 10 tests; fake `send`, fake `search`): capability absent/refused (including one holding `request_fields`) sends nothing and searches nothing; the payload of the chat call has no `tools` and no `tool_choice` and carries the numbered results; a candidate whose symbol is in a result and whose source url is a given result is kept; a candidate whose symbol is in NO result is dropped; a candidate citing a url that is not a given result is dropped; an injection string inside a result's snippet does not change the output shape (the fake model returns what a hostile prompt would elicit and the code still drops the unsupported candidate); an empty search result list makes no chat call; a search error makes no chat call and returns the failure; the symbol is the only thing in the query. And `ycharts/generate/tests/test_kimi_search_port.py` (at least 5 tests; fake `opener`): the request URL/headers/body; a good body; an empty list; a malformed body; an HTTP error code; the key never in the exception text. `before_arm`: run the new tests against HEAD without the change: they cannot import (record that), and run the two edited fixtures: they FAIL on HEAD under the new capability shape. Then: `intake/tests` (365 floor) and the `ycharts/generate/tests` files that collect (4 custody failures and fitz collection errors are the known baseline at 85f43d3456: show they are the same at HEAD, row `W79-S4`).
5. **Write `r22/SWAP_FROM_SEARCH.json`:** `read`, `transport` (file:lines), `advisory` (file:lines; the gate, the query, the prompt shape in words, the drop rules), `tests` {`added`, `passed`, `failed`, `folders`}, `before_arm`, `files_changed`, `claim`, `not_read` (the live endpoint and the live model: nothing was called).
6. **In your report:** the interface as built, the drop rules, the counts.

### ACCEPTANCE

<criterion id="AR249-y-AC1" cell_refs="AR-y-249"><invocation>python C:/dev/wk-irpt-anlreq-82/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y249-swap --root C:/dev/wk-irpt-anlreq-82</invocation><expect>Y249-SWAP-OK</expect></criterion>
`AR249-y-AC1`: the record names the transport and the advisory change, the new test files pass (at least 10 and 5 tests), the intake folder passes at 365 or more, and the old `request_fields` capability shape is refused.

<criterion id="AR249-y-AC2J" cell_refs="AR-y-249" judgment="true"/>
`AR249-y-AC2J` (judgment, graded at L9, never by you): the chat call carries no `tools` or `tool_choice`, only a ticker that appears in a given search result and cites a given url survives, the unsupported are dropped before any provider verification, the key is never printed or logged, and no live call was made.

<expected_criteria>AR249-y-AC1 AR249-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~82/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
infra/aws/lambda/investor-reporting/intake/resolution_kimi.py
infra/aws/lambda/investor-reporting/ycharts/generate/kimi_port.py
infra/aws/lambda/investor-reporting/intake/tests/test_resolution_kimi.py
infra/aws/lambda/investor-reporting/intake/tests/test_swap_from_search.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_kimi_search_port.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R22C_Y.md</decomp_doc>
<owned_cells>AR-y-249</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~82/IRPT_ANLREQ.TO-AR-y-249.swap-from-search-results.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-249`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR249-y-AC1,AR249-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- source and test edits in a worktree; nothing is called, released or applied; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the CTO's ruling (a') (msg 7137) and the 10-03 QA findings (Y5P2) against the cell; the lens: a proposal that was never in a search result, a candidate shown without provider verification, a capability flag set without a receipt, a call to the retiring $web_search. The order requires the ticker-in-a-result and cited-url rule, the verification, and no use of the `tools` request field. NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's ruling (a') (msg 7137: the Kimi search endpoint plus ONE plain chat call; ruling B's gates, proof set, one-round box and fallback (b) stand) as workstream `YR` round 21. The grant names every file the cell writes (the first cuts `AR-y-246`/`-247` omitted them: rows `W79-S1`, `W80-S1`). Base: `AR249-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.
