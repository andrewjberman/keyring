# TO IRPT_ANLREQ.TO-AR-y-494.producer-and-resident-wire-the-swap-model-ports-behind-the-opal-swap-model-binding -- BUILD AND PROVE OFFLINE: the producer composes the swap classify and passes the proposals; the resident builds the swap model ports behind the optional binding opal_swap_model; the bindings builder ships it ON

<to_id>IRPT_ANLREQ.TO-AR-y-494.producer-and-resident-wire-the-swap-model-ports-behind-the-opal-swap-model-binding</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~368</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-21</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ153</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by the path floor | **Decomp cell:** `AR-y-494` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** C-SWAP model leg, graded under FWD-2 (PRD v0.25 and v0.26) | **depends_on:** AR-y-461's read `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~326/SWAP_LEG_READ.md`; CTO ruling v0.26 (kimi-k3, no web search, below 0.80 flagged)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~368`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-368` (branch `wk-IRPT_ANLREQ-368`), provisioned by the issuer from the current branch. FIRST confirm with `git -C C:/dev/wk-irpt-anlreq-368 branch --show-current` that it prints `wk-IRPT_ANLREQ-368` and that this order file exists in it; if not, STOP and report WITHOUT touching any other worktree or branch. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~368 <0.9.0_WK_IRPT_ANLREQ~368@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W368-S<k>`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING, with `spec_asserts` and `world_is` fields. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (ruff clean; no single-letter names `l`, `O`, `I`; no non-ASCII; stdlib only unless the order says otherwise).
- **No AWS call, no network, no model call, no push, no deploy, no release build.** Every model call in a test is a fake `send`. The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/IRPT_ANLREQ.TO-AR-y-459.run7b-browser-leg-script-re-proved-offline-against-the-advisor-required-form.proof_of_spec.json` (read it first; `controls` holds `mutant` and `determinism` only), with `to_id` exactly the order's id; run `python .tools/proof-of-spec-check.py <instance> "AR494-y-AC1,AR494-y-AC2,AR494-y-AC3"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (with the instance, one commit) only on VALID and only after EVERY other edit you intend is committed (a status of complete removes your path grant). The instance's check-script reference is pinned to a commit that EXISTS (commit the script first, then pin it). A test file that leaks `sys.path` makes other files fail at collection in some orders: keep pytest lines in the order written.
### THE INTERFACE (shared by the three cells of the swap leg; code to it exactly)

