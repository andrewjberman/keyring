# TO IRPT_ANLREQ.TO-AR-y-492.swap-pass-takes-the-model-proposals-and-classification-ports-and-carries-the-low-confidence-flag -- BUILD AND PROVE OFFLINE: the swap pass takes the proposals port and the classification extras and carries the 0.80 flag into the swap record

<to_id>IRPT_ANLREQ.TO-AR-y-492.swap-pass-takes-the-model-proposals-and-classification-ports-and-carries-the-low-confidence-flag</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~366</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-21</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ151</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by the path floor | **Decomp cell:** `AR-y-492` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** C-SWAP model leg, graded under FWD-2 (PRD v0.25 and v0.26) | **depends_on:** AR-y-461's read `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~326/SWAP_LEG_READ.md`; CTO ruling v0.26 (kimi-k3, no web search, below 0.80 flagged)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~366`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-366` (branch `wk-IRPT_ANLREQ-366`), provisioned by the issuer from the current branch. FIRST confirm with `git -C C:/dev/wk-irpt-anlreq-366 branch --show-current` that it prints `wk-IRPT_ANLREQ-366` and that this order file exists in it; if not, STOP and report WITHOUT touching any other worktree or branch. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~366 <0.9.0_WK_IRPT_ANLREQ~366@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W366-S<k>`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING, with `spec_asserts` and `world_is` fields. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (ruff clean; no single-letter names `l`, `O`, `I`; no non-ASCII; stdlib only unless the order says otherwise).
- **No AWS call, no network, no model call, no push, no deploy, no release build.** Every model call in a test is a fake `send`. The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/IRPT_ANLREQ.TO-AR-y-459.run7b-browser-leg-script-re-proved-offline-against-the-advisor-required-form.proof_of_spec.json` (read it first; `controls` holds `mutant` and `determinism` only), with `to_id` exactly the order's id; run `python .tools/proof-of-spec-check.py <instance> "AR492-y-AC1,AR492-y-AC2,AR492-y-AC3"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (with the instance, one commit) only on VALID and only after EVERY other edit you intend is committed (a status of complete removes your path grant). The instance's check-script reference is pinned to a commit that EXISTS (commit the script first, then pin it). A test file that leaks `sys.path` makes other files fail at collection in some orders: keep pytest lines in the order written.
### THE INTERFACE (shared by the three cells of the swap leg; code to it exactly)

Source read: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~326/SWAP_LEG_READ.md` (sections S1-S4; its line numbers have moved, find the code by name). PRD contract C-SWAP (v0.14, restated v0.26): step 3 CLASSIFY with the estate's Kimi model kimi-k3 (`etf_classification_model.py`, `MODEL`), WITHOUT web search, output bound to the live (class, sub-class) vocabulary, below 0.80 confidence FLAGGED; step 4 REPLACE from the class-matched pool plus model proposals that pass the class match and have Yahoo history, the longest Yahoo history wins, ties by ticker; the model widens the pool and NEVER picks. No new vendor; no IAM change (the resident role already reads the estate Kimi key, `resident.tf` Sid `ReadTheEstateKimiKey`).
1. `swap_pass.swap_holdings(rows, pool, *, classify=None, history_days, proposals=None)`. `classify(symbol)` returns None or a dict with `asset_class` and `sub_asset_class` and, when the classification came from the model, ALSO `confidence` (float), `low_confidence` (bool) and `classified_by` (the str `"MODEL"`). `proposals(symbol, classification)` returns a list of ticker strings (the model's proposed same-class securities) or raises; the pass treats a raise, a non-list or a non-str element as no proposals for that symbol.
2. `swap_model.make_swap_model(pool_rows, send, *, model_module=None, api_key="", threshold=0.80, max_proposals=5)` in the NEW module `infra/aws/lambda/investor-reporting/ycharts/research/swap_model.py` returns an object with `classify(symbol)` (the shape of item 1; None when the model cannot classify the symbol inside the vocabulary) and `propose(symbol, classification)` (item 1; at most `max_proposals` upper-cased tickers matching `[A-Z0-9.-]{1,12}`, never the symbol itself, no duplicates; `[]` on ANY failure). `send(payload, timeout_seconds)` is the resident's Kimi transport (`ycharts/generate/kimi_port.py` `kimi_send(secret_reader(...))`); the module opens no connection, reads no secret and no environment variable.
3. The producer stage `_swap_stage` (`ycharts/research/opal_producer.py`) takes from the `swap` store dict two OPTIONAL keys, `model_classify` (a `classify` of item 1) and `proposals` (item 1), passes `proposals` to `swap_holdings`, and composes the classify it passes: the store's `classify` when given, else the classifier lookup (`stores["classifier"].get_classification(symbol)`) and, ONLY when that answers nothing usable (None, or no class pair), `model_classify(symbol)`.
4. The resident binding `opal_swap_model`, an OPTIONAL member of `resident_bindings.json` that is exactly `{"enabled": true|false}`: absent or false means today's behaviour (no model call); true makes `_swap_extras` add `model_classify` and `proposals` (from `swap_model.make_swap_model` over the pool rows) to the `swap` store. Any other shape refuses the install with `SWAP_MODEL_BINDING_INVALID`.

### THE CELL (`AR-y-492`)

*What and why.* `swap_pass.swap_holdings` passes the literal `[]` as the model proposals to `swap_replacement.choose_replacement` and never forwards its `classify` there, and its record writes the literal `low_confidence: False` (SWAP_LEG_READ S1, S4 items 1 and 2). This cell makes the pass take the two ports of interface items 1 and uses them; it adds no model call (the ports are injected).

*The change.* In `infra/aws/lambda/investor-reporting/ycharts/research/swap_pass.py` only (read it and `swap_replacement.py` in full first; do NOT edit `swap_replacement.py`):
1. `swap_holdings(rows, pool, *, classify=None, history_days, proposals=None)`. Per UNRESOLVED row, after the classification is known and ONLY when it is not None, call `proposals(symbol, classification)` if `proposals` is callable inside try/except Exception; accept only a list, keep only the elements that are non-blank `str`, cap the list at 20; anything else is `[]`. Call `sr.choose_replacement(symbol, classification, pool_rows, <that list>, history_days, classify=<the pass's own classify wrapper below>)`. When `proposals` is None the list is `[]` and the behaviour is exactly today's.
2. The classify forwarded to `choose_replacement` is the pass's `classify` argument (so a proposal not found in the pool is class-checked by the same port); `choose_replacement` already catches a raising classify.
3. `_symbol_class` must keep returning a dict with exactly the `asset_class` and `sub_asset_class` keys PLUS, only when `classify`'s answer carried them, `confidence`, `low_confidence` and `classified_by`, copied unchanged (the pool-fallback result carries none of the three). The `_prefetch` and `choose_replacement` calls only read the class pair, so extra keys are harmless; do not change `_class_of`.
4. `_record` writes `low_confidence` True exactly when the row's classification carried `low_confidence` True, else False (today's value); when the classification's `classified_by` is `"MODEL"`, `sources` is `[SOURCE, "kimi-k3 classification"]` (a module constant `MODEL_SOURCE = "kimi-k3 classification"`) and the record gains `"classified_by": "MODEL"`; otherwise `sources` is `[SOURCE]` and no `classified_by` key (today's record). `_record`'s caller passes the classification in; its other keys are unchanged.
5. Update the module docstring paragraph that says the module "makes no network or model call": it still holds (ports are injected); add one sentence naming the two ports.

