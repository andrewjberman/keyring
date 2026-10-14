# ETFS_RIVALS task order -- `RIV-xf-1` -- ACWI and IWM are removed from the universe and from the holdings pull (Andrew's DEMQUE form A3, row Z4; CTO msgs 4932 and 4969)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-xf-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~42</issued_to>
<issued_by>2.0.0_SA_COO~V1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell; no S3 or deploy act
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work; at the cut nothing is returned, and the evidence context is this order's check file (dry-run at the base: FAIL as expected)
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric dell1) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two
peer groups): rankings, buying trend, AI accounts, a security dialog per holding, and an audit page.
Code: `data/etfs/scripts/rivalfunds/` (run from `data/etfs/scripts`, package `rivalfunds`); tests:
`data/etfs/scripts/rivalfunds/tests/` (pytest from `data/etfs/scripts`).

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-xf-1` -- ACWI and IWM are removed from the universe and from the holdings pull (Andrew's DEMQUE form A3, row Z4; CTO msgs 4932 and 4969) -- APPENDED 2026-10-14, revision 1.31
- Placement: this seat's staged cell (`round30_prep/STAGED_CELL_enrichment_trading_gate_and_queue_reader.md`, xf-1); CTO msgs 4932 and 4969; form `org/tier1_exec/1.0.0_SA_CTO/deliverables/DEMQUE_QUEUE_FORM_ANDREW_20261013.md` A3 and row Z4.
- Measured (box/dell1): `peer_groups.json` (map_version 2, 15 entries) carries ACWI (group IDVZ) and IWM (group PFOE) as `role: index_control`, `"leg": "pending"`; with `leg_gates.json` reading ENABLE 0, D12 1, D13 0 they are dropped from
  `universe.funds()` (13 funds) and never pulled, so served output does not move. `bbg_budget.json` still sizes them (`est_rows_per_fund_date`: ACWI 2198, IWM 1979). The 2026-10-13 owed read: units whose only holders are ACWI or IWM: 0.
- Interface: delete the two entries from `data/etfs/scripts/rivalfunds/peer_groups.json` (every other entry and `map_version` unchanged); delete the `ACWI` and `IWM` keys of `est_rows_per_fund_date` in `data/etfs/scripts/rivalfunds/bbg_budget.json`
  (every other key and value unchanged). The generic machinery stays: the `index_control` role value, the `"leg": "pending"` mechanism, the gates, `collector_bloomberg.CONTROL_ROW_CAP` and `split_units`, because no served output depends on them and a
  benchmark may return as a map entry. Rewrite the tests that name the two funds to the new facts (a map entry for a benchmark is exercised through a synthetic map or a monkeypatched `_is_control`, never the shipped map).
- Out of bounds: `universe.py`, `collector_bloomberg.py` (code), every other map entry, any gate value in `leg_gates.json`, any S3 or vendor call.
- Checks: `round30/checks/xf1_acwi_iwm_removed_check.py` (AC1 in four gate states no ACWI or IWM and the same 13 funds; AC2 the holdings plan with every gate on is the 7 bloomberg_primary funds in one unit (AMENDMENT 1, issuer, row W42-S1: `request_plan` plans the `bloomberg_primary` funds only, 7 with ENABLE on, so the prior plan was these 7 plus ACWI and IWM and the change removes exactly the two); AC3 the budget config no longer sizes the two funds;
  base FAIL 5, the all-gates-off control PASS = DELTA 0) and the tests you rewrite (AC4: the three test files below, green). J1: none (a LOCAL cell; the deploy is site Z's under the CTO~Z half).

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base box/dell1)

- Read the check before you build: `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round30/checks/xf1_acwi_iwm_removed_check.py`. It FAILS at the base (5 failed, 1 passed) and is your target; do not edit it.
- Tests that name the funds and will break, to be rewritten to the new facts: `tests/test_r5l1_leg_inert.py` (`test_gate_set_joins` asserts `ctl == ["ACWI", "IWM"]` and the plan holds them), `tests/test_r8lg1_leg.py` (the D13 tests admit the benchmarks;
  `test_split_units_queries_each_control_alone` and the cap tests use them: drive them through a monkeypatched `cb._is_control` and plain fund names, or retire a test whose whole subject was the two funds, saying which), and
  `tests/test_r9cb1_bbg_budget.py:102` (`{"ACWI", "IWM", "IDVZ", "PFOE", "default"} <= set(...)` becomes `{"IDVZ", "PFOE", "default"}`). List every assertion you changed or retired and why.
- Read `universe.load` before editing the map: the loader validates the map (one home per group, one `map_version`, entries need every field).

## 3. SURFACES AND BOUNDS

You READ (never edit): every file not in your `<paths>`, including `lib/`, `integrations/`, Terraform, the decomposition and
the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md`.

