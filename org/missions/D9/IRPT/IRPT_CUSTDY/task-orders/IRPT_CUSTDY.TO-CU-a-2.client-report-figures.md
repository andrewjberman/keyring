# TO IRPT_CUSTDY.TO-CU-a-2 -- round 1 CU-a-2: the figures -- returns over the ruled periods, holdings, activity and labelled fees from Schwab's records

<to_id>IRPT_CUSTDY.TO-CU-a-2</to_id>
<project>IRPT_CUSTDY</project>
<issued_to>0.9.0_WK_IRPT_CUSTDY~2</issued_to>
<issued_by>2.0.0_SA_COO~K2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~K2</workstream>

**Directive:** D9 | **Fabric:** laptop (placement dell2) | **Decomp cell:** `CU-a-2` (`decompositions/IRPT_CUSTDY_DECOMP.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none (the decomposition fixes the client-report contract)

---

## WORKER FACE

### THE CELL

`CU-a-2`, hops 2 and 3 of the round-1 thread, FWD-1: every client of one 49 Financial advisor gets a quarter-end report "built by Opal
from Schwab's own records: returns, holdings, activity and fees for each account and household over the standard periods". You build the
FIGURES and prove them on fixtures, plus one real READ of Schwab's coverage; the issuer writes to S3 after the drain. Nothing reads Black
Diamond (PRD ruling 4).

**What exists (READ, never edit):**
- Schwab silver under `opal-data-assets/schwab/<master>/silver/` for masters `08242234` and `08335338` (producer
  `data/assets/scripts/silver/schwab_conversion.py`: read it for the positions, balances and transactions tables and their partitions).
- The returns gold: `data/assets/scripts/gold/irpt_reporting/account_return_daily.py` writes table `account_return_daily` (and
  `holdings_performance_daily`, `dim_return_method`) at `opal_naming.address("irpt", firm, "gold", <table>, "date=<day>")`, firm from
  `firm_scope()` (registry `lookup()`); its sources are declared in `data/assets/scripts/gold/irpt_reporting/sources.json`.
- The periods: `data/assets/scripts/gold/runners_49f/parity_period_returns.py` -- `RULED_PERIODS = ('QTD', 'YTD', '1Y', 'SI')`,
  `period_window(period, asof, anchor)` and `link(daily, accounts, asof, periods, anchors, anchor_basis, earliest_partition, bd_bmvs)`.
  **Import them; never re-type the period list or re-implement the linking.** A window that is not ruled is reported
  `WINDOW_NOT_RULED`, never computed another way.
- IRPT_BCKEND's holdings producer `data/assets/scripts/gold/investor_reporting/holdings_49f.py` (read for how holdings are valued).
- `lib/opal_naming.py`: `lookup(<master>)['firm']`, `address(source, scope, tier, table, partition)`. Never type a firm token or an S3 key.

**The output: the decomposition's CLIENT-REPORT CONTRACT, exactly** (one JSON document per household):
`{"firm", "advisor", "as_of", "household": {"id","name"}, "periods": [RULED_PERIODS in order], "accounts": [{"account" (last 4 only in
anything printed), "registration", "returns": {<period>: {"value", "window": [start,end], "status": "OK|NO_DATA|WINDOW_NOT_RULED"}},
"market_value": {"start","end"}, "holdings": [{"symbol","cusip","quantity","market_value","weight","class","sector","described",
"description_source"}], "activity": [{"date","type","symbol","amount"}], "fees": {"amount", "source": "SCHWAB_TXN_FEE_ROWS",
"is_billed_fee": "UNKNOWN"}}], "household_returns": {<period>: {...}}, "lineage": {"schwab_partitions", "returns_partition",
"classification_vintage"}}`. You leave `class`, `sector`, `described`, `description_source` as `null` (the issuer's join fills them from
another cell). Every figure carries `status`; one that cannot be made says so in place, never dropped, never zero-filled.

**Build `data/assets/scripts/gold/irpt_custody/client_report_figures.py`:**
1. CLI: `--accounts <file: one account per line, with household id>`, `--as-of <YYYY-MM-DD>` (default `2026-09-30`), `--out <local dir>`
   (default a temp dir), `--apply` (writes each document under `address("irpt", <lookup firm>, "gold", "client_report",
   "date=<as-of>")` -- written, NOT run by you), `--coverage --master <m>`, `--self-test`. Device-free.
2. Before computing anything, print the Schwab silver partition dates it read per table and refuse (exit 2, `COVERAGE as_of_covered=False`)
   if `--as-of` is not covered for any requested account.
3. Per account: returns for each ruled period via `link()`; start/end market value; holdings at `--as-of`; activity = the transaction rows
   inside the QTD window; fees = the transaction rows Schwab marks as fees inside the QTD window, labelled `SCHWAB_TXN_FEE_ROWS`. Per
   household: `household_returns` by the same linking over the household's accounts.
4. `--coverage --master <m>` (read only): list the master's silver tables and print `SCHWAB-COVERAGE master=<m> read_ok=<True|False>
   tables=<n> latest=<date> as_of_covered=<True|False>`.
5. `--self-test`: fixture silver and fixture returns for two households (one with an account lacking data in one period), run end to end
   locally; print, as the LAST line, `CLIENT-FIGURES-SELFTEST contract_ok=<True|False> periods_ok=<True|False> nodata_marked=<True|False>`.
6. Tests `data/assets/scripts/gold/irpt_custody/tests/test_client_report_figures.py` (pytest, `tmp_path`, insert the module's directory into
   `sys.path`; no `__init__.py`): the documents validate against the contract's keys; the periods come from `RULED_PERIODS` in order; a
   missing figure is `NO_DATA`, not 0; fee rows are labelled; uncovered `--as-of` exits 2; no printed line carries more than the last 4 of
   an account.

### ACCEPTANCE

<criterion id="CU2-AC1" cell_refs="CU-a-2"><invocation>python -m pytest -q data/assets/scripts/gold/irpt_custody/tests/test_client_report_figures.py</invocation><expect>passed</expect></criterion>
`CU2-AC1` -- the figures on fixtures: contract keys, ruled periods, NO_DATA in place, labelled fees, the coverage refusal, masking.

<criterion id="CU2-AC2" cell_refs="CU-a-2"><invocation>python data/assets/scripts/gold/irpt_custody/client_report_figures.py --coverage --master 08335338</invocation><expect>SCHWAB-COVERAGE master=08335338 read_ok=True</expect></criterion>
`CU2-AC2` -- the hop's seam against its REAL neighbour: one read-only pass over the real Schwab silver of one master through the real CLI.
Whatever `as_of_covered` reads is reported, not graded.

<expected_criteria>CU2-AC1,CU2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **AWS: read only, and only in `--coverage`** (`.tools/aws` shim; list and get on `opal-data-assets/schwab/` only). **Never run
  `--apply`**, and no put, copy or delete anywhere. The S3 write is the issuer's act after the drain, under a change-management entry.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `IRPT_CUSTDY-W2-S<k>`), and do not weaken the test.

<paths>
data/assets/scripts/gold/irpt_custody/client_report_figures.py
data/assets/scripts/gold/irpt_custody/tests/test_client_report_figures.py
org/missions/D9/IRPT/IRPT_CUSTDY/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_CUSTDY/decompositions/IRPT_CUSTDY_DECOMP.md</decomp_doc> (round 1), cell `CU-a-2`.
<owned_cells>CU-a-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CU2-AC1, CU2-AC2. Instance at `org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~2/IRPT_CUSTDY.TO-CU-a-2.client-report-figures.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CU2-AC1,CU2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the self-test and coverage output, the CLI, the test list, the Schwab tables and partitions you read, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE round 1 runs by hand; no schedule (a scheduled producer is an enrichment item, never ad-hoc evidence).
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; CU2-AC2 reads with the dell2 box profile; the --apply write is the issuer's.
comp-adversary: RUN -- cross-firm (49financial scope only, lookup()); WORLD for the --apply path the issuer runs; BLIND: Schwab silver freshness at 2026-09-30 (CU2-AC2 reports it).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD v0.2 @c2bc15f427 section 2 hops 2-3, S02-S04, rulings 2 and 4; decomposition constraints 2, 5, 6, 8 and the contract.
