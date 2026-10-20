# TO-AR-g-171 -- the Opal model data reader (K1) and the committed model-code map

<to_id>IRPT_ANLREQ.TO-AR-g-171</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~330</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>60</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-171` (`decompositions/IRPT_ANLREQ_DECOMP_R60_G.md`) |
**outcome_ref:** FWD-10 (PRD v0.25 @b83ce81b5b, C-MODEL-SOURCE; CTO msg 11442, ruling R1) | **depends_on:** none (first of chain A). Nothing is deployed by this cell.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~330`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-330` (branch `wk-IRPT_ANLREQ-330`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~330 <0.9.0_WK_IRPT_ANLREQ~330@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W330-S<k>` (check the channel file for `W330` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- Python 3.9 syntax, ruff clean, ASCII only. Run tests with plain `python -m pytest --color=no -q -p no:cacheprovider` (the producer's tests need `pypdf`, which `python -I` cannot see). Do not touch anything outside the `<paths>` block. Do NOT run `git sparse-checkout`.
- **You are the one worker of chain A (queue 171, 173, 174, 175, in that order).** The commits of your earlier orders are on this branch and their files are in this worktree; a later order builds on them. You are handed one order at a time.
- **The checker** is `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_compare_checks.py` (read it; you cannot edit it). It builds its own deterministic fixtures and computes every expected number itself, independent of your code: if your number and the checker's differ, re-read the cell text before you doubt the checker, and if you still believe the checker is wrong file a BLOCKING row quoting both numbers, and stop on that criterion.

### THE CELL (`AR-g-171`, inlined)

Directory `RES` = `infra/aws/lambda/investor-reporting/ycharts/research/`; `TESTS` = its `tests/` folder. Create three files; edit nothing else.

**Why.** FWD-10 compares the portfolio with Opal models. The models' returns and current allocation live in two firm-neutral objects of the bucket `opal-data-portal-v2` (PRD C-MODEL-SOURCE; CTO ruling R1). The issuer read both on 2026-10-20 (you have no AWS access and need none: your module takes its bytes from an injected function). Measured shapes:
- `json/benchmarks/model_portfolio_timeseries.json` (plain JSON): top-level keys `generated_at`, `data_as_of` ("2026-10-19"), `inception_date` ("2024-04-30"), `rfr_tenors`, `series_note`, `timeseries`. `timeseries` is a list of 3,225 rows, one per day per model: `{"date": "2024-04-30", "model_code": "INT", "model_return": -0.009261, "benchmark_return": ..., "index_benchmark_return": ..., "etf_benchmark_return": ..., "rfr": 0.00018712}`. Model codes: UST, ST, INT, LT, ULT. `model_return` is that day's simple return.
- `json/positioning/positioning_data.json` (**gzip-compressed JSON**: the bytes start 0x1f 0x8b): top-level keys `generated_at`, `data_as_of` ("2026-10-19"), `note`, `benchmarks`, `portfolios`, `current_holdings`, `data_date`. `portfolios.<code>.allocation` = `{"cash": 0, "fixed_income": 100.0, "equity": 0, "hedge": 0, "structured": 0, "commodities": 0, "alternatives": 0}` (percent numbers) for each of the five codes.

**1. `RES/model_source.py`** (stdlib only: json, gzip, datetime, pathlib; no boto3, no network, no clock). Module docstring cites PRD C-MODEL-SOURCE and the CTO ruling R1. It defines exactly:
- `BUCKET = "opal-data-portal-v2"`, `SERIES_KEY = "json/benchmarks/model_portfolio_timeseries.json"`, `POSITIONING_KEY = "json/positioning/positioning_data.json"`, `CODES = ("UST", "ST", "INT", "LT", "ULT")`.
- `class ModelSourceRefused(ValueError)`.
- `code_for_key(catalogue_key)` -> the model code or `None`. It reads `model_code_map.json` (next to the module, loaded once) and matches the catalogue KEY exactly (`opal_long_term` -> `LT`). Anything else (a display name, a ticker, `""`, `None`) -> `None`. There is NO display-name matching.
- `read_series(get_bytes)` -> `{"as_of": data_as_of, "inception": inception_date, "series": {code: [[epoch_ms, level], ...]}}`. `get_bytes(key)` returns the object's bytes. Detect gzip by the magic bytes 0x1f 0x8b and decompress; decode UTF-8 JSON. Per model code, take its rows sorted by date. The level is `100.0` on that code's FIRST date (the first row's own `model_return` is NOT applied: it is the return into the base day), and every later row multiplies the level by `1 + model_return`. `epoch_ms` is that date at 00:00 UTC in milliseconds (an int). Only the codes present are returned.
- `read_allocation(get_bytes)` -> `{"as_of": data_as_of, "allocation": {code: {"Cash": pct, "Fixed Income": pct, "Equity": pct, "Hedge": pct, "Structured": pct, "Commodities": pct, "Alternatives": pct}}}`: the seven keys of `portfolios.<code>.allocation` renamed (`cash`->`Cash`, `fixed_income`->`Fixed Income`, `equity`->`Equity`, `hedge`->`Hedge`, `structured`->`Structured`, `commodities`->`Commodities`, `alternatives`->`Alternatives`), the values unchanged. The input may be gzip or plain JSON (same detection).
- Every failure raises `ModelSourceRefused` with a short reason and never anything else: `get_bytes` raising (KeyError, OSError, anything), a body that is not JSON, a missing or mistyped `timeseries` / `portfolios` / `data_as_of` / `inception_date`, a row with a non-date `date`, a non-finite `model_return` or a missing `model_code`, an allocation with a key outside the seven, a non-number weight, and no usable series at all.

**2. `RES/model_code_map.json`** (committed contract artifact, the only place the code map is written): `{"schema": "irpt-model-code-map-v1", "codes": {"UST": {"catalogue_key": "opal_ultra_short_term", "label": "Opal Ultra Short-Term"}, "ST": {"catalogue_key": "opal_short_term", "label": "Opal Short-Term"}, "INT": {"catalogue_key": "opal_intermediate_term", "label": "Opal Intermediate-Term"}, "LT": {"catalogue_key": "opal_long_term", "label": "Opal Long-Term"}, "ULT": {"catalogue_key": "opal_ultra_long_term", "label": "Opal Ultra Long-Term"}}}` (UTF-8, LF, two-space indent, sorted as above). These are exactly the five `key` / `label` pairs of `infra/aws/lambda/investor-reporting/ycharts/generate/templates.json` `comparison_catalog.entries` (read it to confirm).

**3. `TESTS/test_model_source.py`** (pytest, your own proof; offline; `sys.path` the research directory like the sibling tests do): the level rule on a small hand-made series including the ignored first return; ms are UTC midnights; gzip and plain both read; the seven renames; each refusal above; `code_for_key` on the five keys, a display name, a ticker and `None`; and that the committed map equals the catalogue's five key/label pairs in `templates.json`.

1. Write the three files. 2. Run your tests and the three criteria. 3. Commit the code and tests first (one commit), then the proof and the status flip as separate commits. 4. Report.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR171-g-AC1" cell_refs="AR-g-171"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_compare_checks.py 171 build</invocation><expect>^AR-CMP-171-OK</expect></criterion>

<criterion id="AR171-g-AC2" cell_refs="AR-g-171"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_compare_checks.py 171 guard</invocation><expect>^AR-CMP-171-OK</expect></criterion>

<criterion id="AR171-g-AC3" cell_refs="AR-g-171"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_compare_checks.py 171 regress</invocation><expect>^AR-CMP-171-REGRESS-OK</expect></criterion>

<expected_criteria>AR171-g-AC1,AR171-g-AC2,AR171-g-AC3</expected_criteria>

- AC1: `model_source` reads both objects (plain and gzip) to the checker's own arithmetic, refuses every bad body with `ModelSourceRefused`, and the committed map equals the catalogue's five key/label pairs. At base it FAILs (the module does not exist).
- AC2: no existing element of the Overview, Multi or Comparison report moves. At base it PASSes.
- AC3: the ten existing producer and layout test files plus your own pass, and the branch changed only your files, your folder, the order and the channel file. At base it PASSes.

## BOUNDS

- **Grant.** The `<paths>` block only. Every other file is read only.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/model_source.py
infra/aws/lambda/investor-reporting/ycharts/research/model_code_map.json
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_model_source.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~330/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-171.model-source-reader-and-model-code-map.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R60_G.md</decomp_doc> round 60, workstream ~G, cell `AR-g-171`.
<owned_cells>AR-g-171</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR171-g-AC1,AR171-g-AC2,AR171-g-AC3. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~330/IRPT_ANLREQ.TO-AR-g-171.model-source-reader-and-model-code-map.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-171`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the code and tests first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's RESULT line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR171-g-AC1,AR171-g-AC2,AR171-g-AC3` BEFORE the flip to complete. Flip the order's `<status>` to complete ONLY if all three criteria PASS.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~308/IRPT_ANLREQ.TO-AR-g-170.producer-guard-held-price-layout-and-stale-tests.proof_of_spec.json` (read it from the main tree `C:/dev/ajb_workspace` if absent in your sparse worktree).
</proof_of_spec>

**REPORT (final message):** the commit hashes, the three criterion outputs (the RESULT lines), and any row filed.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- `model_source.py` and the map are new members of the resident package (the `ycharts/research` directory is packaged whole); nothing calls them until AR-g-175, and no deploy or AWS call is made.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change in this cell (the grant is AR-g-172).
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache key or TTL is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- the criteria were dry-run at the base from the invocations above: 171 build FAIL (no module), 171 guard PASS, 171 regress PASS, calibrate OK. Traps: the positioning object is gzip, the series is plain JSON; the first row's own return is not applied; a display name must not match. NOT seen (blind): the live objects through this module (the issuer runs a real-data control at the drain).
</preflight>

- Cut by the issuer inside its own decomposition (R60) on the CTO's order to decompose and issue FWD-10 as one round (msg 11442). Base: AC1 FAILs, AC2 PASSes, AC3 PASSes.
