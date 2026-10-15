# TO-AR-g-98 -- the backend swap pass: replace every UNRESOLVED holding with a class-matched security from a dated pool snapshot, and the builder of that snapshot

<to_id>IRPT_ANLREQ.TO-AR-g-98</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~199</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>23</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-98` (`decompositions/IRPT_ANLREQ_DECOMP_R23_G.md`) |
**outcome_ref:** FWD-2 (C-SWAP steps 4 and 5; PRD v0.14, v0.18, v0.19) | **depends_on:** `AR-g-52` (`swap_replacement.py`, merged). Order: CTO msgs 8711, 8714 (ADDENDUM 5: a dated pool snapshot, claim `held`, no IAM change, stale after 30 days still swaps and says so) and 8723 (ADDENDUM 6: a holding with no class and no replacement is named "not analysed; Opal Staff will manage the replacement" and never blocks the run).

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~199`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-199` (branch `wk-IRPT_ANLREQ-199`), provisioned by the issuer with the whole of `infra/`, `docs/`, `data/`, `lib/` and `org/missions/D9/IRPT` on disk. Work only there.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~199 <0.9.0_WK_IRPT_ANLREQ~199@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W199-S<k>` (take the next free `<k>`; check the channel file for `W199` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing. Every `.py` you add passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax). No non-ASCII in what you add.
- No live call, NO PUSH, no deploy, no AWS call, no network, no install. Scratch outside the product tree.
- Run each test file ON ITS OWN (`python -m pytest -q <one file>`).

### Read first (under `C:/dev/wk-irpt-anlreq-199/infra/aws/lambda/investor-reporting/ycharts/research/`)

- `swap_replacement.py` (the rule: `choose_replacement(missing, classification, pool_rows, model_proposals, history_days, classify=None)`; its answer has `status` REPLACED or NO_REPLACEMENT, `replacement`, `method`, `candidates`, `dropped`, `confidence`, `named`, `why`); `tests/test_swap_replacement.py` (the style of your tests: made-up tickers, fakes only).
- `runner.py` line 443 (`read_holdings`: a row with `resolution` UNRESOLVED carries that key; the rows have `ticker` and `amount`).

### THE CELL (`AR-g-98`, inlined)

Two NEW modules, stdlib only, no output, no clock, no network, no environment read, no model call; both live in `ycharts/research/`. Your tests run on fakes. The classification of the MISSING security comes from a port, else from the pool itself; there is no model step in this cell.

