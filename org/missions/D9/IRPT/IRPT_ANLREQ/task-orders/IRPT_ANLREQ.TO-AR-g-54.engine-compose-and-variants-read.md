# TO-AR-g-54 -- the report engine's compose points and variants: a READ of what the priced layout consumes, which estate price stores exist and how they are keyed, what the Comparison and Multi-Comp maps need, and where prices and the swap enter the producer; READ ONLY, one record, no source change

<to_id>IRPT_ANLREQ.TO-AR-g-54</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~173</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-54` (`decompositions/IRPT_ANLREQ_DECOMP_R7_G.md`) |
**outcome_ref:** FWD-7 (C-PRICES, hop 9, hop 10) | **depends_on:** none.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~173`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-173` (branch `wk-IRPT_ANLREQ-173`), provisioned by the issuer. Work only there.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~173 <0.9.0_WK_IRPT_ANLREQ~173@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W173-S<k>` (take the next free `<k>`); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- No live call, NO PUSH, no AWS call of any kind, NO edit of any source file. Scratch outside the product tree. Use the native Grep, Glob and Read tools; a recursive shell grep over the repo is denied by a hook.

### THE CELL (`AR-g-54`, inlined) -- a READ. The product tree is not edited.

*Context.* The Opal engine (`infra/aws/lambda/investor-reporting/ycharts/research/opal_producer.py`) renders the Overview with
`pricing=False`, so 251 of 257 sections are NOT_AVAILABLE (return, risk, benchmark and risk-free figures). Andrew wants a report worth
reading: prices from the estate's own stores, then Yahoo, then YCharts one symbol per call (the chain core `price_source.py` is being built
by a sibling cell, `AR-g-51`: `resolve_prices(symbols, start, end, readers, as_of)` returns `series[SYMBOL]["rows"] = [[date, price], ...]`
ascending and labelled by source), a deterministic replacement when a security has no price (`AR-g-52`), and the Comparison and Multi-Comp
variants, which today the Opal engine ignores (it renders an Overview only). To cut the build cells that connect these, the issuer needs to
know the seams. You read them.

Answer these four questions from SOURCE, each with `{file, line, text}` evidence read from the worktree (print the lines you cite; a line you
did not read is not cited). Read first: `ycharts/research/layout_overview.py` (the `pricing` flag at about lines 756-830 and 1040-1140),
`ycharts/research/opal_producer.py`, `ycharts/research/held_data.py`, `ycharts/research/runner.py` (how the YCharts path obtains price
series today), and `ycharts/generate/resident_worker.py` (`run_opal` about line 510, the producer choice about line 748), all under
`C:/dev/wk-irpt-anlreq-173/infra/aws/lambda/investor-reporting/`; the maps under
`C:/dev/wk-irpt-anlreq-173/org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/` (`overview_map.json`, `comparison_map.json`, `multi_map.json`).

