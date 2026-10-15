# TO-AR-g-82 -- the DEMQUE store price adapter: the per-CUSIP stored daily total return, found through the open index row, chained to a base-100 level series

<to_id>IRPT_ANLREQ.TO-AR-g-82</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~182</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>12</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-82` (`decompositions/IRPT_ANLREQ_DECOMP_R12_G.md`) |
**outcome_ref:** FWD-7 (C-PRICES) | **depends_on:** `AR-g-80` (merged `f089142e91`, `tr_level.py`) and `AR-g-69` (merged `d1de2f0cd6`, the read that fixed the one formula).

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~182`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-182` (branch `wk-IRPT_ANLREQ-182`), provisioned by the issuer with the whole of `infra/`, `docs/` and `data/` on disk. Work only there.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~182 <0.9.0_WK_IRPT_ANLREQ~182@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W182-S<k>` (take the next free `<k>`); `surfaced_at` of any row = `date -u +%FT%TZ` at filing. Every `.py` you add passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax). No non-ASCII in what you add.
- No live call, NO PUSH, no deploy, no AWS call, no network, no install. Scratch outside the product tree. `pandas`, `pyarrow` and `yfinance` may be absent from this box: a test that needs one skips with `pytest.importorskip`, never fails.

### Read first (under `C:/dev/wk-irpt-anlreq-182/`)

- `infra/aws/lambda/investor-reporting/ycharts/research/tr_level.py` (merged; the ONE formula: `chain_levels(daily_returns, base=100.0)` and `returns_from_levels(pairs)`) and `infra/aws/lambda/investor-reporting/ycharts/research/price_source.py` (the chain core that will call your reader as `reader(symbol, start, end)`), with their tests under `infra/aws/lambda/investor-reporting/ycharts/research/tests/`.
- The facts record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~176/r9/PRICE_ADAPTER_FACTS.json`: `q2` (the formula for each source) and `q4` (the four adapter shapes).
- `data/mdpf/scripts/demque/price_store.py` (`s3_root()` at line 46 and the column contract `PRICE_COLS`, `TR_COLS`, `OLD_INDEX_COLS` at lines 33-35; the index at `<root>/index/index.parquet`, the prices at `<root>/cusip=<CUSIP>/prices.parquet`) and `data/mdpf/scripts/demque/tr_column.py` (how `total_return` is built). NOT importable on the host; re-write the logic.
- `lib/opal_naming.py` (`address()`), which IS shipped in the resident package.

### THE CELL (`AR-g-82`, inlined)

Andrew's rule: prices are TOTAL RETURN. The price chain (`price_source.resolve_prices`) asks each source for a level series through `reader(symbol, start, end)`; every reader hands back `(date_str, level)` on the same footing: `level = 100` at the first retained date and `level_t = level_(t-1) * (1 + r_t)` with `r_t` that source's DAILY total-return fraction, built by `tr_level`. This cell builds DEMQUE store adapter. It takes its client as an argument and makes no call at import.

**Build a NEW file `infra/aws/lambda/investor-reporting/ycharts/research/price_adapter_demque.py`** with exactly this contract.

1. The module exposes `make_reader(s3, *, s3_root=None, index_rows=None, price_rows=None)` and NO other public name. It returns `reader(symbol, start, end)`: `symbol` is any str (strip blanks, upper-case it); `start` and `end` are inclusive `YYYY-MM-DD` strings. The reader returns a list of `(date_str, level)` tuples, ascending by date, `level` a `float`; `[]` when the symbol has no open index row or no usable price row in the window.
2. `index_rows` is a test seam: a list of dicts with `cusip`, `yahoo_symbol`, `valid_from`, `valid_to`. The symbol's OPEN row is the row whose `yahoo_symbol` equals the symbol and whose `valid_to` is `None`, an empty string or NaN. If several rows are open, take the LAST in list order. A row that is not open is never used, whatever its position in the list. No open row: return `[]` and read NO price rows.
3. `price_rows` is a test seam: a mapping (`dict`-like, read only with `price_rows[cusip]`) from a CUSIP to a list of dicts with `date` (a `YYYY-MM-DD` str) and `total_return` (the stored DAILY total-return FRACTION, 0.01 is one percent, null on the first stored row). A `total_return` that is `None`, NaN, infinite, a `bool` or not a number is dropped by `tr_level` (it never seeds the base). Cut the rows to `start <= date <= end` FIRST, then `tr_level.chain_levels` (`import tr_level`, a bare import) and return the pairs as tuples. `total_return` is a return, never a level.
4. When `index_rows` is `None` the index is read from S3: `s3_root` (a string `s3://<bucket>/<prefix>`; default is `lib/opal_naming.py` `address("yahoo", "global", "silver", "price_history", "x")` with its last path segment removed; import `opal_naming` INSIDE the function, a bare import) joined with `/index/index.parquet`. When `price_rows` is `None` the prices of the CUSIP are read from `<s3_root>/cusip=<CUSIP>/prices.parquet`. Split an `s3://bucket/key` into `Bucket` and `Key`; `s3.get_object(Bucket=..., Key=...)["Body"].read()`; the bytes go through `pyarrow.parquet.read_table(io.BytesIO(raw)).to_pylist()`. `pyarrow` and `io` are imported INSIDE the function only. A `date` value that is not a str is normalised with `.isoformat()[:10]` when it has `isoformat`, else `str(value)[:10]`. Read the index once per reader and each CUSIP once per reader (cache in the closure).
5. When a read from S3 is needed and `s3` is `None`, the FIRST call of the reader raises `ValueError("DEMQUE_SOURCE")` (the chain types it). No other exception is caught or invented.
6. The module is stdlib-only at the top level (`__future__`, `math`, `re`, `datetime`, `collections`, `typing` and `tr_level`); it opens no file, prints nothing, reads no environment variable, makes no connection of its own.

