# TO-AR-t-33 -- the figure projection admits only estate tickers and the request's own model keys; the CTO's condition-4 test (AR-t-33, round 43, workstream T, direct act)

<to_id>IRPT_ANLREQ.TO-AR-t-33</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~192</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>~T</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~T (commentary) | **Decomp cell:** `AR-t-33` (`decompositions/IRPT_ANLREQ_DECOMP_R43_T.md`) |
**outcome_ref:** FWD-10 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`AR-t-33`: "`figures_block` admits a `top_holdings` ticker ONLY if it is in the estate's classification table (`classification.load_classifications()`), and a `model_names` entry ONLY if it is among the request's own `comparison_keys`; anything else is dropped and counted. Three new tests in the existing figures test file, including the condition-4 test: a dollar amount, a name and an account id fed to the projection are all dropped, with a clean control that survives. Fakes only."

Work in your worktree; every path is relative to its root. Measured at the base: in `data/transcripts/scripts/commentary/drafter.py` the ticker pattern `_TICKER_RX` (`[A-Z0-9][A-Z0-9.\-]{0,9}`) fullmatches `12345678` and `A1234567` (neither is in the estate table of 11,361 tickers), so an account number written as a ticker reaches the prompt; and `_model_names_member` keeps any string of at most 80 characters, so a client name written as a model name does too. `AAPL` and `BRK.B` are in the table. The CTO's condition (msg 8577): "a test feeds `figures_block` a dollar amount, a name and an account id, and shows all three dropped."

**Build:**
1. `drafter.py`: `_top_holdings_member` keeps an item only when its ticker fullmatches `_TICKER_RX` AND `ticker.upper()` is a key of `_classification.load_classifications()` (load the table once at import into a module constant next to `ALLOWED_CATEGORIES`, from the same module that already provides it). `figures_block(figures, withheld=None, allowed_models=None)` gains the optional `allowed_models` (an iterable of strings): when it is given, a `model_names` entry is kept only if it is in that set; when it is `None` the previous behaviour stays (this keeps the existing tests valid). `abstract_fields` passes `allowed_models=request.get("comparison_keys") or []` (a request with no comparison keys keeps no model name). Nothing else changes; the counts keep the existing `figures.<member>` names.
2. Three new tests in `data/transcripts/scripts/tests/test_commentary_figures.py` (do not touch the other four there), fakes only:
   - `test_condition_dollar_name_and_account_id_are_all_dropped`: call `drafter.abstract_fields` with a request whose `comparison_keys` is `["Core Growth"]` and whose `figures` carry: a dollar amount as an allocation value (`"$1,250,000"`) and as a ticker (`"$1250000"`); a name as a model name (`"Smith Family Trust"`) and as a ticker (`"Smith"`); an account id as a model name (`"12345678"`) and as a ticker (`"12345678"`, `"A1234567"`). Assert none of those strings appears anywhere in `json.dumps(result)`; assert the `withheld` counts record the drops; assert a clean control survives in the same block: model name `"Core Growth"`, ticker `"AAPL"` with weight 6.2, allocation `{"equity": 60.0}`.
   - `test_tickers_must_be_in_the_estate_table`: `"AAPL"` and `"BRK.B"` survive; `"ZZZZZZZZ9"` (matches the pattern, not in the table) is dropped and counted.
   - `test_model_names_must_be_among_the_requests_comparison_keys`: with `comparison_keys` `["A", "B"]` the entries `"A"` survives and `"C"` is dropped and counted; with `allowed_models=None` passed directly to `figures_block` a name of at most 80 characters still passes (the old behaviour for direct callers).
   Keep every existing `test_commentary_*.py` green.

### ACCEPTANCE

<criterion id="AR33-t-AC1" cell_refs="AR-t-33"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R43_CHECKS/r43_checks.py cn1</invocation><expect>R43-CN1-OK</expect></criterion>
`AR33-t-AC1` -- the three named tests pass together with the four existing figure tests (7 passed). Dry-run at box/dell2 667daf91c8: `R43-CN1-FAIL missing ...` -- FAIL as expected.

<expected_criteria>AR33-t-AC1</expected_criteria>

## BOUNDS

- **Grant.** The paths below, this order's file, your deliverables folder.
- **No network, no AWS, no secret.** You deploy nothing; the packaged copy under `infra/aws/lambda/transcripts-pull/dist/` is build output and is not yours.
- **C-KIMI.** The prompt carries no client, household, advisor or firm name, no account number, no dollar amount and no raw row. Do not widen any list.
- **Refusal clause.** If the classification table cannot be loaded at import in your tree, that is a `BLOCKING` row naming the file; do not stub it. If an existing figures test fails because of the new rule, change the test's fixture to a ticker in the table (and say which) rather than loosening the rule.
- **Your worktree is sparse.** A missing folder is a row, not a reason to stub.

<paths>
data/transcripts/scripts/commentary/drafter.py
data/transcripts/scripts/tests/test_commentary_figures.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R43_T.md</decomp_doc> (round 43, workstream T), cell `AR-t-33`.
<owned_cells>AR-t-33</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: AR33-t-AC1. Instance at `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~192/IRPT_ANLREQ.TO-AR-t-33.figures-tickers-and-model-names-closed.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> AR33-t-AC1` BEFORE the flip. Commit code first, then pin.
</proof_of_spec>

**REPORT:** the two rule changes and where `abstract_fields` passes the keys, the three test names, the check line, commits.

---

<preflight>
comp-blast: RUN (by reading) -- `drafter.py` is imported by `lambda_handler.py` and the packaged copy under `infra/aws/lambda/transcripts-pull/dist/` (build output, not edited); `figures_block` gains an optional third parameter, so existing callers keep working. Nothing is deployed by this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no permission change; fakes only.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is touched. comp-routes and comp-cache: DECLARED-NOT-APPLICABLE.
comp-adversary: RUN -- `comp-adversary compose` on this order at read-vintage 00a9f8ee10: the neighborhood is the decomposition only, 0 unproven dependencies, the one flagged path is this order's own proof instance (absent until built). Traps named for the worker: a test that feeds the strings only through a path that already drops them; a model-name rule that passes when `comparison_keys` is empty; a ticker rule that is applied to the pattern but not to the table.
</preflight>

- Cut on the CTO half condition 4 (msg 8577) and the issuer's measured gap (decomposition R43_T). Risk LOCAL, direct act.
- Base: `AR33-t-AC1` FAIL as expected (`R43-CN1-FAIL missing ...`) at box/dell2 667daf91c8, run by the issuer before the cut.
