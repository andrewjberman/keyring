# TO ADVI_COTBKF.TO-CB-aa-1.trace-512 -- round 27 CB-aa-1: trace the 512 untraced DIFF months to a valuation-side cause

<to_id>ADVI_COTBKF.TO-CB-aa-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~50</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>27</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-aa-1` (`decompositions/ADVI_COTBKF_DECOMP.round27.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-3: an analyst reads each Cottonwood account's return day by day, after fees, from 2013 to June 2026; strung together over a
month, the days give Commonwealth's reported monthly return, or the difference is shown with its reason; a day that cannot be worked
out is never filled in. The chain, under `data/assets/scripts/silver/`: `commonwealth_daily_valuation.py` (holdings x as-traded close;
cash), `commonwealth_daily_returns.py` + `commonwealth_flows.py`, `commonwealth_monthly_grade.py` (TOLERANCE_PCT 0.05); the default cash
leg is `method_r26` (Commonwealth's stated method + sourced unlisted types). `commonwealth_sweep_regrade.py` runs it and persists
`month_grades_before/after.parquet` beside its report; day parquet goes to `--data-dir`.

Round 26's census, `commonwealth_nonmatch_census.py` (rules committed before its run), over the default run
(`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~48/census/nonmatch_census.md` + `.parquet`): of 886 DIFF months,
SWEEP_CASH_LEG 190, INCOME 154, CLIENT_FLOW 30, and **512 unexplained** (478: no posting category's exposure reaches the month's
difference; 34: no driver row at all). The CTO's lead: valuation-side causes -- a price, a holding quantity, or a level carried in.

**Your item (the CTO's ADDENDUM 2, E1).** Trace each of the 512 months to ONE named cause, by rules you write and commit BEFORE the run,
in a new script `data/assets/scripts/silver/commonwealth_diff_trace.py --census <dir> --grades <dir> --data-dir <dir> --out <dir>`.
Candidate classes (add others as the rows show them): `price:<cusip>` (a day whose value step is carried by one security's close move
that the reported return does not share -- e.g. a stale or split-unadjusted close), `holding:<cusip>` (the rebuilt quantity disagrees
with what the account's rows support on the month's days), `carried_level` (a level built before the month), `partial_month`
(the account opened or closed mid-month), `reported_outlier` (Commonwealth's own month disagrees with its own year chain). A month no rule
fits is `untraced:<what was checked>`, never forced. Write `diff_trace.md` + `.parquet`. LAST line exactly:
`DIFF-TRACE months=<n> traced=<t> untraced=<u> classes=<k>`. Run it on a fresh default run (`--before-cash-leg method_r25`, default after
arm) in a data-dir under your `.scratch`, out `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~50/`.

Tests `data/assets/scripts/silver/tests/test_commonwealth_diff_trace.py` (stubs): each class on a stub of its cause; an unfit month is
`untraced:`; the counts sum to the input.

### ACCEPTANCE

<criterion id="CB27aa1-AC1" cell_refs="CB-aa-1"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_diff_trace.py</invocation><expect>passed</expect></criterion>
`CB27aa1-AC1` -- each class on a stub; the untraced fallback; the counts sum.

<criterion id="CB27aa1-AC2" cell_refs="CB-aa-1"><invocation>python data/assets/scripts/silver/commonwealth_diff_trace.py --census org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~48/census --grades org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~50 --data-dir .scratch/advi_cotbkf/r27 --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~50</invocation><expect>months=512</expect></criterion>
`CB27aa1-AC2` -- all 512 read and classed (traced or untraced with what was checked); use `.scratch/advi_cotbkf/r27` as the run's data-dir.

<criterion id="CB27aa1-AC3" cell_refs="CB-aa-1" judgment="true"/>
`CB27aa1-AC3` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: rules committed before the run; each traced class shown on a traced month's day values; nothing forced.

<expected_criteria>CB27aa1-AC1,CB27aa1-AC2,CB27aa1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Large output under `.scratch/`, uncommitted.
- **Reads.** S3 reads of the buckets the chain already reads; never `opal-data-bd`, `opal-data-49financial`, `opal-data-inf`,
  `opal-data-inflection`, `opal-data-demo`. No S3 write, no apply. Egress is open except Bloomberg (law edit 4d77a9c3ea), but this cell needs none.
- **No rule-fitting; blank, never filled.** No change to any cash-leg or flow rule.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a NEW surprise row (id
  `ADVI_COTBKF-D2-W50-S<k>`, `"fabric": "dell2"`, `surfaced_at` the actual UTC time; never an edit of an existing row), and do not
  weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_diff_trace.py
data/assets/scripts/silver/tests/test_commonwealth_diff_trace.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round27.md</decomp_doc> (round 27), cell `CB-aa-1`.
<owned_cells>CB-aa-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB27aa1-AC1, CB27aa1-AC2, CB27aa1-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~50/ADVI_COTBKF.TO-CB-aa-1.trace-512.proof_of_spec.json`, validated with
`python .tools/proof-of-spec-check.py <instance> CB27aa1-AC1,CB27aa1-AC2,CB27aa1-AC3` BEFORE the flip. Mechanical: CB27aa1-AC1,
CB27aa1-AC2; a judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the DIFF-TRACE line, the classes with counts, one traced month per class, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a local derivation run by hand.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity; BLIND: none needed.
comp-adversary: RUN -- classes by rules committed before the run; untraced allowed; BLIND: a cause in Commonwealth's own reported figure (named reported_outlier, never fixed here).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` ADDENDUM 2 (msgs 2213, 2257), E1; row D2-W48-S2.
