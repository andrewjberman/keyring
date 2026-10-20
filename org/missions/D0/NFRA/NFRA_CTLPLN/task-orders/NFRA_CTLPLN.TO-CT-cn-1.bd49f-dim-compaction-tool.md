# TO NFRA_CTLPLN.TO-CT-cn-1.bd49f-dim-compaction-tool -- workstream OUTCOME round 41 (cell CT-cn-1): the one-time compaction tool for the 49F dim history, with a read-only plan mode that prints three equality proofs

<to_id>NFRA_CTLPLN.TO-CT-cn-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~154</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<status_reason>Complete, 2026-10-20, merged @40cecd5f66. Worker 0.9.0_WK_NFRA_CTLPLN~154 (head b85ce2e714): CTcn1-AC1 `6 passed`, CTcn1-AC2 `29 passed` (base 29); proof instance VALID rc=0; two OBSERVATION rows (W154-S1 the checker named in worker.md is absent from the sparse tree; W154-S2 apply also refuses when the prior object has no VersionId, which is the safe side). The issuer read the tool whole and ran `--mode plan --date 2026-10-19` on the REAL stored partition (read-only, writes nothing): `COMPACT-PLAN date=2026-10-19 rows_before=288194 rows_after=6669 merged=281525 accounts=5339 current_equal=True runs_equal=True`. Nothing written to S3 by the cell. The one run is CT-co-1 (TO-APPLY-36), STAGED until the GO.</status_reason>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>41</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-cn-1` (`decompositions/NFRA_CTLPLN_DECOMP.round30.md`, amendment 14) | **outcome_ref:** an inbound ask, no FWD (part 3 of the CTO's fix, `org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_BD49F_DIM_COMPACTION_CTO_HALF_20261020.md` @dee04e1b01; the COO half is `deliverables/2.0.0_SA_COO~C/NEVER_WIDEN_BD49F_DIM_COMPACTION_COO_HALF_20261020.md`) |
**depends_on:** none (`CT-cl-1` merged @82484219d4b; its apply leg is live)

---

## WORKER FACE

### THE CELL

The 49F dim `s3://opal-data-assets/blackdiamond/49f/silver/dim_advisor_fee_role/date=<D>/data.parquet` is an SCD2 history (parquet; columns include `account_id`, `effective_from`, `effective_to`, `is_current`, `absent_from_feed_since`, the change tuple `SCD2_TUPLE` and `*_as_of` stamps; schema `DIM_SCHEMA` in `data/assets/scripts/silver/bd49f_dim_conversion.py`, which also holds `MONOLITH`, `PFX`, `DIM_TABLE`). A defect, now fixed, reopened every account every day, so the stored history holds about 288k rows where about 5.4k plus the real changes are meaningful: runs of CONSECUTIVE periods of one account whose change tuple is identical.

Build ONE new tool, `data/assets/scripts/silver/bd49f_dim_compact.py` (stdlib + pandas + pyarrow + boto3 as the converter already uses; ASCII only; it imports the converter for `SCD2_TUPLE`, `DIM_SCHEMA`, `MONOLITH`, `PFX`, `DIM_TABLE`, never copies them). It is NOT vendored into any Lambda and you do not touch the converter.

THE RULE (the CTO's, binding): within each `account_id`, ordered by `effective_from`, consecutive periods whose `SCD2_TUPLE` is identical AFTER casting each tuple column to its `DIM_SCHEMA` type (float columns to float64, bool to boolean, everything else to object, nulls as `"<NA>"`, then stringified: the same cast `scd2_fold`'s comparison uses after `CT-cl-1`) merge into ONE row. The merged row keeps the EARLIEST `effective_from` of the run, and every column from the EARLIEST row of the run, EXCEPT the three columns that describe the CURRENT state, which come from the LAST row of the run: `effective_to`, `is_current`, `absent_from_feed_since` (so the open row of each account stays open, with its tuple unchanged, and a carried-absent flag is not erased). Periods separated by a different tuple stay separate (a real change is never merged across). Every other row is carried unchanged. Output rows sorted by (`account_id`, `effective_from`).

