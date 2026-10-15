# TO-AR-g-51 -- C-PRICES, the chain core: one pure module that takes a list of symbols and answers each from the estate store, then Yahoo, then YCharts, labelled by source, cut at T-1, and never blocking

<to_id>IRPT_ANLREQ.TO-AR-g-51</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~170</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-51` (`decompositions/IRPT_ANLREQ_DECOMP_R7_G.md`) |
**outcome_ref:** FWD-7 (C-PRICES) | **depends_on:** none.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~170`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-170` (branch `wk-IRPT_ANLREQ-170`), provisioned by the issuer. Work only there.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~170 <0.9.0_WK_IRPT_ANLREQ~170@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W170-S<k>` (take the next free `<k>`); `surfaced_at` of any row = `date -u +%FT%TZ` at filing. Every `.py` you add passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax). No non-ASCII in what you add.
- No live call, NO PUSH, no deploy, no AWS call, no network, no install. Scratch outside the product tree.

### Read first (under `C:/dev/wk-irpt-anlreq-170/infra/aws/lambda/investor-reporting/ycharts/research/`)

- `held_data.py` (the module style: pure functions, readers passed in, no connection opened) and `tests/test_held_data.py` (the test style and fakes).

### THE CELL (`AR-g-51`, inlined)

The Opal report engine renders with most sections NOT_AVAILABLE because it has no price source. Andrew set the order in which a price is
looked for (CTO price ruling ADDENDUM 2, PRD v0.13): the estate's own stores first (already Opal's, so read, not called), then Yahoo
(yfinance), then YCharts through the stored session ONE symbol per call, and if all fail the report is generated without the security and
says so. This cell builds the CHAIN as one pure module. It reads no store and calls no vendor: the three tiers are functions passed in.
The adapters that make those functions (the estate store reader, the yfinance adapter, the YCharts adapter) are a later cell.

**Build a NEW file `infra/aws/lambda/investor-reporting/ycharts/research/price_source.py`** with exactly this contract.

1. `CHAIN = ("estate", "yfinance", "ycharts")`.
2. `resolve_prices(symbols, start, end, readers, as_of)`:
   - `symbols`: an iterable. Each entry that is a non-empty `str` is stripped and upper-cased; duplicates are dropped, first-seen order kept.
     An entry that is not a `str`, or is blank, is not looked up: it goes to `rejected` (a `str` entry as itself, any other as the
     type name, e.g. `"NoneType"`).
   - `start`, `end`, `as_of`: `str` dates `YYYY-MM-DD` (match `^[0-9]{4}-[0-9]{2}-[0-9]{2}$`). Anything else raises
     `ValueError("PRICE_WINDOW")`. `as_of` is the last date a row may carry (the caller passes T-1 from `lib/trading_calendar.py`).
   - `readers`: a `dict` keyed by tier name; a value is a callable `reader(symbol, start, end)` returning an iterable of `(date_str, price)`.
     Anything that is not a `dict` raises `ValueError("PRICE_READERS")`. A missing key is a tier that is absent, not an error.
3. **Per symbol, the tiers are tried in `CHAIN` order and the FIRST tier that answers with at least one usable row wins; later tiers are
   not called for that symbol.** Each tier is called at most once per symbol (so YCharts is one symbol per call, and only for a symbol the
   first two tiers could not price).
4. **Usable rows.** A row `(date, price)` is kept only if `date` is a `str` matching the date pattern and is `<= as_of`, and `price` is an
   `int` or `float` (not a `bool`), finite, and `> 0`. Every other row is dropped. Rows are returned ascending by date as
   `[date, float(price)]`; if a date repeats, the LATER value given by the reader is kept. A tier whose rows are all dropped, or which
   returned nothing, is a `NO_DATA` attempt and the chain goes on.
5. **A tier that raises** is the attempt outcome `"ERROR:" + type(exc).__name__`; the exception message is NEVER put in the result (it may
   hold a credential or a URL), and the chain goes on to the next tier. The function itself never raises for a data problem.
6. **Attempts.** Each symbol carries `attempts`, a list of `{"tier": name, "outcome": ...}` for the tiers actually considered, in order,
   `outcome` being one of `"DATA"`, `"NO_DATA"`, `"ERROR:<ExceptionClassName>"`, `"TIER_ABSENT"` (the key is missing from `readers`).
   Tiers after the winning tier are not listed.
