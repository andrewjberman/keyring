# TO-AR-g-69 -- the price adapters' facts: a READ of the YCharts per-symbol call pattern, the one total-return formula across the estate stores and Yahoo, what the resident host can run, and the four adapters' signatures; READ ONLY, one record, no source change

<to_id>IRPT_ANLREQ.TO-AR-g-69</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~176</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-69` (`decompositions/IRPT_ANLREQ_DECOMP_R9_G.md`) |
**outcome_ref:** FWD-7 (C-PRICES) | **depends_on:** none.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~176`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-176` (branch `wk-IRPT_ANLREQ-176`), provisioned by the issuer. Work only there. The checkout is sparse; the folders this order names are on disk. If a path you must read is absent, say so under `not_read` and go on; do not stop.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~176 <0.9.0_WK_IRPT_ANLREQ~176@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W176-S<k>` (take the next free `<k>`); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- No live call, NO PUSH, no AWS call of any kind, NO edit of any source file. Scratch outside the product tree. Use the native Grep, Glob and Read tools; a recursive shell grep over the repo is denied by a hook.

### THE CELL (`AR-g-69`, inlined) -- a READ. The product tree is not edited.

*Context.* The report engine will look for a price in the order Andrew set (CTO price ruling ADDENDUM 2 and 3, PRD v0.14): the estate's own stores (MDPF_DEMQUE's Yahoo
price store, the Opal ETFs' Bloomberg history), then Yahoo (yfinance), then YCharts one symbol per call, then the replacement rule, else the report runs without the security.
The chain core (`ycharts/research/price_source.py`) takes four reader functions, `reader(symbol, start, end)` returning `(date_str, price)` rows. The issuer must cut the four
adapters that make them. The engine compose read (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~173/r7/ENGINE_COMPOSE_READ.json`, read q2 first) found the
two estate stores' layouts. What is still unknown is below. Andrew's rule (record `org/tier1_exec/2.0.0_SA_COO~Q1/deliverables/ANDREW_DIRECT_20261009_054xZ_PRICES_ARE_TOTAL_RETURN_STORE_PRICE_DIVIDEND_TR_PER_DAY.md`):
prices are TOTAL RETURN: a store's price plus its dividend total return per day.

Answer these four questions from SOURCE, each with `{file, line, text}` evidence read from the worktree (print the lines you cite; a line you did not read is not cited):

1. **Q1, the YCharts per-symbol call.** The CTO ruled (price ruling ADDENDUM 1) that YCharts is reached "through the long-term trust token's EC2-crawl / Lambda REST pattern, ONE symbol per call"
   (the CRO measured it: `fund_data` 200 in 0.1-0.5 s, about 2.3 s per symbol at a 2 s client spacing, 5 years per symbol; CRO notes in
   `org/tier1_exec/4.0.0_SA_CRO/deliverables/`, search for "trust token" and "fund_data"). Find in source and in those notes: the `pattern` (which component
   makes the call), `secret_name` (the NAME of the secret holding the token, never its value), `endpoint_form` (the shape of the URL or function name, never a host typed from memory),
   `call_shape` (the request and the response fields), `pacing` (the spacing and any rate limit), `series_fields` (which response fields hold the dated series and their units), and
   `resident_can_call_today` (yes / no / unknown: does the resident host role hold the secret read and the egress for it; cite the tracked IAM). Each of these strings says `not found` plainly when it is.
2. **Q2, the one total-return formula.** For each of the three price sources (`demque` = MDPF_DEMQUE's store, `bbg` = the Opal ETFs' Bloomberg history, `yfinance`) as a row
   `{source, field_used, level_formula, basis_claim, evidence}`: the field that carries the total return (the DEMQUE `total_return` column, the Bloomberg
   `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS` in percent, Yahoo's adjusted close or close plus dividends), whether each is a daily return or a cumulative level, and the formula that turns it into a `[date, level]`
   series (e.g. `level_t = level_(t-1) * (1 + r_t/100)` from a base of 100). Read the estate's own consumers to see how it is done there (`data/mdpf/scripts/demque/tr_column.py`,
   `tr_compare.py`, and any reader of `total_return`). Then `one_formula`: the single rule the adapters should share so every source yields a total-return level series on the same
   footing, and `basis_claim` per row says `measured` (you read it in code) or `inferred`.
3. **Q3, what the resident host can run.** `python_version`, whether `yfinance`, `pandas` and `pyarrow` are on the resident host or in its package (read the resident package builder
   `reports/build_resident_package.py`, any requirements file or install script for the host under `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/` and `infra/`), and `t1_source`: how the
   resident would obtain T-1 (`lib/trading_calendar.py` `prev_trading_day` / `expected_last_trading_day`; whether `lib/` ships in the resident tarball). Say `not found` plainly where it is.
4. **Q4, the adapters.** `adapters`: four rows for `estate_bbg`, `demque`, `yfinance`, `ycharts`, each `{name, reader_signature, injected, builds_on}`: the function the adapter module would
   expose (its parameters beyond `symbol, start, end`), the clients it takes as injected arguments (S3 client, a yfinance module, an http function, a secret reader) so it can be
   tested with fakes, and the existing code it builds on (file and function). Then `cells`: the BUILD cells for the adapters, each `{id: "AR-g-8<k>", summary, files, ...}`, with write sets
   that do not overlap and a note of any IAM or host change each needs (those are CloudOps acts under a pair, not worker cells).

### Deliverable and ACCEPTANCE

Write `C:/dev/wk-irpt-anlreq-176/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~176/r9/PRICE_ADAPTER_FACTS.json` with these keys:

- `base` (the sha your branch started from), `cell` (`"AR-g-69"`), `not_read` (a list of strings: what you did not read and why).
- `q1`: `{"pattern": str, "secret_name": str, "endpoint_form": str, "call_shape": str, "pacing": str, "series_fields": str, "resident_can_call_today": str, "evidence": [cite, ...]}`.
- `q2`: `{"sources": [{"source": str, "field_used": str, "level_formula": str, "basis_claim": str, "evidence": [cite, ...]}, ... (at least 3)], "one_formula": str}`.
- `q3`: `{"python_version": str, "yfinance_on_host": str, "pandas_on_host": str, "pyarrow_on_host": str, "t1_source": str, "evidence": [cite, ...]}`.
- `q4`: `{"adapters": [{"name": str, "reader_signature": str, "injected": [str, ...], "builds_on": str}, ... (at least 4)], "cells": [{"id": str, "summary": str, "files": [str, ...]}, ...]}`.
- A `cite` is `{"file": "<path under the repo root, forward slashes>", "line": <int>, "text": "<a substring of that line>"}`.

<criterion id="AR69-g-AC1" cell_refs="AR-g-69"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g_read_checks.py shape69 org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~176/r9/PRICE_ADAPTER_FACTS.json</invocation><expect>^SHAPE-OK </expect></criterion>

<criterion id="AR69-g-AC2" cell_refs="AR-g-69"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g_read_checks.py cite org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~176/r9/PRICE_ADAPTER_FACTS.json</invocation><expect>^CITES-OK </expect></criterion>

<criterion id="AR69-g-AC3J" cell_refs="AR-g-69" judgment="true"/>
`AR69-g-AC3J` (judgment, graded at L9, never by you): the answers follow from the cited lines, a "not found" is said plainly with what was searched, the one formula is stated once and is consistent with Andrew's total-return rule, and the adapter cells have non-overlapping write sets.

<expected_criteria>AR69-g-AC1 AR69-g-AC2 AR69-g-AC3J</expected_criteria>

- AC1 loads the record and prints `SHAPE-OK` only when every key and evidence list above is present; otherwise `SHAPE-BAD <why>`. At base it FAILs (no record).
- AC2 re-opens every cite in the record (the denominator is printed) and prints `CITES-OK <n> of <n>` only when each cited line exists and the cited text is a substring of it. At base it FAILs (no record).

## BOUNDS

- **Grant:** exactly the `<paths>` below. You edit NO source file; the product tree is READ ONLY.
- If a cited file does not exist at the path named, find the file that now holds the function (a name search), cite that, and say so in the record.
- Rows: APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~176/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-69.price-adapter-facts-read.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R9_G.md</decomp_doc> round 9, workstream ~G, cell `AR-g-69`.
<owned_cells>AR-g-69</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR69-g-AC1, AR69-g-AC2, AR69-g-AC3J. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~176/IRPT_ANLREQ.TO-AR-g-69.price-adapter-facts-read.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-69`.
- The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: commit the record first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate AFTER its commit with `python .tools/proof-of-spec-check.py <instance> "AR69-g-AC1,AR69-g-AC2,AR69-g-AC3J"`; flip `<status>` to `complete` only when it prints VALID.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~136/IRPT_ANLREQ.TO-AR-y-328.resident-release-bindings-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):** each criterion's output lines; the one formula in one sentence; the adapter cells in one line each; commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read of source and one record; nothing is changed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by reading the cell against the answer shape. Traps: a total-return series built as a price series (Andrew's rule: total return); a daily return read as a cumulative level; a secret value copied into the record (the NAME only); a host typed from memory; a library assumed present on the host because it is installed on this machine; a store assumed readable. NOT seen (blind): the live host, the live secret and the live stores; denominator: 4 questions, each answered with cited lines.
</preflight>

- Cut on CTO msg 8377 (ENGINE lane) and the engine compose read (AR-g-54, q2). Risk LOCAL: the cell reads source and notes and writes one record. Base: `AR69-g-AC1` and `AC2` FAIL as expected (no record).
- Its output decides the adapter build cells and the host and IAM changes they need; nothing is changed by this cell.
