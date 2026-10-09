# TO ADVI_COTBKF.TO-CB-ab-3.trace-at-committed-cap -- round 28 CB-ab-3: the trace re-run at the committed reach cap 0.5

<to_id>ADVI_COTBKF.TO-CB-ab-3</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~54</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>28</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-ab-3` (`decompositions/ADVI_COTBKF_DECOMP.round28.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`data/assets/scripts/silver/commonwealth_diff_trace.py` traces each DIFF month of the FWD-3 daily-return chain to one valuation-side
cause (`price:` split / distribution, `flow_value:`, ...) or `untraced:`. A cause REACHES a month when its repair carries at least 90% of
the month's difference and leaves a remainder under REACH_CAP_PCT (`commonwealth_diff_trace.py:87`, now 1.0). Round 27's run:
`DIFF-TRACE months=512 traced=73 untraced=439 classes=3`
(`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~50/diff_trace.md`). The CTO ruled (ADDENDUM 3, msg 2476): the cap was
moved from 0.5 to 1.0 AFTER exploratory runs on the same months, which raised the traced count from 70 to 73 and created the only
`flow_value` trace -- that is fitting. "The cap returns to 0.5, the value committed before the run. The 3 traces gained at 1.0 are dropped
unless they hold at 0.5. A cap change after this is legal only as a rule stated BEFORE a run on months it has not seen (held out)."

**Your item (E2, with E3 as a bound).**
1. Set REACH_CAP_PCT back to 0.5. Add the cap to the LAST line, keeping the rest:
   `DIFF-TRACE months=<n> traced=<t> untraced=<u> classes=<k> cap=<c>`.
2. Re-run on the round-26 census and a fresh default run (`commonwealth_sweep_regrade.py --before-list v1 --after-list v1
   --before-cash-leg method_r25 --data-dir .scratch/advi_cotbkf/r27 --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~54`
   on the chain as it stands at your cut). In `diff_trace.md`: the traced count at 0.5, the `flow_value` class shown (if it holds at 0.5) or
   dropped (if it does not), and the 3 months that were traced only at 1.0 named with their result at 0.5.
3. **Bound (E3):** you propose NO cap change in this cell. Any future change is a rule committed before a run on held-out months, which is
   a separate cell.

### ACCEPTANCE

<criterion id="CB28ab3-AC1" cell_refs="CB-ab-3"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_diff_trace.py</invocation><expect>passed</expect></criterion>
`CB28ab3-AC1` -- the trace tests pass at the committed cap.

<criterion id="CB28ab3-AC2" cell_refs="CB-ab-3"><invocation>python data/assets/scripts/silver/commonwealth_diff_trace.py --census org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~48/census --grades org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~54 --data-dir .scratch/advi_cotbkf/r27 --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~54</invocation><expect>cap=0.5</expect></criterion>
`CB28ab3-AC2` -- the trace re-run at the committed cap, the cap printed.

<criterion id="CB28ab3-AC3" cell_refs="CB-ab-3" judgment="true"/>
`CB28ab3-AC3` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the cap is the value committed before round 27's run; the three 1.0-only traces are named with their 0.5 result; nothing else in the rules changed.

<expected_criteria>CB28ab3-AC1,CB28ab3-AC2,CB28ab3-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Large output under `.scratch/`, uncommitted.
- **One change only:** REACH_CAP_PCT to 0.5 and the `cap=` field. No other rule or constant changes.
- **Reads.** S3 reads of the buckets the chain reads; never `opal-data-bd`, `opal-data-49financial`, `opal-data-inf`, `opal-data-inflection`,
  `opal-data-demo`. No S3 write.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a NEW surprise row (id
  `ADVI_COTBKF-D2-W54-S<k>`, `"fabric": "dell2"`, `surfaced_at` the actual UTC time), and do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_diff_trace.py
data/assets/scripts/silver/tests/test_commonwealth_diff_trace.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round28.md</decomp_doc> (round 28), cell `CB-ab-3`.
<owned_cells>CB-ab-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB28ab3-AC1, CB28ab3-AC2, CB28ab3-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~54/ADVI_COTBKF.TO-CB-ab-3.trace-at-committed-cap.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB28ab3-AC1,CB28ab3-AC2,CB28ab3-AC3` BEFORE the flip. Mechanical:
CB28ab3-AC1, CB28ab3-AC2; a judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the DIFF-TRACE line, the traced count at 0.5, the three 1.0-only months, `flow_value` shown or dropped, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a local derivation run by hand.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity; BLIND: none needed.
comp-adversary: RUN -- the cap restored to the pre-run committed value; one change only; BLIND: none beyond round 27's.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` ADDENDUM 3 (msg 2476), E2 and E3.
