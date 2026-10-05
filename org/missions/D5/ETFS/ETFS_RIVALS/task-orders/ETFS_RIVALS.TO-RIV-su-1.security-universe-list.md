# ETFS_RIVALS task order -- `RIV-su-1` -- ROUND 8 WORKSTREAM D (ENRICHMENT): ONE SERVED LIST OF EVERY SECURITY THE RIVALS AND OPAL ETFS HELD WITHIN 3 YEARS (gold security_universe)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-su-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~8</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L6 (2026-10-04 ~21:1xZ, --drift) -- WITHIN BUDGET, 6 of 6 carriers scanned (C1=29 C2=32 C3=12 C4=21 C5=334 C6=1); 1 gate armed, not on this project; the notifier moratorium binds.
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, the A1 rankings, buying trend, input census and AI accounts, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg the vehicle runs from the CLOUD working tree). **Round 8, workstream D** (CTO~Z ruling msg 29426; laptop 1.0.0_SA_CTO msg 105132; Andrew-direct 3-year lookback cap @357e681ddf): ETFS_RIVALS serves ONE list of every security the rivals and the Opal ETFs held within 3 years, which MDPF_SECCLASS reads to backfill each into the ETFClassifier table. Nothing in round 8 deploys, merges or flips a gate from a worker. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-su-1` -- one served list of every security held within 3 years (gold security_universe)
- Measured: no such table exists; the laptop's MDPF_SECCLASS FWD-9/FWD-10 (every Rival Funds stock in etf-classifications with
  3 years of history; a routine for new stocks) reads its security list from the artifact ETFS_RIVALS serves.
- Interface: `rivalfunds.gold_security_universe.handler_entry({"date", "sink"})` reads canonical_shape from (as-of minus 3
  calendar years) through the as-of (NYSE T-1 of the page day), newest revision per date, and writes ONE object at
  `address("rivalfunds","etfs","gold","security_universe","date=<as-of>","universe-<revision>.parquet")`: one row per
  security (the G5 window-stable key), identifiers, name, first_seen, last_seen, funds, n_report_dates; no cash lines.
- **Organic trigger:** the 07:00 ET marker publish (the issuer wires it into `publish_page.produce_a1` at the merge).

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD HEAD at the cut (the package equals the deployed pin 75ad1e4d2e))

- The check file's docstring is the exact interface it reads: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/su-1.AC1.py` before you build.
- Model it on the A1 producers (`gold_input_census.py`, `gold_buying_trend.py`): the `handler_entry` shape, `revision.newest`
  to pick a date's newest canonical revision, `homes.canonical_shape` to read, `sinks` to write, a `revision`-named object.
- The G5 key family (first that the row carries): `security_bloomberg`, then `security_cusip`, `security_isin`,
  `security_sedol`, `security_ticker`, else `raw_identifier` (`gold_trade_schedule.py` module docstring).
- Cash and currency lines are not securities: `is_cash_line`, `position_type == cash`, or a `... Curncy` identifier.
- The wiring into `publish_page.produce_a1` (`A1_PRODUCED`) is a shared-file hookup: name it in your report; the issuer adds
  it at the merge. Do not edit `publish_page.py` or `homes.py`.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/` and the earlier rounds' `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round{5,6,7}/checks/`, the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (v0.16 @646ce7f4b8), the decomposition `org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md` (round 8, its WORKSTREAM D section), and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~8/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any environment gate flip outside a test, any file another round-8 chain owns. Tests go beside the code as `tests/test_r8su1_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed). A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/gold_security_universe.py
data/etfs/scripts/rivalfunds/tests/test_r8su1_*.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- one object at the security_universe address for the as-of date holds every security held within 3 years (first/last seen, funds, report-date count), no cash lines, nothing older than the floor; inputs untouched (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/su-1.AC1.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-su-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/su-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~8/ETFS_RIVALS.TO-RIV-su-1.security-universe-list.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-su-1.security-universe-list`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; any existing test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** CTO~Z ruling msg 29426 (ETFS_RIVALS supplies the security list), laptop 1.0.0_SA_CTO msg 105132 relayed by MSTR~Z 29470, Andrew-direct 3-year cap @357e681ddf; decomposition round 8 WORKSTREAM D section. Chain `~8`, slot `~8`, position 1 of 1. Checks dry-run at base CLOUD HEAD at the cut (the package equals the deployed pin 75ad1e4d2e): su-1.AC1 FAIL (3; control OK) as expected. Bounds: no merge before the 2026-10-05 07:00 ET vehicle pull; no deploy before the 13:30Z grades.

<risk>SERVED</risk>
<worker_class>worker-light</worker_class>
<status>complete</status>
<round>8</round>
<workstream>D</workstream>
<slot>~8</slot>
<fabric>site-z</fabric>