BUILD:
1. `compact(dim)` -> the merged DataFrame (pure; same columns and dtypes as the input; refuses with a named exception if an account has two open rows).
2. `proofs(before, after)` -> a dict with three checks: (a) CURRENT ROWS: the set of rows where `is_current` is true, compared on `account_id`, the full tuple (cast form), `effective_to` and `absent_from_feed_since`, equal before and after; (b) TUPLE RUNS: for every account, the ordered list of distinct consecutive tuple runs (cast form) equal before and after; (c) ROW COUNT: `rows_before`, `rows_after`, `merged = rows_before - rows_after`, `accounts`, printed with the denominator.
3. A CLI: `python data/assets/scripts/silver/bd49f_dim_compact.py --date <D> --mode plan` reads the object at `date=<D>` (S3 `get_object`, read-only), runs 1-2, writes NOTHING, and prints one last line `COMPACT-PLAN date=<D> rows_before=<n> rows_after=<m> merged=<k> accounts=<a> current_equal=<True|False> runs_equal=<True|False>`. `--mode apply --confirm-key <the full key>` recomputes the plan, REFUSES (nonzero exit, nothing written) unless `current_equal` and `runs_equal` are both True, the `--confirm-key` equals the computed key, and `merged > 0` (when `merged` is 0 it writes nothing and prints `COMPACT-APPLY date=<D> merged=0 wrote=False`); otherwise it records the prior object's `VersionId` (from `head_object`), does ONE `put_object` of the compacted parquet to the SAME key, reads it back, re-runs the proofs on the read-back, and prints `COMPACT-APPLY date=<D> prior_version=<id> new_version=<id> rows_before=<n> rows_after=<m> readback_equal=<True|False> wrote=True`. `--date` must be a `YYYY-MM-DD` string; the tool never lists, deletes or writes any other key.
4. TESTS in a NEW file `data/assets/scripts/silver/tests/test_bd49f_dim_compact.py` (pytest, in-memory frames, a small fake S3 client class with `get_object`, `head_object`, `put_object` for the apply cases; no network). EXACTLY SIX tests, named: `test_identical_consecutive_periods_merge_earliest_from_latest_to`; `test_real_change_between_runs_stays_separate`; `test_float_zero_and_int_zero_tuple_are_identical_after_cast`; `test_proofs_catch_a_merge_across_a_real_change` (the difference control: a planted wrong `compact` that merges across a different tuple makes `runs_equal` False); `test_apply_refuses_on_failed_proof_or_wrong_confirm_key_and_writes_nothing`; `test_apply_with_zero_merged_writes_nothing`. A seventh test is not allowed.
5. Run `python -m pytest data/assets/scripts/silver/tests/test_bd49f_dim_compact.py -q` and `python -m pytest data/assets/scripts/silver/tests/test_bd49f_dim_conversion.py -q` under `timeout 120` each; the second must stay `29 passed`.

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~154/`. THIS IS A WORLD-ADJACENT CELL (the tool can write a served object): you run the tool in NEITHER mode against real S3, you run NO `aws`, NO `terraform`, NO deploy; the read-only plan on the real partition and the one write are the issuer's and a CloudOps seat's. You do not touch the converter, `infra/`, or any existing test. If an acceptance cannot be met as written, that is a surprise row, not a weaker tool.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTcn1-AC1" cell_refs="CT-cn-1"><invocation>python -m pytest data/assets/scripts/silver/tests/test_bd49f_dim_compact.py -q</invocation><expect>6 passed</expect></criterion>
`CTcn1-AC1` -- the six tests pass: identical neighbours merge (earliest from, latest to, current-state columns from the last row), a real change stays separate, float 0.0 and int 0 are identical after the cast, the proofs catch a merge across a real change (the difference control), apply refuses on a failed proof or a wrong confirm key and writes nothing, apply with zero merged writes nothing (base: the file is absent, so this reads FAIL at the base as expected). Report the whole last line.

<criterion id="CTcn1-AC2" cell_refs="CT-cn-1"><invocation>python -m pytest data/assets/scripts/silver/tests/test_bd49f_dim_conversion.py -q</invocation><expect>29 passed</expect></criterion>
`CTcn1-AC2` -- the converter's tests are untouched and stay green (base: `29 passed`, a control); report the whole last line.
</proof_of_spec>

<expected_criteria>CTcn1-AC1,CTcn1-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~154/NFRA_CTLPLN.TO-CT-cn-1.bd49f-dim-compaction-tool.proof_of_spec.json`, validate it with the checker `.claude/agents/worker.md` names. Do NOT flip this order's status: the order file is outside your `<paths>`; the issuer flips it after the merge. Your final report states the commit hashes and the whole last line of each run.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round30.md</decomp_doc>
<owned_cells>CT-cn-1</owned_cells>
</decomp_ref>

<paths>
data/assets/scripts/silver/bd49f_dim_compact.py
data/assets/scripts/silver/tests/test_bd49f_dim_compact.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE (never travels to the worker)

Issued 2026-10-20 by `2.0.0_SA_COO~C`. The COO half of the never-widen pair names the same blast radius as the CTO half (one key, `date=2026-10-20`, after the 2026-10-21 07:05Z fire). Two criteria (the build; the neighbour control). The seam probe on the real neighbour is the issuer's at the drain: `--mode plan --date 2026-10-19` on the real stored partition, read-only. Interpretation recorded for the CTO: the CTO half says every other field comes from the earliest row of the run; the issuer reads three current-state columns (`effective_to`, `is_current`, `absent_from_feed_since`) as taken from the last row so the open row stays open and a carried-absent flag survives (the CTO half's own sentence "the open row of each account stays open, with its tuple unchanged").

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is read or changed by this cell.
comp-iam: DECLARED-NOT-APPLICABLE no IAM or policy change; the tool's apply mode needs `s3:PutObject` on the one key, read by the CloudOps seat in `CT-co-1` before the run.
comp-adversary: RUN -- a merge across a real change (the difference-control test and the tuple-runs proof); a cast that hides a real change or splits identical values (float 0.0 versus int 0 test); a write to the wrong partition (the confirm-key refusal); a write after a failed proof (the refusal test); a write when nothing merges (the zero-merged test); the open row closed or the absent flag erased (the current-rows proof compares both); a read from the wrong key (plan mode prints the key it read); cost (none).
risk: WORLD by the tool's nature (it can write a served object); the cell writes only code and tests and runs nothing against S3.
</preflight>
