# TO-AR-g-100 -- the Opal producer runs the swap pass: an UNRESOLVED holding is replaced from the pool (or left out and named) before anything is classified or priced, and the report names every substitution

<to_id>IRPT_ANLREQ.TO-AR-g-100</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~202</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>24</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-100` (`decompositions/IRPT_ANLREQ_DECOMP_R24_G.md`) |
**outcome_ref:** FWD-2 (C-SWAP steps 4 and 5: replace, record, name in the report) | **depends_on:** `AR-g-98` (`swap_pass.py`, merged `8540b8449c`), `AR-g-99` (`yahoo_history_days.py`, merged `a6bcac3875`), `AR-g-68` (the UNRESOLVED row and `allow_unresolved`). Order: CTO msgs 8711, 8714, 8723.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~202`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-202` (branch `wk-IRPT_ANLREQ-202`), provisioned by the issuer with the whole of `infra/`, `docs/`, `data/`, `lib/`, `org/standards` and `org/missions/D9/IRPT` on disk. Work only there.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~202 <0.9.0_WK_IRPT_ANLREQ~202@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W202-S<k>` (take the next free `<k>`; check the channel file for `W202` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax). No non-ASCII in what you add.
- No live call, NO PUSH, no deploy, no AWS call, no network, no install. Scratch outside the product tree.
- Run each test file ON ITS OWN (`python -m pytest -q <one file>`). The checker is run WITHOUT `-I` (the producer tests import packages from the user site).

### Read first (under `C:/dev/wk-irpt-anlreq-202/infra/aws/lambda/investor-reporting/ycharts/research/`)

- `opal_producer.py` (the whole file: `_read_stage` line 309, `produce` line 436, the disclosures at line 495-513; `produce_package` and `produce_commentary_pdf` also call `_read_stage`), `swap_pass.py` (`swap_holdings(rows, pool, *, classify=None, history_days)` -> `{"rows", "swaps"}`; the record keys and the `named` sentences are its), `runner.py` line 443 (`read_holdings(..., allow_unresolved=False)`), `tests/test_opal_producer.py` (the fixtures and helpers `make_stores`, `served_world`, `FakeClassifier`, `stored`, `REQ`, `FIRM` you will import) and `tests/fixtures/opal_producer/frozen_input.json`.

### THE CELL (`AR-g-100`, inlined)

All edits are in `opal_producer.py` (plus one new test file). A swap store is OPTIONAL: with none, the producer behaves byte for byte as today.

