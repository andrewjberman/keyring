# TO ADVI_COTBKF.TO-CB-s-1.sweep-is-cash -- round 19 CB-s-1: the FDIC sweep is cash: a declared sweep list, sweep buys and sells INTERNAL, re-graded

<to_id>ADVI_COTBKF.TO-CB-s-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~40</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>19</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-s-1` (`decompositions/ADVI_COTBKF_DECOMP.round19.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-3: an analyst reads each Cottonwood account's return day by day, after fees, from 2013 to June 2026; strung together over a
month, the days give Commonwealth's reported monthly return, or the difference is shown with its reason; a day that cannot be worked
out is never filled in. The chain, all under `data/assets/scripts/silver/`: `commonwealth_daily_valuation.py` (holdings x same-day
close -> `account_day_value.parquet`, `security_day_price.parquet`; cash today = `commonwealth_crosswalk.is_cash`, a PREFIX rule:
CUSIP starting `FDIC` or equal to `CFNCASH`, priced at 1.0), `commonwealth_daily_returns.py` + `commonwealth_flows.py` (after-fee daily
return, external flows out at the end of the day, a non-positive base blank), `commonwealth_monthly_grade.py` (months chained,
compared with Commonwealth's Month TWR at TOLERANCE_PCT 0.05). Parquet goes to `--data-dir`, default
`<repo>/.scratch/advi_cotbkf/fwd3/`; run the three in that order with their defaults (the valuation reads the price stores from S3
read-only on a cold cache, about two minutes). Round 18's real run: `MONTHLY-GRADE months=82593 match=1685 diff=1931 ungradable=78977`.
`data/assets/scripts/analysis/commonwealth_flow_diff_classes.py` classes the DIFF flow months (largest: `lo` over 10%, 249).

**Your item (the CTO's ruling on row D2-W39-S1).** A withdrawal is delivered as an `lo` of CFNCASH plus an `sl` of the FDIC sweep
for the same amount on the same day, so the account value falls by TWICE the withdrawal while the return takes the flow out once
(74 of 106 single-`lo` months; e.g. acct#05dd4a9d on 2023-07-14). The ruling, verbatim in substance: "sweep vehicles are cash. Their
buys and sells are INTERNAL: neither a flow nor a trade. Their balance counts as cash in the daily value. Which securities are
sweeps is a declared, versioned list: each listed CUSIP is named with its source (vendor description, or the CUSIP's issuer), never
inferred per row. A security not on the list is never treated as cash."
1. a new module `data/assets/scripts/silver/commonwealth_sweeps.py`: `SWEEP_LIST_VERSION` and `SWEEPS` -- each CUSIP with its source
   (the vendor's `Security_Description` as delivered, or the issuer); and `CANDIDATES_REJECTED` -- every other CUSIP a census flagged
   as possibly cash (description or prefix), each with its reason. Build the census from the silver transactions (distinct CUSIPs
   whose description or prefix suggests cash or a sweep) and print it;
2. the valuation and the returns use the list, not a prefix: a listed sweep is priced at 1.0 and counted as cash; its buys and sells
   are INTERNAL in `commonwealth_flows.py` (with the list version as the reason). Make the sweep's sale proceeds and purchase cost
   land in cash, so a sweep-funded withdrawal moves the value ONCE. `CFNCASH` stays cash. Leave `commonwealth_crosswalk.is_cash`
   untouched (it serves the applied crosswalk);
3. a runner `data/assets/scripts/silver/commonwealth_sweep_regrade.py` that re-runs the chain before and after and writes
   `sweep_regrade.md` to `--out`: the list and the rejected candidates; the 106 single-`lo` months of the largest class (as
   `commonwealth_flow_diff_classes.py` finds them) MATCH/DIFF before and after, with the 74 double-drop months named and each result;
   the whole grade before and after; and a CONTROL -- every graded month with no sweep row grades identically before and after. LAST
   line exactly:
   `SWEEP-REGRADE sweeps=<s> rejected=<r> double_drop_months=<d> fixed=<f> months_before=<m>/<d>/<u> months_after=<m>/<d>/<u> control_same=<True|False>`.

Tests `data/assets/scripts/silver/tests/test_commonwealth_sweeps.py` (stubs): an `lo` of 100 cash paid by a same-day `sl` of 100 of a
listed sweep moves the value by 100 once and the day's return is 0; a security not on the list with an `FDIC`-like description is
NOT cash (the list governs); a day with no sweep row returns the same as before (the control).

### ACCEPTANCE

<criterion id="CB19s1-AC1" cell_refs="CB-s-1"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_sweeps.py</invocation><expect>passed</expect></criterion>
`CB19s1-AC1` -- the sweep-funded withdrawal moves the value once, the list governs over the description, and the no-sweep control is unchanged.

<criterion id="CB19s1-AC2" cell_refs="CB-s-1"><invocation>python data/assets/scripts/silver/commonwealth_sweep_regrade.py --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~40</invocation><expect>control_same=True</expect></criterion>
`CB19s1-AC2` -- the declared list with sources and rejected candidates; the 74 double-drop months re-graded by name; no-sweep months unmoved.

<criterion id="CB19s1-AC3" cell_refs="CB-s-1" judgment="true"/>
`CB19s1-AC3` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the sweep list reads as a declared list: every CUSIP on it is a bank sweep by its stated source, and no rejected candidate should have been on it.

<expected_criteria>CB19s1-AC1,CB19s1-AC2,CB19s1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Large output under `.scratch/`, uncommitted.
- **Read-only.** No apply, no S3 write, no vendor call, no download of any kind, never bun. Read only the buckets named here; never
  `opal-data-bd`, `opal-data-49financial`, `opal-data-inf`, `opal-data-inflection` or `opal-data-demo`.
- **Blank, never filled.** A value, return, month or page count that cannot be worked out is null with its reason, never estimated.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-D2-W40-S<k>`, `"fabric": "dell2"`, `surfaced_at` the actual UTC time you file it), and do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_sweeps.py
data/assets/scripts/silver/commonwealth_flows.py
data/assets/scripts/silver/commonwealth_daily_valuation.py
data/assets/scripts/silver/commonwealth_daily_returns.py
data/assets/scripts/silver/commonwealth_sweep_regrade.py
data/assets/scripts/silver/tests/test_commonwealth_sweeps.py
data/assets/scripts/silver/tests/test_commonwealth_daily_valuation.py
data/assets/scripts/silver/tests/test_commonwealth_daily_returns.py
data/assets/scripts/silver/tests/test_commonwealth_zero_amount_flows.py
data/assets/scripts/silver/tests/test_commonwealth_non_positive_base.py
data/assets/scripts/silver/tests/test_commonwealth_flow_timing.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round19.md</decomp_doc> (round 19), cell `CB-s-1`.
<owned_cells>CB-s-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB19s1-AC1, CB19s1-AC2, CB19s1-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~40/ADVI_COTBKF.TO-CB-s-1.sweep-is-cash.proof_of_spec.json`, validated
with `python .tools/proof-of-spec-check.py <instance> CB19s1-AC1,CB19s1-AC2,CB19s1-AC3` BEFORE the flip. Mechanical: CB19s1-AC1, CB19s1-AC2; a judgment
criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the SWEEP-REGRADE line, the sweep list with sources, the rejected candidates, the 74 months' results, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a local derivation run by hand.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity; BLIND: none needed.
comp-adversary: RUN -- the list declared with a source per CUSIP, never inferred per row; the no-sweep control unchanged; BLIND: sweeps whose description does not say so (they stay securities until listed).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-18 analysis `CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_18_20261008.md` @04b347e9ea (msg 1237); decomposition round 19.
