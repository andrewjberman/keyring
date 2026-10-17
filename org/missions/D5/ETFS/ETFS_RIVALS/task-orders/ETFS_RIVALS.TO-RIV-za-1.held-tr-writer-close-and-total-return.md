# ETFS_RIVALS task order -- `RIV-za-1` -- A HELD-TR MODE LANDS CLOSE AND TOTAL RETURN TOGETHER FOR NAMED UNITS, ONE TIMED G4 OBJECT PER DATE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-za-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~45</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell; no S3 or deploy act
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work; at the cut nothing is returned, and the evidence context is this order's check file (dry-run at the base: FAIL 5 as expected)
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric dell1) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two
peer groups): rankings, buying trend, AI accounts, a security dialog per holding with a price chart, and an audit page.
Code: `data/etfs/scripts/rivalfunds/` (run from `data/etfs/scripts`, package `rivalfunds`); tests:
`data/etfs/scripts/rivalfunds/tests/` (pytest from `data/etfs/scripts`).

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-za-1` -- a `held-tr` mode asks PX_LAST and DAY_TO_DAY_TOT_RETURN_GROSS_DVDS together for named (security, trading day) units and lands each date as ONE timed G4 object the rankings read (Andrew-direct 2026-10-17; CTO msg 7291) -- APPENDED 2026-10-17, revision 1.33
- Placement: the queued `MDPF_DEMQUE/requests/ETFS_RIVALS-C1-TR-HELD-{D30,D90,D365}` (held at 04:2xZ by `1.0.0_SA_CTO~DELL1` msg 7280: DEMQUE output lands in ZQ_STANDING, not the page store) are the units; no rivalfunds writer lands total return history today (`BACKFILL_FIELDS = ["PX_LAST"]`; the history-owed ask is PX_LAST only).
- Measured (2026-10-17, code read): `gold_holding_contribution._g4_merge` copies the PRICE GROUP (`px_close`, `total_return_index`, `currency`, `as_of`, `source`, `as_of_source`, `price_date`) WHOLE from the first ranked row whose `px_close` is not null, and ranks a non-backfill row before a backfill row; `drop_backfill` removes rows whose `as_of_source` is exactly "backfill". So a TR value reaches the rankings only on a NON-backfill row that carries its own `px_close` -- a TR-only row never does.
- Interface: (1) `handler_entry` accepts mode `held-tr`, event {"units": [{"bloomberg": <key>, "dates": [ISO trading days]}], "max_points": int >= 0 (required), "dry_run": bool (absent = true), "batch_id", "sink"}; the request shape is the DEMQUE dates-entry shape, so a request file's `securities` list is a valid `units`. (2) Plan: units = the (security, date) pairs; fields `["PX_LAST", "DAY_TO_DAY_TOT_RETURN_GROSS_DVDS"]`; currency lookups = the unit securities with no stored currency by `_stored_currencies(s, secs, <first unit date>, _run_date_et())`; points = 2 x units + lookups. REFUSED before any request when points > max_points or `bbg_budget.check_points(points)` refuses; a dry run returns OK with the plan and requests and records nothing. (3) Live: ONE reference CRNCY request for the lookups; then per date, batches of `DEFAULT_BATCH`, `_blp_historical_data(batch, fields, day, day)`; every request sent is recorded with `bbg_budget.record("held-tr", ...)`; a returned value dated other than the asked day is not written and is counted `misdated`; a security whose PX_LAST is missing is not written. Each date's rows are `market_rows(..., MARKET_SOURCE_HIST, prov, "held-tr")` with `price_date` = the day and `currency` = the stored or looked-up currency, landed as ONE new object `market_target_uri(day, f"{rev_mod.compact(rev_mod.capture_time(produced_at))}-{_digest(data)[:12]}")`, never overwriting a name. Result {"status", "plan", "units", "asked", "landed", "carried", "failed", "misdated", "currency_lookups"} and one printed line `HELD TR: units <n>; asked <a>; landed <l>; carried <c>; failed <f>; misdated <m>; currency lookups <k>`. (4) CLI: `--mode held-tr --units-file <json: a list, or an object whose "securities" is the list> --max-points <n> [--live]`.
- Out of bounds: every reader and stage (`gold_holding_contribution.py`, `price_series.py`, the rankings), `bbg_budget.py` and its config, `history_owed.py`, the existing modes' behaviour (market-range, history-owed, daily), any S3 write outside a LocalSink, any vendor call, Terraform and the Lambda.
- Checks: `round32/checks/za1_held_tr_check.py` (AC1 the plan, dry run and refusal, two tests; AC2 the live landing and no overwrite, two tests; AC3 the merged row takes the held-tr price group over a backfill row and `drop_backfill` keeps it, one test; base FAIL 5). J1: none (a LOCAL cell; the run is its own pair, a `SERVED` path).

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base box/dell1)

- Read the check before you build: `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round32/checks/za1_held_tr_check.py`. It FAILS at the base (5 failed) and is your target; do not edit it. It stubs `eb._blp_historical_data`, `eb._blp_reference_data`, `bb.record`, sets the budget ledger dir and `_run_date_et`, and plants one backfill object per unit date plus one non-backfill object (the stored currency) on 2026-09-17.
- The nearest model is `_market_range` (about line 775 of `enrichment_bloomberg.py`): its event checks, `_stored_currencies`, the budget refusal wording, the dry-run return and the per-batch `bbg_budget.record` calls. The second model is the ask branch of `_history_owed` (about line 1000): its per-date batching, the `misdated` rule and the per-date timed object with `price_date`. Reuse their helpers; do not change either function.
- `handler_entry` (about line 1101) refuses an unknown mode at about line 1139 and dispatches `market-range` at about line 1151: add `held-tr` to the allowed tuple and dispatch it the same way. `main` (about line 1256) passes `--start/--end/--max-points/--securities/--live` for market-range at about line 1285: add `--units-file` and the `held-tr` branch beside it.
- `_stored_currencies` never reads a backfill row as a stored currency. `market_rows` fills every `MARKET_MAP` column it is given and leaves the rest null; set `currency` yourself from the stored/looked-up map, as `_history_owed` does.
- Regression net: `cd data/etfs/scripts && python -m pytest -q rivalfunds/tests`; report its final line.

## 3. SURFACES AND BOUNDS

You READ (never edit): every file not in your `<paths>`, including `lib/`, `integrations/`, Terraform, the decomposition and
the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md`.

