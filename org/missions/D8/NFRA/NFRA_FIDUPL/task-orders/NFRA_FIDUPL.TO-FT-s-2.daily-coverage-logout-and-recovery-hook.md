# TO NFRA_FIDUPL.TO-FT-s-2 -- daily-coverage-logout-and-recovery-hook -- coverage record, logout statuses, one recovery attempt

<to_id>NFRA_FIDUPL.TO-FT-s-2</to_id>
<project>NFRA_FIDUPL</project>
<issued_to>0.9.0_WK_NFRA_FIDUPL~5</issued_to>
<issued_by>2.0.0_SA_COO~P1</issued_by>
<issued_date>2026-10-21</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>fidelity-r3</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FT-s-2` (`decompositions/NFRA_FIDUPL_DECOMP_R3.md` section 2) | **outcome_ref:** FWD-3, FWD-9 |
**depends_on:** none (built on fakes; interfaces in reference section 12)

---

## WORKER FACE

### THE CELL

**FT-s-2** -- Make the daily run report what it covered and how it ended. Each run (1) reads the switcher list it already iterates in the attribution sweep, maps labels with `switcher_list.firm_for_label`, and writes a COVERAGE record next to the split record (counts: listed, attributed, unattributed landed under `alongside`, named by ordinal only) with the cross-check against the per-G secret (`added`, `dropped`, or `checked:false` when the secret or its config key is absent); (2) records the logout statuses the session close produced; (3) on a password refusal tries `signin_recover.recover_session` ONCE and records `recovery: attempted|succeeded|failed`, never looped.

**Read first (paths in your worktree):** `org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_R1_WORKER_REFERENCE.md` sections 1 (rules), 7 (box layout), 9 to 12 (interfaces; section 12 is this round's); `box/daily.py`, `box/run.py`, `attribute.py`, `split.py` (the split record's writer is the pattern for the coverage record), `signin.py` (`SigninError`, `Session.close`).

### WHAT TO BUILD

1. In `box/daily.py`: after the attribution sweep, build the coverage record and write it beside the split record through the same address builder and writer (`address('fidelity', <scope>, 'bronze', '_runs', <business day>, 'coverage-<run id>.json')` if that is how the split record is addressed; follow it exactly). Counts only; unattributed G numbers by ordinal. The cross-check difference is NOTED in the record and printed as counts, never fatal. A missing `perg_secret_id` or an unreadable secret gives `checked:false` and one line saying so.
2. The logout statuses: the session close already logs out (`logout statuses=a,b` in the driver's trace); read them from the session object (`session.logout_statuses` if present, else `None`) and put them in the coverage record as `logout`.
3. In `box/run.py`: where `open_session` raises a `SigninError` whose class is the refused class, call `signin_recover.recover_session(config, creds, otp)` ONCE through a lazy import (the module may not be on the box yet: an ImportError is recorded as `recovery: unavailable`); success continues the run with that session; a second failure stops the run with the refusal and `recovery: failed`. The record carries `recovery`.
4. Seven tests in `tests/test_box_daily.py` (names in the criterion), fakes for everything. Existing tests keep their names.
**Fakes only.** No AWS call, no live call, no sign-in, no real secret, no real export file; every test uses synthetic data. ASCII, Python 3.9 syntax, ruff py39 clean.

### REOPENED (issuer, 2026-10-21 ~02:15Z) -- apply your saved AttachError patch

Your row W5-S8 is right: the fix for `signin_recover.AttachError` (both it and `signin.SigninError` mean `recovery: failed`; an ImportError means `recovery: unavailable`) could not be committed under a complete order. The order is pending again so the lane grants your paths. Apply `.scratch/attach_fix.patch` in your worktree, commit, re-run `fidupl_round_checks.py ft2` and `fr4`, the whole module suite, re-pin the proof instance and flip to complete. No new test name.

### REPAIR 1 (issuer, 2026-10-21 ~02:42Z; CloudOps row D1-S10) -- run.py rejects the null account column that split.py now accepts

The first daily-mode proof run stopped at the config check, before any sign-in: `ERROR: config account_columns value for prices.txt is not a column index` (exit 2), from `box/run.py` `_check_account_columns` (about line 84). FR-s-2 REPAIR 4 lets `split.py` take `null` for `prices.txt` and `security.txt` (they have no account number in any column); `run.py`'s own pointer check was not changed with it. Change `box/run.py` and `tests/test_box_daily.py` only: `_check_account_columns` accepts `None` for `prices.txt` and `security.txt` ONLY (a null for position, balance, transact or account is still refused with the same message naming the file), and an integer still works for all six. Add ONE test to the EXISTING `tests/test_box_daily.py`: `test_check_pointers_accepts_null_account_column_only_for_prices_and_security` (a config with the measured map, account 0, position 5, balance 0, transact 0, prices null, security null, passes `check_pointers`; a null for position raises the same `ConfigError`). FT-s-2-AC1 (`ft2`) now needs eight named; FT-s-2-AC2 (`fr4`) must still pass. The whole module suite: no failure, last line in your report. Search for any OTHER place that reads `account_columns` as integers (for example `daily.py`) and report it as a row if you find one: the run on the box must get past the config check, the attribution stage and the split with the measured map. Synthetic data only. The checker is `fidupl_round_checks.py`. FAST.

### REPAIR 2 (issuer, 2026-10-21 ~03:00Z; CloudOps row D1-S11) -- the first live attribution stage raised AdapterShapeError and the run shows only the class

The daily-mode proof run (box on REPAIR 1; run `20261021T024959Z`) signed in, landed the six files (ALL_LANDED), and then `ERROR: stage attribute did not finish: AdapterShapeError`; the split and the coverage counts were skipped (the coverage record was written with null counts and the logout statuses 204 and 400). `AdapterShapeError` (adapters.py) carries a message that names ONLY response key names and value types, by design, so it is safe to show, but `box/daily.py` prints the class name only, so nobody can tell which expectation of the account lister failed against the live `accountList.json`. Change `box/daily.py` (and its tests) only: when the attribute stage raises `adapters.AdapterShapeError`, print one extra line `ERROR: attribute shape: <message>` (the exception's own message, cut to 300 characters, newlines collapsed) and put the same text in the coverage record as `attribute_error`; for ANY other exception keep printing the class name only and record `attribute_error` as the class name. The message must still hold no account number, G number or label: assert that in the test with a made-up exception whose message carries such a value and is NOT an `AdapterShapeError` (it must stay class-only). Add ONE test to the EXISTING `tests/test_box_daily.py`: `test_attribute_shape_error_message_is_printed_and_recorded_names_only`. FT-s-2-AC1 (`ft2`) now needs nine named; FT-s-2-AC2 (`fr4`) must still pass. The whole module suite: no failure, last line in your report. Synthetic data only. The checker is `fidupl_round_checks.py`. FAST: a live re-run waits on it.

### ACCEPTANCE

<criterion id="FT-s-2-AC1" cell_refs="FT-s-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py ft2</invocation><expect>R1-FT2-OK passed=\d+</expect></criterion>
`FT-s-2-AC1` -- the seven named tests exist and pass; the earlier daily tests still pass (the check runs the whole file).

<criterion id="FT-s-2-AC2" cell_refs="FT-s-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fr4</invocation><expect>R1-FR4-OK passed=\d+</expect></criterion>
`FT-s-2-AC2` -- a second criterion, with its reason: the round-2 daily-orchestration tests must still pass after the edit.

<expected_criteria>FT-s-2-AC1,FT-s-2-AC2</expected_criteria>

Dry-run at the base: `FT-s-2-AC1` base: FAIL as expected; `FT-s-2-AC2` base: PASS as expected (a control: the round-2 tests pass before the edit)

## BOUNDS

- **Grant.** The `<paths>` block below and your deliverables folder. Everything else named here you READ.
- **WORLD by the floor**, fakes in effect. Nothing runs on the box from this order.
- **Refusal clause.** A premise that fails is a surprise row in the investigation file (`NFRA_FIDUPL-D1-<your slot>-S<k>`, next unused) and you stop that piece.

<paths>
infra/aws/ec2/canonical-fidelity/box/daily.py
infra/aws/ec2/canonical-fidelity/box/run.py
infra/aws/ec2/canonical-fidelity/tests/test_box_daily.py
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP_R3.md</decomp_doc> (round 3), cell `FT-s-2`.
<owned_cells>FT-s-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FT-s-2-AC1,FT-s-2-AC2. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.9.0_WK_NFRA_FIDUPL~5/NFRA_FIDUPL.TO-FT-s-2.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FT-s-2-AC1,FT-s-2-AC2` BEFORE the flip. Commit the work first, then pin.
</proof_of_spec>

**REPORT:** the criteria with output verbatim, the proof instance, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched; denominator 0 schedules changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no grant changes; denominator 0 IAM statements changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- built on fakes; runs when the live round touches the surface.
lane: the paths block.
</preflight>

Source: CTO msgs 8891 and 8909; PRD v0.5 @c4f8dc3d51; the first landed day (run record run-20261021T012004Z).