**Tests.** A NEW file `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_price_adapter_demque.py` with at least 6 tests, offline, with hand-computed values (made-up dates and numbers): the open-row selection with the closed row listed LAST and listed FIRST; the stored fraction chained from the base; case and blanks in the symbol; the window cut before chaining; a NaN return dropped and never seeding; an unknown symbol returning `[]` with no price read (use a mapping that records its lookups); the `DEMQUE_SOURCE` refusal; and, behind `pytest.importorskip("pyarrow")`, the S3 path with a fake `s3` client and in-memory parquet bytes for the index and one CUSIP.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR82-g-AC1" cell_refs="AR-g-82"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g8x_checks.py g82</invocation><expect>^AR-G82-OK</expect></criterion>

<criterion id="AR82-g-AC2" cell_refs="AR-g-82"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g8x_checks.py hygiene82</invocation><expect>^AR-G82-HYGIENE-OK</expect></criterion>

<expected_criteria>AR82-g-AC1,AR82-g-AC2</expected_criteria>

- AC1 imports `price_adapter_demque`, asks it 7 direct cases with hand-computed values (the contract above, item by item), then runs your test file (0 failed, at least 6 passed). At base it FAILs (no module).
- AC2 reads the module's bytes: ASCII only, top-level imports only the allowed standard library names and `tr_level`, nested imports only `pandas`, `pyarrow`, `yfinance`, `io`, `json`, `time`, no `open`, `print`, `exec`, `eval`. At base it FAILs (no module).

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS call, no HTTP, no installs. The module is NEW and imported by nothing yet; do not import it from any other file.
- **Refusal clause.** If a criterion cannot be met as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/price_adapter_demque.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_price_adapter_demque.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~182/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-82.demque-store-price-adapter.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R12_G.md</decomp_doc> round 12, workstream ~G, cell `AR-g-82`.
<owned_cells>AR-g-82</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR82-g-AC1, AR82-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~182/IRPT_ANLREQ.TO-AR-g-82.demque-store-price-adapter.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-82`.
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: commit the product files first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR82-g-AC1,AR82-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the module's function names with line numbers;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- the module is NEW and imported by nothing; the price chain's wiring cell (a later cut) is its first importer. Nothing deployed, so no edge is changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no permission change in this cell (the grant questions for the host are recorded in the decomposition and stay with the CTO and CloudOps).
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- read against the price-adapter facts record (q2, q4). Traps: a closed index row used (the symbol's history spliced from a retired CUSIP); the stored `total_return` read as a level; the first stored row (null) seeding a wrong base; the window applied after chaining; a read of every CUSIP instead of the symbol's one. The reference build passes all cases; a mutant that takes any row, not the open one, fails three cases.
</preflight>

- Cut on the AR-g-69 record (`q2`, `q4`) and CTO msg 8377. Risk WORLD: the floor of an infrastructure path; source and tests only, nothing deployed. Base: `AR82-g-AC1` and `AC2` FAIL as expected (no module).
- One of four independent adapter cells (`AR-g-81` to `AR-g-84`), each its own file pair; they share only `tr_level`.
