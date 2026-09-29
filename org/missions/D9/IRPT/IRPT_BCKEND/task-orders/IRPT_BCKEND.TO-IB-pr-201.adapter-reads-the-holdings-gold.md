# TO IRPT_BCKEND.TO-IB-pr-201 -- The Performance adapter reads the holdings-basis gold for 49F (thread hop 2; PRD v0.19 rulings 10-12)

<to_id>IRPT_BCKEND.TO-IB-pr-201</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~77</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-09-29</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>20</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cells:** `IB-pr-201`, `IB-pr-202` (decomposition section 15) |
**outcome_ref:** FWD-3 (thread hop 2: gold -> adapter) | **depends_on:** ~E round 1 (TO-IB-er-201, complete: the gold
for account 0010498003, 184 YTD partitions)

---

## WORKER FACE

**AMENDMENT 2 (2026-09-29 ~11:2xZ, issuer, on 1.0.0_SA_CTO 102736 / 102746 and 4.0.0_SA_CRO 102735 / 102737) -- REOPENED
for ONE fix; this is the whole of your work.** The switch built here (drained @a595a14264, served as hD7G6YT1 at
10:14Z) was ROLLED BACK at 10:58Z: every served 49F YTD/QTD/1Y answered UNEXPECTED with
`ModuleNotFoundError: No module named 'parity_period_returns'`.
- Before the switch, `installed._engine_source()` put `data/assets/scripts/gold/runners_49f` on `sys.path`.
- `installed._holdings_source()` replaced it and inserts nothing.
- `holdings_gold._period_for` -> `f49_engine.ruled_period_for` still lazily imports `parity_period_returns`, which the
  zip carries at `data/assets/scripts/gold/runners_49f/`.
- Since inception skips `_period_for`, so the cold start and the since-inception answer passed.

**Build (49F ALONE, CTO 102746: no Inflection change rides this artifact):** in
`C:/Users/AndrewBerman/Desktop/ajb_workspace/infra/aws/lambda/investor-reporting/performance/installed.py`, make
`build_runtime` put the packaged `data/assets/scripts/gold/runners_49f` directory on `sys.path`, beside `lib` and
`investor_reporting`, found from the same `root` it already resolves. Add a test. Change nothing else.

The criteria for THIS amendment are P20-3-AC1 (the packaged layout resolves a ruled period) plus P20-1-AC2 and P20-2-AC1
(unchanged behaviour). P20-1-AC1 stays as written below and is not re-graded here.


### THE CELLS

PRD `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md` ADDENDUM v0.19 (ADMITTED): 49 Financial Performance is
computed from end-of-day holdings into ONE gold, `holdings_performance_daily`, at the builder address
`lib/opal_naming.address("irpt", "49financial", "gold", "holdings_performance_daily", "date=YYYY-MM-DD")` (today:
s3://opal-data-49financial/irpt/49financial/gold/holdings_performance_daily/date=YYYY-MM-DD/data.parquet; columns
account_id (raw 10-digit), business_date, daily_return, account_value, excluded_count, excluded_weight, status, ...).
Ruling 10: the adapter switches to the gold. Ruling 12: the 49F engine read (`f49_engine.calculate` over
`canonical/twr_daily`) retires in the same act -- nothing runs alongside, no fallback.

**`IB-pr-201` -- a gold reader with f49_engine's contract.** New module
`infra/aws/lambda/investor-reporting/performance/holdings_gold.py`:
1. `PROVIDER = "OPAL_HOLDINGS"`; `class HoldingsGoldRefused(ValueError)`;
   `class HoldingsWindowNotRuled(HoldingsGoldRefused)`.