**1. `swap_pass.py`.** Constants: `SCHEMA = "irpt-swap-pool.v1"`, `POOL_CLAIM = "held"`, `STALE_DAYS = 30`, `MAX_POOL_ROWS = 20000`, `REQUEST_CHUNK = 50` (the number of candidates one Yahoo request carries; a comment says it equals `yahoo_history_days.DEFAULT_CHUNK`), `SOURCE = "etf-classifications pool snapshot"`, `NOT_ANALYSED = "%s is not analysed; Opal Staff will manage the replacement."`. `class SwapPoolRefused(ValueError)`: its message is a stable code, never a quote of the file.
- `load_pool(path, today)` -> `{"rows", "pool_as_of", "pool_claim", "rows_count", "stale_days", "stale"}`. The file is UTF-8 JSON `{"schema", "pool_as_of", "pool_claim", "rows"}` with exactly those four keys. `today` is a `YYYY-MM-DD` run date (the module reads no clock). Codes, checked in this order: `POOL_TODAY_INVALID` (today is not a real date), `POOL_UNREADABLE` (cannot open or not JSON), `POOL_SHAPE` (not a dict, other keys, or schema not SCHEMA), `POOL_CLAIM_NOT_HELD`, `POOL_AS_OF_INVALID` (not a real `YYYY-MM-DD` date), `POOL_DATED_IN_FUTURE` (later than today), `POOL_ROWS` (rows not a list, empty, or longer than MAX_POOL_ROWS), `POOL_ROW` (a row that is not a dict with exactly `ticker`, `asset_class`, `sub_asset_class`; a value that is not a str, is blank, or has leading/trailing space; a ticker that is not upper-case; a repeated ticker). `stale_days` is today minus pool_as_of in days; `stale` is `stale_days > STALE_DAYS` (30 days is fresh, 31 is stale).
- `swap_holdings(rows, pool, *, classify=None, history_days)` -> `{"rows": [...], "swaps": [...]}`. `rows` are `{"ticker", "amount", optional "resolution", ...}`; the input is never mutated. A row whose `resolution` is `"UNRESOLVED"` is swapped; every other row passes through (a copy) in order. For a swapped row: the symbol is `str(ticker).strip().upper()`; its class is `classify(symbol)` when that returns a dict with both `asset_class` and `sub_asset_class` (a `classify` that raises counts as no answer), else the single (asset_class, sub_asset_class) the pool holds for that ticker, else none. Before choosing, call `history_days.prefetch(names)` ONCE when the port has that attribute and the class is known, with the sorted tickers of the pool rows of the same class (casefolded, stripped) excluding the symbol; a `prefetch` that raises is ignored; no class means no prefetch. Then call `swap_replacement.choose_replacement(symbol, classification, pool["rows"], [], history_days)`.
  - REPLACED: the row is replaced IN PLACE by `{**row without "resolution", "ticker": <replacement>, "client_ticker": <symbol>}`, the amount untouched. If the replacement is already a ticker of a non-swapped row (earlier or later in the list), or was already placed by an earlier swap, its amount is ADDED to that row instead (no new row) and the record says `merged` true. Amounts add as floats; the sum is a float when the target's amount is a float, and `repr(total)` (a str such as `"15.0"`) when it is a str.
  - NO_REPLACEMENT: the row is left out of `rows`.
  - One record per swapped row, in row order, with exactly these keys: `proxy_for` (the symbol), `proxy` (the replacement or None), `status`, `method`, `confidence` (the answer's), `low_confidence` False, `sources` `[SOURCE]`, `pool_as_of`, `pool_claim`, `pool_stale`, `candidates_priced` (how many candidates the choice priced), `dropped_reasons` (a dict `{reason: count}` over the answer's `dropped`, sorted by reason), `merged`, `named`; plus `history_days` (the winner's) when REPLACED and `why` (the answer's) when NO_REPLACEMENT. `named` is the answer's sentence plus, when the pool is stale, ` The replacement pool was built on <pool_as_of>, <stale_days> days before this run, which is older than 30 days.`; for NO_REPLACEMENT `named` is `NOT_ANALYSED % symbol` (no stale words). A record never holds an amount.
  - Deterministic: the same inputs give an equal output.

**2. `build_swap_pool.py`.** `python build_swap_pool.py --items <export.json> --as-of YYYY-MM-DD --out <pool.json>`; `main(argv=None)` returns the exit code (0 ok, 2 refused). `--items` is a JSON list of items, or an `aws dynamodb scan` answer `{"Items": [...]}`; an attribute is plain (`"SPY"`) or DynamoDB-typed (`{"S": "SPY"}`: decode a dict with the single key `S`). Functions `plain(value)`, `build_rows(items)` -> `(rows, skipped)` (rows sorted by ticker, each with ONLY `ticker`, `asset_class`, `sub_asset_class`, values stripped; `skipped` a `{reason: count}` dict sorted by reason with the reasons `NOT_AN_ITEM` (item not a dict), `BAD_TICKER` (missing, blank, or not matching `[A-Z0-9][A-Z0-9.\-]{0,14}`), `NO_CLASS` (a class missing or blank), `DUPLICATE` (a repeated ticker: the FIRST row is kept)) and `summary(rows, skipped)` -> `rows`, `skipped` (total), `classes` (distinct casefolded class pairs), `max_class` (the most rows in one pair), `max_requests_per_holding` (`ceil(max_class / swap_pass.REQUEST_CHUNK)`, 0 for no rows). `main` refuses (prints a line beginning `SWAP-POOL-REFUSED`, returns 2, writes nothing) a bad `--as-of` date, an unreadable export, or an export with no item list. Otherwise it writes `{"schema": SCHEMA, "pool_as_of": <as-of>, "pool_claim": "held", "rows": rows}` as `json.dumps(doc, sort_keys=True, indent=1, ensure_ascii=True) + "\n"` (UTF-8, `\n` newlines), reads it back through `swap_pass.load_pool(out, as_of)` (a refusal there prints `SWAP-POOL-REFUSED ...` and returns 2), and prints as its LAST line `SWAP-POOL rows=<n> skipped=<n> classes=<n> max_class=<n> max_requests_per_holding=<n> as_of=<date> sha256=<hex of the file bytes>`.

