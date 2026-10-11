# TO ADVI_COTBKF.TO-CB-w-1.conditional-credit -- round 23 CB-w-1: class the 23 regressions; the funding credit only where no cash leg exists

<to_id>ADVI_COTBKF.TO-CB-w-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~45</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>23</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-w-1` (`decompositions/ADVI_COTBKF_DECOMP.round23.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-3: an analyst reads each Cottonwood account's return day by day, after fees, from 2013 to June 2026; strung together over a
month, the days give Commonwealth's reported monthly return, or the difference is shown with its reason; a day that cannot be worked
out is never filled in. The chain, all under `data/assets/scripts/silver/`: `commonwealth_daily_valuation.py`,
`commonwealth_daily_returns.py` + `commonwealth_flows.py`, `commonwealth_monthly_grade.py` (TOLERANCE_PCT 0.05). The two FDIC bank
sweeps (`commonwealth_sweeps.py`, sweeps-v1) are cash; their buys and sells are INTERNAL. `commonwealth_sweeps.py` `with_sweep_cash`
posts the sweep legs to CFNCASH; round 22 added `funding_credit_rows`, which, for each account and trade date with a listed-sweep buy,
credits CFNCASH the smaller of the day's non-sweep sale proceeds and the day's sweep buy. The runner `commonwealth_sweep_regrade.py`
selects the cash-leg rule per arm (`--before-cash-leg` / `--after-cash-leg`: `r19` = round 19's legs, `repaired` = with the funding
credit), persists `month_grades_before/after.parquet` and prints the round-19 movers (`deliverables/0.9.0_WK_ADVI_COTBKF~41/mover_classes.parquet`,
causes `.../~42/mover_causes.parquet`) with their result, the control, and the MATCH -> DIFF regressions by name.

