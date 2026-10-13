# TO IRPT_ANLREQ.TO-AR-y-251.swap-suggestions-wired-and-called-r2 -- the server asks the swap advisory when its capability is verified, verifies each candidate, attaches them as suggestions -- default off; capability carried as a package member

<to_id>IRPT_ANLREQ.TO-AR-y-251</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~84</issued_to>
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
**Decomp cell:** `AR-y-251` (`decompositions/IRPT_ANLREQ_DECOMP_R22C_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~84`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-84` (branch `wk-IRPT_ANLREQ-84`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~84 <0.9.0_WK_IRPT_ANLREQ~84@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W84-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-251`, inlined) -- GATES (2) AND (3), SERVER SIDE, RE-CUT WITH ITS GRANT. Code and tests only; the capability file is absent, so nothing changes until a receipt exists.

**Read first (all three cells of this round):** the CTO's ruling (a') (msg 7137): do NOT build on `$web_search` (the Kimi builtin tool that retires 2026-10-20); the server calls Kimi's search endpoint `POST https://api.moonshot.ai/v1/tools/search` (headers `Content-Type: application/json` and `Authorization: Bearer <key>`; body `{"text_query": <string, not empty>, "limit": <1..20, default 5>, "timeout_seconds": <1..60>}`; 200 answers `{"search_results": [{"authority","date","icon","mime","site_name","snippet","text","title","url"}]}`, an empty list when nothing matches; 400/401/403/408/429/500/502/504 are errors; billed per call that returns a non-empty list; source: https://platform.kimi.ai/docs/api/tools-search), then makes ONE plain chat call (NO `tools`, NO `tool_choice`) that proposes at most 3 ETFs. **The ruling's condition:** the chat call may propose only a ticker that appears in a search result it was given, and each proposal cites that result's `url`; a proposal with no matching result is DROPPED before provider verification. A candidate is shown only after the provider verifies it exactly (`FOUND`, `EXACT_PROVIDER_MATCH`); the user must pick; nothing fills a box. Proof set (fixed BEFORE the run): `TIMXX` plus at least 4 known funds, each suggestion schema-valid and provider-verified, 0 errors; if it fails or does not finish this round, fallback (b) ships (TIMXX keeps "no match", only the hint wording goes out). The capability reaches the resident only inside a signed release pair. The estate's earlier QA record is `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/Y5P2/KIMI_WEB_SEARCH_QA_FINDINGS_20261003.md` (the `$web_search` failures that this design avoids) and the read record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~79/r22/KIMI_QA_HARNESS.json` (the gate, the parse, the transport, the secret name `astn/kimi/api-key`, never its value).
**THE INTERFACE (fixed here so the three cells build in parallel):** `KimiAdvisory(*, send, telemetry, clock=..., search_capability=None, search=None)` where `search` is a port `search(text_query, limit, timeout_seconds) -> list of {title, url, snippet}` (the transport lives in `ycharts/generate/kimi_port.py`: `kimi_search(read_secret, url=KIMI_SEARCH_URL, opener=...)`, same secret and the same no-secret-in-logs rule as `kimi_send`). `search_capability` for the `swap` kind is a dict `{"model": MODEL, "verified": True, "qa_receipt_sha256": <64 hex>, "search_limit": <int 1..10>}` and nothing else (the old `request_fields`/`tools`/`tool_choice` members are REFUSED). `KimiAdvisory.call("swap", symbol, context_symbols=None, excluded=None, deadline=None)` keeps its return shape `{"result": {... "candidates": [{"symbol","reason","sources"}] ...}, "failure": ..., "attempts": [...]}`: a refused capability or a missing `search` port returns `KIMI_WEB_SEARCH_UNVERIFIED` as today, with no send and no search.

1. **Read first:** the first worker's record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~80/r22/SWAP_SUGGESTIONS.json` (the wire shape and the finding that no mechanism carries a search capability into the resident), `intake/upload_suggestions.py`, `intake/security_resolution.py` :242-250, `ycharts/generate/resident_worker.py` :740-790, `ycharts/generate/resident_session.py`, `ycharts/generate/kimi_port.py`, `ycharts/generate/tests/test_y4_check_gate.py`. Record `where_wired`.
2. **The wiring (gate 2) -- the CTO's default, no other mechanism:** the capability is a JSON file `kimi_search_capability.json` that is a MEMBER of the resident release package, read once at resident start from beside the other package members (find how the resident reads a packaged data file, e.g. the census pin or `firm_registry.json`, and use that way); absent, unreadable or not exactly the capability dict of THE INTERFACE means `None` (so `swap` is refused exactly as today). NO file of that name is shipped by this cell: the receipt does not exist. The resident builds `KimiAdvisory` with `search_capability=<that>` and `search=kimi_port.kimi_search(...)` (the same secret reader as `kimi_send`).
3. **The caller (gate 3).** In `intake/upload_suggestions.py` (a sibling function next to `suggest_for`, or an extension of it): for each `TICKER_NOT_FOUND` row the typo `check` left WITHOUT a verified suggestion, and only when the advisory's capability verifies, ask `advisory("swap", symbol, deadline=...)`, pass its `candidates` (at most 3) through the provider verification the file already uses (exact FOUND, EXACT_PROVIDER_MATCH, no `features_needed`, a provider receipt), and attach the kept ones to the finding as a NEW member `suggestions`: a list of `{symbol, source: "KIMI_SWAP_PROVIDER_VERIFIED", provider_receipt_sha256, reason}` (`reason`: the candidate's own reason, bounded to 200 characters, plain text), at most 3. The existing `suggestion` member and the action `ACCEPT_SUGGESTION` stay exactly as they are for the typo lane; the swap lane adds NO action and NEVER writes a proxy or a substitution. The per-upload Kimi time stays inside `TOTAL_SUGGEST_SECONDS` (240) shared with the check lane. A swap failure, an empty list, an unverified candidate or any refusal leaves the finding as it was.
4. **The tests, before and after.** New file `ycharts/generate/tests/test_swap_suggestions.py` (at least 7 tests; fake ports): (a) no capability: a TICKER_NOT_FOUND row gets no `suggestions` and neither `swap` nor search is ever called (TIMXX's case: still no match); (b) capability verified and the provider verifies two of three candidates: the finding carries exactly those two with source and receipt; (c) a candidate the provider does not FIND exactly is dropped; (d) four candidates are refused and the finding is untouched; (e) the per-upload budget is shared with the check lane; (f) the finding's `actions` and `suggestion` are byte-equal to today's in every case; (g) the capability file loader: absent, malformed, extra keys, the old `request_fields` shape, each give `None`; a good file gives the dict. `before_arm`: (b) FAILS at HEAD. Then `intake/tests` (365 floor), `ycharts/generate/tests/test_y4_check_gate.py` stays green, and the neighbours that collect (known baseline: 4 custody failures, fitz collection errors, row `W79-S4`).
5. **Write `r22/SWAP_SUGGESTIONS_R2.json`:** `where_wired`, `capability_carrier` (the member name, how the resident reads it, what a release pair must add), `behaviour`, `wire_shape` (with a constructed example), `tests`, `before_arm`, `files_changed`, `release_size` (members changed in the resident leg; the Lambda leg is NOT touched if `upload_suggestions.py` is not packaged there: read the map), `claim`, `not_read`.
6. **In your report:** the wire shape in one line, the carrier, the counts, the release size.

### ACCEPTANCE

<criterion id="AR251-y-AC1" cell_refs="AR-y-251"><invocation>python C:/dev/wk-irpt-anlreq-84/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y251-swap --root C:/dev/wk-irpt-anlreq-84</invocation><expect>Y251-SWAP-OK</expect></criterion>
`AR251-y-AC1`: the record names the wiring, the package-member carrier and the wire shape, the new test file passes with at least 7 tests whose case (b) fails at HEAD, and the intake folder passes at 365 or more.

<criterion id="AR251-y-AC2J" cell_refs="AR-y-251" judgment="true"/>
`AR251-y-AC2J` (judgment, graded at L9, never by you): with no capability file the behaviour is byte-identical to today (TIMXX still shows no match), a suggestion is never an action or a substitution, every candidate is provider-verified exactly, the Kimi time stays inside the one per-upload budget, and no capability file or secret was shipped.

<expected_criteria>AR251-y-AC1 AR251-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~84/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
infra/aws/lambda/investor-reporting/intake/upload_suggestions.py
infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py
infra/aws/lambda/investor-reporting/ycharts/generate/resident_session.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_swap_suggestions.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R22C_Y.md</decomp_doc>
<owned_cells>AR-y-251</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~84/IRPT_ANLREQ.TO-AR-y-251.swap-suggestions-wired-and-called-r2.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-251`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR251-y-AC1,AR251-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- source and test edits in a worktree; nothing is released, deployed or called; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the CTO's ruling (a') (msg 7137) and the 10-03 QA findings (Y5P2) against the cell; the lens: a proposal that was never in a search result, a candidate shown without provider verification, a capability flag set without a receipt, a call to the retiring $web_search. The order requires the ticker-in-a-result and cited-url rule, the verification, and no use of the `tools` request field. NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's ruling (a') (msg 7137: the Kimi search endpoint plus ONE plain chat call; ruling B's gates, proof set, one-round box and fallback (b) stand) as workstream `YR` round 21. The grant names every file the cell writes (the first cuts `AR-y-246`/`-247` omitted them: rows `W79-S1`, `W80-S1`). Base: `AR251-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.
