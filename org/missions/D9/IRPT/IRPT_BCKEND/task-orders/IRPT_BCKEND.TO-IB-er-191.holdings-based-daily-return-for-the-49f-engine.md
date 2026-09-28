# TO IRPT_BCKEND.TO-IB-er-191 -- The 49F engine's daily return is holdings-based (Andrew-direct call 3; rows S181, W61-S2)

<to_id>IRPT_BCKEND.TO-IB-er-191</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.4.0_DS_ClientPlatform~E</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-09-28</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>seat</worker_class>
<placeholders>NONE</placeholders>
<round>19</round>
<workstream>~E</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** Andrew-direct 2026-09-28 ~22:2xZ calls 2 and 3 (record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_222xZ_OPEN_CALLS_1_2_APPROVED_3_HOLDINGS_BASED_PERFORMANCE.md`),
routed by 1.0.0_SA_CTO 102456 and ruled into workstream ~E by 102461 | **Decomp cell:** `IB-er-191` (decomposition
section 13.2) | **outcome_ref:** FWD-3 (Performance, 49 Financial) | **depends_on:** none

---

## WORKER FACE

### THE CELL

`IB-er-191` -- 49 Financial Performance is read from the 49F engine table `canonical/twr_daily`
(s3://opal-data-49financial/gold/advi/canonical/twr_daily/date=YYYY-MM-DD/data.parquet; the producer is
`C:/Users/AndrewBerman/Desktop/ajb_workspace/data/assets/scripts/gold/runners_49f/c02_twr_engine.py`). Today its daily
return is FLOW-based: `c02_twr_engine.py:264` `r_net = (emv - cf_net) / bmv - 1.0`. Measured on the served table:
- 26 OK rows year to date carry r_net <= -1 across 22 accounts: a value that vanishes with no recorded flow (NEW-01:
  bmv 13,360.59, emv 0.0, cf_net 0.0 on 2026-04-16 answers -100% forever after), and cash flows orders of magnitude
  above the value change (down to r_net -6,942) (row S177, row S181).
- Partitions date=2024-07-08 and date=2025-01-09 lack bmv/emv although schema_version is 1.2 (row W61-S2), so every
  full-history read is refused.

**Andrew's rule (verbatim, the record above):** "cash movements should not matter at all, performance should be
measured as the daily, pro-rated by weight, performance of any securities in a given basket on a given day. It is
important that this is handled explicitly at the asset level, looking at the weight of the assets relative to the
account in question on the subject day, tracking the delta from the previous day. We cannot get involved with
inflow/outflow logic, or be calculating performance in any other basis other than end of day asset holdings values,
otherwise it will get too complicated."

**Build** (the method is fixed; the code is yours):
1. The account's day-t `r_net` is the sum, over the securities it held at the end of day t-1, of
   `w_i * r_i`, where `w_i = market_value_settled_unsettled(i, t-1) / fair_value(account, t-1)` (from
   `canonical/canonical_positions` and `canonical/canonical_valuation`, a cusip's lots summed) and
   `r_i = closing_price(i, t) / closing_price(i, t-1) - 1` (same cusip). Cash earns zero. There is NO inflow/outflow
   term, and `cf_net` no longer enters the return.
2. Name every case the rule cannot price (a t-1 security with no day-t price, a non-positive price, zero account
   value) with a NON-OK status that the table's readers already skip. Never emit status OK for a day the rule
   cannot price.
3. Rebuild the table's history so that every partition carries its value columns (the two partitions of row W61-S2
   included), under the same registry address.
4. Tests beside the producer for: the rule on a trading day with a flow (the flow does not move the return), a full
   exit (not -100%), and each named non-OK case.

**Order of acts (NEVER-class, binding):** the served table is read by irpt-performance-adapter, so rewriting it moves
SERVED output.
- (a) Build and test.
- (b) Run the rebuild ad hoc into a QA prefix you name (ad-hoc runs are for QA), and run the three checks below with
  that prefix as their argument.
- (c) Put a never-widen packet (the blast radius: rows and accounts whose r_net changes, both branches) to
  1.0.0_SA_CTO and 2.0.0_SA_COO~P, and wait for both halves.
- (d) Only then write the served prefix, through your deploy ledger (`.tools/deploy_ledger.py`, opened before the
  first write) and the scheduled path (the scheduler stays the production trigger).

### ACCEPTANCE (run each from the workspace root; each takes the S3 root as an optional argument, default the served one)

<criterion id="E19-AC1" cell_refs="IB-er-191"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r19e/e19_ac1_no_impossible_day.py"</invocation><expect>E19-AC1 PASS</expect></criterion>
`E19-AC1` -- no OK day with r_net <= -1 year to date, and the NEW-01 account's 2026-04-16 is not OK at -1.0. Base:
FAIL (26 rows, 22 accounts, NEW-01 among them).

<criterion id="E19-AC2" cell_refs="IB-er-191"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r19e/e19_ac2_value_columns.py"</invocation><expect>E19-AC2 PASS</expect></criterion>
`E19-AC2` -- date=2024-07-08 and date=2025-01-09 carry bmv, emv and r_net; the neighbour date=2025-01-10 still does
(control). Base: FAIL (both lack bmv and emv).

<criterion id="E19-AC3" cell_refs="IB-er-191"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r19e/e19_ac3_holdings_method.py"</invocation><expect>E19-AC3 PASS</expect></criterion>
`E19-AC3` -- the method, recomputed independently from positions and valuation on days that carry a cash flow (where
the flow rule and the holdings rule differ): at least 20 pairs, every one within 1e-8 of r_net. Base: FAIL (109
pairs, 101 differ, worst 0.485).

<expected_criteria>E19-AC1,E19-AC2,E19-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **Deploy discipline.** The ledger opens before the first write; the served write waits on both halves; the
  scheduler stays the production trigger. The adapter (irpt-performance-adapter) is ~P's and is not touched here.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise
  row, and do not weaken a check to pass. If the rule cannot be applied as stated (for example, positions lack a price
  for a held security on most days), say so in a row before building around it.

<paths>
data/assets/scripts/gold/runners_49f/c02_twr_engine.py
data/assets/scripts/gold/runners_49f/tests/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 13.2 (round 19, workstream ~E), cell `IB-er-191`.
<owned_cells>IB-er-191</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: E19-AC1, E19-AC2, E19-AC3. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~E/IRPT_BCKEND.TO-IB-er-191.holdings-based-daily-return-for-the-49f-engine.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> E19-AC1,E19-AC2,E19-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** one message to `2.0.0_SA_COO~P` naming the QA prefix and its three check lines, then (after the halves)
the ledger slug and the served check lines; surprise rows in the investigation file (id `IRPT_BCKEND-S<next>`).

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- the producer runs on the 49F gold runner schedule; this order keeps the scheduler as the production trigger and adds only an ad-hoc QA run.
comp-iam: DECLARED-NOT-APPLICABLE -- the runner's existing role writes the same registry prefix; no IAM change.
comp-blast: RUN -- the served table's readers: irpt-performance-adapter (f49_engine, 49F Performance); the blast radius is the packet at step (c).
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache surface; retained Performance reports computed before the rebuild stay retained (the adapter's reopen guard IB-pr-194 covers the impossible ones).
comp-adversary: RUN -- the three checks were dry-run at the base (the served table): AC1 FAIL (26 rows / 22 accounts), AC2 FAIL (bmv/emv absent on both), AC3 FAIL (101 of 109 flow-day pairs differ).
lane: 0.4.0_DS_ClientPlatform~E is enumerated in .owned-paths.yaml POD4 for data/*/scripts/gold (MSTR 102458); the <paths> block is the grant.
</preflight>

Seating: `0.0.0_AB_MSTR` seated `0.4.0_DS_ClientPlatform~E` for this order (102458).
