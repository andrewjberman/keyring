# TO MDPF_DEMQUE.TO-DQ-t29 -- round 8 DQ-t-29: the ledger uploader resolves a Name-to-literal field list; the lander reads its consumer through the registry
<to_id>MDPF_DEMQUE.TO-DQ-t29</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~23</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-29` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 8 -- CUT) |
**outcome_ref:** repairs (rows D1-S6, D1-S7) | **depends_on:** none

---

## WORKER FACE

### THE CELL

`DQ-t-29`, the round's batch repair cell (CTO round-7 analysis `org/missions/D8/MDPF/MDPF_DEMQUE/ledger/ROUND_ANALYSIS.round7.md` section 3 items 4
and 5; rows `MDPF_DEMQUE-D1-S6` and `MDPF_DEMQUE-D1-S7`). Two small repairs in `data/mdpf/scripts/demque/`.

**1. D1-S6, `bbg_ledger_upload.py`.** `_field_count(source, symbol)` (about line 44) reads a producer's field list with `ast.literal_eval` on the
assignment's value. `integrations/bloomberg/pipeline/etf_daily_pull.py` now declares `HISTORY_FIELDS = ["PX_LAST", "DAY_TO_DAY_TOT_RETURN_GROSS_DVDS"]` at module
level (line 67) and, inside a function (line 622, which `ast.walk` already reaches), `RET = list(HISTORY_FIELDS)`, which is not a literal, so
ETF-history ledger rows get `cells` null with claim absent. Repair: resolve the value before
`literal_eval`: a `Name` is replaced by that name's own single module-level assignment in the same file (recursively, at most 5 deep), and a call
`list(x)` / `tuple(x)` wrapping a resolvable value is read as that value. A name with no single assignment, or a value that still is not a
non-empty list of non-empty strings, keeps raising `ValueError` as today. Add `test_name_to_literal_assignment_is_resolved_before_literal_eval` to
`test_demque_bbg_ledger_upload.py`: a temp producer source `HISTORY_FIELDS = ["A", "B"]` / `RET = list(HISTORY_FIELDS)` counts 2, and the real
`integrations/bloomberg/pipeline/etf_daily_pull.py` `RET` counts 2. The existing `test_reads_record_lines_and_converts_rows_to_cells_per_mode`
(currently failing: `[48, 64, 5, None, 2] != [48, 64, 5, 14, 2]`) must pass with no assertion changed.

**2. D1-S7, `land_cot.py`.** At import it reads three keys from its consumer's SOURCE TEXT by regex (`_consumer_literal`, lines 32-61); since
ADVI_COTBKF moved the consumer's keys onto `_legacy_key(...)` rows, the regex finds nothing, `SystemExit` fires at import, `test_demque_land.py`
cannot collect, and the whole demque pytest run ends in INTERNALERROR. Repair: read the two registry-backed keys through the SAME address the
consumer uses, `lib/opal_naming.py` `legacy_address(key)` (returns `s3://<bucket>/<template>`; read its docstring and the rows in
`infra/logic/registry/legacy_addresses.json`): `HIST_KEY` from the row `cottonwood-silver-historical-prices` and `TX_PREFIX` from the row
`cottonwood-silver-transactions-prefix`, each as the key part after `s3://<BUCKET>/` with a check that the row's bucket equals the module's
`BUCKET` (a mismatch is a loud `SystemExit`, never a default). `LOOKUP_KEY` stays read from the consumer's source, because
`config/ticker_lookup.json` has no registry row: read it with a regex over the consumer's `'key': 'config/ticker_lookup.json'` entry (open the
consumer, `data/cot/scripts/gold/build_canonical_prices_v2.py`, and match what it shows now). `_routed_bucket()` and `_consumer_path()` stay.
Add `test_consumer_keys_resolve_through_the_registry_legacy_rows` to `test_demque_land.py`: `land_cot.HIST_KEY` equals the key of
`legacy_address("cottonwood-silver-historical-prices")`, `TX_PREFIX` the key of `legacy_address("cottonwood-silver-transactions-prefix")`, and
`LOOKUP_KEY == "config/ticker_lookup.json"`. Every other test in `test_demque_land.py` keeps passing unedited.

### ACCEPTANCE

<criterion id="DQ8-t29-AC1" cell_refs="DQ-t-29"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R8_CHECKS/dq_t29_tests.py</invocation><expect>FIX-OK</expect></criterion>
<criterion id="DQ8-t29-AC2" cell_refs="DQ-t-29"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R8_CHECKS/dq_t29_land.py</invocation><expect>COLLECT-OK</expect></criterion>
`DQ8-t29-AC1` -- the named tests of both files. `DQ8-t29-AC2` -- `pytest --collect-only` over `data/mdpf/scripts/demque` exits 0 with no
INTERNALERROR and collects `test_demque_land.py`'s tests.

<expected_criteria>DQ8-t29-AC1,DQ8-t29-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `FIX-BAD not-passed=...`, `COLLECT-BAD rc=3 internalerror=True land_tests=0`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No AWS write, no Bloomberg call, no deploy.** `land_cot.py`'s `--apply` path is not run; the repair is to its key derivation only.
- **You arm no timer, background task or OS task** unless this face names one.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-D1-W23-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the
  investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/bbg_ledger_upload.py
data/mdpf/scripts/demque/test_demque_bbg_ledger_upload.py
data/mdpf/scripts/demque/land_cot.py
data/mdpf/scripts/demque/test_demque_land.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 8), cell `DQ-t-29`.
<owned_cells>DQ-t-29</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ8-t29-AC1, DQ8-t29-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~23/MDPF_DEMQUE.TO-DQ-t29.ledger-upload-and-lander-repairs.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ8-t29-AC1,DQ8-t29-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE two read-path repairs with tests.
risk: LOCAL -- code and tests.
direct_act: false -- a worker order.
</preflight>

Source: CTO round-7 analysis @f5553ca3d5 section 3 items 4 and 5; rows D1-S6, D1-S7 (REMEDIATION_v6); decomposition round 8.