You WRITE only the `<paths>` below (plus `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~42/`).
NEVER: any S3 read or write outside a LocalSink or memory sink, any deploy, gateway release or Terraform, any vendor call
(Bloomberg, OpenAI, Bright Data or any live web search), any Secrets Manager call, any environment gate flip outside a test.
A row you file goes in the investigation file below with id `ETFS_RIVALS-D1-W42-S<k>`, `"fabric": "dell1"`.

<paths>
data/etfs/scripts/rivalfunds/peer_groups.json
data/etfs/scripts/rivalfunds/bbg_budget.json
data/etfs/scripts/rivalfunds/tests/test_r5l1_leg_inert.py
data/etfs/scripts/rivalfunds/tests/test_r8lg1_leg.py
data/etfs/scripts/rivalfunds/tests/test_r9cb1_bbg_budget.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.dell1.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from the repository root)

- **AC1** -- no gate state brings ACWI or IWM back, and the 13 funds are unchanged.
- **AC2** -- the holdings plan with every gate on is the 7 bloomberg_primary funds in one unit.
- **AC3** -- the budget config no longer sizes the two funds.
- **AC4** -- the three rewritten test files are green (a fourth criterion: this cell rewrites existing tests).
<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-xf-1"><invocation>cd data/etfs/scripts; python -m pytest -q -p no:cacheprovider ../../../org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round30/checks/xf1_acwi_iwm_removed_check.py -k ac1</invocation><expect>4 passed</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-xf-1"><invocation>cd data/etfs/scripts; python -m pytest -q -p no:cacheprovider ../../../org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round30/checks/xf1_acwi_iwm_removed_check.py -k ac2</invocation><expect>1 passed</expect></criterion>
  <criterion id="AC3" cell_refs="RIV-xf-1"><invocation>cd data/etfs/scripts; python -m pytest -q -p no:cacheprovider ../../../org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round30/checks/xf1_acwi_iwm_removed_check.py -k ac3</invocation><expect>1 passed</expect></criterion>
  <criterion id="AC4" cell_refs="RIV-xf-1"><invocation>cd data/etfs/scripts; python -m pytest -q -p no:cacheprovider rivalfunds/tests/test_r5l1_leg_inert.py rivalfunds/tests/test_r8lg1_leg.py rivalfunds/tests/test_r9cb1_bbg_budget.py</invocation><expect>the final line reads N passed with no failed and no error</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Run the rivalfunds suite (`python -m pytest -q rivalfunds/tests` from `data/etfs/scripts`) and report its final line.
Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~42/ETFS_RIVALS.TO-RIV-xf-1.acwi-iwm-removed.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-xf-1.acwi-iwm-removed`. Report once: each criterion's verdict line with the output above it;
files written; every existing test assertion you changed or retired and why; rows filed (id + one line); anything the issuer must do at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L6, 2.0.0_SA_COO~V1):** Round 30, workstream `sz`, ONE issuance on the round-29 analysis section 3 item 3 and the CTO's msgs 4568, 4932, 4969, 5577. Decomposition revision 1.31.
Check file(s) dry-run at the base before the cut (see the issuance commit). Chain C (`peer_groups.json`, `bbg_budget.json` and three test files); no edge to xe-1, xe-2 or xe-3.
The deploy is not a worker's act: xe-3 a Lambda deploy under its own pair (and the issuer's DELTA = 0 live-store read before it), xe-1 and xf-1 site Z's under `1.0.0_SA_CTO~Z`'s half.

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>pending</status>
<round>30</round>
<workstream>5</workstream>
<slot>~42</slot>
<fabric>dell1</fabric>
