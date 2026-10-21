# TO IRPT_ANLREQ.TO-AR-y-497.swap-record-carries-the-class-pair-and-the-model-confidence-and-the-low-confidence-sentence -- BUILD AND PROVE OFFLINE: the swap record carries the class pair and the model confidence for MODEL-classified rows only

<to_id>IRPT_ANLREQ.TO-AR-y-497.swap-record-carries-the-class-pair-and-the-model-confidence-and-the-low-confidence-sentence</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~369</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-21</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ156</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by the path floor | **Decomp cell:** `AR-y-497` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** C-SWAP model leg, graded under FWD-2 (PRD v0.25 and v0.26) | **depends_on:** AR-y-461's read `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~326/SWAP_LEG_READ.md`; CTO ruling v0.26 (kimi-k3, no web search, below 0.80 flagged)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~369`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-369` (branch `wk-IRPT_ANLREQ-369`), provisioned by the issuer from the current branch. FIRST confirm with `git -C C:/dev/wk-irpt-anlreq-369 branch --show-current` that it prints `wk-IRPT_ANLREQ-369` and that this order file exists in it; if not, STOP and report WITHOUT touching any other worktree or branch. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~369 <0.9.0_WK_IRPT_ANLREQ~369@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W369-S<k>`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING, with `spec_asserts` and `world_is` fields. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (ruff clean; no single-letter names `l`, `O`, `I`; no non-ASCII; stdlib only unless the order says otherwise).
- **No AWS call, no network, no model call, no push, no deploy, no release build.** Every model call in a test is a fake `send`. The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/IRPT_ANLREQ.TO-AR-y-459.run7b-browser-leg-script-re-proved-offline-against-the-advisor-required-form.proof_of_spec.json` (read it first; `controls` holds `mutant` and `determinism` only), with `to_id` exactly the order's id; run `python .tools/proof-of-spec-check.py <instance> "AR497-y-AC1,AR497-y-AC2,AR497-y-AC3"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (with the instance, one commit) only on VALID and only after EVERY other edit you intend is committed (a status of complete removes your path grant). The instance's check-script reference is pinned to a commit that EXISTS (commit the script first, then pin it). A test file that leaks `sys.path` makes other files fail at collection in some orders: keep pytest lines in the order written.
### THE INTERFACE (shared by the three cells of the swap leg; code to it exactly)

