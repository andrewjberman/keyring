# TO-AR-g-99 -- the Yahoo history port for the swap pass: days of history per candidate, fetched in batches, a failed request never read as "unpriced"

<to_id>IRPT_ANLREQ.TO-AR-g-99</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~200</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>23</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-99` (`decompositions/IRPT_ANLREQ_DECOMP_R23_G.md`) |
**outcome_ref:** FWD-2 (C-SWAP step 4: "the longest Yahoo history wins"; CTO msg 8711: the r34 packet states the swap's Yahoo calls per holding and their bound) | **depends_on:** `AR-g-52` (`swap_replacement.py`, merged). Parallel to `AR-g-98` (no shared file).

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~200`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-200` (branch `wk-IRPT_ANLREQ-200`), provisioned by the issuer with the whole of `infra/`, `docs/`, `data/`, `lib/` and `org/missions/D9/IRPT` on disk. Work only there.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~200 <0.9.0_WK_IRPT_ANLREQ~200@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W200-S<k>` (take the next free `<k>`; check the channel file for `W200` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing. Every `.py` you add passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax). No non-ASCII in what you add.
- No live call, NO PUSH, no deploy, no AWS call, no network, no install, and NO `import yfinance` that runs in a test. Scratch outside the product tree.
- Run each test file ON ITS OWN (`python -m pytest -q <one file>`).

### Read first (under `C:/dev/wk-irpt-anlreq-200/infra/aws/lambda/investor-reporting/ycharts/research/`)

- `swap_replacement.py` (`choose_replacement` calls `history_days(ticker)` once per candidate and treats an int above 0 as a priced candidate, `None` as NOT_PRICED_BY_YAHOO, and an exception as HISTORY_ERROR); `price_adapter_yfinance.py` (its idiom: an injectable `fetch` and `yf`, the real `yfinance` imported only inside the default); `tests/test_price_adapter_yfinance.py` (the style of your tests: fakes only).

### THE CELL (`AR-g-99`, inlined)

ONE NEW module `yahoo_history_days.py` in `ycharts/research/`, stdlib only, no output, no clock, no environment read, no `import yfinance` at module top.
- `DEFAULT_CHUNK = 50`.
- `days_of(dates)` -> the number of days from the first to the last of the usable dates (`(last - first).days`, so `["2020-01-01", "2020-01-31"]` is 30), or `None` when fewer than two DISTINCT usable dates exist. A usable date is a value whose first ten characters read as an ISO `YYYY-MM-DD` date (so a timestamp string counts, by its date); anything else is ignored; the input may be unordered, repeated, empty or `None`.
- `make_history_days(download=None, yf=None, chunk=DEFAULT_CHUNK)` returns an object that is a `history_days(ticker)` callable AND has `prefetch(tickers)` and a `calls` integer (the number of `download` requests made so far, failed ones included). `chunk` must be a positive int and not a bool, else `ValueError`.
  - `prefetch(tickers)`: the not-yet-fetched tickers, de-duplicated in first-seen order, are asked `chunk` at a time (`download(list_of_tickers)`); each request that raises is skipped without being recorded (so those tickers are later asked one at a time and the failure surfaces then); the other chunks still run. After a request, each asked ticker's value is `days_of(answer.get(ticker))` (a ticker the answer omits, or lists with fewer than two usable dates, is `None`: Yahoo does not price it). A fetched ticker is never fetched again.
  - `__call__(ticker)`: a ticker not yet fetched is asked ALONE in one request; that request's exception PROPAGATES (a failed request must never read as an unpriced ticker); the answer is cached.
  - `download(tickers)` -> `{ticker: [ISO date strings of its observations]}`. The default one (used when `download` is None) calls `yf.download(list(tickers), period="max", interval="1mo", auto_adjust=False, progress=False, group_by="ticker", threads=True)` where `yf` is the injected module or, when None, `import yfinance` done INSIDE that function; for each ticker it reads `frame[ticker]["Close"].dropna()` (a `KeyError` or `TypeError` skips the ticker) and returns that column's index as `YYYY-MM-DD` strings (`strftime` when the index value has it, else `str(value)[:10]`). A month with no Close is not an observation.

