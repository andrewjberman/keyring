# TO IRPT_BCKEND.TO-IB-pr-300 -- the holdings producer's scheduled fire catches up every missed trading day, at most 5 per fire (nothing served)

<to_id>IRPT_BCKEND.TO-IB-pr-300</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~103</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-03</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>36</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** CTO RULINGS batch 202 section 2 (ii) (@8da55ee13b, msg 104524), on row
IRPT_BCKEND-S292. Cut beside IB-pr-299 in ROUND 36 (GATE (x), row S267). | **Decomp cell:** `IB-pr-300` (decomposition section 28) |
**outcome_ref:** the Performance FWD (the gold carries every trading day) | **depends_on:** none

---

## WORKER FACE

**The hazard.**
- `infra/aws/lambda/investor-reporting/holdings-performance/handler.py` `_target_day` computes exactly ONE day per scheduled fire:
  `prev_trading_day(expected_last_trading_day(now))`.
- A fire that is missed, or a schedule created after a day's slot, leaves that day missing FOREVER.
- Inflection's 2026-10-01 was the live case (row S292; landed by hand, row S294).
- The same handler serves both firms: `irpt-holdings-performance-lambda` for 49 Financial and `irpt-inf-holdings-performance-lambda`
  for Inflection, with `source` in the event.

**What you build.**
1. A scheduled fire (an event WITHOUT `date`) computes every trading day from the day after the newest landed gold partition
   through that same T-1, oldest first, at most 5 trading days per fire.
   - Read the newest landed partition for the event's source at the address the producer itself writes (`lib/opal_naming.py`
     `address()`).
   - A day whose silver does not yet hold the close stops the catch-up at that day. Never skip over it: the next fire retries.
   - A missed fire then heals on the next one. The fire stays scheduled; only its window widens.
   - Each write is a NEW key; never rewrite a landed partition.
2. An event WITH `date` (the manual and QA path) is unchanged: exactly that one day.
3. With no gap, a scheduled fire computes exactly the one day it computes today. Prove it in a test.
4. **Do NOT edit the producer** (`data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py`). Call it as the
   handler does today, once per day or with its own range arguments if it has them (read its argument parser).
5. **Tests.** Create `infra/aws/lambda/investor-reporting/holdings-performance/tests/test_catch_up.py`, with a stubbed listing and a
   stubbed producer call, at least 4 tests, naming `catch`, `trading` and `missed`:
   - no gap: one day;
   - one missed trading day: both days, oldest first;
   - a gap longer than 5: exactly the oldest 5;
   - an explicit `date`: unchanged;
   - a day without silver: stops there.

<criterion id="IB36-2-AC1" cell_refs="IB-pr-300"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r36/p36_pytest_floor.py" . IB36-2-AC1</invocation><expect>IB36-2-AC1 PASS</expect></criterion>
`IB36-2-AC1` -- the catch-up tests pass (at least 4). Base: FAIL (no file).

<criterion id="IB36-2-AC2" cell_refs="IB-pr-300"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r36/p36_pytest_floor.py" . IB36-2-AC2</invocation><expect>IB36-2-AC2 PASS</expect></criterion>
`IB36-2-AC2` -- the producer's own suite passes unchanged: at least 60, 0 failed. Base: PASS (a guard).

<expected_criteria>IB36-2-AC1,IB36-2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. A second worker (IB-pr-299) is changing the performance adapter. Do not touch it, and do not
  edit the producer.
- **AWS:** S3 READS only, if you need to see a real listing. No write, no invoke, no deploy.
- **Refusal clause.** A scheduled fire with no gap that computes anything other than today's one day is a defect: stop and file a
  row. Any rewrite of a landed partition is a defect. No client name in any record.

<paths>
infra/aws/lambda/investor-reporting/holdings-performance/handler.py
infra/aws/lambda/investor-reporting/holdings-performance/tests/test_catch_up.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~103/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read without a grant (never written): `data/assets/scripts/gold/irpt_holdings_performance/`, `lib/`,
`infra/aws/terraform/investor-reporting/holdings-performance/`, `infra/aws/lambda/ci/lambda-source-map.json`.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 28 (round 36, workstream ~P), cell `IB-pr-300`.
<owned_cells>IB-pr-300</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB36-2-AC1, IB36-2-AC2. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~103/IRPT_BCKEND.TO-IB-pr-300.holdings-producer-catch-up.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IB36-2-AC1,IB36-2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message must give:
- the commit hashes and each criterion's last line;
- the catch-up rule as coded, with its stop condition;
- how the newest landed day is read;
- any surprise row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the handler shared by irpt-holdings-performance-lambda (49F) and irpt-inf-holdings-performance-lambda (Inflection); 0 served bytes move in the cell; the builds and deploys are a later packet with both halves (each catch-up write is a new key).
comp-iam: DECLARED-NOT-APPLICABLE -- the roles already list and read their own gold prefix; if a listing grant is missing, that is a row.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the 14:00Z (Inflection) and 49F schedules are not moved; only a fire's computed window widens.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- IB36-2-AC1 base FAIL (no file), IB36-2-AC2 base PASS (60, a guard), dry-run at the base 2026-10-03 ~03:4xZ.
lane: the <paths> block IS the grant.
</preflight>
