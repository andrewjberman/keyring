# TO-AR-g-81 -- the Bloomberg history price adapter: the Opal ETFs' daily total return (percent) from the estate's Bloomberg partitions, chained to a base-100 level series

<to_id>IRPT_ANLREQ.TO-AR-g-81</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~181</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>12</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-81` (`decompositions/IRPT_ANLREQ_DECOMP_R12_G.md`) |
**outcome_ref:** FWD-7 (C-PRICES) | **depends_on:** `AR-g-80` (merged `f089142e91`, `tr_level.py`) and `AR-g-69` (merged `d1de2f0cd6`, the read that fixed the one formula).

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~181`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-181` (branch `wk-IRPT_ANLREQ-181`), provisioned by the issuer with the whole of `infra/`, `docs/` and `data/` on disk. Work only there.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~181 <0.9.0_WK_IRPT_ANLREQ~181@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W181-S<k>` (take the next free `<k>`); `surfaced_at` of any row = `date -u +%FT%TZ` at filing. Every `.py` you add passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax). No non-ASCII in what you add.
- No live call, NO PUSH, no deploy, no AWS call, no network, no install. Scratch outside the product tree. `pandas`, `pyarrow` and `yfinance` may be absent from this box: a test that needs one skips with `pytest.importorskip`, never fails.

### Read first (under `C:/dev/wk-irpt-anlreq-181/`)

