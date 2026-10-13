# TO IRPT_ANLREQ.TO-AR-y-246.kimi-search-qa-receipt-harness -- the provider QA receipt for the Kimi web-search capability -- the harness, built and tested offline

<to_id>IRPT_ANLREQ.TO-AR-y-246</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~79</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>20</round>
<workstream>YR</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD
**Decomp cell:** `AR-y-246` (`decompositions/IRPT_ANLREQ_DECOMP_R22B_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~79`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-79` (branch `wk-IRPT_ANLREQ-79`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~79 <0.9.0_WK_IRPT_ANLREQ~79@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W79-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-246`, inlined) -- GATE (1) OF RULING B: THE QA RECEIPT. A harness and a record shape, tested offline. NO LIVE CALL.

*The CTO ruled B (msg 7112): the Kimi swap advisory ('swap': up to three similar-exposure ETFs, web search, each provider-verified) is already built and is refused until its gates read met, in this order: (1) a provider QA receipt, (2) `search_capability` wired, (3) the composer as caller. `KimiAdvisory.call` for kind `swap` returns `KIMI_WEB_SEARCH_UNVERIFIED` unless `search_capability` is a dict with `model == MODEL`, `verified is True`, a `qa_receipt_sha256`, and a non-empty `request_fields` whose keys are only `tools` and `tool_choice` (`intake/resolution_kimi.py` :159-166; tests `intake/tests/test_resolution_kimi.py` :82, :96). Nothing in the estate produces such a receipt (the read record `0.9.0_WK_IRPT_ANLREQ~76/r22/PROXY_SUGGESTION_READ.json`, option B).*

1. **Read what the gate needs and what the transport is.** `intake/resolution_kimi.py` (the whole gate, `MODEL`, `prompt_for`, `_parse` for `swap`, and what `swap` parses into: `identified_asset`, attributes, `sources`, `candidates`), the transport `ycharts/generate/kimi_port.py` (`kimi_send`, the secret by id, the journal telemetry), and the call site `ycharts/generate/resident_worker.py` :755-770 and `resident_session.py` (where `KimiAdvisory` is built and what it passes). Record `gate` {`capability_shape`, `model`, `what_swap_parses`, `transport`, `secret_id_name_only`} (NO key, token or secret value anywhere).
2. **The QA harness.** Write ONE new python file `infra/aws/lambda/investor-reporting/ycharts/generate/kimi_search_qa.py` (ASCII, no network client of its own: it takes the same `send` port `KimiAdvisory` takes) that: takes a candidate `request_fields` (`tools`, `tool_choice` only) and a fixed list of QA cases (at least 6: symbols a web search should identify, including `TIMXX`; a nonsense symbol that must return an empty `candidates`; two prompt-injection strings in the symbol position that must not change the output shape; an ETF that exists), runs each case through `KimiAdvisory(send=<that port>, telemetry=<a recording stub>, search_capability=<the candidate, with `verified` set True ONLY inside this QA run: the real gate refuses an unverified capability, so the QA is how the flag is earned -- say so plainly in a comment and in the record>).call("swap", ...)`; grades each answer for SHAPE only (the JSON keys parse, `candidates` is an array of at most three `{symbol, reason, sources}`, `sources` are HTTPS URLs, unknown attributes are null, an empty answer is an empty array) and never for investment judgment; and writes a QA record (a JSON object: `model`, `request_fields`, the case list with each case's shape verdict and the answer's sha256, `started_at`, `all_shape_ok`, the harness file's own sha256) and returns `qa_receipt_sha256` = the sha256 of that record's canonical JSON (sorted keys). A candidate that fails any case yields NO receipt.
3. **Test it offline, with a fake `send`.** New test file `ycharts/generate/tests/test_kimi_search_qa.py` (at least 5 tests): a fake `send` that answers well produces a receipt equal to the sha256 of the canonical record; a fake that returns a malformed or over-long answer, a candidate list of four, a non-HTTPS source, or an answer that obeys an injection string produces NO receipt; `request_fields` with a key other than `tools`/`tool_choice` is refused before any send; the receipt changes if one case's answer changes; running the harness twice with the same fake gives the same receipt. `before_arm`: the tests cannot run before the file exists (record that). Then the folders: `ycharts/generate/tests` (counts; `pytest cannot collect (fitz missing)` is a known pre-existing limit from the release-20 records: run only your file and the neighbours that collect, and say which) and `intake/tests` (365 floor).
4. **The live QA, designed not run.** Write `live_qa` in the record: the exact command a Dell CloudOps lane would run (the harness with the real `kimi_send` and the secret read by id), what the Kimi provider's web-search request fields are (read the provider's documented `tools`/`tool_choice` shape from the estate if it holds it, e.g. other Kimi callers, `docs/`; if the estate holds none, say `NOT READ` and list what the live order must look up -- do NOT guess a tool name), the cost bound (cases times attempts times the `swap` budget in `BUDGETS`), what is sent (symbols only, no client data), and where the receipt and the QA record would be stored so that step (2) can read them (a repo file for the record is enough; the receipt value goes into the capability the resident reads).
5. **Write `r22/KIMI_QA_HARNESS.json`:** `gate`, `harness` {`path`, `sha256`, `cases`}, `tests` {`added`, `passed`, `failed`, `folders`}, `live_qa`, `claim`, `not_read`.
6. **In your report:** the capability shape, the cases, the tests, and what the live QA still needs.

### ACCEPTANCE

<criterion id="AR246-y-AC1" cell_refs="AR-y-246"><invocation>python C:/dev/wk-irpt-anlreq-79/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y246-qa --root C:/dev/wk-irpt-anlreq-79</invocation><expect>Y246-QA-OK</expect></criterion>
`AR246-y-AC1`: the record names the gate's shape, the harness file with its sha256, at least 6 cases, passing offline tests that include the no-receipt cases, and a live QA design.

<criterion id="AR246-y-AC2J" cell_refs="AR-y-246" judgment="true"/>
`AR246-y-AC2J` (judgment, graded at L9, never by you): no live call was made; the harness cannot mint a receipt for a malformed, over-long, non-HTTPS or injected answer; the flag `verified: True` is set only inside the QA run and said so; no key or secret value appears anywhere.

<expected_criteria>AR246-y-AC1 AR246-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~79/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R22B_Y.md</decomp_doc>
<owned_cells>AR-y-246</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~79/IRPT_ANLREQ.TO-AR-y-246.kimi-search-qa-receipt-harness.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-246`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR246-y-AC1,AR246-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- new source and test files in a worktree; nothing is called, released or applied; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the CTO's ruling B (msg 7112) and the read record `0.9.0_WK_IRPT_ANLREQ~76/r22/PROXY_SUGGESTION_READ.json` against the cell; the lens: a suggestion that fills a box or a request on its own, a candidate shown without its provider verification, a gate that is skipped because the next one is built. The order requires the user to pick, the gates in their order, and the no-suggestion case to show nothing. NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's ruling B (msg 7112: the Kimi swap advisory, behind its own three gates; a suggestion never fills the box) as workstream `YR` round 20. Base: `AR246-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.