New tests in `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_swap_pass_model_ports.py` (hermetic; copy the fixtures style of the neighbouring `test_swap_pass.py`): proposals reach the rule (a proposal in the pool with the right class and the longest history wins; a proposal with the wrong class is dropped CLASS_MISMATCH; a proposal not in the pool is class-checked through `classify`); a raising `proposals`, a non-list return and a non-str element give no proposal and no exception; `proposals=None` gives a result and records byte-equal to the same call before the change (compare against a golden built in the test from the old behaviour: no proposals, `low_confidence` False, `sources` `[SOURCE]`); a classification with `low_confidence` True and `classified_by` MODEL yields a record with `low_confidence` True, `classified_by` MODEL and the two-source list; a replacement still keeps the client's amount; determinism (the same inputs twice give the same output). No existing test is deleted, skipped or edited; the whole of `test_swap_pass.py`, `test_swap_replacement.py` and `test_opal_producer_swap.py` must still pass.

*The checks.* In `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~366/`: `check_swap_pass_ports.py` (stdlib only, ruff clean, offline). It imports `swap_pass` BY PATH from the worktree and runs eight in-process cases (the test cases above, minimal), printing `SWAP-PASS-PORTS-OK cases=8 proposals_forwarded=yes classify_forwarded=yes low_conf_carried=yes baseline_equal=yes` or `SWAP-PASS-PORTS-BAD <why>` (rc 1). `--selftest` mutates the module text in memory three ways (the literal `[]` put back; `classify=classify` removed from the `choose_replacement` call; `low_confidence` fixed to False) and prints `CONTROL-FIRES` only when ALL THREE read BAD. Commit order: the code and test edits as ONE commit first, message citing AR-y-492; then your deliverables and instance.

---

## ACCEPTANCE

<criterion id="AR492-y-AC1" cell_refs="AR-y-492"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~366/check_swap_pass_ports.py</invocation><expect>^SWAP-PASS-PORTS-OK cases=8 proposals_forwarded=yes classify_forwarded=yes low_conf_carried=yes baseline_equal=yes$</expect></criterion>
<criterion id="AR492-y-AC2" cell_refs="AR-y-492"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~366/check_swap_pass_ports.py --selftest</invocation><expect>^CONTROL-FIRES$</expect></criterion>
<criterion id="AR492-y-AC3" cell_refs="AR-y-492"><invocation>(cd infra/aws/lambda/investor-reporting && python -m pytest ycharts/research/tests/test_swap_pass_model_ports.py ycharts/research/tests/test_swap_pass.py ycharts/research/tests/test_swap_replacement.py ycharts/research/tests/test_opal_producer_swap.py -q --color=no -p no:cacheprovider 2>&1 | tail -1)</invocation><expect>^[0-9]+ passed in </expect></criterion>

<proof_of_spec>
The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~366/IRPT_ANLREQ.TO-AR-y-492.swap-pass-takes-the-model-proposals-and-classification-ports-and-carries-the-low-confidence-flag.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-492.swap-pass-takes-the-model-proposals-and-classification-ports-and-carries-the-low-confidence-flag`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR492-y-AC1,AR492-y-AC2,AR492-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-492</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/swap_pass.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_swap_pass_model_ports.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~366/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-492.swap-pass-takes-the-model-proposals-and-classification-ports-and-carries-the-low-confidence-flag.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- source and test files only; nothing is deployed, built into a release or run against AWS or the model; the resident release that carries the swap leg is built by 2.0.0_SA_COO~G2 and applied by IB2 under its own pair.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker; no IAM change in the swap leg.
comp-adversary: RUN -- by reading the contract C-SWAP, the swap rule and the interface above against this cell; the lens: a proposal that skips the class match, a proposals port whose output is trusted unchecked, a classify not forwarded so unknown proposals are dropped, the low-confidence flag still a literal, a changed record when no port is given, a test deleted or edited to pass, a control that cannot fire. NOT seen (blind): the live model's answers and the deployed resident bytes; denominator: 3 criteria.
</preflight>