1. **Import and constants.** `import swap_pass  # noqa: E402` beside the other module imports; a constant `SWAP_ID = "SWAP"` beside `UNPRICED_ID`. In the module docstring's `stores` list add an entry for `swap` (optional): `{"pool": swap_pass.load_pool(...)'s dict, "history_days": a callable (with an optional prefetch), "classify": optional symbol -> class row}`; present means an UNRESOLVED holding is replaced from the pool (or left out and named) before anything is classified or priced; absent means an UNRESOLVED holding refuses the run exactly as before.
2. **`_swap_stage(holdings, swap, stores)`** (new, placed before `_read_stage`) -> `(holdings with the effective rows, the records)`. `pool = swap.get("pool")` must be a dict and `swap.get("history_days")` callable, else `ProducerRefused("store required: swap")`. `classify = swap.get("classify")`; when None it is a function that returns `stores["classifier"].get_classification(symbol)` (the classifier row has `asset_class` and `sub_asset_class`). Run `swap_pass.swap_holdings(holdings["rows"], pool, classify=classify, history_days=<the callable>)`; the effective rows are `[{"ticker": r["ticker"], "amount": r["amount"]} for r in result["rows"]]` (no other key: the pass's `client_ticker` and any `resolution` are dropped); if there are none, `ProducerRefused("NO_ANALYSABLE_HOLDINGS")`; return `dict(holdings, rows=<effective rows>)` and `result["swaps"]`.
3. **`_read_stage`.** `swap = stores.get("swap")`; the `runner.read_holdings` call keeps its exact current arguments (`revision=request_ref["request_revision"]` and nothing else) when `swap` is None, and adds `allow_unresolved=True` ONLY when `swap` is not None (an existing test spies on the kwargs). When `swap` is not None and any read row has `resolution` UNRESOLVED, replace `holdings` and `swaps` from `_swap_stage`. After `run_doc` is built (it is built from the EFFECTIVE rows), `if swaps: run_doc["swaps"] = copy.deepcopy(swaps)` (no key at all when there is none). Nothing else in the stage changes: the classifier is asked about the effective tickers.
4. **`produce`.** After `settings` and the disclosures are built (BOTH the unpriced and the priced branch), `if run_doc.get("swaps"):` prepend one disclosure per record, in row order, `{"disclosure_id": SWAP_ID, "text": <record["named"]>}`, before every other disclosure, and add `settings["swap"] = {"pool_as_of", "pool_claim", "pool_stale"` (taken from the first record), `"swapped"` (the number of records whose status is REPLACED), `"left_out"` (the rest)`}`. Without swaps the disclosures, the settings and the run record are exactly today's.

**Tests (offline; the producer world of `test_opal_producer.py` with one or two UNRESOLVED rows appended to the frozen input).** A NEW file `tests/test_opal_producer_swap.py` importing `test_opal_producer as tp` with these exact test function names (the checker looks for each by name): `test_an_unresolved_holding_is_replaced_before_anything_is_classified`, `test_every_substitution_is_named_first_in_the_disclosures_and_the_settings_say_which_pool`, `test_a_holding_with_no_class_is_left_out_and_named_not_analysed_and_the_run_goes_on`, `test_a_run_with_nothing_analysable_left_refuses_before_any_write`, `test_without_a_swap_store_an_unresolved_holding_refuses_as_it_always_did_and_the_read_is_unchanged`, `test_a_run_with_the_swap_store_and_no_unresolved_holding_is_byte_for_byte_the_run_without_it` (give both runs the same deterministic `timer`), `test_a_stale_pool_still_swaps_and_the_disclosure_and_settings_say_so`, `test_the_packager_path_reads_the_same_effective_rows_and_the_two_request_sizes_agree` (calls `op._read_stage`; asserts `swap_pass.REQUEST_CHUNK == yahoo_history_days.DEFAULT_CHUNK`). The swap store in your tests: `{"pool": swap_pass.load_pool(<a tmp_path pool file>, "2026-10-06"), "history_days": <a dict .get>}`, and a classifier with rows for the client's ticker and the replacement.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR100-g-AC1" cell_refs="AR-g-100"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g100_checks.py g100</invocation><expect>^AR-G100-OK</expect></criterion>

<criterion id="AR100-g-AC2" cell_refs="AR-g-100"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g100_checks.py regress</invocation><expect>^AR-G100-REGRESS-OK</expect></criterion>

<expected_criteria>AR100-g-AC1,AR100-g-AC2</expected_criteria>

- AC1 runs the producer on 25 cases (the replacement in place with the client's amount, the record without amounts, the run record carrying the swaps, the pool not mutated, the document valid against the v2 schema, the disclosure order with pricing off and on, the words, the settings, two swapped holdings in row order, the classify override, a stale pool, a run with nothing left refused before any write, a malformed swap store refused, the unchanged read and the byte-for-byte run without a swap, the packager path, determinism), then checks your eight named tests exist and pass. At base it FAILs.
- AC2 runs six existing test files one at a time (67 tests: the producer, its price and benchmark and page-wording runs, the packager, the unresolved reader) and needs all of them to pass, and it needs your branch (against the merge-base with `box/dell2`) to change only your two files, your folder, your order and the channel file. At base it PASSes. Run it under `timeout 590`.

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS call, no HTTP, no installs.
- **Refusal clause.** If a criterion cannot be met as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/opal_producer.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer_swap.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~202/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-100.producer-runs-the-swap-pass.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R24_G.md</decomp_doc> round 24, workstream ~G, cell `AR-g-100`.
<owned_cells>AR-g-100</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR100-g-AC1, AR100-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~202/IRPT_ANLREQ.TO-AR-g-100.producer-runs-the-swap-pass.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-100`.
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put the `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder (use `kind` `test` for a test file): commit the product files first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR100-g-AC1,AR100-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the lines you changed in `opal_producer.py` with line numbers;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- `opal_producer.py` is a member of the resident package (r32 carries the PRE-swap bytes) and is not staged into any Lambda; nothing is deployed by this cell. With no `swap` store the module's behaviour is byte for byte today's (the check and the existing 67 tests pin it), so the change takes effect only where the resident assembly (round 25's `AR-g-101`) supplies a swap store. The reader call keeps its exact arguments without a swap store. A resident run with a swap store and no UNRESOLVED holding is byte for byte today's (check case W9).
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no permission change; the swap needs no table read the resident role lacks (the pool is a shipped file, CTO ADDENDUM 5; the classifier is the existing GetItem port).
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- read against C-SWAP steps 4 and 5, CTO ADDENDA 5 and 6 and the producer's existing tests. Traps: the reader asked to allow unresolved rows for EVERY run (an existing test spies on its arguments, and an unconfigured run would stop refusing); the pass never run when the store is present; the original rows computed instead of the effective ones (the client's unpriceable ticker classified and priced); the swap disclosures after the pricing ones; an amount lost or changed; a record carrying an amount; a swaps key present on a run with none (breaking the byte-for-byte guarantee for retained artifacts); a run with every holding left out writing a report of nothing; the classify override ignored; the stale flag lost. The checker feeds a green arm (a reference build passes the 25 cases, the eight named tests and the 67 regress tests) and 15 mutant arms, each of which fails the check.
</preflight>

- Cut on CTO msgs 8711, 8714, 8723 and the issuer's reference build in a scratch tree. Risk WORLD: the floor of an infrastructure path; source and tests only, nothing deployed. Base: `AR100-g-AC1` FAILs and `AR100-g-AC2` PASSes (67), as expected.
- NOT claimed: that any run-3 holding is swapped (BREIT, SREIT, KPEC and TIMXX have no class row, read live 2026-10-15: they take the left-out branch); the resident assembly that builds the swap store and ships the pool (`AR-g-101`, round 25); the live Yahoo read (its first run is the r34 apply's smoke read).
