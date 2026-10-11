# TO ADVI_COTBKF.TO-CB-bm-3.withholding-is-a-flow -- round 65 CB-bm-3: a tax withholding is an outflow with or without a withdrawal row; its reach measured first

<to_id>ADVI_COTBKF.TO-CB-bm-3</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~96</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>65</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bm-3` (`decompositions/ADVI_COTBKF_DECOMP.round65.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_65_20261011.md` section 3 item 3; the round-64 record
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~92/FLAGGED_DAYS.json` (class
`WITHHOLDING_WITH_NO_WITHDRAWAL_ROW`) and its `.md`; `data/assets/scripts/silver/commonwealth_flows.py` lines 150 to 230 (the
withholding rule `R25_RIDING_WITHHOLDING`, `RIDING_WITHDRAWAL_TYPE`, `rides_withdrawal`) and the file's header on how a flow rule is
versioned; `data/assets/scripts/silver/commonwealth_daily_returns.py` lines 100 to 125.

**The defect (ruled a defect of the form by the CTO).** A federal or state tax withholding (`ftax`, `stax`) counts as an external flow
ONLY when it rides a same-day cash withdrawal (`lo`). On two measured days a withholding equal to the whole balance is the only cash
leaving, there is no `lo` row, the flow reads zero and the day's return reads -100 percent. Money withheld and paid away has left the
account whether or not a withdrawal row sits beside it.

**Your item. No AWS call. You do NOT re-run the build, re-mint or serve anything; the re-mint is a later order under its own pair.**

