# TO ADVI_COTBKF.TO-CB-z-1.asf-source -- round 26 CB-z-1: ASF sourced before the run, or carried NO-SOURCE

<to_id>ADVI_COTBKF.TO-CB-z-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~48</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>26</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-z-1` (`decompositions/ADVI_COTBKF_DECOMP.round26.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-3: an analyst reads each Cottonwood account's return day by day, after fees, from 2013 to June 2026; strung together over a
month, the days give Commonwealth's reported monthly return, or the difference is shown with its reason; a day that cannot be worked
out is never filled in. The chain, all under `data/assets/scripts/silver/`: `commonwealth_daily_valuation.py`,
`commonwealth_daily_returns.py` + `commonwealth_flows.py`, `commonwealth_monthly_grade.py` (TOLERANCE_PCT 0.05), cash-leg rules in
`commonwealth_sweeps.py`, selected by `commonwealth_sweep_regrade.py` (`--before-cash-leg` / `--after-cash-leg`); LAST line ends
`... regressions=<n> movers_back=<m> year_chain_same=<b> r22_named=<k>/25 dividend_both=<..>`. The CTO ruled `method_r25` the
default (msg 2113): Commonwealth's stated method (CRO research
`org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261008_COMMONWEALTH_TWR_METHOD.md`) plus sourced treatments for the unlisted row
types (`R25_*` tables in `commonwealth_flows.py`; source table in
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~47/unlisted/sweep_regrade.md`). One type, `ASF`, has no source and
stays internal.

**Your item (the CTO's analysis, E2).** "ASF, the one type with no source: a source decided before the run (Commonwealth's documentation
or a CRO read), or carried as NO-SOURCE with its row count."
1. Look for a source in what the repo and the delivery already hold: the delivered files' own field documentation or descriptions,
   the row's pairing in the delivery (what ASF rides on: amount, same-day rows, sign), and the CRO's research. Write the finding, with the
   evidence, BEFORE any run, in a new script `data/assets/scripts/silver/commonwealth_asf_source.py` that reads the transactions and prints
   the ASF census (rows, accounts, date range, signs, same-day pairings) and ends with exactly one LAST line:
   `ASF-SOURCE state=<SOURCED|NO-SOURCE> rows=<n> treatment=<drag|flow|income|internal> source=<short tag>`.
2. If SOURCED: add rule `method_r26` = `method_r25` plus ASF's treatment; re-grade `--before-cash-leg method_r25 --after-cash-leg method_r26`.
   If NO-SOURCE: `method_r26` = `method_r25` (ASF stays internal), and the re-grade is trivially equal; say so. Do not choose a treatment by
   its effect on the grade.

Tests `data/assets/scripts/silver/tests/test_commonwealth_asf.py` (stubs): the census script's LAST line format; ASF treated per the stated
state (or internal when NO-SOURCE); `method_r25` unchanged.

### ACCEPTANCE

<criterion id="CB26z1-AC1" cell_refs="CB-z-1"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_asf.py</invocation><expect>passed</expect></criterion>
`CB26z1-AC1` -- the ASF line format, its treatment per the stated state, `method_r25` unchanged.

<criterion id="CB26z1-AC2" cell_refs="CB-z-1"><invocation>python data/assets/scripts/silver/commonwealth_sweep_regrade.py --before-list v1 --after-list v1 --before-cash-leg method_r25 --after-cash-leg method_r26 --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~48/asf</invocation><expect>regressions=0</expect></criterion>
`CB26z1-AC2` -- ASF's treatment regresses no month that matched under `method_r25`.

<criterion id="CB26z1-AC3" cell_refs="CB-z-1" judgment="true"/>
`CB26z1-AC3` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the ASF state and source were decided before the run from evidence printed by the census script, not from the grade.

<expected_criteria>CB26z1-AC1,CB26z1-AC2,CB26z1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Large output under `.scratch/`, uncommitted.
- **Read-only.** No apply, no S3 write, no vendor call, no download of any kind, never bun. Read only the buckets the chain already
  reads; never `opal-data-bd`, `opal-data-49financial`, `opal-data-inf`, `opal-data-inflection` or `opal-data-demo`.
- **No rule-fitting; blank, never filled.**
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a NEW surprise row (id
  `ADVI_COTBKF-D2-W48-S<k>`, `"fabric": "dell2"`, `surfaced_at` the actual UTC time; never an edit of an existing row), and do not
  weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_asf_source.py
data/assets/scripts/silver/commonwealth_sweeps.py
data/assets/scripts/silver/commonwealth_sweep_regrade.py
data/assets/scripts/silver/commonwealth_flows.py
data/assets/scripts/silver/commonwealth_daily_returns.py
data/assets/scripts/silver/tests/test_commonwealth_asf.py
data/assets/scripts/silver/tests/test_commonwealth_unlisted_types.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round26.md</decomp_doc> (round 26), cell `CB-z-1`.
<owned_cells>CB-z-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB26z1-AC1, CB26z1-AC2, CB26z1-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~48/ADVI_COTBKF.TO-CB-z-1.asf-source.proof_of_spec.json`, validated with
`python .tools/proof-of-spec-check.py <instance> CB26z1-AC1,CB26z1-AC2,CB26z1-AC3` BEFORE the flip. Mechanical: CB26z1-AC1, CB26z1-AC2;
a judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the ASF-SOURCE line, the evidence, the SWEEP-REGRADE line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a local derivation run by hand.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity; BLIND: none needed.
comp-adversary: RUN -- the state is decided from printed evidence before the run; NO-SOURCE is an acceptable outcome; BLIND: documentation outside the repo (it makes the state NO-SOURCE, never a guess).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` analysis ADDENDUM 1 (msg 2113), E2.