Round 22's real run (`r19` -> `repaired`): `months_after=2103/1520/78970 control_same=True`; 25 of 163 movers back to MATCH (all 25
`sweep_balance`); **23 months regressed MATCH -> DIFF**, 19 in accounts acct#c42b98c0 and acct#05dd4a9d (named in
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~43/sweep_regrade.md`). The CTO's lead (row D2-S34): the credit
fires even where the vendor already posts a CFNCASH leg for the sale, which counts the proceeds twice.

**Your item (the CTO's round-22 ruling, E1).** "Fix the regressions before adding anything."
1. Class each of the 23 regressions: `double_credit` (a CFNCASH row already carries the funding sale's cash on the credited day) or
   `other:<name>`; counts summing to 23, each month named with its evidence rows, in the report.
2. A new cash-leg rule `conditional`: the funding credit applies only where no CFNCASH row for that sale already exists. One general
   rule, no account special-cased. `r19` and `repaired` stay selectable and unchanged; make `conditional` the default.
3. Re-grade `--before-cash-leg r19 --after-cash-leg conditional` (list v1 both arms). Extend the runner's LAST line by two fields,
   keeping the rest: `... control_same=<True|False> regressions=<n> movers_back=<m>`, where `regressions` counts months MATCH before and
   DIFF after, and `movers_back` counts round-19 movers MATCH after. In `sweep_regrade.md` show the 23 under the new rule and whether
   each of round 22's 25 recovered movers is still MATCH.

**AMENDMENT 1 (issuer ruling, 2026-10-08 ~20:1xZ, on row D2-W45-S1).** The first run falsified the double-credit lead: 0 of the 23 are `double_credit`; 13 (acct#05dd4a9d) carry a CFNCASH `lo` withdrawal on the credit day; 10 have no CFNCASH row, and in 9 of them the SOLD security has no value on the day before the credit day, so the credit adds proceeds to a value that never held it. The rule `conditional` becomes: the funding credit applies only where (a) the sold security was VALUED (not blank, not UNPRICED) in the account on the day before the credit day, and (b) no same-day credit-signed CFNCASH row equals the proceeds (as built). Then trace one acct#05dd4a9d month end to end (each day's cash rows, sweep legs, the credit, the value) and state, in the report and before any change, the general condition that would or would not clear it; ship that condition only if it is one general rule over row types that keeps round 22's 25 MATCH and the control unchanged. AC2 stays `regressions=0`; if it still cannot be met, refuse again with the remaining months named and their traced cause, and do not weaken the test.

**AMENDMENT 2 (issuer ruling, 2026-10-08 ~20:5xZ, on row D2-W45-S2).** Amendment 1's condition (a) is withdrawn: measured, a credit from a sale of a security not valued the day before can restore the level (round 22's 25) or inflate it (the 9), and nothing in the data separates the two until that security is priced. PRD C-DAILY decides it: "A day not computable is UNKNOWN, never interpolated." So: (a') where the funding sale's security was NOT valued in the account on the day before, the credit day's return is BLANK with the reason `UNVALUED_FUNDING_SALE` (and the month UNGRADABLE by the existing chain rule), never credited and never skipped; (b) and (c) stay as built. No condition is chosen by its result: report the variant table you measured beside this one. In `sweep_regrade.md` count round 22's 25 by their new verdict (MATCH / DIFF / UNGRADABLE) and name every month still MATCH -> DIFF with its traced cause (acct#57e741a5 2025-07's funding security 316067107 is the parked core candidate, row D2-S30). AC2 stays `regressions=0`; if it cannot be met, refuse with the remaining months named and do not weaken the test.

**AMENDMENT 3 (CTO ruling msg 1618, 2026-10-08 ~21:0xZ, on row D2-W45-S3).** "Accept acct#57e741a5 as the one named regression: it is funded by the parked 316067107 and stays labeled with that cause." AC2's expectation becomes `regressions=1`, and that one month must be acct#57e741a5 2025-07 labeled with the parked cause (D2-S30) in `sweep_regrade.md`. Record that round 22's 25 recovered months are DIFF again under `conditional`. No code change is ordered by this amendment.

Tests `data/assets/scripts/silver/tests/test_commonwealth_cash_leg.py` (add to it): a funding sale WITH an existing CFNCASH leg gets no
second credit (the value moves by the sale once); a funding sale WITHOUT one is credited (round 22's case still holds).

### ACCEPTANCE

<criterion id="CB23w1-AC1" cell_refs="CB-w-1"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_cash_leg.py</invocation><expect>passed</expect></criterion>
`CB23w1-AC1` -- an existing cash leg is not credited twice; a sale without one still is.

<criterion id="CB23w1-AC2" cell_refs="CB-w-1"><invocation>python data/assets/scripts/silver/commonwealth_sweep_regrade.py --before-list v1 --after-list v1 --before-cash-leg r19 --after-cash-leg conditional --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~45</invocation><expect>regressions=1</expect></criterion>
`CB23w1-AC2` -- the conditional credit regresses no month that matched under round 19's legs.

<criterion id="CB23w1-AC3" cell_refs="CB-w-1" judgment="true"/>
`CB23w1-AC3` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the 23 are classed with evidence rows and sum to 23; the rule is one general condition; round 22's 25 recovered movers are still MATCH and the non-sweep control is unchanged.

<expected_criteria>CB23w1-AC1,CB23w1-AC2,CB23w1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Large output under `.scratch/`, uncommitted.
- **Read-only.** No apply, no S3 write, no vendor call, no download of any kind, never bun. Read only the buckets the chain already
  reads; never `opal-data-bd`, `opal-data-49financial`, `opal-data-inf`, `opal-data-inflection` or `opal-data-demo`.
- **Blank, never filled.** A value, return or month that cannot be worked out is null with its reason, never estimated.
- **Refusal clause.** If a criterion cannot be met as written (e.g. a regression that no general condition removes), stop, write the
  reason in your report and a NEW surprise row (id `ADVI_COTBKF-D2-W45-S<k>`, `"fabric": "dell2"`, `surfaced_at` the actual UTC time),
  and do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_sweeps.py
data/assets/scripts/silver/commonwealth_sweep_regrade.py
data/assets/scripts/silver/commonwealth_daily_valuation.py
data/assets/scripts/silver/commonwealth_flows.py
data/assets/scripts/silver/commonwealth_daily_returns.py
data/assets/scripts/silver/tests/test_commonwealth_cash_leg.py
data/assets/scripts/silver/tests/test_commonwealth_sweeps.py
data/assets/scripts/silver/tests/test_commonwealth_daily_valuation.py
data/assets/scripts/silver/tests/test_commonwealth_zero_amount_flows.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round23.md</decomp_doc> (round 23), cell `CB-w-1`.
<owned_cells>CB-w-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB23w1-AC1, CB23w1-AC2, CB23w1-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~45/ADVI_COTBKF.TO-CB-w-1.conditional-credit.proof_of_spec.json`, validated
with `python .tools/proof-of-spec-check.py <instance> CB23w1-AC1,CB23w1-AC2,CB23w1-AC3` BEFORE the flip. Mechanical: CB23w1-AC1,
CB23w1-AC2; a judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the SWEEP-REGRADE line, the 23 by class with evidence, the rule (file and line), the 25 kept or not, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a local derivation run by hand.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity; BLIND: none needed.
comp-adversary: RUN -- one general condition on an existing cash leg, never an account special case; regressions counted against round 19's legs; BLIND: a regression whose cause is not the credit (it stays named under other).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-22 analysis `CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_22_20261008.md` @4899e3797f (msg 1501), section 2 and E1; row D2-S34.