1. FIRST measure the reach, before changing code, over the whole silver transactions cache
   (`C:/dev/ajb_workspace/.scratch/advi_cotbkf/tx_cache/trade_year=*/*.parquet`, with
   `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in the command line of anything
   that imports a commonwealth script): the account-days carrying a cash withholding row; of them, those with NO same-day `lo`; of
   THOSE, how many are measured days in `C:/dev/ajb_workspace/.scratch/advi_cotbkf/fwd3_serve_r34/daily_returns.parquet` (a non-null `return`). Counts only.
2. Make the change in `commonwealth_flows.py`, the smallest that states the rule: a cash withholding row is an external outflow
   whether or not a withdrawal rides the same day. Follow the file's OWN convention for changing a flow rule (if the file versions its
   rules, add this the way the last version was added and leave the earlier versions reproducible; say which you did and why). Fix the
   comments and the reason text that say "only where it rides".
3. Tests in `data/assets/scripts/silver/tests/` (synthetic rows only): a withholding with no `lo` is a flow; a withholding with a
   same-day `lo` is unchanged (still counted once, never twice); a day with neither is unchanged. Keep every existing assertion's `==`;
   if an existing test asserted the old rule, change its expectation and say so in your report, by name.
4. Write the reach record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~96/WITHHOLDING_FLOW_REACH.json` with exactly these keys: `withholding_account_days`, `no_withdrawal_account_days`,
   `no_withdrawal_measured_days`, `rule_change` (one sentence), `flow_rule_version` (the name the code now runs under), `tests_added`
   (names), `tests_changed` (names), `not_established`.

**If the reach is much wider than two measured days, do NOT narrow the rule to fit two: report the count. Whether a wider re-mint is
wanted is not yours to decide.**

### AMENDMENT 1 (2026-10-11T10:34, issuer `2.0.0_SA_COO~C2`) -- a NEW rule version `method_r29`, NOT the default; the grant is widened

Worker ~96 stopped at the refusal clause, correctly (row ADVI_COTBKF-D2-W96-S1): the rule is versioned, and a new version cannot be
made in `commonwealth_flows.py` alone. It measured the reach first: 4,115 account-days carry a cash withholding row; 71 of them have
no same-day cash `lo`; 7 of the 71 are measured days. **This amendment replaces step 2 of THE CELL. Steps 1, 3 and 4 stand; the reach
in step 1 is already measured and is re-used, not re-derived, unless your own run disagrees.**

**Step 2, replaced.** Add the rule as the NEXT version, `method_r29`, the way `method_r28` was added, and leave `method_r25` to
`method_r28` byte-for-byte as they are:
- `commonwealth_flows.py`: under `method_r29` a cash withholding row (`ftax`, `stax`) is an external outflow whether or not a cash `lo`
  rides the same day; under every earlier rule it rides or it is not a flow, as today. The reason text says which.
- `commonwealth_sweeps.py`: `method_r29` joins `CASH_LEGS` as a selectable leg. **`CASH_LEG_DEFAULT` stays `method_r28`.** Making a rule
  the default has been the CTO's act (its ADDENDUM 3 made r28 the default); it is not this order's.
- `commonwealth_daily_returns.py`: the consumer passes the rule to the withholding test (near line 118), and wherever the code selects
  a behaviour by `flow_rule == fl.FLOW_RULE_METHOD_R28` (near line 156, the in-kind repair) `method_r29` gets the SAME behaviour as r28:
  r29 is r28 plus this one change and drops nothing r28 does. Find every such comparison in the three files and list them in your report.
- Change nothing else in those two files.

**Tests, added to step 3:** under `method_r28` a withholding with no `lo` is still NOT a flow (the old answer, unchanged); under
`method_r29` it is; under `method_r29` every r28-only repair still applies (assert it on the in-kind repair); the default leg is still
`method_r28`.

**The record's `flow_rule_version` is `method_r29`.** Its three reach counts are 4115, 71 and 7 unless your own run disagrees, in which
case that is the refusal clause.

**Your surprise rows take the next free `ADVI_COTBKF-D2-S<k>` id**, read at write time. Append your row with a writer that adds lines
at the end of the file and rewrites nothing else: the earlier row commit changed trailing whitespace on 206 existing lines and was not
merged for that reason.

### AMENDMENT 2 (2026-10-11T10:42Z, issuer `2.0.0_SA_COO~C2`) -- the grant covers EVERY script that names the r28 rule; `method_r29` is the default (CTO msg 4734)

Worker ~96 stopped a second time, correctly (row ADVI_COTBKF-D2-W96-S2): `commonwealth_daily_valuation.py` selects the round-28
valuation repairs by comparing the cash leg against r28 (lines 875 to 898 and 939), so an r29 leg would lose the split repair and the
distribution close-step blanking. AMENDMENT 1 did not grant that file. The issuer has now taken the census it should have taken first
(`comp-find -i 'METHOD_R28|method_r28' data/assets/scripts`: 51 hits, 14 files of 407 scanned; 8 scripts and 6 tests). **This amendment
adds to AMENDMENT 1; where they differ, this one wins.**

1. **The rule, unchanged:** `method_r29` is `method_r28` plus ONE change (a cash withholding is an outflow with or without a same-day
   `lo`). It loses nothing r28 does, anywhere.
2. **How.** Wherever one of the eight granted scripts SELECTS a behaviour by comparing a leg or a flow rule against r28 (an `==`, an
   `in (...)`, a `choices=`, a default), r29 gets r28's behaviour. Prefer ONE named set defined beside the constants (the legs that
   carry the round-28 repairs: r28 and r29) and membership tests against it, over repeating `or == r29` at each site, so the next
   version is one edit. `method_r25` to `method_r28` stay byte-for-byte in behaviour.
