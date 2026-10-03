# TO IRPT_BCKEND.TO-IB-pr-299 -- the holdings-gold adapter never links across a missing trading day silently: it names the gap on the value (nothing served)

<to_id>IRPT_BCKEND.TO-IB-pr-299</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~102</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-03</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>36</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** CTO RULINGS batch 202 section 2 (i) (@8da55ee13b, msg 104524), relaying
3.0.0_SA_CVO's row IRPT_BCKEND-S292. The consuming half comes first because it covers every cause: a missed fire, a failed compute,
late silver. GATE (x) puts this in ROUND 36 (row S267). | **Decomp cell:** `IB-pr-299` (decomposition section 28) |
**outcome_ref:** the Performance FWD (a day the data cannot support says so) | **depends_on:** none

---

## WORKER FACE

**The hazard.**
- `infra/aws/lambda/investor-reporting/performance/holdings_gold.py:220-246` chains the daily returns of whatever `date=`
  partitions exist inside the requested window. It never compares them with the trading calendar.
- So a trading day with no partition (a missed fire, a failed compute, late silver) is linked over silently, and that day's market
  move is left out of the figure with no disclosure.
- Inflection's 2026-10-01 was the live case (row S292; the day has since been landed, row S294).

**What you build.**
1. In `holdings_gold.py`, compare the window's partitions with the trading days of `lib/trading_calendar.py` over the same window.
2. A trading day with no partition is NAMED on the value, as a disclosed absence of its own reason. When any trading day is
   missing, the value's claim is no longer `measured`. Use the module's existing claim and absence vocabulary; read it first.
3. The adapter does NOT refuse the window: a refusal would blank the page. It never links across a missing day silently.
4. Days the calendar marks as non-trading are not absences. A window wholly inside the calendar's range uses that range; read how
   the calendar bounds itself.
5. Packaging: if `lib/trading_calendar.py` is not already packaged with `irpt-performance-adapter` (read its
   `infra/aws/lambda/ci/lambda-source-map.json` entry), file a row with the member list. Do NOT edit the map: the packet stages it.
6. **Tests.** Create `performance/tests/test_holdings_gold_calendar_gap.py`, at least 3 tests, naming `trading`, `missing` and
   `measured`:
   - a window with every trading day present is unchanged (claim `measured`, no new absence);
   - a window missing one trading day names that day, and its claim is not `measured`;
   - a weekend or holiday is never named missing.

<criterion id="IB36-1-AC1" cell_refs="IB-pr-299"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r36/p36_pytest_floor.py" . IB36-1-AC1</invocation><expect>IB36-1-AC1 PASS</expect></criterion>
`IB36-1-AC1` -- the gap tests pass (at least 3). Base: FAIL (no file).

<criterion id="IB36-1-AC2" cell_refs="IB-pr-299"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r36/p36_pytest_floor.py" . IB36-1-AC2</invocation><expect>IB36-1-AC2 PASS</expect></criterion>
`IB36-1-AC2` -- the whole performance suite passes, at least 242 (239 at the base), 0 failed. Base: FAIL (239).

<expected_criteria>IB36-1-AC1,IB36-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. A second worker (IB-pr-300) is changing the holdings producer's handler. Do not touch it.
- **AWS:** none. Tests use fixtures and stubs.
- **Refusal clause.** A change to a window with every trading day present is a defect: stop and file a row. An existing test that
  moves is a defect: stop and file a row. If the response contract has no place to name the absence, file a row; do not edit a
  contract. No client name in any record.

<paths>
infra/aws/lambda/investor-reporting/performance/holdings_gold.py
infra/aws/lambda/investor-reporting/performance/tests/test_holdings_gold_calendar_gap.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~102/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read without a grant (never written): `infra/aws/lambda/investor-reporting/`, `lib/`, `org/standards/`,
`infra/aws/lambda/ci/lambda-source-map.json`.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 28 (round 36, workstream ~P), cell `IB-pr-299`.
<owned_cells>IB-pr-299</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB36-1-AC1, IB36-1-AC2. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~102/IRPT_BCKEND.TO-IB-pr-299.holdings-gold-calendar-gap-disclosure.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IB36-1-AC1,IB36-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message must give:
- the commit hashes and each criterion's last line;
- how a missing day is named and the claim it sets;
- the packaging finding;
- any surprise row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the served irpt-performance-adapter's holdings_gold.py (49 Financial and Inflection Performance); 0 served bytes move in the cell; its build and deploy are a later packet with both halves.
comp-iam: DECLARED-NOT-APPLICABLE -- no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- IB36-1-AC1 base FAIL (no file), IB36-1-AC2 base FAIL (239 < 242), dry-run at the base 2026-10-03 ~03:4xZ.
lane: the <paths> block IS the grant.
</preflight>
