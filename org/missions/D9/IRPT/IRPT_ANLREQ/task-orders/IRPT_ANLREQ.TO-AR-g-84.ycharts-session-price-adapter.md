# TO-AR-g-84 -- the YCharts price adapter: one fund_data call per symbol over the resident session transport, the served cumulative level turned into a base-100 total-return series

<to_id>IRPT_ANLREQ.TO-AR-g-84</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~184</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>12</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-84` (`decompositions/IRPT_ANLREQ_DECOMP_R12_G.md`) |
**outcome_ref:** FWD-7 (C-PRICES) | **depends_on:** `AR-g-80` (merged `f089142e91`, `tr_level.py`) and `AR-g-69` (merged `d1de2f0cd6`, the read that fixed the one formula).

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~184`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-184` (branch `wk-IRPT_ANLREQ-184`), provisioned by the issuer with the whole of `infra/`, `docs/` and `data/` on disk. Work only there.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~184 <0.9.0_WK_IRPT_ANLREQ~184@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W184-S<k>` (take the next free `<k>`); `surfaced_at` of any row = `date -u +%FT%TZ` at filing. Every `.py` you add passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax). No non-ASCII in what you add.
- No live call, NO PUSH, no deploy, no AWS call, no network, no install. Scratch outside the product tree. `pandas`, `pyarrow` and `yfinance` may be absent from this box: a test that needs one skips with `pytest.importorskip`, never fails.

### Read first (under `C:/dev/wk-irpt-anlreq-184/`)

- `infra/aws/lambda/investor-reporting/ycharts/research/tr_level.py` (merged; the ONE formula: `chain_levels(daily_returns, base=100.0)` and `returns_from_levels(pairs)`) and `infra/aws/lambda/investor-reporting/ycharts/research/price_source.py` (the chain core that will call your reader as `reader(symbol, start, end)`), with their tests under `infra/aws/lambda/investor-reporting/ycharts/research/tests/`.
- The facts record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~176/r9/PRICE_ADAPTER_FACTS.json`: `q2` (the formula for each source) and `q4` (the four adapter shapes).
- `infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py` (`BENCHMARK_FIELD` line 62 and `_series_points` line 386: the served `chart_data[0][0].raw_data` list of `[epoch_ms, level]` pairs) and `infra/aws/lambda/investor-reporting/ycharts/session/resident_session.py` (the transport the production wiring will pass in; this cell never calls it).
- The CRO's measured call shape: path `/charts/fund_data.json`, params `securities` = `id:<SYM>,include:true,` and `zoom` = `max`, one symbol per call, about 0.1 to 0.5 s per call (`org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261014_ANALYSIS_REPORT_PRICE_COVERAGE.md` around line 128).

### THE CELL (`AR-g-84`, inlined)

Andrew's rule: prices are TOTAL RETURN. The price chain (`price_source.resolve_prices`) asks each source for a level series through `reader(symbol, start, end)`; every reader hands back `(date_str, level)` on the same footing: `level = 100` at the first retained date and `level_t = level_(t-1) * (1 + r_t)` with `r_t` that source's DAILY total-return fraction, built by `tr_level`. This cell builds YCharts session adapter. It takes its client as an argument and makes no call at import.

**Build a NEW file `infra/aws/lambda/investor-reporting/ycharts/research/price_adapter_ycharts.py`** with exactly this contract.

1. The module exposes `make_reader(transport, *, spacing_s=2.0, sleep=None)` and NO other public name. It returns `reader(symbol, start, end)`: `symbol` is any str (strip blanks, upper-case it); `start` and `end` are inclusive `YYYY-MM-DD` strings. The reader returns a list of `(date_str, level)` tuples, ascending by date, `level` a `float`; `[]` when the symbol is blank or the answer holds no usable point in the window.
2. `transport(path, params)` returns the parsed JSON answer. The reader makes ONE call per reader call, with `path == "/charts/fund_data.json"` and `params == {"securities": "id:<SYM>,include:true,", "zoom": "max"}` (no other key). A blank symbol makes no call.
3. Pacing: the FIRST call of a reader sleeps nothing; every later call first calls `sleep(spacing_s)` once (`sleep` defaults to `time.sleep`, imported at the top level). Pacing is per reader, held in the closure.
4. The points are `answer["chart_data"][0][0]["raw_data"]`, a list of `[epoch_ms, level]` pairs. Any missing key, wrong type or short list is a malformed answer: return `[]` (no exception). `epoch_ms` becomes a UTC calendar date `YYYY-MM-DD` (days since 1970-01-01 = `epoch_ms // 86400000`). A point is usable only if `level` is a finite number above zero (not a `bool`).
5. Cut the usable points to `start <= date <= end` FIRST. The served `level` is a CUMULATIVE level, not a return: take `tr_level.returns_from_levels(points)`, put the first usable date in front with `r = 0.0`, and call `tr_level.chain_levels` (`import tr_level`, a bare import), so the first usable date is level 100.0 and each later date is `level_t / level_(t-1)` of the served series. Return the pairs as tuples. A single usable point returns `[(date, 100.0)]`.
6. A transport error propagates unchanged (the chain types it); nothing is caught or invented, and no error text is stored or logged. No secret, credential or session id is read, named or stored in this module.
7. The module is stdlib-only at the top level (`__future__`, `math`, `re`, `datetime`, `time`, `collections`, `typing` and `tr_level`); it opens no file, prints nothing, reads no environment variable.