**Tests (offline; made-up tickers, files in `tmp_path`).** NEW `tests/test_swap_pass.py` with these exact test function names (the checker looks for each by name): `test_load_pool_reads_a_dated_held_snapshot_and_flags_a_stale_one`, `test_load_pool_refuses_every_malformed_snapshot_with_a_stable_code` (parametrized over every code above), `test_an_unresolved_row_is_replaced_in_place_keeping_the_amount_and_naming_the_client_ticker`, `test_a_row_with_no_class_or_no_priced_candidate_is_left_out_and_named_not_analysed`, `test_a_replacement_already_held_merges_its_amount`, `test_the_pick_is_the_longest_history_ties_to_the_first_ticker_and_resolved_rows_pass_through`, `test_the_record_carries_the_pool_vintage_and_the_stale_words` (also assert `dropped_reasons`), `test_a_history_port_with_prefetch_is_asked_once_for_the_same_class_candidates`. NEW `tests/test_build_swap_pool.py`: `test_plain_and_typed_items_build_the_same_snapshot`, `test_rows_without_a_ticker_or_class_are_skipped_and_counted`, `test_the_snapshot_loads_through_swap_pass_and_carries_the_claim_and_date`, `test_the_summary_line_states_rows_classes_the_largest_class_and_the_request_bound` (101 rows in one class gives a bound of 3), `test_a_bad_date_or_an_unreadable_export_is_refused_with_nothing_written`.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR98-g-AC1" cell_refs="AR-g-98"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g98_checks.py g98</invocation><expect>^AR-G98-OK</expect></criterion>

<criterion id="AR98-g-AC2" cell_refs="AR-g-98"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g98_checks.py regress</invocation><expect>^AR-G98-REGRESS-OK</expect></criterion>

<expected_criteria>AR98-g-AC1,AR98-g-AC2</expected_criteria>

- AC1 asks the two modules 56 things on fakes (the pool file's refusals and its 30-day edge, in-place replacement keeping the amount, the pick rule, the left-out words, merges in both orders, amounts conserved, the record's exact keys, the prefetch hook, the builder's output bytes, skips, summary line and request bound, refusals), scans both sources for a banned import or call, then checks your thirteen named tests exist and pass. At base it FAILs.
- AC2 runs six existing test files one at a time (59 tests) and needs all of them to pass, and it needs your branch (against the merge-base with `box/dell2`) to change only your four files, your folder, your order and the channel file. At base it PASSes. Run it under `timeout 590`.

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS call, no HTTP, no installs.
- **Refusal clause.** If a criterion cannot be met as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/swap_pass.py
infra/aws/lambda/investor-reporting/ycharts/research/build_swap_pool.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_swap_pass.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_build_swap_pool.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~199/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-98.swap-pass-and-pool-builder.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R23_G.md</decomp_doc> round 23, workstream ~G, cell `AR-g-98`.
<owned_cells>AR-g-98</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR98-g-AC1, AR98-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~199/IRPT_ANLREQ.TO-AR-g-98.swap-pass-and-pool-builder.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-98`.
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put the `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder (use `kind` `test` for a test file): commit the product files first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR98-g-AC1,AR98-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the files you added with their line counts;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- two NEW modules and their tests; nothing imports them yet (the producer wiring is `AR-g-100`, the release packaging `AR-g-101`), so no deployed or resident byte changes and no behaviour moves. The pool file format they define is what the r34 resident ships (a dated snapshot, claim held, no IAM change: CTO ADDENDUM 5).
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no permission change; the builder reads one local export file.
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- read against PRD v0.14 (C-SWAP), CTO ADDENDA 5 and 6 and `swap_replacement.py`. Traps: a stale or future-dated pool accepted; a claim other than held accepted; the client's amount lost or changed on a swap, or carried into a record; a replacement that is already held creating a second row of the same ticker; a left-out holding silently dropped without words; a lower-case or repeated pool ticker; the swap reading a clock or the environment; the builder keeping the LAST duplicate or copying extra attributes; the request bound rounded down. The checker feeds a green arm (a reference build passes the 56 cases, the thirteen named tests and the 59 regress tests) and 27 mutant arms (eighteen on `swap_pass.py`, nine on `build_swap_pool.py`), each of which fails the check.
</preflight>

- Cut on CTO msgs 8711, 8714, 8723 and the issuer's reference build in a scratch tree. Risk WORLD: the floor of an infrastructure path; new source and tests only, nothing deployed. Base: `AR98-g-AC1` FAILs and `AR98-g-AC2` PASSes (59), as expected.
- NOT claimed: that any holding of run 3 has a class (BREIT, SREIT, KPEC and TIMXX have no row in `etf-classifications`, read live 2026-10-15; the classifier is its own cell and pair after run 3, CTO ADDENDUM 6); the Yahoo history port (`AR-g-99`), the producer wiring (`AR-g-100`) and the resident package (`AR-g-101`).
