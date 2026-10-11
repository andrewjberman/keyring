# TO IRPT_DASHBD.TO-DB-b-15 -- FWD-8: C-VALUE becomes the account's equity (net_mv_plus_cash + margin_balance) as a new method_version, with all 14 pairs, the population figure and the guard re-measured (nothing served)

<to_id>IRPT_DASHBD.TO-DB-b-15</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~2</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-03</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** CTO RULINGS batch 193 (@ff04f71e47, msg 104467), answering row
IRPT_DASHBD-W1-S18. C-VALUE is the account's EQUITY, `net_mv_plus_cash + margin_balance`. It is ONE rule for every account and a new
`method_version`, and all 14 pairs, the population figure and the guard are re-measured. GATE (x) refuses a new file into round 7,
so this is ROUND 8 (IRPT_BCKEND row S267). | **Decomp cell:** `DB-b-15` (decomposition section 8) | **outcome_ref:** FWD-8 |
**depends_on:** DB-b-13 (merged @9a169d31ad)

---

## WORKER FACE

**The ruling.** C-VALUE is the account's equity, its net liquidation value: `net_mv_plus_cash + margin_balance`.
- The margin balance is signed as the custodian reports it, so a debit reduces value.
- It is ONE rule for every account. An account with no margin carries `margin_balance = 0` and does not move. Mint no margin
  special case.
- Black Diamond's accrual stays OUTSIDE Opal's figure, because Opal books income on receipt. That difference is stated per pair.

Round 6 measured the ground (`deliverables/0.9.0_WK_IRPT_DASHBD~1/DECOMPOSE_THREE_PAIRS_R6.json`). At 6 of 6 window endpoints, Black
Diamond's value = `net_mv_plus_cash + margin_balance` + its own accrual.

**What you build.**
1. **The value basis, as data.** In `data/assets/scripts/gold/irpt_reporting/sources.json`, declare the account value as the equity
   sum of `net_mv_plus_cash` and `margin_balance`. A list of columns is one shape; choose the clearest. Rewrite the comment to cite
   batch 193.
   - In `data/assets/scripts/gold/irpt_reporting/account_return_daily.py`, read it everywhere the value is read today (the
     balance reads near `:757`, `:789`, `:807`).
   - Read the custodian's sign as stored. Confirm the sign on the three round-6 accounts before you rely on it.
   - A null `margin_balance` is never silently zero. Count such rows; if any exist, file a row with the count and say how the
     day is treated.
2. **The method version.** Raise `METHOD_VERSION` (`:98`) by one. `emit_method_row` records the new version and its basis, citing
   "1.0.0_SA_CTO RULINGS batch 193". The tolerance fields DB-b-13 added stay as they are.
3. **Re-measure ALL 14 pairs, with NO vendor call.**
   - Black Diamond's side is the stored round-4 responses: `deliverables/0.9.0_WK_IRPT_DASHBD~1/RAW_BD_PERIOD_<account>.sanitised.json.gz`
     and `TIEOUT_49F_BLACKDIAMOND_R4.json`.
   - Opal's side is the producer in your worktree, run locally and reading only. `remeasure_three_pairs_r6.py` and
     `decompose_three_pairs_r6.py` in the same folder are the round-6 tools; reuse what fits.
   - Write `deliverables/0.9.0_WK_IRPT_DASHBD~2/TIEOUT_49F_BLACKDIAMOND_R8.json` with this shape:
     `{"tolerance": 0.0035, "vendor_calls": 0, "method_version": <new>, "pairs": [{"account","start","end","abs_diff_r4","abs_diff_now","bd_accrual","within","reason"}], "s22": {"account","start","residual","disposition","reason"}}`
   - `bd_accrual` is Black Diamond's accrual over the window. `within` is `abs_diff_now <= 0.0035`. A pair beyond it carries a
     measured reason. Add a short `.md` beside the record.
   - **S22 re-read:** pair acct#89d0916a 2026-06-25 is DISARMED if its residual is within 0.35 pp. Otherwise it is RESTATED, with the
     residual and its measured reason. Round 6 found a 4,429.53 `INTRA/FC/IN` "MARGIN INT ADJ" credit (row W1-S20). CTO batch 195
     (@8dcb24b212) ruled it RETURN: margin interest is internal, and its adjustment takes the same side. Do NOT re-class it. If the
     pair's residual is that credit, state it as the non-defect reason: "Black Diamond books MARGIN INT ADJ as a net addition; Opal
     keeps margin interest internal by ruling (batch 195)".
