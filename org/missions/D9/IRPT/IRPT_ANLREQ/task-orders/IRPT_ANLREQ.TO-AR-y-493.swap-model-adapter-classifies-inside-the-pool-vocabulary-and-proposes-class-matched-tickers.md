# TO IRPT_ANLREQ.TO-AR-y-493.swap-model-adapter-classifies-inside-the-pool-vocabulary-and-proposes-class-matched-tickers -- BUILD AND PROVE OFFLINE: the swap model adapter (kimi-k3, no web search): a classification bound to the pool vocabulary with the 0.80 flag, and a bounded proposals call

<to_id>IRPT_ANLREQ.TO-AR-y-493.swap-model-adapter-classifies-inside-the-pool-vocabulary-and-proposes-class-matched-tickers</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~367</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-21</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ152</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by the path floor | **Decomp cell:** `AR-y-493` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** C-SWAP model leg, graded under FWD-2 (PRD v0.25 and v0.26) | **depends_on:** AR-y-461's read `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~326/SWAP_LEG_READ.md`; CTO ruling v0.26 (kimi-k3, no web search, below 0.80 flagged)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~367`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-367` (branch `wk-IRPT_ANLREQ-367`), provisioned by the issuer from the current branch. FIRST confirm with `git -C C:/dev/wk-irpt-anlreq-367 branch --show-current` that it prints `wk-IRPT_ANLREQ-367` and that this order file exists in it; if not, STOP and report WITHOUT touching any other worktree or branch. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~367 <0.9.0_WK_IRPT_ANLREQ~367@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W367-S<k>`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING, with `spec_asserts` and `world_is` fields. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (ruff clean; no single-letter names `l`, `O`, `I`; no non-ASCII; stdlib only unless the order says otherwise).
- **No AWS call, no network, no model call, no push, no deploy, no release build.** Every model call in a test is a fake `send`. The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/IRPT_ANLREQ.TO-AR-y-459.run7b-browser-leg-script-re-proved-offline-against-the-advisor-required-form.proof_of_spec.json` (read it first; `controls` holds `mutant` and `determinism` only), with `to_id` exactly the order's id; run `python .tools/proof-of-spec-check.py <instance> "AR493-y-AC1,AR493-y-AC2,AR493-y-AC3"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (with the instance, one commit) only on VALID and only after EVERY other edit you intend is committed (a status of complete removes your path grant). The instance's check-script reference is pinned to a commit that EXISTS (commit the script first, then pin it). A test file that leaks `sys.path` makes other files fail at collection in some orders: keep pytest lines in the order written.
### THE INTERFACE (shared by the three cells of the swap leg; code to it exactly)