2. `class HoldingsGoldSource(s3, *, bucket, prefix)` -- a read-only port (list the date partitions under `prefix`, read
   one account's rows), receipted per object like `f49_engine.EngineSource`.
3. `calculate(scope, start, end, source)` -- the SAME return contract and report shape as `f49_engine.calculate` (one
   permitted 49F account; `normalize.build_performance_report`; `returns.account_detail`,
   `returns.daily_cumulative_series`, `dates.actual_start/actual_end`, `lineage.provider = OPAL_HOLDINGS`). The value
   is `prod(1 + daily_return) - 1` over the account's status-OK rows with business_date inside the window; a
   non-OK row is skipped and disclosed as a PARTIAL absence. Windows: YTD, QTD and 1Y as `f49_engine.ruled_period_for`
   rules them, and Since inception when start is `1970-01-01`, starting at the account's FIRST landed row (ruling 6).
   Any other window raises `HoldingsWindowNotRuled`; an account with no gold rows raises `HoldingsGoldRefused`.
   Account mapping is `f49_engine.map_account`'s rule (the canonical id is `ids.opaque_account` of the raw key).
4. `entry.py` reasons table: `"HoldingsWindowNotRuled": "UNSUPPORTED_OPERATION"`,
   `"HoldingsGoldRefused": "OBJECT_NOT_COVERED"` (a subclass keeps its own line, which is named first).

**`IB-pr-202` -- the switch, and no engine report reopens after it.** In `retained.py`:
1. `RetainedPerformance(..., holdings_source=None)`: 49 Financial is composed iff `holdings_source` is set, and its fresh
   path calls `holdings_gold.calculate(scope, start, end, self.holdings_source)` INSTEAD of `f49_engine.calculate`. The
   `engine_source` port no longer serves 49F.
2. A retained 49F report whose `lineage.provider` is not `OPAL_HOLDINGS` (computed by the retired engine) is NOT
   reopened: that request takes the fresh path, and the holdings answer publishes as the accepted report for the same
   firm, account set and window. A holdings report reopens as today, with no second gold read.
3. `installed.py`: compose `holdings_source` from the builder address, with the prefix derived from
   `opal_naming.address(...)`, never typed. The COT and INF paths are unchanged.

### ACCEPTANCE (run each from your worktree root)

<criterion id="P20-1-AC1" cell_refs="IB-pr-201"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r20/p20_1_ac1_gold_fixture.py" .</invocation><expect>P20-1-AC1 PASS</expect></criterion>
`P20-1-AC1` -- on in-memory gold: YTD = the chain, provider OPAL_HOLDINGS, actual_start the first in-window day; Since
inception starts at the first landed day; an uncovered account and a 3-year window refuse by name. Base: FAIL
(holdings_gold absent).

<criterion id="P20-1-AC2" cell_refs="IB-pr-201"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r20/p20_1_ac2_gold_live.py" .</invocation><expect>P20-1-AC2 PASS</expect></criterion>
`P20-1-AC2` -- the seam probe against the REAL gold, read-only: the thread account's YTD through
`holdings_gold.calculate` equals the independent chain of its 184 landed days (0.058285199226) within 1e-12. Base:
FAIL.

<criterion id="P20-2-AC1" cell_refs="IB-pr-202"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r20/p20_2_ac1_retained_recompute.py" .</invocation><expect>P20-2-AC1 PASS</expect></criterion>
`P20-2-AC1` -- the check retains a 49F report through the PRE-switch retained.py (git ae8da14d12, engine port), then
asks your RetainedPerformance(holdings_source=...) for the same window. Arm A: the answer is OPAL_HOLDINGS at the gold
chain, and the engine report is not reopened. Arm B: asking again reopens it unchanged, with no second gold read.
Base: FAIL (holdings_gold absent; the pre-switch half runs clean).

<criterion id="P20-3-AC1" cell_refs="IB-pr-201"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r20/p20_3_ac1_packaged_ruled_period.py" .</invocation><expect>P20-3-AC1 PASS</expect></criterion>
`P20-3-AC1` (amendment 2) -- the adapter layout is built from the source map using your worktree's bytes. In an
interpreter whose import path is only that layout, `installed.build_runtime(...)` then `holdings_gold._period_for` for YTD
resolves without ModuleNotFoundError. Base: FAIL (`No module named 'parity_period_returns'`); with the one-line insert:
PASS (measured at the cut).

<expected_criteria>P20-3-AC1,P20-1-AC2,P20-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **No deploy, no AWS write.** AC2 reads S3 only. The served move is the COO's later act under both never-widen
  halves, and it waits until the gold covers every 49F account (today it covers the thread account only).
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise
  row, and do not weaken a check to pass.

<paths>
infra/aws/lambda/investor-reporting/performance/holdings_gold.py
infra/aws/lambda/investor-reporting/performance/retained.py
infra/aws/lambda/investor-reporting/performance/installed.py
infra/aws/lambda/investor-reporting/performance/entry.py
infra/aws/lambda/investor-reporting/performance/tests/test_holdings_gold.py
infra/aws/lambda/investor-reporting/performance/tests/test_retained_performance.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 15 (round 20, workstream ~P), cells `IB-pr-201`, `IB-pr-202`.
<owned_cells>IB-pr-201, IB-pr-202</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: P20-3-AC1, P20-1-AC2, P20-2-AC1 (amendment 2). Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~77/IRPT_BCKEND.TO-IB-pr-201.adapter-reads-the-holdings-gold.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> P20-3-AC1,P20-1-AC2,P20-2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message: the commit hash, each criterion's last line, and any surprise row id
(`IRPT_BCKEND-W77-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule, trigger or cron is created or changed; code and tests on a branch.
comp-iam: RUN -- the served adapter will read opal-data-49financial irpt/49financial/gold/holdings_performance_daily/*; its role's grant is part of the later served move's packet (plan + IAM diff), not this cell.
comp-blast: DECLARED-NOT-APPLICABLE -- nothing served moves in this cell.
comp-routes: DECLARED-NOT-APPLICABLE -- the route table is unchanged.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache surface; the retained store is the cell's subject and is only read/written by the served function later.
comp-adversary: RUN -- the three checks dry-run at the base (CLOUD): P20-1-AC1 FAIL (holdings_gold absent); P20-1-AC2 FAIL (independent chain over the live gold computes 0.058285199226 over 184 days); P20-2-AC1 FAIL at the holdings_gold import only -- the pre-switch half (retain an OPAL_ENGINE report through git ae8da14d12) runs clean.
lane: the <paths> block IS the grant.
</preflight>