7. **Result.** A `dict`:
   `{"as_of": as_of, "window": [start, end], "series": {SYMBOL: row, ...}, "missing": [sorted SYMBOLS with status MISSING],
   "sources_used": [sorted tier names that won at least once], "rejected": [...]}`
   where each `row` is `{"symbol", "status": "PRICED"|"MISSING", "source": tier|None, "rows": [[date, price], ...],
   "first_date": str|None, "last_date": str|None, "attempts": [...]}`. `series` keys are in first-seen order. A MISSING symbol has
   `source` None, `rows` `[]`, and both dates None. The report layer reads `missing` to say which securities it ran without.
8. **The module is pure and stdlib-only:** it imports nothing but `math`, `re`, `datetime`, `collections`, `typing` (and `__future__`);
   it opens no file, makes no connection, reads no environment variable, and has no `print`.

**Tests.** A NEW file `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_price_source.py` with at least 8 tests, offline,
using fake tier functions that record their calls: the order and early stop (later tiers uncalled), the empty-answer fall-through, the
raising tier (typed outcome, message absent from `json.dumps` of the result), all-tiers-empty is MISSING and listed, the T-1 cut (the
`as_of` row is kept, later rows dropped, and a tier whose only rows are later is NO_DATA), YCharts called once per lacking symbol and
never for a priced one, an absent tier, symbol normalisation and `rejected`, bad rows dropped, ascending order with a repeated date, and
the two typed refusals.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR51-g-AC1" cell_refs="AR-g-51"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g51_checks.py g51</invocation><expect>^AR-G51-OK</expect></criterion>

<criterion id="AR51-g-AC2" cell_refs="AR-g-51"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g51_checks.py hygiene</invocation><expect>^AR-G51-HYGIENE-OK</expect></criterion>

<expected_criteria>AR51-g-AC1,AR51-g-AC2</expected_criteria>

- AC1 imports `price_source`, asks `resolve_prices` twelve cases with fake tiers (the contract above, item by item), then runs your test file (0 failed, at least 8 passed). At base it FAILs (no module).
- AC2 reads the module's bytes: ASCII only, only the allowed imports, no `open`, `print`, `exec`, `eval`. At base it FAILs (no module).

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS call, no HTTP, no installs. Nothing outside the two new files, your deliverable folder, this order's status flip and the channel file is edited.
- **Refusal clause.** If a criterion cannot be met as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/price_source.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_price_source.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~170/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-51.price-source-chain-core.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R7_G.md</decomp_doc> round 7, workstream ~G, cell `AR-g-51`.
<owned_cells>AR-g-51</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR51-g-AC1, AR51-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~170/IRPT_ANLREQ.TO-AR-g-51.price-source-chain-core.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-51`.
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: commit the product files first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR51-g-AC1,AR51-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the module's function names with line numbers;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- the module is NEW and imported by nothing; the later compose cell is the first importer. Nothing deployed, so no edge is changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no permission change; the tiers are functions passed in.
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- read the cell against Andrew's chain (estate, Yahoo, YCharts one symbol per call, else without the security). Traps: a later tier called after an earlier one answered (a vendor call spent for nothing); YCharts batched; today's intraday row let through; an exception message with a credential in the result; a blank price treated as a price; the chain raising and so blocking the report ("it never blocks"). The checker feeds a green arm (a reference build passes all twelve cases) and a mutant arm (a `<= 0` relaxed to `< 0` fails case 9). NOT seen (blind): the real stores and vendors, which the adapter cell reads.
</preflight>

- Cut on CTO msg 8377 (ENGINE lane, `2.0.0_SA_COO~G2`), PRD v0.14 FWD-7 and the CTO price ruling ADDENDUM 2 (`CTO_RULING_DELL2_IRPT_ANLREQ_PRICE_SOURCES_AFTER_COVERAGE_READ_20261014.md`). Risk WORLD: the class the infrastructure path in `<paths>` implies (the gate floor); new source and tests only, nothing deployed or called.
- Base: `AR51-g-AC1` and `AC2` FAIL as expected (no module). The checker's green arm and mutant arm were run by the issuer before the cut (see the issuance commit).
- Ships to the host only in the single resident release (`AR-g-6x`, a later cell of this workstream); `price_source.py` must be added to the resident package's member list in that cell.