Source read: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~326/SWAP_LEG_READ.md` (sections S1-S4; its line numbers have moved, find the code by name). PRD contract C-SWAP (v0.14, restated v0.26): step 3 CLASSIFY with the estate's Kimi model kimi-k3 (`etf_classification_model.py`, `MODEL`), WITHOUT web search, output bound to the live (class, sub-class) vocabulary, below 0.80 confidence FLAGGED; step 4 REPLACE from the class-matched pool plus model proposals that pass the class match and have Yahoo history, the longest Yahoo history wins, ties by ticker; the model widens the pool and NEVER picks. No new vendor; no IAM change (the resident role already reads the estate Kimi key, `resident.tf` Sid `ReadTheEstateKimiKey`).
1. `swap_pass.swap_holdings(rows, pool, *, classify=None, history_days, proposals=None)`. `classify(symbol)` returns None or a dict with `asset_class` and `sub_asset_class` and, when the classification came from the model, ALSO `confidence` (float), `low_confidence` (bool) and `classified_by` (the str `"MODEL"`). `proposals(symbol, classification)` returns a list of ticker strings (the model's proposed same-class securities) or raises; the pass treats a raise, a non-list or a non-str element as no proposals for that symbol.
2. `swap_model.make_swap_model(pool_rows, send, *, model_module=None, api_key="", threshold=0.80, max_proposals=5)` in the NEW module `infra/aws/lambda/investor-reporting/ycharts/research/swap_model.py` returns an object with `classify(symbol)` (the shape of item 1; None when the model cannot classify the symbol inside the vocabulary) and `propose(symbol, classification)` (item 1; at most `max_proposals` upper-cased tickers matching `[A-Z0-9.-]{1,12}`, never the symbol itself, no duplicates; `[]` on ANY failure). `send(payload, timeout_seconds)` is the resident's Kimi transport (`ycharts/generate/kimi_port.py` `kimi_send(secret_reader(...))`); the module opens no connection, reads no secret and no environment variable.
3. The producer stage `_swap_stage` (`ycharts/research/opal_producer.py`) takes from the `swap` store dict two OPTIONAL keys, `model_classify` (a `classify` of item 1) and `proposals` (item 1), passes `proposals` to `swap_holdings`, and composes the classify it passes: the store's `classify` when given, else the classifier lookup (`stores["classifier"].get_classification(symbol)`) and, ONLY when that answers nothing usable (None, or no class pair), `model_classify(symbol)`.
4. The resident binding `opal_swap_model`, an OPTIONAL member of `resident_bindings.json` that is exactly `{"enabled": true|false}`: absent or false means today's behaviour (no model call); true makes `_swap_extras` add `model_classify` and `proposals` (from `swap_model.make_swap_model` over the pool rows) to the `swap` store. Any other shape refuses the install with `SWAP_MODEL_BINDING_INVALID`.

### THE CELL (`AR-y-497`)

*What and why.* The CTO's read of run 7N asks, for each swap, its class, its confidence and its low_confidence flag (G2 msg 11993). The swap record that AR-y-492 wrote carries `low_confidence` and `classified_by` but NOT the class pair the model assigned and NOT the model's number: its `confidence` field is the replacement rule's label (CLASS_MATCH_PRICED...). This cell adds the three missing facts to the record, for MODEL-classified rows only, so every existing record stays byte-equal.

*The change.* In `infra/aws/lambda/investor-reporting/ycharts/research/swap_pass.py` only (read `_record`, `_symbol_class` and the call site of `_record` first): when the row's classification carries `classified_by` equal to `"MODEL"`, the record gains exactly three keys: `"asset_class"` and `"sub_asset_class"` (the classification's two strings, unchanged) and `"model_confidence"` (the classification's `confidence` copied as a float when it is a real number from 0 to 1 inclusive and not a bool; else the key is omitted). A row whose classification is not from the model (pool or lookup) gets none of the three: the record is exactly what it is today. No other new key, no change to `sources`, `low_confidence` or `classified_by`, no change to any other file. SECOND CHANGE (CTO msg of 11:22Z, the product call): the disclosure text `named` of a REPLACED swap whose classification carries `low_confidence` True gets ONE added plain sentence, appended after the existing text and after any stale-pool sentence: `<SYMBOL> was replaced by <PROXY> on a low-confidence match; review before relying on it.` (the client's symbol and the public replacement ticker, no number); `named` for every other swap (not low confidence, not REPLACED, not from the model) is byte-equal to today's. WRITE THE TESTS FIRST (failing-first): commit nothing before you have run the new test file against the UNCHANGED `swap_pass.py` and seen the named-sentence cases and the record-key cases FAIL; print the failure counts in your report; then make the change and see them pass. Update the module docstring sentence that lists the model fields to name the three keys.

New tests in `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_swap_record_class.py` (hermetic; the fixtures style of `test_swap_pass_model_ports.py`): a low-confidence MODEL replacement ends its `named` with the exact sentence (and a stale-pool sentence, when present, comes before it); a MODEL replacement at confidence 0.80 or above, a non-model replacement and a NOT_ANALYSED row have `named` equal to today's; a MODEL classification yields the three keys with the exact values; a confidence of exactly 0.8 and of 0.79 are copied as floats; a bool, a string or an out-of-range number omits `model_confidence` only; a non-MODEL classification (a lookup answer, the pool fallback) yields a record equal to the same call's record before this change (the golden is built in the test from the old key set); a NOT_ANALYSED row (no classification) is unchanged; the record never carries an amount. No existing test is edited, deleted or skipped; `test_swap_pass.py`, `test_swap_pass_model_ports.py`, `test_swap_replacement.py`, `test_opal_producer_swap.py` and `test_opal_producer_swap_model.py` must still pass.

*The checks.* In `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~369/`: `check_swap_record_class.py` (stdlib only, ruff clean, offline). It imports `swap_pass` BY PATH from the worktree and runs seven in-process cases, printing `SWAP-RECORD-CLASS-OK cases=7 model_rows_carry_class=yes model_confidence_float=yes other_rows_unchanged=yes low_conf_sentence=yes` or `SWAP-RECORD-CLASS-BAD <why>` (rc 1). `--selftest` mutates the module text in memory four ways (the `model_confidence` copy removed; the three keys added to every record, not only MODEL rows; `sub_asset_class` dropped; the low-confidence sentence removed) and prints `CONTROL-FIRES` only when ALL FOUR read BAD. Commit order: the code and test edits as ONE commit first, message citing AR-y-497; then your deliverables and instance.

---

## ACCEPTANCE

<criterion id="AR497-y-AC1" cell_refs="AR-y-497"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~369/check_swap_record_class.py</invocation><expect>^SWAP-RECORD-CLASS-OK cases=7 model_rows_carry_class=yes model_confidence_float=yes other_rows_unchanged=yes low_conf_sentence=yes$</expect></criterion>
<criterion id="AR497-y-AC2" cell_refs="AR-y-497"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~369/check_swap_record_class.py --selftest</invocation><expect>^CONTROL-FIRES$</expect></criterion>
<criterion id="AR497-y-AC3" cell_refs="AR-y-497"><invocation>(cd infra/aws/lambda/investor-reporting && python -m pytest ycharts/research/tests/test_swap_record_class.py ycharts/research/tests/test_swap_pass_model_ports.py ycharts/research/tests/test_swap_pass.py ycharts/research/tests/test_swap_replacement.py ycharts/research/tests/test_opal_producer_swap.py ycharts/research/tests/test_opal_producer_swap_model.py -q --color=no -p no:cacheprovider 2>&1 | tail -1)</invocation><expect>^[0-9]+ passed in </expect></criterion>

<proof_of_spec>
The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~369/IRPT_ANLREQ.TO-AR-y-497.swap-record-carries-the-class-pair-and-the-model-confidence-and-the-low-confidence-sentence.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-497.swap-record-carries-the-class-pair-and-the-model-confidence-and-the-low-confidence-sentence`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR497-y-AC1,AR497-y-AC2,AR497-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-497</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/swap_pass.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_swap_record_class.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~369/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-497.swap-record-carries-the-class-pair-and-the-model-confidence-and-the-low-confidence-sentence.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- source and test files only; nothing is deployed, built into a release or run against AWS or the model; the resident release that carries the swap leg is built by 2.0.0_SA_COO~G2 and applied by IB2 under its own pair.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker; no IAM change in the swap leg.
comp-adversary: RUN -- by reading the contract C-SWAP, the swap rule and the interface above against this cell; the lens: the three keys added to non-model rows (a record that changes where it should not), a confidence copied as a bool or an out-of-range number, the class pair re-spelled, an amount or client string reaching the record, an existing test edited to pass, a control that cannot fire. NOT seen (blind): the live model's answers and the deployed resident bytes; denominator: 3 criteria.
</preflight>
