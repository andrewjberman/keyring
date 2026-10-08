# TO ADVI_COTBKF.TO-CB-v-2.mover-data-folder -- round 22 CB-v-2: the mover scripts name their data folder and refuse a list-version mismatch

<to_id>ADVI_COTBKF.TO-CB-v-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~44</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>22</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-v-2` (`decompositions/ADVI_COTBKF_DECOMP.round22.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-3's daily-return chain lives under `data/assets/scripts/silver/`. `commonwealth_sweep_regrade.py` re-runs it for two sweep-list
arms (`--before-list none|v1|v2`, `--after-list ...`) and writes day parquet under `--data-dir` (`<dir>/before`, `<dir>/after`;
default `<repo>/.scratch/advi_cotbkf/fwd3/`) plus `month_grades_before/after.parquet` beside its report (each grade row carries the
list version used). Two analysis scripts read those: `commonwealth_mover_classes.py --grades <dir> --out <dir>` and
`commonwealth_mover_causes.py --grades <dir> [--data-dir <dir>] --out <dir>`.

**Your item (the CTO's round-21 analysis, E2; row D2-S31).** On the trunk, `commonwealth_mover_causes.py` read day values from the
default data folder, which held round 20's v1 -> v2 arms instead of round 19's none -> v1, and classed all 147 movers
`other:unexplained` until the arms were rebuilt. Make both mover scripts self-describing:
1. each takes an explicit data folder (`--data-dir`, REQUIRED where the script reads day values; no silent default) and the arms'
   expected list versions (`--before-list`, `--after-list`, defaults `none` and `v1`, the round-19 arms);
2. before classing, each checks the list version recorded in the arms it reads (day parquet and/or persisted grades) against the
   expected ones and REFUSES with a non-zero exit and one line naming both versions when they differ -- never a silent fallback to
   `other:unexplained` for every month.
Do not change what either script computes when the arms are right.

Tests in `data/assets/scripts/silver/tests/test_commonwealth_mover_data_folder.py` (stubs): arms whose recorded version matches run;
arms recorded `v1`/`v2` against an expected `none`/`v1` are refused with a non-zero exit and the refusal line; a missing data folder
is refused.

### ACCEPTANCE

<criterion id="CB22v2-AC1" cell_refs="CB-v-2"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_mover_data_folder.py</invocation><expect>passed</expect></criterion>
`CB22v2-AC1` -- matching arms run; mismatched arms and a missing folder are refused loudly.

<expected_criteria>CB22v2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **Read-only.** No apply, no S3 write, no vendor call, no download of any kind, never bun.
- **Refusal clause.** If the criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-D2-W44-S<k>`, `"fabric": "dell2"`, `surfaced_at` the actual UTC time you file it; a NEW row, never an edit of an
  existing one), and do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_mover_classes.py
data/assets/scripts/silver/commonwealth_mover_causes.py
data/assets/scripts/silver/tests/test_commonwealth_mover_data_folder.py
data/assets/scripts/silver/tests/test_commonwealth_mover_classes.py
data/assets/scripts/silver/tests/test_commonwealth_mover_causes.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round22.md</decomp_doc> (round 22), cell `CB-v-2`.
<owned_cells>CB-v-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB22v2-AC1. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~44/ADVI_COTBKF.TO-CB-v-2.mover-data-folder.proof_of_spec.json`, validated
with `python .tools/proof-of-spec-check.py <instance> CB22v2-AC1` BEFORE the flip. Mechanical.
</proof_of_spec>

**REPORT:** the refusal line as printed, the test count, the existing mover tests' count, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a local derivation run by hand.
comp-iam: DECLARED-NOT-APPLICABLE no cloud read needed.
comp-adversary: RUN -- a version mismatch refuses loudly instead of classing every month unexplained; BLIND: arms built before list versions were recorded (they refuse, which is the safe side).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-21 analysis `CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_21_20261008.md` (msg 1449), E2; row D2-S31.