1. **Q1, what the priced layout consumes.** With `pricing=True`, list every price-based element FAMILY of the Overview map (returns, risk,
   benchmark-relative, risk-free, and any other) and for each: the function in `layout_overview.py` that computes it, the series input it
   reads (type, whether a list of `[date, price]` rows, a dict, a dataframe; the column or key names; the date type), and the window it
   uses. Name the benchmark symbol(s) and the risk-free input the layout expects (or `null`), and state in `series_contract` the ONE input shape
   a price source must hand the layout (the issuer will have the compose cell build that shape from `price_source`'s rows).
2. **Q2, the estate stores.** Two stores hold prices the report may read first: MDPF_DEMQUE's Yahoo price store (written by
   `data/mdpf/scripts/demque/price_store.py`; `s3_root()` and its address builder call) and the Opal ETFs' Bloomberg history (the
   `opal-data-etfs/bbg/<date>/...` family; `held_data.py` and `layout_overview._read_characteristics` read its `characteristics.parquet`; find
   where the HISTORY lives, or say `not found`). For EACH, as a row `name` = `"demque_price_store"` and `"opal_etf_bbg_history"`:
   `address_builder_call` (the `lib/opal_naming.py` / registry call that produces the address; never a typed bucket), `key_form`, `format`,
   `columns`, `symbol_key` (ticker, CUSIP or other), `basis` (price or total return; read Andrew's record
   `org/tier1_exec/2.0.0_SA_COO~Q1/deliverables/ANDREW_DIRECT_20261009_054xZ_PRICES_ARE_TOTAL_RETURN_STORE_PRICE_DIVIDEND_TR_PER_DAY.md`),
   `resident_can_read_today` (yes / no / unknown: from the resident host role's tracked IAM), and `cross_firm_note` (whether the store is
   per-firm or shared estate data; CLAUDE.md forbids a pipeline tree referencing another firm's data, so say which this is).
3. **Q3, the variants.** For each map (`overview_map.json`, `comparison_map.json`, `multi_map.json`): `variant`, `path`, `elements`
   (a count), and `needs_prices` (true when any element is price-based). Then `selection`: how the resident chooses a map for a job (the
   request's `variant` field; cite where `run_opal` / `opal_stores` supplies the map), `today_for_variants_2_3`: what the Opal engine does
   TODAY with a Comparison or Multi-Comp request (state it plainly), and `smallest_change`: the smallest change set that makes the Opal
   engine render the variant the filer chose (the files and what each gains).
4. **Q4, the seams and the round-8 cells.** `price_seam`: the exact place (file, line) where a price result enters the producer (the
   `held_readers` hook in `opal_producer._read_stage` about line 226, or a new store key; say which and why). `swap_seam`: where the
   replacement of an unpriced security runs, relative to pricing and to `lo.read_classifications`. `pricing_flag_seam`: where `pricing` is
   set for an Opal run (`opal_producer.produce`). Then `round8_cells`: a list of BUILD cells that connect the finished chain core and the
   replacement rule (each `{"id": "AR-g-6<k>", "summary": str, "files": [paths it would write], "edges": [ids it depends on]}`), with
   write sets that do not overlap, in the order they should be cut.

### Deliverable and ACCEPTANCE

Write `C:/dev/wk-irpt-anlreq-173/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~173/r7/ENGINE_COMPOSE_READ.json` with these keys:

- `base` (the sha your branch started from), `cell` (`"AR-g-54"`), `not_read` (a list of strings: what you did not read and why).
- `q1`: `{"elements": [{"family": str, "function": str, "input_shape": str, "evidence": [cite, ...]}, ... (at least 3)], "benchmark_symbols": [str, ...], "risk_free": str or null, "series_contract": str}`.
- `q2`: `{"stores": [{"name": str, "address_builder_call": str, "key_form": str, "format": str, "columns": [str, ...], "symbol_key": str, "basis": str, "resident_can_read_today": "yes"|"no"|"unknown", "cross_firm_note": str, "evidence": [cite, ...]}, ...]}`, the two names above both present. A string field says `not found` plainly when it is.
- `q3`: `{"maps": [{"variant": str, "path": str, "elements": int, "needs_prices": bool}, ... (at least 2)], "selection": {"evidence": [cite, ...]}, "today_for_variants_2_3": str, "smallest_change": str}`.
- `q4`: `{"price_seam": {"evidence": [cite, ...]}, "swap_seam": {"evidence": [cite, ...]}, "pricing_flag_seam": {"evidence": [cite, ...]}, "round8_cells": [{"id": str, "summary": str, "files": [str, ...], "edges": [str, ...]}, ... (at least 2)]}`.
- A `cite` is `{"file": "<path under the repo root, forward slashes>", "line": <int>, "text": "<a substring of that line>"}`.

<criterion id="AR54-g-AC1" cell_refs="AR-g-54"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g_read_checks.py shape54 org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~173/r7/ENGINE_COMPOSE_READ.json</invocation><expect>^SHAPE-OK </expect></criterion>

<criterion id="AR54-g-AC2" cell_refs="AR-g-54"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g_read_checks.py cite org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~173/r7/ENGINE_COMPOSE_READ.json</invocation><expect>^CITES-OK </expect></criterion>

<criterion id="AR54-g-AC3J" cell_refs="AR-g-54" judgment="true"/>
`AR54-g-AC3J` (judgment, graded at L9, never by you): the answers follow from the cited lines, a "not found" is said plainly with what was searched, and the round-8 cell list has non-overlapping write sets in a buildable order.

<expected_criteria>AR54-g-AC1 AR54-g-AC2 AR54-g-AC3J</expected_criteria>

- AC1 loads the record and prints `SHAPE-OK` only when every key, enum and evidence list above is present; otherwise `SHAPE-BAD <why>`. At base it FAILs (no record).
- AC2 re-opens every cite in the record (the denominator is printed) and prints `CITES-OK <n> of <n>` only when each cited line exists and the cited text is a substring of it. At base it FAILs (no record).

## BOUNDS

- **Grant:** exactly the `<paths>` below. You edit NO source file; the product tree is READ ONLY.
- If a cited file does not exist at the path named, find the file that now holds the function (a name search), cite that, and say so in the record.
- Rows: APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~173/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-54.engine-compose-and-variants-read.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R7_G.md</decomp_doc> round 7, workstream ~G, cell `AR-g-54`.
<owned_cells>AR-g-54</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR54-g-AC1, AR54-g-AC2, AR54-g-AC3J. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~173/IRPT_ANLREQ.TO-AR-g-54.engine-compose-and-variants-read.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-54`.
- The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: commit the record first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate AFTER its commit with `python .tools/proof-of-spec-check.py <instance> "AR54-g-AC1,AR54-g-AC2,AR54-g-AC3J"`; flip `<status>` to `complete` only when it prints VALID.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~136/IRPT_ANLREQ.TO-AR-y-328.resident-release-bindings-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):** each criterion's output lines; the round-8 cell list in one line each; commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read of source and one record; nothing is changed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by reading the cell against the answer shape. Traps: a store assumed readable because its path is known; a price basis assumed (price versus total return); a store read across a firm boundary; a variant assumed rendered because its map exists; a round-8 cell list with overlapping write sets. NOT seen (blind): the live stores, the live roles and the deployed bytes; denominator: 4 questions, each answered with cited lines.
</preflight>

- Cut on CTO msg 8377 (ENGINE lane) and PRD v0.14 FWD-7. Risk LOCAL: the cell reads source and writes one record. Base: `AR54-g-AC1` and `AC2` FAIL as expected (no record). The checker's green arm, mutant arm and absent-record arm were run by the issuer before the cut.
- Its output feeds the round-8 build cells (the store adapters, the compose into `opal_producer`, the variants); nothing is changed by this cell.
