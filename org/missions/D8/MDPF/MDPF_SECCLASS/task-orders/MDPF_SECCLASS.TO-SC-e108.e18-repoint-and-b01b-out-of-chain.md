# TO MDPF_SECCLASS.TO-SC-e108.e18-repoint-and-b01b-out-of-chain -- round 27 SC-e-108: E_18 reads the canonical list as its known set and stops using the old list; B_01b leaves the canonical chain (build only, nothing is deployed)

<to_id>MDPF_SECCLASS.TO-SC-e108</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~98</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>27</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-108` (`decompositions/MDPF_SECCLASS_DECOMP_R27.md`) |
**outcome_ref:** FWD-4 / FWD-5 | **depends_on:** none | **source:** CTO round-26 analysis section 2-3 items 1 and 2 (msg 6482); FWD45_B01B_E18_DISPOSITION.md section f items 1, 2, 5

---

## WORKER FACE

### THE CELL

`SC-e-108`. Round 26's record (`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~93/FWD45_B01B_E18_DISPOSITION.md`, read it first) names every line of `data/black_diamond/scripts/gold/E_18.detect_new_securities.py` that uses the old DynamoDB table `bd-securities`, and the CTO ruled the order: a separate cell seeds the 22 tickers the old list holds and the canonical table lacks; THIS cell builds the repoint, which a CloudOps seat ships only after that seed is applied. Facts (measured): E_18 skips every pair whose key is in `known` (line 247) and `known` is the old list's key set (line 215), so its lookup `default_bd_securities_lookup(BD_SECURITIES_TABLE)` at line 291 never sees an old-list ticker and returns nothing. The gold chain (`data/black_diamond/scripts/gold/gold_dispatch.sh`) runs `B_01b` (an outside-model classifier whose only output is the old list; no later step reads it, `B_02-READS-BD-SECURITIES: no`) between B_01 and E_18. **Ruling (the issuer's): B_01b leaves the chain in this cell; its FILE STAYS (dead) until the shipped chain is proven; E_18 stops using the old list entirely; the shared module `_shared/etf_classification_scheduled.py` is NOT edited this round (its `default_bd_securities_lookup` stays, unused by E_18).**

**What you build:**
1. **E_18** (`data/black_diamond/scripts/gold/E_18.detect_new_securities.py`): (a) build the `ETFClassifier()` instance and `known = existing_tickers(classifier)` (the canonical table's key set, `NAME::` keys included) at the top of `detect_new_securities`, right after the shared import, and delete `load_known_tickers`, the `table = dynamodb.Table(BD_SECURITIES_TABLE)` handle, `_scan_db_asset_names` and the name-prefix block (lines ~256-265) with its `db_asset_names`/`prefix_resolved` counter; (b) delete the `BD_SECURITIES_TABLE` constant, remove `default_bd_securities_lookup` from the import list and call `plan_rows(...)` without `bd_securities_lookup` (it defaults to None); (c) reuse the `classifier`/`vocab`/`existing` objects the later block builds (do not build `ETFClassifier()` twice); (d) rewrite the docstrings, comments, the summary prints and the `--upload` help so that NO line of the file contains the strings `bd-securities`, `BD_SECURITIES_TABLE`, `bd_securities` or `default_bd_securities_lookup` (a pointer such as `the retired old list` is fine); keep `normalize_key`, `_normalize_asset_name`, `_load_resolution_table`, the resolution-aware skip and the tickerless counts working.
2. **gold_dispatch.sh** (`data/black_diamond/scripts/gold/gold_dispatch.sh`): `CHAIN_CANONICAL="B_00 B_01 E_18 B_02 B_03 C_00 C_01 C_02 C_04"`, `CHAIN_HOLDINGS_SEED="B_01"`, `GROUP_B="B_00 B_01 B_02 B_03"`, delete the `PHASE_B3: B_01b` block (`echo`, `run_background B_01b`, `wait_phase PHASE_B3`) and fix the comments and help text that say B_01b runs, that B_02 reads what it writes, or that E_18 follows it (around lines 46, 49, 144-162, 556-566, 580, 919, 933-935, 957); the registry row `B_01b|B_01b.classify_new_securities.py|--upload` STAYS (the script file stays); E_18 stays dispatched and NONFATAL.
3. A new test `data/black_diamond/scripts/gold/tests/test_e18_known_set_r27.py`. Read a sibling test in that folder first (for example `test_c06_rolling_rederive_r23.py` or `test_thread_trace.py`) for how a gold script is loaded without side effects. Stub the module's `s3`/`dynamodb` clients and put a fake `etf_classification_scheduled` module into `sys.modules` (with `ETFClassifier`, `TableVocabulary.from_live_table`, `existing_tickers`, `plan_rows` that records its arguments, `write`) and a small holdings parquet (built with pandas) as the S3 body. Show: (a) a pair whose key is in the stub canonical key set is skipped and a pair that is not is passed to `plan_rows` as a candidate; (b) the recorder of every `dynamodb.Table(<name>)` call sees NO name containing `bd-securities`; (c) `plan_rows` is called with no truthy `bd_securities_lookup`; (d) the DIFFERENCE CONTROL: the same recorder DOES flag a deliberate `dynamodb.Table('bd-securities')` call made by the test itself, so the recorder can tell; (e) a `NAME::`-keyed tickerless pair in the stub canonical set is skipped.
Do not touch any other file (not the shared module, not B_01b, not other gold scripts).

### ACCEPTANCE

<criterion id="SC27-e108-AC1" cell_refs="SC-e-108"><invocation>python -m pytest data/black_diamond/scripts/gold/tests/test_e18_known_set_r27.py -q --tb=short</invocation><expect>passed</expect></criterion>
`SC27-e108-AC1` -- the new test passes, including the difference control (d).

<criterion id="SC27-e108-AC2" cell_refs="SC-e-108"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R27_CHECKS/check_chain_without_b01b.py</invocation><expect>CHAIN-NO-B01B ok=True</expect></criterion>
`SC27-e108-AC2` -- the canonical chain, the holdings-seed alias and group B no longer name B_01b, no phase runs it, E_18 is still dispatched and non-fatal, and `bash -n` accepts the file.

<criterion id="SC27-e108-AC3" cell_refs="SC-e-108"><invocation>bash -c 'git grep -n -i -E "bd-securities|BD_SECURITIES_TABLE|bd_securities|default_bd_securities_lookup" -- data/black_diamond/scripts/gold/E_18.detect_new_securities.py | wc -l'</invocation><expect>0</expect></criterion>
`SC27-e108-AC3` -- E_18 names the old list nowhere (17 lines at the base).

<expected_criteria>SC27-e108-AC1, SC27-e108-AC2, SC27-e108-AC3</expected_criteria>

Dry-run at the base (dell1 box/dell1 HEAD, 2026-10-16 ~04:5xZ): AC1 FAILS as expected (the test file is absent); AC2 FAILS as expected (`CHAIN-NO-B01B ok=False`, four problems); AC3 FAILS as expected (`17`). The check's own green arm (a copy of gold_dispatch.sh with the four edits) read `ok=True`; its negative arm (GROUP_B left with B_01b) read `ok=False`. A third verification the drain adds: the sibling gold test suites stay green.

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, curl or tool fetch). pandas, pyarrow and boto3 are already installed.
- **No AWS call of any kind.** Nothing is deployed.
- **Nothing is deployed.** The ship of E_18 and `gold_dispatch.sh` is a LATER order to a CloudOps seat under a signed never-widen pair, after the seed is applied.
- **Never edit** anything outside the `<paths>` block; the check scripts under `R27_CHECKS/` are READ-ONLY to you. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and file a surprise row (id `MDPF_SECCLASS-D1-W98-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). Do not weaken a check, and do not edit a check to make it pass.
- Run every invocation under `timeout 120`; the checks end well inside it.

