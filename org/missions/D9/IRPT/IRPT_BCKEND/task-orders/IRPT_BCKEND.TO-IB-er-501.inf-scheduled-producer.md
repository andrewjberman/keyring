# TO IRPT_BCKEND.TO-IB-er-501 -- The Inflection holdings producer runs on its own schedule, function and role

<to_id>IRPT_BCKEND.TO-IB-er-501</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~80</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-09-29</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>~E</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** 1.0.0_SA_CTO 102832 (S205 half: an INF switch needs a SCHEDULED
producer and fire) and decomposition section 19 (the daily runner's widening, named there) | **Decomp cell:**
`IB-er-501` (decomposition section 21) | **outcome_ref:** FWD-3 (INF) | **depends_on:** none

---

## WORKER FACE

**The cell.** The holdings-basis gold producer
`C:/Users/AndrewBerman/Desktop/wk-irpt-p-80/data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py`
(DS-owned; do NOT edit it) computes one custody source per run (`--source <key>`). Its declaration `sources.json` has
three keys: `schwab_08335338` (49F), `orion` (Inflection) and `blackdiamond_z09` (Cottonwood).

Today ONE Terraform root schedules it for 49F only:
`C:/Users/AndrewBerman/Desktop/wk-irpt-p-80/infra/aws/terraform/investor-reporting/holdings-performance/`
(main.tf, lambda.tf, iam.tf, locals.tf, schedule.tf). Its Lambda handler is
`infra/aws/lambda/investor-reporting/holdings-performance/handler.py`. The schedule's input carries
`source = "schwab_08335338"`, and `locals.tf` derives the role's grants from declared sources that carry `master`.

Your change: the same root also schedules `orion`, under its OWN Lambda function, role and schedule.
- **Firm isolation:** no single role reads or writes two firms' data. Reuse the same artifact for the new function
  (the Lambda module's S3 key). A `for_each` over the scheduled source keys is welcome, as long as the existing 49F
  resources keep their addresses: use `moved` blocks if you restructure, and the plan must destroy nothing.
- **What the INF role reads:** the `orion` entry's silver. Its `positions_prefix` is the template
  `{monolith}/{scope}/silver/fact_positions/` on `opal-data-assets`, `balance_prefix` is null, and the scope is the ONE
  registry scope whose monolith is `orion`. Derive it from `infra/logic/registry/scopes.json` the way the producer's
  `firm_scope()` does.
- **What the INF role writes:** the Inflection gold. Its prefixes are
  `irpt/inflection/gold/holdings_performance_{daily,manifest}/` in the firm's gold bucket. Derive every address from
  the registry or builder, never typed: the commit-time naming gate refuses a typed firm token in `.tf`.
- **The INF schedule input:** `{kind, note, source = "orion"}`.
- **The INF fire time:** measure when `orion/<scope>/silver/fact_positions/date=D/` lands (S3 LastModified over the
  last 10 trading days) and fire after the worst case with margin.
  - `handler.py` targets `prev_trading_day(expected_last_trading_day(now))`, which fits a next-morning landing.
  - If Inflection's landing breaks that rule, file a surprise row with the measurement and stop on it; do not edit
    the handler.
- Cottonwood (`blackdiamond_z09`) is NOT in this cell.
- Plan only: no apply, no invoke, no upload. Run terraform from PATH (v1.14+); `.tools/terraform.exe` v1.9.8 cannot
  evaluate `locals.tf`.

<criterion id="E5-AC1" cell_refs="IB-er-501"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/e5/e5_ac1_inf_scheduled_producer_plan.py" .</invocation><expect>E5-AC1 PASS</expect></criterion>
`E5-AC1` -- the plan reads as follows:
- it CREATES exactly one schedule whose input has `source == "orion"`;
- the policies name an `orion/` silver prefix and the INF gold prefix;
- no policy names `blackdiamond`, and no single policy grants both firms' gold;
- nothing is destroyed.
Base: FAIL (no orion schedule).

<expected_criteria>E5-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **No deploy, no AWS write.** The plan uses `-lock=false`. The served move is the issuer's, under both never-widen
  halves.
- **Refusal clause.** If the criterion cannot be met as written, stop, write the reason in your report and a surprise
  row, and do not weaken the check.

<paths>
infra/aws/terraform/investor-reporting/holdings-performance/main.tf
infra/aws/terraform/investor-reporting/holdings-performance/lambda.tf
infra/aws/terraform/investor-reporting/holdings-performance/iam.tf
infra/aws/terraform/investor-reporting/holdings-performance/locals.tf
infra/aws/terraform/investor-reporting/holdings-performance/schedule.tf
infra/aws/terraform/investor-reporting/holdings-performance/moved.tf
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 21 (round 5, workstream ~E), cell `IB-er-501`.
<owned_cells>IB-er-501</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: E5-AC1. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~80/IRPT_BCKEND.TO-IB-er-501.inf-scheduled-producer.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> E5-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message: the commit hash, the criterion's last line, the measured INF landing times and the fire
time you chose, and any surprise row id (`IRPT_BCKEND-W80-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- one new EventBridge schedule (Inflection), plan only; the 49F schedule keeps its address.
comp-iam: RUN -- one new role, read orion silver + write INF gold, derived from the registry; no grant is added to the 49F role.
comp-blast: RUN -- the new function writes only the Inflection holdings gold, which no served path reads until the INF switch (pr-221) ships under its own halves.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache.
comp-adversary: RUN -- E5-AC1 dry-run at the base: FAIL (no orion schedule); positive control on the live plan: the policy reader finds the 49F gold prefix and the schwab silver prefix (2 policies read).
lane: the <paths> block IS the grant.
</preflight>
