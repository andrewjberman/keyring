# TO IRPT_ANLREQ.TO-AR-y-250.kimi-search-qa-harness -- the QA harness for the search-based swap -- earns the flag, yields the receipt; offline with fakes, the live run designed

<to_id>IRPT_ANLREQ.TO-AR-y-250</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~83</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>21</round>
<workstream>YR</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD
**Decomp cell:** `AR-y-250` (`decompositions/IRPT_ANLREQ_DECOMP_R22C_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~83`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-83` (branch `wk-IRPT_ANLREQ-83`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~83 <0.9.0_WK_IRPT_ANLREQ~83@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W83-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-250`, inlined) -- GATE (1): THE QA RECEIPT, FOR THE SEARCH-BASED SWAP. A harness and a record shape, tested offline. NO LIVE CALL.

**Read first (all three cells of this round):** the CTO's ruling (a') (msg 7137): do NOT build on `$web_search` (the Kimi builtin tool that retires 2026-10-20); the server calls Kimi's search endpoint `POST https://api.moonshot.ai/v1/tools/search` (headers `Content-Type: application/json` and `Authorization: Bearer <key>`; body `{"text_query": <string, not empty>, "limit": <1..20, default 5>, "timeout_seconds": <1..60>}`; 200 answers `{"search_results": [{"authority","date","icon","mime","site_name","snippet","text","title","url"}]}`, an empty list when nothing matches; 400/401/403/408/429/500/502/504 are errors; billed per call that returns a non-empty list; source: https://platform.kimi.ai/docs/api/tools-search), then makes ONE plain chat call (NO `tools`, NO `tool_choice`) that proposes at most 3 ETFs. **The ruling's condition:** the chat call may propose only a ticker that appears in a search result it was given, and each proposal cites that result's `url`; a proposal with no matching result is DROPPED before provider verification. A candidate is shown only after the provider verifies it exactly (`FOUND`, `EXACT_PROVIDER_MATCH`); the user must pick; nothing fills a box. Proof set (fixed BEFORE the run): `TIMXX` plus at least 4 known funds, each suggestion schema-valid and provider-verified, 0 errors; if it fails or does not finish this round, fallback (b) ships (TIMXX keeps "no match", only the hint wording goes out). The capability reaches the resident only inside a signed release pair. The estate's earlier QA record is `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/Y5P2/KIMI_WEB_SEARCH_QA_FINDINGS_20261003.md` (the `$web_search` failures that this design avoids) and the read record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~79/r22/KIMI_QA_HARNESS.json` (the gate, the parse, the transport, the secret name `astn/kimi/api-key`, never its value).
**THE INTERFACE (fixed here so the three cells build in parallel):** `KimiAdvisory(*, send, telemetry, clock=..., search_capability=None, search=None)` where `search` is a port `search(text_query, limit, timeout_seconds) -> list of {title, url, snippet}` (the transport lives in `ycharts/generate/kimi_port.py`: `kimi_search(read_secret, url=KIMI_SEARCH_URL, opener=...)`, same secret and the same no-secret-in-logs rule as `kimi_send`). `search_capability` for the `swap` kind is a dict `{"model": MODEL, "verified": True, "qa_receipt_sha256": <64 hex>, "search_limit": <int 1..10>}` and nothing else (the old `request_fields`/`tools`/`tool_choice` members are REFUSED). `KimiAdvisory.call("swap", symbol, context_symbols=None, excluded=None, deadline=None)` keeps its return shape `{"result": {... "candidates": [{"symbol","reason","sources"}] ...}, "failure": ..., "attempts": [...]}`: a refused capability or a missing `search` port returns `KIMI_WEB_SEARCH_UNVERIFIED` as today, with no send and no search.

1. **Read** `intake/resolution_kimi.py` (the gate as it stands at HEAD and the interface in THE INTERFACE above: another worker builds it in parallel as cell `AR-y-249`; build against the interface, not against its code), `ycharts/generate/kimi_port.py`, and the 10-03 findings file. Record `read`.
2. **The harness.** ONE new file `ycharts/generate/kimi_search_qa.py` (ASCII; no network client of its own: it takes the `send` and `search` ports the advisory takes) that: holds a FIXED case list written in the file BEFORE any run: `TIMXX` plus at least 4 known funds/ETFs/mutual funds the provider can be asked about, plus one nonsense symbol that must yield an empty candidate list, plus two symbol-shaped injection strings that must not change the output shape (symbols are validated by `validate_symbols` before send, so only symbol-shaped strings can reach the model: row `W79-S3`); builds its own `KimiAdvisory(send=..., search=..., telemetry=<a recording stub>, search_capability=<the candidate {model, verified: True, qa_receipt_sha256: <placeholder 64 hex of zeros>, search_limit}>)` with `verified` set True ONLY inside the QA run (the real gate refuses an unverified capability, so the QA is how the flag is earned: say so in a comment and in the record); runs each case through `advisory.call("swap", symbol)`; grades each answer for SHAPE and SUPPORT only (the JSON keys parse; at most three candidates; every candidate's symbol appears in a result the fake or real search returned and every source is a result url, i.e. the drop rules held; an empty answer is an empty list; 0 errors/failures per case) and for PROVIDER VERIFICATION through a `verify` port it is given (exact FOUND), never for investment judgment; writes a QA record (a JSON object: `model`, `search_limit`, the case list with each case's verdict, the answer's sha256, the search results' sha256, `started_at`, `all_ok`, the harness file's own sha256) and returns `qa_receipt_sha256` = the sha256 of that record's canonical JSON (sorted keys, no whitespace variance); ANY case failing yields NO receipt.
3. **Tests, offline.** `ycharts/generate/tests/test_kimi_search_qa.py` (at least 7 tests; fake `send`, `search`, `verify`): good fakes produce a receipt equal to the sha256 of the canonical record and the same twice; a case with a candidate the provider does not verify, a malformed or over-long answer, a candidate not supported by a result, a four-candidate answer, a non-HTTPS source, or an answer that obeys an injection string yields NO receipt; a case list shorter than 6 or without `TIMXX` is refused before any send; the receipt changes if one answer changes. `before_arm`: the tests cannot run before the file exists (record that). Then `ycharts/generate/tests` files that collect (counts; the known baseline from `AR-y-246`'s record) and `intake/tests` (365 floor).
4. **The live QA, designed not run.** Write `live_qa` in the record: the exact command a Dell CloudOps lane would run (the harness with `kimi_port.kimi_send` and `kimi_port.kimi_search` over the real secret read by id), what is sent (symbols only, no client data), the cost bound (cases times attempts times the `swap` budget plus one search call per case), where the QA record and the receipt value are stored (the QA record is a repo file; the receipt value goes into the capability file the resident package carries, see cell `AR-y-251`), and that the live run is a LATER order to a Dell lane under the signed pair.
5. **Write `r22/KIMI_SEARCH_QA_HARNESS.json`:** `read`, `harness` {`path`, `sha256`, `cases` (the fixed list)}, `tests` {`added`, `passed`, `failed`, `folders`}, `live_qa`, `claim`, `not_read`.
6. **In your report:** the case list, the tests, what the live QA still needs.

### ACCEPTANCE

<criterion id="AR250-y-AC1" cell_refs="AR-y-250"><invocation>python C:/dev/wk-irpt-anlreq-83/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y250-qa --root C:/dev/wk-irpt-anlreq-83</invocation><expect>Y250-QA-OK</expect></criterion>
`AR250-y-AC1`: the record names the fixed case list (TIMXX, at least 4 known funds, a nonsense symbol, two injection strings), the harness file with its sha256, at least 7 passing offline tests including every no-receipt case, and a live QA design.

<criterion id="AR250-y-AC2J" cell_refs="AR-y-250" judgment="true"/>
`AR250-y-AC2J` (judgment, graded at L9, never by you): the case list is fixed in the file before any run, `verified` is True only inside the QA run and said so, no receipt is minted for an unverified, unsupported, malformed or injected answer, the harness has no network client of its own, and no live call was made.

<expected_criteria>AR250-y-AC1 AR250-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~83/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/kimi_search_qa.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_kimi_search_qa.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R22C_Y.md</decomp_doc>
<owned_cells>AR-y-250</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~83/IRPT_ANLREQ.TO-AR-y-250.kimi-search-qa-harness.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-250`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR250-y-AC1,AR250-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- new source and test files in a worktree; nothing is called, released or applied; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the CTO's ruling (a') (msg 7137) and the 10-03 QA findings (Y5P2) against the cell; the lens: a proposal that was never in a search result, a candidate shown without provider verification, a capability flag set without a receipt, a call to the retiring $web_search. The order requires the ticker-in-a-result and cited-url rule, the verification, and no use of the `tools` request field. NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's ruling (a') (msg 7137: the Kimi search endpoint plus ONE plain chat call; ruling B's gates, proof set, one-round box and fallback (b) stand) as workstream `YR` round 21. The grant names every file the cell writes (the first cuts `AR-y-246`/`-247` omitted them: rows `W79-S1`, `W80-S1`). Base: `AR250-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.