**Tests (offline).** NEW `tests/test_yahoo_history_days.py` with these exact test function names (the checker looks for each by name): `test_days_of_counts_the_span_and_needs_two_dates`, `test_prefetch_batches_the_tickers_in_chunks_and_counts_the_requests`, `test_a_ticker_the_answer_omits_or_leaves_empty_answers_none`, `test_a_failed_request_raises_for_the_ticker_and_prefetch_tolerates_it`, `test_the_default_download_reads_each_tickers_close_from_a_frame` (a fake `yf` object whose `download` records its arguments and returns a fake frame; a fake Series with `dropna()` and `index`), `test_a_chunk_must_be_a_positive_int` (parametrized: 0, -1, True, 2.5, "3").

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR99-g-AC1" cell_refs="AR-g-99"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g99_checks.py g99</invocation><expect>^AR-G99-OK</expect></criterion>

<criterion id="AR99-g-AC2" cell_refs="AR-g-99"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g99_checks.py regress</invocation><expect>^AR-G99-REGRESS-OK</expect></criterion>

<expected_criteria>AR99-g-AC1,AR99-g-AC2</expected_criteria>

- AC1 asks the module 25 things on fakes (the span rule and its edge inputs, batching and the request count, no refetch, an unfetched ticker asked alone once, omitted and empty tickers, a failed request raising and prefetch tolerating it, the chunk guard, the default download's exact arguments and Close reading including empty months at the edges, use as the history port of `choose_replacement`, no top-level yfinance import, hygiene), then checks your six named tests exist and pass. At base it FAILs.
- AC2 runs three existing test files one at a time (51 tests) and needs all of them to pass, and it needs your branch (against the merge-base with `box/dell2`) to change only your two files, your folder, your order and the channel file. At base it PASSes. Run it under `timeout 590`.

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS call, no HTTP, no installs.
- **Refusal clause.** If a criterion cannot be met as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/yahoo_history_days.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_yahoo_history_days.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~200/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-99.yahoo-history-days-port.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R23_G.md</decomp_doc> round 23, workstream ~G, cell `AR-g-99`.
<owned_cells>AR-g-99</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR99-g-AC1, AR99-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~200/IRPT_ANLREQ.TO-AR-g-99.yahoo-history-days-port.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-99`.
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put the `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder (use `kind` `test` for a test file): commit the product files first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR99-g-AC1,AR99-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the files you added with their line counts;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- one NEW module and its tests; nothing imports it yet (`AR-g-100` wires it), so no deployed or resident byte changes and no behaviour moves. At the wiring it is the only Yahoo caller of the swap: one request per `chunk` candidates per swapped holding (ceil(class size / 50)), stated by `build_swap_pool.py`'s summary line (`AR-g-98`) and in the r34 packet.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- read against PRD C-SWAP step 4, `swap_replacement.py` and the yfinance adapter's idiom. Traps: a failed request cached or returned as "no history" (the choice would then read a Yahoo outage as an unpriced class and leave a holding out silently); a chunk request that fails dropping the other chunks; a repeated ticker asked twice; an empty month counted as an observation (a span too long); `import yfinance` at the top (the resident would need it to import the module); a bool chunk. The default download cannot be run here (no network): its exact arguments and its reading of a fake frame are pinned, and its first real run is the r34 apply's one-ticker smoke read. The checker feeds a green arm (a reference build passes the 25 cases, the six named tests and the 51 regress tests) and 14 mutant arms, each of which fails the check.
</preflight>

- Cut on CTO msg 8711 and the issuer's reference build in a scratch tree. Risk WORLD: the floor of an infrastructure path; new source and tests only, nothing deployed. Base: `AR99-g-AC1` FAILs and `AR99-g-AC2` PASSes (51), as expected.
- NOT claimed: that `yf.download` with `group_by="ticker"` returns the frame shape the default reads for every ticker count (a single-ticker request may shape its columns differently: the first real read at the r34 apply measures it, and a mis-shaped read yields `None`, never a wrong number).
