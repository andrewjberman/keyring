# TO ADVI_COTBKF.TO-CB-q-2.flow-timing -- round 17 CB-q-2: flow timing tested: start of day against end of day

<to_id>ADVI_COTBKF.TO-CB-q-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~35</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>17</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-q-2` (`decompositions/ADVI_COTBKF_DECOMP.round17.md`) |
**outcome_ref:** FWD-3 | **depends_on:** CB-q-1 (same files, same worker, after it)

---

## WORKER FACE

### THE CELL

FWD-3: an analyst reads each Cottonwood account's return day by day, after fees, from 2013 to June 2026; strung together over a
month, the days give Commonwealth's reported monthly return, or the difference is shown with its reason; a day that cannot be worked
out is never filled in. Round 16 built the chain (all under `data/assets/scripts/silver/`): `commonwealth_daily_valuation.py`
(holdings x same-day close -> `account_day_value.parquet`), `commonwealth_daily_returns.py` + `commonwealth_flows.py` (after-fee
daily return, external flows out -> `daily_returns.parquet`), `commonwealth_monthly_grade.py` (months chained, compared with
Commonwealth's Month TWR at TOLERANCE_PCT 0.05). Parquet goes to `--data-dir`, default `<repo>/.scratch/advi_cotbkf/fwd3/`. Its real
run graded 4,231 fully priced months: 1,947 MATCH, 2,284 DIFF.

**Your item (row D2-S28).** On the graded months, those with an external flow mostly DIFF (866 of 1,138, median |diff| 7.4 points)
while those with none MATCH 1,675 of 3,093. The daily return today takes flows at the END of the day:
`ret_t = (value_t - flow_t) / value_(t-1) - 1`. Test the other convention and keep the better one:
1. `commonwealth_daily_returns.py` gains `--flow-timing end|start`; start of day is `ret_t = value_t / (value_(t-1) + flow_t) - 1`
   (a zero or negative base stays blank, `ZERO_BASE`); the default stays `end` until the result below picks;
2. build `data/assets/scripts/silver/commonwealth_flow_timing.py`: run the returns under each convention, grade each with
   `commonwealth_monthly_grade.py`, and over the fully priced months print side by side, for flow months and no-flow months
   separately, the MATCH count and the median |diff| of the DIFFs; its LAST line exactly:
   `FLOW-TIMING flow_months=<f> end_match=<a> start_match=<b> end_diff_median=<x> start_diff_median=<y> control_months=<c> control_same=<True|False> chosen=<end|start>`
   -- `control_same` is True when every no-flow month grades identically under both; `chosen` is the convention with more MATCH on
   flow months (ties: the lower median), and the script writes it as the module default `FLOW_TIMING` in the returns module only
   when you commit it by hand after reading the result -- state the reason in `flow_timing.md`;
3. a tax-withholding note: also print the flow-month MATCH count with `ftax`/`stax` treated as INTERNAL under the chosen timing
   (one extra field `chosen_tax_internal_match=<m>` is allowed before the last line, on its own line), and keep the FLOW table's
   decision unless that count is higher -- then change it in `commonwealth_flows.py` with the reason.

Tests `data/assets/scripts/silver/tests/test_commonwealth_flow_timing.py` (stubs): a deposit day returns the hand-computed value under
each convention; a no-flow path returns the same under both (the control).

### ACCEPTANCE

<criterion id="CB17q2-AC1" cell_refs="CB-q-2"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_flow_timing.py</invocation><expect>passed</expect></criterion>
`CB17q2-AC1` -- both conventions and the no-flow control on stubs.

<criterion id="CB17q2-AC2" cell_refs="CB-q-2"><invocation>python data/assets/scripts/silver/commonwealth_flow_timing.py --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~35</invocation><expect>control_same=True</expect></criterion>
`CB17q2-AC2` -- the side-by-side on the real fully priced months, with the convention chosen by the result.

<expected_criteria>CB17q2-AC1,CB17q2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Large output under `.scratch/`, uncommitted.
- **Read-only.** No apply, no S3 write, no vendor call, no download of any kind, never bun. Read only the buckets named here; never
  `opal-data-bd`, `opal-data-49financial`, `opal-data-inf`, `opal-data-inflection` or `opal-data-demo`.
- **Blank, never filled.** A value, return, month or page count that cannot be worked out is null with its reason, never estimated.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-D2-W35-S<k>`, `"fabric": "dell2"`, `surfaced_at` the actual UTC time you file it), and do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_daily_returns.py
data/assets/scripts/silver/commonwealth_flows.py
data/assets/scripts/silver/commonwealth_flow_timing.py
data/assets/scripts/silver/tests/test_commonwealth_flow_timing.py
data/assets/scripts/silver/tests/test_commonwealth_daily_returns.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round17.md</decomp_doc> (round 17), cell `CB-q-2`.
<owned_cells>CB-q-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB17q2-AC1, CB17q2-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~35/ADVI_COTBKF.TO-CB-q-2.flow-timing.proof_of_spec.json`, validated
with `python .tools/proof-of-spec-check.py <instance> CB17q2-AC1,CB17q2-AC2` BEFORE the flip. Mechanical: CB17q2-AC1, CB17q2-AC2; a judgment
criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the FLOW-TIMING line, the side-by-side table, the convention chosen and why, the tax-withholding count, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a local derivation run by hand.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity; BLIND: none needed.
comp-adversary: RUN -- the convention chosen by measured MATCH, not by preference; no-flow months must not move; BLIND: Commonwealth's own intraday flow method.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-16 analysis `CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_16_20261007.md` @8b6829c89f (msg 1100); decomposition round 17.