- `infra/aws/lambda/investor-reporting/ycharts/research/tr_level.py` (merged; the ONE formula: `chain_levels(daily_returns, base=100.0)` and `returns_from_levels(pairs)`) and `infra/aws/lambda/investor-reporting/ycharts/research/price_source.py` (the chain core that will call your reader as `reader(symbol, start, end)`), with their tests under `infra/aws/lambda/investor-reporting/ycharts/research/tests/`.
- The facts record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~176/r9/PRICE_ADAPTER_FACTS.json`: `q2` (the formula for each source) and `q4` (the four adapter shapes).
- `data/mdpf/scripts/demque/tr_compare.py` (`load_bloomberg`: the union of `bbg/<day>/history_topup.parquet`, a later partition wins; the `frames=` test seam) and `data/mdpf/scripts/demque/tr_column.py` (`_bloomberg_returns`: percent divided by 100). These are NOT importable on the host; re-write the logic, do not import them.

### THE CELL (`AR-g-81`, inlined)

Andrew's rule: prices are TOTAL RETURN. The price chain (`price_source.resolve_prices`) asks each source for a level series through `reader(symbol, start, end)`; every reader hands back `(date_str, level)` on the same footing: `level = 100` at the first retained date and `level_t = level_(t-1) * (1 + r_t)` with `r_t` that source's DAILY total-return fraction, built by `tr_level`. This cell builds Bloomberg history adapter. It takes its client as an argument and makes no call at import.

**Build a NEW file `infra/aws/lambda/investor-reporting/ycharts/research/price_adapter_bbg.py`** with exactly this contract.

1. The module exposes `make_reader(s3, *, partitions=None)` and NO other public name. It returns `reader(symbol, start, end)`: `symbol` is any str (strip blanks, upper-case it); `start` and `end` are inclusive `YYYY-MM-DD` strings. The reader returns a list of `(date_str, level)` tuples, ascending by date, `level` a `float`, `[]` when the symbol has no usable row in the window.
2. The security for a symbol is `<SYM> US Equity`. Rows of any other security are ignored (never mixed in).
3. `partitions` is the test seam: a list of `(day_str, rows)` pairs, oldest first; `rows` is a list of dicts with the keys `date` (a `YYYY-MM-DD` str), `security`, `PX_LAST` and `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS` (Bloomberg's daily total return in PERCENT). A later partition's row for the same security and date REPLACES the earlier one, whatever its value.
4. Per row: the percent is usable only if it is an `int` or `float` (not a `bool`) and finite; the daily fraction is `percent / 100`. An unusable row is dropped and never seeds the base. Cut the usable rows to `start <= date <= end` FIRST, then call `tr_level.chain_levels(rows)` (`import tr_level`, a bare import, as `layout_overview.py` imports `held_data`) and return its pairs as tuples. `PX_LAST` is never used for the level.
5. When `partitions` is `None` the reader reads S3 through the injected `s3` client, once per reader (cache the result in the closure): `list_objects_v2(Bucket="opal-data-etfs", Prefix="bbg/")` following `ContinuationToken` while `IsTruncated`; every key ending `/history_topup.parquet`, ascending by key; `day = key.split("/")[1]`; `get_object(Bucket=..., Key=...)["Body"].read()`; the bytes go through `pyarrow.parquet.read_table(io.BytesIO(raw), columns=[the four names above]).to_pylist()`. `pyarrow` and `io` are imported INSIDE that function only (pyarrow is not installed in the tests or on the host today). A `date` value that is not a str is normalised with `.isoformat()[:10]` when it has `isoformat`, else `str(value)[:10]`.
6. When `partitions` is `None` and `s3` is `None`, the FIRST call of the reader raises `ValueError("BBG_SOURCE")` (the chain types it). No other exception is caught or invented.
7. The module is stdlib-only at the top level (`__future__`, `math`, `re`, `datetime`, `collections`, `typing` and `tr_level`); it opens no file, prints nothing, reads no environment variable, makes no connection of its own (the client is passed in).

**Tests.** A NEW file `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_price_adapter_bbg.py` with at least 6 tests, offline, with hand-computed values (made-up dates and numbers): the percent / 100 chain from the base; case and blanks in the symbol; the window cut before chaining; another security not mixed in; an unknown symbol returns `[]`; a later partition winning for the same security and date; null and NaN percents never seeding the base; the `BBG_SOURCE` refusal; and, behind `pytest.importorskip("pyarrow")`, the S3 path with a fake `s3` client (one list page that is truncated and one that is not, two partitions, a `history_topup.parquet` built in memory with pyarrow).

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR81-g-AC1" cell_refs="AR-g-81"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g8x_checks.py g81</invocation><expect>^AR-G81-OK</expect></criterion>

<criterion id="AR81-g-AC2" cell_refs="AR-g-81"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g8x_checks.py hygiene81</invocation><expect>^AR-G81-HYGIENE-OK</expect></criterion>

<expected_criteria>AR81-g-AC1,AR81-g-AC2</expected_criteria>

- AC1 imports `price_adapter_bbg`, asks it 8 direct cases with hand-computed values (the contract above, item by item), then runs your test file (0 failed, at least 6 passed). At base it FAILs (no module).
- AC2 reads the module's bytes: ASCII only, top-level imports only the allowed standard library names and `tr_level`, nested imports only `pandas`, `pyarrow`, `yfinance`, `io`, `json`, `time`, no `open`, `print`, `exec`, `eval`. At base it FAILs (no module).

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS call, no HTTP, no installs. The module is NEW and imported by nothing yet; do not import it from any other file.
- **Refusal clause.** If a criterion cannot be met as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/price_adapter_bbg.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_price_adapter_bbg.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~181/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-81.bloomberg-history-price-adapter.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R12_G.md</decomp_doc> round 12, workstream ~G, cell `AR-g-81`.
<owned_cells>AR-g-81</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR81-g-AC1, AR81-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~181/IRPT_ANLREQ.TO-AR-g-81.bloomberg-history-price-adapter.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-81`.
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: commit the product files first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR81-g-AC1,AR81-g-AC2` BEFORE the flip to complete.
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
comp-adversary: RUN -- read against the price-adapter facts record (q2, q4). Traps: the percent used as a fraction (a 1.0 percent day read as +100 percent); PX_LAST used as the level; the window applied after chaining (the base moves); a later partition ignored; another security's rows chained in; a null seeding the base. The checker feeds a green arm (a reference build passes all cases) and mutant arms (no `/ 100` fails six cases).
</preflight>

- Cut on the AR-g-69 record (`q2`, `q4`) and CTO msg 8377. Risk WORLD: the floor of an infrastructure path; source and tests only, nothing deployed. Base: `AR81-g-AC1` and `AC2` FAIL as expected (no module).
- One of four independent adapter cells (`AR-g-81` to `AR-g-84`), each its own file pair; they share only `tr_level`.
