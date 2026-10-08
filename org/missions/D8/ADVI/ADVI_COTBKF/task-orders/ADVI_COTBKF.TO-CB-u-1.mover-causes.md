# TO ADVI_COTBKF.TO-CB-u-1.mover-causes -- round 21 CB-u-1: name the cause of the 147 "neither" MATCH -> DIFF movers

<to_id>ADVI_COTBKF.TO-CB-u-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~42</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>21</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-u-1` (`decompositions/ADVI_COTBKF_DECOMP.round21.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-3: an analyst reads each Cottonwood account's return day by day, after fees, from 2013 to June 2026; strung together over a
month, the days give Commonwealth's reported monthly return, or the difference is shown with its reason; a day that cannot be worked
out is never filled in. The chain, all under `data/assets/scripts/silver/`: `commonwealth_daily_valuation.py` (holdings x same-day
close), `commonwealth_daily_returns.py` + `commonwealth_flows.py` (after-fee daily return, external flows out at the end of the day),
`commonwealth_monthly_grade.py` (months chained vs Commonwealth's Month TWR, TOLERANCE_PCT 0.05). Round 19 made the two FDIC bank
sweeps (FDIC66606, FDIC66853; `commonwealth_sweeps.py`) cash, their buys and sells INTERNAL. `commonwealth_sweep_regrade.py`
re-runs the chain for two list arms (`--before-list none|v1|v2`, `--after-list ...`), writes day parquet under `--data-dir`
(`<dir>/before`, `<dir>/after`; default `<repo>/.scratch/advi_cotbkf/fwd3/`, uncommitted) and persists month grades beside the report.

Round 19's re-grade (arm `none` -> arm `v1`) moved 163 months MATCH -> DIFF. Round 20 classed them by account holdings
(`commonwealth_mover_classes.py`): `MOVER-CLASSES movers=163 core=16 other_mmf=0 neither=147 sum_ok=True`. The persisted files, READ
only: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~41/month_grades_before.parquet`,
`month_grades_after.parquet`, `mover_classes.parquet`, `mover_classes.md`.

**Your item (the CTO's round-20 analysis, E1).** "A month that went MATCH -> DIFF when the sweep turned INTERNAL may also have matched
before only because two errors offset. If so, DIFF is the truer state, and the fix lies elsewhere in the chain."
A new script `data/assets/scripts/silver/commonwealth_mover_causes.py --grades <dir> --data-dir <dir> --out <dir>`:
1. reads the 147 `neither` movers from `mover_classes.parquet` and the day values of both arms (re-run
   `commonwealth_sweep_regrade.py --before-list none --after-list v1 --data-dir <dir> --out <scratch>` first if the day parquet is
   absent);
2. assigns EACH month exactly one cause class, by a rule written in the report BEFORE the counts. At least: `sweep_balance` -- the
   sweep balance now entering the daily value moves the month (the after-arm value differs from the before-arm value on days with no
   sweep trade); `offsetting` -- the before-arm month matched only because two errors cancelled, shown by the before-state's two
   components (e.g. the value change and the flow taken out) each off by about the same amount in opposite directions; `other:<name>`
   -- any further cause, named. A month no rule fits is `other:unexplained`, never forced into a class;
3. traces ONE month per class end to end (account, month, each day's before and after value, flow and return, the chained month vs
   the reported return), with the day values printed;
4. reports E1's 16 `core` months SEPARATELY, under the same rule, never counted in the 147.
Write `mover_causes.md` and `mover_causes.parquet` to `--out`. LAST line exactly:
`MOVER-CAUSES movers=<n> sweep_balance=<a> offsetting=<b> other=<c> sum_ok=<True|False> core_separate=<k>` (`other` = all `other:*`).

Tests `data/assets/scripts/silver/tests/test_commonwealth_mover_causes.py` (stubs): a month whose after-arm value moves only by a
sweep balance is `sweep_balance`; a month whose before-arm components err equally and oppositely is `offsetting`; a month neither rule
fits is `other:unexplained`; a `core` month never enters the 147 count.

### ACCEPTANCE

<criterion id="CB21u1-AC1" cell_refs="CB-u-1"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_mover_causes.py</invocation><expect>passed</expect></criterion>
`CB21u1-AC1` -- the three classes by rule, the unexplained fallback, and the core months kept apart.

<criterion id="CB21u1-AC2" cell_refs="CB-u-1"><invocation>python data/assets/scripts/silver/commonwealth_mover_causes.py --grades org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~41 --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~42</invocation><expect>sum_ok=True</expect></criterion>
`CB21u1-AC2` -- each of the 147 classed once, the counts summing to 147, the 16 reported apart.

<criterion id="CB21u1-AC3" cell_refs="CB-u-1" judgment="true"/>
`CB21u1-AC3` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: each class's traced month shows its named mechanism in the printed day values, and the rule, not the result, decided the class.

<expected_criteria>CB21u1-AC1,CB21u1-AC2,CB21u1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Large output under `.scratch/`, uncommitted.
- **Read-only.** No apply, no S3 write, no vendor call, no download of any kind, never bun. Read only the buckets the chain already
  reads; never `opal-data-bd`, `opal-data-49financial`, `opal-data-inf`, `opal-data-inflection` or `opal-data-demo`.
- **No fix in this item.** Name and trace the causes; change nothing in the chain.
- **Blank, never filled.** A value, return or month that cannot be worked out is null with its reason, never estimated.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-D2-W42-S<k>`, `"fabric": "dell2"`, `surfaced_at` the actual UTC time you file it; a NEW row, never an edit of an
  existing one), and do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_mover_causes.py
data/assets/scripts/silver/tests/test_commonwealth_mover_causes.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round21.md</decomp_doc> (round 21), cell `CB-u-1`.
<owned_cells>CB-u-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB21u1-AC1, CB21u1-AC2, CB21u1-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~42/ADVI_COTBKF.TO-CB-u-1.mover-causes.proof_of_spec.json`, validated
with `python .tools/proof-of-spec-check.py <instance> CB21u1-AC1,CB21u1-AC2,CB21u1-AC3` BEFORE the flip. Mechanical: CB21u1-AC1,
CB21u1-AC2; a judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the MOVER-CAUSES line, the class rule as written, counts per class (and for the 16), one traced month per class, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a local derivation run by hand.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity; BLIND: none needed.
comp-adversary: RUN -- the class decided by a rule stated before the counts; an unfit month stays unexplained, never forced; BLIND: a cause that spans both arms identically (it would not show as a mover at all).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-20 analysis `CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_20_20261008.md` @9129f4e33d (msg 1412), E1; row D2-S29.