You WRITE only the `<paths>` below (plus `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~45/`).
NEVER: any S3 read or write outside a LocalSink or memory sink, any deploy, gateway release or Terraform, any vendor call
(Bloomberg, OpenAI, Bright Data or any live web search), any Secrets Manager call, any environment gate flip outside a test.
A row you file goes in the investigation file below with id `ETFS_RIVALS-D1-W45-S<k>`, `"fabric": "dell1"`, `surfaced_at` = `date -u +%FT%TZ` at filing.

<paths>
data/etfs/scripts/rivalfunds/enrichment_bloomberg.py
data/etfs/scripts/rivalfunds/tests/test_riv_za1_held_tr.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.dell1.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from the repository root)

- **AC1** -- the plan, the dry run and the refusal: two points per unit plus lookups, nothing requested or recorded on a dry run or a refusal.
- **AC2** -- the live landing: one timed object per date carrying close, total return, currency and its own trading date; a misdated value is not written; a second run overwrites nothing.
- **AC3** -- the readers: the merged G4 row takes the held-tr price group over a backfill row, and `drop_backfill` keeps it.
<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-za-1"><invocation>cd data/etfs/scripts; python -m pytest -q -p no:cacheprovider ../../../org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round32/checks/za1_held_tr_check.py -k ac1</invocation><expect>2 passed</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-za-1"><invocation>cd data/etfs/scripts; python -m pytest -q -p no:cacheprovider ../../../org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round32/checks/za1_held_tr_check.py -k ac2</invocation><expect>2 passed</expect></criterion>
  <criterion id="AC3" cell_refs="RIV-za-1"><invocation>cd data/etfs/scripts; python -m pytest -q -p no:cacheprovider ../../../org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round32/checks/za1_held_tr_check.py -k ac3</invocation><expect>1 passed</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Add `rivalfunds/tests/test_riv_za1_held_tr.py`: one test per behaviour you added that the check file does not pin (for example the CLI `--units-file` reading a DEMQUE request object's `securities`, and the printed `HELD TR:` line). Run the rivalfunds suite (`python -m pytest -q rivalfunds/tests` from `data/etfs/scripts`) and report its final line.
Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~45/ETFS_RIVALS.TO-RIV-za-1.held-tr-writer-close-and-total-return.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-za-1.held-tr-writer-close-and-total-return`. Report once: each criterion's verdict line with the output above it;
files written; every existing test assertion you changed and why; rows filed (id + one line); anything the issuer must do at
the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L6, 2.0.0_SA_COO~RV):** Round 32, ONE issuance, one cell, on Andrew-direct 2026-10-17 ~04:2xZ "Yeah I want all those completely filled" / "now" and `1.0.0_SA_CTO~DELL1` msg 7291 ("cut the TR writer cell in your next issuance now"). Decomposition revision 1.33. `fanout: 1 of 1 chains, cap 8`. Check file dry-run at the base before the cut: za1 base: FAIL (5 failed) as expected. Chain A (`enrichment_bloomberg.py`); round 31's cells are complete and touch no file here. At the drain: merge, the Lambda package question (the live run executes the site-Z working tree, the vehicle's own code, not the Lambda), the served-rankings never-widen pair to `1.0.0_SA_CTO~DELL1` BEFORE any held-tr row lands on live S3, then the site-Z run over the three TR-HELD request files.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>32</round>
<workstream>1</workstream>
<slot>~45</slot>
<fabric>dell1</fabric>