3. **The default (this REVERSES AMENDMENT 1's "the default stays r28").** `1.0.0_SA_CTO~DELL2` ruled (msg 4734): `method_r29` becomes
   the default. Set `CASH_LEG_DEFAULT` (and any flow-rule default that follows it) to r29, and update the comment beside it to cite
   "CTO msg 4734, 2026-10-11". A test asserts the default is r29. An existing test that asserts the default is r28 changes its
   expectation; name each one in your report.
4. **The three trace and regrade scripts** (`commonwealth_div_dating_trace.py`, `commonwealth_scale_trace.py`,
   `commonwealth_sweep_regrade.py`) and `commonwealth_fwd3_serve.py`: read each r28 mention. Where it selects behaviour or refuses a
   leg that is not r28, r29 is admitted exactly as r28 is. Where it only NAMES r28 in prose about a past round, leave it. List every
   site and what you did.
5. **Nothing is run for real**: no build, no serve, no trace. The r28-versus-r29 comparison over all days is a LATER order.
6. **Tests added by this amendment:** under r29 the split repair and the close-step blanking still apply (assert on the valuation's
   selection, the way the existing split-repair test does for r28); the default leg is r29; r28 selected explicitly still gives the
   old withholding answer.
7. **Your rows are `ADVI_COTBKF-D2-W96-S<k>`** (the gate requires the worker form; the earlier text of this order named the wrong form).

### ACCEPTANCE

<criterion id="CB65bm3-AC1" cell_refs="CB-bm-3"><invocation>env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests -q</invocation><expect>passed</expect></criterion>
`CB65bm3-AC1` -- the silver suite passes with the variable unset: 0 failed, 0 errors, 12 skipped as before this order.

<criterion id="CB65bm3-AC2" cell_refs="CB-bm-3"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~96/WITHHOLDING_FLOW_REACH.json',encoding='utf-8'));print('WITHHOLDING-FLOW-RECORD withholding_account_days=%d no_withdrawal_account_days=%d no_withdrawal_measured_days=%d flow_rule_version=%s tests_added=%d tests_changed=%d'%(d['withholding_account_days'],d['no_withdrawal_account_days'],d['no_withdrawal_measured_days'],d['flow_rule_version'],len(d['tests_added']),len(d['tests_changed'])))"</invocation><expect>WITHHOLDING-FLOW-RECORD withholding_account_days=</expect></criterion>
`CB65bm3-AC2` -- the reach is recorded with its three counts, the rule's version and the tests by name. The issuer reads the counts.

<expected_criteria>CB65bm3-AC1,CB65bm3-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, your deliverables folder and the file of this order.
- **Do NOT touch:** the mint adapter (`commonwealth_account_return_daily.py`), any manifest, anything under
  `data/assets/scripts/gold/`. (AMENDMENTS 1 and 2 widened the grant to the eight scripts in the `<paths>` block, for the edits they
  name only.)
- **Do NOT run the build, `--apply` or `--verify-served`.** No AWS or S3 call. No push.
- **No gate override** of any kind and no `--force`. If a gate refuses and the fix is not an ordinary correction inside your grant,
  stop and report its exact refusal line.
- **Never print** an account id or an account's amount; the reach is counts.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row: the next
  free `ADVI_COTBKF-D2-S<k>` id read from the channel at write time, `"fabric": "dell2"`, `surfaced_at` read from the clock. Do not
  weaken or skip a test.

<paths>
data/assets/scripts/silver/commonwealth_flows.py
data/assets/scripts/silver/commonwealth_daily_returns.py
data/assets/scripts/silver/commonwealth_sweeps.py
data/assets/scripts/silver/commonwealth_daily_valuation.py
data/assets/scripts/silver/commonwealth_fwd3_serve.py
data/assets/scripts/silver/commonwealth_div_dating_trace.py
data/assets/scripts/silver/commonwealth_scale_trace.py
data/assets/scripts/silver/commonwealth_sweep_regrade.py
data/assets/scripts/silver/tests/
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round65.md</decomp_doc> (round 65), cell `CB-bm-3`.
<owned_cells>CB-bm-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB65bm3-AC1, CB65bm3-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~96/ADVI_COTBKF.TO-CB-bm-3.withholding-is-a-flow.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB65bm3-AC1,CB65bm3-AC2` BEFORE the flip. Both are mechanical.
</proof_of_spec>

**REPORT:** the three reach counts, measured BEFORE the change; the rule change in one sentence and the version it runs under; the diff of `commonwealth_flows.py`; tests added and tests changed, by name; the pytest line; the `WITHHOLDING-FLOW-RECORD` line; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE one hand-run script and its tests; nothing is re-run or served.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- the reach is measured before the change and is not pinned to two, so a wide rule shows itself; a withholding beside a withdrawal is tested as counted once; BLIND: what the changed flow does to returns on the affected days, which only the re-mint order measures.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-65 analysis @1e9128413f (msg 4715), section 4 item 3; `3.0.0_SA_CVO` REMEDIATION_v37 @054e94e8fc.