4. **The population figure and the guard, on 2026-10-01.**
   - DB-b-11 measured 6,685 of the 7,570 population accounts with a positive value on that day under the old basis
     (`P2_SCALE_R5.json`). Re-measure it under equity.
   - Run the producer for that day under both versions. Count C-GUARD's `guard_state` per state for each.
   - Prove the one rule: every account whose `margin_balance` is 0 that day computes identical rows under both versions, apart
     from `method_version`.
   - Write `deliverables/0.9.0_WK_IRPT_DASHBD~2/POPULATION_EQUITY_R8.json` with this shape:
     `{"day": "2026-10-01", "accounts": 7570, "positive_before": 6685, "positive_after", "guard_state_before": {}, "guard_state_after": {}, "zero_margin_accounts", "zero_margin_rows_changed", "null_margin_balance_rows"}`
5. **Tests.** Create `data/assets/scripts/gold/irpt_reporting/tests/test_account_equity_value.py`, at least 4 tests, naming
   `equity`, `margin_balance` and `method_version`:
   - the value is `net_mv_plus_cash + margin_balance`, and a debit balance reduces it;
   - an account with `margin_balance` 0 computes exactly as before;
   - a null `margin_balance` is not read as zero;
   - the method row carries the new version and the batch 193 citation.

<criterion id="DB8-1-AC1" cell_refs="DB-b-15"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r8/p8_1_ac1_equity_value_tests.py" .</invocation><expect>DB8-1-AC1 PASS</expect></criterion>
`DB8-1-AC1` -- the equity value tests pass (at least 4). Base: FAIL (no file).

<criterion id="DB8-1-AC2" cell_refs="DB-b-15"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r8/p8_1_ac2_fourteen_pairs_population_guard.py" .</invocation><expect>DB8-1-AC2 PASS</expect></criterion>
`DB8-1-AC2` -- the R8 record covers exactly round 4's 14 pairs, and every pair beyond 0.35 pp has a reason. S22's disposition
matches its residual. The population record shows positive 6,685 before, a guard census before and after over the same rows, and 0
zero-margin rows changed. 0 vendor calls. Base: FAIL (no record).

<criterion id="DB8-1-AC3" cell_refs="DB-b-15"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r5/p5_ac3_suites_unchanged.py" . DB8-1-AC3</invocation><expect>DB8-1-AC3 PASS</expect></criterion>
`DB8-1-AC3` -- reporting-gold and reporting-publish suites pass unchanged. Base: PASS (a regression guard).

<expected_criteria>DB8-1-AC1,DB8-1-AC2,DB8-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Do not touch `infra/`: the reporting Lambdas and the publish role are DB-b-14's, complete.
- **AWS:** reads only. No S3 write, no upload, no deploy. **No vendor call** of any kind: Black Diamond's side is the stored round-4
  responses.
- **Refusal clause.** A change that moves an account whose `margin_balance` is 0 is a defect: stop and file a row. An existing test
  that moves is a defect: stop and file a row. A reason you cannot measure is said, never guessed. No client name in any record;
  ids only.

<paths>
data/assets/scripts/gold/irpt_reporting/account_return_daily.py
data/assets/scripts/gold/irpt_reporting/sources.json
data/assets/scripts/gold/irpt_reporting/tests/test_account_equity_value.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r8/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read without a grant (never written): `data/assets/scripts/`, `infra/aws/lambda/investor-reporting/`, `lib/`,
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/`.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 8 (round 8, workstream B), cell `DB-b-15`.
<owned_cells>DB-b-15</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB8-1-AC1, DB8-1-AC2, DB8-1-AC3. Instance at `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2/IRPT_DASHBD.TO-DB-b-15.c-value-account-equity-remeasure.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DB8-1-AC1,DB8-1-AC2,DB8-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message must give:
- the commit hashes and each criterion's last line;
- the value basis as declared and the sign check;
- the 14 pairs, as abs_diff now and bd_accrual, with those beyond 0.35 pp and their reasons;
- S22's disposition;
- the population and guard numbers before and after;
- any surprise row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the reporting gold producer (packaged into irpt-49f-reporting-gold-lambda by pins), its source declaration and its method row; 0 served bytes move in the cell. The re-pin, the gold rewrite of every landed day under the new method_version (the publisher refuses a file of mixed method_version, publisher.py:173), and the method row's served write are the issuer's P-2 packet with both halves.
comp-iam: DECLARED-NOT-APPLICABLE -- no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the 07:41 ET reporting gold schedule is not moved.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB8-1-AC1 base FAIL (no file), DB8-1-AC2 base FAIL (no record), DB8-1-AC3 base PASS (regression guard), dry-run at the base 2026-10-03 ~00:1xZ.
lane: the <paths> block IS the grant.
</preflight>