Source read: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~326/SWAP_LEG_READ.md` (sections S1-S4; its line numbers have moved, find the code by name). PRD contract C-SWAP (v0.14, restated v0.26): step 3 CLASSIFY with the estate's Kimi model kimi-k3 (`etf_classification_model.py`, `MODEL`), WITHOUT web search, output bound to the live (class, sub-class) vocabulary, below 0.80 confidence FLAGGED; step 4 REPLACE from the class-matched pool plus model proposals that pass the class match and have Yahoo history, the longest Yahoo history wins, ties by ticker; the model widens the pool and NEVER picks. No new vendor; no IAM change (the resident role already reads the estate Kimi key, `resident.tf` Sid `ReadTheEstateKimiKey`).
1. `swap_pass.swap_holdings(rows, pool, *, classify=None, history_days, proposals=None)`. `classify(symbol)` returns None or a dict with `asset_class` and `sub_asset_class` and, when the classification came from the model, ALSO `confidence` (float), `low_confidence` (bool) and `classified_by` (the str `"MODEL"`). `proposals(symbol, classification)` returns a list of ticker strings (the model's proposed same-class securities) or raises; the pass treats a raise, a non-list or a non-str element as no proposals for that symbol.
2. `swap_model.make_swap_model(pool_rows, send, *, model_module=None, api_key="", threshold=0.80, max_proposals=5)` in the NEW module `infra/aws/lambda/investor-reporting/ycharts/research/swap_model.py` returns an object with `classify(symbol)` (the shape of item 1; None when the model cannot classify the symbol inside the vocabulary) and `propose(symbol, classification)` (item 1; at most `max_proposals` upper-cased tickers matching `[A-Z0-9.-]{1,12}`, never the symbol itself, no duplicates; `[]` on ANY failure). `send(payload, timeout_seconds)` is the resident's Kimi transport (`ycharts/generate/kimi_port.py` `kimi_send(secret_reader(...))`); the module opens no connection, reads no secret and no environment variable.
3. The producer stage `_swap_stage` (`ycharts/research/opal_producer.py`) takes from the `swap` store dict two OPTIONAL keys, `model_classify` (a `classify` of item 1) and `proposals` (item 1), passes `proposals` to `swap_holdings`, and composes the classify it passes: the store's `classify` when given, else the classifier lookup (`stores["classifier"].get_classification(symbol)`) and, ONLY when that answers nothing usable (None, or no class pair), `model_classify(symbol)`.
4. The resident binding `opal_swap_model`, an OPTIONAL member of `resident_bindings.json` that is exactly `{"enabled": true|false}`: absent or false means today's behaviour (no model call); true makes `_swap_extras` add `model_classify` and `proposals` (from `swap_model.make_swap_model` over the pool rows) to the `swap` store. Any other shape refuses the install with `SWAP_MODEL_BINDING_INVALID`.

### THE CELL (`AR-y-494`)

*What and why.* Cells AR-y-492 (swap pass ports; drained) and AR-y-493 (the model adapter `ycharts/research/swap_model.py`; drained) are built and proved offline; nothing yet hands them to the producer or the resident. This cell wires them, behind an OPTIONAL binding that ships ON in the bindings builder, using interface items 3 and 4. No model call is made by this cell: tests inject fakes.

*The change.* Read first, in full: `infra/aws/lambda/investor-reporting/ycharts/research/swap_pass.py` (the new `proposals` port), `infra/aws/lambda/investor-reporting/ycharts/research/swap_model.py` (`make_swap_model`), `infra/aws/lambda/investor-reporting/ycharts/research/opal_producer.py` (`_swap_stage` and where it is called), `infra/aws/lambda/investor-reporting/reports/resident_installed.py` (`_swap_extras`, `OPAL_SWAP_POOL_BINDING`, the binding validation block for `opal_swap_pool`, `build_resident_runtime` where `swap_extras=` is passed, and `make_opal_stores` where the extras are merged), and `infra/aws/lambda/investor-reporting/reports/build_resident_package.py` (the `bindings` dict). Then:
1. `opal_producer._swap_stage(holdings, swap, stores)`: read `proposals = swap.get("proposals")` and `model_classify = swap.get("model_classify")` (each must be None or callable, else `ProducerRefused("store required: swap")`). Compose the `classify` it passes to `swap_pass.swap_holdings`: the store's `classify` when given; otherwise `lookup(symbol)` = `stores["classifier"].get_classification(symbol)` as today, and, ONLY when `model_classify` is set and `lookup` answered None or a dict lacking a non-blank `asset_class` or `sub_asset_class`, `model_classify(symbol)` (a raise from `lookup` is treated as no answer, not propagated; a raise from `model_classify` is no answer). Pass `proposals=proposals` to `swap_holdings`. With neither key present the behaviour is exactly today's.
2. `resident_installed.py`: a constant `OPAL_SWAP_MODEL_BINDING = "opal_swap_model"`; in the install validation, when the document carries it, it must be a dict equal to exactly `{"enabled": <bool>}` (a `bool`, not an int), else `ResidentInstallRefused("SWAP_MODEL_BINDING_INVALID")`; absent is valid. `_swap_extras(bindings, base, clock, secrets_client=None)`: when the swap-pool binding is present AND `bindings.get(OPAL_SWAP_MODEL_BINDING) == {"enabled": True}`, the `extras()` dict's `swap` value gains `model_classify` and `proposals`, built from `swap_model.make_swap_model(pool["rows"], send)` where `send` is `kimi_port.kimi_send(kimi_port.secret_reader(secrets_client))` (read `ycharts/session/resident_session.py` lines ~130-140 for the exact existing usage and copy its imports and shape; the import of `swap_model`, `kimi_port` happens inside `extras()` so install never imports them); if `secrets_client` is None while enabled, raise `ResidentInstallRefused("SWAP_MODEL_SECRETS_CLIENT_REQUIRED")` at install, not at job time. `build_resident_runtime` passes `clients["secretsmanager"]` as `secrets_client`. With the model binding absent or `enabled` false the `swap` dict is exactly today's.
3. `build_resident_package.py`: add `"opal_swap_model": {"enabled": True},` to the `bindings` dict (next to `opal_pricing`; one line, with a comment line naming the cell and that false switches it off). Nothing else changes in that file. Do NOT change the file list or package members: the release builder (2.0.0_SA_COO~G2) packages `swap_model.py` and `etf_classification_model.py`; say so in your report.
4. Tests: new `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer_swap_model.py` (hermetic; the style of `test_opal_producer_swap.py`; fakes for the classifier, `model_classify` and `proposals`): lookup answers -> `model_classify` not called; lookup answers None -> `model_classify` called once and its class used; lookup raises -> `model_classify` used; no ports -> today's behaviour; a proposal from `proposals` reaches the replacement choice and a proposal with a wrong class does not win; a non-callable `proposals` refuses. New `infra/aws/lambda/investor-reporting/reports/tests/test_resident_swap_model_binding.py` (the style of `reports/tests/test_resident_tickets_binding.py` and the swap-pool tests): `{"enabled": true}`, `{"enabled": false}`, absent are valid; `{}`, `{"enabled": 1}`, `{"enabled": true, "x": 1}`, `true` refuse with `SWAP_MODEL_BINDING_INVALID`; enabled + pool binding + a fake secrets client -> the `swap` dict has `model_classify` and `proposals` callables and they call the injected fake `send` only (no network: assert the fake recorded the payload and no socket was opened, by stubbing `kimi_port.kimi_send` to a recorder); enabled without a secrets client refuses at install; disabled -> the dict has neither key. Existing tests are not edited or skipped; `test_opal_producer_swap.py`, `test_resident_installed.py` and `test_resident_tickets_binding.py` still pass.

*The checks.* In `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~368/`: `check_swap_wiring.py` (stdlib only, ruff clean, offline). It reads the three source files as TEXT and prints `SWAP-WIRING-OK producer_composes=yes proposals_passed=yes binding_validated=yes secrets_client_wired=yes builder_binding=ON` or `SWAP-WIRING-BAD <why>` (rc 1): the producer text contains the composition (model_classify consulted only after the lookup) and passes `proposals=`; `resident_installed.py` contains `OPAL_SWAP_MODEL_BINDING`, the refusal text `SWAP_MODEL_BINDING_INVALID` and `SWAP_MODEL_SECRETS_CLIENT_REQUIRED`, and passes `clients["secretsmanager"]`; the builder text carries `"opal_swap_model": {"enabled": True}`. `--selftest` mutates the texts in memory three ways (the producer's `proposals=` removed; the refusal text removed; the builder's `True` set to `False`) and prints `CONTROL-FIRES` only when ALL THREE read BAD. Commit order: the code and test edits as ONE commit first, message citing AR-y-494; then your deliverables and instance.

---

## ACCEPTANCE

<criterion id="AR494-y-AC1" cell_refs="AR-y-494"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~368/check_swap_wiring.py</invocation><expect>^SWAP-WIRING-OK producer_composes=yes proposals_passed=yes binding_validated=yes secrets_client_wired=yes builder_binding=ON$</expect></criterion>
<criterion id="AR494-y-AC2" cell_refs="AR-y-494"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~368/check_swap_wiring.py --selftest</invocation><expect>^CONTROL-FIRES$</expect></criterion>
<criterion id="AR494-y-AC3" cell_refs="AR-y-494"><invocation>(cd infra/aws/lambda/investor-reporting && python -m pytest ycharts/research/tests/test_opal_producer_swap_model.py reports/tests/test_resident_swap_model_binding.py ycharts/research/tests/test_opal_producer_swap.py reports/tests/test_resident_installed.py reports/tests/test_resident_tickets_binding.py -q --color=no -p no:cacheprovider 2>&1 | tail -1)</invocation><expect>^[0-9]+ passed in </expect></criterion>

<proof_of_spec>
The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~368/IRPT_ANLREQ.TO-AR-y-494.producer-and-resident-wire-the-swap-model-ports-behind-the-opal-swap-model-binding.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-494.producer-and-resident-wire-the-swap-model-ports-behind-the-opal-swap-model-binding`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR494-y-AC1,AR494-y-AC2,AR494-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-494</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/opal_producer.py
infra/aws/lambda/investor-reporting/reports/resident_installed.py
infra/aws/lambda/investor-reporting/reports/build_resident_package.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer_swap_model.py
infra/aws/lambda/investor-reporting/reports/tests/test_resident_swap_model_binding.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~368/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-494.producer-and-resident-wire-the-swap-model-ports-behind-the-opal-swap-model-binding.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- source and test files only; nothing is deployed, built into a release or run against AWS or the model; the resident release that carries the swap leg is built by 2.0.0_SA_COO~G2 and applied by IB2 under its own pair.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker; no IAM change in the swap leg.
comp-adversary: RUN -- by reading the contract C-SWAP, the swap rule and the interface above against this cell; the lens: the model consulted when the classifier lookup already answered, a raise from the model or the lookup killing the run, a binding of the wrong shape accepted, the model ports built at install (a network or secret read at install), the secrets client missing and found only at job time, the builder shipping OFF or a different shape, an existing test edited, a control that cannot fire. NOT seen (blind): the live model's answers and the deployed resident bytes; denominator: 3 criteria.
</preflight>