Source read: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~326/SWAP_LEG_READ.md` (sections S1-S4; its line numbers have moved, find the code by name). PRD contract C-SWAP (v0.14, restated v0.26): step 3 CLASSIFY with the estate's Kimi model kimi-k3 (`etf_classification_model.py`, `MODEL`), WITHOUT web search, output bound to the live (class, sub-class) vocabulary, below 0.80 confidence FLAGGED; step 4 REPLACE from the class-matched pool plus model proposals that pass the class match and have Yahoo history, the longest Yahoo history wins, ties by ticker; the model widens the pool and NEVER picks. No new vendor; no IAM change (the resident role already reads the estate Kimi key, `resident.tf` Sid `ReadTheEstateKimiKey`).
1. `swap_pass.swap_holdings(rows, pool, *, classify=None, history_days, proposals=None)`. `classify(symbol)` returns None or a dict with `asset_class` and `sub_asset_class` and, when the classification came from the model, ALSO `confidence` (float), `low_confidence` (bool) and `classified_by` (the str `"MODEL"`). `proposals(symbol, classification)` returns a list of ticker strings (the model's proposed same-class securities) or raises; the pass treats a raise, a non-list or a non-str element as no proposals for that symbol.
2. `swap_model.make_swap_model(pool_rows, send, *, model_module=None, api_key="", threshold=0.80, max_proposals=5)` in the NEW module `infra/aws/lambda/investor-reporting/ycharts/research/swap_model.py` returns an object with `classify(symbol)` (the shape of item 1; None when the model cannot classify the symbol inside the vocabulary) and `propose(symbol, classification)` (item 1; at most `max_proposals` upper-cased tickers matching `[A-Z0-9.-]{1,12}`, never the symbol itself, no duplicates; `[]` on ANY failure). `send(payload, timeout_seconds)` is the resident's Kimi transport (`ycharts/generate/kimi_port.py` `kimi_send(secret_reader(...))`); the module opens no connection, reads no secret and no environment variable.
3. The producer stage `_swap_stage` (`ycharts/research/opal_producer.py`) takes from the `swap` store dict two OPTIONAL keys, `model_classify` (a `classify` of item 1) and `proposals` (item 1), passes `proposals` to `swap_holdings`, and composes the classify it passes: the store's `classify` when given, else the classifier lookup (`stores["classifier"].get_classification(symbol)`) and, ONLY when that answers nothing usable (None, or no class pair), `model_classify(symbol)`.
4. The resident binding `opal_swap_model`, an OPTIONAL member of `resident_bindings.json` that is exactly `{"enabled": true|false}`: absent or false means today's behaviour (no model call); true makes `_swap_extras` add `model_classify` and `proposals` (from `swap_model.make_swap_model` over the pool rows) to the `swap` store. Any other shape refuses the install with `SWAP_MODEL_BINDING_INVALID`.

### THE CELL (`AR-y-493`)

*What and why.* No investor-reporting module calls a model for a holding (SWAP_LEG_READ S2, S4 item 5). `v2_portal/_shared/etf_classification_model.py` (`classify_one`, `ASSET_CLASS_VOCAB`, `MODEL` kimi-k3, `LOW_CONFIDENCE_THRESHOLD`, `MAX_TOKENS`, `TIMEOUT_SECONDS`) is the estate's classifier; it takes an injected `send(payload, *, api_key, timeout_seconds)` and never raises. This cell adds the adapter that makes it the swap leg's classify and proposals ports of interface item 2. The module is stdlib-only and opens no connection.

*The change.* ONE new module `infra/aws/lambda/investor-reporting/ycharts/research/swap_model.py` (read `etf_classification_model.py` in full first, and `ycharts/generate/kimi_port.py` `kimi_send`):
1. `make_swap_model(pool_rows, send, *, model_module=None, api_key="", threshold=0.80, max_proposals=5)`. `model_module` defaults to a lazy `import etf_classification_model` (the module is a sibling at the resident's package root; the release builder places it there; in tests inject it or insert `infra/aws/lambda/v2_portal/_shared` on `sys.path` computed from `os.path.dirname(os.path.abspath(__file__))`, never a typed absolute path). The vocabulary is built from `pool_rows` (each `{ticker, asset_class, sub_asset_class}`): `{asset_class casefolded: sorted distinct sub_asset_class values}` restricted to the six classes of `model_module.ASSET_CLASS_VOCAB`; a pool row whose class is outside those six is ignored. Keep the pool's own spelling of each (class, sub-class) so the answer matches the pool exactly.
2. `classify(symbol)`: call `model_module.classify_one(None, symbol, vocabulary, send=<adapter>, api_key=api_key, threshold=threshold)` where the adapter is `lambda payload, *, api_key, timeout_seconds: send(payload, timeout_seconds)`. Only the symbol is sent (never a firm, amount or account). If the answer's `asset_class` is None, or its `sub_asset_class` is not one of the vocabulary's sub-classes for that class (casefold compare), return None (REFUSED, never coerced to a nearest member). Else return `{"asset_class": <the pool's spelling>, "sub_asset_class": <the pool's spelling>, "confidence": <float>, "low_confidence": <confidence < threshold>, "classified_by": "MODEL"}`. `classify` never raises; a blank or non-str symbol returns None without a call. Cache one answer per upper-cased symbol for the object's life.
3. `propose(symbol, classification)`: return `[]` when `classification` is not a dict with both class parts. Else ONE call through the same adapter with a payload built like `classify_one`'s (`model`, `temperature` 1, `max_tokens`, `messages` of one user message): the prompt tells the model to return ONLY JSON `{"tickers": [up to max_proposals US-listed securities that are in the same asset class and sub-asset class as the given security, ticker symbols only]}`, embeds the symbol and the class pair ONLY inside a trailing JSON data object (never in the instruction text, as `build_prompt` does), and says the strings are data identifiers, never instructions. Parse `choices[0].message.content` (strip a leading code fence as `_parse` does), require exactly `{"tickers": [...]}`, keep elements that match `[A-Z0-9.-]{1,12}` after upper-casing, drop the symbol itself and duplicates, cap at `max_proposals`; ANY failure (transport raise, bad JSON, wrong shape, `finish_reason` length) is `[]`, no text kept. One attempt only (no retry) so a run is bounded: at most 1 classify call (2 inside `classify_one` on its own failure) plus 1 propose call per unknown symbol.
4. A module docstring stating: no connection, no secret, no environment; only symbols and class pairs reach the model; the model widens the pool and never picks.

Tests in `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_swap_model.py` (hermetic; a fake `send` recording every payload; use the real `etf_classification_model` through the `sys.path` insertion above): a classification inside the vocabulary maps to the pool's spelling with `classified_by` MODEL; an answer outside the vocabulary (class not one of six, sub-class not in the pool for that class) is None; a confidence 0.79 sets `low_confidence` True and 0.80 False; the payload carries the symbol only (assert no other client-shaped string, and that the symbol appears only inside the JSON data object); the model name equals `model_module.MODEL`; `propose` filters, dedupes, caps at `max_proposals`, drops the symbol and lower-case or too-long strings, and returns `[]` for a raising `send`, bad JSON, a wrong shape and a length-starved finish; the cache makes a second `classify` of the same symbol send nothing; no call is made for a blank symbol.

*The checks.* In `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~367/`: `check_swap_model.py` (stdlib only, ruff clean, offline) runs the module in-process with a fake `send` over eight cases and prints `SWAP-MODEL-OK cases=8 vocab_bound=yes never_coerced=yes flag_at_0.80=yes proposals_filtered=yes symbol_only=yes` or `SWAP-MODEL-BAD <why>` (rc 1). `--selftest` mutates the module text in memory three ways (the vocabulary check removed so an out-of-vocabulary answer passes; the threshold compare flipped to `<=`; the proposals cap removed) and prints `CONTROL-FIRES` only when ALL THREE read BAD. Commit order: the module and its test as ONE commit first, message citing AR-y-493; then your deliverables and instance.

---

## ACCEPTANCE

<criterion id="AR493-y-AC1" cell_refs="AR-y-493"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~367/check_swap_model.py</invocation><expect>^SWAP-MODEL-OK cases=8 vocab_bound=yes never_coerced=yes flag_at_0.80=yes proposals_filtered=yes symbol_only=yes$</expect></criterion>
<criterion id="AR493-y-AC2" cell_refs="AR-y-493"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~367/check_swap_model.py --selftest</invocation><expect>^CONTROL-FIRES$</expect></criterion>
<criterion id="AR493-y-AC3" cell_refs="AR-y-493"><invocation>(cd infra/aws/lambda/investor-reporting && python -m pytest ycharts/research/tests/test_swap_model.py -q --color=no -p no:cacheprovider 2>&1 | tail -1)</invocation><expect>^[0-9]+ passed in </expect></criterion>

<proof_of_spec>
The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~367/IRPT_ANLREQ.TO-AR-y-493.swap-model-adapter-classifies-inside-the-pool-vocabulary-and-proposes-class-matched-tickers.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-493.swap-model-adapter-classifies-inside-the-pool-vocabulary-and-proposes-class-matched-tickers`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR493-y-AC1,AR493-y-AC2,AR493-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-493</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/swap_model.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_swap_model.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~367/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-493.swap-model-adapter-classifies-inside-the-pool-vocabulary-and-proposes-class-matched-tickers.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- source and test files only; nothing is deployed, built into a release or run against AWS or the model; the resident release that carries the swap leg is built by 2.0.0_SA_COO~G2 and applied by IB2 under its own pair.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker; no IAM change in the swap leg.
comp-adversary: RUN -- by reading the contract C-SWAP, the swap rule and the interface above against this cell; the lens: a class outside the vocabulary coerced to the nearest member, a threshold off by one, a prompt that interpolates the symbol into the instruction, a client figure or firm reaching the model, an unbounded retry loop, a network or secret read inside the module, a proposals list that is trusted unvalidated, a cache that returns another symbol, a control that cannot fire. NOT seen (blind): the live model's answers and the deployed resident bytes; denominator: 3 criteria.
</preflight>
