# TO IRPT_DASHBD.TO-DB-b-13 -- FWD-8: fix the short-position income sign (S22), state the reason for the two other pairs beyond 0.35 pp, and carry the ruled tolerance in the method row (nothing served)

<to_id>IRPT_DASHBD.TO-DB-b-13</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~1</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-02</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** CTO RULINGS batch 181 (@57e16650b5, msg 104364) and its correction batch 182
(@ff0acc0bc5, msg 104375). The ruling sets `tieout_tolerance` = 0.35 percentage points per like-day window. "A reason that is an Opal
defect is a defect row: it is fixed and the pair re-measured". The tolerance is to be written into `dim_return_method` "by its
producer in the next round-4 cell". GATE (x) admits no new file into round 4 or 5, so this cell is round 6 (IRPT_BCKEND row S267).
Row IRPT_DASHBD-S22 | **Decomp cell:** `DB-b-13` (decomposition section 6) | **outcome_ref:** FWD-8 | **depends_on:** DB-b-10 (merged
@8b1df51795)

---

## WORKER FACE

**The cell.** Round 4's tie-out (`deliverables/0.9.0_WK_IRPT_DASHBD~1/TIEOUT_49F_BLACKDIAMOND_R4.{json,md}`) has 11 of 14 like-day
pairs within 0.35 pp. Three are beyond it. FWD-8 is REALIZED only when all three are dispositioned:

| account | window | abs_diff (R4) | disposition owed |
|---|---|---|---|
| acct#89d0916a | 2026-06-25..07-06 | 1.2130 pp | row S22: Opal books income +0.4627% on 06-25 where Black Diamond nets -2,470.31 on an account about 47 pct short. An Opal DEFECT: fix it and re-measure |
| acct#ffa615d2 | 2026-08-21..10-01 | 0.7078 pp | a stated, measured reason; if the reason is an Opal defect, fix it and re-measure |
| acct#89d0916a | 2026-04-09..04-30 | 0.4555 pp | a stated, measured reason; same rule |

**What you build.**
1. **S22 fix.** In `data/assets/scripts/gold/irpt_reporting/account_return_daily.py`, income (`:662`, `INCOME_CATEGORY_RE` over
   cash rows) must carry the sign of what the account received or paid. A dividend PAID on a short position is negative income,
   never positive. Read the account's Schwab transactions for 06-25 to see how a short's dividend is coded. Fix the treatment by
   the code, not by account. Long positions' income does not move.
2. **The two reasons.** Measure each window: day by day, Opal against Black Diamond's response (flows, income timing, the share of
   the window in withheld or edge days), and state the reason in one sentence each with its number. A reason that turns out to be
   an Opal defect is fixed here too, or filed as a row if it is outside this file.
3. **The tolerance in the method row.** `emit_method_row` (`:1660`) writes `tieout_tolerance` = 0.0035 (0.35 pp) and
   `tieout_tolerance_ruling` = "1.0.0_SA_CTO RULINGS batch 181". `tieout_tolerance_proposed` is kept as it is (null) unless the
   row's contract says otherwise, in which case file a row. The served write of the row is the issuer's packet.
4. **Re-measure with NO vendor call.** Recompute Opal's side for the three windows with the fixed producer, locally and reading
   only. BD's side is the stored round-4 responses (`RAW_BD_PERIOD_<account>.sanitised.json.gz`). Write
   `TIEOUT_49F_BLACKDIAMOND_R6.json`:
   `{"tolerance": 0.0035, "vendor_calls": 0, "pairs": [{"account","start","end","abs_diff_r4","abs_diff_now","reason","defect","fixed"}]}`,
   plus a short `.md`.
5. **Tests.** Create `data/assets/scripts/gold/irpt_reporting/tests/test_short_income_and_tolerance.py`, at least 4 tests,
   naming `short`, `income` and `tieout_tolerance`:
   - a short position's paid dividend is negative income;
   - a long dividend is unchanged;
   - an account with no short position computes exactly as before;
   - the method row carries 0.0035 and the ruling.

<criterion id="DB6-1-AC1" cell_refs="DB-b-13"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r6/p6_1_ac1_short_income_tests.py" .</invocation><expect>DB6-1-AC1 PASS</expect></criterion>
`DB6-1-AC1` -- the short-income and tolerance tests pass (at least 4). Base: FAIL (no file).

<criterion id="DB6-1-AC2" cell_refs="DB-b-13"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r6/p6_1_ac2_three_pairs_dispositioned.py" .</invocation><expect>DB6-1-AC2 PASS</expect></criterion>
`DB6-1-AC2` -- the three pairs each carry a reason. S22 is recorded fixed and re-measured, with 0 vendor calls. Base: FAIL (no
record).

<criterion id="DB6-1-AC3" cell_refs="DB-b-13"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r5/p5_ac3_suites_unchanged.py" . DB6-1-AC3</invocation><expect>DB6-1-AC3 PASS</expect></criterion>
`DB6-1-AC3` -- reporting-gold and reporting-publish suites pass unchanged. Base: PASS (a regression guard).

<expected_criteria>DB6-1-AC1,DB6-1-AC2,DB6-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** reads only. No S3 write, no upload, no deploy. **No vendor call** of any kind: Black Diamond's side is the stored round-4
  responses.
- **Refusal clause.** A fix that moves a long-only account's income or any account without a short position is a defect: stop and
  file a row. A reason you cannot measure is said, never guessed. No client name in any record; ids only.

<paths>
data/assets/scripts/gold/irpt_reporting/account_return_daily.py
data/assets/scripts/gold/irpt_reporting/tests/test_short_income_and_tolerance.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r6/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read without a grant (never written): `data/assets/scripts/`, `infra/aws/lambda/investor-reporting/`, `lib/`,
`org/tier1_exec/4.0.0_SA_CRO/deliverables/SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811.json`.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 6 (round 6, workstream B), cell `DB-b-13`.
<owned_cells>DB-b-13</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB6-1-AC1, DB6-1-AC2, DB6-1-AC3. Instance at `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/IRPT_DASHBD.TO-DB-b-13.fwd8-three-pairs-and-tolerance.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DB6-1-AC1,DB6-1-AC2,DB6-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message must give:
- the commit hashes and each criterion's last line;
- the S22 fix in two lines;
- each pair's reason and its abs_diff now;
- any surprise row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the reporting gold producer (packaged into irpt-49f-reporting-gold-lambda by pins) and its method row; 0 served bytes move in the cell; the re-pin, the gold rewrite of affected account-days and the method row's served write are the issuer's packet with both halves.
comp-iam: DECLARED-NOT-APPLICABLE -- no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the 07:41 ET reporting gold schedule is not moved.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB6-1-AC1 base FAIL (no file), DB6-1-AC2 base FAIL (no record), DB6-1-AC3 base PASS (regression guard), dry-run at the base 2026-10-02 ~19:2xZ.
lane: the <paths> block IS the grant.
</preflight>