<paths>
data/black_diamond/scripts/gold/E_18.detect_new_securities.py
data/black_diamond/scripts/gold/gold_dispatch.sh
data/black_diamond/scripts/gold/tests/test_e18_known_set_r27.py
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R27.md</decomp_doc> (round 27), cell `SC-e-108`.
<owned_cells>SC-e-108</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC27-e108-AC1, SC27-e108-AC2, SC27-e108-AC3. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~98/MDPF_SECCLASS.TO-SC-e108.e18-repoint-and-b01b-out-of-chain.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC27-e108-AC1,SC27-e108-AC2,SC27-e108-AC3`.
</proof_of_spec>

**REPORT:** the exact diff of E_18 and gold_dispatch.sh, each criterion's output verbatim, the lines of E_18 that changed behaviour (a list), commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE nothing is scheduled; nothing ships.
comp-iam: DECLARED-NOT-APPLICABLE only the reads the seat's role already makes.
comp-adversary: RUN -- a test that passes against the old E_18 (the difference control (d) proves the recorder; the old file also fails AC3); an E_18 that still builds a second classifier or still reads the old list through the shared lookup (AC3 and (b)); a dispatch edit that breaks the shell syntax (AC2 runs `bash -n`); BLIND: the first scheduled run of the shipped chain (the issuer's later read), and any tool outside this tree that runs B_01b by name.
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-26 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_26_20261016.md`, msg 6482); DECOMP_R27.