**Tests.** A NEW file `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_price_adapter_ycharts.py` with at least 6 tests, offline, with hand-computed values (made-up dates and numbers): the served levels becoming a base-100 series with the first row seeding; one call per symbol with the exact path and params; no sleep before the first call and one `sleep(2.0)` before the second; the window cut before chaining; a blank symbol returning `[]` with no call; a malformed answer returning `[]`; a zero or negative level dropped; a single usable point returning `[(date, 100.0)]`; and a transport error propagating.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR84-g-AC1" cell_refs="AR-g-84"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g8x_checks.py g84</invocation><expect>^AR-G84-OK</expect></criterion>

<criterion id="AR84-g-AC2" cell_refs="AR-g-84"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g8x_checks.py hygiene84</invocation><expect>^AR-G84-HYGIENE-OK</expect></criterion>

<expected_criteria>AR84-g-AC1,AR84-g-AC2</expected_criteria>

- AC1 imports `price_adapter_ycharts`, asks it 8 direct cases with hand-computed values (the contract above, item by item), then runs your test file (0 failed, at least 6 passed). At base it FAILs (no module).
- AC2 reads the module's bytes: ASCII only, top-level imports only the allowed standard library names and `tr_level`, nested imports only `pandas`, `pyarrow`, `yfinance`, `io`, `json`, `time`, no `open`, `print`, `exec`, `eval`. At base it FAILs (no module).

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS call, no HTTP, no installs. The module is NEW and imported by nothing yet; do not import it from any other file.
- **Refusal clause.** If a criterion cannot be met as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/price_adapter_ycharts.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_price_adapter_ycharts.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~184/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-84.ycharts-session-price-adapter.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R12_G.md</decomp_doc> round 12, workstream ~G, cell `AR-g-84`.
<owned_cells>AR-g-84</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR84-g-AC1, AR84-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~184/IRPT_ANLREQ.TO-AR-g-84.ycharts-session-price-adapter.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-84`.
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: commit the product files first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR84-g-AC1,AR84-g-AC2` BEFORE the flip to complete.
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
comp-adversary: RUN -- read against the price-adapter facts record (q2, q4). Traps: the served level used as the price; sleeping before the first call; a call per date instead of per symbol; the window applied after the returns (the base moves); a malformed answer raising into the chain; a secret read in the adapter. The reference build passes all cases; a mutant that sleeps before the first call fails two.
</preflight>

- Cut on the AR-g-69 record (`q2`, `q4`) and CTO msg 8377. Risk WORLD: the floor of an infrastructure path; source and tests only, nothing deployed. Base: `AR84-g-AC1` and `AC2` FAIL as expected (no module).
- One of four independent adapter cells (`AR-g-81` to `AR-g-84`), each its own file pair; they share only `tr_level`.
