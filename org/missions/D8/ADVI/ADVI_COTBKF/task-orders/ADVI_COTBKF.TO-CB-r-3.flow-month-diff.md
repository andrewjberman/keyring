# TO ADVI_COTBKF.TO-CB-r-3.flow-month-diff -- round 18 CB-r-3: the remaining flow-month DIFFs classed by flow type and size

<to_id>ADVI_COTBKF.TO-CB-r-3</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~39</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>18</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-r-3` (`decompositions/ADVI_COTBKF_DECOMP.round18.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-3: an analyst reads each Cottonwood account's return day by day, after fees, from 2013 to June 2026; strung together over a
month, the days give Commonwealth's reported monthly return, or the difference is shown with its reason; a day that cannot be worked
out is never filled in. The chain, all under `data/assets/scripts/silver/`: `commonwealth_daily_valuation.py` (holdings x same-day
close -> `account_day_value.parquet`, `security_day_price.parquet`), `commonwealth_daily_returns.py` + `commonwealth_flows.py`
(after-fee daily return, external flows out at the END of the day, zero-Amount transfers valued at quantity x close ->
`daily_returns.parquet`), `commonwealth_monthly_grade.py` (months chained, compared with Commonwealth's Month TWR at TOLERANCE_PCT
0.05 -> `monthly_grade.csv`). Parquet goes to `--data-dir`, default `<repo>/.scratch/advi_cotbkf/fwd3/`; run the three in that
order with their defaults (the valuation reads the price stores from S3 read-only on a cold cache, about two minutes). Round 17's
real run: `MONTHLY-GRADE months=82593 match=1973 diff=2264 ungradable=78356 tolerance_pct=0.05`.

**Your item (a new question after row D2-S28).** On the fully priced months, months with an external flow MATCH 242 of 937 (median
|diff| of the DIFFs 6.3 points) while no-flow months MATCH 1,440 of 2,676 (median 0.32). Flow timing and tax withholding are ruled
out. Name where the rest comes from -- **no fix in this item**:
1. build `data/assets/scripts/analysis/commonwealth_flow_diff_classes.py`: for every DIFF flow month, the flow rows in it (type, sign,
   size relative to the account's value that day, whether valued from Amount or quantity x close), and class each month by its
   dominant flow type and a size band (under 1% / 1-10% / over 10% of value);
2. write `flow_diff_classes.csv` and `flow_diff_classes.md` to `--out`: the classes with month counts and median |diff|; for the
   LARGEST class, three example accounts read against their transactions (account, month, the flow rows, the computed vs reported
   return) -- ids and numbers only; LAST line exactly:
   `FLOW-DIFF-CLASSES diff_flow_months=<n> classes=<k> largest=<type>/<band> largest_months=<m> examples=3`.

Tests `data/assets/scripts/analysis/tests/test_commonwealth_flow_diff_classes.py` (stubs): a month with one 20% `li` flow classes
as `li/over 10%`; a month with two types classes by the larger one.

### ACCEPTANCE

<criterion id="CB18r3-AC1" cell_refs="CB-r-3"><invocation>python -m pytest -q data/assets/scripts/analysis/tests/test_commonwealth_flow_diff_classes.py</invocation><expect>passed</expect></criterion>
`CB18r3-AC1` -- the classing rule on stubs.

<criterion id="CB18r3-AC2" cell_refs="CB-r-3"><invocation>python data/assets/scripts/analysis/commonwealth_flow_diff_classes.py --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~39</invocation><expect>examples=3</expect></criterion>
`CB18r3-AC2` -- every DIFF flow month classed; the largest class named with three accounts read against their transactions.

<expected_criteria>CB18r3-AC1,CB18r3-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Large output under `.scratch/`, uncommitted.
- **Read-only.** No apply, no S3 write, no vendor call, no download of any kind, never bun. Read only the buckets named here; never
  `opal-data-bd`, `opal-data-49financial`, `opal-data-inf`, `opal-data-inflection` or `opal-data-demo`.
- **Blank, never filled.** A value, return, month or page count that cannot be worked out is null with its reason, never estimated.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-D2-W39-S<k>`, `"fabric": "dell2"`, `surfaced_at` the actual UTC time you file it), and do not weaken the test.

<paths>
data/assets/scripts/analysis/commonwealth_flow_diff_classes.py
data/assets/scripts/analysis/tests/test_commonwealth_flow_diff_classes.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round18.md</decomp_doc> (round 18), cell `CB-r-3`.
<owned_cells>CB-r-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB18r3-AC1, CB18r3-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~39/ADVI_COTBKF.TO-CB-r-3.flow-month-diff.proof_of_spec.json`, validated
with `python .tools/proof-of-spec-check.py <instance> CB18r3-AC1,CB18r3-AC2` BEFORE the flip. Mechanical: CB18r3-AC1, CB18r3-AC2; a judgment
criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the FLOW-DIFF-CLASSES line, the class table, the three example accounts, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a local derivation run by hand.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity; BLIND: none needed.
comp-adversary: RUN -- the classes counted over every DIFF flow month, not a sample; examples read against the transactions; no fix made; BLIND: Commonwealth's own flow method.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-17 analysis `CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_17_20261008.md` @0ae2f15e5c (msg 1185); decomposition round 18.
