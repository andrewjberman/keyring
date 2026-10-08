# TO ADVI_COTBKF.TO-CB-t-1.mover-classes -- round 20 CB-t-1: class the 163 MATCH -> DIFF months; persist month grades

<to_id>ADVI_COTBKF.TO-CB-t-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~41</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>20</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-t-1` (`decompositions/ADVI_COTBKF_DECOMP.round20.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-3: an analyst reads each Cottonwood account's return day by day, after fees, from 2013 to June 2026; strung together over a
month, the days give Commonwealth's reported monthly return, or the difference is shown with its reason; a day that cannot be worked
out is never filled in. The chain, all under `data/assets/scripts/silver/`: `commonwealth_daily_valuation.py`,
`commonwealth_daily_returns.py` + `commonwealth_flows.py`, `commonwealth_monthly_grade.py` (TOLERANCE_PCT 0.05). Round 19 added
`commonwealth_sweeps.py` (`SWEEP_LIST_VERSION` sweeps-v1-20261008: FDIC66606, FDIC66853; `CANDIDATES_REJECTED`) and the runner
`commonwealth_sweep_regrade.py`, which re-runs the chain without and with the sweep list and writes `sweep_regrade.md` to `--out`.
Parquet goes to `--data-dir` (default `<repo>/.scratch/advi_cotbkf/fwd3/`); the valuation reads the price stores from S3 read-only on
a cold cache (minutes). Round 19's real run, LAST line:
`SWEEP-REGRADE sweeps=2 rejected=517 double_drop_months=74 fixed=42 months_before=1685/1931/78977 months_after=2057/1522/79014 control_same=True`.
Its verdict moves include **MATCH -> DIFF: 163** (`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~40/sweep_regrade.md`,
the block "Verdict moves"). Nobody has looked at why those 163 moved.

**Your item (the CTO's round-19 analysis, E1).**
1. Make `commonwealth_sweep_regrade.py` PERSIST the month grades of both arms beside the report: `month_grades_before.parquet` and
   `month_grades_after.parquet` in `--out`, one row per (account, month) with at least the computed month return, Commonwealth's
   reported return, the verdict and the list version used. Add `--before-list` / `--after-list` options naming the arm's sweep list
   version (`none` = no list, as round 19's before arm; `v1` = sweeps-v1), defaults reproducing round 19 exactly.
2. A new script `data/assets/scripts/silver/commonwealth_mover_classes.py --grades <dir> --out <dir>`: reads the two persisted grade
   files, takes every month MATCH before and DIFF after, and classes each by its ACCOUNT's holdings on or before that month: `core`
   (holds 316067107), `other_mmf` (holds another CUSIP the round-19 `CANDIDATES_REJECTED` lists with reason MMF), `neither`. A month
   that is both `core` and `other_mmf` is `core`. Write `mover_classes.md` (counts per class; every month named with account, month,
   before and after return, reported return, class) and `mover_classes.parquet`. LAST line exactly:
   `MOVER-CLASSES movers=<n> core=<a> other_mmf=<b> neither=<c> sum_ok=<True|False>`.
Run both against the real data: the runner with `--out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~41`, then
the classifier with `--grades` and `--out` both that folder. Its `movers` must equal the runner's MATCH -> DIFF count.

Tests `data/assets/scripts/silver/tests/test_commonwealth_mover_classes.py` (stubs): a month MATCH -> DIFF of an account holding
316067107 is `core`; one holding only another MMF is `other_mmf`; one holding neither is `neither`; a month that did not move is not
classed; the persisted grade file has one row per (account, month).

### ACCEPTANCE

<criterion id="CB20t1-AC1" cell_refs="CB-t-1"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_mover_classes.py</invocation><expect>passed</expect></criterion>
`CB20t1-AC1` -- the three classes, the unmoved month, and the persisted grade file's grain.

<criterion id="CB20t1-AC2" cell_refs="CB-t-1"><invocation>python data/assets/scripts/silver/commonwealth_mover_classes.py --grades org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~41 --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~41</invocation><expect>sum_ok=True</expect></criterion>
`CB20t1-AC2` -- every MATCH -> DIFF month of the persisted grades classed once; the counts sum to the movers.

<expected_criteria>CB20t1-AC1,CB20t1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Large output under `.scratch/`, uncommitted;
  the two month-grade parquet files and `mover_classes.parquet` are committed in the deliverables folder.
- **Read-only.** No apply, no S3 write, no vendor call, no download of any kind, never bun. Read only the buckets the chain already
  reads; never `opal-data-bd`, `opal-data-49financial`, `opal-data-inf`, `opal-data-inflection` or `opal-data-demo`.
- **Blank, never filled.** A value, return or month that cannot be worked out is null with its reason, never estimated.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-D2-W41-S<k>`, `"fabric": "dell2"`, `surfaced_at` the actual UTC time you file it), and do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_sweep_regrade.py
data/assets/scripts/silver/commonwealth_mover_classes.py
data/assets/scripts/silver/tests/test_commonwealth_mover_classes.py
data/assets/scripts/silver/tests/test_commonwealth_sweeps.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round20.md</decomp_doc> (round 20), cell `CB-t-1`.
<owned_cells>CB-t-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB20t1-AC1, CB20t1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~41/ADVI_COTBKF.TO-CB-t-1.mover-classes.proof_of_spec.json`, validated
with `python .tools/proof-of-spec-check.py <instance> CB20t1-AC1,CB20t1-AC2` BEFORE the flip. Both mechanical.
</proof_of_spec>

**REPORT:** the runner's SWEEP-REGRADE line (must reproduce round 19's), the MOVER-CLASSES line, the counts per class, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a local derivation run by hand.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity; BLIND: none needed.
comp-adversary: RUN -- the movers taken from persisted grades, not re-derived from day values; the class by account holdings on or before the month; BLIND: a core position the account held under a CUSIP other than 316067107.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-19 analysis `CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_19_20261008.md` @c015b6de3d (msg 1355), E1; row D2-S29.
